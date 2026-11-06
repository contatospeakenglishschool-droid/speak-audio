# Speak! Ponte (Italian A2+): Riferimento grammaticale pages, one function per topic, page(b) style
# (modelled on engine/grammar_ref.py of the English line). Each function adds one SB/TB page to a Book.


def _h(t):
    return f'<h4 style="color:#0f4a5a;margin:1.4mm 0 .5mm">{t}</h4>'


def _tbl(head, rows, size="8.8pt", widths=None):
    w = widths or [None] * len(head)
    th = "".join(f'<th{f" style=\'width:{x}\'" if x else ""}>{h}</th>' for h, x in zip(head, w))
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table style="table-layout:fixed;margin-top:0;font-size:{size}"><tr>{th}</tr>{tr}</table>'


def _dont(items):
    return '<div class="box sand" style="margin-top:1.5mm"><h4>NON DIRE</h4>' + " · ".join(f"<s>{a}</s> → {b}" for a, b in items) + "</div>"


def pronomi_indiretti(b):
    """A2 Ponte 01: i pronomi indiretti atoni e tonici, posizione, diretto o indiretto."""
    forms = [("io", "<b>mi</b>", "<b>a me</b>", "Come <b>mi</b> sta? · <b>A me</b> piace il blu."),
             ("tu", "<b>ti</b>", "<b>a te</b>", "Il blu <b>ti</b> sta benissimo!"),
             ("lui", "<b>gli</b>", "<b>a lui</b>", "<b>Gli</b> ho comprato una camicia. (a Bruno)"),
             ("lei", "<b>le</b>", "<b>a lei</b>", "<b>Le</b> scrivo un messaggio. (a Sara)"),
             ("Lei (formale)", "<b>Le</b>", "<b>a Lei</b>", "Signora, <b>Le</b> piace questo vestito?"),
             ("noi", "<b>ci</b>", "<b>a noi</b>", "<b>Ci</b> hanno mandato l'invito."),
             ("voi", "<b>vi</b>", "<b>a voi</b>", "<b>Vi</b> telefono domani."),
             ("loro", "<b>gli</b>", "<b>a loro</b>", "<b>Gli</b> regaliamo un buono. (a Luca e Sara)")]
    dir_ind = [("Chiamo <b>Bruno</b>. → <b>Lo</b> chiamo.", "Telefono <b>a Bruno</b>. → <b>Gli</b> telefono."),
               ("Vedo <b>Giulia</b>. → <b>La</b> vedo.", "Scrivo <b>a Giulia</b>. → <b>Le</b> scrivo."),
               ("Prendo <b>il vestito</b>. → <b>Lo</b> prendo.", "Regalo il vestito <b>a Júlia</b>. → <b>Le</b> regalo il vestito.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: i pronomi indiretti", "")}
