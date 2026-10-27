# Speak! Esencial A1 - Unidad 01 "¡Hola!" (todo en español latinoamericano, para principiantes absolutos) - built with the shared engine + Spanish layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_es import *
setup(band="A1 · UNIDAD 01", audio_json=os.path.join(HERE, "audio_es-a1-unidad-01.json"), img_dir=os.path.join(HERE, "img"), lang="es-419")

PHOTOS = [("A", "¡Hola!", "hola"), ("B", "¡Buenos días!", "buenos días"), ("C", "¡Buenas tardes!", "buenas tardes"), ("D", "¡Buenas noches!", "buenas noches"),
          ("E", "¡Adiós!", "adiós"), ("F", "¡Hasta luego!", "hasta luego"), ("G", "¡Hasta mañana!", "hasta mañana"), ("H", "¡Mucho gusto!", "mucho gusto")]

SCRIPT = [("Narradora", "Diálogo uno."), ("Doña Carmen", "Buenos días. Soy Carmen Ruiz. ¿Cómo se llama usted?"),
          ("Pedro", "Buenos días, señora. Me llamo Pedro Almeida."), ("Doña Carmen", "Mucho gusto, señor Almeida."), ("Pedro", "Mucho gusto, señora Ruiz."),
          ("Narradora", "Diálogo dos."), ("Lucía", "¡Hola! Me llamo Lucía. ¿Cómo te llamas?"), ("Pedro", "¡Hola, Lucía! Soy Pedro."),
          ("Lucía", "Mucho gusto, Pedro."), ("Pedro", "Igualmente."),
          ("Narradora", "Diálogo tres."), ("Paco", "¡Buenas noches!"), ("Pedro", "¡Buenas noches! Soy Pedro."),
          ("Paco", "¡Hola, Pedro! Soy Paco. Mucho gusto."), ("Pedro", "Igualmente. ¡Adiós, Paco!"), ("Paco", "¡Hasta mañana!")]
