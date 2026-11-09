# Speak! Ponte A2 - Unità 17 "Qui si fa così" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 17", audio_json=os.path.join(HERE, "audio_it-a2-unita-17.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "vietato fumare", "vietato"), ("B", "il palazzo", "palazzo"), ("C", "il portone", "portone"), ("D", "la raccolta differenziata", "raccolta"),
          ("E", "il cappuccino", "cappuccino"), ("F", "il banco del bar", "banco"), ("G", "lo scontrino", "scontrino"), ("H", "il guinzaglio", "guinzaglio")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-17"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["17.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S172 = [x.split(": ", 1)[1] for x in _r["17.2 Ripeti"].split("\n")]
S173 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["17.3 Semplice o doppia"].split("\n")]

AVVISO = [("Nelle ore di riposo (13–15 e 22–9) e la domenica <b>è vietato</b> fare rumore: <b>non si usano</b> l'aspirapolvere e la lavatrice."),
          ("La raccolta differenziata <b>è obbligatoria</b>. La plastica <b>si butta</b> il martedì, la carta il venerdì; il vetro <b>si porta</b> alla campana."),
          ("<b>È vietato</b> lasciare biciclette e passeggini nell'ingresso: <b>si mettono</b> in cortile."),
          ("Il bucato <b>non si stende</b> sui balconi che danno sulla strada."),
          ("Il portone <b>si chiude</b> sempre, anche di giorno."),
          ("Gli animali sono benvenuti, ma sulle scale <b>è obbligatorio</b> il guinzaglio.")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split(" ", 1)[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 17", "Qui si fa così", "Regole e buone maniere · <b>si impersonale · è vietato / è obbligatorio + infinito</b>",
                       [("SAI FARE", "capire un avviso con delle regole, spiegare come si fa una cosa nel tuo paese, comportarti al bar come un italiano"),
                        ("LINGUA", "Qui si paga prima. · Il cappuccino si beve la mattina. · Le bici si mettono in cortile. · È vietato fumare."),
                        ("PRONUNCIA", "consonanti semplici e doppie: caro / carro, casa / cassa")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: le regole", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Abiti in un palazzo o in una casa? Ci sono regole? Quali?</li><li>Nel tuo paese fai la raccolta differenziata?</li><li>Quando bevi il cappuccino (o il caffè con il latte)? A che ora?</li></ol>""",
    24, """<ol><li>A: <i>il palazzo</i> = edificio con appartamenti (non solo "palácio"); <i>il portone</i> = la porta grande del palazzo; <i>lo scontrino</i> = la ricevuta del negozio o del bar.</li>
<li>B: frasi come <i>Non si può fumare</i> vanno benissimo: il <i>si</i> arriva a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: regole, palazzo, bar</td><td>1</td></tr>
<tr><td>2 Lettura e ascolto</td><td>10 min</td><td>L'avviso del condominio · la signora Rossi spiega · al bar di Giulia</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>si impersonale · è vietato / è obbligatorio + infinito</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>si + singolare / plurale · si può · le regole</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Consonanti semplici e doppie</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Riscrivi con si · i cartelli · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>In Italia e nel mio paese · il regolamento</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio giugno. Nell'ingresso del palazzo c'è un avviso dell'amministratore con le regole: ore di riposo, raccolta differenziata, niente bici nell'ingresso, niente bucato sui balconi che danno sulla strada, portone sempre chiuso, guinzaglio sulle scale. Júlia pensa: "Parla di me?" (unità 15: il bucato, l'aspirapolvere). La signora Rossi la rassicura e le spiega tutto, con un po' di ironia. Al bar di Giulia, alle tre del pomeriggio, una turista inglese ordina un cappuccino: Giulia le spiega le abitudini del bar italiano, e alla fine la turista prende un caffè al banco.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Nel portoghese parlato si dice <i>aqui paga antes, no Brasil come tarde</i>, senza <i>se</i>: lo studente dice <i>qui paga prima</i> (→ <b>qui si paga prima</b>). Poi il plurale: <i>si mette le bici</i> (→ <b>si mettono le bici</b>). Dopo <i>è vietato / è obbligatorio</i> lo studente aggiunge <i>di</i>: <i>è vietato di fumare</i> (→ <b>è vietato fumare</b>). Posizione: <b>non si</b> fuma (non <i>si non fuma</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Le regole al bar: il <b>cappuccino</b> si beve la mattina, quasi mai dopo i pasti; nelle grandi città spesso <b>si paga prima alla cassa</b> e si dà lo scontrino al barista; <b>al banco</b> si spende meno che al tavolo. Nei condomini c'è un <b>amministratore</b> e un <b>regolamento</b>: ogni città ha i suoi giorni per la raccolta differenziata.</div>
<div class="box"><h4>AUDIO</h4>Traccia 17.1 I due dialoghi (lento e naturale) · Traccia 17.2 Ascolta e ripeti · Traccia 17.3 Semplice o doppia?</div>""")

    # Page 2
    av = "".join(f"<li>{x}</li>" for x in AVVISO)
    vf = [("Alle 14 si può usare la lavatrice.", "F"), ("La carta si butta il venerdì.", "V"), ("Le bici si lasciano nell'ingresso.", "F"),
          ("Sulle scale i cani devono avere il guinzaglio.", "V")]
    vfl = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    p1 = [("Il bucato si stende", "sul balcone dietro o in casa"), ("Le bici si mettono", "in cortile"), ("Il vetro si porta", "alla campana in fondo alla via")]
    p1l = "".join(f"<li>{a} {A(x, 'min-width:58mm')}</li>" for a, x in p1)
    vf2 = [("Il cappuccino si beve dopo pranzo.", "F"), ("In molti bar si paga prima alla cassa.", "V"), ("Da Giulia si deve pagare prima.", "F"),
           ("Alla fine la turista prende un caffè al banco.", "V")]
    vf2l = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf2))
    b.page(f"""{sec(2, "Lettura e ascolto: le regole", "10 min")}
{audiocard(["17.1 · SLOW", "17.1 · NATURAL"])}
{sub("A", "Leggi l'avviso nell'ingresso del palazzo di Júlia. Vero (V) o falso (F)?", "4 min")}
<div class="msg" style="max-width:none;padding:1.5mm 3.5mm;font-size:8.8pt;line-height:1.4;border:1.2px solid {TEAL}"><b style="color:{TEAL}">AVVISO AI CONDÒMINI</b> · Gentili condòmini, ricordiamo alcune regole del palazzo:
<ol style="margin:.5mm 0 .5mm 4mm">{av}</ol>Grazie per la collaborazione. <i>L'amministratore</i></div>
<table style="margin:1mm 0 0">{vfl}</table>
{sub("B", "Prima parte. La signora Rossi spiega. Completa.", "3 min", "17.1 · SLOW")}
<ol style="line-height:1.55">{p1l}</ol>
{sub("C", "Seconda parte. Al bar di Giulia. Vero (V) o falso (F)?", "3 min", "17.1 · NATURAL")}
<table style="margin:0">{vf2l}</table>""",
    22, """<ol><li>A: far sottolineare tutte le forme con <i>si</i> e con <i>è vietato / obbligatorio</i>. <i>Condòmini</i> (abitanti del condominio) ≠ <i>condomìni</i> (palazzi).</li>
<li>B–C: chiedere: <i>Perché Júlia pensa che l'avviso parli di lei?</i> (il bucato, l'aspirapolvere: unità 15).</li></ol>""")

    # Page 3
    rules = [("<i>Qui <b>si paga</b> prima.</i> Chi paga?", ["tutti, le persone in generale", "Giulia"], "tutti, le persone in generale"),
             ("Con il <i>si</i> impersonale il verbo è alla", ["3ª persona", "1ª persona"], "3ª persona"),
             ("<i>Le bici <b>si mettono</b> in cortile.</i> Il verbo è plurale perché", ["le bici è plurale", "si è plurale"], "le bici è plurale"),
             ("La negazione è", ["non si stende", "si non stende"], "non si stende"),
             ("<i>È vietato</i> = ", ["non si può", "si deve"], "non si può"),
             ("Dopo <i>è vietato / è obbligatorio</i> c'è", ["l'infinito", "di + infinito"], "l'infinito")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("In Italia", ["si mangia", "si mangiano"], "si mangia", "tardi."), ("In questo negozio", ["si vende", "si vendono"], "si vendono", "biglietti dell'autobus."),
          ("È vietato", ["di parcheggiare", "parcheggiare"], "parcheggiare", "davanti al portone."), ("Al bar", ["non si", "si non"], "non si", "fuma.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il si impersonale, è vietato", "10 min")}
{sub("A", "Studia le frasi dell'avviso e dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. In Brasile <b>si stende</b> dappertutto. · Qui <b>si paga</b> prima o dopo? · Qui da me <b>si può</b> pagare anche dopo. · Al banco <b>si spende</b> meno.<br>
2. Il cappuccino <b>si beve</b> la mattina. · Il portone <b>si chiude</b> sempre. · La plastica <b>si butta</b> il martedì.<br>
3. Le bici <b>si mettono</b> in cortile. · <b>Non si usano</b> l'aspirapolvere e la lavatrice.<br>
4. <b>È vietato</b> lasciare le biciclette nell'ingresso. · Sulle scale <b>è obbligatorio</b> il guinzaglio.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>si + verbo alla 3ª persona</b> = le persone in generale: <i>qui si paga prima</i>. Con un nome plurale, verbo plurale: <i>le bici si mettono</i>. Negazione: <b>non si</b>. Regole: <b>è vietato / è obbligatorio + infinito</b> (senza <i>di</i>). Tutto: pagina 4.</div>""",
    22, """<ol><li>A: confrontare con il portoghese: <i>aqui se paga antes</i> = <i>qui si paga prima</i>; <i>a gente paga</i> → stesso significato.</li>
<li>C: frase 2: il soggetto vero è <i>biglietti</i> (plurale) → <i>si vendono</i>.</li></ol>""")

    grammar_ref_it.si_impersonale(b)

    # Page 5
    pairs = [("sete", "sette"), ("caro", "carro"), ("capello", "cappello"), ("pena", "penna"), ("casa", "cassa"), ("fato", "fatto")]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>In Italia mangia tardi.</td><td><b>In Italia si mangia tardi.</b></td><td>Le persone in generale: <i>si</i>.</td></tr>
<tr><td>Si mette le bici in cortile.</td><td><b>Si mettono le bici in cortile.</b></td><td>Nome plurale → verbo plurale.</td></tr>
<tr><td>È vietato di fumare.</td><td><b>È vietato fumare.</b></td><td>Nessuna preposizione.</td></tr>
<tr><td>Qui si non fuma.</td><td><b>Qui non si fuma.</b></td><td><i>non</i> prima di <i>si</i>.</td></tr>
<tr><td>Si paga in la cassa.</td><td><b>Si paga alla cassa.</b></td><td><i>a + la = alla</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["17.2", "17.3"])}
{sub("A", "Ascolta e ripeti. Attenzione alle doppie: obbligatorio, cappuccino, scontrino, portone.", "2 min", "17.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S172)}</div>
{sub("B", "Semplice o doppia? Ascolta e scegli la parola.", "2 min", "17.3")}
{twocol([f'<li value="{i+1}">{ch([a, d], S173[i])}</li>' for i, (a, d) in enumerate(pairs)], 4)}""",
    28, """<ol><li>Errori: <i>si</i> + verbo è anche negli annunci: <i>si affitta, si vende</i> (con nome plurale: <i>si affittano camere</i>).</li>
<li>4B: la doppia è più lunga e più forte: <i>cassa</i> (al bar) ≠ <i>casa</i>. Far tenere la consonante "un attimo di più".</li></ol>""")

    # Page 6
    qa = [("In Italia la gente beve il caffè al banco.", "In Italia si beve il caffè al banco."), ("In Brasile la gente mangia il riso tutti i giorni.", "In Brasile si mangia il riso tutti i giorni."),
          ("Qui la gente compra i biglietti dal tabaccaio.", "Qui si comprano i biglietti dal tabaccaio."), ("In questo bar la gente non paga prima.", "In questo bar non si paga prima."),
          ("A Bologna la gente usa molto la bici.", "A Bologna si usa molto la bici.")]
    qal = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in qa)
    sg = [("in moto: il casco", "È obbligatorio portare il casco."), ("in ospedale: fumare", "È vietato fumare."),
          ("al museo: fare foto con il flash", "È vietato fare foto con il flash."), ("in macchina: la cintura", "È obbligatorio mettere la cintura.")]
    sgl = "".join(f"<li>{s} {A(a, 'min-width:64mm')}</li>" for s, a in sg)
    wb = [("vietare", "il divieto"), ("obbligare", "l'obbligo"), ("permettere", "il permesso"), ("multare", "la multa")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Riscrivi le frasi con il si impersonale.", "4 min")}
<ol style="line-height:1.45">{qal}</ol>
{sub("B", "I cartelli. Scrivi la regola con è vietato o è obbligatorio.", "3 min")}
<ol style="line-height:1.7">{sgl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 3: <i>i biglietti</i> plurale → <i>si comprano</i>. <i>Il tabaccaio</i>: in Italia i biglietti dell'autobus si comprano anche lì.</li>
<li>C: <i>il permesso</i> si usa anche per chiedere di entrare: <i>Permesso?</i> · <i>il permesso di soggiorno</i> (A2 08). <i>La multa</i>: se non si rispetta un divieto.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "In Italia e nel mio paese. Come si fa in Brasile? Confronta con l'Italia. Usa il si impersonale.", "6 min")}
<table style="margin:1mm 0 0;font-size:9pt"><tr><th>Situazione</th><th>In Italia…</th><th>Nel mio paese…</th></tr>
<tr><td>al bar</td><td>si beve il caffè al banco, in piedi</td><td></td></tr>
<tr><td>a tavola</td><td>si mangia la pasta prima della carne</td><td></td></tr>
<tr><td>a casa di amici</td><td>si porta un dolce o una bottiglia di vino</td><td></td></tr>
<tr><td>quando si incontra qualcuno</td><td>si danno due baci (tra amici)</td><td></td></tr>
<tr><td>a cena</td><td>si mangia verso le otto, le otto e mezza</td><td></td></tr></table>
{sub("B", "Il regolamento. Sei l'amministratore di un palazzo (o il direttore di una scuola, di una palestra…). Scrivi quattro regole e spiegale all'insegnante, che fa domande.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>È vietato… · È obbligatorio… · Non si può… · Si deve… · Si può… ? · Perché è vietato…? · E se un condòmino non…? · Mi sembra giusto / esagerato.</div>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: nessun giudizio: <i>si fa così</i>, non "meglio" o "peggio". Accettare anche paragoni (unità 13): <i>In Brasile si cena più tardi.</i></li>
<li>B: l'insegnante fa il condòmino difficile: <i>Ma io ho un cane grande!</i> Pretendere <i>è vietato / è obbligatorio</i> + infinito senza <i>di</i>.</li></ol>""")

    # Page 8
    pc = [("A2 · 16", "So usare che e preposizione + cui."), ("A2 · 17", "So capire un avviso con delle regole."),
          ("A2 · 17", "So usare il si impersonale (qui si paga prima)."), ("A2 · 17", "So dire le regole con è vietato / è obbligatorio."),
          ("A2 · 17", "So spiegare come si fa una cosa nel mio paese.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("In Brasile mangia molto riso.", "In Brasile si mangia"), ("Il cappuccino si beve la mattina.", "✓"),
          ("Si mette le bici in cortile.", "Si mettono le bici"), ("È vietato di fumare.", "È vietato fumare."),
          ("Qui si non paga prima.", "Qui non si paga"), ("È obbligatorio chiudere il portone.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Consigli per un italiano in Brasile (50–75 parole).</b> Un amico italiano viene nel tuo paese. Scrivigli come si fa: al bar, a tavola, con gli amici. Che cosa è vietato? Che cosa è obbligatorio? Usa il <i>si</i> impersonale.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge i consigli; l'insegnante reagisce (<i>Davvero? In Italia invece…</i>). Unità 18: <i>Ti scrivo</i> (e-mail formali e informali, i connettivi).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("17.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("17.2", "Ascolta e ripeti")}
<p>{" · ".join(S172)}</p>
{sub("17.3", "Semplice o doppia?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S173))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 17 - Qui si fa cosi")
