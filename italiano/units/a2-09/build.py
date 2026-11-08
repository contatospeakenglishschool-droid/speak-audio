# Speak! Ponte A2 - Unità 09 "Secondo me…" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 09", audio_json=os.path.join(HERE, "audio_it-a2-unita-09.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il giornale", "giornale"), ("B", "il plastico", "plastico"), ("C", "il parco", "parco"), ("D", "il palazzo", "palazzo"),
          ("E", "la pista ciclabile", "pista ciclabile"), ("F", "gli amici al bar", "amici al bar"), ("G", "il cantiere", "cantiere"), ("H", "l'inaugurazione", "inaugurazione")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-09"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["09.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S092 = [x.split(": ", 1)[1] for x in _r["09.2 Ripeti le opinioni"].split("\n")]
S093 = [x.split(": ", 1)[1] for x in _r["09.3 Indicativo o congiuntivo"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split(" ", 1)[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 09", "Secondo me…", "Opinioni e speranze · <b>primo incontro con il congiuntivo</b>",
                       [("SAI FARE", "dare la tua opinione, essere d'accordo o no, e parlare delle tue speranze"),
                        ("LINGUA", "Secondo me è caro. · Penso che sia caro. · Spero che il Comune scelga noi."),
                        ("PRONUNCIA", "la voce dell'opinione · indicativo o congiuntivo?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: la mia città", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali di queste cose ci sono vicino a casa tua?</li><li>Che cosa manca nella tua città? Un parco, una pista ciclabile…?</li><li>Leggi il giornale? Su carta o sul telefono?</li></ol>""",
    22, """<ol><li>A: <i>il plastico</i> = il modello in piccolo di un progetto di architettura. <i>Il cantiere</i>: dove si costruisce.</li>
<li>B: lo studente userà spontaneamente <i>secondo me</i> o <i>penso che è</i>: annotare e riprendere a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: la città</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il progetto del giardino · gli affitti a Bologna · la bella notizia</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Penso, credo, spero che + congiuntivo · secondo me + indicativo</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Forme · espressioni · indicativo o congiuntivo · di + infinito</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>La voce dell'opinione · indicativo o congiuntivo?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Scegli il modo · essere e avere · speranze per gli amici</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Sei d'accordo? (dibattito) · le tue speranze</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 01–09) e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Marzo. Marco e Júlia aspettano la risposta del Comune: il loro progetto è un giardino in Bolognina con alberi, panchine e una pista ciclabile. Marco pensa che sia il migliore, Júlia spera che il Comune scelga loro. Al bar Davide legge che gli affitti sono aumentati: Giulia pensa che Bologna sia diventata troppo cara, Davide crede che sia ancora la città più bella d'Italia, Júlia è d'accordo con lui. Venerdì sera la signora Rossi ha letto sul giornale la notizia: il Comune ha scelto il progetto di Marco e Júlia. I lavori cominceranno a maggio e l'inaugurazione sarà a settembre: la signora Rossi verrà con Franco e Briciola.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese ha il congiuntivo (<i>espero que venha</i>), ma dopo <i>acho que</i> usa l'indicativo (<i>acho que é caro</i>). Per questo lo studente dice <i>penso che è caro</i>: con <i>spero che</i> invece sbaglia poco. Altri errori: <i>secondo me sia</i> (→ <b>secondo me è</b>), <i>vadi, facci</i> (→ <b>vada, faccia</b>) e <i>spero che io vinca</i> (→ <b>spero di vincere</b>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Gli italiani amano discutere: al bar si parla di calcio, politica e prezzi, e non essere d'accordo è normale e anche divertente. A Bologna gli <b>affitti</b> sono tra i più cari d'Italia, per i tanti studenti universitari e i turisti. La <b>Bolognina</b> è un quartiere a nord della stazione, oggi in grande trasformazione.</div>
<div class="box"><h4>AUDIO</h4>Traccia 09.1 Tre dialoghi (lento e naturale) · Traccia 09.2 Le opinioni · Traccia 09.3 Indicativo o congiuntivo?</div>""")

    # Page 2
    st = [("Che cosa aspettano Marco e Júlia?", "la risposta del Comune sul progetto"), ("Com'è il loro progetto?", "un giardino con alberi, panchine e una pista ciclabile"),
          ("Che cosa spera Júlia?", "che il Comune scelga loro")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    who = [("Bologna è diventata troppo cara.", "Giulia"), ("È ancora la città più bella d'Italia.", "Davide"), ("La gente vive bene, va dappertutto in bicicletta.", "Júlia"),
           ("In bicicletta con la pioggia? Non sono d'accordo!", "Giulia"), ("Spero che a ottobre non piova.", "Davide")]
    wl = "".join(f"<tr><td>{s}</td><td style='width:26mm;text-align:center'>{A(w, 'min-width:18mm')}</td></tr>" for s, w in who)
    b.page(f"""{sec(2, "Ascolto: speriamo bene!", "10 min")}
<p>Marco e Júlia aspettano una risposta importante, al bar si discute di Bologna e la signora Rossi ha letto una notizia sul giornale.</p>
{audiocard(["09.1 · SLOW", "09.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "09.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Chi lo pensa? Davide, Giulia o Júlia?", "4 min", "09.1 · NATURAL")}
<table style="margin:0">{wl}</table>
{sub("C", "Dialogo 3. Qual è la bella notizia? Quando sarà pronto il giardino?", "3 min")}
<div class="wline">{R("il Comune ha scelto il loro progetto · a settembre (i lavori cominciano a maggio)")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Far notare <i>secondo me <b>arriva</b></i> e <i>penso che <b>sia</b></i>: due modi per la stessa idea.</li>
<li>B: versione <b>naturale</b>. Poi chiedere: <i>E tu, con chi sei d'accordo?</i></li></ol>""")

    # Page 3
    rules = [("Dopo <b>penso che</b>, <b>credo che</b> e <b>spero che</b> usiamo", ["il congiuntivo (sia, scelga)", "l'indicativo (è, sceglie)"], "il congiuntivo (sia, scelga)"),
             ("Dopo <b>secondo me</b> usiamo", ["l'indicativo (è)", "il congiuntivo (sia)"], "l'indicativo (è)"),
             ("<i>Sia, abbia, scelga, piova</i> sono come", ["l'imperativo formale (unità 08)", "il futuro (unità 07)"], "l'imperativo formale (unità 08)"),
             ("Al congiuntivo <i>io, tu, lui, lei</i> hanno", ["la stessa forma", "tre forme diverse"], "la stessa forma"),
             ("<i>Sono sicura che</i> e <i>so che</i> presentano", ["un fatto sicuro: indicativo", "un dubbio: congiuntivo"], "un fatto sicuro: indicativo"),
             ("<i>Spero di vincere</i>: con lo stesso soggetto usiamo", ["di + infinito", "che + congiuntivo"], "di + infinito")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Secondo me Bologna", ["è", "sia"], "è", "bellissima."), ("Penso che gli affitti", ["sono", "siano"], "siano", "troppo cari."),
          ("Spero che il Comune", ["sceglie", "scelga"], "scelga", "il nostro progetto."), ("So che Marco", ["ha", "abbia"], "ha", "lavorato tanto."),
          ("Credo che Davide", ["ha", "abbia"], "abbia", "ragione."), ("Mi sembra che qui la gente", ["vive", "viva"], "viva", "bene.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: penso che sia…", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Penso che</b> il nostro progetto <b>sia</b> il migliore. · <b>Credo che</b> gli altri studi <b>abbiano</b> idee molto buone.<br>
2. <b>Spero che</b> il Comune <b>scelga</b> noi. · <b>Spero che</b> a ottobre non <b>piova</b>. · <b>Spero che</b> Lei <b>venga</b>!<br>
3. <b>Mi sembra che</b> qui la gente <b>viva</b> bene.<br>
4. <b>Secondo me</b> la decisione <b>arriva</b> venerdì. · <b>Secondo me</b> Bologna <b>è diventata</b> troppo cara.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Indicativo o congiuntivo? Scegli.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>penso che · credo che · spero che · mi sembra che</b> + <b>congiuntivo</b> (<i>sia, abbia, scelga, vada</i>). <b>secondo me · so che · sono sicuro/a che</b> + <b>indicativo</b> (<i>è, ha, sceglie</i>). Stesso soggetto: <b>di + infinito</b> (<i>spero di vincere</i>). Le forme del congiuntivo sono come l'imperativo formale. Tutto: pagina 4.</div>""",
    20, """<ol><li>B: è un primo contatto: basta riconoscere le espressioni e usare <i>sia, abbia</i> e i verbi più frequenti.</li>
<li>C: 4: <i>so che</i> = un fatto sicuro (indicativo). Chiedere: <i>Opinione o certezza?</i></li></ol>""")

    grammar_ref_it.congiuntivo_presente(b)

    # Page 5
    ans3 = ["congiuntivo", "indicativo", "congiuntivo", "indicativo", "congiuntivo", "indicativo"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Penso che Bologna è cara.</td><td><b>Penso che Bologna sia cara.</b></td><td><i>penso che</i> + congiuntivo.</td></tr>
<tr><td>Secondo me sia cara.</td><td><b>Secondo me è cara.</b></td><td><i>secondo me</i> + indicativo.</td></tr>
<tr><td>Spero che vadi tutto bene.</td><td><b>Spero che vada tutto bene.</b></td><td>Irregolare: <i>vada</i>.</td></tr>
<tr><td>Spero che io vinca la maratona.</td><td><b>Spero di vincere la maratona.</b></td><td>Stesso soggetto: <i>di</i> + infinito.</td></tr>
<tr><td>Sono d'accordo a te.</td><td><b>Sono d'accordo con te.</b></td><td><i>d'accordo con</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["09.2", "09.3"])}
{sub("A", "La voce dell'opinione. Ascolta e ripeti: una piccola pausa dopo «secondo me…» e «penso che…».", "2 min", "09.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S092)}</div>
{sub("B", "Indicativo o congiuntivo? Ascolta e scegli.", "2 min", "09.3")}
{twocol([f'<li value="{i+1}">{ch(["indicativo", "congiuntivo"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: nel parlato veloce alcuni italiani dicono <i>penso che è</i>, ma nello scritto e all'esame (CILS) il congiuntivo è necessario.</li>
<li>4B: le frasi sono 1 penso che sia, 2 secondo me è, 3 spero che venga, 4 so che viene, 5 credo che abbia, 6 sono sicura che ha.</li></ol>""")

    # Page 6
    ea = [("Penso che Marco", "sia", " molto bravo."), ("Credo che Giulia", "abbia", " ragione sugli affitti."), ("Spero che voi", "siate", " contenti del giardino."),
          ("Mi sembra che i turisti", "siano", " sempre di più."), ("Penso che tu", "abbia", " bisogno di una vacanza.")]
    eal = "".join(f"<li>{a} {A(c, 'min-width:18mm')}{z}</li>" for a, c, z in ea)
    hp = [("Davide corre la maratona a ottobre.", "Spero che Davide finisca la maratona!"), ("Bruno si laurea a luglio.", "Spero che Bruno prenda un bel voto."),
          ("Giulia vende le colombe a Pasqua.", "Spero che i clienti le comprino tutte."), ("Il giardino sarà pronto a settembre.", "Spero che non ci siano ritardi.")]
    hpl = "".join(f"<li>{a}<div class='wline'>{R(c)}</div></li>" for a, c in hp)
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Essere o avere? Scrivi il congiuntivo (sia, siate, siano, abbia…).", "3 min")}
<ol style="line-height:1.75">{eal}</ol>
{sub("B", "Le speranze per gli amici. Scrivi una frase con spero che… per ogni notizia.", "4 min")}
<ol style="line-height:1.5">{hpl}</ol>
{sub("C", "E tu? Completa con la tua opinione.", "2 min")}
<ol style="line-height:1.9"><li>Secondo me la mia città <span class="wline" style="display:inline-block;width:90mm"></span></li>
<li>Penso che l'italiano <span class="wline" style="display:inline-block;width:96mm"></span></li>
<li>Spero di <span class="wline" style="display:inline-block;width:110mm"></span></li></ol>""",
    20, """<ol><li>A: tutte le forme sono di <i>essere</i> e <i>avere</i>: i due verbi più usati con il congiuntivo.</li>
<li>B: accettare ogni speranza corretta. Promemoria: <i>-are → -i</i> (<i>compri</i>), <i>-ere/-ire → -a</i> (<i>prenda, finisca</i>).</li></ol>""")

    # Page 7
    cards = ["In città tutti dovrebbero andare in bicicletta.", "È meglio vivere in una città piccola che in una grande.", "Gli affitti sono troppo cari per i giovani.",
             "Imparare una lingua da adulti è facile.", "I social network ci rendono più soli.", "Il calcio è lo sport più bello del mondo."]
    cl = "".join(f'<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>{i+1}.</b> {t}</div>' for i, t in enumerate(cards))
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Sei d'accordo? Scegli una frase e dai la tua opinione con due ragioni. L'insegnante risponde: è d'accordo o no? Poi cambiate.", "7 min")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;margin-top:1mm">{cl}</div>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Secondo me… · Per me… · Penso che… · Credo che… · Mi sembra che… · Sono d'accordo (con te). · Non sono d'accordo. · Hai ragione. · Dipende. · Da una parte… dall'altra… · Invece…</div>
{sub("B", "Le tue speranze. Rispondi e fai le stesse domande all'insegnante.", "5 min")}
<ol style="line-height:1.6"><li>Che cosa speri per quest'anno?</li><li>Che cosa speri per la tua città o per il tuo paese?</li><li>Che cosa pensi che sia la cosa più difficile dell'italiano? E la più bella?</li></ol>""",
    22, """<ol><li>A: incoraggiare il disaccordo gentile: <i>Capisco, ma secondo me…</i> Annotare <i>penso che è</i> e correggere alla fine.</li>
<li>B: domanda 3: lo studente risponde con <i>penso che sia…</i> o <i>secondo me è…</i></li></ol>""")

    # Page 8
    pc = [("A2 · 01–03", "So descrivere vestiti, ricordi e raccontare una storia al passato."), ("A2 · 04–05", "So dare consigli e chiedere in modo gentile (imperativo, condizionale)."),
          ("A2 · 06–08", "So parlare di lavoro, progetti e servizi (futuro, imperativo formale)."), ("A2 · 09", "So dare la mia opinione: secondo me…, penso che sia…"),
          ("A2 · 09", "So esprimere una speranza: spero che…, spero di…")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Penso che il film è bellissimo.", "Penso che il film sia…"), ("Secondo me hai ragione.", "✓"),
          ("Spero che tu stai meglio.", "Spero che tu stia meglio."), ("Credo che Marco abbia ragione.", "✓"),
          ("Spero che io trovi un lavoro.", "Spero di trovare un lavoro."), ("Secondo me sia troppo tardi.", "Secondo me è troppo tardi.")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione: unità 01–09", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. La mia città: pro e contro (50–75 parole).</b> Che cosa ti piace e che cosa non ti piace della tua città? Che cosa speri per il futuro? Usa <i>secondo me, penso che, spero che</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il testo e l'insegnante risponde con la sua opinione. Poi il <b>Ripasso 1</b> (unità 01–09): ripassare prima le unità con più «Non ancora».</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("09.1", "Speriamo bene! (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("09.2", "Le opinioni")}
<p>{" · ".join(S092)}</p>
{sub("09.3", "Indicativo o congiuntivo?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S093))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 09 - Secondo me")
