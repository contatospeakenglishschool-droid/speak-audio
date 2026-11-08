# Speak! Esencial A1 - Unidad 03 "¿De dónde eres?" (todo en español latinoamericano, para principiantes absolutos) - built with the shared engine + Spanish layer
# Plan (Aula Internacional Plus 1, unidad 1): nacionalidad y origen; ser (yo, tú, él/ella, usted); género de las nacionalidades.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_es import *
setup(band="A1 · UNIDAD 03", audio_json=os.path.join(HERE, "audio_es-a1-unidad-03.json"), img_dir=os.path.join(HERE, "img"), lang="es-419")

PHOTOS = [("A", "México", "méxico"), ("B", "Brasil", "brasil"), ("C", "Argentina", "argentina"), ("D", "Colombia", "colombia"),
          ("E", "Chile", "chile"), ("F", "Perú", "perú"), ("G", "España", "españa"), ("H", "Estados Unidos", "estados unidos")]

SCRIPT = [("Narradora", "Diálogo uno."), ("Lucía", "Pedro, ¿de dónde eres? ¿De São Paulo?"),
          ("Pedro", "No, soy de Recife. Soy brasileño. ¿Y tú? ¿Eres de aquí?"), ("Lucía", "Sí, soy mexicana. Soy de la Ciudad de México."),
          ("Narradora", "Diálogo dos."), ("Sofía", "¡Hola! Soy Sofía, tu vecina."), ("Pedro", "¡Hola, Sofía! Soy Pedro. ¿Eres mexicana?"),
          ("Sofía", "No, soy española. Soy de Madrid. ¿Y tú?"), ("Pedro", "Soy brasileño, de Recife."), ("Sofía", "¡Ah, Brasil! ¡Qué bien!"),
          ("Narradora", "Diálogo tres."), ("Señor", "Perdón, ¿usted es de Brasil?"), ("Pedro", "Sí, soy brasileño. ¿Y usted? ¿De dónde es?"),
          ("Señor", "Soy argentino, de Buenos Aires."), ("Paco", "¡Y yo soy de Oaxaca! Bienvenidos.")]
NAT = [("México", "mexicano", "mexicana"), ("Brasil", "brasileño", "brasileña"), ("Argentina", "argentino", "argentina"), ("Colombia", "colombiano", "colombiana"),
       ("Chile", "chileno", "chilena"), ("Perú", "peruano", "peruana"), ("España", "español", "española"), ("Estados Unidos", "estadounidense", "estadounidense")]
