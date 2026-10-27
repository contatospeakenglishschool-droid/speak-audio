# Speak! Esencial A1 - Unidad 02 "¿Qué tal?" (todo en español latinoamericano, para principiantes absolutos) - built with the shared engine + Spanish layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_es import *
setup(band="A1 · UNIDAD 02", audio_json=os.path.join(HERE, "audio_es-a1-unidad-02.json"), img_dir=os.path.join(HERE, "img"), lang="es-419")

PHOTOS = [("A", "¡Excelente!", "excelente"), ("B", "¡Muy bien!", "muy bien"), ("C", "Bien.", "bien"), ("D", "Más o menos.", "más o menos"),
          ("E", "Regular.", "regular"), ("F", "Mal.", "mal"), ("G", "cansado", "cansado"), ("H", "enferma", "enferma")]

SCRIPT = [("Narradora", "Diálogo uno."), ("Pedro", "¡Buenos días, doña Carmen! ¿Cómo está usted?"),
          ("Doña Carmen", "Muy bien, gracias. ¿Y usted, señor Almeida?"), ("Pedro", "Bien, gracias."),
          ("Narradora", "Diálogo dos."), ("Lucía", "¡Hola, Pedro! ¿Qué tal?"), ("Pedro", "Bien, ¿y tú?"),
          ("Lucía", "¡Muy bien! Pedro, ¿cómo se escribe Almeida?"), ("Pedro", "A – ele – eme – e – i – de – a."), ("Lucía", "¡Gracias!"),
          ("Narradora", "Diálogo tres."), ("Paco", "¡Hola, Pedro! ¿Cómo estás?"), ("Pedro", "Más o menos. Estoy cansado. ¿Y tú?"),
          ("Paco", "¡Excelente! Un café… ¿Cómo se escribe tu nombre?"), ("Pedro", "Pe – e – de – erre – o."), ("Paco", "¡Un café para Pedro!")]
S022 = ["¡Excelente!", "¡Muy bien!", "Bien.", "Más o menos.", "Regular.", "Mal.", "cansado, cansada", "enfermo, enferma"]
ABC = [("A", "a"), ("B", "be"), ("C", "ce"), ("D", "de"), ("E", "e"), ("F", "efe"), ("G", "ge"), ("H", "hache"), ("I", "i"), ("J", "jota"),
       ("K", "ka"), ("L", "ele"), ("M", "eme"), ("N", "ene"), ("Ñ", "eñe"), ("O", "o"), ("P", "pe"), ("Q", "cu"), ("R", "erre"), ("S", "ese"),
       ("T", "te"), ("U", "u"), ("V", "ve"), ("W", "doble ve"), ("X", "equis"), ("Y", "ye"), ("Z", "zeta")]
