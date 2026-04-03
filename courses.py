"""
Course data for Contra Amenaza.
Each course has modules, each module has lessons with theory + exercises.
"""

COURSES = {
    "cybersecurity": {
        "id": "cybersecurity",
        "title": "Ciberseguridad Blue Team",
        "description": "Aprende defensa cibernetica desde los fundamentos hasta operaciones SOC y respuesta a incidentes.",
        "icon": "shield",
        "color": "#00bcd4",
        "modules": [
            {
                "id": "m1",
                "title": "Fundamentos de Ciberseguridad",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Triada CIA y principios de seguridad",
                        "theory": """## La Triada CIA

Los tres pilares fundamentales de la seguridad de la informacion:

### Confidencialidad
Garantizar que la informacion solo sea accesible por personas autorizadas.
- **Controles**: Cifrado, control de acceso, autenticacion
- **Amenazas**: Intercepcion, espionaje, acceso no autorizado
- **Ejemplo**: Cifrar datos en transito con TLS/SSL

### Integridad
Garantizar que la informacion no ha sido alterada de forma no autorizada.
- **Controles**: Hashing, firmas digitales, checksums
- **Amenazas**: Modificacion de datos, man-in-the-middle
- **Ejemplo**: Verificar integridad de archivos con SHA-256

### Disponibilidad
Garantizar que los sistemas y datos esten accesibles cuando se necesiten.
- **Controles**: Redundancia, backups, balanceo de carga
- **Amenazas**: DDoS, fallos de hardware, desastres naturales
- **Ejemplo**: Servidores redundantes en diferentes zonas

### Principios adicionales:
- **Autenticacion**: Verificar la identidad (quien eres)
- **Autorizacion**: Verificar permisos (que puedes hacer)
- **No repudio**: Garantizar que no se pueda negar una accion
- **Principio de minimo privilegio**: Solo dar accesos necesarios
- **Defensa en profundidad**: Multiples capas de seguridad""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Que componente de la triada CIA protege contra la modificacion no autorizada de datos?",
                                "options": ["Confidencialidad", "Integridad", "Disponibilidad", "Autenticacion"],
                                "correct": 1,
                                "explanation": "La Integridad garantiza que los datos no han sido alterados de forma no autorizada. Se protege con hashing, firmas digitales y checksums."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Un ataque DDoS afecta principalmente a cual componente de la triada CIA?",
                                "options": ["Confidencialidad", "Integridad", "Disponibilidad", "Todas por igual"],
                                "correct": 2,
                                "explanation": "Un ataque DDoS busca saturar los recursos del sistema para que no este disponible para los usuarios legitimos, afectando la Disponibilidad."
                            },
                            {
                                "id": "e3",
                                "type": "fill_blank",
                                "question": "El principio de ___ establece que un usuario solo debe tener los permisos estrictamente necesarios para su trabajo",
                                "correct": "minimo privilegio",
                                "explanation": "El principio de minimo privilegio (Least Privilege) reduce la superficie de ataque limitando los accesos de cada usuario al minimo necesario."
                            }
                        ]
                    },
                    {
                        "id": "l2",
                        "title": "Tipos de amenazas y atacantes",
                        "theory": """## Panorama de Amenazas

### Tipos de Malware:
- **Virus**: Se adjunta a programas legitimos y se replica
- **Gusano (Worm)**: Se replica automaticamente por la red
- **Troyano**: Se disfraza de software legitimo
- **Ransomware**: Cifra archivos y pide rescate
- **Spyware**: Recopila informacion sin consentimiento
- **Rootkit**: Se oculta en el sistema para mantener acceso
- **Keylogger**: Registra las pulsaciones del teclado

### Tipos de Ataques:
| Ataque | Descripcion |
|--------|-------------|
| Phishing | Engano por email/web para robar credenciales |
| Man-in-the-Middle | Interceptar comunicaciones |
| SQL Injection | Inyectar codigo SQL malicioso |
| XSS | Inyectar scripts en paginas web |
| Brute Force | Probar todas las combinaciones posibles |
| Social Engineering | Manipulacion psicologica |
| DDoS | Saturar un servicio con trafico |

### Tipos de Atacantes:
- **Script Kiddies**: Usan herramientas sin entenderlas
- **Hacktivistas**: Motivados por ideologia
- **Cibercriminales**: Motivados por dinero
- **APT (Advanced Persistent Threat)**: Grupos patrocinados por estados
- **Insiders**: Amenazas internas (empleados)

### Frameworks de referencia:
- **MITRE ATT&CK**: Base de conocimiento de tacticas y tecnicas de ataque
- **Cyber Kill Chain**: Fases de un ataque (Lockheed Martin)
- **OWASP Top 10**: Principales vulnerabilidades web""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Que tipo de malware cifra los archivos y pide rescate?",
                                "options": ["Spyware", "Trojan", "Ransomware", "Rootkit"],
                                "correct": 2,
                                "explanation": "El Ransomware cifra los archivos de la victima y exige un pago (generalmente en criptomonedas) para proporcionar la clave de descifrado."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Que framework cataloga tacticas y tecnicas de atacantes reales?",
                                "options": ["OWASP Top 10", "MITRE ATT&CK", "ISO 27001", "PCI DSS"],
                                "correct": 1,
                                "explanation": "MITRE ATT&CK es una base de conocimiento que cataloga tacticas, tecnicas y procedimientos (TTPs) observados en ataques reales."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m2",
                "title": "Seguridad de Red",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Firewalls, IDS e IPS",
                        "theory": """## Seguridad Perimetral

### Firewalls:
Filtran el trafico de red basandose en reglas.

**Tipos de Firewalls:**
- **Packet Filter**: Filtra por IP, puerto, protocolo
- **Stateful**: Rastrea el estado de las conexiones
- **Application Layer (WAF)**: Inspecciona contenido de capa 7
- **Next-Generation (NGFW)**: Combina todo + DPI + threat intelligence

**Reglas basicas de iptables (Linux):**
```bash
# Bloquear todo el trafico entrante por defecto
iptables -P INPUT DROP

# Permitir trafico SSH (puerto 22)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Permitir trafico HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Permitir trafico de loopback
iptables -A INPUT -i lo -j ACCEPT

# Permitir conexiones establecidas
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

### IDS (Intrusion Detection System):
Detecta actividad sospechosa y genera alertas (modo pasivo).
- **NIDS**: Basado en red (Snort, Suricata)
- **HIDS**: Basado en host (OSSEC, Wazuh)
- **Deteccion por firmas**: Patrones conocidos
- **Deteccion por anomalias**: Comportamiento inusual

### IPS (Intrusion Prevention System):
Como un IDS pero puede BLOQUEAR trafico automaticamente (modo activo).

### Ejemplo de regla Snort:
```
alert tcp any any -> $HOME_NET 80 (msg:"Possible SQL Injection";
content:"' OR '1'='1"; nocase; sid:100001; rev:1;)
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Cual es la diferencia principal entre un IDS y un IPS?",
                                "options": ["El IDS es mas caro", "El IPS puede bloquear trafico automaticamente", "El IDS solo funciona en la nube", "No hay diferencia"],
                                "correct": 1,
                                "explanation": "El IDS solo detecta y alerta (modo pasivo), mientras que el IPS puede detectar Y bloquear trafico malicioso automaticamente (modo activo)."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Que tipo de firewall puede inspeccionar el contenido de las aplicaciones web?",
                                "options": ["Packet Filter", "Stateful Firewall", "WAF (Web Application Firewall)", "Router ACL"],
                                "correct": 2,
                                "explanation": "Un WAF opera en la capa 7 (aplicacion) y puede inspeccionar solicitudes HTTP/HTTPS para detectar ataques como SQL Injection o XSS."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m3",
                "title": "SIEM y Analisis de Logs",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Introduccion a SIEM",
                        "theory": """## SIEM - Security Information and Event Management

### Que es un SIEM?
Un SIEM recopila, normaliza, correlaciona y analiza logs de multiples fuentes para detectar amenazas.

### Funciones principales:
1. **Recopilacion de logs**: Centraliza logs de firewalls, servidores, endpoints
2. **Normalizacion**: Convierte logs de diferentes formatos a un formato comun
3. **Correlacion**: Relaciona eventos de multiples fuentes
4. **Alertas**: Genera alertas basadas en reglas y anomalias
5. **Dashboards**: Visualizacion en tiempo real
6. **Retencion**: Almacena logs para investigacion forense

### SIEMs populares:
- **Splunk**: Lider comercial, potente busqueda
- **Elastic SIEM (ELK Stack)**: Open source (Elasticsearch, Logstash, Kibana)
- **Microsoft Sentinel**: SIEM en la nube de Azure
- **Wazuh**: Open source, basado en OSSEC
- **QRadar**: IBM, para grandes empresas

### Fuentes de logs comunes:
```
- Firewalls: trafico permitido/denegado
- Servidores web: accesos, errores (Apache, Nginx)
- Active Directory: logins, cambios de permisos
- Endpoints: antivirus, EDR
- Aplicaciones: errores, accesos
- DNS: consultas, respuestas
- Proxy: navegacion web
```

### Ejemplo de busqueda en Splunk:
```spl
index=security sourcetype=firewall action=blocked
| stats count by src_ip, dest_port
| where count > 100
| sort -count
```

### Logs clave en Windows (Event IDs):
| Event ID | Descripcion |
|----------|-------------|
| 4624 | Login exitoso |
| 4625 | Login fallido |
| 4720 | Cuenta creada |
| 4732 | Usuario agregado a grupo |
| 1102 | Log de auditoria borrado |""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Cual es la funcion principal de un SIEM?",
                                "options": ["Bloquear malware", "Centralizar y correlacionar logs para detectar amenazas", "Cifrar comunicaciones", "Gestionar parches"],
                                "correct": 1,
                                "explanation": "Un SIEM centraliza logs de multiples fuentes, los normaliza, correlaciona eventos y genera alertas para detectar amenazas de seguridad."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "El Event ID ___ de Windows indica un intento de login fallido",
                                "correct": "4625",
                                "explanation": "El Event ID 4625 en Windows registra cada intento de inicio de sesion fallido, es crucial para detectar ataques de fuerza bruta."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m4",
                "title": "Respuesta a Incidentes",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Proceso de respuesta a incidentes",
                        "theory": """## Respuesta a Incidentes (Incident Response)

### Fases del Incident Response (NIST SP 800-61):

#### 1. Preparacion
- Crear el equipo de respuesta (CSIRT/CERT)
- Documentar procedimientos y playbooks
- Configurar herramientas de deteccion
- Realizar ejercicios y simulacros
- Mantener lista de contactos actualizada

#### 2. Deteccion y Analisis
- Monitorear alertas del SIEM
- Validar si es un incidente real (triage)
- Determinar el alcance y la severidad
- Documentar hallazgos (timeline)
- Clasificar el incidente (categoria y prioridad)

**Categorias de severidad:**
| Nivel | Descripcion | Ejemplo |
|-------|-------------|---------|
| Critico | Impacto masivo | Ransomware en produccion |
| Alto | Impacto significativo | Cuenta admin comprometida |
| Medio | Impacto limitado | Malware en un endpoint |
| Bajo | Impacto minimo | Phishing detectado y bloqueado |

#### 3. Contencion, Erradicacion y Recuperacion
**Contencion a corto plazo:**
- Aislar sistemas afectados
- Bloquear IPs maliciosas
- Desactivar cuentas comprometidas

**Erradicacion:**
- Eliminar malware
- Cerrar vulnerabilidades
- Cambiar credenciales comprometidas

**Recuperacion:**
- Restaurar sistemas desde backups
- Verificar integridad
- Monitorear actividad post-incidente

#### 4. Actividad Post-Incidente
- Lessons learned (lecciones aprendidas)
- Actualizar procedimientos
- Mejorar detecciones
- Documentar el incidente completo""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Cual es la primera accion al detectar un incidente de ransomware activo?",
                                "options": ["Pagar el rescate", "Aislar los sistemas afectados", "Formatear los equipos", "Notificar a la prensa"],
                                "correct": 1,
                                "explanation": "La contencion inmediata (aislar sistemas) es crucial para evitar la propagacion del ransomware a otros equipos de la red."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Segun NIST, cual es la fase final del proceso de respuesta a incidentes?",
                                "options": ["Erradicacion", "Recuperacion", "Actividad Post-Incidente", "Contencion"],
                                "correct": 2,
                                "explanation": "La fase de Post-Incidente incluye lecciones aprendidas, actualizacion de procedimientos y documentacion del incidente completo."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m5",
                "title": "Analisis de Trafico de Red",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Wireshark y tcpdump",
                        "theory": """## Analisis de Trafico de Red

### Wireshark
Analizador de protocolos con interfaz grafica.

**Filtros de visualizacion comunes:**
```
# Filtrar por IP
ip.addr == 192.168.1.100

# Filtrar por protocolo
http || dns || tcp

# Filtrar por puerto
tcp.port == 443

# Trafico HTTP GET
http.request.method == "GET"

# DNS queries
dns.qry.name contains "malware"

# Trafico TCP con flags SYN
tcp.flags.syn == 1 && tcp.flags.ack == 0

# Paquetes con errores
tcp.analysis.retransmission
```

### tcpdump (linea de comandos)
```bash
# Capturar en una interfaz
tcpdump -i eth0

# Filtrar por host
tcpdump host 192.168.1.100

# Filtrar por puerto
tcpdump port 80

# Guardar a archivo
tcpdump -w captura.pcap

# Leer archivo
tcpdump -r captura.pcap

# Filtrar DNS
tcpdump port 53

# Mostrar contenido ASCII
tcpdump -A port 80
```

### Que buscar en el trafico:
- Conexiones a IPs/dominios sospechosos
- Trafico en puertos inusuales
- Grandes transferencias de datos (exfiltracion)
- Beaconing (conexiones periodicas a un C2)
- DNS tunneling (consultas DNS anormalmente largas)
- Trafico no cifrado con datos sensibles""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "fill_blank",
                                "question": "El filtro de Wireshark para ver solo trafico HTTP es: ___",
                                "correct": "http",
                                "explanation": "En Wireshark, simplemente escribir 'http' como filtro de visualizacion muestra solo los paquetes del protocolo HTTP."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Que patron de trafico podria indicar comunicacion con un servidor C2 (Command & Control)?",
                                "options": ["Trafico HTTP normal", "Conexiones periodicas regulares (beaconing)", "Descargas de actualizaciones", "Trafico HTTPS a google.com"],
                                "correct": 1,
                                "explanation": "El beaconing (conexiones periodicas y regulares a un servidor externo) es un indicador clasico de malware comunicandose con un servidor de comando y control (C2)."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m6",
                "title": "Forense Digital Basico",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Principios de forensia digital",
                        "theory": """## Forense Digital

### Principios fundamentales:
1. **Preservar la evidencia**: No modificar los datos originales
2. **Cadena de custodia**: Documentar quien maneja la evidencia
3. **Documentar todo**: Cada paso debe ser registrado
4. **Reproducibilidad**: Otro analista debe poder repetir el proceso

### Proceso forense:
1. **Identificacion**: Determinar que dispositivos son relevantes
2. **Adquisicion**: Crear copias forenses (imagenes)
3. **Analisis**: Examinar la evidencia
4. **Documentacion**: Reportar hallazgos

### Herramientas forenses:
| Herramienta | Uso |
|-------------|-----|
| FTK Imager | Adquisicion de imagenes de disco |
| Autopsy | Analisis forense de disco (open source) |
| Volatility | Analisis de memoria RAM |
| The Sleuth Kit | Herramientas de linea de comandos |
| KAPE | Triaje rapido de artefactos |

### Artefactos importantes en Windows:
- **Prefetch**: Programas ejecutados recientemente
- **Registry**: Configuracion del sistema y usuario
- **Event Logs**: Registros de eventos
- **MFT**: Master File Table del sistema de archivos
- **$UsnJrnl**: Journal de cambios del sistema de archivos
- **Amcache/Shimcache**: Historial de ejecucion de programas

### Comandos utiles para triaje:
```bash
# Hash de un archivo (integridad)
sha256sum archivo.exe

# Listar procesos (Linux)
ps aux

# Conexiones de red activas
netstat -antup

# Usuarios conectados
who
last
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Cual es el primer paso critico en una investigacion forense?",
                                "options": ["Analizar los archivos", "Preservar la evidencia original", "Borrar los logs", "Reiniciar el sistema"],
                                "correct": 1,
                                "explanation": "Preservar la evidencia es crucial. Se debe crear una copia forense (imagen) del sistema y trabajar sobre la copia, nunca sobre el original."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m7",
                "title": "Operaciones SOC",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "El Security Operations Center",
                        "theory": """## Operaciones del SOC

### Que es un SOC?
Centro de Operaciones de Seguridad: equipo dedicado a monitorear, detectar y responder a incidentes de seguridad 24/7.

### Roles en el SOC:
| Nivel | Rol | Responsabilidades |
|-------|-----|-------------------|
| Tier 1 | Analista SOC | Monitorear alertas, triage inicial |
| Tier 2 | Analista Senior | Investigacion profunda, contencion |
| Tier 3 | Threat Hunter | Busqueda proactiva de amenazas |
| Lead | SOC Manager | Gestion del equipo, metricas, mejora |

### Metricas del SOC:
- **MTTD** (Mean Time to Detect): Tiempo promedio para detectar
- **MTTR** (Mean Time to Respond): Tiempo promedio para responder
- **False Positive Rate**: Porcentaje de falsas alarmas
- **Alert Volume**: Numero de alertas por periodo

### Proceso de Triage de alertas:
1. Recibir alerta del SIEM
2. Verificar si es un falso positivo
3. Determinar severidad e impacto
4. Investigar el contexto (IOCs, logs relacionados)
5. Escalar si es necesario (Tier 2/3)
6. Documentar acciones y decisiones

### Threat Intelligence:
- **IOC (Indicators of Compromise)**: IPs, hashes, dominios maliciosos
- **TTP (Tactics, Techniques, Procedures)**: Metodos de los atacantes
- **Feeds**: Listas de IOCs actualizadas (AlienVault OTX, VirusTotal)

### Herramientas del analista SOC:
- SIEM (Splunk, ELK, Sentinel)
- EDR (CrowdStrike, Carbon Black, SentinelOne)
- Threat Intelligence (MISP, OTX)
- Ticketing (Jira, TheHive)
- Sandbox (Any.run, VirusTotal)""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Un analista Tier 1 del SOC recibe una alerta. Cual es su primera accion?",
                                "options": ["Bloquear la IP inmediatamente", "Verificar si es un falso positivo", "Escalar a Tier 3", "Reiniciar el servidor"],
                                "correct": 1,
                                "explanation": "El triage inicial del Tier 1 comienza verificando si la alerta es un falso positivo antes de tomar acciones o escalar."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "MTTD significa Mean Time to ___",
                                "correct": "Detect",
                                "explanation": "MTTD (Mean Time to Detect) mide el tiempo promedio que tarda el SOC en detectar un incidente de seguridad."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    "networking": {
        "id": "networking",
        "title": "Redes y Networking",
        "description": "Domina los fundamentos de redes: modelo OSI, TCP/IP, subnetting y protocolos esenciales.",
        "icon": "network",
        "color": "#4caf50",
        "modules": [
            {
                "id": "m1",
                "title": "Fundamentos de Redes",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Modelo OSI y TCP/IP",
                        "theory": """## Modelos de Red

### Modelo OSI (7 capas):
| # | Capa | Funcion | Protocolo/Ejemplo |
|---|------|---------|-------------------|
| 7 | Aplicacion | Interfaz con usuario | HTTP, FTP, DNS, SMTP |
| 6 | Presentacion | Formato de datos | SSL/TLS, JPEG, ASCII |
| 5 | Sesion | Gestion de sesiones | NetBIOS, RPC |
| 4 | Transporte | Entrega extremo a extremo | TCP, UDP |
| 3 | Red | Enrutamiento | IP, ICMP, ARP |
| 2 | Enlace de Datos | Acceso al medio | Ethernet, WiFi, MAC |
| 1 | Fisica | Transmision de bits | Cables, senales, voltaje |

**Mnemotecnico**: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing

### Modelo TCP/IP (4 capas):
| Capa TCP/IP | Capas OSI equivalentes |
|-------------|----------------------|
| Aplicacion | 7, 6, 5 |
| Transporte | 4 |
| Internet | 3 |
| Acceso a Red | 2, 1 |

### TCP vs UDP:
| Caracteristica | TCP | UDP |
|----------------|-----|-----|
| Conexion | Orientado a conexion | Sin conexion |
| Fiabilidad | Garantiza entrega | No garantiza |
| Orden | Mantiene orden | Sin orden |
| Velocidad | Mas lento | Mas rapido |
| Uso | Web, email, SSH | DNS, VoIP, streaming |

### Three-Way Handshake (TCP):
```
Cliente  -->  SYN       -->  Servidor
Cliente  <--  SYN-ACK   <--  Servidor
Cliente  -->  ACK       -->  Servidor
(Conexion establecida)
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "En que capa del modelo OSI opera un router?",
                                "options": ["Capa 1 - Fisica", "Capa 2 - Enlace de Datos", "Capa 3 - Red", "Capa 4 - Transporte"],
                                "correct": 2,
                                "explanation": "Los routers operan en la Capa 3 (Red) porque toman decisiones de enrutamiento basadas en direcciones IP."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Que protocolo usarias para streaming de video donde la velocidad es mas importante que la fiabilidad?",
                                "options": ["TCP", "UDP", "ICMP", "ARP"],
                                "correct": 1,
                                "explanation": "UDP es preferido para streaming porque no tiene la sobrecarga de TCP. Perder algunos paquetes es aceptable en video/audio."
                            },
                            {
                                "id": "e3",
                                "type": "fill_blank",
                                "question": "El proceso de establecimiento de conexion TCP se llama ___-Way Handshake",
                                "correct": "Three",
                                "explanation": "El Three-Way Handshake establece una conexion TCP mediante tres pasos: SYN, SYN-ACK, ACK."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m2",
                "title": "Direccionamiento IP",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "IPv4 y Subnetting",
                        "theory": """## Direccionamiento IPv4

### Estructura de una IP:
Una direccion IPv4 tiene 32 bits divididos en 4 octetos:
```
192.168.1.100
11000000.10101000.00000001.01100100
```

### Clases de IP:
| Clase | Rango | Mascara por defecto | Redes privadas |
|-------|-------|---------------------|----------------|
| A | 1.0.0.0 - 126.x.x.x | 255.0.0.0 (/8) | 10.0.0.0/8 |
| B | 128.0.0.0 - 191.x.x.x | 255.255.0.0 (/16) | 172.16.0.0/12 |
| C | 192.0.0.0 - 223.x.x.x | 255.255.255.0 (/24) | 192.168.0.0/16 |

### Subnetting:
Dividir una red grande en subredes mas pequenas.

**Ejemplo: 192.168.1.0/24 dividida en 4 subredes (/26)**
```
Subred 1: 192.168.1.0/26   (hosts: .1 - .62, broadcast: .63)
Subred 2: 192.168.1.64/26  (hosts: .65 - .126, broadcast: .127)
Subred 3: 192.168.1.128/26 (hosts: .129 - .190, broadcast: .191)
Subred 4: 192.168.1.192/26 (hosts: .193 - .254, broadcast: .255)
```

### Calcular hosts por subred:
```
Hosts utilizables = 2^(32 - prefijo) - 2

/24 = 2^8 - 2 = 254 hosts
/26 = 2^6 - 2 = 62 hosts
/28 = 2^4 - 2 = 14 hosts
/30 = 2^2 - 2 = 2 hosts (para enlaces punto a punto)
```

### IPs especiales:
- `127.0.0.1` - Loopback (localhost)
- `0.0.0.0` - Todas las interfaces
- `255.255.255.255` - Broadcast global
- `169.254.x.x` - APIPA (autoasignacion)""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Cuantos hosts utilizables tiene una red /26?",
                                "options": ["26", "64", "62", "30"],
                                "correct": 2,
                                "explanation": "Una red /26 tiene 2^6 = 64 direcciones, menos la de red y broadcast = 62 hosts utilizables."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Cual de estas es una IP privada?",
                                "options": ["8.8.8.8", "192.168.1.1", "200.100.50.25", "1.1.1.1"],
                                "correct": 1,
                                "explanation": "192.168.1.1 pertenece al rango privado 192.168.0.0/16 (Clase C). Las otras son IPs publicas."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m3",
                "title": "Protocolos Esenciales",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "DNS, DHCP, ARP y HTTP",
                        "theory": """## Protocolos Esenciales

### DNS (Domain Name System) - Puerto 53:
Traduce nombres de dominio a direcciones IP.
```
Navegador: "Cual es la IP de google.com?"
DNS: "142.250.185.78"
```

**Tipos de registros DNS:**
| Tipo | Funcion |
|------|---------|
| A | Dominio -> IPv4 |
| AAAA | Dominio -> IPv6 |
| CNAME | Alias de dominio |
| MX | Servidor de correo |
| NS | Servidor DNS autoritativo |
| TXT | Texto (SPF, DKIM) |
| PTR | IP -> Dominio (inverso) |

**Comandos DNS:**
```bash
nslookup google.com
dig google.com
dig -x 8.8.8.8  # Reverse lookup
```

### DHCP (Dynamic Host Configuration Protocol):
Asigna IPs automaticamente. Proceso DORA:
1. **D**iscover: Cliente busca servidor DHCP
2. **O**ffer: Servidor ofrece una IP
3. **R**equest: Cliente acepta la oferta
4. **A**ck: Servidor confirma la asignacion

### ARP (Address Resolution Protocol):
Traduce IP a direccion MAC (capa 2).
```bash
arp -a              # Ver tabla ARP
arping 192.168.1.1  # Resolver IP a MAC
```

### HTTP/HTTPS:
| Metodo | Descripcion |
|--------|-------------|
| GET | Obtener recurso |
| POST | Enviar datos |
| PUT | Actualizar recurso |
| DELETE | Eliminar recurso |

**Codigos de estado:**
- 200: OK
- 301: Redireccion permanente
- 403: Prohibido
- 404: No encontrado
- 500: Error del servidor""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "fill_blank",
                                "question": "El proceso de asignacion de IP por DHCP sigue las fases D-O-R-A. La D significa ___",
                                "correct": "Discover",
                                "explanation": "DORA: Discover (descubrir), Offer (ofrecer), Request (solicitar), Acknowledge (confirmar). El cliente envia un Discover para encontrar servidores DHCP."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "Que registro DNS usarias para encontrar el servidor de correo de un dominio?",
                                "options": ["A", "CNAME", "MX", "PTR"],
                                "correct": 2,
                                "explanation": "El registro MX (Mail Exchange) indica que servidor se encarga de recibir correos para un dominio."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m4",
                "title": "Escaneo y Reconocimiento",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Nmap y reconocimiento de red",
                        "theory": """## Escaneo de Red con Nmap

### Que es Nmap?
Network Mapper: herramienta de escaneo de red para descubrir hosts, puertos y servicios.

**IMPORTANTE**: Solo usar en redes propias o con autorizacion explicita.

### Escaneos basicos:
```bash
# Ping sweep (descubrir hosts activos)
nmap -sn 192.168.1.0/24

# Escaneo de puertos TCP (SYN scan - rapido)
nmap -sS 192.168.1.100

# Escaneo de puertos TCP completo
nmap -sT 192.168.1.100

# Escaneo de todos los puertos
nmap -p- 192.168.1.100

# Escaneo de puertos especificos
nmap -p 22,80,443,3389 192.168.1.100

# Deteccion de version de servicios
nmap -sV 192.168.1.100

# Deteccion de sistema operativo
nmap -O 192.168.1.100

# Escaneo agresivo (OS + version + scripts + traceroute)
nmap -A 192.168.1.100
```

### Puertos comunes:
| Puerto | Servicio | Uso |
|--------|----------|-----|
| 21 | FTP | Transferencia de archivos |
| 22 | SSH | Acceso remoto seguro |
| 23 | Telnet | Acceso remoto (inseguro) |
| 25 | SMTP | Envio de correo |
| 53 | DNS | Resolucion de nombres |
| 80 | HTTP | Web |
| 443 | HTTPS | Web segura |
| 3306 | MySQL | Base de datos |
| 3389 | RDP | Escritorio remoto Windows |

### Scripts de Nmap (NSE):
```bash
# Scripts de vulnerabilidades
nmap --script vuln 192.168.1.100

# Scripts de descubrimiento
nmap --script discovery 192.168.1.100

# Script especifico
nmap --script http-headers 192.168.1.100
```

### Guardar resultados:
```bash
nmap -oN resultado.txt 192.168.1.100    # Normal
nmap -oX resultado.xml 192.168.1.100    # XML
nmap -oG resultado.gnmap 192.168.1.100  # Grepable
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Que flag de Nmap se usa para detectar la version de los servicios?",
                                "options": ["-sS", "-sV", "-O", "-sn"],
                                "correct": 1,
                                "explanation": "El flag -sV activa la deteccion de version, que intenta determinar que software y version esta corriendo en cada puerto abierto."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "El puerto estandar para SSH es el ___",
                                "correct": "22",
                                "explanation": "SSH (Secure Shell) utiliza el puerto 22 por defecto. Es el metodo seguro para acceso remoto a servidores."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    "linux": {
        "id": "linux",
        "title": "Linux y SysAdmin",
        "description": "Domina Linux desde la linea de comandos hasta la administracion de servidores y automatizacion.",
        "icon": "terminal",
        "color": "#ff9800",
        "modules": [
            {
                "id": "m1",
                "title": "Introduccion a Linux",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Linux basico y la terminal",
                        "theory": """## Introduccion a Linux

### Por que Linux para ciberseguridad?
- La mayoria de servidores web usan Linux
- Herramientas de seguridad nativas (nmap, tcpdump, etc.)
- Control total del sistema
- Open source (puedes auditar el codigo)
- Distribuciones especializadas (Kali, Parrot, Security Onion)

### Distribuciones populares:
| Distro | Base | Uso |
|--------|------|-----|
| Ubuntu | Debian | General, servidores |
| Kali Linux | Debian | Pentesting |
| CentOS/Rocky | RHEL | Servidores empresariales |
| Parrot OS | Debian | Seguridad |
| Security Onion | Ubuntu | Blue Team/SOC |

### Estructura del sistema de archivos:
```
/          Raiz del sistema
/home      Directorios de usuarios
/etc       Archivos de configuracion
/var       Datos variables (logs, bases de datos)
/tmp       Archivos temporales
/opt       Software opcional
/bin       Binarios esenciales
/sbin      Binarios del sistema
/usr       Programas del usuario
/dev       Dispositivos
/proc      Informacion del kernel
/root      Home del usuario root
```

### Comandos basicos de navegacion:
```bash
pwd                  # Directorio actual
ls                   # Listar archivos
ls -la               # Listar con detalles y ocultos
cd /var/log          # Cambiar directorio
cd ..                # Subir un nivel
cd ~                 # Ir al home
mkdir carpeta        # Crear directorio
rmdir carpeta        # Eliminar directorio vacio
rm -r carpeta        # Eliminar directorio con contenido
cp origen destino    # Copiar
mv origen destino    # Mover/renombrar
touch archivo.txt    # Crear archivo vacio
cat archivo.txt      # Ver contenido
less archivo.txt     # Ver con paginacion
head -n 20 archivo   # Primeras 20 lineas
tail -f /var/log/syslog  # Seguir log en tiempo real
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Donde se almacenan los archivos de configuracion del sistema en Linux?",
                                "options": ["/home", "/etc", "/var", "/opt"],
                                "correct": 1,
                                "explanation": "El directorio /etc contiene los archivos de configuracion del sistema y de las aplicaciones instaladas."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "El comando para ver un log en tiempo real es: tail ___ /var/log/syslog",
                                "correct": "-f",
                                "explanation": "El flag -f (follow) hace que tail muestre nuevas lineas a medida que se agregan al archivo, ideal para monitorear logs en tiempo real."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "Que distribucion de Linux esta especializada en Blue Team y operaciones SOC?",
                                "options": ["Kali Linux", "Ubuntu", "Security Onion", "Arch Linux"],
                                "correct": 2,
                                "explanation": "Security Onion viene preconfigurada con herramientas de monitoreo, IDS/IPS y analisis de trafico orientadas a operaciones Blue Team y SOC."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m2",
                "title": "Usuarios y Permisos",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Gestion de usuarios y permisos",
                        "theory": """## Usuarios y Permisos en Linux

### Gestion de usuarios:
```bash
# Crear usuario
sudo useradd -m -s /bin/bash usuario

# Establecer contrasena
sudo passwd usuario

# Eliminar usuario
sudo userdel -r usuario

# Agregar a grupo
sudo usermod -aG grupo usuario

# Ver grupos del usuario
groups usuario
id usuario

# Cambiar a otro usuario
su - usuario

# Ejecutar como root
sudo comando
```

### Permisos de archivos:
```
-rwxr-xr-- 1 usuario grupo 4096 Jan 15 10:30 archivo.txt

Tipo: - (archivo) d (directorio) l (enlace)
Owner:  rwx (lectura, escritura, ejecucion)
Group:  r-x (lectura, ejecucion)
Others: r-- (solo lectura)
```

### Notacion numerica:
| Permiso | Valor |
|---------|-------|
| r (read) | 4 |
| w (write) | 2 |
| x (execute) | 1 |

```bash
chmod 755 archivo    # rwxr-xr-x
chmod 644 archivo    # rw-r--r--
chmod 700 archivo    # rwx------
chmod 600 archivo    # rw-------

# Cambiar propietario
chown usuario:grupo archivo
chown -R usuario:grupo directorio/

# Cambiar grupo
chgrp grupo archivo
```

### Permisos especiales:
```bash
# SUID - Ejecuta con permisos del propietario
chmod u+s programa
# Ejemplo: /usr/bin/passwd tiene SUID

# SGID - Hereda grupo del directorio
chmod g+s directorio

# Sticky Bit - Solo el propietario puede borrar
chmod +t /tmp
```

### Archivos importantes de seguridad:
```
/etc/passwd     - Informacion de usuarios
/etc/shadow     - Hashes de contrasenas
/etc/group      - Grupos del sistema
/etc/sudoers    - Configuracion de sudo
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Que permisos numericos representan rwxr-xr--?",
                                "options": ["644", "754", "755", "744"],
                                "correct": 1,
                                "explanation": "rwx=4+2+1=7, r-x=4+0+1=5, r--=4+0+0=4. Resultado: 754"
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "El archivo que contiene los hashes de las contrasenas en Linux es ___",
                                "correct": "/etc/shadow",
                                "explanation": "/etc/shadow almacena los hashes de las contrasenas de los usuarios. Solo root puede leerlo (permisos 640)."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m3",
                "title": "Shell Scripting",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Bash scripting basico",
                        "theory": """## Shell Scripting con Bash

### Tu primer script:
```bash
#!/bin/bash
# Mi primer script
echo "Hola, soy un script de Bash!"
```

```bash
chmod +x script.sh   # Dar permisos de ejecucion
./script.sh          # Ejecutar
```

### Variables:
```bash
nombre="Carlos"
edad=25
echo "Me llamo $nombre y tengo $edad anios"
echo "Home: $HOME"
echo "Usuario: $USER"
```

### Entrada del usuario:
```bash
read -p "Ingresa tu nombre: " nombre
echo "Hola, $nombre"
```

### Condicionales:
```bash
#!/bin/bash
read -p "Ingresa un numero: " num

if [ $num -gt 0 ]; then
    echo "Positivo"
elif [ $num -lt 0 ]; then
    echo "Negativo"
else
    echo "Cero"
fi
```

### Operadores de comparacion:
| Numerico | String | Significado |
|----------|--------|-------------|
| -eq | = | Igual |
| -ne | != | Diferente |
| -gt | | Mayor que |
| -lt | | Menor que |
| -ge | | Mayor o igual |
| -le | | Menor o igual |

### Bucles:
```bash
# For loop
for i in 1 2 3 4 5; do
    echo "Numero: $i"
done

# For con rango
for i in $(seq 1 10); do
    echo $i
done

# While loop
contador=0
while [ $contador -lt 5 ]; do
    echo "Contador: $contador"
    ((contador++))
done
```

### Script de seguridad (ejemplo):
```bash
#!/bin/bash
# Escaneo rapido de puertos abiertos
echo "=== Puertos abiertos en localhost ==="
for port in 22 80 443 3306 8080; do
    (echo >/dev/tcp/localhost/$port) 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "[OPEN] Puerto $port"
    fi
done
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Que linea debe ir al inicio de todo script Bash?",
                                "options": ["#!bash", "#!/bin/bash", "//bin/bash", "@bash"],
                                "correct": 1,
                                "explanation": "#!/bin/bash es el 'shebang' que indica al sistema que interprete usar para ejecutar el script."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "Para dar permisos de ejecucion a un script se usa: chmod ___ script.sh",
                                "correct": "+x",
                                "explanation": "chmod +x agrega el permiso de ejecucion al script, permitiendo ejecutarlo con ./script.sh"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m4",
                "title": "Servicios y Redes en Linux",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Servicios, procesos y red",
                        "theory": """## Servicios, Procesos y Red en Linux

### Gestion de servicios (systemd):
```bash
# Ver estado de un servicio
sudo systemctl status ssh

# Iniciar/detener/reiniciar servicio
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx

# Habilitar al inicio
sudo systemctl enable ssh

# Ver todos los servicios
sudo systemctl list-units --type=service
```

### Gestion de procesos:
```bash
# Ver procesos
ps aux
ps aux | grep nginx

# Monitor en tiempo real
top
htop

# Matar proceso
kill PID
kill -9 PID          # Forzar
killall nombre_proceso

# Procesos en segundo plano
comando &            # Ejecutar en background
jobs                 # Ver trabajos
fg %1                # Traer al frente
bg %1                # Enviar al fondo
```

### Comandos de red:
```bash
# Configuracion de red
ip addr show
ip route show
ifconfig             # Legacy

# Conexiones activas
ss -tuln             # TCP/UDP listening
netstat -antup       # Legacy

# Pruebas de conectividad
ping 8.8.8.8
traceroute google.com
mtr google.com       # Ping + traceroute

# DNS
dig google.com
nslookup google.com
host google.com

# Transferencia
curl -I https://example.com  # Solo headers
wget https://example.com/file.zip
```

### Firewall con UFW (Ubuntu):
```bash
sudo ufw status
sudo ufw enable
sudo ufw allow 22/tcp       # Permitir SSH
sudo ufw allow 80/tcp       # Permitir HTTP
sudo ufw deny 23/tcp        # Bloquear Telnet
sudo ufw allow from 192.168.1.0/24  # Permitir subred
sudo ufw delete allow 80/tcp
```

### Logs del sistema:
```bash
# Logs principales
/var/log/syslog      # Log general
/var/log/auth.log    # Autenticacion
/var/log/kern.log    # Kernel
/var/log/apache2/    # Apache web server

# Ver logs con journalctl
journalctl -u ssh    # Logs de SSH
journalctl -f        # Seguir en tiempo real
journalctl --since "1 hour ago"
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Que comando muestra las conexiones de red activas y puertos en escucha?",
                                "options": ["ps aux", "ss -tuln", "top", "df -h"],
                                "correct": 1,
                                "explanation": "ss -tuln muestra sockets TCP/UDP (-tu) en estado listening (-l) con numeros de puerto (-n)."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "El log de autenticacion en Ubuntu se encuentra en ___",
                                "correct": "/var/log/auth.log",
                                "explanation": "/var/log/auth.log registra todos los eventos de autenticacion: logins exitosos, fallidos, uso de sudo, etc."
                            }
                        ]
                    }
                ]
            }
        ]
    }
    ,

    "osint": {
        "id": "osint",
        "title": "OSINT & Threat Intelligence",
        "description": "Domina la inteligencia de fuentes abiertas para defender organizaciones. Aprende a rastrear amenazas, analizar IOCs y usar threat intelligence como un profesional Blue Team.",
        "icon": "search",
        "color": "#8b5cf6",
        "modules": [
            {
                "id": "m1",
                "title": "Fundamentos de OSINT",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Que es OSINT y por que importa en ciberseguridad",
                        "theory": """## OSINT: Open Source Intelligence

OSINT es la recopilacion y analisis de informacion de fuentes publicamente disponibles para producir inteligencia accionable.

### Fuentes de OSINT
- **Internet abierto**: paginas web, foros, blogs, redes sociales
- **Registros publicos**: WHOIS, registros DNS, certificados SSL
- **Bases de datos publicas**: Shodan, Censys, GreyNoise
- **Dark Web**: foros clandestinos, mercados (con precaucion legal)
- **Codigo fuente**: GitHub, GitLab, Pastebin

### OSINT en Blue Team
En defensa, OSINT se usa para:
1. **Threat Intelligence**: entender que atacantes apuntan a tu industria
2. **Attack Surface Management**: descubrir que expone tu organizacion
3. **Incident Response**: identificar la infraestructura del atacante
4. **Vulnerability Research**: encontrar sistemas expuestos antes que el atacante

### OSINT vs HUMINT vs SIGINT
| Tipo | Fuente | Ejemplo |
| ---- | ------ | ------- |
| OSINT | Publica | Google, Shodan, redes sociales |
| HUMINT | Humana | Informantes, entrevistas |
| SIGINT | Señales | Interceptacion de comunicaciones |

### Ciclo de Inteligencia
1. **Planificacion**: definir que necesitas saber
2. **Recoleccion**: obtener datos de fuentes relevantes
3. **Procesamiento**: organizar y filtrar datos
4. **Analisis**: interpretar y encontrar patrones
5. **Diseminacion**: compartir inteligencia con quien la necesita
6. **Retroalimentacion**: evaluar si fue util""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "¿Que significa el acronimo OSINT?",
                                "options": ["Open Source Intelligence", "Online Security Investigation Tool", "Operational Security Insight", "Open Systems Internet"],
                                "correct": 0,
                                "explanation": "OSINT = Open Source Intelligence. 'Open Source' no se refiere a software, sino a informacion de fuentes publicas y abiertas."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "¿Cual de estas herramientas es tipicamente usada para OSINT de dispositivos conectados a internet?",
                                "options": ["Nmap", "Shodan", "Metasploit", "John the Ripper"],
                                "correct": 1,
                                "explanation": "Shodan es un motor de busqueda para dispositivos conectados a internet. Indexa servidores, camaras, routers y otros dispositivos con sus puertos y servicios abiertos."
                            },
                            {
                                "id": "e3",
                                "type": "fill_blank",
                                "question": "El ciclo de inteligencia tiene 6 fases. La primera es ___ y la ultima es ___. (formato: primera/ultima)",
                                "correct": "planificacion/retroalimentacion",
                                "explanation": "El ciclo comienza con Planificacion (definir objetivos) y termina con Retroalimentacion (evaluar si la inteligencia fue util para mejorar el proceso)."
                            }
                        ]
                    },
                    {
                        "id": "l2",
                        "title": "Busquedas avanzadas con Google Dorks",
                        "theory": """## Google Dorks: Busqueda Avanzada para Inteligencia

Los Google Dorks son operadores de busqueda avanzada que permiten encontrar informacion especifica que no aparece en busquedas normales.

### Operadores Fundamentales

| Operador | Funcion | Ejemplo |
| -------- | ------- | ------- |
| `site:` | Limita a un dominio | `site:empresa.com` |
| `filetype:` | Busca tipo de archivo | `filetype:pdf` |
| `intitle:` | Texto en el titulo | `intitle:"index of"` |
| `inurl:` | Texto en la URL | `inurl:admin` |
| `intext:` | Texto en el contenido | `intext:password` |
| `cache:` | Version cacheada | `cache:sitio.com` |

### Dorks de Reconocimiento (Blue Team los usa para proteger)
```
# Archivos de configuracion expuestos
site:empresa.com filetype:env
site:empresa.com filetype:conf
site:empresa.com filetype:xml intext:password

# Paneles de administracion expuestos
site:empresa.com inurl:admin
site:empresa.com inurl:login intitle:"Admin Panel"

# Listados de directorios
site:empresa.com intitle:"index of" "parent directory"

# Documentos sensibles
site:empresa.com filetype:pdf "confidential"
site:empresa.com filetype:xlsx "internal use only"
```

### Uso Etico
Los Google Dorks en Blue Team se usan para:
- **Attack Surface Assessment**: descubrir que expone tu propia organizacion
- **Verificacion de exposicion**: asegurarse de que datos sensibles no esten indexados
- **Threat Intelligence**: buscar menciones de tu organizacion en contextos maliciosos

**IMPORTANTE**: Solo usar en dominios y sistemas de los que tienes autorizacion.""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "¿Que operador de Google Dork usarias para buscar archivos .pdf en el sitio ejemplo.com?",
                                "options": ["site:ejemplo.com type:pdf", "site:ejemplo.com filetype:pdf", "domain:ejemplo.com file:pdf", "from:ejemplo.com ext:pdf"],
                                "correct": 1,
                                "explanation": "La sintaxis correcta es: site:ejemplo.com filetype:pdf. El operador 'site:' limita al dominio y 'filetype:' filtra por extension."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "Para buscar paneles de login en un sitio, el dork seria: site:victima.com inurl:___",
                                "correct": "login",
                                "explanation": "inurl:login busca paginas cuya URL contenga la palabra 'login'. Tambien se puede usar inurl:admin, inurl:wp-admin, inurl:dashboard, etc."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "¿Para que usa el Blue Team los Google Dorks en su organizacion?",
                                "options": ["Para atacar competidores", "Para encontrar informacion expuesta de su propia organizacion antes que los atacantes", "Para hackear bases de datos", "Para evitar pagar por herramientas de seguridad"],
                                "correct": 1,
                                "explanation": "El Blue Team usa Google Dorks defensivamente: para encontrar lo que su organizacion expone inadvertidamente en internet (archivos de configuracion, credenciales, paneles de admin) antes de que los atacantes lo encuentren."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m2",
                "title": "Threat Intelligence y IOCs",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Indicadores de Compromiso (IOCs) y como usarlos",
                        "theory": """## Indicadores de Compromiso (IOCs)

Los IOCs son artefactos forenses que indican con alta probabilidad que un sistema ha sido comprometido o esta siendo atacado.

### Tipos de IOCs

**Basados en Red:**
- Direcciones IP maliciosas
- Dominios maliciosos
- URLs de C2 (Command & Control)
- Hash de certificados SSL maliciosos
- User-Agents especificos de malware

**Basados en Host:**
- Hashes de archivos maliciosos (MD5, SHA1, SHA256)
- Nombres de archivos y rutas
- Claves de registro maliciosas
- Nombres de servicios o procesos maliciosos
- Artefactos de persistencia

**Basados en Comportamiento:**
- Patrones de trafico de red (beacons)
- Tecnicas de inyeccion de procesos
- Metodos de persistencia
- Tecnicas de evasion de defensa

### Piramide del Dolor (David Bianco)
La Piramide del Dolor clasifica IOCs por el dolor que causa al atacante bloquearlos:

```
    /\\
   /  \\  TTPs (Tacticas, Tecnicas, Procedimientos)  <- MAS DIFICIL cambiar
  /----\\
 / Tools \\  Herramientas del atacante
/--------\\
/ Network \\ Artefactos de red
/----------\\
/   Domain  \\ Nombres de dominio
/------------\\
/    IP Addr  \\ Direcciones IP                       <- FACIL cambiar
/--------------\\
```

### Fuentes de Threat Intelligence
- **AlienVault OTX**: feeds de IOCs de la comunidad
- **VirusTotal**: analisis de archivos e IOCs
- **Shodan**: dispositivos y servicios expuestos
- **AbuseIPDB**: IPs reportadas como maliciosas
- **MISP**: plataforma de sharing de threat intel
- **MITRE ATT&CK**: base de datos de TTPs de atacantes""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Segun la Piramide del Dolor, ¿que tipo de IOC causa MAS dificultad al atacante cuando es bloqueado?",
                                "options": ["Direcciones IP", "Dominios maliciosos", "Hashes de archivos", "TTPs (Tacticas, Tecnicas y Procedimientos)"],
                                "correct": 3,
                                "explanation": "Las TTPs estan en la cima de la piramide porque son los comportamientos y metodos del atacante. Cambiar una IP o dominio es trivial, pero cambiar sus metodos operativos requiere mucho mas esfuerzo y recursos."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "¿Cual de estos es un IOC basado en HOST?",
                                "options": ["Una direccion IP de C2", "El hash SHA256 de un archivo malicioso", "Un dominio de phishing", "Un patron de trafico de red"],
                                "correct": 1,
                                "explanation": "El hash SHA256 de un archivo es un IOC basado en host porque se encuentra en el sistema de archivos del equipo comprometido. Los hashes son inmutables: si cambias un bit del archivo, cambia el hash."
                            },
                            {
                                "id": "e3",
                                "type": "fill_blank",
                                "question": "La base de datos de TTPs de atacantes mantenida por MITRE se llama MITRE ___",
                                "correct": "ATT&CK",
                                "explanation": "MITRE ATT&CK (Adversarial Tactics, Techniques & Common Knowledge) es la base de datos mas completa de comportamientos de atacantes del mundo. Es esencial para el Blue Team."
                            }
                        ]
                    },
                    {
                        "id": "l2",
                        "title": "Herramientas OSINT: Shodan, VirusTotal y WHOIS",
                        "theory": """## Herramientas OSINT Esenciales para Blue Team

### Shodan
Shodan es el motor de busqueda para dispositivos conectados a internet.

**Uso en Blue Team:**
```bash
# Buscar tu organizacion en Shodan
org:"Mi Empresa S.A."

# Buscar servicios en un rango de IPs
net:203.0.113.0/24

# Buscar servicios vulnerables
product:"Apache httpd" version:"2.2"

# Buscar camaras expuestas
port:554 has_screenshot:true
```

**Que buscar:**
- Servidores con puertos innecesarios abiertos
- Servicios con versiones vulnerables
- Paneles de administracion expuestos a internet
- Credenciales por defecto en dispositivos IoT

### VirusTotal
Plataforma para analisis de archivos, URLs, dominios e IPs.

**Uso en Blue Team:**
- Subir archivo sospechoso para analisis con 70+ antivirus
- Verificar si una IP esta reportada como maliciosa
- Analizar dominios: cuando fue visto, que malware usa ese dominio
- Buscar por hash de archivo para encontrar variantes conocidas

**API de VirusTotal (Python):**
```python
import requests
API_KEY = "tu_api_key"
url = f"https://www.virustotal.com/api/v3/files/HASH"
headers = {"x-apikey": API_KEY}
response = requests.get(url, headers=headers)
data = response.json()
detections = data["data"]["attributes"]["last_analysis_stats"]
print(f"Malicioso: {detections['malicious']}/72")
```

### WHOIS y DNS Recon
```bash
# Informacion del dominio
whois ejemplo.com

# Registros DNS
dig ejemplo.com ANY
nslookup -type=MX ejemplo.com

# Historial DNS (pasivo)
# Usar: SecurityTrails, PassiveTotal, DNSDumpster

# Certificados SSL (pueden revelar subdominios)
# Usar: crt.sh -> site:%.empresa.com
```

### Maltego (Grafico de relaciones)
Maltego permite visualizar relaciones entre:
- Dominios, IPs, emails, nombres de personas
- Ideal para mapear la infraestructura de un atacante
- Conecta datos de multiples fuentes OSINT""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "¿Para que se usa principalmente Shodan en Blue Team?",
                                "options": ["Para hackear servidores remotos", "Para descubrir que servicios y dispositivos de tu organizacion estan expuestos en internet", "Para enviar emails de phishing", "Para analizar malware"],
                                "correct": 1,
                                "explanation": "El Blue Team usa Shodan para ver su organizacion desde los ojos del atacante: que puertos, servicios y versiones son visibles publicamente, permitiendo corregir exposiciones antes de ser explotadas."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "Para buscar todos los subdominios de empresa.com usando certificados SSL en crt.sh, la busqueda seria: site:___.empresa.com",
                                "correct": "%",
                                "explanation": "En crt.sh, el wildcard % reemplaza cualquier subdominio. La busqueda '%.empresa.com' retorna todos los certificados SSL emitidos para subdominios de empresa.com, revelando subdominios no documentados."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "¿Que informacion proporciona VirusTotal sobre un hash de archivo?",
                                "options": ["Solo si el archivo es ejecutable", "Resultados de analisis de 70+ motores antivirus y metadata del archivo", "El codigo fuente del malware", "La clave de descifrado del malware"],
                                "correct": 1,
                                "explanation": "VirusTotal agrega resultados de mas de 70 motores antivirus y herramientas de analisis, proporcionando detecciones, comportamientos, relaciones con otros artefactos, primera vez visto, y mucho mas."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m3",
                "title": "Reconocimiento Pasivo",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Mapeo de Superficie de Ataque",
                        "theory": """## Attack Surface Management (ASM)

La superficie de ataque es todo lo que un atacante puede ver, acceder e intentar comprometer de tu organizacion.

### Componentes de la Superficie de Ataque

**Externa (lo que ve internet):**
- Sitios web y aplicaciones publicas
- APIs expuestas
- Servidores de correo (MX records)
- VPNs y acceso remoto
- Subdominios olvidados
- Certificados SSL/TLS
- Puertos y servicios abiertos

**Humana:**
- Empleados con emails corporativos expuestos
- Cuentas de redes sociales corporativas
- Informacion en LinkedIn (estructura organizacional)
- Datos en filtraciones publicas (HaveIBeenPwned)

**Codigo y datos:**
- Repositorios publicos de GitHub con credenciales
- Documentos publicos con metadata sensible
- Archivos de backup expuestos

### Proceso de ASM

```
1. Descubrimiento de activos
   - Enumeracion de subdominios
   - Escaneo de rangos IP propios
   - Busqueda en Shodan/Censys

2. Fingerprinting
   - Identificar tecnologias usadas
   - Versiones de software
   - CMS, frameworks, servidores

3. Analisis de vulnerabilidades
   - CVEs conocidos para las versiones detectadas
   - Configuraciones incorrectas
   - Datos expuestos inadvertidamente

4. Priorizacion y remediacion
   - Severidad del riesgo
   - Facilidad de explotacion
   - Plan de correccion
```

### Herramientas para ASM
- **Amass**: enumeracion de subdominios
- **theHarvester**: recoleccion de emails, dominios, IPs
- **Recon-ng**: framework de reconocimiento modular
- **SpiderFoot**: automatizacion de OSINT
- **Censys**: similar a Shodan con datos adicionales""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "Un subdominio 'test.empresa.com' que apunta a un servidor olvidado con software desactualizado es un ejemplo de:",
                                "options": ["Un honeypot", "Una superficie de ataque descuidada", "Un sistema de monitoreo", "Un servidor de desarrollo seguro"],
                                "correct": 1,
                                "explanation": "Los subdominios olvidados (Shadow IT) son superficies de ataque comunes. Los atacantes los buscan porque suelen tener software desactualizado, parches sin aplicar y menos monitoreo que los sistemas principales."
                            },
                            {
                                "id": "e2",
                                "type": "multiple_choice",
                                "question": "¿Por que es importante revisar los repositorios publicos de GitHub de tu organizacion?",
                                "options": ["Para copiar codigo de competidores", "Para verificar que no haya credenciales, API keys o configuraciones sensibles expuestas accidentalmente", "Para reclutar desarrolladores", "GitHub no es relevante para ciberseguridad"],
                                "correct": 1,
                                "explanation": "Es muy comun que desarrolladores suban accidentalmente API keys, contrasenas de bases de datos, credenciales de AWS, etc. a repositorios publicos. Herramientas como truffleHog o GitLeaks buscan estos secretos automaticamente."
                            },
                            {
                                "id": "e3",
                                "type": "fill_blank",
                                "question": "El sitio web ___ permite verificar si un email fue comprometido en filtraciones de datos publicas",
                                "correct": "HaveIBeenPwned",
                                "explanation": "HaveIBeenPwned (haveibeenpwned.com) de Troy Hunt es la referencia para verificar si un email aparece en filtraciones de datos publicas. Esencial para evaluar riesgo de credenciales comprometidas."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    "python-sec": {
        "id": "python-sec",
        "title": "Python para Ciberseguridad",
        "description": "Aprende Python enfocado en automatizar tareas de seguridad: analisis de logs, escaneo de redes, analisis de malware, desarrollo de herramientas y scripting para Blue Team.",
        "icon": "terminal",
        "color": "#06b6d4",
        "modules": [
            {
                "id": "m1",
                "title": "Python Basico para Seguridad",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Por que Python es esencial en ciberseguridad",
                        "theory": """## Python en Ciberseguridad

Python es el lenguaje preferido en ciberseguridad por su simplicidad, potente ecosistema de librerias y velocidad de desarrollo.

### ¿Por que Python?
- **Sintaxis simple**: prototipa herramientas rapidamente
- **Librerias especializadas**: scapy, impacket, pyshark, pwntools
- **Multiplataforma**: funciona en Windows, Linux, macOS
- **Comunidad enorme**: casi toda herramienta de seguridad tiene bindings en Python
- **Scripting**: automatiza tareas repetitivas del SOC

### Casos de uso en Blue Team
1. **Analisis de logs**: procesar millones de lineas de logs
2. **Automatizacion**: respuesta automatica a incidentes
3. **Threat Hunting**: busqueda de patrones anomalos
4. **Desarrollo de herramientas**: IDS simples, detectores de anomalias
5. **Integracion de APIs**: VirusTotal, Shodan, SIEM APIs
6. **Forense**: analisis de memoria, artefactos del sistema

### Tu primer script de seguridad
```python
import hashlib
import sys

def calcular_hash(archivo):
    '''Calcula MD5, SHA1 y SHA256 de un archivo.'''
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(archivo, 'rb') as f:
        while chunk := f.read(8192):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    print(f"Archivo: {archivo}")
    print(f"MD5:    {md5.hexdigest()}")
    print(f"SHA1:   {sha1.hexdigest()}")
    print(f"SHA256: {sha256.hexdigest()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python hasher.py <archivo>")
    else:
        calcular_hash(sys.argv[1])
```

### Entorno de desarrollo recomendado
```bash
# Instalar Python 3.10+
python --version

# Crear entorno virtual (siempre)
python -m venv venv-security
source venv-security/bin/activate  # Linux/Mac
venv-security\\Scripts\\activate   # Windows

# Librerias esenciales de seguridad
pip install requests scapy python-whois dnspython shodan
pip install pyshark yara-python pycryptodome
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "¿Que libreria de Python se usa para manipular paquetes de red a nivel bajo (crear, enviar, capturar paquetes)?",
                                "options": ["requests", "scapy", "flask", "pandas"],
                                "correct": 1,
                                "explanation": "Scapy es LA libreria de Python para manipulacion de paquetes de red. Permite crear paquetes personalizados, sniffar trafico, hacer fuzzing de protocolos y mucho mas. Es usada tanto en offensive como defensive security."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "En Python, el modulo ___ de la libreria estandar permite calcular hashes MD5, SHA256, etc.",
                                "correct": "hashlib",
                                "explanation": "hashlib es un modulo de la libreria estandar de Python que proporciona implementaciones de MD5, SHA1, SHA256, SHA512 y otros algoritmos de hash criptograficos."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "¿Por que es importante usar entornos virtuales (venv) en proyectos de seguridad?",
                                "options": ["Son obligatorios por ley", "Aislan las dependencias del proyecto evitando conflictos y manteniendo el sistema limpio", "Hacen el codigo mas rapido", "Solo los profesionales los usan"],
                                "correct": 1,
                                "explanation": "Los entornos virtuales aislan las dependencias de cada proyecto. En seguridad es especialmente importante: evitas contaminar el sistema base, controlas exactamente que librerias estan instaladas y puedes reproducir el entorno exactamente."
                            }
                        ]
                    },
                    {
                        "id": "l2",
                        "title": "Analisis de Logs con Python",
                        "theory": """## Analisis de Logs con Python

Los logs son la principal fuente de evidencia en ciberseguridad. Python permite procesar millones de lineas eficientemente.

### Lectura basica de logs
```python
# Leer un archivo de log linea por linea
with open('/var/log/auth.log', 'r') as f:
    for linea in f:
        if 'Failed password' in linea:
            print(linea.strip())
```

### Usar expresiones regulares para extraer datos
```python
import re

def parse_ssh_failures(log_file):
    '''Extrae IPs con intentos fallidos de SSH.'''
    patron = r'Failed password for \S+ from (\d+\.\d+\.\d+\.\d+)'
    conteo = {}

    with open(log_file) as f:
        for linea in f:
            match = re.search(patron, linea)
            if match:
                ip = match.group(1)
                conteo[ip] = conteo.get(ip, 0) + 1

    # Ordenar por numero de intentos (mayor primero)
    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)

resultados = parse_ssh_failures('/var/log/auth.log')
for ip, intentos in resultados:
    print(f"{ip}: {intentos} intentos fallidos")
```

### Detector de Fuerza Bruta con umbral
```python
from collections import defaultdict
from datetime import datetime
import re

UMBRAL = 10  # intentos antes de alertar

def detectar_brute_force(log_file, umbral=UMBRAL):
    patron = r'(\w+\s+\d+ \d+:\d+:\d+).*Failed password for \S+ from (\S+)'
    intentos = defaultdict(list)

    with open(log_file) as f:
        for linea in f:
            m = re.search(patron, linea)
            if m:
                timestamp, ip = m.group(1), m.group(2)
                intentos[ip].append(timestamp)

    alertas = []
    for ip, timestamps in intentos.items():
        if len(timestamps) >= umbral:
            alertas.append({
                'ip': ip,
                'intentos': len(timestamps),
                'primer_intento': timestamps[0],
                'ultimo_intento': timestamps[-1]
            })

    return alertas

for alerta in detectar_brute_force('/var/log/auth.log'):
    print(f"[ALERTA] IP {alerta['ip']}: {alerta['intentos']} intentos")
    print(f"  Desde: {alerta['primer_intento']}")
    print(f"  Hasta: {alerta['ultimo_intento']}")
```

### Analizar logs de Apache/Nginx
```python
import re
from collections import Counter

def top_attackers(access_log):
    '''Encuentra las IPs que mas peticiones 4xx generan.'''
    patron = r'(\d+\.\d+\.\d+\.\d+).+" \d{3} '
    errores_4xx = r'" 4\d{2} '
    ip_errores = []

    with open(access_log) as f:
        for linea in f:
            if re.search(errores_4xx, linea):
                m = re.search(patron, linea)
                if m:
                    ip_errores.append(m.group(1))

    return Counter(ip_errores).most_common(10)
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "En Python, ¿que modulo se usa para buscar patrones en texto (como IPs en logs)?",
                                "options": ["string", "re", "text", "grep"],
                                "correct": 1,
                                "explanation": "El modulo 're' (Regular Expressions) de Python permite buscar y extraer patrones de texto. Es fundamental para el analisis de logs donde necesitas extraer IPs, timestamps, usuarios, etc."
                            },
                            {
                                "id": "e2",
                                "type": "code_output",
                                "question": "¿Que imprime este codigo?\n```python\nimport re\nlinea = 'Failed password for root from 10.0.0.1 port 22'\nm = re.search(r'from (\\S+)', linea)\nprint(m.group(1))\n```",
                                "correct": "10.0.0.1",
                                "explanation": "re.search busca el patron 'from (\\S+)' que captura la primera secuencia sin espacios despues de 'from'. En este caso captura '10.0.0.1'."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "¿Que estructura de datos de Python es ideal para contar ocurrencias de IPs en logs?",
                                "options": ["Lista", "Tupla", "Diccionario / Counter", "Set"],
                                "correct": 2,
                                "explanation": "Un diccionario (o collections.Counter) es ideal: la IP es la clave y el conteo es el valor. Counter ademas permite encontrar los elementos mas comunes con .most_common(n)."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m2",
                "title": "Redes y Protocolos con Python",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Sockets y conexiones de red",
                        "theory": """## Programacion de Redes con Python

### Sockets basicos
```python
import socket

# Resolver un dominio a IP
ip = socket.gethostbyname('google.com')
print(f"google.com -> {ip}")

# Verificar si un puerto esta abierto
def puerto_abierto(host, puerto, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        resultado = sock.connect_ex((host, puerto))
        sock.close()
        return resultado == 0  # 0 = conectado
    except:
        return False

# Escanear puertos comunes
puertos_comunes = [21, 22, 23, 25, 53, 80, 443, 3389, 8080]
host = '192.168.1.1'

print(f"Escaneando {host}...")
for puerto in puertos_comunes:
    if puerto_abierto(host, puerto):
        print(f"  Puerto {puerto}: ABIERTO")
```

### Escaneo de puertos con threading (mas rapido)
```python
import socket
import threading
from queue import Queue

def escanear_puerto(host, puerto, resultados):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((host, puerto)) == 0:
            resultados.append(puerto)
        s.close()
    except:
        pass

def escaneo_rapido(host, inicio=1, fin=1024):
    resultados = []
    hilos = []

    for puerto in range(inicio, fin + 1):
        t = threading.Thread(
            target=escanear_puerto,
            args=(host, puerto, resultados)
        )
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    return sorted(resultados)

puertos_abiertos = escaneo_rapido('192.168.1.1', 1, 1024)
print(f"Puertos abiertos: {puertos_abiertos}")
```

### Consultas DNS con Python
```python
import dns.resolver  # pip install dnspython

def recon_dns(dominio):
    tipos = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']

    for tipo in tipos:
        try:
            respuestas = dns.resolver.resolve(dominio, tipo)
            print(f"\\n{tipo} records:")
            for r in respuestas:
                print(f"  {r}")
        except:
            pass

recon_dns('empresa.com')
```

### Banner Grabbing (identificar servicios)
```python
import socket

def grab_banner(host, puerto):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, puerto))
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        return banner
    except:
        return None

puertos_interes = [21, 22, 25, 80, 443, 3306]
for puerto in puertos_interes:
    banner = grab_banner('192.168.1.1', puerto)
    if banner:
        print(f"Puerto {puerto}: {banner[:100]}")
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "¿Que retorna socket.connect_ex() cuando logra conectarse exitosamente?",
                                "options": ["True", "1", "0", "-1"],
                                "correct": 2,
                                "explanation": "connect_ex() retorna 0 si la conexion fue exitosa (el puerto esta abierto). Retorna un codigo de error distinto de 0 si fallo. Esto es diferente a connect() que lanza una excepcion."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "Para hacer el escaneo de puertos mas rapido, se usa ___ para ejecutar multiples conexiones simultaneamente",
                                "correct": "threading",
                                "explanation": "threading permite ejecutar multiples funciones en paralelo. En escaneo de puertos, en lugar de esperar el timeout de un puerto antes de pasar al siguiente, se escanean decenas/cientos simultaneamente."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "El 'Banner Grabbing' en ciberseguridad sirve para:",
                                "options": ["Robar imagenes de sitios web", "Identificar el software y version que corre en un puerto abierto", "Enviar spam a un servidor", "Crear copias de sitios web"],
                                "correct": 1,
                                "explanation": "Banner Grabbing lee la respuesta inicial de un servicio (el 'banner') que tipicamente incluye el nombre del software y su version. Ejemplo: 'SSH-2.0-OpenSSH_8.4'. Esta informacion permite identificar versiones vulnerables."
                            }
                        ]
                    },
                    {
                        "id": "l2",
                        "title": "Analisis de paquetes con Scapy",
                        "theory": """## Scapy: Manipulacion de Paquetes de Red

Scapy es la libreria mas potente para trabajar con paquetes de red en Python.

### Instalacion y primeros pasos
```bash
pip install scapy
```

```python
from scapy.all import *

# Ver las capas de un paquete
pkt = IP(dst="8.8.8.8")/ICMP()
pkt.show()
```

### Sniffing de trafico
```python
from scapy.all import sniff, IP, TCP

def analizar_paquete(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        proto = pkt[IP].proto

        if TCP in pkt:
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
            print(f"{src}:{sport} -> {dst}:{dport} [TCP]")

# Capturar 100 paquetes en la interfaz eth0
print("Capturando trafico...")
sniff(iface="eth0", prn=analizar_paquete, count=100)
```

### Detector de escaneo de puertos
```python
from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time

conexiones = defaultdict(set)
UMBRAL_PUERTOS = 20  # si una IP toca mas de 20 puertos -> alerta

def detectar_scan(pkt):
    if TCP in pkt and IP in pkt:
        # Detectar paquetes SYN (inicio de conexion TCP)
        if pkt[TCP].flags == 'S':
            src_ip = pkt[IP].src
            dst_port = pkt[TCP].dport
            conexiones[src_ip].add(dst_port)

            if len(conexiones[src_ip]) > UMBRAL_PUERTOS:
                print(f"[ALERTA SCAN] {src_ip} escaneo {len(conexiones[src_ip])} puertos!")

sniff(prn=detectar_scan, store=0)
```

### Analisis de archivo PCAP
```python
from scapy.all import rdpcap, IP, TCP, DNS

# Leer archivo PCAP guardado
paquetes = rdpcap('captura.pcap')

# Extraer todas las consultas DNS
print("Consultas DNS detectadas:")
for pkt in paquetes:
    if DNS in pkt and pkt[DNS].qr == 0:  # qr=0 es query
        consulta = pkt[DNS].qd.qname.decode('utf-8')
        print(f"  {consulta}")

# Encontrar transferencias de datos grandes (posible exfiltracion)
print("\\nTransferencias grandes (>10KB):")
for pkt in paquetes:
    if IP in pkt and len(pkt) > 10240:
        print(f"  {pkt[IP].src} -> {pkt[IP].dst}: {len(pkt)} bytes")
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "En un paquete TCP, ¿que indica el flag 'S' (SYN)?",
                                "options": ["Cierre de conexion", "Inicio de un intento de conexion TCP (primer paso del handshake)", "Datos enviados", "Confirmacion de recepcion"],
                                "correct": 1,
                                "explanation": "El flag SYN (Synchronize) es el primer paso del TCP 3-way handshake. Un escaneo de puertos como Nmap envia paquetes SYN a multiples puertos para ver cuales responden. Detectar muchos SYN de una misma IP en poco tiempo indica un port scan."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "Para leer un archivo de captura de red (.pcap) con Scapy, se usa la funcion ___",
                                "correct": "rdpcap",
                                "explanation": "rdpcap (Read PCAP) carga un archivo .pcap o .pcapng en memoria como una lista de paquetes que puedes iterar y analizar. Es el equivalente Python de abrir un archivo en Wireshark."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "¿Para que sirve el modulo 'defaultdict' de collections en el detector de port scan?",
                                "options": ["Para ordenar los paquetes", "Para crear un diccionario que automaticamente inicializa valores nuevos (en este caso, un set por IP)", "Para cifrar los datos", "Para filtrar paquetes"],
                                "correct": 1,
                                "explanation": "defaultdict(set) crea un diccionario donde cada IP nueva automaticamente tiene un set vacio asociado. Sin esto, habria que verificar si la IP ya existe antes de agregar puertos. Simplifica el codigo y evita KeyError."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "m3",
                "title": "Herramientas de Seguridad con Python",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Interaccion con APIs de seguridad",
                        "theory": """## APIs de Seguridad en Python

### VirusTotal API
```python
import requests

VT_API_KEY = "tu_api_key_aqui"

def verificar_hash(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": VT_API_KEY}

    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        return {
            "malicioso": stats["malicious"],
            "sospechoso": stats["suspicious"],
            "limpio": stats["undetected"],
            "total": sum(stats.values())
        }
    return None

resultado = verificar_hash("hash_del_archivo")
if resultado:
    print(f"Detecciones: {resultado['malicioso']}/{resultado['total']}")
```

### AbuseIPDB API
```python
import requests

ABUSE_API_KEY = "tu_api_key"

def verificar_ip(ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {"ipAddress": ip_address, "maxAgeInDays": 90}
    headers = {"Key": ABUSE_API_KEY, "Accept": "application/json"}

    resp = requests.get(url, params=params, headers=headers)
    data = resp.json()["data"]

    return {
        "ip": ip_address,
        "score_abuso": data["abuseConfidenceScore"],
        "reportes": data["totalReports"],
        "pais": data["countryCode"],
        "isp": data["isp"]
    }

info = verificar_ip("203.0.113.45")
print(f"IP: {info['ip']} | Score: {info['score_abuso']}% | Pais: {info['pais']}")
```

### Shodan API
```python
import shodan

SHODAN_KEY = "tu_api_key"
api = shodan.Shodan(SHODAN_KEY)

def buscar_organizacion(org_name):
    try:
        resultados = api.search(f'org:"{org_name}"')
        print(f"Dispositivos encontrados: {resultados['total']}")
        for r in resultados['matches'][:5]:
            print(f"  IP: {r['ip_str']}")
            print(f"  Puertos: {r.get('port', 'N/A')}")
            print(f"  Banner: {r.get('data', '')[:100]}")
            print()
    except shodan.APIError as e:
        print(f"Error: {e}")
```

### Script completo de triage de incidente
```python
import requests
import json

def triage_ip(ip, vt_key, abuse_key):
    '''Verifica una IP en multiples fuentes de threat intelligence.'''
    reporte = {"ip": ip, "fuentes": {}}

    # VirusTotal
    vt_resp = requests.get(
        f"https://www.virustotal.com/api/v3/ip_addresses/{ip}",
        headers={"x-apikey": vt_key}
    )
    if vt_resp.ok:
        stats = vt_resp.json()["data"]["attributes"]["last_analysis_stats"]
        reporte["fuentes"]["virustotal"] = {
            "malicioso": stats["malicious"],
            "total": sum(stats.values())
        }

    # AbuseIPDB
    abuse_resp = requests.get(
        "https://api.abuseipdb.com/api/v2/check",
        params={"ipAddress": ip},
        headers={"Key": abuse_key, "Accept": "application/json"}
    )
    if abuse_resp.ok:
        data = abuse_resp.json()["data"]
        reporte["fuentes"]["abuseipdb"] = {
            "score": data["abuseConfidenceScore"],
            "reportes": data["totalReports"]
        }

    return reporte

resultado = triage_ip("203.0.113.45", VT_KEY, ABUSE_KEY)
print(json.dumps(resultado, indent=2))
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "¿Por que es mejor guardar las API keys en variables de entorno en lugar de escribirlas directamente en el codigo?",
                                "options": ["Las variables de entorno son mas rapidas", "Para evitar exponer credenciales si el codigo se sube a GitHub u otros repositorios publicos", "Python solo lee API keys de variables de entorno", "Es solo una convencion de estilo"],
                                "correct": 1,
                                "explanation": "Las API keys en el codigo fuente son credenciales expuestas. Si el repositorio es publico o se filtra, cualquiera puede usar tus API keys. Las variables de entorno (os.environ['API_KEY']) mantienen las credenciales fuera del codigo."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "La libreria de Python para hacer peticiones HTTP (como llamadas a APIs REST) se llama ___",
                                "correct": "requests",
                                "explanation": "requests es la libreria HTTP mas popular de Python. Con requests.get(url, headers=...) puedes consumir cualquier API REST. Es mucho mas simple que urllib de la libreria estandar."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "¿Que hace el metodo resp.json() en una respuesta de la libreria requests?",
                                "options": ["Guarda la respuesta en un archivo JSON", "Convierte el cuerpo de la respuesta HTTP (texto JSON) a un diccionario/lista de Python", "Verifica si la respuesta es JSON valido", "Cifra la respuesta en formato JSON"],
                                "correct": 1,
                                "explanation": "resp.json() parsea el cuerpo de la respuesta HTTP que esta en formato JSON y lo convierte a tipos nativos de Python (dict, list, str, int, etc.). Es equivalente a json.loads(resp.text)."
                            }
                        ]
                    },
                    {
                        "id": "l2",
                        "title": "Automatizacion de respuesta a incidentes",
                        "theory": """## Automatizacion en Incident Response

### Recolector de evidencia del sistema
```python
import os
import subprocess
import json
from datetime import datetime

def recolectar_evidencia():
    evidencia = {
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": os.uname().nodename if hasattr(os, 'uname') else os.environ.get('COMPUTERNAME'),
        "usuarios_activos": [],
        "procesos": [],
        "conexiones_red": [],
        "archivos_recientes": []
    }

    # Usuarios activos (Linux)
    try:
        resultado = subprocess.run(['who'], capture_output=True, text=True)
        evidencia["usuarios_activos"] = resultado.stdout.strip().split('\\n')
    except:
        pass

    # Procesos en ejecucion (Linux)
    try:
        resultado = subprocess.run(
            ['ps', 'aux', '--no-headers'],
            capture_output=True, text=True
        )
        # Solo los 20 procesos con mas CPU
        lineas = resultado.stdout.strip().split('\\n')
        evidencia["procesos"] = lineas[:20]
    except:
        pass

    # Conexiones de red activas
    try:
        resultado = subprocess.run(
            ['ss', '-tupn'],
            capture_output=True, text=True
        )
        evidencia["conexiones_red"] = resultado.stdout.strip().split('\\n')
    except:
        pass

    return evidencia

evidencia = recolectar_evidencia()
with open(f"evidencia_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'w') as f:
    json.dump(evidencia, f, indent=2)
print("Evidencia recolectada y guardada.")
```

### Detector de anomalias en logs en tiempo real
```python
import time
import re
from collections import defaultdict

class DetectorBruteForce:
    def __init__(self, umbral=5, ventana=60):
        self.umbral = umbral      # intentos maximos
        self.ventana = ventana    # en segundos
        self.intentos = defaultdict(list)
        self.alertas_enviadas = set()

    def procesar_linea(self, linea):
        patron = r'Failed password for \S+ from (\S+)'
        m = re.search(patron, linea)
        if not m:
            return

        ip = m.group(1)
        ahora = time.time()

        # Limpiar intentos antiguos fuera de la ventana
        self.intentos[ip] = [t for t in self.intentos[ip]
                               if ahora - t < self.ventana]
        self.intentos[ip].append(ahora)

        if (len(self.intentos[ip]) >= self.umbral and
                ip not in self.alertas_enviadas):
            self.alertar(ip, len(self.intentos[ip]))
            self.alertas_enviadas.add(ip)

    def alertar(self, ip, cantidad):
        print(f"[!] ALERTA: {ip} - {cantidad} intentos en {self.ventana}s")
        # Aqui se podria: enviar email, bloquear IP con iptables,
        # crear ticket en JIRA, enviar a SIEM, etc.

# Monitorear log en tiempo real
detector = DetectorBruteForce(umbral=5, ventana=60)
log_file = '/var/log/auth.log'

with open(log_file) as f:
    f.seek(0, 2)  # Ir al final del archivo
    print(f"Monitoreando {log_file}...")
    while True:
        linea = f.readline()
        if linea:
            detector.procesar_linea(linea)
        else:
            time.sleep(0.1)
```

### Bloqueo automatico de IPs (Linux con iptables)
```python
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def bloquear_ip(ip):
    '''Bloquea una IP maliciosa con iptables.'''
    # Verificar que no sea una IP privada (evitar bloquear la red local)
    rangos_privados = ['10.', '192.168.', '172.16.', '127.']
    if any(ip.startswith(r) for r in rangos_privados):
        logging.warning(f"No se bloquea IP privada: {ip}")
        return False

    cmd = ['iptables', '-I', 'INPUT', '-s', ip, '-j', 'DROP']
    resultado = subprocess.run(cmd, capture_output=True)

    if resultado.returncode == 0:
        logging.info(f"IP bloqueada: {ip}")
        return True
    else:
        logging.error(f"Error bloqueando {ip}: {resultado.stderr}")
        return False

def desbloquear_ip(ip):
    '''Elimina el bloqueo de una IP.'''
    cmd = ['iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP']
    subprocess.run(cmd)
    logging.info(f"IP desbloqueada: {ip}")
```""",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "question": "¿Por que el script de bloqueo de IPs verifica si es una IP privada antes de bloquearla?",
                                "options": ["Por requisitos legales", "Para evitar bloquear accidentalmente equipos de la red interna, lo que cortaria la comunicacion corporativa", "Las IPs privadas no pueden ser maliciosas", "iptables no puede bloquear IPs privadas"],
                                "correct": 1,
                                "explanation": "Las IPs privadas (10.x.x.x, 192.168.x.x, etc.) son equipos de la red interna. Bloquearlas accidentalmente cortaria la comunicacion con servidores internos, VPNs y otros servicios criticos. Siempre se debe filtrar antes de aplicar reglas automaticas."
                            },
                            {
                                "id": "e2",
                                "type": "fill_blank",
                                "question": "Para ejecutar comandos del sistema operativo desde Python y capturar su salida, se usa subprocess.___",
                                "correct": "run",
                                "explanation": "subprocess.run() ejecuta un comando del sistema y captura su salida. Con capture_output=True captura stdout y stderr. Es la forma moderna de ejecutar comandos desde Python (antes se usaba os.system() o subprocess.call())."
                            },
                            {
                                "id": "e3",
                                "type": "multiple_choice",
                                "question": "En el detector de brute force, ¿para que sirve la 'ventana de tiempo' (ventana=60)?",
                                "options": ["Para limitar el uso de CPU", "Para contar solo los intentos que ocurrieron en los ultimos N segundos, evitando falsos positivos de intentos espaciados en el tiempo", "Para definir cuanto tiempo dura la alerta", "Para el timeout de conexiones de red"],
                                "correct": 1,
                                "explanation": "La ventana deslizante solo cuenta intentos recientes. Sin ella, una IP con 1 intento fallido por hora durante 5 horas dispararía la misma alerta que 5 intentos en 1 segundo. La ventana temporal distingue ataques reales de errores normales de usuarios."
                            }
                        ]
                    }
                ]
            }
        ]
    }
}


def get_course(course_id):
    return COURSES.get(course_id)


def get_all_courses_summary():
    summary = []
    for cid, course in COURSES.items():
        total_lessons = sum(len(m["lessons"]) for m in course["modules"])
        total_exercises = sum(
            len(l["exercises"])
            for m in course["modules"]
            for l in m["lessons"]
        )
        summary.append({
            "id": course["id"],
            "title": course["title"],
            "description": course["description"],
            "icon": course["icon"],
            "color": course["color"],
            "totalModules": len(course["modules"]),
            "totalLessons": total_lessons,
            "totalExercises": total_exercises
        })
    return summary
