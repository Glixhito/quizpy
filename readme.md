# QuizPy 🧠

Aplicación web de trivia interactiva construida con **Flask** (Python).

## Descripción

QuizPy es un juego de preguntas y respuestas sobre cultura general y programación.
Cada partida mezcla aleatoriamente las preguntas y las opciones de respuesta, por lo
que la experiencia es diferente en cada intento. Al finalizar se muestra un resumen
detallado con el puntaje y las respuestas correctas.

## Funciones

| Función | Descripción |
|---|---|
| **Mezcla aleatoria** | Las preguntas y sus opciones se ordenan al azar en cada partida |
| **Feedback inmediato** | Después de cada respuesta se indica si fue correcta o no |
| **Barra de progreso** | Muestra visualmente cuántas preguntas quedan |
| **Resultado final** | Porcentaje de aciertos, contadores y mensaje según puntaje |
| **Resumen detallado** | Lista completa de respuestas dadas vs. respuestas correctas |
| **Sesión por usuario** | Cada jugador tiene su propio estado de partida independiente |
| **Reinicio fácil** | Botón para volver a jugar con preguntas remezcladas |

## Instalación

```bash
# 1. Entrar a la carpeta del proyecto
cd quizapp

# 2. (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python app.py
```

Abrir en el navegador: **http://127.0.0.1:5000**

## Estructura del proyecto

```
quizapp/
├── app.py              ← lógica Flask: rutas y funciones auxiliares
├── requirements.txt    ← dependencias del proyecto
├── LEEME.md            ← este archivo
└── templates/
    ├── base.html       ← plantilla base con estilos compartidos
    ├── inicio.html     ← pantalla de bienvenida
    ├── pregunta.html   ← pantalla de pregunta con opciones
    ├── feedback.html   ← resultado de cada respuesta
    └── resultado.html  ← pantalla final con puntaje y resumen
```

## Rutas de la aplicación

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET | Pantalla de inicio, reinicia la sesión |
| `/pregunta` | GET, POST | Muestra la pregunta actual o procesa la respuesta |
| `/siguiente` | GET | Avanza a la siguiente pregunta |
| `/resultado` | GET | Muestra el resultado final |

## Tecnologías

- **Python 3** — lenguaje base
- **Flask 2.1** — framework web (rutas, sesiones, templates)
- **Jinja2** — motor de plantillas (incluido con Flask)
- **random** — módulo estándar para mezclar preguntas y opciones