HOT = {"G", "H", "J", "Ñ", "Q", "R", "V", "W", "Y", "Z"}


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Página 1
    cover = cover_html(T, "NIVEL A1 · UNIDAD 02", "¿Qué tal?", "Preguntar y decir cómo estás · el alfabeto",
                       [("PUEDES", "preguntar cómo está alguien, contestar y deletrear tu nombre"),
                        ("LENGUA", "¿Qué tal? · ¿Cómo estás? / ¿Cómo está usted? · estoy, estás, está"),
                        ("PRONUNCIACIÓN", "el alfabeto · j, g, r, ñ")])
    words = ["cansado", "enferma", "Bien.", "¡Excelente!", "Mal.", "Más o menos.", "¡Muy bien!", "Regular."]
    me = "".join(f'<td style="text-align:center">☐<br><span class="small">{w}</span></td>' for w in ["¡Excelente!", "¡Muy bien!", "Bien.", "Más o menos.", "Regular.", "Mal."])
    b.page(f"""{sec(1, "Calentamiento: ¿Qué tal?", "8 min")}
{sub("A", "Escucha y repite. Escribe.", "5 min", "02.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "¿Y tú? ¿Cómo estás hoy? Marca.", "3 min")}
<table class="ck"><tr>{me}</tr></table>""",
    30, """<ol><li>A: Pista 02.2. Mostrar con la cara y con gestos: pulgar arriba = <b>¡Excelente! / ¡Muy bien!</b>, mano que oscila = <b>Más o menos. / Regular.</b>, pulgar abajo = <b>Mal.</b> Repaso de la Unidad 01: empezar con <i>¡Hola! / ¡Buenos días!</i></li>
<li>G y H: <b>cansado</b> (hombre) / <b>cansada</b> (mujer), <b>enfermo</b> / <b>enferma</b>. Solo mostrarlo; no explicar el género todavía.</li>
<li>B: El profesor pregunta: <i>¿Cómo estás?</i> El alumno señala la palabra y la dice. Después, el alumno pregunta al profesor.</li></ol>""", cover=cover)

    b.extra("Panorama de la clase · 55 min", """
<table><tr><th>Fase</th><th>Tiempo</th><th>Objetivo</th><th>Página</th></tr>
<tr><td>1 Calentamiento</td><td>8 min</td><td>¿Qué tal? 8 respuestas con fotos</td><td>1</td></tr>
<tr><td>2 Escucha</td><td>10 min</td><td>El segundo día de Pedro: tres diálogos cortos</td><td>2</td></tr>
<tr><td>3 Gramática</td><td>10 min</td><td><i>estar</i> (singular) · <i>¿Cómo estás? / ¿Cómo está usted?</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio de pronunciación</td><td>5 min</td><td>El alfabeto · deletrear nombres</td><td>4</td></tr>
<tr><td>5 Práctica</td><td>8 min</td><td>Completar, ordenar, unir</td><td>5</td></tr>
<tr><td>6 Conversación</td><td>12 min</td><td>Cuatro personas: ¿Cómo estás? · dictado de apellidos</td><td>6</td></tr>
<tr><td>7 Cierre</td><td>2 min</td><td>Autoevaluación y tarea</td><td>7</td></tr></table>
<div class="box"><h4>CÓMO FUNCIONA ESTA GUÍA</h4>Cada página corresponde a la página del Libro del alumno con el mismo número. Tus notas están en el <b>recuadro amarillo</b>.
<span class="red">Las respuestas en rojo</span> no aparecen en el Libro del alumno. Las etiquetas <span class="time">5 min</span> indican el tiempo de cada actividad. Las transcripciones están en la última página.</div>
<div class="box"><h4>SIEMPRE DESPACIO</h4>Solo hay tres cosas nuevas: <i>¿Qué tal? / ¿Cómo estás? / ¿Cómo está usted?</i> con sus respuestas, las formas de <i>estar</i> en singular y el alfabeto. Todo lo de la Unidad 01 (saludos, <i>Me llamo …</i>, <i>¿Cómo te llamas?</i>) vuelve a aparecer. Hablar despacio, mostrar mucho y repetir.</div>
<div class="box sand"><h4>LA HISTORIA</h4>El segundo día de Pedro en la Ciudad de México. Por la mañana saluda a doña Carmen (usted). En la oficina, Lucía le pregunta cómo se escribe <i>Almeida</i>. Por la noche, en el café, Pedro está cansado. Paco escribe su nombre en el vaso: <i>¡Un café para Pedro!</i></div>
<div class="box"><h4>EL PROBLEMA PARA LOS BRASILEÑOS</h4><i>Estoy muy bueno</i> ✗ → <b>Estoy muy bien</b>: <i>bueno</i> no es <i>bien</i> (y <i>estar bueno</i> significa otra cosa). <i>Bien, obrigado</i> ✗ → <b>Bien, gracias</b>. Con <i>señor / señora / doña</i>: <b>¿Cómo está usted?</b>, no <i>¿Cómo estás?</i> En el alfabeto: <b>J</b> = jota, <b>G</b> = ge (con sonido fuerte), <b>H</b> = hache, <b>Ñ</b> = eñe, <b>Y</b> = ye.</div>
<div class="box"><h4>LA REALIDAD LATINOAMERICANA</h4>En México, entre jóvenes, se oye <b>¿Qué onda?</b> (muy informal). En muchos países, la <b>B</b> se llama «be grande» o «be larga» y la <b>V</b>, «ve chica» o «ve corta», porque suenan igual. La <b>Y</b> también se llama «i griega». En las cafeterías es normal escribir el nombre del cliente en el vaso.</div>
<div class="box"><h4>AUDIO</h4>Pista 02.1 Tres diálogos (lento y natural) · Pista 02.2 ¿Qué tal? · Pista 02.3 El alfabeto</div>""")

    # Página 2
    gr = [("1", "Doña Carmen", ["Muy bien.", "Mal."], "Muy bien."), ("2", "Lucía", ["¡Muy bien!", "Más o menos."], "¡Muy bien!"), ("3", "Pedro", ["¡Excelente!", "Más o menos."], "Más o menos.")]
    wr = "".join(f'<td style="width:33%"><b>Diálogo {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("¿Cómo", "está", " usted?"), ("¡Hola, Pedro! ¿Qué", "tal", "?"), ("Bien, ¿y", "tú", "?"),
          ("¿Cómo se", "escribe", " Almeida?"), ("Más o menos.", "Estoy", " cansado."), ("¡Hola, Pedro! ¿Cómo", "estás", "?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Escucha: el segundo día de Pedro", "10 min")}
