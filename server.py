"""
Contra Amenaza - Server
Plataforma de aprendizaje en Ciberseguridad
"""
import os
import hashlib
import secrets
from functools import wraps
from flask import Flask, request, jsonify, send_from_directory, session, g

from database import init_db, get_db
from courses import COURSES, get_all_courses_summary, get_course
from simulator import SCENARIOS, get_all_scenarios_summary, get_scenario, get_scenario_safe

app = Flask(__name__, static_folder='public', static_url_path='')
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))

init_db()


# ── DB connection lifecycle via Flask g ──────────────────────────────

def db():
    """Get DB connection for current request, reusing if already open."""
    if 'db' not in g:
        g.db = get_db()
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Always close DB connection at end of request."""
    conn = g.pop('db', None)
    if conn is not None:
        conn.close()


# ── Helpers ──────────────────────────────────────────────────────────

def hash_password(password):
    salt = secrets.token_hex(16)
    h = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{h}"


def verify_password(stored, password):
    salt, h = stored.split(':')
    return hashlib.sha256((salt + password).encode()).hexdigest() == h


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"error": "No autenticado"}), 401
        return f(*args, **kwargs)
    return decorated


# ── Static files ─────────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')


@app.route('/<path:path>')
def static_files(path):
    file_path = os.path.join('public', path)
    if os.path.isfile(file_path):
        return send_from_directory('public', path)
    return send_from_directory('public', 'index.html')


# ── Auth API ─────────────────────────────────────────────────────────

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '')
    display_name = data.get('displayName', '').strip()

    if not username or not password or not display_name:
        return jsonify({"error": "Todos los campos son requeridos"}), 400
    if len(username) < 3:
        return jsonify({"error": "El usuario debe tener al menos 3 caracteres"}), 400
    if len(password) < 4:
        return jsonify({"error": "La contrasena debe tener al menos 4 caracteres"}), 400

    existing = db().execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
    if existing:
        return jsonify({"error": "El usuario ya existe"}), 409

    pw_hash = hash_password(password)
    cursor = db().execute(
        "INSERT INTO users (username, password_hash, display_name) VALUES (?, ?, ?)",
        (username, pw_hash, display_name)
    )
    db().commit()
    user_id = cursor.lastrowid

    session['user_id'] = user_id
    session['username'] = username
    session['display_name'] = display_name

    return jsonify({"id": user_id, "username": username, "displayName": display_name}), 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '')

    user = db().execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if not user or not verify_password(user['password_hash'], password):
        return jsonify({"error": "Usuario o contrasena incorrectos"}), 401

    session['user_id'] = user['id']
    session['username'] = user['username']
    session['display_name'] = user['display_name']

    return jsonify({
        "id": user['id'],
        "username": user['username'],
        "displayName": user['display_name']
    })


@app.route('/api/auth/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"ok": True})


@app.route('/api/auth/me')
def me():
    if 'user_id' not in session:
        return jsonify(None)
    return jsonify({
        "id": session['user_id'],
        "username": session['username'],
        "displayName": session['display_name']
    })


# ── Courses API ──────────────────────────────────────────────────────

@app.route('/api/courses')
def list_courses():
    return jsonify(get_all_courses_summary())


@app.route('/api/courses/<course_id>')
def get_course_detail(course_id):
    course = get_course(course_id)
    if not course:
        return jsonify({"error": "Curso no encontrado"}), 404

    result = {
        "id": course["id"],
        "title": course["title"],
        "description": course["description"],
        "icon": course["icon"],
        "color": course["color"],
        "modules": []
    }
    for mod in course["modules"]:
        module_data = {
            "id": mod["id"],
            "title": mod["title"],
            "lessons": [{"id": l["id"], "title": l["title"]} for l in mod["lessons"]]
        }
        result["modules"].append(module_data)
    return jsonify(result)


@app.route('/api/courses/<course_id>/modules/<module_id>/lessons/<lesson_id>')
def get_lesson(course_id, module_id, lesson_id):
    course = get_course(course_id)
    if not course:
        return jsonify({"error": "Curso no encontrado"}), 404

    for mod in course["modules"]:
        if mod["id"] == module_id:
            for lesson in mod["lessons"]:
                if lesson["id"] == lesson_id:
                    exercises = []
                    for ex in lesson.get("exercises", []):
                        exercise_data = {
                            "id": ex["id"],
                            "type": ex["type"],
                            "question": ex["question"]
                        }
                        if "options" in ex:
                            exercise_data["options"] = ex["options"]
                        exercises.append(exercise_data)

                    return jsonify({
                        "id": lesson["id"],
                        "title": lesson["title"],
                        "theory": lesson["theory"],
                        "exercises": exercises,
                        "courseId": course_id,
                        "moduleId": module_id
                    })

    return jsonify({"error": "Leccion no encontrada"}), 404


# ── Exercise submission ──────────────────────────────────────────────

@app.route('/api/exercises/check', methods=['POST'])
@login_required
def check_exercise():
    data = request.get_json()
    course_id = data.get('courseId')
    module_id = data.get('moduleId')
    lesson_id = data.get('lessonId')
    exercise_id = data.get('exerciseId')
    user_answer = data.get('answer')

    course = get_course(course_id)
    if not course:
        return jsonify({"error": "Curso no encontrado"}), 404

    exercise = None
    for mod in course["modules"]:
        if mod["id"] == module_id:
            for lesson in mod["lessons"]:
                if lesson["id"] == lesson_id:
                    for ex in lesson.get("exercises", []):
                        if ex["id"] == exercise_id:
                            exercise = ex
                            break

    if not exercise:
        return jsonify({"error": "Ejercicio no encontrado"}), 404

    is_correct = False
    if exercise["type"] == "multiple_choice":
        is_correct = int(user_answer) == exercise["correct"]
    elif exercise["type"] in ("fill_blank", "code_output"):
        is_correct = user_answer.strip().lower() == exercise["correct"].strip().lower()

    db().execute(
        """INSERT INTO exercise_submissions (user_id, course_id, module_id, lesson_id, exercise_id, user_answer, is_correct)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (session['user_id'], course_id, module_id, lesson_id, exercise_id, str(user_answer), int(is_correct))
    )
    db().commit()

    return jsonify({
        "correct": is_correct,
        "explanation": exercise.get("explanation", "")
    })


