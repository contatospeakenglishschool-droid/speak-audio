# Speak! Ponte A2 - Unità 31 "Un po' di storia" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 31", audio_json=os.path.join(HERE, "audio_it-a2-unita-31.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "le torri", "torri"), ("B", "il portico", "portico"), ("C", "il santuario", "santuario"), ("D", "la piazza", "piazza"),
          ("E", "l'aula", "aula"), ("F", "i libri antichi", "libri antichi"), ("G", "i gradini", "gradini"), ("H", "la mappa antica", "mappa antica")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-31"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["31.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S312 = [x.split(": ", 1)[1] for x in _r["31.2 Ripeti"].split("\n")]
S313 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["31.3 Che secolo"].split("\n")]


def _key(w):
    if w.startswith("l'"):
        return w[2:].lower()
    a, _, rest = w.partition(" ")
    return (rest if a in ("la", "il", "i", "gli", "lo", "le") else w).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 31", "Un po' di storia", "La storia di una città · <b>terzo · undicesimo · il XII secolo · il Trecento · nel 1088</b>",
                       [("SAI FARE", "raccontare la storia di un posto con date e secoli, fare da guida in una città, mettere le cose in ordine"),
                        ("LINGUA", "il terzo capitolo · la seconda cosa · il dodicesimo secolo, cioè il Millecento · nel 1088 · del Cinquecento"),
                        ("PRONUNCIA", "l'accento di -esimo: undicèsimo, ventèsimo")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: la città antica", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Ti piace la storia? Che cosa studiavi volentieri a scuola?</li><li>Qual è il posto più antico della tua città?</li><li>Quando visiti una città, preferisci i musei o le strade?</li></ol>""",
    28, """<ol><li>A: le foto A, B, C e D sono di Bologna: le torri (A), un portico (B), il santuario di San Luca sulla collina, dove arriva il portico più lungo (C), e piazza Maggiore con Palazzo d'Accursio (D).</li>
<li>B: domanda 2: accettare <i>è antico, è vecchio</i>; le date arrivano a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: Bologna e la storia</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La lezione del professore · Bruno fa da guida</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Gli ordinali · i secoli · gli anni</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Primo… undicesimo · il XIII secolo = il Duecento</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'accento di -esimo · che secolo?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Gli ordinali · i secoli · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Guida per un giorno · la storia e io</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Metà ottobre. Bruno è al secondo anno di Storia. A lezione di Storia medievale il professore (personaggio di una sola volta) parla della Bologna del XII secolo: quasi cento torri, costruite per difendersi e per mostrare la ricchezza; l'università, nata secondo la tradizione nel 1088. Sabato Bruno fa da guida a Camila (unità 30): le Due Torri (Camila non vuole salire i quasi 500 gradini dell'Asinelli), San Petronio (cominciata nel 1390, la facciata non è mai stata finita), il Nettuno del Cinquecento, l'Archiginnasio, i portici, patrimonio dell'UNESCO dal 2021. Camila: <i>Dovresti fare la guida turistica!</i></div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il brasiliano dice <i>em 1088</i>: in italiano <b>nel</b> 1088. I nomi dei secoli confondono: <i>il Duecento</i> è il XIII secolo (gli anni 1200), non il XII; lo studente dice <i>il Milletrecento</i> per il XIII secolo. Gli ordinali sono più facili che in portoghese (<i>décimo primeiro</i> → <i>undicesimo</i>), ma lo studente dimentica l'accordo (<i>la terzo volta</i>) e l'apostrofo (<i>l'undicesimo</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>L'Università di Bologna, l'<i>Alma Mater Studiorum</i>, è considerata la più antica del mondo occidentale (1088). Bologna ha tre soprannomi: <b>la Dotta</b> (per l'università), <b>la Grassa</b> (per la cucina) e <b>la Rossa</b> (per il colore dei tetti e dei palazzi). Nel centro ci sono quasi 40 km di portici: dal 2021 sono patrimonio dell'UNESCO.</div>
<div class="box"><h4>AUDIO</h4>Traccia 31.1 I due dialoghi (lento e naturale) · Traccia 31.2 Ascolta e ripeti · Traccia 31.3 Che secolo?</div>""")

    # Page 2
    p1 = [("Nel XII secolo a Bologna c'erano quasi", "cento torri"), ("Le famiglie costruivano le torri per", "difendersi e mostrare la ricchezza"),
          ("La torre degli Asinelli è alta", "97 metri"), ("L'università è nata nel", "1088"), ("Per la prossima lezione devono leggere", "il terzo e il quarto capitolo")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("La Garisenda è la torre storta.", "V"), ("Camila sale sulla torre degli Asinelli.", "F"), ("La facciata di San Petronio non è finita.", "V"),
          ("Il Nettuno è del Trecento.", "F"), ("Il portico di San Luca ha 666 archi.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: la Bologna antica", "10 min")}
{audiocard(["31.1 · SLOW", "31.1 · NATURAL"])}
{sub("A", "Prima parte. La lezione di Storia medievale. Completa.", "4 min", "31.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Bruno fa da guida a Camila. Vero (V) o falso (F)?", "4 min", "31.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa è stato l'Archiginnasio?", "2 min")}
<div class="wline">{R("La sede dell'università per più di duecento anni.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Il professore dice <i>il dodicesimo secolo, cioè il Millecento</i>: scrivere alla lavagna <i>XII = 1101–1200</i>.</li>
<li>B: frase 2: Camila preferisce <i>passare alla seconda cosa della lista</i>. Frase 4: il Nettuno è del <b>Cinquecento</b>.</li></ol>""")

    # Page 3
    rules = [("<i>il <b>terzo</b> capitolo</i>: <i>terzo</i> è un numero", ["ordinale", "cardinale"], "ordinale"),
             ("Dopo il 10 gli ordinali finiscono in", ["-esimo", "-imo"], "-esimo"),
             ("<i>la <b>seconda</b> cosa</i>: l'ordinale", ["si accorda con il nome", "non cambia"], "si accorda con il nome"),
             ("Il dodicesimo secolo (XII) è", ["il Millecento", "il Milleduecento"], "il Millecento"),
             ("<i>Il Trecento</i> sono gli anni", ["1301–1400", "1201–1300"], "1301–1400"),
             ("Con gli anni si dice", ["nel 1088", "in 1088"], "nel 1088")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("È la", ["terza", "terzo"], "terza", "volta che vengo a Bologna."), ("Dante è nato nel", ["Duecento", "Trecento"], "Duecento", "(1265)."),
          ("L'università è nata", ["nell'XI secolo", "nel XI secolo"], "nell'XI secolo", "."), ("Abito al", ["quinto", "cinque"], "quinto", "piano.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" .", ".") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: gli ordinali e i secoli", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Leggete il <b>terzo</b> e il <b>quarto</b> capitolo. · Passiamo alla <b>seconda</b> cosa della lista! · Devo finire il <b>secondo</b> anno.<br>
2. Siamo nel <b>dodicesimo secolo</b>, cioè nel <b>Millecento</b>. · Alla fine dell'<b>undicesimo</b> secolo.<br>
3. È nata <b>nel 1088</b>. · L'hanno cominciata <b>nel 1390</b>, <b>nel Trecento</b>. · Il Nettuno è <b>del Cinquecento</b>. · <b>Dal 2021</b> sono patrimonio dell'UNESCO.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Ordinali: <b>primo… decimo</b>, poi numero + <b>-esimo</b> (<i>undicesimo, ventesimo, centesimo</i>); si accordano (<i>la terza volta</i>). Secoli: <i>il XIII secolo</i> = <b>il Duecento</b> (1201–1300), <i>il XIV</i> = <b>il Trecento</b>, <i>il XX</i> = <b>il Novecento</b>. Anni: <b>nel</b> 1088, <b>dal</b> 2021. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: frase 4: il trucco: il secolo è <b>uno in più</b> delle centinaia (1100 → XII; 1300 → XIV), come in portoghese.</li>
<li>C: frase 3: <i>XI</i> si legge <i>undicesimo</i>, quindi <i>nell'</i>, con l'apostrofo.</li></ol>""")

    grammar_ref_it.ordinali_secoli(b)

    # Page 5
    opts3 = [["XI secolo", "XII secolo"], ["XIII secolo", "XIV secolo"], ["il Cinquecento", "il Seicento"],
             ["XIX secolo", "XX secolo"], ["XX secolo", "XXI secolo"], ["XII secolo", "XIII secolo"]]
    ans3 = ["XI secolo", "XIV secolo", "il Cinquecento", "XX secolo", "XXI secolo", "XIII secolo"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>È la terzo volta.</td><td><b>È la terza volta.</b></td><td>L'ordinale si accorda.</td></tr>
<tr><td>Il secolo tredici.</td><td><b>Il tredicesimo secolo.</b></td><td>Ordinale prima di <i>secolo</i>.</td></tr>
<tr><td>In 1088.</td><td><b>Nel 1088.</b></td><td>Anni: <i>nel</i>.</td></tr>
<tr><td>Il XIII secolo, il Milletrecento.</td><td><b>Il XIII secolo, il Duecento.</b></td><td>XIII = anni 1200.</td></tr>
<tr><td>Il undicesimo capitolo.</td><td><b>L'undicesimo capitolo.</b></td><td>Vocale: <i>l'</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["31.2", "31.3"])}
{sub("A", "Ascolta e ripeti. Negli ordinali in -esimo l'accento è sulla e: undicèsimo, ventèsimo, centèsimo.", "2 min", "31.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S312)}</div>
{sub("B", "Che secolo? Ascolta e scegli.", "2 min", "31.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: riga 4: far fare sempre la prova: <i>Duecento</i> = <i>anni 1200</i> = XIII.</li>
<li>4A: il brasiliano tende a dire <i>undicesìmo</i>; battere le mani su <i>-CÈ-</i>.</li>
<li>4B: 1 1088 → XI · 2 Trecento → XIV · 3 1566 → Cinquecento · 4 Novecento → XX · 5 2021 → XXI · 6 Duecento → XIII.</li></ol>""")

    # Page 6
    od = [("il 3° capitolo", "il terzo capitolo"), ("la 2ª volta", "la seconda volta"), ("il 21° secolo", "il ventunesimo secolo"),
          ("il 15° compleanno", "il quindicesimo compleanno"), ("la 100ª visita", "la centesima visita")]
    odl = "".join(f"<li>{a} → {A(c, 'min-width:44mm')}</li>" for a, c in od)
    sc = [("il XV secolo", "il Quattrocento"), ("il Seicento", "il XVII secolo"), ("nel 1492", "nel Quattrocento"), ("il Novecento", "il XX secolo"), ("nel 1265", "nel Duecento")]
    scl = [f'<li value="{i+1}">{a} → {A(c, "min-width:30mm")}</li>' for i, (a, c) in enumerate(sc)]
    wb = [("la storia", "storico"), ("il Medioevo", "medievale"), ("l'università", "universitario"), ("il turismo", "turistico")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Scrivi l'ordinale in lettere.", "3 min")}
<ol style="line-height:1.7">{odl}</ol>
{sub("B", "Il secolo con l'altro nome.", "4 min")}
{twocol(scl, 4)}
{sub("C", "Costruisci le parole. Dal nome all'aggettivo.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: <i>ventuno → ventunesimo</i> (cade la <i>o</i>); <i>la centesima</i>: femminile.</li>
<li>B: 1492 è nel XV secolo, cioè nel Quattrocento (il viaggio di Colombo).</li>
<li>C: <i>il centro storico, la città medievale, la mensa universitaria, il menù turistico</i>.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Guida per un giorno. Sei la guida della tua città. Presenta all'insegnante tre posti in ordine (il primo, il secondo, il terzo): quando sono nati, perché sono famosi, che cosa si vede. L'insegnante è il turista e fa domande.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>La prima cosa da vedere è… · È del Settecento / del XIX secolo. · L'hanno costruito nel… · È nato/a nel… · Si può salire / entrare. · Secondo la tradizione… · Alla fine dell'Ottocento… · Passiamo alla seconda cosa!</div>
{sub("B", "La storia e io. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Qual è il tuo secolo preferito? Perché?</li><li>In che anno è nata la tua città? In che secolo?</li><li>Qual è la prima cosa che fai in una città nuova?</li><li>Hai mai fatto da guida a un amico straniero? Dove l'hai portato?</li><li>Secondo te, è importante studiare la storia? Perché?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: per le città brasiliane: Salvador (1549, Cinquecento), Rio de Janeiro (1565), San Paolo (1554), Belo Horizonte (1897, fine Ottocento), Brasília (1960, Novecento).</li>
<li>B: domanda 2: <i>nel</i> + anno; domanda 4: <i>l'ho portato a…</i> (unità A2 11).</li></ol>""")

    # Page 8
    pc = [("A2 · 30", "So dare consigli con dovresti e ti consiglio di."), ("A2 · 31", "So usare gli ordinali (terzo, undicesimo, ventesimo)."),
          ("A2 · 31", "So dire i secoli (il Duecento, il XIII secolo)."), ("A2 · 31", "So raccontare la storia di un posto con le date."),
          ("A2 · 31", "So fare da guida in una città.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("È la terzo volta che vengo.", "È la terza volta che vengo."), ("Il XIII secolo è il Duecento.", "✓"),
          ("La città è nata in 1554.", "La città è nata nel 1554."), ("Il secolo venti è stato difficile.", "Il ventesimo secolo è stato difficile."),
          ("È la mia prima visita a Roma.", "✓"), ("Abito al undicesimo piano.", "Abito all'undicesimo piano.")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Un posto della mia città (50–75 parole).</b> Scrivi la storia di un monumento, una piazza o un palazzo della tua città: quando è nato, in che secolo, che cosa è successo, perché è importante oggi. Usa almeno due ordinali e un secolo con il nome (<i>il Novecento…</i>).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il testo; l'insegnante chiede <i>In che secolo? E prima?</i> Unità 32: <i>Ce la faccio!</i> (la maratona di Davide: farcela, metterci, ce n'è / ce ne sono).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("31.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("31.2", "Ascolta e ripeti")}
<p>{" · ".join(S312)}</p>
{sub("31.3", "Che secolo?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S313))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 31 - Un po' di storia")