S032 = [f"{p}: {m}, {f}" if m != f else f"{p}: {m}" for p, m, f in NAT]
S033 = ["¿De dónde eres?", "Soy de Recife.", "Soy brasileño. Soy brasileña.", "¿De dónde es usted?", "Ella es española.", "Él es de México."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Página 1
    cover = cover_html(T, "NIVEL A1 · UNIDAD 03", "¿De dónde eres?", "Decir de dónde eres y tu nacionalidad",
                       [("PUEDES", "preguntar y decir de dónde eres y tu nacionalidad"),
                        ("LENGUA", "¿De dónde eres? · Soy de … · soy, eres, es · mexicano / mexicana"),
                        ("PRONUNCIACIÓN", "países · ñ · la x de México")])
    words = ["Argentina", "Brasil", "Chile", "Colombia", "España", "Estados Unidos", "México", "Perú"]
    nb = [("México", "mexicano", "mexicana"), ("Brasil", "brasileño", "brasileña"), ("Colombia", "colombiano", "colombiana"), ("Perú", "peruano", "peruana")]
    nr = "".join(f'<td style="width:25%;text-align:center"><b>{p}</b><br>♂ {A(m, "min-width:24mm")}<br>♀ {A(f, "min-width:24mm")}</td>' for p, m, f in nb)
    b.page(f"""{sec(1, "Calentamiento: países", "8 min")}
{sub("A", "Escucha y repite. Escribe el país.", "5 min", "03.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Escucha otra vez. Escribe.", "3 min", "03.2")}
<table class="ck"><tr>{nr}</tr></table>""",
    34, """<ol><li>A: Pista 03.2. Mostrar cada foto: ¿qué país es? El alumno repite el país y lo escribe. Mostrar en un mapa dónde está cada país.</li>
<li>B: La misma pista: después del país vienen las dos nacionalidades (hombre / mujer). El alumno escribe solo las de estos cuatro países. No explicar la regla todavía: llega en la página 3.</li>
<li>Repaso: empezar con <i>¡Hola! ¿Qué tal?</i></li></ol>""", cover=cover)

    b.extra("Panorama de la clase · 55 min", """
<table><tr><th>Fase</th><th>Tiempo</th><th>Objetivo</th><th>Página</th></tr>
<tr><td>1 Calentamiento</td><td>8 min</td><td>8 países con fotos · nacionalidades</td><td>1</td></tr>
<tr><td>2 Escucha</td><td>10 min</td><td>¿De dónde eres? Tres diálogos cortos</td><td>2</td></tr>
<tr><td>3 Gramática</td><td>10 min</td><td><i>ser</i> (singular) · <i>Soy de …</i> · nacionalidades: hombre / mujer</td><td>3–4</td></tr>
<tr><td>4 Laboratorio de pronunciación</td><td>5 min</td><td>Países y nacionalidades · ñ · la x de México</td><td>4</td></tr>
<tr><td>5 Práctica</td><td>8 min</td><td>Completar, ordenar, unir</td><td>5</td></tr>
<tr><td>6 Conversación</td><td>12 min</td><td>Cuatro personas: ¿De dónde eres? / ¿De dónde es usted?</td><td>6</td></tr>
<tr><td>7 Cierre</td><td>2 min</td><td>Autoevaluación y tarea</td><td>7</td></tr></table>
<div class="box"><h4>CÓMO FUNCIONA ESTA GUÍA</h4>Cada página corresponde a la página del Libro del alumno con el mismo número. Tus notas están en el <b>recuadro amarillo</b>.
<span class="red">Las respuestas en rojo</span> no aparecen en el Libro del alumno. Las etiquetas <span class="time">5 min</span> indican el tiempo de cada actividad. Las transcripciones están en la última página.</div>
<div class="box"><h4>SIEMPRE DESPACIO</h4>Tres cosas nuevas: <i>¿De dónde eres? / ¿De dónde es usted?</i> con <i>Soy de …</i>, el verbo <i>ser</i> en singular (<i>soy, eres, es</i>) y las nacionalidades en masculino y femenino. Lo de las Unidades 01 y 02 vuelve a aparecer.</div>
<div class="box sand"><h4>LA HISTORIA</h4>El tercer día de Pedro. En la oficina, Lucía le pregunta de dónde es: él es de Recife; ella, de la Ciudad de México. En la escalera conoce a Sofía, su vecina, que es española, de Madrid. En el café, un señor argentino le habla de usted, y Paco cuenta que él es de Oaxaca.</div>
<div class="box"><h4>EL PROBLEMA PARA LOS BRASILEÑOS</h4><i>Soy brasilero</i> ✗ → <b>Soy brasileño</b> (con ñ). <i>Sofía es español</i> ✗ → <b>Sofía es española</b>: la nacionalidad cambia para mujer. <i>Soy Brasileño</i> ✗ → <b>brasileño</b>: las nacionalidades se escriben con minúscula, como en portugués. Y con <i>usted</i>: <b>¿De dónde es usted?</b>, no <i>¿De dónde eres?</i></div>
<div class="box"><h4>LA REALIDAD LATINOAMERICANA</h4>Para los Estados Unidos se dice <b>estadounidense</b> («americano» es cualquier persona de América). <b>México</b> y <b>Oaxaca</b>: la x suena como j. Sofía es de Madrid y pronuncia la <b>z</b> y la <b>c</b> (ce, ci) con la lengua entre los dientes: solo para reconocer.</div>
<div class="box"><h4>AUDIO</h4>Pista 03.1 Tres diálogos (lento y natural) · Pista 03.2 Países y nacionalidades · Pista 03.3 Frases</div>""")

    # Página 2
    gr = [("1", "Lucía", ["mexicana", "española"], "mexicana"), ("2", "Sofía", ["mexicana", "española"], "española"), ("3", "El señor", ["argentino", "brasileño"], "argentino")]
    wr = "".join(f'<td style="width:33%"><b>Diálogo {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Pedro, ¿de dónde", "eres", "?"), ("No,", "soy", " de Recife."), ("Sí, soy mexicana. Soy de", "la Ciudad de México", "."),
          ("No, soy española. Soy de", "Madrid", "."), ("Perdón, ¿usted", "es", " de Brasil?"), ("¡Y yo soy de", "Oaxaca", "!")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Escucha: ¿De dónde eres?", "10 min")}
<p>Es el tercer día de Pedro. Habla con Lucía, con Sofía (su vecina) y con un señor en el café de Paco.</p>
{audiocard(["03.1 · SLOW", "03.1 · NATURAL"])}
{sub("A", "Escucha. ¿De dónde es? Elige.", "3 min", "03.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Escucha otra vez. Completa.", "5 min", "03.1 · NATURAL")}
<div class="bank">eres · es · la Ciudad de México · Madrid · Oaxaca · soy</div>
{twocol(gl, 3)}
{sub("C", "Lee los diálogos con el profesor.", "2 min")}""",
    30, """<ol><li>A: versión <b>lenta</b>, dos veces. Antes, presentar a Sofía: <i>Es nueva. Es la vecina de Pedro.</i></li>
<li>B: versión <b>natural</b>, parar después de cada diálogo. Preguntar: <i>¿Y Paco? ¿De dónde es?</i> (de Oaxaca, en México).</li>
<li>C: Los diálogos están en la última página. El alumno es Pedro; después, cambiar.</li></ol>""")

    # Página 3
    ser = [("yo", "soy", "Soy de Recife."), ("tú", "eres", "¿De dónde eres?"), ("él / ella", "es", "Ella es española."), ("usted", "es", "¿De dónde es usted?")]
    ts = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in ser)
    gn = [("-o → -a", "mexican<b>o</b>", "mexican<b>a</b>"), ("-o → -a", "brasileñ<b>o</b>", "brasileñ<b>a</b>"),
          ("+ a", "español", "español<b>a</b>"), ("-e = -e", "estadounidens<b>e</b>", "estadounidens<b>e</b>")]
    tg = "".join(f"<tr><td class='small'>{r}</td><td>{m}</td><td>{f}</td></tr>" for r, m, f in gn)
    chk = [("Lucía es …", ["mexicano", "mexicana"], "mexicana"), ("Sofía es …", ["español", "española"], "española"),
           ("Pedro es …", ["brasileño", "brasileña"], "brasileño"), ("¿De dónde … usted?", ["eres", "es"], "es")]
    wt = "".join(f'<td style="width:25%"><span class="small">{s}</span><br>{ch(o, a)}</td>' for s, o, a in chk)
    b.page(f"""{sec(3, "Gramática: ser · ¿De dónde eres?", "10 min")}
{sub("A", "Lee.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">ser</th></tr>{ts}</table></div>
<div><table style="margin:0"><tr><th></th><th>♂ hombre</th><th>♀ mujer</th></tr>{tg}</table></div></div>
<div class="box"><h4>LA REGLA</h4><b>¿De dónde eres?</b> (tú) · <b>¿De dónde es usted?</b> (usted) → <b>Soy de</b> + ciudad o país: <i>Soy de Recife. Soy de Brasil.</i> &nbsp;·&nbsp; Nacionalidad con <b>ser</b> y sin <i>de</i>: <i>Soy brasileño.</i> &nbsp;·&nbsp; Siempre con minúscula: <i>mexicana</i>, no <i>Mexicana</i>.</div>
{sub("B", "Elige.", "4 min")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "¿Y tú? Escribe.", "3 min")}
<div class="two"><div class="wline">Soy de {R("… (ciudad)")}.</div><div class="wline">Soy {R("brasileño / brasileña")}.</div></div>""",
    32, """<ol><li>3A: Explicar primero. <i>ser</i> solo en singular; el plural llega más adelante. <i>usted</i> usa la misma forma que <i>él / ella</i>: <b>es</b>. En la tabla de la derecha, mostrar las tres reglas con los ejemplos del diálogo (Lucía, Sofía, Pedro).</li>
<li>3B: El alumno elige y dice la frase completa en voz alta.</li>
<li>3C: Frases del propio alumno. Si es mujer: <i>brasileña</i>.</li></ol>""")

    # Página 4
    b.page(f"""{sub("D", "Errores comunes", "2 min")}
<div class="box sand"><h4>ATENCIÓN: ERRORES COMUNES</h4>
<table style="margin:0"><tr><th>No digas</th><th>Di</th></tr>
<tr><td>Soy brasilero.</td><td><b>Soy brasileño.</b></td></tr>
<tr><td>Sofía es español.</td><td><b>Sofía es española.</b></td></tr>
<tr><td>Soy Mexicana.</td><td><b>Soy mexicana.</b></td></tr>
<tr><td>¿De dónde eres, señor?</td><td><b>¿De dónde es usted, señor?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio de pronunciación", "5 min")}
{audiocard(["03.2", "03.3"])}
{sub("A", "Escucha y repite.", "2 min", "03.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S032)}</div>
{sub("B", "Escucha y repite.", "3 min", "03.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S033)}</div>
<div class="box"><h4>SONIDOS</h4><b>ñ</b> = «nh»: <i>Espa<b>ñ</b>a, brasile<b>ñ</b>o</i> &nbsp;·&nbsp; la <b>x</b> de <b>México</b> suena como <b>j</b> &nbsp;·&nbsp; la <b>o</b> final es <b>o</b>: <i>mexican<b>o</b>, argentin<b>o</b></i></div>""",
    36, """<ol><li>Errores: <i>brasilero</i> viene del portugués; en español es <b>brasileño</b>. Con <i>señor / señora</i> → <i>usted</i> → <b>es</b>.</li>
<li>4A/4B: Repetir dos veces. La <b>ñ</b> es como «nh». <b>México</b>: la x suena fuerte, como la j de <i>jota</i>. La <b>o</b> final no se convierte en «u»: <i>mexicano</i>, no «mexicanu». Mostrar, sin explicar demasiado.</li></ol>""")

    # Página 5
    gw = ["soy", "eres", "es", "es", "soy", "es"]
    gs = [("Yo", " de Recife."), ("¿De dónde", " tú?"), ("Lucía", " mexicana."), ("¿De dónde", " usted, señor?"), ("Yo", " brasileña."), ("Paco", " de Oaxaca.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("eres / dónde / de / ¿ / ?", "¿De dónde eres?"), ("de / soy / Madrid", "Soy de Madrid."), ("es / ella / colombiana", "Ella es colombiana.")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Chile", "c", "argentino"), ("Argentina", "a", "peruana"), ("Perú", "b", "chilena"), ("Estados Unidos", "d", "estadounidense")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Práctica", "8 min")}
{sub("A", "Completa.", "3 min")}
<div class="bank">eres · es · es · es · soy · soy</div>
{twocol(gl5, 3)}
{sub("B", "Ordena.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Une.", "3 min")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Frase 4: <i>usted</i> → <i>es</i>. Frase 5: <i>brasileña</i> → es una mujer.</li>
<li>C: Después de unir, preguntar la otra forma: <i>chileno → chilena, peruana → peruano</i>.</li></ol>""")

    # Página 6
    ppl = [("Valentina", "Bogotá · Colombia · 25 años", "tú · ¿De dónde eres?", "colombiana"), ("El señor Rojas", "Lima · Perú · 60 años", "usted · ¿De dónde es usted?", "peruano"),
           ("Mateo", "Santiago · Chile · 30 años", "tú · ¿De dónde eres?", "chileno"), ("La señora Brown", "Nueva York · Estados Unidos", "usted · ¿De dónde es usted?", "estadounidense")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + q + " · " + nat)}</div>' for n, d, q, nat in ppl)
    b.page(f"""{sec(6, "Conversación", "12 min")}
{sub("A", "Juega con el profesor. Saluda. Pregunta: ¿De dónde eres?", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> ¡Buenos días! ¿De dónde es usted?<br><b>B:</b> Soy de Lima. Soy peruano. ¿Y usted?<br><b>A:</b> Soy de … Soy …</div>
{sub("B", "Contesta al profesor.", "5 min")}
<ol style="line-height:1.8"><li>¿De dónde eres?</li><li>¿Eres brasileño / brasileña?</li><li>¿De dónde es tu familia?</li><li>¿De dónde es Sofía? ¿Y Lucía?</li></ol>""",
    28, """<ol><li>A: El profesor hace las cuatro personas. El alumno elige <i>¿De dónde eres?</i> (Valentina, Mateo) o <i>¿De dónde es usted?</i> (el señor Rojas, la señora Brown) y después dice la nacionalidad: <i>Valentina es colombiana.</i> Después, cambiar.</li>
<li>B: Respuestas libres. Pregunta 3: aceptar <i>Es de …</i> sin explicar <i>son</i>.</li></ol>""")

    # Página 7
    pc = [("Unidad 01", "Puedo saludar y decir mi nombre."), ("Unidad 02", "Puedo preguntar ¿Qué tal? y deletrear."),
          ("Unidad 03", "Puedo preguntar: ¿De dónde eres? / ¿De dónde es usted?"), ("Unidad 03", "Puedo decir mi nacionalidad.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Argentina", "argentino", "argentina"), ("Colombia", "colombiano", "colombiana"), ("España", "español", "española"), ("Chile", "chileno", "chilena")]
    hr = "".join(f"<tr><td><b>{p}</b></td><td>♂ {A(m, 'min-width:28mm')}</td><td>♀ {A(f, 'min-width:28mm')}</td></tr>" for p, m, f in hw)
    b.page(f"""{sec(7, "Cierre y tarea", "2 min")}
{sub("A", "Autoevaluación", "1 min")}
<table class="ck"><tr><th style="width:19mm"></th><th>En español …</th><th style="width:18mm">¡Fácil!</th><th style="width:18mm">A veces</th><th style="width:18mm">Todavía no</th></tr>{pcr}</table>
{sub("B", "Tarea", "1 min")}
<p><b>1. Escribe las nacionalidades.</b></p>
<table style="margin:0">{hr}</table>
<p style="margin-top:2mm"><b>2. Completa el diálogo.</b></p>
<div class="msg"><b>Sofía:</b> ¡Hola! ¿De dónde eres?<br><b>Tú:</b> {A("Soy de … Soy brasileño / brasileña.", "min-width:70mm")}<br><b>Sofía:</b> Yo soy de Madrid. Soy española.</div>
<p style="margin-top:2mm"><b>3. Escribe dos frases: tu ciudad y tu nacionalidad.</b></p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Próxima clase: empezar con <i>¡Hola! ¿Qué tal? ¿De dónde eres?</i> El alumno lee las frases del ejercicio 3. En la Unidad 04 llegan las profesiones: <i>¿A qué te dedicas?</i></p>""")

    b.extra("Transcripciones", f"""
{sub("03.1", "¿De dónde eres? (lento y natural)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("03.2", "Países y nacionalidades")}
<p>{" · ".join(S032)}</p>
{sub("03.3", "Las frases")}
<p>{" · ".join(S033)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Esencial 03 - De donde eres")
