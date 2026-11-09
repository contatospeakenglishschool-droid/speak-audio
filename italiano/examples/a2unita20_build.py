# Speak! Ponte A2 - Unità 20 "Il primo esame" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 20", audio_json=os.path.join(HERE, "audio_it-a2-unita-20.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'aula", "aula"), ("B", "gli appunti", "appunti"), ("C", "l'evidenziatore", "evidenziatore"), ("D", "la sveglia", "sveglia"),
          ("E", "agitato", "agitato"), ("F", "il professore", "professore"), ("G", "lo zaino", "zaino"), ("H", "festeggiare", "festeggiare")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-20"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["20.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S202 = [x.split(": ", 1)[1] for x in _r["20.2 Ripeti"].split("\n")]
S203 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["20.3 A o di"].split("\n")]


def _key(w):
    w = w.split("'")[-1] if "'" in w else (w.split(" ", 1)[1] if " " in w else w)
    return w.lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 20", "Il primo esame", "Lo studio e gli esami · <b>cominciare a · finire di · provare a · decidere di · smettere di</b>",
                       [("SAI FARE", "parlare di studio ed esami, incoraggiare una persona agitata, raccontare come è andata, fare promesse e propositi"),
                        ("LINGUA", "Ho cominciato a studiare. · Non ho finito di ripassare. · Smetti di preoccuparti! · Ho deciso di… · Prova a…"),
                        ("PRONUNCIA", "a + consonante doppia: a presto [apprèsto], a casa [akkàsa]")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: studiare", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Hai fatto un esame importante? Quale? Com'è andato?</li><li>Come studi: con gli appunti, con l'evidenziatore, con la musica?</li><li>Che cosa fai quando sei agitato o agitata?</li></ol>""",
    24, """<ol><li>A: <i>l'aula</i> = la sala delle lezioni; <i>gli appunti</i> = quello che scrivi a lezione; <i>agitato</i> = nervoso, preoccupato.</li>
<li>B: annotare frasi come <i>ho cominciato…, ho deciso…</i>: le riprendiamo a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: lo studio</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La mattina dell'esame · la sera al bar</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Verbi + a / di + infinito</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Verbi + a · verbi + di · senza preposizione</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>a + doppia · a o di?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>a, di o niente? · i propositi di Bruno · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Calma un amico agitato · i miei propositi</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine giugno. Bruno, il fratello di Júlia, dà l'esame di Storia medievale (a novembre aveva preso trenta a una prova di storia; ad aprile Chiara diceva che era ancora a pagina cento, unità 11). Alle sette di mattina telefona a Júlia: non riesce a dormire, non ha finito di ripassare l'ultimo capitolo, ha paura di dimenticare le date, ha deciso di non bere il caffè. Júlia: <i>Smetti di preoccuparti, prova a respirare, ricordati di portare il documento!</i> La sera al bar: ventotto! Il professore ha cominciato con Carlo Magno; Bruno ha dimenticato una data, però ha continuato a parlare. Chiara racconta che Bruno ha promesso di smettere di giocare ai videogiochi fino a settembre. Giulia offre da bere.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese usa <i>decidir</i>, <i>tentar</i>, <i>prometer</i> senza preposizione: lo studente dice <i>ho deciso partire</i> (→ <b>ho deciso di partire</b>), <i>ho promesso studiare</i> (→ <b>di studiare</b>). Al contrario aggiunge <i>di</i> dopo i modali: <i>voglio di dormire</i> (→ <b>voglio dormire</b>). <i>Parar de</i> → <b>smettere di</b> (non <i>fermare di</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>All'università italiana molti esami sono <b>orali</b>: lo studente parla con il professore per 15–30 minuti. I voti vanno da <b>18</b> (sufficiente) a <b>30</b>; il massimo è <b>30 e lode</b>. Lo studente può rifiutare il voto e ripetere l'esame. Ci sono diverse <b>sessioni</b>: gennaio–febbraio, giugno–luglio e settembre.</div>
<div class="box"><h4>AUDIO</h4>Traccia 20.1 I due dialoghi (lento e naturale) · Traccia 20.2 Ascolta e ripeti · Traccia 20.3 A o di?</div>""")

    # Page 2
    p1 = [("Bruno non riesce", "a dormire"), ("Non ha finito", "di ripassare l'ultimo capitolo"), ("Ha paura", "di dimenticare tutte le date"),
          ("Ha deciso", "di non bere il caffè"), ("Júlia: Ricordati", "di portare il documento!")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:62mm')}</td></tr>" for a, x in p1)
    vf = [("Bruno ha preso trenta.", "F"), ("Il professore ha cominciato con Carlo Magno.", "V"), ("Bruno ha dimenticato una data.", "V"),
          ("Dopo la data Bruno ha smesso di parlare.", "F"), ("A settembre Bruno ha un altro esame.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: il giorno dell'esame", "10 min")}
{audiocard(["20.1 · SLOW", "20.1 · NATURAL"])}
{sub("A", "Prima parte. Alle sette di mattina Bruno telefona a Júlia. Completa.", "4 min", "20.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. La sera, al bar. Vero (V) o falso (F)?", "4 min", "20.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa ha promesso Bruno? Perché?", "2 min")}
<div class="wline">{R("Di smettere di giocare ai videogiochi fino a settembre: c'è un altro esame.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>; far notare che ogni frase ha <i>a</i> o <i>di</i> + infinito. <i>Sorellina</i> = sorella (con affetto).</li>
<li>B: frase 1: ha preso <b>ventotto</b> (su trenta, vedi LA REALTÀ ITALIANA). Chiedere: <i>È un buon voto?</i></li></ol>""")

    # Page 3
    rules = [("<i>Ho cominciato <b>a</b> studiare. · Prova <b>a</b> respirare.</i> Dopo <i>cominciare</i> e <i>provare</i> c'è", ["a", "di"], "a"),
             ("<i>Non ho finito <b>di</b> ripassare. · Smetti <b>di</b> preoccuparti.</i> Dopo <i>finire</i> e <i>smettere</i> c'è", ["di", "a"], "di"),
             ("Dopo la preposizione il verbo è", ["all'infinito", "coniugato"], "all'infinito"),
             ("<i>Ho deciso <b>di</b> non bere.</i> La negazione va", ["prima dell'infinito", "prima di decidere"], "prima dell'infinito"),
             ("Dopo <i>volere, potere, dovere</i>", ["non c'è preposizione", "c'è di"], "non c'è preposizione"),
             ("I verbi con <i>a</i> o <i>di</i>", ["si imparano a memoria", "seguono una regola fissa"], "si imparano a memoria")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Ho imparato", ["a", "di"], "a", "nuotare da bambina."), ("Ricordati", ["di", "a"], "di", "chiamare la mamma!"),
          ("Voglio", ["–", "di"], "–", "dormire fino a mezzogiorno."), ("Ho cercato", ["di", "a"], "di", "studiare, ma c'era troppo rumore.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: verbi + a / di + infinito", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Ho cominciato <b>a</b> studiare a maggio. · Non riesco <b>a</b> dormire. · Chiara ti ha aiutato <b>a</b> ripassare. · Prova <b>a</b> respirare. · Ho continuato <b>a</b> parlare.<br>
2. Non ho finito <b>di</b> ripassare. · Smetti <b>di</b> preoccuparti! · Ho paura <b>di</b> dimenticare. · Ho deciso <b>di</b> non bere il caffè. · Ricordati <b>di</b> portare il documento. · Ho dimenticato <b>di</b> dire una data. · Ha promesso <b>di</b> smettere.<br>
3. Non posso dormire. · Voglio festeggiare. · Devi studiare.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "A, di o niente (–)? Scegli.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>+ a</b>: cominciare, continuare, provare, aiutare, imparare, riuscire. <b>+ di</b>: finire, smettere, decidere, dimenticare, ricordarsi, promettere, cercare, avere paura, sperare. <b>Niente</b>: dovere, potere, volere, sapere, preferire. Poi sempre l'<b>infinito</b>. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: proporre un aiuto: verbi di <b>inizio</b> → <i>a</i>; verbi di <b>fine</b> e di <b>testa</b> (decidere, ricordarsi, dimenticare) → <i>di</i>. Non è una regola sicura.</li>
<li>C: frase 4: <i>cercare di</i> = <i>provare a</i> (stesso significato, preposizione diversa!).</li></ol>""")

    grammar_ref_it.verbi_preposizione(b)

    # Page 5
    ans3 = ["a", "di", "a", "di", "di", "a"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho deciso partire domani.</td><td><b>Ho deciso di partire domani.</b></td><td><i>decidere di</i>.</td></tr>
<tr><td>Ho smesso fumare.</td><td><b>Ho smesso di fumare.</b></td><td><i>smettere di</i> (= parar de).</td></tr>
<tr><td>Voglio di dormire.</td><td><b>Voglio dormire.</b></td><td>Modali: niente preposizione.</td></tr>
<tr><td>Prova di respirare.</td><td><b>Prova a respirare.</b></td><td><i>provare a</i> (ma <i>cercare di</i>).</td></tr>
<tr><td>Non riesco dormire.</td><td><b>Non riesco a dormire.</b></td><td><i>riuscire a</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["20.2", "20.3"])}
{sub("A", "Ascolta e ripeti. Dopo a la consonante si sente doppia: a presto [apprèsto], a casa [akkàsa], a studiare.", "2 min", "20.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S202)}</div>
{sub("B", "A o di? Ascolta e scegli.", "2 min", "20.3")}
{twocol([f'<li value="{i+1}">{ch(["a", "di"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>provare a</i> e <i>cercare di</i> vogliono dire la stessa cosa: buon esempio del perché bisogna impararli a memoria.</li>
<li>4A: è il <i>raddoppiamento sintattico</i>: dopo <i>a, e, da, che, tre, è, più</i> la consonante si allunga (<i>a Roma</i> = [arròma]). Nel Nord Italia si sente meno: accettare le due pronunce.</li></ol>""")

    # Page 6
    fl = [("Ho finito ___ lavorare alle sei.", "di"), ("Mi aiuti ___ portare la valigia?", "a"), ("Devo ___ studiare stasera.", "–"),
          ("Cerco ___ dormire otto ore.", "di"), ("Ho imparato ___ cucinare la pasta.", "a"), ("Preferisco ___ restare a casa.", "–")]
    fll = [f'<li value="{i+1}">{s.replace("___", A(a, "min-width:9mm"))}</li>' for i, (s, a) in enumerate(fl)]
    pr = [("decidere / studiare ogni giorno", "Ho deciso di studiare ogni giorno."), ("smettere / giocare ai videogiochi", "Ho smesso di giocare ai videogiochi."),
          ("cominciare / andare in biblioteca", "Ho cominciato ad andare in biblioteca."), ("promettere / non dormire in biblioteca", "Ho promesso di non dormire in biblioteca.")]
    prl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in pr)
    wb = [("studiare", "lo studio"), ("ripassare", "il ripasso"), ("laurearsi", "la laurea"), ("promettere", "la promessa")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "A, di o niente (–)? Completa.", "3 min")}
{twocol(fll, 4)}
{sub("B", "I propositi di Bruno per l'estate. Scrivi le frasi al passato prossimo (io).", "4 min")}
<ol style="line-height:1.45">{prl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>B: frase 3: davanti a vocale <i>a</i> diventa spesso <b>ad</b> (<i>ad andare</i>). Frase 4: <i>dormire in biblioteca</i> ricorda l'unità 03.</li>
<li>C: <i>il ripasso</i> come nei nostri <i>Ripassi</i>. <i>Laurearsi</i>: Bruno lo farà fra tre anni!</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Calma un amico agitato. L'insegnante ha un esame (o un colloquio, un volo, un appuntamento) domani ed è agitatissimo. Dagli consigli e fai domande. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Smetti di preoccuparti! · Prova a… · Cerca di… · Ricordati di… · Non dimenticare di… · Hai finito di…? · Quando hai cominciato a…? · Ce la fai! · In bocca al lupo! — Crepi!</div>
{sub("B", "I miei propositi. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Che cosa hai cominciato a fare quest'anno?</li><li>Che cosa hai smesso di fare? Che cosa vuoi smettere di fare?</li><li>Che cosa vuoi imparare a fare?</li><li>Che cosa hai deciso di fare quest'estate?</li><li>Che cosa dimentichi sempre di fare?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: insegnare <i>In bocca al lupo!</i> — <i>Crepi!</i> (si dice prima di un esame; non si risponde <i>grazie</i>).</li>
<li>B: pretendere la preposizione giusta in ogni risposta; scrivere alla lavagna i verbi sbagliati e farli correggere alla fine.</li></ol>""")

    # Page 8
    pc = [("A2 · 18", "So scrivere una mail formale e informale con i connettivi."), ("A2 · 20", "So parlare di studio ed esami."),
          ("A2 · 20", "So usare i verbi + a (cominciare a, provare a)."), ("A2 · 20", "So usare i verbi + di (finire di, decidere di)."),
          ("A2 · 20", "So incoraggiare una persona agitata.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ho deciso partire.", "Ho deciso di partire."), ("Ho cominciato a studiare a maggio.", "✓"),
          ("Voglio di dormire.", "Voglio dormire."), ("Non riesco dormire.", "Non riesco a dormire."),
          ("Prova di respirare.", "Prova a respirare."), ("Ricordati di portare il documento.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. I miei propositi per l'estate (50–75 parole).</b> Che cosa hai deciso di fare? Che cosa vuoi smettere di fare? Che cosa vuoi imparare a fare? Che cosa prometti di fare? Usa almeno quattro verbi con <i>a</i> o <i>di</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge i propositi; l'insegnante chiede <i>Ci riuscirai?</i> Unità 21: <i>Prima di partire</i> (prima di + infinito).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("20.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("20.2", "Ascolta e ripeti")}
<p>{" · ".join(S202)}</p>
{sub("20.3", "A o di?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S203))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 20 - Il primo esame")
