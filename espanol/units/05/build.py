# Speak! Esencial A1 - Unidad 05 "Mis datos" (todo en español latinoamericano, para principiantes absolutos) - built with the shared engine + Spanish layer
# Plan (Aula Internacional Plus 1, unidad 1): datos personales: edad, teléfono, correo; tener (… años); números 0-100; ¿cuál es tu número?
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_es import *
setup(band="A1 · UNIDAD 05", audio_json=os.path.join(HERE, "audio_es-a1-unidad-05.json"), img_dir=os.path.join(HERE, "img"), lang="es-419")

PHOTOS = [("A", "el celular", "celular"), ("B", "el correo electrónico", "correo"), ("C", "el pasaporte", "pasaporte"), ("D", "el cumpleaños", "cumpleaños"),
          ("E", "la tarjeta de visita", "tarjeta"), ("F", "la dirección", "dirección"), ("G", "el formulario", "formulario"), ("H", "la cartera", "cartera")]

SCRIPT = [("Narradora", "Diálogo uno."), ("Recepcionista", "Buenas tardes. ¿Cómo se llama usted?"), ("Pedro", "Pedro Almeida."),
          ("Recepcionista", "¿Cuántos años tiene?"), ("Pedro", "Tengo treinta y dos años."), ("Recepcionista", "¿Y cuál es su número de teléfono?"),
          ("Pedro", "Es el 55 – 23 – 81 – 46 – 07."),
          ("Narradora", "Diálogo dos."), ("Lucía", "Pedro, ¿cuál es tu correo?"), ("Pedro", "Es pedro.almeida@correo.com."),
          ("Lucía", "Gracias. Ah, hoy es el cumpleaños de Javier. Tiene treinta años."), ("Pedro", "¿Treinta? ¡Yo tengo treinta y dos!"),
          ("Narradora", "Diálogo tres."), ("Pedro", "Sofía, ¿cuál es tu número?"), ("Sofía", "Es el 55 – 19 – 72 – 30 – 64."),
          ("Pedro", "¿Cómo? Más despacio, por favor."), ("Sofía", "Cincuenta y cinco… diecinueve… setenta y dos… treinta… sesenta y cuatro."), ("Pedro", "¡Gracias!")]
W052 = ["el celular", "el correo electrónico", "el pasaporte", "el cumpleaños", "la tarjeta de visita", "la dirección", "el formulario", "la cartera"]
N0_20 = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince",
         "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"]
TENS = [(21, "veintiuno"), (22, "veintidós"), (23, "veintitrés"), (30, "treinta"), (40, "cuarenta"), (50, "cincuenta"), (60, "sesenta"),
        (70, "setenta"), (80, "ochenta"), (90, "noventa"), (100, "cien"), (32, "treinta y dos"), (45, "cuarenta y cinco"), (99, "noventa y nueve")]