<div class="box" style="margin-top:0"><h4>CHE COSA SONO?</h4>Il pronome indiretto risponde alla domanda <b>a chi?</b> e sostituisce <b>a + persona</b>: <i>Regalo una cravatta <b>a Bruno</b>.</i> → <i><b>Gli</b> regalo una cravatta.</i> Così non ripetiamo il nome della persona.</div>
{_h("1. LA FORMA: ATONO E TONICO")}
{_tbl(["persona", "atono", "tonico", "esempio"], forms, "8.6pt", ["24mm", "17mm", "19mm", None])}
<p class="small" style="margin:.6mm 0">Per <i>loro</i> nella lingua di tutti i giorni si usa <b>gli</b>; nello scritto formale anche <i>loro</i> dopo il verbo (<i>Regaliamo <b>loro</b> un buono</i>).</p>
{_h("2. I VERBI CON A + PERSONA")}
<p style="margin:0 0 .5mm;font-size:8.8pt"><b>piacere · stare bene / male · regalare · dare · dire · telefonare · scrivere · chiedere · rispondere · prestare · mandare · portare</b> (qualcosa <b>a</b> qualcuno)</p>
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. DOVE VA L'ATONO?</b><br><b>prima del verbo</b>: <i>Gli telefono.</i> · con <i>non</i>: <i>Non gli telefono.</i><br>passato prossimo: <b>prima dell'ausiliare</b>, il participio non cambia: <i>Le ho regalato un libro.</i><br>con <i>potere, dovere, volere</i>: <i>Gli puoi prestare…?</i> = <i>Puoi prestar<b>gli</b>…?</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. ATONO O TONICO?</b><br>di solito l'<b>atono</b>: <i>Mi piace.</i><br>il <b>tonico</b> per il contrasto, con <i>anche / neanche</i> e da solo:<br><i>A Bruno le cravatte non piacciono, <b>a me</b> sì!</i><br><i>Anche <b>a te</b>? — A chi piace il verde? — <b>A me!</b></i></div></div>
{_h("5. DIRETTO O INDIRETTO?")}
{_tbl(["diretto: lo, la, li, le (chi? che cosa?)", "indiretto: gli, le (a chi?)"], dir_ind, "8.6pt")}
<p class="small" style="margin:.6mm 0">Attenzione: <b>telefonare a</b> vuole l'indiretto; <b>chiamare</b> vuole il diretto: <i>Gli telefono = Lo chiamo.</i></p>
{_dont([("Lo telefono stasera.", "<b>Gli</b> telefono stasera."), ("A Giulia gli piace il blu.", "A Giulia piace il blu. / <b>Le</b> piace il blu."),
        ("Gli piace (a Sara).", "<b>Le</b> piace."), ("Ti sta bene a te.", "<b>Ti</b> sta bene. / <b>A te</b> sta bene."), ("Ho gli comprato…", "<b>Gli</b> ho comprato…")])}""",
    16, """<p>Domanda chiave: <b>a chi?</b> Persona con <i>a</i> → indiretto. <i>A me mi piace</i> si sente nel parlato, ma è da evitare. <i>Glielo, me lo</i> arrivano più avanti.</p>""")


_LINEA_IMPF = """<svg viewBox="0 0 520 64" width="100%" height="15mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="34" x2="500" y2="34" stroke="#77acb5" stroke-width="2"/><polygon points="500,34 490,29 490,39" fill="#77acb5"/>
<text x="20" y="58" font-size="11" fill="#7d858a">PASSATO</text><text x="448" y="58" font-size="11" fill="#7d858a">OGGI</text>
<line x1="456" y1="18" x2="456" y2="50" stroke="#176074" stroke-width="2"/>
<rect x="70" y="27" width="240" height="14" rx="3" fill="#cbbca0" opacity=".75"/>
<text x="74" y="16" font-size="11" fill="#9a7b4f" font-weight="700">imperfetto: com'era? che cosa si faceva di solito?</text>
<circle cx="380" cy="34" r="7" fill="#176074"/><text x="336" y="58" font-size="11" fill="#176074" font-weight="700">passato prossimo: un fatto</text></svg>"""


def imperfetto(b):
    """A2 Ponte 02: l'imperfetto (forme, irregolari, abitudini e descrizioni, primo contrasto con il passato prossimo)."""
    forms = [("io", "parl<b>avo</b>", "prend<b>evo</b>", "dorm<b>ivo</b>", "<b>ero</b>"),
             ("tu", "parl<b>avi</b>", "prend<b>evi</b>", "dorm<b>ivi</b>", "<b>eri</b>"),
             ("lui / lei / Lei", "parl<b>ava</b>", "prend<b>eva</b>", "dorm<b>iva</b>", "<b>era</b>"),
             ("noi", "parl<b>avamo</b>", "prend<b>evamo</b>", "dorm<b>ivamo</b>", "<b>eravamo</b>"),
             ("voi", "parl<b>avate</b>", "prend<b>evate</b>", "dorm<b>ivate</b>", "<b>eravate</b>"),
             ("loro", "parl<b>avano</b>", "prend<b>evano</b>", "dorm<b>ivano</b>", "<b>erano</b>")]
    usi = [("<b>abitudini</b>: che cosa si faceva di solito", "sempre · di solito · ogni domenica · d'estate · spesso · da bambino/a",
            "<i>Ogni domenica <b>andavamo</b> dal nonno.</i>"),
           ("<b>descrizioni</b>: persone, luoghi, età, tempo", "era · aveva · c'era / c'erano",
            "<i><b>Avevo</b> sei anni. <b>Ero</b> bionda. <b>C'erano</b> poche macchine.</i>"),
           ("<b>stati d'animo e desideri</b>", "volevo · mi piaceva · sapevo · ero felice",
            "<i>Da grande <b>volevo</b> fare la cantante.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: l'imperfetto", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>L'imperfetto è il tempo dei <b>ricordi</b>: racconta <b>com'era</b> una persona o un posto e <b>che cosa si faceva di solito</b> nel passato. Non dice quando l'azione è cominciata o finita: è come una foto o un film, non un fatto preciso.
{_LINEA_IMPF}</div>
{_h("1. LA FORMA: -AVO, -EVO, -IVO")}
{_tbl(["", "-are: parlare", "-ere: prendere", "-ire: dormire", "essere"], forms, "8.6pt", ["26mm", None, None, None, None])}
<p class="small" style="margin:.6mm 0"><b>avere</b> è regolare: <i>avevo, avevi, aveva…</i> · Irregolari (dal latino): <b>fare → facevo</b> · <b>bere → bevevo</b> · <b>dire → dicevo</b> · <b>tradurre → traducevo</b>. L'accento: par<u>la</u>vo, parla<u>va</u>mo, ma <u>par</u>lavano.</p>
{_h("2. QUANDO SI USA?")}
{_tbl(["uso", "parole che aiutano", "esempio"], usi, "8.6pt", ["52mm", "56mm", None])}
{_h("3. IMPERFETTO O PASSATO PROSSIMO? (PRIMO CONTATTO)")}
{_tbl(["imperfetto: abitudine, descrizione", "passato prossimo: un fatto, una volta"],
      [("D'estate <b>andavamo</b> a Rimini. (ogni anno)", "Nel 1975 <b>siamo andati</b> a Rimini. (una volta)"),
       ("Il nonno <b>faceva</b> la polenta. (sempre)", "Domenica il nonno <b>ha fatto</b> la polenta. (quella domenica)"),
       ("<b>Era</b> una bambina vivace.", "Mia madre mi <b>ha mandato</b> le foto.")], "8.6pt")}
<p class="small" style="margin:.6mm 0">Nell'unità 03 usiamo i due tempi insieme per raccontare una storia: <i>Mentre <b>giocavo</b>, <b>è arrivato</b> il nonno.</i></p>
{_dont([("Quando ero piccola, ho abitato a Belo Horizonte.", "…<b>abitavo</b> a Belo Horizonte."), ("Io facevevo…", "<b>facevo</b>"),
        ("Era sei anni.", "<b>Avevo</b> sei anni."), ("C'era tanti turisti.", "<b>C'erano</b> tanti turisti."), ("Parlávamo.", "parla<b>va</b>mo")])}""",
    16, """<p>Il portoghese ha lo stesso tempo (<i>pretérito imperfeito</i>), quindi l'uso è facile: la difficoltà è la forma. Far coniugare <i>essere</i> e <i>fare</i> a voce. L'età si dice con <b>avere</b>.</p>""")
