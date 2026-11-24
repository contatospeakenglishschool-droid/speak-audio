# Speak! Esencial A1 - Unidad 06 "Quiero aprender español" (todo en español latinoamericano, para principiantes absolutos) - built with the shared engine + Spanish layer
# Plan (Aula Internacional Plus 1, unidad 2): intenciones, por qué estudias español; querer + infinitivo; porque / para.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_es import *
setup(band="A1 · UNIDAD 06", audio_json=os.path.join(HERE, "audio_es-a1-unidad-06.json"), img_dir=os.path.join(HERE, "img"), lang="es-419")

# photos shuffled against the alphabetical bank (rule 2026-11-23)
PHOTOS = [("A", "ver series", "ver series"), ("B", "conocer gente", "conocer gente"), ("C", "trabajar", "trabajar"), ("D", "viajar", "viajar"),
          ("E", "hablar con amigos", "hablar con amigos"), ("F", "vivir en otro país", "vivir en otro país"), ("G", "leer", "leer"), ("H", "estudiar", "estudiar")]
BANK = sorted(w for _, w, _ in PHOTOS)
_r = [BANK.index(w) for _, w, _ in PHOTOS]
assert all(r != j for j, r in enumerate(_r)) and all(abs(_r[j + 1] - _r[j]) != 1 for j in range(7))

SCRIPT = [("Narradora", "Diálogo uno."), ("Profesora", "Pedro, ¿por qué quieres aprender español?"),
          ("Pedro", "Porque trabajo en México. Y quiero hablar bien con mis colegas."), ("Profesora", "¡Muy bien! ¿Y tú, Mark?"),
          ("Mark", "Yo quiero aprender español para viajar por América Latina."),
          ("Narradora", "Diálogo dos."), ("Pedro", "Mark, ¿de dónde eres?"), ("Mark", "Soy canadiense. Quiero vivir en Chile."),
          ("Pedro", "¿En Chile? ¿Para qué?"), ("Mark", "Para trabajar. Y porque me gustan las montañas."),
          ("Narradora", "Diálogo tres."), ("Paco", "Javier, ¿quieres un café?"), ("Javier", "Sí, gracias. Pedro, ¿quieres viajar a Oaxaca el sábado?"),
          ("Pedro", "¡Sí! Quiero conocer Oaxaca."), ("Paco", "¡Es mi ciudad! Yo también quiero ir.")]