# ── Progress API ─────────────────────────────────────────────────────

@app.route('/api/progress', methods=['GET'])
@login_required
def get_progress():
    rows = db().execute(
        "SELECT course_id, module_id, lesson_id, completed, score FROM progress WHERE user_id = ?",
        (session['user_id'],)
    ).fetchall()

    submissions = db().execute(
        """SELECT course_id, module_id, lesson_id, exercise_id, is_correct
           FROM exercise_submissions WHERE user_id = ?
           ORDER BY submitted_at DESC""",
        (session['user_id'],)
    ).fetchall()

    progress = {}
    for row in rows:
        key = f"{row['course_id']}.{row['module_id']}.{row['lesson_id']}"
        progress[key] = {"completed": bool(row['completed']), "score": row['score']}

    exercise_progress = {}
    for sub in submissions:
        key = f"{sub['course_id']}.{sub['module_id']}.{sub['lesson_id']}.{sub['exercise_id']}"
        if key not in exercise_progress:
            exercise_progress[key] = bool(sub['is_correct'])

    return jsonify({"lessons": progress, "exercises": exercise_progress})


@app.route('/api/progress/complete', methods=['POST'])
@login_required
def complete_lesson():
    data = request.get_json()
    course_id = data.get('courseId')
    module_id = data.get('moduleId')
    lesson_id = data.get('lessonId')
    score = data.get('score', 0)

    db().execute(
        """INSERT INTO progress (user_id, course_id, module_id, lesson_id, completed, score, completed_at)
           VALUES (?, ?, ?, ?, 1, ?, CURRENT_TIMESTAMP)
           ON CONFLICT(user_id, course_id, module_id, lesson_id)
           DO UPDATE SET completed = 1, score = MAX(score, ?), completed_at = CURRENT_TIMESTAMP""",
        (session['user_id'], course_id, module_id, lesson_id, score, score)
    )
    db().commit()

    return jsonify({"ok": True})


