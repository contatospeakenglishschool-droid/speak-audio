# Speak! Esencial A1 - Unidad 04 "¿A qué te dedicas?" (todo en español latinoamericano, para principiantes absolutos) - built with the shared engine + Spanish layer
# Plan (Aula Internacional Plus 1, unidad 1): profesión y lugar de trabajo; trabajar de / en; masculino y femenino de las profesiones; artículos un / una.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_es import *
setup(band="A1 · UNIDAD 04", audio_json=os.path.join(HERE, "audio_es-a1-unidad-04.json"), img_dir=os.path.join(HERE, "img"), lang="es-419")

PHOTOS = [("A", "el médico", "médico"), ("B", "la profesora", "profesora"), ("C", "el ingeniero", "ingeniero"), ("D", "la mesera", "mesera"),
          ("E", "el cocinero", "cocinero"), ("F", "la enfermera", "enfermera"), ("G", "el estudiante", "estudiante"), ("H", "el guía de turismo", "guía")]

SCRIPT = [("Narradora", "Diálogo uno."), ("Lucía", "Pedro, él es Javier, mi hermano."), ("Javier", "¡Mucho gusto, Pedro! ¿A qué te dedicas?"),
          ("Pedro", "Soy ingeniero. Trabajo aquí, con Lucía. ¿Y tú?"), ("Javier", "Soy guía de turismo. Trabajo en una agencia de viajes."),
          ("Narradora", "Diálogo dos."), ("Pedro", "Sofía, ¿a qué te dedicas?"), ("Sofía", "Soy estudiante. Y los sábados trabajo de camarera en un restaurante."),
          ("Pedro", "¿Camarera? Aquí en México se dice mesera."), ("Sofía", "¡Ah, sí! Mesera."),
          ("Narradora", "Diálogo tres."), ("Pedro", "Doña Carmen, ¿a qué se dedica usted?"), ("Doña Carmen", "Soy médica. Trabajo en un hospital."),
          ("Paco", "¡Y yo soy cocinero y mesero! Trabajo aquí, en mi café.")]
JOBS = [("médico", "médica"), ("profesor", "profesora"), ("ingeniero", "ingeniera"), ("mesero", "mesera"),
        ("cocinero", "cocinera"), ("enfermero", "enfermera"), ("estudiante", "estudiante"), ("guía", "guía de turismo")]
