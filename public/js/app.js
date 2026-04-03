/* ── Contra Amenaza - SPA ── */

const App = {
    user: null,
    progress: { lessons: {}, exercises: {} },
    simProgress: { scenarios: {}, completedScenarios: 0, totalPoints: 0 },
    courses: [],
    currentRoute: '',

    // ── Icons ──
    icons: {
        code: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>`,
        shield: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
        network: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="5" r="3"/><circle cx="4" cy="19" r="3"/><circle cx="20" cy="19" r="3"/><line x1="12" y1="8" x2="4" y2="16"/><line x1="12" y1="8" x2="20" y2="16"/></svg>`,
        terminal: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>`,
        search: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`,
        check: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>`,
        chevron: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>`,
        back: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>`,
        book: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>`,
        trophy: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 22V8a6 6 0 0 1 12 0v14"/></svg>`,
        note: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`,
        target: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>`,
        alert: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>`,
        bug: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 2l1.88 1.88"/><path d="M14.12 3.88 16 2"/><path d="M9 7.13v-1a3.003 3.003 0 1 1 6 0v1"/><path d="M12 20c-3.3 0-6-2.7-6-6v-3a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v3c0 3.3-2.7 6-6 6z"/><path d="M12 20v-9"/><path d="M6.53 9C4.6 8.8 3 7.1 3 5"/><path d="M6 13H2"/><path d="M3 21c0-2.1 1.7-3.9 4-4"/><path d="M17.47 9c1.93-.2 3.53-1.9 3.53-4"/><path d="M18 13h4"/><path d="M21 21c0-2.1-1.7-3.9-4-4"/></svg>`,
        hint: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>`,
        star: `<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>`,
    },

    // ── Init ──
    async init() {
        await this.checkAuth();
        window.addEventListener('hashchange', () => this.route());
        this.route();
    },

    // ── API helpers ──
    async api(url, opts = {}) {
        const res = await fetch(url, {
            headers: { 'Content-Type': 'application/json' },
            ...opts,
            body: opts.body ? JSON.stringify(opts.body) : undefined,
        });
        const data = await res.json();
        if (!res.ok) throw { status: res.status, ...data };
        return data;
    },

    async checkAuth() {
        try {
            const user = await this.api('/api/auth/me');
            this.user = user;
            if (user) {
                try {
                    await this.loadProgress();
                    await this.loadSimProgress();
                } catch (e) {
                    this.user = null;
                    await fetch('/api/auth/logout', { method: 'POST' });
                }
            }
        } catch (e) { this.user = null; }
    },

    async loadProgress() {
        if (!this.user) return;
        this.progress = await this.api('/api/progress');
    },

    async loadSimProgress() {
        if (!this.user) return;
        try { this.simProgress = await this.api('/api/simulator/progress'); } catch (e) {}
    },

    async loadCourses() {
        if (this.courses.length) return;
        this.courses = await this.api('/api/courses');
    },

    // ── Router ──
    route() {
        const hash = location.hash.slice(1) || '/';
        this.currentRoute = hash;

        if (!this.user && hash !== '/auth') { location.hash = '#/auth'; return; }
        if (this.user && hash === '/auth') { location.hash = '#/'; return; }

        const parts = hash.split('/').filter(Boolean);

        if (parts[0] === 'auth') return this.renderAuth();
        if (parts[0] === 'simulator' && parts.length === 1) return this.renderSimulator();
        if (parts[0] === 'simulator' && parts.length === 2) return this.renderScenario(parts[1]);
        if (parts[0] === 'course' && parts.length === 2) return this.renderCourse(parts[1]);
        if (parts[0] === 'lesson' && parts.length === 4) return this.renderLesson(parts[1], parts[2], parts[3]);
        return this.renderDashboard();
    },

    $app: () => document.getElementById('app'),
    render(html) { this.$app().innerHTML = html; },

    // ── Markdown-lite parser ──
    parseTheory(text) {
        let html = text
            .replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) =>
                `<pre><code class="lang-${lang}">${this.escapeHtml(code.trim())}</code></pre>`)
            .replace(/`([^`]+)`/g, '<code>$1</code>')
            .replace(/^### (.+)$/gm, '<h3>$1</h3>')
            .replace(/^## (.+)$/gm, '<h2>$1</h2>')
            .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
            .replace(/^\|(.+)\|$/gm, (match) => {
                const cells = match.split('|').filter(c => c.trim());
                return `<tr>${cells.map(c => {
                    const content = c.trim();
                    if (/^[\s-:]+$/.test(content)) return null;
                    return `<td>${content}</td>`;
                }).filter(Boolean).join('')}</tr>`;
            })
            .replace(/^- (.+)$/gm, '<li>$1</li>')
            .replace(/^(\d+)\. (.+)$/gm, '<li>$2</li>')
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>');

        html = html.replace(/((?:<tr>.*?<\/tr>\s*)+)/g, (match) => {
            const rows = match.match(/<tr>.*?<\/tr>/g);
            if (!rows || rows.length < 2) return match;
            let tableHtml = '<table><thead>' + rows[0].replace(/<td>/g, '<th>').replace(/<\/td>/g, '</th>') + '</thead>';
            const startData = rows[1] && rows[1].replace(/<\/?t[dr]>/g, '').replace(/[\s-:]/g, '').length === 0 ? 2 : 1;
            tableHtml += '<tbody>' + rows.slice(startData).join('') + '</tbody></table>';
            return tableHtml;
        });

        html = html.replace(/((?:<li>.*?<\/li>\s*)+)/g, '<ul>$1</ul>');
        return `<div class="theory-content"><p>${html}</p></div>`;
    },

    escapeHtml(str) {
        return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    },

    parseExerciseQuestion(text) {
        return text
            .replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) =>
                `<pre><code>${this.escapeHtml(code.trim())}</code></pre>`)
            .replace(/`([^`]+)`/g, '<code>$1</code>')
            .replace(/\n/g, '<br>');
    },

    // ── Navbar ──
    navbar(activeSection = '') {
        if (!this.user) return '';
        const initials = this.user.displayName.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2);
        return `
        <nav class="navbar">
            <a class="nav-logo" href="#/" onclick="App.goHome()">
                <div class="logo-icon">CA</div>
                <span>Contra Amenaza</span>
            </a>
            <div class="nav-links">
                <a href="#/" class="${activeSection === 'home' ? 'active' : ''}">Cursos</a>
                <a href="#/simulator" class="${activeSection === 'simulator' ? 'active' : ''}">
                    ${this.icons.target} Simulador
                </a>
                <div class="nav-user">
                    <div class="avatar">${initials}</div>
                    <span class="name">${this.user.displayName}</span>
                </div>
                <button onclick="App.logout()">Salir</button>
            </div>
        </nav>`;
    },

    goHome() { location.hash = '#/'; },

    // ── Auth page ──
    renderAuth() {
        this.render(`
        <div class="auth-page">
            <div class="auth-card fade-in">
                <h1>Contra Amenaza</h1>
                <p class="subtitle">Tu plataforma de aprendizaje en ciberseguridad</p>
                <div class="auth-tabs">
                    <button class="auth-tab active" onclick="App.switchAuthTab('login')">Iniciar Sesion</button>
                    <button class="auth-tab" onclick="App.switchAuthTab('register')">Registrarse</button>
                </div>
                <div id="auth-error"></div>
                <form id="auth-form" onsubmit="App.handleAuth(event)">
                    <div id="register-fields" style="display:none">
                        <div class="form-group">
                            <label>Nombre completo</label>
                            <input type="text" id="auth-name" placeholder="Tu nombre">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Usuario</label>
                        <input type="text" id="auth-user" placeholder="Tu usuario" required>
                    </div>
                    <div class="form-group">
                        <label>Contrasena</label>
                        <input type="password" id="auth-pass" placeholder="Tu contrasena" required>
                    </div>
                    <button type="submit" class="btn btn-primary" id="auth-submit">Iniciar Sesion</button>
                </form>
            </div>
        </div>`);
        this._authMode = 'login';
    },

    switchAuthTab(mode) {
        this._authMode = mode;
        document.querySelectorAll('.auth-tab').forEach((t, i) => {
            t.classList.toggle('active', (i === 0 && mode === 'login') || (i === 1 && mode === 'register'));
        });
        document.getElementById('register-fields').style.display = mode === 'register' ? 'block' : 'none';
        document.getElementById('auth-submit').textContent = mode === 'login' ? 'Iniciar Sesion' : 'Crear Cuenta';
        document.getElementById('auth-error').innerHTML = '';
    },

    async handleAuth(e) {
        e.preventDefault();
        const username = document.getElementById('auth-user').value;
        const password = document.getElementById('auth-pass').value;
        const errEl = document.getElementById('auth-error');
        try {
            if (this._authMode === 'register') {
                const displayName = document.getElementById('auth-name').value;
                if (!displayName) { errEl.innerHTML = '<div class="alert alert-error">Ingresa tu nombre</div>'; return; }
                this.user = await this.api('/api/auth/register', { method: 'POST', body: { username, password, displayName } });
            } else {
                this.user = await this.api('/api/auth/login', { method: 'POST', body: { username, password } });
            }
            await this.loadProgress();
            await this.loadSimProgress();
            location.hash = '#/';
        } catch (err) {
            errEl.innerHTML = `<div class="alert alert-error">${err.error || 'Error de conexion'}</div>`;
        }
    },

    async logout() {
        await this.api('/api/auth/logout', { method: 'POST' });
        this.user = null;
        this.progress = { lessons: {}, exercises: {} };
        this.simProgress = { scenarios: {}, completedScenarios: 0, totalPoints: 0 };
        this.courses = [];
        location.hash = '#/auth';
    },

    // ── Dashboard ──
    async renderDashboard() {
        await this.loadCourses();
        await this.loadProgress();
        await this.loadSimProgress();

        let stats = { completedLessons: 0, totalLessons: 0, correctExercises: 0, totalSubmissions: 0, courseStats: {} };
        try { stats = await this.api('/api/stats'); } catch (e) {}

        const pct = stats.totalLessons > 0 ? Math.round((stats.completedLessons / stats.totalLessons) * 100) : 0;
        const exPct = stats.totalSubmissions > 0 ? Math.round((stats.correctExercises / stats.totalSubmissions) * 100) : 0;
        const sp = this.simProgress;

        const courseCards = this.courses.map((c, i) => {
            const cs = stats.courseStats[c.id] || { completedLessons: 0 };
            const coursePct = c.totalLessons > 0 ? Math.round((cs.completedLessons / c.totalLessons) * 100) : 0;
            const iconSvg = this.icons[c.icon] || this.icons.code;
            return `
            <div class="course-card fade-in" style="--card-color:${c.color}; animation-delay:${i * 0.06}s"
                 onclick="location.hash='#/course/${c.id}'">
                <div class="course-icon" style="background:${c.color}15; color:${c.color}">${iconSvg}</div>
                <h3>${c.title}</h3>
                <p>${c.description}</p>
                <div class="course-meta">
                    <span>${this.icons.book} ${c.totalModules} modulos</span>
                    <span>${this.icons.note} ${c.totalLessons} lecciones</span>
                    <span>${this.icons.trophy} ${c.totalExercises} ejercicios</span>
                </div>
                <div class="course-progress">
                    <div class="course-progress-bar" style="width:${coursePct}%; background:${c.color}"></div>
                </div>
                <div class="course-pct-label" style="color:${c.color}">${coursePct}%</div>
            </div>`;
        }).join('');

        this.render(`
        ${this.navbar('home')}
        <div class="main-content">
            <div class="container">
                <div class="hero fade-in">
                    <h1>Bienvenido, ${this.user.displayName}</h1>
                    <p>Tu camino hacia la ciberseguridad profesional comienza aqui. Aprende, practica y domina las habilidades esenciales.</p>
                </div>
                <div class="stats-bar">
                    <div class="stat-card fade-in" style="animation-delay:0.08s">
                        <div class="stat-label">Progreso Cursos</div>
                        <div class="stat-value" style="color:var(--accent)">${pct}%</div>
                        <div class="stat-sub">${stats.completedLessons} / ${stats.totalLessons} lecciones</div>
                    </div>
                    <div class="stat-card fade-in" style="animation-delay:0.13s">
                        <div class="stat-label">Ejercicios Correctos</div>
                        <div class="stat-value" style="color:var(--success)">${stats.correctExercises}</div>
                        <div class="stat-sub">${exPct}% de precision</div>
                    </div>
                    <div class="stat-card fade-in" style="animation-delay:0.18s">
                        <div class="stat-label">Puntos Simulador</div>
                        <div class="stat-value" style="color:#f59e0b">${sp.totalPoints || 0}</div>
                        <div class="stat-sub">${sp.completedScenarios || 0} escenarios completados</div>
                    </div>
                    <div class="stat-card fade-in" style="animation-delay:0.23s">
                        <div class="stat-label">Cursos Activos</div>
                        <div class="stat-value">${this.courses.length}</div>
                        <div class="stat-sub">CyberSec · Redes · Linux · OSINT · Python</div>
                    </div>
                </div>

                <h2 class="section-title fade-in" style="animation-delay:0.28s">Cursos de Aprendizaje</h2>
                <div class="courses-grid">${courseCards}</div>

                <div class="sim-banner fade-in" onclick="location.hash='#/simulator'">
                    <div class="sim-banner-icon">${this.icons.target}</div>
                    <div class="sim-banner-text">
                        <h3>Cyber Operations Simulator</h3>
                        <p>Practica con escenarios reales de SOC e Incident Response. Analiza logs, detecta ataques, investiga malware — como LetsDefend y HackTheBox.</p>
                    </div>
                    <div class="sim-banner-stats">
                        <span class="sim-stat">${sp.totalPoints || 0} pts</span>
                        <span class="sim-stat-label">obtenidos</span>
                    </div>
                    <div class="sim-banner-arrow">${this.icons.chevron}</div>
                </div>
            </div>
        </div>`);
    },

    // ── Course detail ──
    async renderCourse(courseId) {
        let course;
        try { course = await this.api(`/api/courses/${courseId}`); }
        catch (e) { location.hash = '#/'; return; }
        await this.loadProgress();

        const moduleCards = course.modules.map((mod, mi) => {
            const lessonsHtml = mod.lessons.map((lesson) => {
                const key = `${courseId}.${mod.id}.${lesson.id}`;
                const done = this.progress.lessons[key]?.completed;
                return `
                <div class="lesson-item" onclick="location.hash='#/lesson/${courseId}/${mod.id}/${lesson.id}'">
                    <div class="lesson-info">
                        <div class="lesson-status ${done ? 'completed' : ''}">${done ? this.icons.check : ''}</div>
                        <span class="lesson-title">${lesson.title}</span>
                    </div>
                </div>`;
            }).join('');

            const completedCount = mod.lessons.filter(l => this.progress.lessons[`${courseId}.${mod.id}.${l.id}`]?.completed).length;
            return `
            <div class="module-card ${mi === 0 ? 'open' : ''} fade-in" style="animation-delay:${mi * 0.06}s" id="mod-${mod.id}">
                <div class="module-header" onclick="App.toggleModule('${mod.id}')">
                    <div>
                        <h3>Modulo ${mi + 1}: ${mod.title}</h3>
                        <span class="module-count">${completedCount}/${mod.lessons.length} completadas</span>
                    </div>
                    <span class="chevron">${this.icons.chevron}</span>
                </div>
                <div class="module-lessons">${lessonsHtml}</div>
            </div>`;
        }).join('');

        const totalLessons = course.modules.reduce((s, m) => s + m.lessons.length, 0);
        const completedLessons = course.modules.reduce((s, m) =>
            s + m.lessons.filter(l => this.progress.lessons[`${courseId}.${m.id}.${l.id}`]?.completed).length, 0);

        this.render(`
        ${this.navbar('home')}
        <div class="main-content">
            <div class="container">
                <button class="btn-back" onclick="location.hash='#/'">${this.icons.back} Volver al inicio</button>
                <div class="course-header fade-in">
                    <h1 style="color:${course.color}">${course.title}</h1>
                    <p>${course.description}</p>
                    <div class="course-header-meta">
                        <span>${course.modules.length} modulos</span>
                        <span>${totalLessons} lecciones</span>
                        <span>${completedLessons} completadas</span>
                    </div>
                    <div class="course-progress" style="margin-top:16px; height:6px;">
                        <div class="course-progress-bar" style="width:${totalLessons > 0 ? Math.round(completedLessons / totalLessons * 100) : 0}%; background:${course.color}"></div>
                    </div>
                </div>
                <div class="modules-list">${moduleCards}</div>
            </div>
        </div>`);
    },

    toggleModule(modId) {
        document.getElementById(`mod-${modId}`).classList.toggle('open');
    },

    // ── Lesson page ──
    async renderLesson(courseId, moduleId, lessonId) {
        let lesson;
        try { lesson = await this.api(`/api/courses/${courseId}/modules/${moduleId}/lessons/${lessonId}`); }
        catch (e) { location.hash = `#/course/${courseId}`; return; }
        await this.loadProgress();

        let course;
        try { course = await this.api(`/api/courses/${courseId}`); } catch (e) {}

        const lessonKey = `${courseId}.${moduleId}.${lessonId}`;
        const isCompleted = this.progress.lessons[lessonKey]?.completed;

        const exercisesHtml = lesson.exercises.map((ex, i) => {
            const exKey = `${courseId}.${moduleId}.${lessonId}.${ex.id}`;
            const isDone = this.progress.exercises[exKey];

            let inputHtml = '';
            if (ex.type === 'multiple_choice') {
                inputHtml = `<div class="exercise-options">
                    ${ex.options.map((opt, oi) => `
                        <button class="option-btn ${isDone !== undefined ? (oi === isDone ? 'correct-answer' : '') : ''}"
                            onclick="App.selectOption('${ex.id}', ${oi})"
                            id="opt-${ex.id}-${oi}" ${isDone !== undefined ? 'disabled' : ''}>
                            ${opt}
                        </button>
                    `).join('')}
                </div>`;
            } else {
                inputHtml = `
                    <input type="text" class="exercise-input" id="input-${ex.id}"
                        placeholder="${ex.type === 'code_output' ? 'Escribe la salida del codigo...' : 'Escribe tu respuesta...'}"
                        ${isDone !== undefined ? 'disabled' : ''}>
                    <button class="exercise-submit" onclick="App.submitExercise('${ex.id}', '${ex.type}')"
                        id="submit-${ex.id}" ${isDone !== undefined ? 'disabled' : ''}>
                        Verificar
                    </button>`;
            }

            return `
            <div class="exercise ${isDone === true ? 'correct' : isDone === false ? 'incorrect' : ''}" id="exercise-${ex.id}">
                <div class="exercise-question">${this.parseExerciseQuestion(ex.question)}</div>
                ${inputHtml}
                <div id="explanation-${ex.id}"></div>
            </div>`;
        }).join('');

        let prevLesson = null, nextLesson = null;
        if (course) {
            const allLessons = [];
            course.modules.forEach(m => m.lessons.forEach(l => allLessons.push({ ...l, moduleId: m.id })));
            const idx = allLessons.findIndex(l => l.id === lessonId && l.moduleId === moduleId);
            if (idx > 0) prevLesson = allLessons[idx - 1];
            if (idx < allLessons.length - 1) nextLesson = allLessons[idx + 1];
        }

        this.render(`
        ${this.navbar('home')}
        <div class="main-content">
            <div class="container">
                <button class="btn-back" onclick="location.hash='#/course/${courseId}'">${this.icons.back} Volver al curso</button>
                <div class="lesson-layout">
                    <div class="lesson-content fade-in">
                        <h1>${lesson.title}</h1>
                        ${this.parseTheory(lesson.theory)}
                        <div class="lesson-nav">
                            ${prevLesson ? `<button class="btn btn-secondary btn-sm" onclick="location.hash='#/lesson/${courseId}/${prevLesson.moduleId}/${prevLesson.id}'">${this.icons.back} Anterior</button>` : '<div></div>'}
                            ${!isCompleted ? `<button class="btn btn-success btn-sm" onclick="App.completeLesson('${courseId}','${moduleId}','${lessonId}')" id="complete-btn">${this.icons.check} Marcar como completada</button>` : `<span style="color:var(--success); font-size:14px; font-weight:500;">${this.icons.check} Completada</span>`}
                            ${nextLesson ? `<button class="btn btn-primary btn-sm" onclick="location.hash='#/lesson/${courseId}/${nextLesson.moduleId}/${nextLesson.id}'">Siguiente ${this.icons.chevron}</button>` : '<div></div>'}
                        </div>
                    </div>
                    <div class="lesson-sidebar">
                        <div class="exercises-panel fade-in" style="animation-delay:0.1s">
                            <h3>${this.icons.trophy} Ejercicios (${lesson.exercises.length})</h3>
                            ${exercisesHtml || '<p style="color:var(--text-muted); font-size:13px;">No hay ejercicios para esta leccion.</p>'}
                        </div>
                        <div class="notes-panel fade-in" style="animation-delay:0.15s">
                            <h3>${this.icons.note} Mis Notas</h3>
                            <textarea class="notes-textarea" id="lesson-notes" placeholder="Escribe tus notas aqui..."></textarea>
                            <div class="notes-actions">
                                <button class="btn btn-secondary btn-sm" onclick="App.saveNotes('${courseId}','${moduleId}','${lessonId}')">Guardar notas</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>`);

        this._currentLesson = { courseId, moduleId, lessonId };
        this.loadNotes(courseId, moduleId, lessonId);
    },

    // ── Exercise handling ──
    _selectedOptions: {},

    selectOption(exerciseId, optionIndex) {
        this._selectedOptions[exerciseId] = optionIndex;
        document.querySelectorAll(`[id^="opt-${exerciseId}-"]`).forEach((btn, i) => {
            btn.classList.toggle('selected', i === optionIndex);
        });
        this.submitExercise(exerciseId, 'multiple_choice');
    },

    async submitExercise(exerciseId, type) {
        const { courseId, moduleId, lessonId } = this._currentLesson;
        let answer;
        if (type === 'multiple_choice') {
            answer = this._selectedOptions[exerciseId];
            if (answer === undefined) return;
        } else {
            const input = document.getElementById(`input-${exerciseId}`);
            answer = input.value.trim();
            if (!answer) return;
        }

        try {
            const result = await this.api('/api/exercises/check', {
                method: 'POST',
                body: { courseId, moduleId, lessonId, exerciseId, answer: String(answer) }
            });

            const exEl = document.getElementById(`exercise-${exerciseId}`);
            const explEl = document.getElementById(`explanation-${exerciseId}`);

            if (result.correct) {
                exEl.classList.add('correct'); exEl.classList.remove('incorrect');
                explEl.innerHTML = `<div class="exercise-explanation correct">${result.explanation}</div>`;
            } else {
                exEl.classList.add('incorrect'); exEl.classList.remove('correct');
                explEl.innerHTML = `<div class="exercise-explanation incorrect">${result.explanation}</div>`;
            }

            if (type === 'multiple_choice') {
                document.querySelectorAll(`[id^="opt-${exerciseId}-"]`).forEach((btn, i) => {
                    btn.disabled = true;
                    if (result.correct && i === answer) btn.classList.add('correct-answer');
                    if (!result.correct && i === answer) btn.classList.add('wrong-answer');
                });
            } else {
                document.getElementById(`input-${exerciseId}`).disabled = true;
                document.getElementById(`submit-${exerciseId}`).disabled = true;
            }

            const exKey = `${courseId}.${moduleId}.${lessonId}.${exerciseId}`;
            this.progress.exercises[exKey] = result.correct;
        } catch (err) { console.error('Error submitting exercise', err); }
    },

    async completeLesson(courseId, moduleId, lessonId) {
        try {
            const key = `${courseId}.${moduleId}.${lessonId}`;
            let correctCount = 0, totalCount = 0;
            for (const [k, v] of Object.entries(this.progress.exercises)) {
                if (k.startsWith(key + '.')) { totalCount++; if (v) correctCount++; }
            }
            const score = totalCount > 0 ? Math.round((correctCount / totalCount) * 100) : 100;
            await this.api('/api/progress/complete', { method: 'POST', body: { courseId, moduleId, lessonId, score } });
            this.progress.lessons[key] = { completed: true, score };
            const btn = document.getElementById('complete-btn');
            if (btn) btn.outerHTML = `<span style="color:var(--success); font-size:14px; font-weight:500;">${this.icons.check} Completada</span>`;
        } catch (err) { console.error('Error completing lesson', err); }
    },

    async loadNotes(courseId, moduleId, lessonId) {
        try {
            const data = await this.api(`/api/notes?courseId=${courseId}&moduleId=${moduleId}&lessonId=${lessonId}`);
            const el = document.getElementById('lesson-notes');
            if (el && data.content) el.value = data.content;
        } catch (e) {}
    },

    async saveNotes(courseId, moduleId, lessonId) {
        const content = document.getElementById('lesson-notes').value;
        try {
            await this.api('/api/notes', { method: 'POST', body: { courseId, moduleId, lessonId, content } });
            const btn = event.target;
            const orig = btn.textContent;
            btn.textContent = 'Guardado!';
            btn.classList.remove('btn-secondary'); btn.classList.add('btn-success');
            setTimeout(() => {
                btn.textContent = orig;
                btn.classList.remove('btn-success'); btn.classList.add('btn-secondary');
            }, 1500);
        } catch (e) { console.error('Error saving notes', e); }
    },

    // ══════════════════════════════════════════════════════════
    // ── SIMULATOR ──
    // ══════════════════════════════════════════════════════════

    async renderSimulator() {
        await this.loadSimProgress();
        let scenarios = [];
        try { scenarios = await this.api('/api/simulator/scenarios'); } catch (e) {}

        const socScenarios = scenarios.filter(s => s.category === 'soc');
        const malScenarios = scenarios.filter(s => s.category === 'malware');
        const sp = this.simProgress;

        const makeCard = (s, i) => {
            const prog = sp.scenarios[s.id] || { tasks: {}, completed: false, total_points: 0 };
            const completedTasks = Object.values(prog.tasks || {}).filter(t => t.correct).length;
            const pct = s.task_count > 0 ? Math.round((completedTasks / s.task_count) * 100) : 0;
            const isCompleted = prog.completed;

            return `
            <div class="scenario-card fade-in ${isCompleted ? 'scenario-done' : ''}" style="animation-delay:${i * 0.06}s"
                 onclick="location.hash='#/simulator/${s.id}'">
                <div class="scenario-header">
                    <div class="scenario-diff" style="background:${s.difficulty_color}20; color:${s.difficulty_color}">
                        ${s.difficulty}
                    </div>
                    <div class="scenario-pts">${this.icons.star} ${s.points} pts</div>
                </div>
                <h3>${s.title}</h3>
                <p class="scenario-sub">${s.subcategory}</p>
                <p class="scenario-desc">${s.description.substring(0, 100)}...</p>
                <div class="scenario-objectives">
                    ${s.objectives.slice(0, 2).map(o => `<span>${this.icons.check} ${o}</span>`).join('')}
                </div>
                <div class="scenario-progress-row">
                    <div class="scenario-progress-bar-wrap">
                        <div class="scenario-progress-bar" style="width:${pct}%; background:${s.difficulty_color}"></div>
                    </div>
                    <span class="scenario-pct">${completedTasks}/${s.task_count} tareas</span>
                </div>
                ${isCompleted ? `<div class="scenario-complete-badge">${this.icons.check} Completado</div>` : ''}
            </div>`;
        };

        this.render(`
        ${this.navbar('simulator')}
        <div class="main-content">
            <div class="container">
                <div class="sim-hero fade-in">
                    <div class="sim-hero-icon">${this.icons.target}</div>
                    <div>
                        <h1>Cyber Operations Simulator</h1>
                        <p>Escenarios reales de SOC, Incident Response y Malware Analysis. Aprende haciendo, no solo leyendo.</p>
                    </div>
                    <div class="sim-hero-stats">
                        <div class="sim-stat-box">
                            <span class="sim-stat-num">${sp.totalPoints || 0}</span>
                            <span class="sim-stat-lbl">Puntos</span>
                        </div>
                        <div class="sim-stat-box">
                            <span class="sim-stat-num">${sp.completedScenarios || 0}/${sp.totalScenarios || scenarios.length}</span>
                            <span class="sim-stat-lbl">Completados</span>
                        </div>
                    </div>
                </div>

                <div class="sim-section fade-in" style="animation-delay:0.1s">
                    <div class="sim-section-header">
                        <div class="sim-section-icon" style="background:#3b82f620; color:#3b82f6">${this.icons.shield}</div>
                        <div>
                            <h2>SOC & Incident Response</h2>
                            <p>Analiza alertas, logs y evidencia como un analista de SOC real. Detecta ataques, clasifica incidentes, responde amenazas.</p>
                        </div>
                    </div>
                    <div class="scenarios-grid">${socScenarios.map((s, i) => makeCard(s, i)).join('')}</div>
                </div>

                <div class="sim-section fade-in" style="animation-delay:0.2s">
                    <div class="sim-section-header">
                        <div class="sim-section-icon" style="background:#ef444420; color:#ef4444">${this.icons.bug}</div>
                        <div>
                            <h2>Malware Analysis Lab</h2>
                            <p>Analiza muestras de malware, scripts maliciosos, trafico de red y artefactos forenses de sistemas comprometidos.</p>
                        </div>
                    </div>
                    <div class="scenarios-grid">${malScenarios.map((s, i) => makeCard(s, i)).join('')}</div>
                </div>
            </div>
        </div>`);
    },

    // ── Scenario detail ──
    async renderScenario(scenarioId) {
        let scenario;
        try { scenario = await this.api(`/api/simulator/scenarios/${scenarioId}`); }
        catch (e) { location.hash = '#/simulator'; return; }
        await this.loadSimProgress();

        const sp = this.simProgress.scenarios[scenarioId] || { tasks: {} };
        this._currentScenario = scenarioId;
        this._simHints = {};

        const diffColors = { 'Principiante': '#10b981', 'Intermedio': '#f59e0b', 'Avanzado': '#ef4444' };
        const diffColor = diffColors[scenario.difficulty] || '#8b5cf6';

        const evidenceHtml = Object.entries(scenario.evidence || {}).map(([title, content], i) => `
        <div class="evidence-block fade-in" style="animation-delay:${i * 0.06}s">
            <div class="evidence-title" onclick="App.toggleEvidence('ev-${i}')">
                <span>${this.icons.note} ${title}</span>
                <span class="ev-toggle" id="ev-toggle-${i}">${this.icons.chevron}</span>
            </div>
            <div class="evidence-content" id="ev-${i}">
                <pre>${this.escapeHtml(content)}</pre>
            </div>
        </div>`).join('');

        const tasksHtml = scenario.tasks.map((task, ti) => {
            const taskProg = sp.tasks[task.id];
            const isDone = taskProg?.correct;
            const alreadyDone = isDone;

            let inputHtml = '';
            if (task.type === 'multiple_choice') {
                inputHtml = `<div class="sim-options">
                    ${task.options.map((opt, oi) => `
                        <button class="sim-option-btn ${alreadyDone ? 'disabled' : ''}"
                            onclick="App.submitSimTask('${task.id}', ${oi}, 'multiple_choice')"
                            id="simopt-${task.id}-${oi}" ${alreadyDone ? 'disabled' : ''}>
                            <span class="sim-opt-letter">${String.fromCharCode(65 + oi)}</span>
                            ${opt}
                        </button>
                    `).join('')}
                </div>`;
            } else {
                inputHtml = `
                <div class="sim-text-input-row">
                    <input type="text" class="sim-text-input" id="siminput-${task.id}"
                        placeholder="Tu respuesta..."
                        ${alreadyDone ? 'disabled' : ''}
                        onkeydown="if(event.key==='Enter') App.submitSimTask('${task.id}', null, 'text')">
                    <button class="btn btn-primary btn-sm" onclick="App.submitSimTask('${task.id}', null, 'text')"
                        id="simsub-${task.id}" ${alreadyDone ? 'disabled' : ''}>
                        Verificar
                    </button>
                </div>`;
            }

            return `
            <div class="sim-task ${isDone ? 'sim-task-done' : ''}" id="simtask-${task.id}">
                <div class="sim-task-header">
                    <div class="sim-task-num">${ti + 1}</div>
                    <div class="sim-task-q">${this.parseExerciseQuestion(task.question)}</div>
                    ${isDone ? `<div class="sim-task-check">${this.icons.check}</div>` : ''}
                </div>
                ${!isDone ? inputHtml : ''}
                <div id="simfeedback-${task.id}" class="${isDone ? 'sim-feedback-done' : ''}">
                    ${isDone ? `<div class="sim-explanation correct">Correcto. ${isDone ? '' : ''}</div>` : ''}
                </div>
                ${!alreadyDone ? `
                <div class="sim-task-actions">
                    <button class="btn-hint" onclick="App.getSimHint('${task.id}')" id="hint-btn-${task.id}">
                        ${this.icons.hint} Ver pista
                    </button>
                    <div id="hint-${task.id}" class="sim-hint" style="display:none"></div>
                </div>` : ''}
            </div>`;
        }).join('');

        const completedTasks = Object.values(sp.tasks || {}).filter(t => t.correct).length;
        const totalPts = Object.values(sp.tasks || {}).reduce((s, t) => s + (t.points || 0), 0);

        this.render(`
        ${this.navbar('simulator')}
        <div class="main-content">
            <div class="container">
                <button class="btn-back" onclick="location.hash='#/simulator'">${this.icons.back} Volver al Simulador</button>
                <div class="scenario-detail-header fade-in">
                    <div class="scenario-detail-meta">
                        <span class="scenario-diff" style="background:${diffColor}20; color:${diffColor}">${scenario.difficulty}</span>
                        <span class="scenario-cat">${scenario.subcategory}</span>
                        <span class="scenario-pts-badge">${this.icons.star} ${scenario.points} puntos disponibles</span>
                    </div>
                    <h1>${scenario.title}</h1>
                    <p>${scenario.description}</p>
                    <div class="scenario-objectives-list">
                        <strong>Objetivos:</strong>
                        ${scenario.objectives.map(o => `<span>${this.icons.check} ${o}</span>`).join('')}
                    </div>
                    <div class="scenario-score-bar">
                        <span>${completedTasks} / ${scenario.tasks.length} tareas completadas</span>
                        <span class="scenario-score-pts">${totalPts} pts obtenidos</span>
                    </div>
                </div>

                <div class="sim-layout">
                    <div class="sim-evidence-panel fade-in" style="animation-delay:0.1s">
                        <h2>${this.icons.note} Evidencia del Incidente</h2>
                        <p class="sim-evidence-note">Analiza toda la evidencia disponible antes de responder las preguntas.</p>
                        ${evidenceHtml}
                    </div>
                    <div class="sim-tasks-panel fade-in" style="animation-delay:0.15s">
                        <h2>${this.icons.target} Preguntas de Investigacion</h2>
                        <div class="sim-tasks-list">${tasksHtml}</div>
                    </div>
                </div>
            </div>
        </div>`);

        // Auto-open first evidence
        const firstEv = document.getElementById('ev-0');
        if (firstEv) firstEv.style.display = 'block';
    },

    toggleEvidence(evId) {
        const el = document.getElementById(evId);
        if (!el) return;
        const isOpen = el.style.display !== 'none';
        el.style.display = isOpen ? 'none' : 'block';
    },

    async getSimHint(taskId) {
        const btn = document.getElementById(`hint-btn-${taskId}`);
        const hintEl = document.getElementById(`hint-${taskId}`);
        if (!hintEl) return;

        if (hintEl.style.display !== 'none') {
            hintEl.style.display = 'none';
            if (btn) btn.innerHTML = `${this.icons.hint} Ver pista`;
            return;
        }

        try {
            const data = await this.api('/api/simulator/hint', {
                method: 'POST',
                body: { scenarioId: this._currentScenario, taskId }
            });
            hintEl.innerHTML = `<span>${this.icons.hint} ${data.hint}</span>`;
            hintEl.style.display = 'block';
            if (btn) btn.innerHTML = `${this.icons.hint} Ocultar pista`;
        } catch (e) {}
    },

    async submitSimTask(taskId, optionIndex, type) {
        let answer;
        if (type === 'multiple_choice') {
            answer = String(optionIndex);
            // Visual selection
            document.querySelectorAll(`[id^="simopt-${taskId}-"]`).forEach((btn, i) => {
                btn.classList.toggle('selected', i === optionIndex);
            });
        } else {
            const input = document.getElementById(`siminput-${taskId}`);
            answer = input ? input.value.trim() : '';
            if (!answer) return;
        }

        try {
            const result = await this.api('/api/simulator/submit', {
                method: 'POST',
                body: { scenarioId: this._currentScenario, taskId, answer }
            });

            const feedbackEl = document.getElementById(`simfeedback-${taskId}`);
            const taskEl = document.getElementById(`simtask-${taskId}`);

            if (result.correct) {
                taskEl.classList.add('sim-task-done');
                if (feedbackEl) feedbackEl.innerHTML = `<div class="sim-explanation correct">${this.icons.check} Correcto! (+${result.points_earned} pts)<br>${result.explanation}</div>`;

                // Disable inputs
                if (type === 'multiple_choice') {
                    document.querySelectorAll(`[id^="simopt-${taskId}-"]`).forEach((btn, i) => {
                        btn.disabled = true;
                        if (i === optionIndex) btn.classList.add('sim-correct');
                    });
                } else {
                    const input = document.getElementById(`siminput-${taskId}`);
                    const sub = document.getElementById(`simsub-${taskId}`);
                    if (input) input.disabled = true;
                    if (sub) sub.disabled = true;
                }

                // Add check icon
                const header = taskEl.querySelector('.sim-task-header');
                if (header && !header.querySelector('.sim-task-check')) {
                    const checkDiv = document.createElement('div');
                    checkDiv.className = 'sim-task-check';
                    checkDiv.innerHTML = this.icons.check;
                    header.appendChild(checkDiv);
                }

                // Hide hint button
                const hintArea = document.getElementById(`hint-btn-${taskId}`)?.closest('.sim-task-actions');
                if (hintArea) hintArea.remove();

                // Update progress
                await this.loadSimProgress();
            } else {
                if (feedbackEl) feedbackEl.innerHTML = `<div class="sim-explanation incorrect">${this.icons.alert} Incorrecto. ${result.hint ? `<br><em>Pista: ${result.hint}</em>` : ''}</div>`;
                if (type === 'multiple_choice') {
                    document.querySelectorAll(`[id^="simopt-${taskId}-"]`).forEach((btn, i) => {
                        if (i === optionIndex) btn.classList.add('sim-wrong');
                        btn.disabled = false;
                        setTimeout(() => { btn.classList.remove('sim-wrong', 'selected'); btn.disabled = false; }, 1500);
                    });
                }
            }
        } catch (err) { console.error('Sim submit error', err); }
    }
};

// Boot
document.addEventListener('DOMContentLoaded', () => App.init());