# ── Notes API ────────────────────────────────────────────────────────

@app.route('/api/notes', methods=['GET'])
@login_required
def get_notes():
    course_id = request.args.get('courseId')
    module_id = request.args.get('moduleId')
    lesson_id = request.args.get('lessonId')

    note = db().execute(
        "SELECT content FROM notes WHERE user_id = ? AND course_id = ? AND module_id = ? AND lesson_id = ?",
        (session['user_id'], course_id, module_id, lesson_id)
    ).fetchone()

    return jsonify({"content": note['content'] if note else ""})


@app.route('/api/notes', methods=['POST'])
@login_required
def save_note():
    data = request.get_json()
    db().execute(
        """INSERT INTO notes (user_id, course_id, module_id, lesson_id, content, updated_at)
           VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
           ON CONFLICT(user_id, course_id, module_id, lesson_id)
           DO UPDATE SET content = ?, updated_at = CURRENT_TIMESTAMP""",
        (session['user_id'], data['courseId'], data['moduleId'], data['lessonId'],
         data['content'], data['content'])
    )
    db().commit()
    return jsonify({"ok": True})


# ── Stats API ────────────────────────────────────────────────────────

@app.route('/api/stats')
@login_required
def get_stats():
    completed = db().execute(
        "SELECT COUNT(*) as c FROM progress WHERE user_id = ? AND completed = 1",
        (session['user_id'],)
    ).fetchone()['c']

    correct = db().execute(
        "SELECT COUNT(*) as c FROM exercise_submissions WHERE user_id = ? AND is_correct = 1",
        (session['user_id'],)
    ).fetchone()['c']

    total_submissions = db().execute(
        "SELECT COUNT(*) as c FROM exercise_submissions WHERE user_id = ?",
        (session['user_id'],)
    ).fetchone()['c']

    course_stats = {}
    for cid in COURSES:
        course_completed = db().execute(
            "SELECT COUNT(*) as c FROM progress WHERE user_id = ? AND course_id = ? AND completed = 1",
            (session['user_id'], cid)
        ).fetchone()['c']
        course_stats[cid] = {"completedLessons": course_completed}

    total_lessons = sum(
        len(l["lessons"]) for c in COURSES.values() for l in c["modules"]
    )

    return jsonify({
        "completedLessons": completed,
        "totalLessons": total_lessons,
        "correctExercises": correct,
        "totalSubmissions": total_submissions,
        "courseStats": course_stats
    })


# ── Simulator API ────────────────────────────────────────────────────

@app.route('/api/simulator/scenarios')
def list_scenarios():
    return jsonify(get_all_scenarios_summary())


@app.route('/api/simulator/scenarios/<scenario_id>')
def get_scenario_detail(scenario_id):
    scenario = get_scenario_safe(scenario_id)
    if not scenario:
        return jsonify({"error": "Escenario no encontrado"}), 404
    return jsonify(scenario)