S012 = ["Hola", "Buenos días", "Buenas tardes", "Buenas noches", "Adiós", "Hasta luego", "Hasta mañana", "Mucho gusto"]
S013 = ["Me llamo Pedro.", "Soy Lucía.", "¿Cómo te llamas?", "¿Cómo se llama usted?", "Mucho gusto.", "Igualmente."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Página 1
    cover = cover_html(T, "NIVEL A1 · UNIDAD 01", "¡Hola!", "Saludar y decir tu nombre",
                       [("PUEDES", "saludar, decir tu nombre y preguntar el nombre"),
                        ("LENGUA", "Me llamo … · Soy … · ¿Cómo te llamas? · ¿Cómo se llama usted?"),
                        ("PRONUNCIACIÓN", "saludos · h · ll")])
    words = ["¡Adiós!", "¡Buenas noches!", "¡Buenas tardes!", "¡Buenos días!", "¡Hasta luego!", "¡Hasta mañana!", "¡Hola!", "¡Mucho gusto!"]
    qs = [("08:00", "¡Buenos días!"), ("14:00", "¡Buenas tardes!"), ("17:00", "¡Buenas tardes!"), ("21:00", "¡Buenas noches!")]
    cl = "".join(f'<td style="width:25%;text-align:center"><b style="font-size:13pt">{t}</b><br>{A(a, "min-width:30mm")}</td>' for t, a in qs)
    b.page(f"""{sec(1, "Calentamiento: ¡Hola!", "8 min")}
{sub("A", "Escucha y repite. Escribe.", "5 min", "01.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "¿Qué hora es? Escribe.", "3 min")}
<table class="ck"><tr>{cl}</tr></table>""",
    30, """<ol><li>A: Pista 01.2. El profesor señala cada foto, pone la palabra, el alumno repite y escribe. Despacio, con gestos (levantar la mano, dar la mano). Repetir mucho.</li>
<li>B: Mostrar con el reloj: <b>Buenos días</b> por la mañana (hasta las 12), <b>Buenas tardes</b> desde las 12 hasta que oscurece, <b>Buenas noches</b> por la noche (para saludar y para despedirse). <b>Adiós</b> = me voy. <b>Hasta luego</b> = nos vemos más tarde u otro día. <b>Hasta mañana</b> = nos vemos mañana.</li></ol>""", cover=cover)

    b.extra("Panorama de la clase · 55 min", """
<table><tr><th>Fase</th><th>Tiempo</th><th>Objetivo</th><th>Página</th></tr>
<tr><td>1 Calentamiento</td><td>8 min</td><td>8 saludos con fotos y horas</td><td>1</td></tr>
<tr><td>2 Escucha</td><td>10 min</td><td>Pedro en la Ciudad de México: tres diálogos cortos</td><td>2</td></tr>
<tr><td>3 Gramática</td><td>10 min</td><td><i>Me llamo … / Soy …</i> · <i>¿Cómo te llamas? / ¿Cómo se llama usted?</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio de pronunciación</td><td>5 min</td><td>Repetir frases · h · ll</td><td>4</td></tr>
<tr><td>5 Práctica</td><td>8 min</td><td>Completar, ordenar, unir</td><td>5</td></tr>
<tr><td>6 Conversación</td><td>12 min</td><td>Saludar a cuatro personas · preguntas del profesor</td><td>6</td></tr>
<tr><td>7 Cierre</td><td>2 min</td><td>Autoevaluación y tarea</td><td>7</td></tr></table>
<div class="box"><h4>CÓMO FUNCIONA ESTA GUÍA</h4>Cada página corresponde a la página del Libro del alumno con el mismo número. Tus notas están en el <b>recuadro amarillo</b>.
<span class="red">Las respuestas en rojo</span> no aparecen en el Libro del alumno. Las etiquetas <span class="time">5 min</span> indican el tiempo de cada actividad. Las transcripciones están en la última página.</div>
<div class="box"><h4>PRIMERA CLASE: ¡DESPACIO!</h4>El alumno nunca ha estudiado español. El español se parece al portugués, pero en esta clase no hay que ir más rápido: hablar despacio, mostrar mucho (fotos, gestos, reloj) y repetir cada estructura muchas veces. Las instrucciones son cortas y siempre las mismas: <i>Escucha. Repite. Escribe. Completa. Une. Ordena.</i> El profesor las lee y muestra qué hacer. Objetivo de la clase: saludar, decir el nombre y preguntar el nombre. Nada más.</div>
<div class="box sand"><h4>LA HISTORIA EMPIEZA</h4>Pedro Almeida es de Recife y ahora vive en la Ciudad de México. Por la mañana conoce a su casera, doña Carmen (usted). En la oficina conoce a Lucía, una colega (tú). Por la noche, en el café de la esquina, conoce a Paco, el dueño.</div>
<div class="box"><h4>EL PROBLEMA PARA LOS BRASILEÑOS</h4>El alumno entiende mucho, pero mezcla: <i>Me chamo Pedro</i> ✗ → <b>Me llamo Pedro</b>. <i>Bom dia / Buenos tardes</i> ✗ → <b>Buenos días / Buenas tardes</b> (siempre en plural; <i>días</i> es masculino y <i>tardes</i> femenino). Y a <i>señor / señora / doña …</i> se le dice <b>usted</b>: <i>¿Cómo se llama usted?</i></div>
<div class="box"><h4>LA REALIDAD LATINOAMERICANA</h4>En México, a una señora mayor se le dice <b>doña</b> + nombre: <i>doña Carmen</i>. En Argentina y Uruguay también se oye <b>Buen día</b>. En Chile, Colombia y Argentina se dice mucho <b>Chao</b>. Entre amigos, un beso en la mejilla es normal en casi toda América Latina.</div>
<div class="box"><h4>AUDIO</h4>Pista 01.1 Tres diálogos (lento y natural) · Pista 01.2 Saludos · Pista 01.3 Frases</div>""")

    # Página 2
    gr = [("1", "Pedro y doña Carmen", ["¡Hola!", "¡Buenos días!"], "¡Buenos días!"), ("2", "Pedro y Lucía", ["¡Hola!", "¡Buenas noches!"], "¡Hola!"),
          ("3", "Pedro y Paco", ["¡Buenos días!", "¡Buenas noches!"], "¡Buenas noches!")]
    wr = "".join(f'<td style="width:33%"><b>Diálogo {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("", "Soy", " Carmen Ruiz."), ("¿Cómo se", "llama", " usted?"), ("", "Me llamo", " Pedro Almeida."),
          ("¿Cómo te", "llamas", "?"), ("", "Mucho gusto", ", Pedro."), ("", "Igualmente", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:22mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Escucha: Pedro en la Ciudad de México", "10 min")}
<p>Este es Pedro. Es de Brasil. Vive en la Ciudad de México.</p>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL"])}
{sub("A", "Escucha. Elige.", "3 min", "01.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Escucha otra vez. Completa.", "5 min", "01.1 · NATURAL")}
<div class="bank">Igualmente · llama · llamas · Me llamo · Mucho gusto · Soy</div>
{twocol(gl, 3)}
{sub("C", "Lee los diálogos con el profesor.", "2 min")}""",
    30, """<ol><li>A: versión <b>lenta</b>, dos veces. Antes de escuchar, mostrar tres fotos de la página 1 (B, A, D): mañana, oficina, noche.</li>
<li>B: versión <b>natural</b>. Palabras del recuadro. Parar después de cada diálogo.</li>
<li>C: Los diálogos están en la última página de la guía. El profesor lee, el alumno es Pedro. Después, cambiar.</li></ol>""")

    # Página 3
    who = [("Lucía", "colega", "¿Cómo te llamas?"), ("Doña Carmen", "casera", "¿Cómo se llama usted?"), ("Diego", "vecino, 22 años", "¿Cómo te llamas?"), ("La doctora Méndez", "médica", "¿Cómo se llama usted?")]
    wt = "".join(f'<td style="width:25%"><b>{n}</b><br><span class="small">{d}</span><br>{ch(["¿Cómo te llamas?", "¿Cómo se llama usted?"], a)}</td>' for n, d, a in who)
    b.page(f"""{sec(3, "Gramática: Me llamo … / ¿Cómo te llamas?", "10 min")}
{sub("A", "Lee.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="2">Mi nombre</th></tr>
<tr><td><b>Me llamo</b> Pedro.</td><td><b>Soy</b> Pedro.</td></tr>
<tr><td><b>Me llamo</b> Lucía.</td><td><b>Soy</b> Lucía.</td></tr></table></div>
<div><table style="margin:0"><tr><th colspan="2">La pregunta</th></tr>
<tr><td><b>tú</b></td><td>¿Cómo <b>te llamas</b>?</td></tr>
<tr><td><b>usted</b></td><td>¿Cómo <b>se llama usted</b>?</td></tr></table></div></div>
<div class="box"><h4>¿TÚ O USTED?</h4><b>tú</b> = amigos, colegas, jóvenes. &nbsp; <b>usted</b> = señor …, señora …, doña …, personas mayores. &nbsp; En español: <b>¿</b>…? &nbsp;<b>¡</b>…!</div>
{sub("B", "¿Tú o usted? Elige la pregunta.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "Escribe tu nombre.", "3 min")}
<div class="two"><div class="wline">Me llamo {R("…")}</div><div class="wline">Soy {R("…")}</div></div>""",
    32, """<ol><li>A: <i>Me llamo …</i> y <i>Soy …</i> significan aquí lo mismo. Practicar solo estas dos formas y las dos preguntas, sin conjugación completa (llega más adelante). El alumno lee en voz alta. Mostrar los signos <b>¿</b> y <b>¡</b> al principio: no existen en portugués.</li>
<li>B: Mostrar con gestos: amigo = tú, señor / señora = usted. Diego: joven, vecino → tú.</li>
<li>C: El alumno dice su nombre en voz alta: <i>Me llamo …</i></li></ol>""")

    # Página 4
    b.page(f"""{sub("D", "Errores comunes", "2 min")}
<div class="box sand"><h4>ATENCIÓN: ERRORES COMUNES</h4>
<table style="margin:0"><tr><th>No digas</th><th>Di</th></tr>
<tr><td>Me chamo Pedro.</td><td><b>Me llamo Pedro.</b></td></tr>
<tr><td>Bueno día.</td><td><b>Buenos días.</b></td></tr>
<tr><td>Buenos tardes.</td><td><b>Buenas tardes.</b></td></tr>
<tr><td>¿Cómo te llamas, señora Ruiz?</td><td><b>¿Cómo se llama usted, señora Ruiz?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio de pronunciación", "5 min")}
{audiocard(["01.2", "01.3"])}
{sub("A", "Escucha y repite.", "2 min", "01.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S012)}</div>
{sub("B", "Escucha y repite.", "3 min", "01.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S013)}</div>
<div class="box"><h4>SONIDOS</h4><b>h</b> = no suena: <i><b>h</b>ola, <b>h</b>asta</i> &nbsp;·&nbsp; <b>ll</b> = [y]: <i><b>ll</b>amo, <b>ll</b>amas</i> &nbsp;·&nbsp; <b>d</b> y <b>s</b> claras: <i>bueno<b>s</b> <b>d</b>ía<b>s</b>, noche<b>s</b></i></div>""",
    36, """<ol><li>Errores: <i>Me chamo</i> es el error más frecuente (portugués «me chamo»). <i>Buenos días</i> y <i>Buenas tardes</i> van siempre en plural. Corregir con amabilidad y repetir la forma correcta.</li>
<li>4A/4B: Repetir cada palabra dos veces. La <b>h</b> no se pronuncia: <i>hola</i> = «ola». La <b>ll</b> suena como [y] en México: <i>llamo</i>. En <i>días</i> la <b>d</b> no suena «dj» como en portugués, y en <i>noches</i> la <b>e</b> final no se convierte en «i». Mostrar, no explicar demasiado.</li></ol>""")

    # Página 5
    gw = ["llamo", "Soy", "llamas", "llama", "gusto", "Igualmente"]
    gs = [("Me", "Lucía."), ("", "Pedro."), ("¿Cómo te", "?"), ("¿Cómo se", "usted?"), ("Mucho", ", Paco."), ("", ".")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:20mm")} {c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("llamo / me / Diego", "Me llamo Diego."), ("te / cómo / llamas / ¿ / ?", "¿Cómo te llamas?"), ("usted / se / cómo / llama / ¿ / ?", "¿Cómo se llama usted?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("¡Buenos días!", "c", "Me llamo Diego."), ("¿Cómo te llamas?", "a", "Igualmente."), ("Mucho gusto.", "b", "¡Buenos días!"), ("¡Adiós!", "d", "¡Hasta luego!")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Práctica", "8 min")}
{sub("A", "Completa.", "3 min")}
<div class="bank">gusto · Igualmente · llama · llamas · llamo · Soy</div>
{twocol(gl5, 3)}
{sub("B", "Ordena.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Une.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: En la 2, <i>Me llamo</i> también es correcto si el alumno lo escribe: aceptar.</li>
<li>B: Mostrar que en la pregunta <i>cómo</i> va al principio y que la pregunta empieza con <b>¿</b>. C: Leer los pares en voz alta; el profesor hace la primera persona.</li></ol>""")

    # Página 6
    ppl = [("Lucía", "colega · 9:00", "tú · ¡Hola! / ¡Buenos días!"), ("Doña Carmen", "casera · 8:00", "usted · ¡Buenos días!"),
           ("Diego", "vecino · 20:00", "tú · ¡Hola! / ¡Buenas noches!"), ("La doctora Méndez", "médica · 16:00", "usted · ¡Buenas tardes!")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + a)}</div>' for n, d, a in ppl)
    b.page(f"""{sec(6, "Conversación", "12 min")}
{sub("A", "Juega con el profesor. Saluda. Di tu nombre. Pregunta el nombre.", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="bank" style="background:#fff">¡Hola! / ¡Buenos días! / ¡Buenas tardes! / ¡Buenas noches! · Me llamo … · ¿Cómo te llamas? / ¿Cómo se llama usted? · Mucho gusto. · Igualmente. · ¡Adiós! / ¡Hasta luego!</div>
<div class="msg"><b>A:</b> ¡Buenos días! Me llamo … ¿Cómo se llama usted?<br><b>B:</b> ¡Buenos días! Soy …<br><b>A:</b> Mucho gusto.<br><b>B:</b> Igualmente. … ¡Hasta luego!</div>
{sub("B", "Contesta al profesor.", "5 min")}
<ol style="line-height:1.8"><li>¡Hola! ¿Cómo te llamas?</li><li>¡Buenas tardes! ¿Cómo se llama usted?</li><li>Mucho gusto.</li><li>¡Adiós!</li></ol>""",
    28, """<ol><li>A: El profesor hace las cuatro personas (con tarjeta de nombre o foto). El alumno sigue el modelo del recuadro. Después, cambiar: el alumno es doña Carmen y el profesor es Pedro.</li>
<li>B: El profesor pregunta y el alumno contesta libremente. Respuestas esperadas: <i>Me llamo … · Igualmente. · ¡Adiós! / ¡Hasta luego!</i> Corregir enseguida <i>Me chamo …</i></li></ol>""")

    # Página 7
    pc = [("Unidad 01", "Puedo saludar (mañana, tarde y noche)."), ("Unidad 01", "Puedo decir mi nombre."),
          ("Unidad 01", "Puedo preguntar el nombre (tú y usted).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("07:00", "¡Buenos días!"), ("15:00", "¡Buenas tardes!"), ("20:00", "¡Buenas noches!"), ("10:00", "¡Buenos días!")]
    hl = [f'<li value="{i+1}"><b>{t}</b> {A(a, "min-width:32mm")}</li>' for i, (t, a) in enumerate(hw)]
    b.page(f"""{sec(7, "Cierre y tarea", "2 min")}
{sub("A", "Autoevaluación", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En español …</th><th style="width:18mm">¡Fácil!</th><th style="width:18mm">A veces</th><th style="width:18mm">Todavía no</th></tr>{pcr}</table>
{sub("B", "Tarea", "1 min")}
<p><b>1. Escribe el saludo.</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Completa el diálogo.</b></p>
<div class="msg"><b>A:</b> ¡Hola! Me llamo Lucía. ¿Cómo te llamas?<br><b>B:</b> {A("¡Hola! Me llamo …", "min-width:60mm")}<br><b>A:</b> Mucho gusto.<br><b>B:</b> {A("Igualmente.", "min-width:60mm")}<br><b>A:</b> ¡Adiós!<br><b>B:</b> {A("¡Adiós! / ¡Hasta luego!", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>3. Escribe.</b> Me llamo … <div class="wline"></div></p>""",
    22, """<p>Próxima clase: leer la tarea en voz alta. Empezar con un saludo (<i>¡Buenos días! / ¡Buenas tardes!</i>) y preguntar: <i>¿Cómo te llamas?</i> En la Unidad 02 llegan <i>¿Qué tal? / ¿Cómo estás?</i> y el alfabeto.</p>""")

    b.extra("Transcripciones", f"""
{sub("01.1", "Pedro en la Ciudad de México (lento y natural)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "Los saludos")}
<p>{" · ".join(S012)}</p>
{sub("01.3", "Las frases")}
<p>{" · ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Esencial 01 - Hola")