S042 = [f"el {m}, la {f}" for m, f in JOBS]
S043 = ["¿A qué te dedicas?", "¿A qué se dedica usted?", "Soy ingeniero.", "Soy médica.", "Trabajo en un hospital.", "Trabajo de mesera en un restaurante."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Página 1
    cover = cover_html(T, "NIVEL A1 · UNIDAD 04", "¿A qué te dedicas?", "Hablar de tu profesión y de tu lugar de trabajo",
                       [("PUEDES", "preguntar y decir tu profesión y dónde trabajas"),
                        ("LENGUA", "¿A qué te dedicas? · Soy médico / médica · Trabajo en un hospital"),
                        ("PRONUNCIACIÓN", "profesiones · j · r suave")])
    words = ["el cocinero", "el estudiante", "el guía de turismo", "el ingeniero", "el médico", "la enfermera", "la mesera", "la profesora"]
    pl = [("el médico", ["un hospital", "una escuela"], "un hospital"), ("la profesora", ["una oficina", "una escuela"], "una escuela"),
          ("la mesera", ["un restaurante", "un hospital"], "un restaurante"), ("el ingeniero", ["un restaurante", "una oficina"], "una oficina")]
    pr = "".join(f'<td style="width:25%;text-align:center"><b>{j}</b><br>{ch(o, p)}</td>' for j, o, p in pl)
    b.page(f"""{sec(1, "Calentamiento: profesiones", "8 min")}
{sub("A", "Escucha y repite. Escribe.", "5 min", "04.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "¿Dónde trabaja? Elige.", "3 min")}
<table class="ck"><tr>{pr}</tr></table>""",
    32, """<ol><li>A: Pista 04.2. En la pista se oyen las dos formas (hombre / mujer); el alumno escribe la forma de la foto. Mostrar con gestos qué hace cada uno.</li>
<li>B: El alumno elige el lugar y dice la frase: <i>El médico trabaja en un hospital.</i> No explicar <i>un / una</i> todavía: llega en la página 3.</li>
<li>Repaso: empezar con <i>¡Hola! ¿Qué tal? ¿De dónde eres?</i></li></ol>""", cover=cover)

    b.extra("Panorama de la clase · 55 min", """
<table><tr><th>Fase</th><th>Tiempo</th><th>Objetivo</th><th>Página</th></tr>
<tr><td>1 Calentamiento</td><td>8 min</td><td>8 profesiones con fotos · lugares de trabajo</td><td>1</td></tr>
<tr><td>2 Escucha</td><td>10 min</td><td>¿A qué te dedicas? Tres diálogos cortos</td><td>2</td></tr>
<tr><td>3 Gramática</td><td>10 min</td><td><i>Soy</i> + profesión · <i>trabajo en / de</i> · <i>un / una</i> · hombre / mujer</td><td>3–4</td></tr>
<tr><td>4 Laboratorio de pronunciación</td><td>5 min</td><td>Profesiones · j · r suave</td><td>4</td></tr>
<tr><td>5 Práctica</td><td>8 min</td><td>Completar, ordenar, unir</td><td>5</td></tr>
<tr><td>6 Conversación</td><td>12 min</td><td>Cuatro tarjetas de visita · preguntas personales</td><td>6</td></tr>
<tr><td>7 Cierre</td><td>2 min</td><td>Autoevaluación y tarea</td><td>7</td></tr></table>
<div class="box"><h4>CÓMO FUNCIONA ESTA GUÍA</h4>Cada página corresponde a la página del Libro del alumno con el mismo número. Tus notas están en el <b>recuadro amarillo</b>.
<span class="red">Las respuestas en rojo</span> no aparecen en el Libro del alumno. Las etiquetas <span class="time">5 min</span> indican el tiempo de cada actividad. Las transcripciones están en la última página.</div>
<div class="box"><h4>SIEMPRE DESPACIO</h4>Tres cosas nuevas: <i>¿A qué te dedicas? / ¿A qué se dedica usted?</i> con <i>Soy</i> + profesión, <i>trabajo, trabajas, trabaja</i> con <i>en</i> (lugar) y <i>de</i> (función), y las profesiones en masculino y femenino. <i>ser</i> (Unidad 03) vuelve a aparecer.</div>
<div class="box sand"><h4>LA HISTORIA</h4>Lucía presenta a Javier, su hermano: es guía de turismo. Sofía es estudiante y los sábados trabaja de <i>camarera</i>; Pedro le enseña la palabra mexicana: <i>mesera</i>. Doña Carmen es médica, y Paco es cocinero y mesero en su café.</div>
<div class="box"><h4>EL PROBLEMA PARA LOS BRASILEÑOS</h4><i>Trabalho</i> ✗ → <b>trabajo</b> (con j). <i>en um hospital</i> ✗ → <b>en un hospital</b>. <i>Ella es médico</i> ✗ → <b>Ella es médica</b>. Falso amigo: <b>oficina</b> = lugar de trabajo con escritorios y computadoras; para los carros se dice <b>taller</b>.</div>
<div class="box"><h4>LA REALIDAD LATINOAMERICANA</h4>La persona que sirve en un restaurante: <b>mesero</b> (México, Colombia), <b>mozo</b> (Argentina, Uruguay, Perú), <b>garzón</b> (Chile); en España, <b>camarero</b>.</div>
<div class="box"><h4>AUDIO</h4>Pista 04.1 Tres diálogos (lento y natural) · Pista 04.2 Profesiones · Pista 04.3 Frases</div>""")

    # Página 2
    gr = [("1", "Javier", ["guía de turismo", "médico"], "guía de turismo"), ("2", "Sofía", ["estudiante", "profesora"], "estudiante"), ("3", "Doña Carmen", ["médica", "enfermera"], "médica")]
    wr = "".join(f'<td style="width:33%"><b>Diálogo {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("¿A qué te", "dedicas", "?"), ("", "Soy", " ingeniero."), ("Trabajo en una", "agencia", " de viajes."),
          ("Los sábados trabajo de", "camarera", "."), ("Doña Carmen, ¿a qué se", "dedica", " usted?"), ("Trabajo en un", "hospital", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Escucha: ¿A qué te dedicas?", "10 min")}
<p>Pedro conoce a Javier, el hermano de Lucía. También habla con Sofía y con doña Carmen.</p>
{audiocard(["04.1 · SLOW", "04.1 · NATURAL"])}
{sub("A", "Escucha. ¿A qué se dedica? Elige.", "3 min", "04.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Escucha otra vez. Completa.", "5 min", "04.1 · NATURAL")}
<div class="bank">agencia · camarera · dedica · dedicas · hospital · Soy</div>
{twocol(gl, 3)}
{sub("C", "Lee los diálogos con el profesor.", "2 min")}""",
    30, """<ol><li>A: versión <b>lenta</b>, dos veces. Antes, presentar a Javier: <i>Es el hermano de Lucía.</i></li>
<li>B: versión <b>natural</b>, parar después de cada diálogo. Preguntar: <i>¿Y Paco? ¿A qué se dedica?</i> (cocinero y mesero). <i>Camarera</i> (España) = <i>mesera</i> (México).</li>
<li>C: Los diálogos están en la última página. El alumno es Pedro; después, cambiar.</li></ol>""")

    # Página 3
    tr = [("yo", "trabajo"), ("tú", "trabajas"), ("él / ella / usted", "trabaja")]
    tt = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in tr)
    gn = [("-o → -a", "médic<b>o</b>", "médic<b>a</b>"), ("-or → -ora", "profes<b>or</b>", "profes<b>ora</b>"), ("-e, -a = igual", "estudiant<b>e</b>", "estudiant<b>e</b>")]
    tg = "".join(f"<tr><td class='small'>{r}</td><td>{m}</td><td>{f}</td></tr>" for r, m, f in gn)
    chk = [("Soy …", ["ingeniero", "un ingeniero"], "ingeniero"), ("Trabajo en … oficina.", ["un", "una"], "una"),
           ("Doña Carmen es …", ["médico", "médica"], "médica"), ("Sofía trabaja … mesera.", ["de", "en"], "de")]
    wt = "".join(f'<td style="width:25%"><span class="small">{s}</span><br>{ch(o, a)}</td>' for s, o, a in chk)
    b.page(f"""{sec(3, "Gramática: ¿A qué te dedicas?", "10 min")}
{sub("A", "Lee.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="2">trabajar</th></tr>{tt}
<tr><td colspan="2" class="small">Trabajo <b>en</b> un hospital. (lugar)<br>Trabajo <b>de</b> mesera. (función)</td></tr></table></div>
<div><table style="margin:0"><tr><th></th><th>♂ hombre</th><th>♀ mujer</th></tr>{tg}</table></div></div>
<div class="box"><h4>LA REGLA</h4><b>¿A qué te dedicas?</b> (tú) · <b>¿A qué se dedica usted?</b> (usted) → <b>Soy</b> + profesión, sin <i>un / una</i>: <i>Soy ingeniero.</i> &nbsp;·&nbsp; El lugar sí lleva artículo: <b>un</b> hospital, <b>un</b> restaurante (masculino) · <b>una</b> oficina, <b>una</b> escuela (femenino). En español es <b>un</b>, no <i>um</i>.</div>
{sub("B", "Elige.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "¿Y tú? Escribe.", "3 min")}
<div class="two"><div class="wline">Soy {R("… (profesión)")}.</div><div class="wline">Trabajo en {R("un / una … (lugar)")}.</div></div>""",
    32, """<ol><li>3A: Explicar primero. <i>trabajar</i> solo en singular. Como en portugués, la profesión va sin artículo después de <i>ser</i>: <i>Soy ingeniero</i>. <i>en</i> = el lugar; <i>de</i> = la función (<i>trabajo de mesera</i>).</li>
<li>3B: El alumno elige y dice la frase completa.</li>
<li>3C: Si el alumno no trabaja: <i>Soy estudiante</i>, <i>Estoy jubilado / jubilada</i> (solo como frase hecha).</li></ol>""")

    # Página 4
    b.page(f"""{sub("D", "Errores comunes", "2 min")}
<div class="box sand"><h4>ATENCIÓN: ERRORES COMUNES</h4>
<table style="margin:0"><tr><th>No digas</th><th>Di</th></tr>
<tr><td>Trabalho en un hospital.</td><td><b>Trabajo en un hospital.</b></td></tr>
<tr><td>Trabajo en um restaurante.</td><td><b>Trabajo en un restaurante.</b></td></tr>
<tr><td>Ella es médico.</td><td><b>Ella es médica.</b></td></tr>
<tr><td>¿A qué te dedicas, doña Carmen?</td><td><b>¿A qué se dedica usted, doña Carmen?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio de pronunciación", "5 min")}
{audiocard(["04.2", "04.3"])}
{sub("A", "Escucha y repite.", "2 min", "04.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S042)}</div>
{sub("B", "Escucha y repite.", "3 min", "04.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S043)}</div>
<div class="box"><h4>SONIDOS</h4><b>j</b> fuerte: <i>traba<b>j</b>o, <b>J</b>avier</i> &nbsp;·&nbsp; <b>r</b> suave entre vocales: <i>mese<b>r</b>o, mese<b>r</b>a, enfe<b>r</b>me<b>r</b>a</i> &nbsp;·&nbsp; <b>un</b> con n: <i>u<b>n</b> hospital</i></div>""",
    36, """<ol><li>Errores: <i>trabalho</i> y <i>um</i> vienen del portugués. En español, <i>trabajo</i> con j y <i>un</i> con n (la boca no se cierra al final).</li>
<li>4A/4B: Repetir dos veces. La <b>j</b> suena fuerte, desde la garganta. La <b>r</b> entre vocales es suave, como en «caro» en portugués. Mostrar, sin explicar demasiado.</li></ol>""")

    # Página 5
    gw = ["trabajo", "trabajas", "trabaja", "Soy", "en", "de"]
    gs = [("Yo", " en una oficina."), ("¿Dónde", " tú?"), ("Javier", " en una agencia de viajes."), ("", " médica."), ("Trabajo", " un restaurante."), ("Sofía trabaja", " mesera.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("dedicas / qué / te / a / ¿ / ?", "¿A qué te dedicas?"), ("profesora / soy", "Soy profesora."), ("en / trabajo / una escuela", "Trabajo en una escuela.")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("el cocinero", "c", "una escuela"), ("la enfermera", "a", "una agencia de viajes"), ("el guía de turismo", "b", "un restaurante"), ("la profesora", "d", "un hospital")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Práctica", "8 min")}
{sub("A", "Completa.", "3 min")}
<div class="bank">de · en · Soy · trabaja · trabajas · trabajo</div>
{twocol(gl5, 3)}
{sub("B", "Ordena.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Une. ¿Dónde trabaja?", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Frase 5: lugar → <i>en</i>. Frase 6: función → <i>de</i>.</li>
<li>C: Después de unir, decir la frase completa: <i>El cocinero trabaja en un restaurante.</i></li></ol>""")

    # Página 6
    ppl = [("Valeria Ruiz", "abogada · una oficina · 28 años", "tú · ¿A qué te dedicas?"), ("El señor Ortega", "taxista · la Ciudad de México", "usted · ¿A qué se dedica usted?"),
           ("Diego Pérez", "enfermero · un hospital · 31 años", "tú · ¿A qué te dedicas?"), ("La señora Vega", "profesora · una escuela", "usted · ¿A qué se dedica usted?")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + q)}</div>' for n, d, q in ppl)
    b.page(f"""{sec(6, "Conversación", "12 min")}
{sub("A", "Juega con el profesor. Pregunta: ¿A qué te dedicas? ¿Dónde trabajas?", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> Buenos días. ¿A qué se dedica usted?<br><b>B:</b> Soy profesora. Trabajo en una escuela. ¿Y usted?<br><b>A:</b> Soy … Trabajo en …</div>
{sub("B", "Contesta al profesor.", "5 min")}
<ol style="line-height:1.8"><li>¿A qué te dedicas?</li><li>¿Dónde trabajas?</li><li>¿A qué se dedica Javier? ¿Y Sofía?</li><li>¿Eres estudiante?</li></ol>""",
    28, """<ol><li>A: El profesor hace las cuatro personas. El alumno elige <i>¿A qué te dedicas?</i> o <i>¿A qué se dedica usted?</i> y después cuenta: <i>Valeria es abogada. Trabaja en una oficina.</i> Después, cambiar.</li>
<li>B: Respuestas libres. Si el alumno no conoce el nombre de su profesión, darlo y escribirlo en <i>Mis notas</i>.</li></ol>""")

    # Página 7
    pc = [("Unidad 02", "Puedo preguntar ¿Qué tal? y deletrear."), ("Unidad 03", "Puedo decir de dónde soy y mi nacionalidad."),
          ("Unidad 04", "Puedo preguntar: ¿A qué te dedicas? / ¿A qué se dedica usted?"), ("Unidad 04", "Puedo decir mi profesión y dónde trabajo.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("profesor", "profesora"), ("cocinero", "cocinera"), ("enfermero", "enfermera"), ("estudiante", "estudiante")]
    hr = "".join(f"<tr><td>♂ <b>{m}</b></td><td>♀ {A(f, 'min-width:30mm')}</td></tr>" for m, f in hw)
    b.page(f"""{sec(7, "Cierre y tarea", "2 min")}
{sub("A", "Autoevaluación", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En español …</th><th style="width:18mm">¡Fácil!</th><th style="width:18mm">A veces</th><th style="width:18mm">Todavía no</th></tr>{pcr}</table>
{sub("B", "Tarea", "1 min")}
<p><b>1. Escribe la forma para mujer.</b></p>
<table style="margin:0">{hr}</table>
<p style="margin-top:2mm"><b>2. Completa: un o una.</b> &nbsp; Trabajo en {A("una", "min-width:12mm")} oficina. · Trabaja en {A("un", "min-width:12mm")} hospital. · Trabajas en {A("una", "min-width:12mm")} escuela.</p>
<p style="margin-top:2mm"><b>3. Escribe dos frases: tu profesión y dónde trabajas.</b></p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Próxima clase: empezar con <i>¡Hola! ¿Qué tal? ¿A qué te dedicas?</i> El alumno lee las frases del ejercicio 3. En la Unidad 05 llegan los datos personales: la edad, el teléfono y el correo.</p>""")

    b.extra("Transcripciones", f"""
{sub("04.1", "¿A qué te dedicas? (lento y natural)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("04.2", "Profesiones")}
<p>{" · ".join(S042)}</p>
{sub("04.3", "Las frases")}
<p>{" · ".join(S043)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Esencial 04 - A que te dedicas")