@app.route('/api/simulator/submit', methods=['POST'])
@login_required
def submit_simulator_task():
    data = request.get_json()
    scenario_id = data.get('scenarioId')
    task_id = data.get('taskId')
    user_answer = str(data.get('answer', '')).strip()

    scenario = get_scenario(scenario_id)
    if not scenario:
        return jsonify({"error": "Escenario no encontrado"}), 404

    task = next((t for t in scenario['tasks'] if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    # Check if already answered correctly
    existing = db().execute(
        "SELECT is_correct FROM simulator_attempts WHERE user_id=? AND scenario_id=? AND task_id=?",
        (session['user_id'], scenario_id, task_id)
    ).fetchone()
    if existing and existing['is_correct']:
        return jsonify({"correct": True, "explanation": task.get("explanation", ""), "already_done": True})

    # Evaluate answer
    is_correct = False
    if task['type'] == 'multiple_choice':
        try:
            is_correct = int(user_answer) == task['correct']
        except (ValueError, TypeError):
            is_correct = False
    else:
        correct_val = str(task['correct']).strip().lower()
        is_correct = user_answer.lower() == correct_val

    points_earned = task['points'] if is_correct else 0

    db().execute(
        """INSERT INTO simulator_attempts (user_id, scenario_id, task_id, user_answer, is_correct, points_earned)
           VALUES (?, ?, ?, ?, ?, ?)
           ON CONFLICT(user_id, scenario_id, task_id)
           DO UPDATE SET user_answer=?, is_correct=MAX(is_correct,?), points_earned=MAX(points_earned,?)""",
        (session['user_id'], scenario_id, task_id, user_answer, int(is_correct), points_earned,
         user_answer, int(is_correct), points_earned)
    )
    db().commit()

    # Check if scenario is now complete
    total_tasks = len(scenario['tasks'])
    completed_tasks = db().execute(
        "SELECT COUNT(*) as c FROM simulator_attempts WHERE user_id=? AND scenario_id=? AND is_correct=1",
        (session['user_id'], scenario_id)
    ).fetchone()['c']

    if completed_tasks == total_tasks:
        total_pts = db().execute(
            "SELECT SUM(points_earned) as s FROM simulator_attempts WHERE user_id=? AND scenario_id=?",
            (session['user_id'], scenario_id)
        ).fetchone()['s'] or 0
        max_pts = sum(t['points'] for t in scenario['tasks'])
        db().execute(
            """INSERT INTO simulator_completions (user_id, scenario_id, total_points, max_points)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(user_id, scenario_id)
               DO UPDATE SET total_points=MAX(total_points,?), completed_at=CURRENT_TIMESTAMP""",
            (session['user_id'], scenario_id, total_pts, max_pts, total_pts)
        )
        db().commit()

    return jsonify({
        "correct": is_correct,
        "explanation": task.get("explanation", ""),
        "points_earned": points_earned,
        "hint": task.get("hint", "") if not is_correct else None
    })


@app.route('/api/simulator/hint', methods=['POST'])
@login_required
def get_simulator_hint():
    data = request.get_json()
    scenario_id = data.get('scenarioId')
    task_id = data.get('taskId')
    scenario = get_scenario(scenario_id)
    if not scenario:
        return jsonify({"error": "Escenario no encontrado"}), 404
    task = next((t for t in scenario['tasks'] if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify({"hint": task.get("hint", "No hay pista disponible para esta tarea.")})


@app.route('/api/simulator/progress')
@login_required
def get_simulator_progress():
    attempts = db().execute(
        "SELECT scenario_id, task_id, is_correct, points_earned FROM simulator_attempts WHERE user_id=?",
        (session['user_id'],)
    ).fetchall()

    completions = db().execute(
        "SELECT scenario_id, total_points, max_points FROM simulator_completions WHERE user_id=?",
        (session['user_id'],)
    ).fetchall()

    progress = {}
    for a in attempts:
        sid = a['scenario_id']
        if sid not in progress:
            progress[sid] = {"tasks": {}, "completed": False, "total_points": 0}
        progress[sid]["tasks"][a['task_id']] = {
            "correct": bool(a['is_correct']),
            "points": a['points_earned']
        }

    completed_ids = set()
    for c in completions:
        completed_ids.add(c['scenario_id'])
        if c['scenario_id'] in progress:
            progress[c['scenario_id']]["completed"] = True
            progress[c['scenario_id']]["total_points"] = c['total_points']
            progress[c['scenario_id']]["max_points"] = c['max_points']

    total_points = db().execute(
        "SELECT SUM(points_earned) as s FROM simulator_attempts WHERE user_id=?",
        (session['user_id'],)
    ).fetchone()['s'] or 0

    return jsonify({
        "scenarios": progress,
        "completedScenarios": len(completed_ids),
        "totalScenarios": len(SCENARIOS),
        "totalPoints": total_points
    })


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    print("\n" + "=" * 55)
    print("  Contra Amenaza")
    print("  Plataforma de Aprendizaje en Ciberseguridad")
    print("=" * 55)
    print("  Servidor: http://localhost:5000")
    print("  Cursos:   Ciberseguridad | Redes | Linux | OSINT | Python")
    print("=" * 55 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
