# Speak! Essenziale A1 - Unità 31 "Il telefono nuovo" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from offerte import offerte
setup(band="A1 · UNITÀ 31", audio_json=os.path.join(HERE, "audio_it-a1-unita-31.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la SIM", "SIM"), ("B", "il messaggio", "messaggio"), ("C", "il cellulare", "cellulare"), ("D", "il caricabatterie", "caricabatterie"),
          ("E", "la spina", "spina"), ("F", "le cuffie", "cuffie"), ("G", "la videochiamata", "videochiamata"), ("H", "la presa", "presa")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-31"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["31.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S312 = [x.split(": ", 1)[1] for x in _r["31.2 Ripeti"].split("\n")]
S313 = [x.split(": ", 1)[1] for x in _r["31.3 Domanda o frase"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split()[-1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 31", "Il telefono nuovo", "Bruno compra una SIM · <b>mi serve / mi servono · potere e volere + infinito</b>",
                       [("SAI FARE", "comprare una SIM, scegliere un'offerta, chiedere il permesso e fare una telefonata"),
                        ("LINGUA", "Mi serve una SIM · Mi servono molti giga · Posso pagare con la carta? · Vuoi venire?"),
                        ("PRONUNCIA", "l'intonazione: domanda o frase?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: il telefono", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quante ore al giorno usi il cellulare? Per che cosa?</li><li>Preferisci telefonare, scrivere un messaggio o mandare un vocale?</li><li>Quanto costa al mese il tuo telefono?</li></ol>""",
    22, """<ol><li>A: <i>il cellulare</i> = il telefono; si dice anche <i>il telefonino</i>. <i>La presa</i> è nel muro, <i>la spina</i> è sul cavo.</li>
<li>B: domanda 2: <i>il vocale</i> = il messaggio vocale. Accettare risposte brevi.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il telefono e gli accessori</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Le offerte · la telefonata a Júlia · l'adattatore e il vocale</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Mi serve / mi servono · potere e volere + infinito</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Intonazione: domanda o frase?</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Mi serve o mi servono? · rispondere agli inviti</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Nel negozio (gioco di ruolo) · Posso…?</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Con il numero brasiliano Bruno spende troppo. In un negozio di telefonia in via Indipendenza la commessa presenta tre offerte: Giga 150 (9,99 €), Mondo 50 (12,99 €, con i minuti verso l'estero) e Base 20 (5,99 €). Bruno vuole chiamare la mamma, ma con internet le videochiamate sono gratis: sceglie Giga 150 e paga con la carta. Servono il passaporto e il codice fiscale. Poi chiama Júlia con il nuovo numero: stasera cena da Marco, Bruno porta il pane. A casa il caricabatterie brasiliano non entra nella presa: serve un adattatore. Bruno manda un vocale a Paolo per vedere la stanza in via Zamboni sabato mattina.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Eu preciso de uma SIM</i> → <b>Mi serve una SIM</b>: la cosa è il soggetto, quindi al plurale <b>mi servono</b> (<i>mi servono molti giga</i>). Non si dice <i>io servo</i>. Dopo <i>potere</i> e <i>volere</i> c'è l'infinito senza preposizione: <i>Posso pagare</i> (non <i>posso di pagare</i>). <i>Eu quero um café</i> al bar è normale in Brasile; in Italia è più gentile <b>vorrei</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia per comprare una SIM serve sempre un <b>documento d'identità</b>, e di solito anche il <b>codice fiscale</b>. I numeri di cellulare italiani cominciano con il <b>3</b>. Le offerte sono quasi tutte <i>ricaricabili</i>, con un prezzo fisso al mese. Le prese italiane sono di tipo <b>L</b> e <b>F</b>: la spina brasiliana (tipo N) non entra, serve un <b>adattatore</b> (in ferramenta o al supermercato).</div>
<div class="box"><h4>AUDIO</h4>Traccia 31.1 Tre dialoghi (lento e naturale) · Traccia 31.2 Ascolta e ripeti · Traccia 31.3 Domanda o frase?</div>""")

    # Page 2
    vf = [("Bruno chiama Júlia con il numero nuovo.", "V"), ("Júlia conosce già il numero.", "F"),
          ("Stasera Bruno e Júlia vanno a cena da Marco.", "V"), ("Bruno porta il dolce.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: nel negozio", "10 min")}
<p>Bruno compra una SIM italiana, chiama Júlia e poi ha un problema con il caricabatterie.</p>
{audiocard(["31.1 · SLOW", "31.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e completa le offerte: quanti giga? quanto costa?", "5 min", "31.1 · SLOW")}
{offerte(T)}
<p style="margin:1.5mm 0 0">Quale offerta sceglie Bruno? {A("Giga 150", "min-width:30mm")} &nbsp; Il suo nuovo numero: {A("331 562 4087", "min-width:40mm")}</p>
{sub("B", "Dialogo 2. Vero (V) o falso (F)?", "3 min", "31.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. Che cosa serve a Bruno? Perché manda un vocale a Paolo?", "2 min")}
<div class="wline">{R("Gli serve un adattatore. Vuole vedere la stanza in via Zamboni sabato mattina.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>, anche due volte. Il numero si dice cifra per cifra. Bruno sceglie Giga 150 perché le videochiamate con internet sono gratis.</li>
<li>B: versione <b>naturale</b>. 2: Júlia non conosce il numero. 4: Bruno porta il <b>pane</b>, Júlia il dolce.</li></ol>""")

    # Page 3
    sv = [("<b>mi serve</b> + una cosa (singolare)", "<b>Mi serve</b> una SIM. · <b>Mi serve</b> un adattatore."),
          ("<b>mi servono</b> + più cose (plurale)", "<b>Mi servono</b> molti giga. · <b>Mi servono</b> due documenti."),
          ("<b>mi serve</b> + infinito", "<b>Mi serve</b> chiamare mia madre.")]
    svr = "".join(f"<tr><td style='width:60mm'>{a}</td><td>{x}</td></tr>" for a, x in sv)
    conj = [("io", "posso", "voglio"), ("tu", "puoi", "vuoi"), ("lui / lei / Lei", "può", "vuole"),
            ("noi", "possiamo", "vogliamo"), ("voi", "potete", "volete"), ("loro", "possono", "vogliono")]
    cjr = "<tr><th></th>" + "".join(f"<th>{p}</th>" for p, _, _ in conj) + "</tr>" + "".join(
        f"<tr><td><b>{v}</b></td>" + "".join(f"<td><b>{c[i]}</b></td>" for c in conj) + "</tr>" for v, i in [("potere", 1), ("volere", 2)])
    ck = [("Mi ", ["serve", "servono"], "servono", " le cuffie."), ("Ti ", ["serve", "servono"], "serve", " il caricabatterie?"),
          ("Scusi, ", ["puoi", "può"], "può", " ripetere?"), ("Stasera (noi) ", ["vogliamo", "volete"], "vogliamo", " guardare un film.")]
    ckl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in ck)
    pr = [("Bruno", "può", "potere", "pagare con la carta."), ("(io)", "Voglio", "volere", "vedere la stanza."), ("Ragazzi,", "volete", "volere", "venire a cena?"),
          ("Júlia e Marco non", "possono", "potere", "venire domani."), ("(tu)", "Puoi", "potere", "comprare il pane?")]
    prl = "".join(f"<li>{s} {A(v, 'min-width:24mm')} ({inf}) {z}</li>" for s, v, inf, z in pr)
    b.page(f"""{sec(3, "Grammatica: mi serve, potere e volere", "10 min")}
{sub("A", "Leggi la spiegazione.", "4 min")}
<table style="margin:0">{svr}</table>
<table style="margin:1.5mm 0 0">{cjr}</table>
<div class="box sand" style="margin-top:1.5mm"><h4>REGOLA</h4><b>potere</b> = è possibile, ho il permesso: <i>Posso pagare con la carta?</i> · <b>volere</b> = ho il desiderio: <i>Voglio chiamare mia madre.</i> · Dopo <i>potere</i> e <i>volere</i>: <b>infinito</b>, senza preposizione. Con <i>mi serve</i> la cosa è il soggetto: <i>ti serve, Le serve</i> (formale). Per chiedere con gentilezza: <b>vorrei</b>.</div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "Completa con potere o volere.", "4 min")}
<ol>{prl}</ol>""",
    24, """<ol><li>A: far trovare nei dialoghi: <i>Mi serve una SIM, Posso pagare…?, Voglio chiamare…, Vuoi venire…?, Puoi comprare…?</i></li>
<li>C: accettare anche <i>potete venire</i> nella 3. Far notare <i>può / vuole</i> anche con il <i>Lei</i>.</li></ol>""")

    # Page 4
    dl = [f'<li value="{i+1}">{A(x, "min-width:12mm")}</li>' for i, x in enumerate(["?", ".", "?", ".", "?", "."])]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Io servo una SIM.</td><td><b>Mi serve una SIM.</b></td><td>La cosa è il soggetto.</td></tr>
<tr><td>Mi serve molti giga.</td><td><b>Mi servono molti giga.</b></td><td>Plurale: <i>servono</i>.</td></tr>
<tr><td>Posso di pagare con la carta?</td><td><b>Posso pagare con la carta?</b></td><td>Infinito senza <i>di</i>.</td></tr>
<tr><td>Scusi, puoi ripetere?</td><td><b>Scusi, può ripetere?</b></td><td>Con il <i>Lei</i>: <i>può</i>.</td></tr>
<tr><td>Voglio un caffè. (al bar)</td><td><b>Vorrei un caffè.</b></td><td>Più gentile.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["31.2", "31.3"])}
{sub("A", "Ascolta e ripeti. Attenzione alla voce: nella domanda sale alla fine ↗.", "2 min", "31.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S312)}</div>
{sub("B", "Domanda o frase? Ascolta e scrivi ? o . (le parole sono uguali!)", "3 min", "31.3")}
{twocol(dl, 4)}""",
    34, """<ol><li>Errori: <i>io servo</i> esiste, ma vuol dire «servire» (il cameriere serve il caffè).</li>
<li>4B: 1 ? · 2 . · 3 ? · 4 . · 5 ? · 6 . In italiano la domanda sì/no ha le stesse parole della frase: cambia solo la voce.</li></ol>""")

    # Page 5
    things = ["una SIM", "le cuffie", "il caricabatterie", "due documenti", "un adattatore", "molti giga", "il codice fiscale", "le chiavi"]
    sing = [t for t in things if not (t.startswith("le ") or t.startswith("due") or t.startswith("molti"))]
    plur = [t for t in things if t not in sing]
    col = lambda lab, xs: f"<div><b>{lab}</b><div class='wline'>{R(', '.join(xs)) if T else ''}</div><div class='wline'></div></div>"
    inv = [("Vuoi venire al cinema stasera?", "Sì, voglio venire! / Mi dispiace, non posso: devo studiare."),
           ("Puoi comprare il pane?", "Sì, certo, lo compro io."), ("Volete mangiare una pizza sabato?", "Sì, vogliamo venire! A che ora?"),
           ("Posso usare il tuo telefono?", "Certo, eccolo.")]
    invl = "".join(f"<li>{q}<div class='wline'>{R(a) if T else ''}</div></li>" for q, a in inv)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Mi serve o mi servono? Scrivi le cose nella colonna giusta.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(things)}</div>
<div class="two">{col("Mi serve…", sing)}{col("Mi servono…", plur)}</div>
{sub("B", "Rispondi. Di' sì o no (Mi dispiace, non posso…).", "5 min")}
<ol style="line-height:1.6">{invl}</ol>""",
    22, """<ol><li>A: serve: una SIM, il caricabatterie, un adattatore, il codice fiscale; servono: le cuffie, due documenti, molti giga, le chiavi.</li>
<li>B: accettare risposte libere; <i>devo</i> + infinito solo come espressione fissa (<i>devo studiare</i>).</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Nel negozio. L'insegnante è il commesso / la commessa. Guarda le offerte a pagina 2: di' che cosa ti serve, fai domande e scegli un'offerta. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt"><h4>PAROLE UTILI</h4>Buongiorno, mi serve una SIM. · Quanti giga Le servono? · Mi servono… · Posso chiamare all'estero? · Quanto costa al mese? · Posso pagare con la carta? · Le serve un documento. · Prendo…</div>
{sub("B", "Posso…? Chiedi il permesso all'insegnante in queste situazioni.", "4 min")}
<ol><li>Il tuo telefono è scarico.</li><li>Hai sete.</li><li>Non capisci una parola.</li><li>Fa caldo in classe.</li><li>Vuoi fare una foto alla lavagna.</li></ol>
{sub("C", "E tu? Che cosa ti serve nel telefono? Quanti giga ti servono? Che cosa vuoi fare con il telefono questa settimana?", "2 min")}""",
    24, """<ol><li>A: alla fine l'insegnante chiede <i>Il Suo numero, per favore?</i> e lo scrive: ripasso dei numeri.</li>
<li>B: possibili risposte: <i>Posso usare il tuo caricabatterie? Posso bere un po' d'acqua? Può ripetere? Posso aprire la finestra? Posso fare una foto?</i></li></ol>""")

    # Page 7
    pc = [("Unità 30", "So dire l'alfabeto e fare domande con chi, che cosa, quale, quanto."), ("Unità 31", "So dire che cosa mi serve (mi serve / mi servono)."),
          ("Unità 31", "So chiedere il permesso con posso…? / può…?"), ("Unità 31", "So dire che cosa voglio fare (voglio + infinito)."),
          ("Unità 31", "So scegliere un'offerta e fare una telefonata.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Io servo un caricabatterie.", "Mi serve un caricabatterie."), ("Mi serve due biglietti.", "Mi servono due biglietti."),
          ("Posso di entrare?", "Posso entrare?"), ("Noi vogliono mangiare.", "Noi vogliamo mangiare."),
          ("Signora, puoi aspettare?", "Signora, può aspettare?"), ("Vuoi venire con noi?", "✓ corretta")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> Una frase è corretta.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il mio vocale.</b> Scrivi un messaggio a un amico italiano, come Bruno a Paolo: chi sei, che cosa vuoi fare, quando puoi venire, che cosa ti serve.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge (o registra) il suo vocale. Unità 32: <i>In autobus</i> (l'abbonamento, le linee, prendere / scendere).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("31.1", "Il telefono nuovo (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("31.2", "Ascolta e ripeti")}
<p>{" · ".join(S312)}</p>
{sub("31.3", "Domanda o frase?")}
<p>{" · ".join(S313)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 31 - Il telefono nuovo")