S053 = ["¿Cuántos años tienes?", "Tengo treinta y dos años.", "¿Cuál es tu número de teléfono?", "Mi correo es pedro.almeida@correo.com."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Página 1
    cover = cover_html(T, "NIVEL A1 · UNIDAD 05", "Mis datos", "La edad, el teléfono y el correo",
                       [("PUEDES", "decir tu edad, tu número de teléfono y tu correo"),
                        ("LENGUA", "¿Cuántos años tienes? · Tengo … años · ¿Cuál es tu número? · 0–100"),
                        ("PRONUNCIACIÓN", "números · ñ · c y z como s")])
    words = sorted(W052, key=lambda w: w.split()[1])
    nums = [(3, "tres"), (7, "siete"), (12, "doce"), (15, "quince"), (16, "dieciséis"), (20, "veinte")]
    nr = "".join(f'<td style="width:16%;text-align:center"><b style="font-size:13pt">{n}</b><br>{A(w, "min-width:20mm")}</td>' for n, w in nums)
    b.page(f"""{sec(1, "Calentamiento: mis datos", "8 min")}
{sub("A", "Escucha y repite. Escribe.", "5 min", "05.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Escucha los números 0–20. Escribe.", "3 min", "05.2")}
<table class="ck"><tr>{nr}</tr></table>""",
    32, """<ol><li>A: Pista 05.2 (primera parte). Mostrar cada foto y preguntar: <i>¿Qué es?</i> El alumno repite y escribe.</li>
<li>B: La misma pista, segunda parte: los números de 0 a 20. El alumno escribe estos seis números con letras. <i>quince</i> con qu; <i>dieciséis</i> con tilde.</li>
<li>Repaso: empezar con <i>¡Hola! ¿Qué tal? ¿A qué te dedicas?</i></li></ol>""", cover=cover)

    b.extra("Panorama de la clase · 55 min", """
<table><tr><th>Fase</th><th>Tiempo</th><th>Objetivo</th><th>Página</th></tr>
<tr><td>1 Calentamiento</td><td>8 min</td><td>8 palabras de datos personales · números 0–20</td><td>1</td></tr>
<tr><td>2 Escucha</td><td>10 min</td><td>Edad, teléfono y correo: tres diálogos cortos</td><td>2</td></tr>
<tr><td>3 Gramática</td><td>10 min</td><td><i>tener</i> (singular) · <i>¿Cuántos años …?</i> · números 21–100</td><td>3–4</td></tr>
<tr><td>4 Laboratorio de pronunciación</td><td>5 min</td><td>Números · ñ · c y z como s</td><td>4</td></tr>
<tr><td>5 Práctica</td><td>8 min</td><td>Completar, escribir números, unir</td><td>5</td></tr>
<tr><td>6 Conversación</td><td>12 min</td><td>Fichas con datos que faltan · preguntas personales</td><td>6</td></tr>
<tr><td>7 Cierre</td><td>2 min</td><td>Autoevaluación y tarea</td><td>7</td></tr></table>
<div class="box"><h4>CÓMO FUNCIONA ESTA GUÍA</h4>Cada página corresponde a la página del Libro del alumno con el mismo número. Tus notas están en el <b>recuadro amarillo</b>.
<span class="red">Las respuestas en rojo</span> no aparecen en el Libro del alumno. Las etiquetas <span class="time">5 min</span> indican el tiempo de cada actividad. Las transcripciones están en la última página.</div>
<div class="box"><h4>SIEMPRE DESPACIO</h4>Tres cosas nuevas: <i>tener</i> en singular para la edad (<i>tengo, tienes, tiene</i>), los números de 0 a 100 y <i>¿Cuál es tu número / tu correo?</i> (<i>arroba, punto</i>). <i>Más despacio, por favor</i> (Unidad 02) vuelve a aparecer. El alumno puede inventar sus datos si prefiere no darlos.</div>
<div class="box sand"><h4>LA HISTORIA</h4>Pedro se inscribe en un gimnasio: la recepcionista le pregunta la edad (32) y el teléfono. Lucía le pide su correo y cuenta que hoy es el cumpleaños de Javier: cumple 30. Sofía le da su número, pero muy rápido: <i>¿Cómo? Más despacio, por favor.</i></div>
<div class="box"><h4>EL PROBLEMA PARA LOS BRASILEÑOS</h4><i>Tenho</i> ✗ → <b>Tengo</b>. <i>Tengo 30 anos</i> ✗ → <b>años</b>, siempre con ñ (sin ñ es otra palabra, muy diferente). <i>veinte y dos</i> ✗ → <b>veintidós</b>: del 21 al 29, una sola palabra. Con <i>usted</i>: <b>¿Cuántos años tiene usted?</b></div>
<div class="box"><h4>LA REALIDAD LATINOAMERICANA</h4>En México los celulares tienen 10 dígitos y se dicen de dos en dos: <i>cincuenta y cinco, veintitrés…</i> El teléfono es el <b>celular</b> en América Latina y el <b>móvil</b> en España. En México, en los cumpleaños se canta <i>Las mañanitas</i>.</div>
<div class="box"><h4>AUDIO</h4>Pista 05.1 Tres diálogos (lento y natural) · Pista 05.2 Palabras y números 0–20 · Pista 05.3 Números 21–100 y frases</div>""")

    # Página 2
    gr = [("1", "Pedro: ¿cuántos años tiene?", ["23", "32"], "32"), ("2", "Javier: ¿cuántos años tiene?", ["30", "13"], "30"), ("3", "El número de Sofía empieza con …", ["55 19", "55 23"], "55 19")]
    wr = "".join(f'<td style="width:33%"><b>Diálogo {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("¿Cuántos años", "tiene", "?"), ("", "Tengo", " treinta y dos años."), ("¿Y cuál es su número de", "teléfono", "?"),
          ("Pedro, ¿cuál es tu", "correo", "?"), ("pedro punto almeida", "arroba", " correo punto com"), ("¿Cómo? Más", "despacio", ", por favor.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Escucha: mis datos", "10 min")}
<p>Pedro da sus datos en el gimnasio, a Lucía y a Sofía.</p>
{audiocard(["05.1 · SLOW", "05.1 · NATURAL"])}
{sub("A", "Escucha. Elige.", "3 min", "05.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Escucha otra vez. Completa.", "5 min", "05.1 · NATURAL")}
<div class="bank">arroba · correo · despacio · Tengo · teléfono · tiene</div>
{twocol(gl, 3)}
{sub("C", "Escucha otra vez. Escribe el número de Sofía.", "2 min", "05.1 · NATURAL")}
<div class="wline" style="max-width:80mm">{R("55 19 72 30 64")}</div>""",
    30, """<ol><li>A: versión <b>lenta</b>, dos veces. Antes, preguntar: <i>¿Dónde está Pedro en el diálogo 1?</i> (en un gimnasio, con la recepcionista).</li>
<li>B: versión <b>natural</b>, parar después de cada diálogo. La recepcionista dice <i>su número</i> (usted); Lucía dice <i>tu correo</i> (tú): solo notarlo.</li>
<li>C: El alumno escribe el número con cifras. Si es difícil, el profesor lo dice despacio, de dos en dos.</li></ol>""")

    # Página 3
    tn = [("yo", "tengo", "Tengo 32 años."), ("tú", "tienes", "¿Cuántos años tienes?"), ("él / ella / usted", "tiene", "Javier tiene 30 años.")]
    tt = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in tn)
    nt = [("21–29", "una palabra", "veinti<b>uno</b>, veinti<b>dós</b>"), ("31–99", "decena + <b>y</b> + número", "treinta <b>y</b> dos"), ("100", "", "<b>cien</b>")]
    tg = "".join(f"<tr><td><b>{r}</b></td><td class='small'>{d}</td><td>{e}</td></tr>" for r, d, e in nt)
    chk = [("Pedro: «Yo … 32 años.»", ["tengo", "tiene"], "tengo"), ("25 =", ["veinte y cinco", "veinticinco"], "veinticinco"),
           ("43 =", ["cuarenta y tres", "cuarentaitrés"], "cuarenta y tres"), ("¿Cuántos años … usted?", ["tienes", "tiene"], "tiene")]
    wt = "".join(f'<td style="width:25%"><span class="small">{s}</span><br>{ch(o, a)}</td>' for s, o, a in chk)
    b.page(f"""{sec(3, "Gramática: tener · los números", "10 min")}
{sub("A", "Lee.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">tener</th></tr>{tt}</table></div>
<div><table style="margin:0"><tr><th colspan="3">Los números</th></tr>{tg}</table></div></div>
<div class="box"><h4>LA REGLA</h4>La edad: <b>tener</b> + número + <b>años</b>: <i>Tengo 32 años.</i> (con <b>ñ</b>) &nbsp;·&nbsp; <b>¿Cuál es tu número / tu correo?</b> (tú) · <b>¿Cuál es su número?</b> (usted) → <i>Es el 55…</i> &nbsp;·&nbsp; En el correo: <b>@</b> = arroba · <b>.</b> = punto.</div>
{sub("B", "Elige.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "¿Y tú? Escribe. Puedes inventar los datos.", "3 min")}
<div class="two"><div class="wline">Tengo {R("…")} años.</div><div class="wline">Mi correo es {R("… arroba … punto …")}</div></div>""",
    32, """<ol><li>3A: Explicar primero. <i>tener</i> solo en singular. Como en portugués, la edad va con <i>tener</i>. Los números: del 21 al 29 en una palabra; del 31 en adelante, con <i>y</i>. 100 = <i>cien</i>.</li>
<li>3B: El alumno elige y lee el número en voz alta.</li>
<li>3C: El alumno puede inventar la edad y el correo. Leerlos en voz alta.</li></ol>""")

    # Página 4
    tens_txt = " &nbsp;·&nbsp; ".join(f"{n} {w}" for n, w in TENS)
    b.page(f"""{sub("D", "Errores comunes", "2 min")}
<div class="box sand"><h4>ATENCIÓN: ERRORES COMUNES</h4>
<table style="margin:0"><tr><th>No digas</th><th>Di</th></tr>
<tr><td>Tenho 32 años.</td><td><b>Tengo 32 años.</b></td></tr>
<tr><td>Tengo 30 anos.</td><td><b>Tengo 30 años.</b></td></tr>
<tr><td>veinte y dos</td><td><b>veintidós</b></td></tr>
<tr><td>¿Cuántos años tienes, señora?</td><td><b>¿Cuántos años tiene usted, señora?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio de pronunciación", "5 min")}
{audiocard(["05.2", "05.3"])}
{sub("A", "Escucha y repite: 0–20.", "2 min", "05.2")}
<div class="bank" style="font-weight:600;background:#fff">{" · ".join(N0_20)}</div>
{sub("B", "Escucha y repite: 21–100 y frases.", "3 min", "05.3")}
<div class="bank" style="font-weight:600">{tens_txt}</div>
<div class="box"><h4>SONIDOS</h4><b>ñ</b>: <i>a<b>ñ</b>os</i> &nbsp;·&nbsp; <b>c</b> (ce, ci) y <b>z</b> = <b>s</b>: <i><b>c</b>ero, <b>c</b>inco, on<b>c</b>e, die<b>z</b></i> &nbsp;·&nbsp; <b>v</b> = <b>b</b>: <i><b>v</b>einte, nue<b>v</b>e</i></div>""",
    36, """<ol><li>Errores: <i>tenho</i> viene del portugués. <i>anos</i> sin ñ es una palabra muy diferente: corregir con naturalidad. <i>veintidós</i> en una palabra.</li>
<li>4A/4B: Repetir dos veces. En América Latina, <i>cero, cinco, diez</i> se dicen con <b>s</b>. La <b>v</b> de <i>veinte</i> suena como <b>b</b>. Atención: <i>seis</i> (6) y <i>siete</i> (7); <i>sesenta</i> (60) y <i>setenta</i> (70).</li></ol>""")

    # Página 5
    gw = ["tengo", "tienes", "tiene", "tiene", "tengo", "tienes"]
    gs = [("Yo", " 32 años."), ("¿Cuántos años", " tú?"), ("Javier", " 30 años."), ("¿Cuántos años", " usted, señor?"), ("No", " correo."), ("Sofía, ¿", " WhatsApp?")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    wn = [(18, "dieciocho"), (27, "veintisiete"), (46, "cuarenta y seis"), (65, "sesenta y cinco"), (73, "setenta y tres"), (100, "cien")]
    wl = "".join(f'<td style="width:16%;text-align:center"><b style="font-size:13pt">{n}</b><br>{A(w, "min-width:22mm")}</td>' for n, w in wn)
    mt = [("50", "c", "noventa"), ("90", "d", "sesenta"), ("70", "a", "cincuenta"), ("60", "b", "setenta")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Práctica", "8 min")}
{sub("A", "Completa.", "3 min")}
<div class="bank">tengo · tengo · tiene · tiene · tienes · tienes</div>
{twocol(gl5, 3)}
{sub("B", "Escribe el número.", "3 min")}
<table class="ck"><tr>{wl}</tr></table>
{sub("C", "Une.", "2 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Frase 4: <i>usted</i> → <i>tiene</i>. Frase 5: <i>No tengo correo</i> (aceptar). Frase 6: Sofía es amiga → <i>tienes</i>.</li>
<li>B: Leer cada número en voz alta. C: cuidado con <i>sesenta</i> (60) y <i>setenta</i> (70).</li></ol>""")

    # Página 6
    ppl = [("Valentina Ruiz", "tú", "26", "55 31 48 92 07", "vale.ruiz@correo.com"), ("El señor Ortega", "usted", "64", "55 12 60 75 38", "ortega@correo.com"),
           ("Diego Pérez", "tú", "31", "55 87 24 19 50", "diego.p@correo.com"), ("La señora Vega", "usted", "48", "55 40 93 16 81", "vega@correo.com")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b><span class="small">{f}</span><br>Edad: {R(e) if T else "____"}<br>Tel.:<br>{R(t) if T else "____________________"}<br>Correo:<br>{R(c) if T else "____________________"}</div>' for n, f, e, t, c in ppl)
    b.page(f"""{sec(6, "Conversación", "12 min")}
{sub("A", "Pregunta al profesor. Escribe los datos.", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> ¿Cuántos años tiene usted?<br><b>B:</b> Tengo 64 años.<br><b>A:</b> ¿Cuál es su número de teléfono?<br><b>B:</b> Es el 55 12 60 75 38.</div>
{sub("B", "Contesta al profesor. Puedes inventar los datos.", "5 min")}
<ol style="line-height:1.8"><li>¿Cuántos años tienes?</li><li>¿Cuál es tu número de teléfono?</li><li>¿Cuál es tu correo?</li><li>¿Cuántos años tiene Javier? ¿Y Pedro?</li></ol>""",
    28, """<ol><li>A: El profesor es cada persona y contesta con los datos en rojo. El alumno elige <i>tú</i> o <i>usted</i> según la ficha y escribe. Los teléfonos, de dos en dos. Si el alumno no entiende: <i>Más despacio, por favor.</i></li>
<li>B: Respuestas libres; el alumno puede inventar sus datos. Pregunta 4: Javier tiene 30; Pedro, 32.</li></ol>""")

    # Página 7
    pc = [("Unidad 03", "Puedo decir de dónde soy y mi nacionalidad."), ("Unidad 04", "Puedo decir mi profesión y dónde trabajo."),
          ("Unidad 05", "Puedo decir mi edad: Tengo … años."), ("Unidad 05", "Puedo decir y entender números de teléfono y correos.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hn = [(14, "catorce"), (22, "veintidós"), (38, "treinta y ocho"), (57, "cincuenta y siete"), (81, "ochenta y uno"), (96, "noventa y seis")]
    hl = "".join(f'<td style="width:16%;text-align:center"><b>{n}</b><br>{A(w, "min-width:22mm")}</td>' for n, w in hn)
    b.page(f"""{sec(7, "Cierre y tarea", "2 min")}
{sub("A", "Autoevaluación", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En español …</th><th style="width:18mm">¡Fácil!</th><th style="width:18mm">A veces</th><th style="width:18mm">Todavía no</th></tr>{pcr}</table>
{sub("B", "Tarea", "1 min")}
<p><b>1. Escribe los números.</b></p>
<table class="ck"><tr>{hl}</tr></table>
<p style="margin-top:2mm"><b>2. Completa el formulario. Puedes inventar los datos.</b></p>
<div class="msg">Nombre: {A("…", "min-width:55mm")}<br>Edad: {A("… años", "min-width:55mm")}<br>Teléfono: {A("…", "min-width:55mm")}<br>Correo: {A("…", "min-width:55mm")}</div>
<p style="margin-top:2mm"><b>3. Escribe tus datos en una frase: Tengo … años y mi número es …</b></p>
<div class="wline"></div>""",
    22, """<p>Próxima clase: empezar con <i>¡Hola! ¿Qué tal? ¿Cuántos años tienes?</i> El alumno dicta su número del formulario y el profesor lo escribe. En la Unidad 06: <i>Quiero aprender español</i>.</p>""")

    b.extra("Transcripciones", f"""
{sub("05.1", "Mis datos (lento y natural)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("05.2", "Palabras y números 0–20")}
<p>{" · ".join(W052)} · {" · ".join(N0_20)}</p>
{sub("05.3", "Números 21–100 y frases")}
<p>{" · ".join(f"{n} {w}" for n, w in TENS)} · {" · ".join(S053)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Esencial 05 - Mis datos")
