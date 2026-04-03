import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'db', 'cyberlearn.db')


def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db()
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            display_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            course_id TEXT NOT NULL,
            module_id TEXT NOT NULL,
            lesson_id TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            score INTEGER DEFAULT 0,
            completed_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, course_id, module_id, lesson_id)
        );

        CREATE TABLE IF NOT EXISTS exercise_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            course_id TEXT NOT NULL,
            module_id TEXT NOT NULL,
            lesson_id TEXT NOT NULL,
            exercise_id TEXT NOT NULL,
            user_answer TEXT,
            is_correct INTEGER DEFAULT 0,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            course_id TEXT NOT NULL,
            module_id TEXT NOT NULL,
            lesson_id TEXT NOT NULL,
            content TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, course_id, module_id, lesson_id)
        );

        CREATE TABLE IF NOT EXISTS simulator_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            scenario_id TEXT NOT NULL,
            task_id TEXT NOT NULL,
            user_answer TEXT,
            is_correct INTEGER DEFAULT 0,
            points_earned INTEGER DEFAULT 0,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, scenario_id, task_id)
        );

        CREATE TABLE IF NOT EXISTS simulator_completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            scenario_id TEXT NOT NULL,
            total_points INTEGER DEFAULT 0,
            max_points INTEGER DEFAULT 0,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, scenario_id)
        );
    ''')
    conn.commit()
    conn.close()