<p>Es el segundo día de Pedro en la Ciudad de México. Habla con doña Carmen, con Lucía y con Paco.</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Escucha. ¿Cómo está? Elige.", "3 min", "02.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Escucha otra vez. Completa.", "5 min", "02.1 · NATURAL")}
<div class="bank">escribe · está · estás · Estoy · tal · tú</div>
{twocol(gl, 3)}
{sub("C", "Lee los diálogos con el profesor.", "2 min")}""",
    30, """<ol><li>A: versión <b>lenta</b>, dos veces. Antes, preguntar: <i>¿Quién es?</i> (doña Carmen, Lucía y Paco, de la Unidad 01).</li>
<li>B: versión <b>natural</b>, parar después de cada diálogo. Pedro deletrea <i>Almeida</i> y <i>Pedro</i>: solo mostrarlo; el alfabeto llega en la página 4.</li>
<li>C: Los diálogos están en la última página. El alumno es Pedro; después, cambiar.</li></ol>""")

    # Página 3
    est = [("yo", "estoy", "Estoy bien."), ("tú", "estás", "¿Cómo estás?"), ("él / ella", "está", "Lucía está muy bien."), ("usted", "está", "¿Cómo está usted?")]
    ts = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in est)
    who = [("Lucía", "colega", "¿Y tú?"), ("Doña Carmen", "casera", "¿Y usted?"), ("Paco", "café", "¿Y tú?"), ("La doctora Méndez", "médica", "¿Y usted?")]
    wt = "".join(f'<td style="width:25%"><b>{n}</b><br><span class="small">{d}</span><br>{ch(["¿Y tú?", "¿Y usted?"], a)}</td>' for n, d, a in who)
    b.page(f"""{sec(3, "Gramática: estar · ¿Cómo estás?", "10 min")}
{sub("A", "Lee.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">estar</th></tr>{ts}</table></div>
<div><table style="margin:0"><tr><th>tú</th><th>usted</th></tr>
<tr><td>¿Qué tal?<br>¿Cómo <b>estás</b>?</td><td>¿Cómo <b>está usted</b>?</td></tr>
<tr><td>Bien, gracias. ¿Y <b>tú</b>?</td><td>Bien, gracias. ¿Y <b>usted</b>?</td></tr></table></div></div>
<div class="box"><h4>ATENCIÓN</h4>Estoy muy <b>bien</b>. &nbsp;No: <i>Estoy muy bueno.</i> &nbsp;·&nbsp; Pedro está cansad<b>o</b>. Lucía está cansad<b>a</b>.</div>
{sub("B", "¿Y tú? o ¿Y usted? Elige.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "¿Y tú? Escribe.", "3 min")}
<div class="two"><div class="wline">¿Cómo estás? – {R("Bien, gracias. / Más o menos. / …")}</div><div class="wline">Me llamo {R("… (nombre)")}</div></div>""",
    32, """<ol><li>A: Solo el singular de <i>estar</i>; el plural (nosotros, ustedes, ellos) llega más adelante. Repaso: <i>tú</i> = amigos, <i>usted</i> = señor / señora. <i>¿Qué tal?</i> es solo informal.</li>
<li>Recuadro: <i>Estoy muy bueno</i> viene del portugués «estou muito bem» mal traducido. Mostrar <b>bien</b> con el pulgar arriba. <i>cansado / cansada</i>: hombre / mujer.</li>
<li>B: Como en la Unidad 01: colega, Paco → tú; doña, doctora → usted.</li></ol>""")

    # Página 4
    abc = "".join(f'<td style="width:11%;text-align:center;padding:1.2mm 0.5mm{";background:#f3ead8" if l in HOT else ""}"><b style="font-size:12pt">{l}</b><br><span class="small">{n}</span></td>' + ("</tr><tr>" if (i + 1) % 9 == 0 and i < len(ABC) - 1 else "") for i, (l, n) in enumerate(ABC))
    names = ["Lucía", "Paco", "Carmen", "México", "Juárez", "tu nombre"]
    b.page(f"""{sub("D", "Errores comunes", "2 min")}
<div class="box sand"><h4>ATENCIÓN: ERRORES COMUNES</h4>
<table style="margin:0"><tr><th>No digas</th><th>Di</th></tr>
<tr><td>Estoy muy bueno.</td><td><b>Estoy muy bien.</b></td></tr>
<tr><td>Bien, obrigado.</td><td><b>Bien, gracias.</b></td></tr>
<tr><td>Tú está cansado.</td><td><b>Tú estás cansado.</b></td></tr>
<tr><td>¿Cómo estás, doña Carmen?</td><td><b>¿Cómo está usted, doña Carmen?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio de pronunciación: el alfabeto", "5 min")}
{audiocard(["02.3"])}
{sub("A", "Escucha y repite.", "3 min", "02.3")}
<table class="ck" style="table-layout:fixed"><tr>{abc}</tr></table>
<div class="box"><h4>DIFERENTE DEL PORTUGUÉS</h4>Las letras de color: <b>G</b> [ge] &nbsp;·&nbsp; <b>H</b> [hache] &nbsp;·&nbsp; <b>J</b> [jota] &nbsp;·&nbsp; <b>Ñ</b> [eñe] &nbsp;·&nbsp; <b>Q</b> [cu] &nbsp;·&nbsp; <b>R</b> [erre] &nbsp;·&nbsp; <b>V</b> [ve] &nbsp;·&nbsp; <b>W</b> [doble ve] &nbsp;·&nbsp; <b>Y</b> [ye] &nbsp;·&nbsp; <b>Z</b> [zeta]</div>
{sub("B", "Deletrea.", "2 min")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(names)}</div>""",
    38, """<ol><li>Errores: corregir enseguida <i>Estoy muy bueno</i> y <i>obrigado</i>. <i>Tú está</i> ✗: con <i>tú</i>, siempre <b>-s</b>: <i>estás</i>.</li>
<li>4A: Pista 02.3 dos veces. Las letras de color son difíciles para brasileños: la <b>J</b> y la <b>G</b> (antes de e, i) suenan fuerte, casi como la «rr» de «carro»; la <b>Ñ</b> = «nh»; la <b>Q</b> = «cu», no «quê»; la <b>V</b> suena igual que la <b>B</b>. La <b>H</b> no suena.</li>
<li>4B: El alumno deletrea y el profesor escribe. Después, al revés. Si no entiende: <i>¿Cómo? Otra vez, por favor.</i></li></ol>""")

    # Página 5
    gw = ["estoy", "estás", "está", "está", "estoy", "estás"]
    gs = [("Yo", " bien."), ("¿Cómo", " tú?"), ("¿Cómo", " usted?"), ("Lucía", " muy bien."), ("Hoy", " cansado."), ("Paco, ¿cómo", "?")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("usted / cómo / está / ¿ / ?", "¿Cómo está usted?"), ("gracias / bien / ,", "Bien, gracias."), ("se / escribe / cómo / ¿ / ?", "¿Cómo se escribe?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("¿Qué tal?", "c", "Pe – e – de – erre – o."), ("¿Cómo está usted?", "d", "¡Adiós!"), ("¿Cómo se escribe Pedro?", "a", "Bien, ¿y tú?"), ("¡Hasta mañana!", "b", "Muy bien, gracias. ¿Y usted?")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Práctica", "8 min")}
{sub("A", "Completa.", "3 min")}
<div class="bank">está · está · estás · estás · estoy · estoy</div>
{twocol(gl5, 3)}
{sub("B", "Ordena.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Une.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Frase 4: <i>Lucía</i> = ella → <i>está</i>, como <i>usted</i>. Frase 6: Paco es amigo → tú → <i>estás</i>.</li>
<li>C: Leer los pares en voz alta. El profesor pregunta, el alumno contesta.</li></ol>""")

    # Página 6
    ppl = [("Lucía", "colega · ¡Excelente!"), ("Doña Carmen", "casera · Bien."), ("Paco", "café · cansado"), ("La doctora Méndez", "médica · Más o menos.")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + ("¿Cómo está usted?" if n.startswith(("Doña", "La doctora")) else "¿Qué tal? / ¿Cómo estás?"))}</div>' for n, d in ppl)
    b.page(f"""{sec(6, "Conversación", "12 min")}
{sub("A", "Juega con el profesor. Saluda. Pregunta: ¿Cómo estás?", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> ¡Buenos días, doña Carmen! ¿Cómo está usted?<br><b>B:</b> Bien, gracias. ¿Y usted?<br><b>A:</b> Más o menos. Estoy cansado.</div>
{sub("B", "Escucha y escribe los apellidos.", "5 min")}
<ol style="line-height:2"><li>{A("HERRERA", "min-width:55mm")}</li><li>{A("ROJAS", "min-width:55mm")}</li><li>{A("ZAPATA", "min-width:55mm")}</li><li>{A("VILLAGÓMEZ", "min-width:55mm")}</li></ol>""",
    30, """<ol><li>A: El profesor hace las cuatro personas y contesta como en la tarjeta. El alumno elige <i>¿Qué tal? / ¿Cómo estás?</i> o <i>¿Cómo está usted?</i> Después, cambiar.</li>
<li>B: El profesor deletrea despacio, dos veces: H-E-R-R-E-R-A, R-O-J-A-S, Z-A-P-A-T-A, V-I-L-L-A-G-O-M-E-Z (la tilde: «con tilde en la o»). El alumno escribe y lee el apellido en voz alta. Practicar: <i>¿Cómo? Otra vez, por favor.</i></li></ol>""")

    # Página 7
    pc = [("Unidad 01", "Puedo saludar y decir mi nombre."), ("Unidad 02", "Puedo preguntar: ¿Qué tal? / ¿Cómo está usted?"),
          ("Unidad 02", "Puedo decir cómo estoy."), ("Unidad 02", "Puedo deletrear mi nombre.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    b.page(f"""{sec(7, "Cierre y tarea", "2 min")}
{sub("A", "Autoevaluación", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En español …</th><th style="width:18mm">¡Fácil!</th><th style="width:18mm">A veces</th><th style="width:18mm">Todavía no</th></tr>{pcr}</table>
{sub("B", "Tarea", "1 min")}
<p><b>1. Completa el diálogo.</b></p>
<div class="msg"><b>Lucía:</b> ¡Hola, Pedro! ¿Qué tal?<br><b>Pedro:</b> {A("Bien, gracias. ¿Y tú?", "min-width:60mm")}<br><b>Lucía:</b> ¡Muy bien, gracias!<br><br>
<b>Pedro:</b> ¡Buenas tardes, doña Carmen! ¿Cómo está usted?<br><b>Doña Carmen:</b> {A("Muy bien, gracias. ¿Y usted?", "min-width:60mm")}<br><b>Pedro:</b> {A("Más o menos. Estoy cansado.", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>2. Completa: estoy, estás o está.</b> &nbsp; Yo {A("estoy", "min-width:14mm")} bien. · ¿Cómo {A("estás", "min-width:14mm")} tú? · Paco {A("está", "min-width:14mm")} cansado. · ¿Cómo {A("está", "min-width:14mm")} usted?</p>
<p style="margin-top:2mm"><b>3. Escribe tu nombre y tu ciudad.</b> Deletréalos en la próxima clase.</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Próxima clase: empezar con <i>¡Hola! ¿Qué tal?</i> El alumno deletrea su nombre y su ciudad (ejercicio 3) y el profesor escribe. En la Unidad 03 llegan los países: <i>¿De dónde eres?</i></p>""")

    b.extra("Transcripciones", f"""
{sub("02.1", "El segundo día de Pedro (lento y natural)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "¿Qué tal?")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "El alfabeto")}
<p>{" · ".join(f"{l} ({n})" for l, n in ABC)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Esencial 02 - Que tal")