S062 = ["viajar", "trabajar", "estudiar", "vivir en otro país", "hablar con amigos", "ver series", "leer", "conocer gente"]
S063 = ["¿Por qué quieres aprender español?", "Porque trabajo en México.", "Quiero viajar.", "Para viajar por América Latina.", "¿Quieres un café?", "Quiero conocer Oaxaca."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Página 1
    cover = cover_html(T, "NIVEL A1 · UNIDAD 06", "Quiero aprender español", "Decir qué quieres hacer y por qué",
                       [("PUEDES", "decir qué quieres hacer y por qué estudias español"),
                        ("LENGUA", "quiero, quieres, quiere + infinitivo · porque … · para …"),
                        ("PRONUNCIACIÓN", "ie: quiero · la r final · v = b")])
    me = "".join(f'<td style="text-align:center">☐<br><span class="small">{w}</span></td>' for w in ["viajar", "trabajar", "vivir en otro país", "hablar con amigos", "ver series", "conocer gente"])
    b.page(f"""{sec(1, "Calentamiento: ¿qué quieres hacer?", "8 min")}
{sub("A", "Escucha y repite. Escribe.", "5 min", "06.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(BANK)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "¿Y tú? ¿Para qué quieres el español? Marca.", "3 min")}
<table class="ck"><tr>{me}</tr></table>""",
    32, """<ol><li>A: Pista 06.2. Mostrar cada foto y hacer el gesto (viajar, leer, trabajar). Todas las palabras son verbos en infinitivo: terminan en <b>-ar, -er, -ir</b>.</li>
<li>B: El alumno marca y dice: <i>viajar, trabajar…</i> No pedir frases todavía; la estructura <i>Quiero + infinitivo</i> llega en la página 3.</li>
<li>Repaso: empezar con <i>¡Hola! ¿Qué tal? ¿Cuántos años tienes?</i></li></ol>""", cover=cover)

    b.extra("Panorama de la clase · 55 min", """
<table><tr><th>Fase</th><th>Tiempo</th><th>Objetivo</th><th>Página</th></tr>
<tr><td>1 Calentamiento</td><td>8 min</td><td>8 actividades (infinitivos) con fotos</td><td>1</td></tr>
<tr><td>2 Escucha</td><td>10 min</td><td>¿Por qué quieres aprender español? Tres diálogos</td><td>2</td></tr>
<tr><td>3 Gramática</td><td>10 min</td><td><i>querer</i> + infinitivo · <i>porque / para</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio de pronunciación</td><td>5 min</td><td>ie (quiero) · la r final · v = b</td><td>4</td></tr>
<tr><td>5 Práctica</td><td>8 min</td><td>Completar, ordenar, unir</td><td>5</td></tr>
<tr><td>6 Conversación</td><td>12 min</td><td>Cuatro estudiantes de español · preguntas personales</td><td>6</td></tr>
<tr><td>7 Cierre</td><td>2 min</td><td>Autoevaluación y tarea</td><td>7</td></tr></table>
<div class="box"><h4>CÓMO FUNCIONA ESTA GUÍA</h4>Cada página corresponde a la página del Libro del alumno con el mismo número. Tus notas están en el <b>recuadro amarillo</b>.
<span class="red">Las respuestas en rojo</span> no aparecen en el Libro del alumno. Las etiquetas <span class="time">5 min</span> indican el tiempo de cada actividad. Las transcripciones están en la última página.</div>
<div class="box"><h4>SIEMPRE DESPACIO</h4>Tres cosas nuevas: <i>quiero, quieres, quiere</i> + infinitivo, la pregunta <i>¿Por qué …?</i> con <i>Porque …</i>, y <i>para</i> + infinitivo. <i>ser, tener</i> y <i>trabajar</i> (Unidades 03–05) vuelven a aparecer. Es una buena clase para hablar de los objetivos reales del alumno.</div>
<div class="box sand"><h4>LA HISTORIA</h4>Pedro estudia español por la noche en una escuela. La profesora le pregunta por qué: trabaja en México y quiere hablar bien con sus colegas. Su compañero Mark, canadiense, quiere viajar y vivir en Chile. En el café, Javier invita a Pedro a Oaxaca, y Paco también quiere ir: ¡es su ciudad!</div>
<div class="box"><h4>EL PROBLEMA PARA LOS BRASILEÑOS</h4><i>Quero</i> ✗ → <b>Quiero</b> (con ie). <i>Quiero de viajar</i> ✗ → <b>Quiero viajar</b>. <i>¿Porqué?</i> ✗ → <b>¿Por qué?</b> (pregunta, dos palabras) y <b>porque</b> (respuesta, una palabra). La r del infinitivo se pronuncia: <i>viajar</i>, no «viajá».</div>
<div class="box"><h4>LA REALIDAD LATINOAMERICANA</h4><b>Oaxaca</b>, en el sur de México, es famosa por su comida (el mole) y sus tradiciones. Para series y películas se usa <b>ver</b>: <i>ver series, ver la tele</i>. <i>Asistir</i> significa «ir a un evento» (<i>asistir a una clase</i>).</div>
<div class="box"><h4>AUDIO</h4>Pista 06.1 Tres diálogos (lento y natural) · Pista 06.2 Actividades · Pista 06.3 Frases</div>""")

    # Página 2
    gr = [("1", "Pedro quiere aprender español …", ["para viajar", "porque trabaja en México"], "porque trabaja en México"), ("2", "Mark quiere vivir en …", ["Chile", "Canadá"], "Chile"), ("3", "El sábado quieren viajar a …", ["Oaxaca", "Chile"], "Oaxaca")]
    wr = "".join(f'<td style="width:33%"><b>Diálogo {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Pedro, ¿por qué", "quieres", " aprender español?"), ("", "Porque", " trabajo en México."), ("Yo quiero aprender español", "para", " viajar por América Latina."),
          ("¿En Chile? ¿Para", "qué", "?"), ("Javier, ¿quieres un", "café", "?"), ("¡Sí!", "Quiero", " conocer Oaxaca.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Escucha: ¿Por qué quieres aprender español?", "10 min")}
<p>Pedro estudia español por la noche. Habla con la profesora, con Mark (su compañero) y después con Javier y Paco.</p>
{audiocard(["06.1 · SLOW", "06.1 · NATURAL"])}
{sub("A", "Escucha. Elige.", "3 min", "06.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Escucha otra vez. Completa.", "5 min", "06.1 · NATURAL")}
<div class="bank">café · para · Porque · qué · Quiero · quieres</div>
{twocol(gl, 3)}
{sub("C", "Lee los diálogos con el profesor.", "2 min")}""",
    30, """<ol><li>A: versión <b>lenta</b>, dos veces. Antes, presentar a Mark: <i>Es el compañero de clase de Pedro. Es canadiense.</i></li>
<li>B: versión <b>natural</b>, parar después de cada diálogo. Preguntar: <i>¿Por qué quiere vivir Mark en Chile?</i> (para trabajar y porque le gustan las montañas; <i>me gustan</i> solo como frase hecha: llega en la Unidad 15).</li>
<li>C: Los diálogos están en la última página. El alumno es Pedro; después, cambiar.</li></ol>""")

    # Página 3
    qu = [("yo", "quiero", "Quiero viajar."), ("tú", "quieres", "¿Quieres un café?"), ("él / ella / usted", "quiere", "Paco quiere ir.")]
    tq = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in qu)
    pp = [("¿Por qué …?", "<b>Porque</b> + frase", "Porque trabajo en México."), ("¿Para qué …?", "<b>Para</b> + infinitivo", "Para viajar.")]
    tp = "".join(f"<tr><td><b>{q}</b></td><td>{r}</td><td class='small'>{e}</td></tr>" for q, r, e in pp)
    chk = [("Yo … aprender español.", ["quiero", "quiere"], "quiero"), ("¿… quieres vivir en Chile?", ["Por qué", "Porque"], "Por qué"),
           ("Estudio español … viajar.", ["para", "porque"], "para"), ("¿… usted un café?", ["Quieres", "Quiere"], "Quiere")]
    wt = "".join(f'<td style="width:25%"><span class="small">{s}</span><br>{ch(o, a)}</td>' for s, o, a in chk)
    b.page(f"""{sec(3, "Gramática: querer · porque / para", "10 min")}
{sub("A", "Lee.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">querer + infinitivo</th></tr>{tq}</table></div>
<div><table style="margin:0"><tr><th colspan="3">La razón</th></tr>{tp}</table></div></div>
<div class="box"><h4>LA REGLA</h4><b>querer</b> + infinitivo, sin <i>de</i>: <i>Quiero viajar.</i> En <i>quiero, quieres, quiere</i> hay <b>ie</b>. &nbsp;·&nbsp; Pregunta: <b>¿Por qué?</b> (dos palabras, con tilde) → respuesta: <b>porque</b> (una palabra) + frase. &nbsp;·&nbsp; <b>para</b> + infinitivo: <i>para trabajar</i>.</div>
{sub("B", "Elige.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "¿Y tú? Escribe.", "3 min")}
<div class="two"><div class="wline">Quiero aprender español para {R("… (infinitivo)")}.</div><div class="wline">Estudio español porque {R("… (frase)")}.</div></div>""",
    32, """<ol><li>3A: Explicar primero. <i>querer</i> solo en singular; la e → ie se ve aquí como vocabulario (la regla completa llega en la Unidad 17). Después de <i>quiero</i> y de <i>para</i>, siempre infinitivo.</li>
<li>3B: El alumno elige y lee la frase completa. Frase 4: <i>usted</i> → <i>quiere</i>.</li>
<li>3C: Respuestas personales y reales: es un buen momento para hablar de los objetivos del alumno.</li></ol>""")

    # Página 4
    b.page(f"""{sub("D", "Errores comunes", "2 min")}
<div class="box sand"><h4>ATENCIÓN: ERRORES COMUNES</h4>
<table style="margin:0"><tr><th>No digas</th><th>Di</th></tr>
<tr><td>Quero viajar.</td><td><b>Quiero viajar.</b></td></tr>
<tr><td>Quiero de aprender español.</td><td><b>Quiero aprender español.</b></td></tr>
<tr><td>¿Porqué quieres vivir en Chile?</td><td><b>¿Por qué quieres vivir en Chile?</b></td></tr>
<tr><td>Estudio español para trabajo en México.</td><td><b>Estudio español porque trabajo en México.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio de pronunciación", "5 min")}
{audiocard(["06.2", "06.3"])}
{sub("A", "Escucha y repite.", "2 min", "06.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S062)}</div>
{sub("B", "Escucha y repite.", "3 min", "06.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S063)}</div>
<div class="box"><h4>SONIDOS</h4><b>ie</b>: <i>qu<b>ie</b>ro, qu<b>ie</b>res, qu<b>ie</b>re</i> &nbsp;·&nbsp; la <b>r</b> final suena: <i>viaja<b>r</b>, lee<b>r</b>, vivi<b>r</b></i> &nbsp;·&nbsp; <b>v</b> = <b>b</b>: <i><b>v</b>iajar, <b>v</b>i<b>v</b>ir</i></div>""",
    36, """<ol><li>Errores: <i>quero</i> viene del portugués. <i>para</i> va con infinitivo; con una frase completa, <i>porque</i>.</li>
<li>4A/4B: Repetir dos veces. En el infinitivo la <b>r</b> final se pronuncia siempre, suave: <i>viajar</i>, no «viajá». La <b>v</b> suena como <b>b</b>.</li></ol>""")

    # Página 5
    gw = ["quiero", "quieres", "quiere", "Porque", "para", "quiere"]
    gs = [("Yo", " viajar a Oaxaca."), ("¿", " un café, Javier?"), ("Mark", " vivir en Chile."), ("¿Por qué estudias español? —", " trabajo en México."), ("Estudio español", " viajar."), ("¿Qué", " hacer usted el sábado?")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("aprender / quiero / español", "Quiero aprender español."), ("qué / quieres / por / ¿ / ? / viajar", "¿Por qué quieres viajar?"), ("para / trabajar / español / estudio", "Estudio español para trabajar.")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Quiero aprender español …", "c", "… porque me gusta la comida mexicana."), ("Estudio español …", "d", "… conocer Oaxaca."),
          ("Quiero viajar a México …", "a", "… para viajar por América Latina."), ("Pedro quiere …", "b", "… para hablar con mis amigos.")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Práctica", "8 min")}
{sub("A", "Completa.", "3 min")}
<div class="bank">para · Porque · quiere · quiere · quieres · quiero</div>
{twocol(gl5, 3)}
{sub("B", "Ordena.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Une.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Frase 4: respuesta → <i>Porque</i>, una palabra. Frase 6: <i>usted</i> → <i>quiere</i>.</li>
<li>C: Hay más de una opción posible en 1, 2 y 3: aceptar las que tengan sentido. La 4 solo puede ser <i>… conocer Oaxaca</i> (infinitivo después de <i>quiere</i>).</li></ol>""")

    # Página 6
    ppl = [("Ana · 24 años", "estudiante · Brasil", "vivir en Chile", "porque quiere estudiar allí"), ("El señor Silva · 61 años", "jubilado · Brasil", "viajar por Perú", "porque le gusta la historia"),
           ("Lucas · 35 años", "ingeniero · Brasil", "trabajar en México", "para hablar con sus colegas"), ("La señora Costa · 47 años", "médica · Brasil", "ver series en español", "para practicar")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>Quiere: {R(q) if T else "________"}<br>¿Por qué?: {R(p) if T else "________"}</div>' for n, d, q, p in ppl)
    b.page(f"""{sec(6, "Conversación", "12 min")}
{sub("A", "Pregunta al profesor. ¿Qué quiere hacer? ¿Por qué?", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> Ana, ¿por qué quieres aprender español?<br><b>B:</b> Porque quiero vivir en Chile.<br><b>A:</b> ¿Para qué?<br><b>B:</b> Para estudiar allí.</div>
{sub("B", "Contesta al profesor.", "5 min")}
<ol style="line-height:1.8"><li>¿Por qué quieres aprender español?</li><li>¿Quieres viajar? ¿Adónde?</li><li>¿Quieres vivir en otro país?</li><li>¿Qué quieres hacer el sábado?</li></ol>""",
    28, """<ol><li>A: El profesor es cada persona y contesta con los datos en rojo. El alumno elige <i>tú</i> (Ana, Lucas) o <i>usted</i> (el señor Silva, la señora Costa) y escribe. <i>le gusta</i>: solo como frase hecha.</li>
<li>B: Respuestas libres. Pregunta 2: aceptar solo el nombre del lugar (<i>A México.</i>).</li></ol>""")

    # Página 7
    pc = [("Unidad 04", "Puedo decir mi profesión y dónde trabajo."), ("Unidad 05", "Puedo decir mi edad, mi teléfono y mi correo."),
          ("Unidad 06", "Puedo decir qué quiero hacer: Quiero + infinitivo."), ("Unidad 06", "Puedo explicar por qué: porque … / para …")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    b.page(f"""{sec(7, "Cierre y tarea", "2 min")}
{sub("A", "Autoevaluación", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En español …</th><th style="width:18mm">¡Fácil!</th><th style="width:18mm">A veces</th><th style="width:18mm">Todavía no</th></tr>{pcr}</table>
{sub("B", "Tarea", "1 min")}
<p><b>1. Completa: quiero, quieres o quiere.</b> &nbsp; Yo {A("quiero", "min-width:14mm")} viajar. · ¿Tú {A("quieres", "min-width:14mm")} un café? · Javier {A("quiere", "min-width:14mm")} ir a Oaxaca. · ¿Usted {A("quiere", "min-width:14mm")} estudiar?</p>
<p style="margin-top:2mm"><b>2. Completa: porque o para.</b> &nbsp; Estudio español {A("para", "min-width:14mm")} viajar. · Quiero vivir en México {A("porque", "min-width:14mm")} me gusta la comida.</p>
<p style="margin-top:2mm"><b>3. Escribe tres frases: ¿Por qué quieres aprender español?</b></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Próxima clase: empezar con <i>¡Hola! ¿Qué tal? ¿Qué quieres hacer el fin de semana?</i> El alumno lee las tres frases del ejercicio 3. En la Unidad 07: <i>¿Qué haces?</i> (verbos regulares en presente).</p>""")

    b.extra("Transcripciones", f"""
{sub("06.1", "¿Por qué quieres aprender español? (lento y natural)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("06.2", "Actividades")}
<p>{" · ".join(S062)}</p>
{sub("06.3", "Las frases")}
<p>{" · ".join(S063)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Esencial 06 - Quiero aprender espanol")
