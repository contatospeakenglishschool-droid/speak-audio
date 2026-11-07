# Speak! Essenziale A1 - Unità 34 "Al mercatino" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from spesa import spesa
setup(band="A1 · UNITÀ 34", audio_json=os.path.join(HERE, "audio_it-a1-unita-34.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il mercatino", "mercatino"), ("B", "la lampada", "lampada"), ("C", "il tappeto", "tappeto"), ("D", "le sedie", "sedie"),
          ("E", "i libri usati", "libri"), ("F", "lo specchio", "specchio"), ("G", "i colori", "colori"), ("H", "il prezzo", "prezzo")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-34"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["34.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S342 = [x.split(": ", 1)[1] for x in _r["34.2 Ripeti"].split("\n")]
S343 = [x.split(": ", 1)[1] for x in _r["34.3 Una o due"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split()[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 34", "Al mercatino", "La stanza di Bruno · <b>questo e quello · i colori · Mi fa uno sconto?</b>",
                       [("SAI FARE", "comprare cose usate, scegliere tra due oggetti, chiedere il prezzo e uno sconto"),
                        ("LINGUA", "questa lampada / quella lì · Quale preferisci? · È verde, sono bianche · Mi fa uno sconto?"),
                        ("PRONUNCIA", "consonanti doppie: caro / carro, sete / sette")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: cose usate", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Compri cose usate? Che cosa? Dove?</li><li>Che cosa c'è nella tua stanza? Di che colore è?</li><li>Qual è il tuo colore preferito?</li></ol>""",
    22, """<ol><li>A: <i>usato</i> = non nuovo, di seconda mano. <i>Il mercatino</i> = un piccolo mercato (dell'usato, dell'antiquariato).</li>
<li>B: domanda 2: ripasso di <i>c'è / ci sono</i> e dei mobili (unità sulla casa).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il mercatino</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La lampada · il tappeto e la sedia · la videochiamata</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>questo / quello · i colori</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Consonanti doppie</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Questo o quello? · di che colore è?</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Al mercatino (gioco di ruolo) · la mia stanza</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Bruno ha preso la stanza di Paolo in via Zamboni (unità 29 e 32), ma è vuota. Sabato va al mercatino dell'usato con Chiara: non vuole la lampada gialla («troppo piccola»), preferisce quella verde e ottiene uno sconto: 15 euro invece di 20. Al banco dei tappeti sceglie quello blu e una sedia bianca: 40 euro, ma con lo sconto 35. Chiara compra tre libri a 2 euro l'uno. La sera, in videochiamata, Bruno fa vedere la stanza a Júlia: 50 euro in tutto. I libri? Chiara «li ha dimenticati» lì… Bruno vuole una parete arancione, ma Paolo dice di no.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Este / esse</i> → <b>questo</b>; <i>aquele</i> → <b>quello</b>. Davanti al nome <i>quello</i> cambia come l'articolo: <b>quel</b> tappeto, <b>quello</b> specchio, <b>quella</b> sedia, <b>quell'</b>armadio, <b>quei</b> libri, <b>quegli</b> specchi, <b>quelle</b> sedie. <i>Laranja</i> → <b>arancione</b>; <i>roxo</i> → <b>viola</b>; <i>marrom</i> → <b>marrone</b>. <i>Me dá um desconto?</i> → <b>Mi fa uno sconto?</b> Attenzione alle doppie: <i>caro</i> (costa molto) ≠ <i>carro</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia i <b>mercatini dell'usato</b> e dell'antiquariato sono molto popolari: si trovano mobili, vestiti, libri, dischi. A Bologna c'è il grande mercato della <b>Piazzola</b> (piazza VIII Agosto), il venerdì e il sabato. Al mercato si può chiedere uno sconto con gentilezza: <i>Mi fa un prezzo? Facciamo…?</i> Nei negozi normali, invece, di solito il prezzo è fisso.</div>
<div class="box"><h4>AUDIO</h4>Traccia 34.1 Tre dialoghi (lento e naturale) · Traccia 34.2 Ascolta e ripeti · Traccia 34.3 Una o due consonanti?</div>""")

    # Page 2
    vf = [("Chiara preferisce la lampada gialla, Bruno quella verde.", "V"), ("Bruno sceglie il tappeto rosso.", "F"),
          ("Il venditore fa uno sconto due volte.", "V"), ("I libri sono di Bruno.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Mi fa uno sconto?", "10 min")}
<p>Bruno ha una stanza nuova, ma è vuota. Sabato va al mercatino con Chiara.</p>
{audiocard(["34.1 · SLOW", "34.1 · NATURAL"])}
{sub("A", "Dialoghi 1 e 2. Ascolta e completa: colori e prezzi.", "5 min", "34.1 · SLOW")}
{spesa(T)}
{sub("B", "Vero (V) o falso (F)?", "3 min", "34.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. Di che colore sono le pareti della stanza? E di che colore le vuole Bruno?", "2 min")}
<div class="wline">{R("Sono bianche. Bruno vuole una parete arancione (ma Paolo dice di no).")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>, anche due volte. 15 + 35 = 50 euro.</li>
<li>B: versione <b>naturale</b>. 3: lampada (20 → 15) e tappeto + sedia (40 → 35). 4: sono di Chiara. <i>Li ha dimenticati</i>: solo da capire. Júlia ripete la frase… perché?</li></ol>""")

    # Page 3
    qq = [("", "maschile", "femminile"), ("singolare", "<b>questo</b> tappeto", "<b>questa</b> lampada"), ("plurale", "<b>questi</b> libri", "<b>queste</b> sedie")]
    qqr = "".join(f"<tr><td>{a}</td><td>{x}</td><td>{y}</td></tr>" if i else f"<tr><th>{a}</th><th>{x}</th><th>{y}</th></tr>" for i, (a, x, y) in enumerate(qq))
    ql = [("come <i>il</i> → <b>quel</b> tappeto", "come <i>i</i> → <b>quei</b> libri"), ("come <i>lo</i> → <b>quello</b> specchio", "come <i>gli</i> → <b>quegli</b> specchi"),
          ("come <i>la</i> → <b>quella</b> sedia", "come <i>le</i> → <b>quelle</b> sedie"), ("come <i>l'</i> → <b>quell'</b>armadio", "")]
    qlr = "".join(f"<tr><td>{a}</td><td>{x}</td></tr>" for a, x in ql)
    col = ("<b>-o</b> (4 forme): rosso, rossa, rossi, rosse · giallo, nero, bianco → bianchi, bianche · "
           "<b>-e</b> (2 forme): verde → verdi, arancione → arancioni, marrone → marroni · "
           "<b>non cambiano</b>: blu, rosa, viola, beige")
    ck = [("Mi piace ", ["questo", "questa"], "questa", " sedia."), ("Quanto costano ", ["quei", "quelli"], "quei", " libri?"),
          ("Preferisco ", ["quel", "quello"], "quello", " specchio."), ("Le pareti sono ", ["bianchi", "bianche"], "bianche", ".")]
    ckl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in ck)
    b.page(f"""{sec(3, "Grammatica: questo, quello e i colori", "10 min")}
{sub("A", "Leggi la spiegazione.", "5 min")}
<div class="two"><div><b>questo</b> = vicino a me<table style="margin:.5mm 0 0">{qqr}</table></div>
<div><b>quello</b> = lontano da me<table style="margin:.5mm 0 0">{qlr}</table></div></div>
<div class="box sand" style="margin-top:1.5mm"><h4>REGOLA</h4>Senza nome (da solo) diciamo <b>questo, questa, questi, queste</b> e <b>quello, quella, quelli, quelle</b>: <i>Quale preferisci? — Quello blu. · Quelli sono di Chiara.</i> I colori sono aggettivi e vanno <b>dopo</b> il nome: <i>la lampada verde</i>. {col}.</div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "Di che colore è? Scrivi il colore giusto.", "3 min")}
<ol><li>il mare: {A("blu", "min-width:22mm")}</li><li>le banane: {A("gialle", "min-width:22mm")}</li><li>l'erba: {A("verde", "min-width:22mm")}</li><li>i pomodori: {A("rossi", "min-width:22mm")}</li><li>la neve: {A("bianca", "min-width:22mm")}</li></ol>""",
    24, """<ol><li>A: far trovare nei dialoghi: <i>questa lampada, quella lì, quello blu, questi libri, quei libri, quelli sono di Chiara</i>.</li>
<li>C: accettare <i>azzurro</i> per il mare. Attenzione all'accordo: <i>le banane gialle, i pomodori rossi</i>.</li></ol>""")

    # Page 4
    dl = [f'<li value="{i+1}">{A(w, "min-width:24mm")}</li>' for i, w in enumerate(["palla", "caro", "sette", "nono", "carro", "sete"])]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Quello tappeto è bello.</td><td><b>Quel tappeto è bello.</b></td><td>Come <i>il</i>: <i>quel</i>.</td></tr>
<tr><td>Quelli libri costano poco.</td><td><b>Quei libri costano poco.</b></td><td>Come <i>i</i>: <i>quei</i>.</td></tr>
<tr><td>la verde lampada</td><td><b>la lampada verde</b></td><td>Il colore va dopo.</td></tr>
<tr><td>Le sedie sono bianchi.</td><td><b>Le sedie sono bianche.</b></td><td>Femminile plurale.</td></tr>
<tr><td>Una parete laranja.</td><td><b>Una parete arancione.</b></td><td>In italiano: <i>arancione</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["34.2", "34.3"])}
{sub("A", "Ascolta e ripeti. La consonante doppia è più lunga e più forte.", "2 min", "34.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S342)}</div>
{sub("B", "Una o due consonanti? Ascolta e scrivi la parola.", "3 min", "34.3")}
{twocol(dl, 4)}""",
    34, """<ol><li>Errori: con <i>quello</i> lo studente pensa all'articolo: <i>il → quel, i → quei, gli → quegli</i>.</li>
<li>4: le doppie cambiano il significato: <i>caro</i> (costoso) / <i>carro</i>; <i>sete</i> (voglia di bere) / <i>sette</i> (7); <i>nono</i> (9°) / <i>nonno</i>.</li></ol>""")

    # Page 5
    qs = [("(vicino) ___ lampada è troppo piccola.", "Questa"), ("(lontano) Quanto costa ___ specchio?", "quello"),
          ("(lontano) Mi piacciono ___ sedie rosse.", "quelle"), ("(vicino) ___ libri sono di Chiara.", "Questi"),
          ("(lontano) Preferisco ___ tappeto blu.", "quel"), ("(lontano) Quale vuoi? — ___ verde.", "Quella")]
    qsl = "".join(f"<li>{s.replace('___', A(a, 'min-width:20mm'))}</li>" for s, a in qs)
    cs = [("il tappeto ___ (blu)", "blu"), ("le pareti ___ (bianco)", "bianche"), ("i libri ___ (rosso)", "rossi"),
          ("la lampada ___ (verde)", "verde"), ("le sedie ___ (arancione)", "arancioni"), ("le borse ___ (rosa)", "rosa")]
    csl = "".join(f"<li>{s.replace('___', A(a, 'min-width:22mm'))}</li>" for s, a in cs)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Questo o quello? Completa.", "4 min")}
<ol style="line-height:1.75">{qsl}</ol>
{sub("B", "Scrivi il colore nella forma giusta.", "4 min")}
{twocol([f'<li value="{i+1}">' + x[4:] for i, x in enumerate(csl.split('</li>')[:-1])], 4)}""",
    22, """<ol><li>A: la prima e la quarta cominciano la frase: maiuscola.</li>
<li>B: <i>blu</i> e <i>rosa</i> non cambiano; <i>arancione</i> ha solo due forme (<i>arancione / arancioni</i>).</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Al mercatino. L'insegnante è il venditore. Vuoi comprare tre cose per la tua casa: scegli (questo o quello?), chiedi il prezzo e uno sconto. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt"><h4>PAROLE UTILI</h4>Quanto costa questo/a…? · Quanto costano quei/quelle…? · Quale preferisci? · Quello/a rosso/a. · È troppo caro! · Mi fa uno sconto? · Mi fa un prezzo? · Facciamo… euro? · Va bene, lo/la prendo.</div>
{sub("B", "Indovina l'oggetto. Pensa a una cosa nella classe. L'insegnante fa domande: Di che colore è? È grande o piccolo? È vicino o lontano? Poi cambiate.", "3 min")}
<div class="wline"></div>
{sub("C", "La mia stanza. Descrivi la tua stanza: che cosa c'è e di che colore sono le cose.", "3 min")}""",
    24, """<ol><li>A: portare oggetti veri o foto con il prezzo: lo studente indica <i>questo</i> (vicino) e <i>quello</i> (lontano).</li>
<li>B: l'insegnante risponde solo <i>sì</i> o <i>no</i> quando lo studente indovina: <i>È quella sedia? — Sì!</i></li></ol>""")

    # Page 7
    pc = [("Unità 33", "So dire che cosa mi è piaciuto e che cosa no."), ("Unità 34", "So usare questo e quello."),
          ("Unità 34", "So dire i colori nella forma giusta."), ("Unità 34", "So chiedere un prezzo e uno sconto."),
          ("Unità 34", "So pronunciare le consonanti doppie.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Quello libro è vecchio.", "Quel libro è vecchio."), ("Mi piace la rossa borsa.", "Mi piace la borsa rossa."),
          ("Queste scarpe sono neri.", "Queste scarpe sono nere."), ("Quelli ragazzi sono simpatici.", "Quei ragazzi sono simpatici."),
          ("Ho una maglietta laranja.", "Ho una maglietta arancione."), ("Quanto costa quello specchio?", "✓ corretta")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> Una frase è corretta.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il mio mercatino.</b> Scegli 5 cose che vuoi vendere (vestiti, libri, mobili…). Scrivi per ogni cosa il colore e il prezzo: <i>Questa sedia bianca: 10 euro.</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: mercatino in classe con gli oggetti dei compiti. Unità 35: <i>Arriva l'invito</i> (il matrimonio di Luca e Sara; le date; rispondere a un invito).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("34.1", "Al mercatino (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("34.2", "Ascolta e ripeti")}
<p>{" · ".join(S342)}</p>
{sub("34.3", "Una o due consonanti?")}
<p>{" · ".join(S343)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 34 - Al mercatino")
