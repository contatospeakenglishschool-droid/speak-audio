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
