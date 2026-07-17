from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "quizapp_secret_2026"

PREGUNTAS = [
    {
        "pregunta": "¿Cuál es el lenguaje de programación más usado según Stack Overflow 2022?",
        "opciones": ["Python", "JavaScript", "Java", "C++"],
        "respuesta": "JavaScript",
    },
    {
        "pregunta": "¿Qué función de Python convierte un texto a número entero?",
        "opciones": ["float()", "str()", "int()", "num()"],
        "respuesta": "int()",
    },
    {
        "pregunta": "¿Cuántos países hay en América del Sur?",
        "opciones": ["10", "12", "14", "9"],
        "respuesta": "12",
    },
    {
        "pregunta": "¿Qué significa HTML?",
        "opciones": [
            "HyperText Markup Language",
            "HighText Machine Language",
            "HyperTool Multi Language",
            "HyperText Modern Links",
        ],
        "respuesta": "HyperText Markup Language",
    },
    {
        "pregunta": "¿En qué año se fundó Python?",
        "opciones": ["1985", "1991", "1998", "2003"],
        "respuesta": "1991",
    },
    {
        "pregunta": "¿Cuál planeta es conocido como el planeta rojo?",
        "opciones": ["Venus", "Júpiter", "Marte", "Saturno"],
        "respuesta": "Marte",
    },
    {
        "pregunta": "¿Qué estructura de datos usa LIFO (último en entrar, primero en salir)?",
        "opciones": ["Cola", "Lista", "Pila", "Árbol"],
        "respuesta": "Pila",
    },
    {
        "pregunta": "¿Cuál es la capital de Australia?",
        "opciones": ["Sídney", "Melbourne", "Brisbane", "Canberra"],
        "respuesta": "Canberra",
    },
    {
        "pregunta": "¿Qué símbolo se usa para comentarios de una línea en Python?",
        "opciones": ["//", "/*", "#", "--"],
        "respuesta": "#",
    },
    {
        "pregunta": "¿Cuántos bits tiene un byte?",
        "opciones": ["4", "16", "8", "32"],
        "respuesta": "8",
    },
]


def obtener_pregunta(indice):
    return PREGUNTAS[indice]


def calcular_porcentaje(correctas, total):
    if total == 0:
        return 0
    return round((correctas / total) * 100)


def obtener_mensajes(porcentaje):
    if porcentaje == 100:
        return "Perfecto! Eres un genio!"
    elif porcentaje >= 80:
        return "Excelente resultado! "
    elif porcentaje >= 60:
        return "Buen trabajo! Puedes mejorar un poco más. 💪"
    elif porcentaje >= 40:
        return "Vas por buen camino, sigue practicando. 📚"
    else:
        return "No te rindas, inténtalo de nuevo! 🔄"


@app.route("/")
def inicio():
    session.clear()
    preguntas_mezcladas = random.sample(PREGUNTAS, len(PREGUNTAS))
    session["orden"] = [PREGUNTAS.index(p) for p in preguntas_mezcladas]
    session["indice"] = 0
    session["correctas"] = 0
    session["respuestas"] = []
    return render_template("inicio.html", total=len(PREGUNTAS))


@app.route("/pregunta", methods=["GET", "POST"])
def pregunta():
    if "indice" not in session:
        return redirect(url_for("inicio"))

    indice_actual = session["indice"]
    total = len(PREGUNTAS)

    if indice_actual >= total:
        return redirect(url_for("resultado"))

    indice_real = session["orden"][indice_actual]
    pregunta_actual = obtener_pregunta(indice_real)
    opciones = pregunta_actual["opciones"][:]
    random.shuffle(opciones)

    if request.method == "POST":
        respuesta_usuario = request.form.get("opcion")
        es_correcta = respuesta_usuario == pregunta_actual["respuesta"]

        if es_correcta:
            session["correctas"] = session.get("correctas", 0) + 1

        session["respuestas"] = session.get("respuestas", []) + [
            {
                "pregunta": pregunta_actual["pregunta"],
                "dada": respuesta_usuario,
                "correcta": pregunta_actual["respuesta"],
                "bien": es_correcta,
            }
        ]

        session["indice"] = indice_actual + 1

        return render_template(
            "feedback.html",
            es_correcta=es_correcta,
            respuesta_correcta=pregunta_actual["respuesta"],
            respuesta_dada=respuesta_usuario,
            numero=indice_actual + 1,
            total=total,
        )

    return render_template(
        "pregunta.html",
        pregunta=pregunta_actual["pregunta"],
        opciones=opciones,
        numero=indice_actual + 1,
        total=total,
        progreso=round((indice_actual / total) * 100),
    )


@app.route("/siguiente")
def siguiente():
    return redirect(url_for("pregunta"))


@app.route("/resultado")
def resultado():
    if "correctas" not in session:
        return redirect(url_for("inicio"))

    correctas = session.get("correctas", 0)
    total = len(PREGUNTAS)
    porcentaje = calcular_porcentaje(correctas, total)
    mensaje = obtener_mensajes(porcentaje)
    respuestas = session.get("respuestas", [])

    return render_template(
        "resultado.html",
        correctas=correctas,
        total=total,
        porcentaje=porcentaje,
        mensaje=mensaje,
        respuestas=respuestas,
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
