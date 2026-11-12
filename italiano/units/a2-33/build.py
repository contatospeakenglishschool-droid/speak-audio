# Speak! Ponte A2 - Unità 33 "Ci siamo conosciuti così" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 33", audio_json=os.path.join(HERE, "audio_it-a2-unita-33.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la festa", "festa"), ("B", "la coppia", "coppia"), ("C", "i messaggi", "messaggi"), ("D", "le fedi", "fedi"),
          ("E", "il matrimonio", "matrimonio"), ("F", "il carnevale", "carnevale"), ("G", "il sorriso", "sorriso"), ("H", "le candeline", "candeline")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-33"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["33.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S332 = [x.split(": ", 1)[1] for x in _r["33.2 Ripeti"].split("\n")]
S333 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["33.3 L'uno con l'altro"].split("\n")]


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
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 33", "Ci siamo conosciuti così", "Storie d'amore e d'amicizia · <b>ci siamo conosciuti · si sono sposati · mentre · quando</b>",
                       [("SAI FARE", "raccontare come si sono conosciute due persone, parlare di amore e amicizia, raccontare con lo sfondo e i fatti"),
                        ("LINGUA", "Come vi siete conosciuti? · Ci scrivevamo tutti i giorni. · Mentre tutti ballavano, io parlavo. · Quando la musica è finita, …"),
                        ("PRONUNCIA", "la voce di mentre: sale, poi scende")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: storie di coppia", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Conosci una bella storia d'amore? Di chi?</li><li>Secondo te, dov'è più facile conoscere gente nuova?</li><li>Festeggi gli anniversari? Quali?</li></ol>""",
    28, """<ol><li>A: <i>le fedi</i> = gli anelli del matrimonio (<i>la fede</i>); <i>le candeline</i> = le piccole candele sulla torta; <i>la coppia</i> = due persone che stanno insieme.</li>
<li>B: argomento personale: lo studente può parlare di amici, di film o di libri; non insistere sulla vita privata.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: amore e feste</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Bruno e Chiara · i genitori di Camila</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>I verbi reciproci · mentre e quando</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Ci siamo conosciuti · mentre + imperfetto</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>La voce di mentre · l'uno con l'altro?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Il passato dei reciproci · mentre / quando · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Come si sono conosciuti? · amore e amicizia</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio novembre. Bruno e Chiara stanno insieme da un anno e Júlia fa una cena per loro, con Camila. Si sono conosciuti a una festa quando Bruno era a Bologna in vacanza da Júlia (unità A1 20: Chiara è timida, Bruno parla sempre): <i>mentre tutti ballavano, io parlavo e lei ascoltava</i>. Quando Bruno è tornato in Brasile <i>si scrivevano</i> ogni giorno; quando è tornato per studiare <i>si sono messi insieme</i>. Camila racconta i suoi genitori: <i>si sono conosciuti</i> al Carnevale di Olinda (lui suonava il frevo, lei ballava) e <i>si sono sposati</i> dopo sei mesi. E lei? Ieri un ragazzo le ha sorriso alla fermata, poi è salito sul suo autobus… ma non si sono parlati.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Nos conhecemos, se casaram</i> funzionano come in italiano, ma in portoghese l'ausiliare è sempre <i>ter</i>: lo studente dice <i>abbiamo conosciuto</i> invece di <i>ci siamo conosciuti</i> e dimentica l'accordo (<i>si sono sposato</i>). <i>Casar com</i> diventa <i>sposare con</i> (si dice <i>sposare qualcuno</i> o <i>sposarsi con</i>), <i>apaixonar-se por</i> diventa <i>innamorarsi per</i> (si dice <i>innamorarsi di</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia ci si sposa sempre più tardi: in media verso i 33–35 anni, e molte coppie vivono insieme prima del matrimonio. Le parole della coppia: <i>stare insieme</i>, <i>mettersi insieme</i>, <i>il mio ragazzo / la mia ragazza</i>, <i>il fidanzato / la fidanzata</i>, <i>il colpo di fulmine</i> (l'amore a prima vista).</div>
<div class="box"><h4>AUDIO</h4>Traccia 33.1 I due dialoghi (lento e naturale) · Traccia 33.2 Ascolta e ripeti · Traccia 33.3 L'uno con l'altro?</div>""")

    # Page 2
    p1 = [("Bruno e Chiara stanno insieme da", "un anno"), ("Si sono conosciuti a", "una festa"), ("Quando Bruno era in Brasile si scrivevano", "tutti i giorni"),
          ("Si telefonavano", "la domenica"), ("Adesso si vedono", "quasi ogni giorno")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("I genitori di Camila si sono conosciuti a Recife.", "F"), ("Il padre di Camila suonava il frevo.", "V"), ("Si sono sposati dopo sei anni.", "F"),
          ("Un ragazzo ha sorriso a Camila alla fermata.", "V"), ("Camila e il ragazzo si sono parlati.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: un anno insieme", "10 min")}
{audiocard(["33.1 · SLOW", "33.1 · NATURAL"])}
{sub("A", "Prima parte. Bruno e Chiara raccontano. Completa.", "4 min", "33.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Camila racconta. Vero (V) o falso (F)?", "4 min", "33.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa consiglia Júlia a Camila?", "2 min")}
<div class="wline">{R("Di parlare lei al ragazzo la prossima volta.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Bruno e Chiara si sono conosciuti nell'unità A1 20 (la festa raccontata da Davide).</li>
<li>B: frase 1: a <b>Olinda</b>, vicino a Recife; frase 3: dopo sei <b>mesi</b>. Il <i>frevo</i> è la musica del Carnevale di Pernambuco.</li></ol>""")

    # Page 3
    rules = [("<i>Ci siamo conosciuti</i> (io ho conosciuto lei, lei ha conosciuto me): il verbo è", ["reciproco", "riflessivo"], "reciproco"),
             ("I verbi reciproci sono sempre", ["al plurale", "al singolare"], "al plurale"),
             ("Al passato prossimo usano", ["essere", "avere"], "essere"),
             ("<i>Mentre tutti ballavano</i>: dopo <i>mentre</i> di solito c'è", ["l'imperfetto", "il passato prossimo"], "l'imperfetto"),
             ("<i>Quando la musica è finita, lui le ha chiesto il numero</i>: sono", ["fatti brevi", "azioni in corso"], "fatti brevi"),
             ("<i>Mentre aspettavo, un ragazzo mi ha sorriso</i>: l'azione che interrompe è", ["al passato prossimo", "all'imperfetto"], "al passato prossimo")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Io e Marco", ["ci siamo visti", "abbiamo visto"], "ci siamo visti", "ieri."), ("Bruno e Chiara", ["si sono messi", "si è messo"], "si sono messi", "insieme."),
          ("Mentre", ["cucinavo", "ho cucinato"], "cucinavo", ", è arrivata Camila."), ("Quando", ["è arrivato", "arrivava"], "è arrivato", "il treno, siamo saliti.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" ,", ",") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: ci siamo conosciuti · mentre e quando", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Come <b>vi siete conosciuti</b>? — <b>Ci siamo conosciuti</b> a una festa. · <b>Ci scrivevamo</b> tutti i giorni. · <b>Ci siamo messi</b> insieme.<br>
2. I miei genitori <b>si sono conosciuti</b> a Olinda. · <b>Si sono sposati</b> dopo sei mesi. · E <b>vi siete parlati</b>?<br>
3. <b>Mentre</b> tutti <b>ballavano</b>, io <b>parlavo</b>. · <b>Quando</b> la musica <b>è finita</b>, lui le <b>ha chiesto</b> il numero. · <b>Mentre aspettavo</b> l'autobus, un ragazzo mi <b>ha sorriso</b>.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Reciproci: <b>ci / vi / si</b> + verbo al plurale (<i>ci vediamo, si scrivono</i>); al passato <b>essere</b> + participio accordato (<i>ci siamo conosciuti/e</i>). Racconto: <b>mentre</b> + imperfetto = lo sfondo, l'azione in corso; <b>quando</b> + passato prossimo = il fatto (unità 03). Tutto: pagina 4.</div>""",
    22, """<ol><li>B: frase 1: disegnare due frecce che si incrociano (reciproco) e una freccia che torna su se stessa (riflessivo: <i>mi lavo</i>).</li>
<li>B: frasi 4–6: ripasso dell'unità A2 03 (imperfetto e passato prossimo), qui con <i>mentre</i> e <i>quando</i>.</li></ol>""")

    grammar_ref_it.reciproci_mentre(b)

    # Page 5
    opts3 = [["l'uno con l'altro", "da solo"]] * 6
    ans3 = ["l'uno con l'altro", "da solo", "l'uno con l'altro", "da solo", "l'uno con l'altro", "da solo"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Abbiamo conosciuto a una festa.</td><td><b>Ci siamo conosciuti a una festa.</b></td><td>Reciproco: <i>ci</i> + <i>essere</i>.</td></tr>
<tr><td>Si sono sposato.</td><td><b>Si sono sposati.</b></td><td>Participio plurale.</td></tr>
<tr><td>Mentre ho aspettato, lui sorrideva.</td><td><b>Mentre aspettavo, lui ha sorriso.</b></td><td>Sfondo / fatto.</td></tr>
<tr><td>Si è innamorata con lui.</td><td><b>Si è innamorata di lui.</b></td><td><i>Innamorarsi di</i>.</td></tr>
<tr><td>Ha sposato con Marco.</td><td><b>Ha sposato Marco. / Si è sposata con Marco.</b></td><td><i>Sposare</i> qualcuno.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["33.2", "33.3"])}
{sub("A", "Ascolta e ripeti. Con mentre la voce sale e resta «aperta», poi scende alla fine: Mentre aspettavo l'autobus ↗, un ragazzo mi ha sorriso ↘.", "2 min", "33.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S332)}</div>
{sub("B", "L'uno con l'altro o da solo? Ascolta e scegli.", "2 min", "33.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: riga 3: l'imperfetto è lo sfondo (aspettavo), il passato prossimo il fatto nuovo (ha sorriso).</li>
<li>4A: far muovere la mano: su alla virgola, giù alla fine.</li>
<li>4B: <i>mi sono svegliato, si è vestita, ci laviamo le mani</i> = riflessivi (ognuno per sé); <i>ci siamo visti, si sono sposati, ci scriviamo</i> = reciproci.</li></ol>""")

    # Page 6
    rp = [("(conoscersi) Io e Chiara", "ci siamo conosciuti", "a una festa."), ("(sposarsi) I miei genitori", "si sono sposati", "nel 1995."),
          ("(vedersi) Tu e Marco", "vi siete visti", "ieri?"), ("(salutarsi) Noi", "ci siamo salutati", "e siamo andati a casa."),
          ("(scriversi, imperfetto) Bruno e Chiara", "si scrivevano", "ogni giorno.")]
    rpl = "".join(f"<li>{a} {A(r, 'min-width:32mm')} {z}</li>" for a, r, z in rp)
    mq = [("io / guidare — telefonare mia madre", "Mentre guidavo, ha telefonato mia madre."), ("noi / cenare — andare via la luce", "Mentre cenavamo, è andata via la luce."),
          ("Camila / aspettare l'autobus — un ragazzo / sorridere", "Mentre Camila aspettava l'autobus, un ragazzo le ha sorriso."),
          ("finire il film — noi / andare a casa", "Quando è finito il film, siamo andati a casa.")]
    mql = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in mq)
    wb = [("incontrare", "l'incontro"), ("salutare", "il saluto"), ("ballare", "il ballo"), ("sposarsi", "lo sposo / la sposa")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Completa con il verbo reciproco al passato prossimo.", "3 min")}
<ol style="line-height:1.7">{rpl}</ol>
{sub("B", "Scrivi una frase con mentre o quando.", "4 min")}
<ol style="line-height:1.4">{mql}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 5: l'abitudine nel passato va all'imperfetto (<i>si scrivevano ogni giorno</i>).</li>
<li>B: accettare anche <i>Mentre guidavo, mia madre mi ha telefonato</i>. <i>Andare via la luce</i> = non c'è più elettricità.</li>
<li>C: <i>gli sposi</i> = la coppia il giorno del matrimonio.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Come si sono conosciuti? Racconta all'insegnante come si sono conosciute due persone importanti per te (i tuoi genitori, due amici, tu e il tuo migliore amico…): dove, quando, che cosa succedeva, che cosa è successo dopo. L'insegnante fa domande. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Si sono conosciuti a / al… · Mentre…, … · Quando…, … · Si sono messi insieme. · Si sono sposati nel… · Si scrivevano / si telefonavano. · È stato un colpo di fulmine! · Non si sono più lasciati.</div>
{sub("B", "Amore e amicizia. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Dove si conosce gente nuova nella tua città?</li><li>Come hai conosciuto il tuo migliore amico o la tua migliore amica?</li><li>Con chi ti scrivi ogni giorno?</li><li>Credi nel colpo di fulmine?</li><li>Secondo te, che cosa dovrebbe fare Camila se rivede il ragazzo dell'autobus?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: se lo studente preferisce non parlare della sua vita, può raccontare la storia di una coppia famosa o di un film.</li>
<li>B: domanda 5: <i>dovrebbe</i> (unità 30): <i>Dovrebbe parlargli, dovrebbe sorridere anche lei…</i></li></ol>""")

    # Page 8
    pc = [("A2 · 32", "So usare ce la faccio e ci metto."), ("A2 · 33", "So usare i verbi reciproci (ci siamo conosciuti)."),
          ("A2 · 33", "So raccontare con mentre e quando."), ("A2 · 33", "So raccontare come si sono conosciute due persone."),
          ("A2 · 33", "So parlare di amore e di amicizia.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Abbiamo conosciuto a scuola.", "Ci siamo conosciuti a scuola."), ("Si sono sposati nel 2010.", "✓"),
          ("Mentre ho cucinato, è arrivata mia sorella.", "Mentre cucinavo, è arrivata mia sorella."), ("Ci scriviamo ogni giorno.", "✓"),
          ("Si è innamorato con Chiara.", "Si è innamorato di Chiara."), ("Mia madre e mia zia si sono visto ieri.", "Si sono viste ieri.")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Una storia d'amore o d'amicizia (50–75 parole).</b> Racconta come si sono conosciute due persone (vere o di un film): dove, che cosa succedeva, che cosa è successo dopo. Usa almeno due verbi reciproci, una frase con <i>mentre</i> e una con <i>quando</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge la storia; l'insegnante chiede <i>E poi? Si sono lasciati?</i> Unità 34: <i>Che cosa ne pensi?</i> (opinioni e accordo: penso di + infinito, penso che; ne = di questo).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("33.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("33.2", "Ascolta e ripeti")}
<p>{" · ".join(S332)}</p>
{sub("33.3", "L'uno con l'altro?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S333))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 33 - Ci siamo conosciuti così")
