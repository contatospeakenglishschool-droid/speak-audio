# Speak! Esencial A1 - Unidad 02 "¿Cómo se escribe?" (todo en español latinoamericano, para principiantes absolutos) - built with the shared engine + Spanish layer
# Plan 2026-10-27 (Aula Internacional Plus 1, unidad 0): ¿qué tal?, el alfabeto, frases de la clase.
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
          ("Lucía", "¡Muy bien! Pedro, ¿cómo se escribe Almeida?"), ("Pedro", "A – ele – eme – e – i – de – a."),
          ("Lucía", "Perdón… más despacio, por favor."), ("Pedro", "A… ele… eme… e… i… de… a."), ("Lucía", "¡Gracias!"),
          ("Narradora", "Diálogo tres."), ("Paco", "¡Hola, Pedro! ¿Cómo estás?"), ("Pedro", "Más o menos. Estoy cansado. ¿Y tú?"),
          ("Paco", "¡Muy bien! ¿Cómo se escribe tu nombre?"), ("Pedro", "Pe – e – de – erre – o."),
          ("Paco", "¡Un café para Pedro! ¿Con popote?"), ("Pedro", "¿Qué significa «popote»?"), ("Paco", "Esto. Un popote."), ("Pedro", "¡Ah! No, gracias.")]
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
    cover = cover_html(T, "NIVEL A1 · UNIDAD 02", "¿Cómo se escribe?", "¿Qué tal? · el alfabeto · frases para la clase",
                       [("PUEDES", "preguntar cómo está alguien, deletrear tu nombre y pedir ayuda en clase"),
                        ("LENGUA", "¿Qué tal? · ¿Cómo se escribe? · ¿Qué significa …? · Más despacio, por favor."),
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
<li>B: El profesor pregunta: <i>¿Qué tal?</i> El alumno señala la palabra y la dice. Después, el alumno pregunta al profesor.</li></ol>""", cover=cover)

    b.extra("Panorama de la clase · 55 min", """
<table><tr><th>Fase</th><th>Tiempo</th><th>Objetivo</th><th>Página</th></tr>
<tr><td>1 Calentamiento</td><td>8 min</td><td>¿Qué tal? 8 respuestas con fotos</td><td>1</td></tr>
<tr><td>2 Escucha</td><td>10 min</td><td>El segundo día de Pedro: tres diálogos cortos</td><td>2</td></tr>
<tr><td>3 Gramática</td><td>10 min</td><td><i>¿Qué tal? / ¿Cómo está usted?</i> · frases para la clase</td><td>3–4</td></tr>
<tr><td>4 Laboratorio de pronunciación</td><td>5 min</td><td>El alfabeto · deletrear nombres</td><td>4</td></tr>
<tr><td>5 Práctica</td><td>8 min</td><td>Completar, ordenar, unir</td><td>5</td></tr>
<tr><td>6 Conversación</td><td>12 min</td><td>Cuatro personas: ¿Qué tal? · dictado de apellidos</td><td>6</td></tr>
<tr><td>7 Cierre</td><td>2 min</td><td>Autoevaluación y tarea</td><td>7</td></tr></table>
<div class="box"><h4>CÓMO FUNCIONA ESTA GUÍA</h4>Cada página corresponde a la página del Libro del alumno con el mismo número. Tus notas están en el <b>recuadro amarillo</b>.
<span class="red">Las respuestas en rojo</span> no aparecen en el Libro del alumno. Las etiquetas <span class="time">5 min</span> indican el tiempo de cada actividad. Las transcripciones están en la última página.</div>
<div class="box"><h4>SIEMPRE DESPACIO</h4>Hay tres cosas nuevas, todas como frases hechas, sin conjugación: <i>¿Qué tal? / ¿Cómo estás? / ¿Cómo está usted?</i> con sus respuestas, el alfabeto con <i>¿Cómo se escribe?</i> y las frases para la clase (<i>¿Cómo se dice …? ¿Qué significa …? Más despacio, por favor.</i>). Desde hoy, el alumno usa estas frases en todas las clases. Todo lo de la Unidad 01 vuelve a aparecer.</div>
<div class="box sand"><h4>LA HISTORIA</h4>El segundo día de Pedro en la Ciudad de México. Por la mañana saluda a doña Carmen (usted). En la oficina, Lucía le pregunta cómo se escribe <i>Almeida</i> y le pide: <i>más despacio, por favor</i>. Por la noche, en el café, Paco escribe su nombre en el vaso y le ofrece un <i>popote</i>. Pedro no sabe qué es: <i>¿Qué significa «popote»?</i></div>
<div class="box"><h4>EL PROBLEMA PARA LOS BRASILEÑOS</h4><i>Estoy muy bueno</i> ✗ → <b>Estoy muy bien</b>: <i>bueno</i> no es <i>bien</i> (y <i>estar bueno</i> significa otra cosa). <i>Bien, obrigado</i> ✗ → <b>Bien, gracias</b>. <i>¿Cómo se fala …?</i> ✗ → <b>¿Cómo se dice …?</b> En el alfabeto: <b>J</b> = jota, <b>G</b> = ge (sonido fuerte), <b>H</b> = hache, <b>Ñ</b> = eñe, <b>Y</b> = ye.</div>
<div class="box"><h4>LA REALIDAD LATINOAMERICANA</h4>El <b>popote</b> (México) tiene muchos nombres: <i>pitillo</i> (Colombia, Venezuela), <i>bombilla</i> (Chile), <i>sorbete</i> (Argentina, Uruguay), <i>pajilla</i> (Centroamérica); en España, <i>pajita</i>. Por eso <i>¿Qué significa …?</i> es tan útil. La <b>B</b> se llama «be grande» o «be larga» y la <b>V</b>, «ve chica» o «ve corta», porque suenan igual. En México, entre jóvenes, se oye <b>¿Qué onda?</b></div>
<div class="box"><h4>AUDIO</h4>Pista 02.1 Tres diálogos (lento y natural) · Pista 02.2 ¿Qué tal? · Pista 02.3 El alfabeto</div>""")

    # Página 2
    gr = [("1", "Doña Carmen", ["Muy bien.", "Mal."], "Muy bien."), ("2", "Lucía", ["¡Muy bien!", "Más o menos."], "¡Muy bien!"), ("3", "Pedro", ["¡Excelente!", "Más o menos."], "Más o menos.")]
    wr = "".join(f'<td style="width:33%"><b>Diálogo {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("¿Cómo", "está", " usted?"), ("¡Hola, Pedro! ¿Qué", "tal", "?"), ("¿Cómo se", "escribe", " Almeida?"),
          ("Perdón… más", "despacio", ", por favor."), ("¿Qué", "significa", " «popote»?"), ("¡Ah! No,", "gracias", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Escucha: el segundo día de Pedro", "10 min")}
<p>Es el segundo día de Pedro en la Ciudad de México. Habla con doña Carmen, con Lucía y con Paco.</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Escucha. ¿Cómo está? Elige.", "3 min", "02.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Escucha otra vez. Completa.", "5 min", "02.1 · NATURAL")}
<div class="bank">despacio · escribe · está · gracias · significa · tal</div>
{twocol(gl, 3)}
{sub("C", "Lee los diálogos con el profesor.", "2 min")}""",
    30, """<ol><li>A: versión <b>lenta</b>, dos veces. Antes, preguntar: <i>¿Quién es?</i> (doña Carmen, Lucía y Paco, de la Unidad 01).</li>
<li>B: versión <b>natural</b>, parar después de cada diálogo. Pedro deletrea <i>Almeida</i> y <i>Pedro</i>: solo mostrarlo; el alfabeto llega en la página 4. <i>Popote</i>: mostrar uno (o una foto) después de escuchar.</li>
<li>C: Los diálogos están en la última página. El alumno es Pedro; después, cambiar.</li></ol>""")

    # Página 3
    cls = [("¿Cómo se escribe …?", "¿Cómo se escribe «Juárez»?"), ("¿Cómo se dice … en español?", "¿Cómo se dice esto en español?"),
           ("¿Qué significa …?", "¿Qué significa «popote»?"), ("Más despacio, por favor.", ""), ("Otra vez, por favor.", ""), ("No entiendo.", "")]
    tc = "".join(f"<tr><td><b>{p}</b></td><td class='small'>{e}</td></tr>" for p, e in cls)
    sit = [("Hablas con doña Carmen.", ["¿Qué tal?", "¿Cómo está usted?"], "¿Cómo está usted?"),
           ("El profesor habla muy rápido.", ["Más despacio, por favor.", "Mucho gusto."], "Más despacio, por favor."),
           ("No entiendes «popote».", ["¿Cómo estás?", "¿Qué significa «popote»?"], "¿Qué significa «popote»?"),
           ("Quieres escribir «Juárez».", ["¿Cómo se escribe?", "¡Hasta luego!"], "¿Cómo se escribe?")]
    wt = "".join(f'<td style="width:25%"><span class="small">{s}</span><br>{ch(o, a)}</td>' for s, o, a in sit)
    b.page(f"""{sec(3, "Gramática: ¿Qué tal? · frases para la clase", "10 min")}
{sub("A", "Lee.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th>tú</th><th>usted</th></tr>
<tr><td>¿Qué tal?<br>¿Cómo estás?</td><td>¿Cómo está usted?</td></tr>
<tr><td>Bien, gracias. ¿Y <b>tú</b>?</td><td>Bien, gracias. ¿Y <b>usted</b>?</td></tr>
<tr><td colspan="2" class="small">Estoy bien. · Estoy cansado. · Estoy cansada.</td></tr></table></div>
<div><table style="margin:0"><tr><th colspan="2">En la clase</th></tr>{tc}</table></div></div>
<div class="box"><h4>ATENCIÓN</h4>Estoy muy <b>bien</b>. &nbsp;No: <i>Estoy muy bueno.</i> &nbsp;·&nbsp; ¿Cómo se <b>dice</b>? &nbsp;No: <i>¿Cómo se fala?</i></div>
{sub("B", "¿Qué dices? Elige.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "¿Y tú? Escribe.", "3 min")}
<div class="two"><div class="wline">¿Qué tal? – {R("Bien, gracias. / Más o menos. / …")}</div><div class="wline">Mi nombre se escribe: {R("… (deletrear)")}</div></div>""",
    32, """<ol><li>A: Todo son frases hechas: no explicar la conjugación de <i>estar</i> ni de <i>decir</i> (llegan más adelante). Repaso: <i>tú</i> = amigos, <i>usted</i> = señor / señora. <i>¿Qué tal?</i> es solo informal.</li>
<li>Desde hoy, el alumno usa las frases de la clase siempre que lo necesite: pegarlas en un lugar visible o volver a esta página.</li>
<li>B: Leer cada situación en voz alta y mostrarla con gestos (hablar rápido, no entender, escribir).</li></ol>""")

    # Página 4
    abc = "".join(f'<td style="width:11%;text-align:center;padding:1.2mm 0.5mm{";background:#f3ead8" if l in HOT else ""}"><b style="font-size:12pt">{l}</b><br><span class="small">{n}</span></td>' + ("</tr><tr>" if (i + 1) % 9 == 0 and i < len(ABC) - 1 else "") for i, (l, n) in enumerate(ABC))
    names = ["Lucía", "Paco", "Carmen", "México", "Juárez", "tu nombre"]
    b.page(f"""{sub("D", "Errores comunes", "2 min")}
<div class="box sand"><h4>ATENCIÓN: ERRORES COMUNES</h4>
<table style="margin:0"><tr><th>No digas</th><th>Di</th></tr>
<tr><td>Estoy muy bueno.</td><td><b>Estoy muy bien.</b></td></tr>
<tr><td>Bien, obrigado.</td><td><b>Bien, gracias.</b></td></tr>
<tr><td>¿Cómo se fala «popote»?</td><td><b>¿Cómo se dice «popote»?</b></td></tr>
<tr><td>¿Cómo estás, doña Carmen?</td><td><b>¿Cómo está usted, doña Carmen?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio de pronunciación: el alfabeto", "5 min")}
{audiocard(["02.3"])}
{sub("A", "Escucha y repite.", "3 min", "02.3")}
<table class="ck" style="table-layout:fixed"><tr>{abc}</tr></table>
<div class="box"><h4>DIFERENTE DEL PORTUGUÉS</h4>Las letras de color: <b>G</b> [ge] &nbsp;·&nbsp; <b>H</b> [hache] &nbsp;·&nbsp; <b>J</b> [jota] &nbsp;·&nbsp; <b>Ñ</b> [eñe] &nbsp;·&nbsp; <b>Q</b> [cu] &nbsp;·&nbsp; <b>R</b> [erre] &nbsp;·&nbsp; <b>V</b> [ve] &nbsp;·&nbsp; <b>W</b> [doble ve] &nbsp;·&nbsp; <b>Y</b> [ye] &nbsp;·&nbsp; <b>Z</b> [zeta]</div>
{sub("B", "Deletrea.", "2 min")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(names)}</div>""",
    38, """<ol><li>Errores: corregir enseguida <i>Estoy muy bueno</i>, <i>obrigado</i> y <i>¿Cómo se fala?</i>.</li>
<li>4A: Pista 02.3 dos veces. Las letras de color son difíciles para brasileños: la <b>J</b> y la <b>G</b> (antes de e, i) suenan fuerte, casi como la «rr» de «carro»; la <b>Ñ</b> = «nh»; la <b>Q</b> = «cu», no «quê»; la <b>V</b> suena igual que la <b>B</b>. La <b>H</b> no suena.</li>
<li>4B: El alumno deletrea y el profesor escribe. Después, al revés. Si no entiende: <i>Más despacio, por favor. / Otra vez, por favor.</i></li></ol>""")

    # Página 5
    gw = ["tal", "está", "escribe", "significa", "dice", "despacio"]
    gs = [("¿Qué", ", Lucía?"), ("¿Cómo", " usted, doña Carmen?"), ("¿Cómo se", " «Juárez»?"), ("¿Qué", " «popote»?"), ("¿Cómo se", " esto en español?"), ("Más", ", por favor.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("despacio / más / , / por favor", "Más despacio, por favor."), ("significa / qué / «popote» / ¿ / ?", "¿Qué significa «popote»?"), ("se / escribe / cómo / tu nombre / ¿ / ?", "¿Cómo se escribe tu nombre?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("¿Qué tal?", "c", "Pe – e – de – erre – o."), ("¿Cómo está usted?", "d", "Esto. Un popote."), ("¿Cómo se escribe Pedro?", "a", "Bien, ¿y tú?"), ("¿Qué significa «popote»?", "b", "Muy bien, gracias. ¿Y usted?")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Práctica", "8 min")}
{sub("A", "Completa.", "3 min")}
<div class="bank">despacio · dice · escribe · está · significa · tal</div>
{twocol(gl5, 3)}
{sub("B", "Ordena.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Une.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Frase 2: <i>doña Carmen</i> → usted → <i>¿Cómo está usted?</i> Frase 5: el profesor señala un objeto de la sala (un libro, una taza).</li>
<li>C: Leer los pares en voz alta. El profesor pregunta, el alumno contesta.</li></ol>""")

    # Página 6
    ppl = [("Lucía", "colega · ¡Excelente!"), ("Doña Carmen", "casera · Bien."), ("Paco", "café · cansado"), ("La doctora Méndez", "médica · Más o menos.")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + ("¿Cómo está usted?" if n.startswith(("Doña", "La doctora")) else "¿Qué tal? / ¿Cómo estás?"))}</div>' for n, d in ppl)
    b.page(f"""{sec(6, "Conversación", "12 min")}
{sub("A", "Juega con el profesor. Saluda. Pregunta: ¿Qué tal?", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> ¡Buenos días, doña Carmen! ¿Cómo está usted?<br><b>B:</b> Bien, gracias. ¿Y usted?<br><b>A:</b> Más o menos. Estoy cansado.</div>
{sub("B", "Escucha y escribe los apellidos. Pide ayuda: «Más despacio, por favor.»", "5 min")}
<ol style="line-height:2"><li>{A("HERRERA", "min-width:55mm")}</li><li>{A("ROJAS", "min-width:55mm")}</li><li>{A("ZAPATA", "min-width:55mm")}</li><li>{A("VILLAGÓMEZ", "min-width:55mm")}</li></ol>""",
    30, """<ol><li>A: El profesor hace las cuatro personas y contesta como en la tarjeta. El alumno elige <i>¿Qué tal? / ¿Cómo estás?</i> o <i>¿Cómo está usted?</i> Después, cambiar.</li>
<li>B: El profesor deletrea rápido a propósito la primera vez, para que el alumno pida <i>Más despacio, por favor</i> u <i>Otra vez, por favor</i>: H-E-R-R-E-R-A, R-O-J-A-S, Z-A-P-A-T-A, V-I-L-L-A-G-O-M-E-Z («con tilde en la o»). El alumno escribe y lee el apellido en voz alta.</li></ol>""")

    # Página 7
    pc = [("Unidad 01", "Puedo saludar y decir mi nombre."), ("Unidad 02", "Puedo preguntar: ¿Qué tal? / ¿Cómo está usted?"),
          ("Unidad 02", "Puedo deletrear mi nombre."), ("Unidad 02", "Puedo pedir ayuda en clase (¿Qué significa …? Más despacio …).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw2 = [("No entiendes una palabra.", "¿Qué significa …?"), ("El profesor habla rápido.", "Más despacio, por favor."), ("No sabes escribir un nombre.", "¿Cómo se escribe …?")]
    hl = "".join(f"<li>{s} {A(a, 'min-width:45mm')}</li>" for s, a in hw2)
    b.page(f"""{sec(7, "Cierre y tarea", "2 min")}
{sub("A", "Autoevaluación", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En español …</th><th style="width:18mm">¡Fácil!</th><th style="width:18mm">A veces</th><th style="width:18mm">Todavía no</th></tr>{pcr}</table>
{sub("B", "Tarea", "1 min")}
<p><b>1. Completa el diálogo.</b></p>
<div class="msg"><b>Lucía:</b> ¡Hola, Pedro! ¿Qué tal?<br><b>Pedro:</b> {A("Bien, gracias. ¿Y tú?", "min-width:60mm")}<br><b>Lucía:</b> ¡Muy bien, gracias!<br><br>
<b>Pedro:</b> ¡Buenas tardes, doña Carmen! ¿Cómo está usted?<br><b>Doña Carmen:</b> {A("Muy bien, gracias. ¿Y usted?", "min-width:60mm")}<br><b>Pedro:</b> {A("Más o menos. Estoy cansado.", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>2. ¿Qué dices? Escribe.</b></p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>3. Escribe tu nombre y tu ciudad.</b> Deletréalos en la próxima clase.</p>
<div class="wline"></div>""",
    22, """<p>Próxima clase: empezar con <i>¡Hola! ¿Qué tal?</i> El alumno deletrea su nombre y su ciudad (ejercicio 3) y el profesor escribe. Usar las frases de la clase desde el primer minuto. En la Unidad 03 llegan los países: <i>¿De dónde eres?</i></p>""")

    b.extra("Transcripciones", f"""
{sub("02.1", "El segundo día de Pedro (lento y natural)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "¿Qué tal?")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "El alfabeto")}
<p>{" · ".join(f"{l} ({n})" for l, n in ABC)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Esencial 02 - Como se escribe")
