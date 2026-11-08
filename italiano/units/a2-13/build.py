# Speak! Ponte A2 - Unità 13 "Che tipo sei?" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 13", audio_json=os.path.join(HERE, "audio_it-a2-unita-13.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "timido", "timido"), ("B", "socievole", "socievole"), ("C", "pigro", "pigro"), ("D", "sportivo", "sportivo"),
          ("E", "disordinato", "disordinato"), ("F", "ordinato", "ordinato"), ("G", "curioso", "curioso"), ("H", "tranquillo", "tranquillo")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-13"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["13.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S132 = [x.split(": ", 1)[1] for x in _r["13.2 Ripeti"].split("\n")]
S133 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["13.3 Dettato"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 13", "Che tipo sei?", "Il carattere · <b>bravo quanto · così… come · -issimo · meglio / migliore</b>",
                       [("SAI FARE", "descrivere il carattere, paragonare due persone, scegliere la persona o la cosa migliore"),
                        ("LINGUA", "Elena è brava quanto Tommaso. · È la più disordinata del palazzo. · Gentilissima! · Parla meglio di lui."),
                        ("PRONUNCIA", "-issimo: bellissimo, simpaticissimo, lunghissimo")])
    words = sorted(w for _, w, _ in PHOTOS)
    b.page(f"""{sec(1, "Riscaldamento: il carattere", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi l'aggettivo sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali di questi aggettivi sono veri per te? E quali no?</li><li>Com'è il tuo migliore amico o la tua migliore amica?</li><li>Qual è il contrario di <i>timido</i>, <i>pigro</i>, <i>ordinato</i>?</li></ol>""",
    24, """<ol><li>A: ricordare il femminile: <i>timida, pigra, sportiva</i>; <i>socievole</i> non cambia (-e).</li>
<li>B: domanda 3: <i>socievole / estroverso, attivo / sportivo, disordinato</i>. Lo studente farà paragoni spontanei: annotarli per pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: aggettivi del carattere</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il test di Giulia · lo stagista · il regalo per Chiara</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>quanto / come · il più… di · -issimo · meglio / migliore</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Comparativi · superlativi · forme speciali</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>-issimo · dettato</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Paragoni · meglio o migliore? · -issimo</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Il test «Che tipo sei?» · io e una persona della mia famiglia</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio maggio. Al bar Giulia fa il test di una rivista, «Che tipo sei?»: Davide dice di essere socievolissimo e pazientissimo, ma Júlia ricorda che ieri ha aspettato l'autobus due minuti e poi ha preso un taxi. Il risultato: energico e curioso, ma non così paziente come pensa. Allo studio Marco e Júlia scelgono uno stagista per il progetto del giardino (i lavori cominciano a maggio): Tommaso ha più esperienza, ma Elena è brava quanto lui, ha disegni migliori, parla inglese meglio ed è gentilissima. Prendono Elena. La sera Bruno chiede a Júlia un consiglio per il compleanno di Chiara (sabato): un libro della sua scrittrice preferita e una cena.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese <i>melhor</i> e <i>pior</i> sono sia aggettivi sia avverbi; in italiano c'è <b>migliore</b> (aggettivo: <i>il regalo migliore</i>) e <b>meglio</b> (avverbio: <i>parla meglio</i>). Errori tipici: <i>parla inglese migliore</i>, <i>più alto que me</i> (→ <b>di</b> me), <i>il più migliore</i>, <i>molto bellissimo</i>. Attenzione anche a <i>simpaticissimo</i> (senza <i>h</i>) ma <i>ricchissimo, lunghissimo</i> (con <i>h</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Gli italiani usano tantissimo il superlativo in <b>-issimo</b>, anche in situazioni normali: <i>Grazie mille! Gentilissimo!</i>, <i>Buonissimo!</i>, <i>Carissimi amici…</i> In Italia lo <b>stage</b> (o tirocinio) è il primo lavoro di molti giovani dopo l'università, spesso di sei mesi.</div>
<div class="box"><h4>AUDIO</h4>Traccia 13.1 Tre dialoghi (lento e naturale) · Traccia 13.2 Ascolta e ripeti · Traccia 13.3 Dettato</div>""")

    # Page 2
    st = [("Come si descrive Davide?", "socievolissimo e pazientissimo"), ("Perché Júlia non è d'accordo?", "ha aspettato l'autobus due minuti e ha preso un taxi"),
          ("Qual è il risultato del test?", "energico e curioso, ma non così paziente come pensa")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    who = [("ha più esperienza", "Tommaso"), ("ha i disegni migliori", "Elena"), ("parla inglese meglio", "Elena"), ("sembra un po' arrogante", "Tommaso"),
           ("è gentilissima e precisa", "Elena")]
    wl = "".join(f"<tr><td>{s}</td><td style='width:42mm;text-align:center'>{ch(['Elena', 'Tommaso'], w)}</td></tr>" for s, w in who)
    b.page(f"""{sec(2, "Ascolto: che tipo sei?", "10 min")}
<p>Al bar Giulia fa un test, allo studio Marco e Júlia devono scegliere uno stagista e Bruno ha bisogno di un consiglio.</p>
{audiocard(["13.1 · SLOW", "13.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "13.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Elena o Tommaso?", "4 min", "13.1 · NATURAL")}
<table style="margin:0">{wl}</table>
{sub("C", "Dialogo 3. Che cosa regala Bruno a Chiara? Perché?", "3 min")}
<div class="wline">{R("Un libro della sua scrittrice preferita (Chiara è timida e legge tantissimo) e una cena.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Far notare l'ironia: <i>pazientissimo?</i> e <i>Questo test è sbagliatissimo!</i></li>
<li>B: versione <b>naturale</b>. Chiedere: <i>E tu, chi prendi? Perché?</i> C: <i>invitala</i> = imperativo + pronome (unità 04).</li></ol>""")

    # Page 3
    rules = [("<i>Elena è brava quanto Tommaso.</i> Vuol dire che sono", ["bravi uguale", "uno più bravo dell'altro"], "bravi uguale"),
             ("Per l'uguaglianza usiamo", ["(tanto)… quanto / (così)… come", "più… di"], "(tanto)… quanto / (così)… come"),
             ("<i>La più disordinata del palazzo</i>: il secondo termine si introduce con", ["di (del, della…)", "che"], "di (del, della…)"),
             ("<i>Bellissimo, gentilissima</i> vogliono dire", ["molto bello, molto gentile", "più bello di tutti"], "molto bello, molto gentile"),
             ("<i>Il regalo migliore</i>: <i>migliore</i> va con", ["un nome (= più buono)", "un verbo"], "un nome (= più buono)"),
             ("<i>Parla inglese meglio di lui</i>: <i>meglio</i> va con", ["un verbo (= più bene)", "un nome"], "un verbo (= più bene)")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Chiara è più timida", ["di", "che"], "di", "Bruno."), ("Questa pizza è", ["migliore", "meglio"], "migliore", "di quella."),
          ("Oggi sto", ["meglio", "migliore"], "meglio", "di ieri."), ("Davide non è così paziente", ["come", "di"], "come", "pensa.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: paragoni e superlativi", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Elena è brava <b>quanto</b> Tommaso. · Sono <b>tanto</b> ordinato <b>quanto</b> disordinato. · Non sei <b>così</b> paziente <b>come</b> pensi.<br>
2. La tua stanza è <b>la più</b> disordinata <b>del</b> palazzo. · Sei la sorella <b>migliore del</b> mondo!<br>
3. socievol<b>issimo</b> · pazient<b>issimo</b> · bell<b>issimi</b> · gentil<b>issima</b> · brav<b>issima</b><br>
4. I disegni di Elena sono <b>migliori</b>. · Parla inglese <b>meglio</b> di lui. · Un libro è <b>meglio</b> di un profumo. · La stanza di Bruno è <b>peggiore</b> della mia.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
{twocol([f'<li value="{i+1}">' + x[4:] for i, x in enumerate(ccl.split('</li>')[:-1])], 3)}
<div class="box sand"><h4>REGOLA</h4>Uguaglianza: <b>(tanto)… quanto</b>, <b>(così)… come</b>. Superlativo relativo: <b>il / la più… di</b>. Superlativo assoluto: <b>-issimo</b> (= molto). <b>migliore / peggiore</b> + nome (= più buono / più cattivo); <b>meglio / peggio</b> + verbo (= più bene / più male). Tutto: pagina 4.</div>""",
    22, """<ol><li>B: per <i>meglio / migliore</i> usare la prova: si può dire <i>più buono</i>? → <i>migliore</i>. Si può dire <i>più bene</i>? → <i>meglio</i>.</li>
<li>C: <i>più… di</i> davanti a un nome o un pronome (<i>di Bruno, di me</i>); <i>che</i> solo tra due verbi o due aggettivi (unità 01).</li></ol>""")

    grammar_ref_it.comparativi_superlativi(b)

    # Page 5
    dl = [f'<li value="{i+1}">{A(w, "min-width:30mm")}</li>' for i, w in enumerate(["bellissima", "simpaticissimi", "pigrissimo", "gentilissime", "lunghissimo", "ricchissimo"])]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Bruno è più alto que me.</td><td><b>Bruno è più alto di me.</b></td><td><i>più… di</i>.</td></tr>
<tr><td>Elena parla inglese migliore.</td><td><b>Elena parla inglese meglio.</b></td><td>Con un verbo: <i>meglio</i>.</td></tr>
<tr><td>È il più migliore.</td><td><b>È il migliore.</b></td><td><i>migliore</i> = già <i>più buono</i>.</td></tr>
<tr><td>È molto bellissima.</td><td><b>È bellissima.</b></td><td><i>-issimo</i> = già <i>molto</i>.</td></tr>
<tr><td>È tanto brava come Tommaso.</td><td><b>È brava quanto Tommaso.</b></td><td><i>tanto… quanto</i>, <i>così… come</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["13.2", "13.3"])}
{sub("A", "Ascolta e ripeti. L'accento è sempre su -ìssimo, con la doppia s.", "2 min", "13.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S132)}</div>
{sub("B", "Dettato. Ascolta e scrivi l'aggettivo in -issimo.", "2 min", "13.3")}
{twocol(dl, 4)}""",
    28, """<ol><li>Errori: <i>que</i> (port. <i>que</i>) è l'errore più frequente nei paragoni: in italiano <i>di</i>.</li>
<li>4B: controllare l'ortografia: <i>simpaticissimi</i> (senza <i>h</i>), <i>lunghissimo, ricchissimo</i> (con <i>h</i>), e l'accordo (<i>gentilissime</i>).</li></ol>""")

    # Page 6
    pg = [("Davide / Bruno (+ socievole)", "Davide è più socievole di Bruno."), ("Elena / Tommaso (= brava)", "Elena è brava quanto Tommaso."),
          ("Chiara / Bruno (– sportiva)", "Chiara è meno sportiva di Bruno."), ("la stanza di Davide / del palazzo (+ disordinata)", "È la più disordinata del palazzo.")]
    pgl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in pg)
    mm = [("I tortellini di Giulia sono i ___ di Bologna.", "migliori"), ("Bruno nuota ___ di Júlia.", "meglio"), ("Questo caffè è ___ di quello.", "peggiore"),
          ("Oggi Marco sta ___: ha la febbre.", "peggio")]
    mml = "".join(f"<li>{s.replace('___', A(a, 'min-width:18mm'))}</li>" for s, a in mm)
    iss = [("Il film era molto bello.", "bellissimo"), ("Elena è molto gentile.", "gentilissima"), ("I cicchetti erano molto buoni.", "buonissimi"),
           ("Il viaggio è stato molto lungo.", "lunghissimo")]
    isl = [f'<li value="{i+1}">{s} → {A(a, "min-width:24mm")}</li>' for i, (s, a) in enumerate(iss)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Fai il paragone.", "3 min")}
<ol style="line-height:1.45">{pgl}</ol>
{sub("B", "Meglio, migliore, peggio o peggiore?", "3 min")}
<ol style="line-height:1.7">{mml}</ol>
{sub("C", "Molto → -issimo.", "3 min")}
{twocol(isl, 3)}""",
    22, """<ol><li>A: l'ordine è <i>più + aggettivo + di</i> (non <i>socievole più di</i>).</li>
<li>B: frase 1: <i>i migliori di Bologna</i> = superlativo relativo con <i>di</i>. C: <i>lunghissimo</i> con la <i>h</i>.</li></ol>""")

    # Page 7
    qz = ["Il sabato sera: a casa o fuori?", "Ordinato/a o disordinato/a?", "Paziente o impaziente?", "Sportivo/a o pigro/a?", "Il tuo regalo migliore?", "La cosa che fai meglio?"]
    qzl = "".join(f'<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>{i+1}.</b> {t}</div>' for i, t in enumerate(qz))
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Il test «Che tipo sei?». Fai le domande all'insegnante, poi rispondi tu. Alla fine scrivete il risultato dell'altro: Sei un tipo… ma non sei così… come pensi!", "6 min")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;margin-top:1mm">{qzl}</div>
<div class="wline"></div>
{sub("B", "Io e una persona della mia famiglia. Paragona te stesso/a con un fratello, una sorella o un genitore: chi è più…? Chi fa meglio…? Siete… quanto…?", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>più… di · meno… di · … quanto… · non così… come · il / la più… della famiglia · -issimo · meglio / peggio · migliore / peggiore · invece · tutti e due</div>""",
    22, """<ol><li>A: l'insegnante risponde con ironia e qualche paragone (<i>Sono ordinata quanto un gatto!</i>) per dare il modello.</li>
<li>B: lo studente può mostrare una foto di famiglia. Correggere soprattutto <i>que → di</i> e <i>migliore / meglio</i>.</li></ol>""")

    # Page 8
    pc = [("A2 · 12", "So usare volevo / ho voluto e ne con le quantità."), ("A2 · 13", "So descrivere il carattere di una persona."),
          ("A2 · 13", "So fare paragoni: più… di, quanto, così… come."), ("A2 · 13", "So usare il superlativo: il più… di, -issimo."),
          ("A2 · 13", "So scegliere tra meglio e migliore.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Marco è più alto que Luca.", "più alto di Luca"), ("Elena parla meglio di Tommaso.", "✓"),
          ("È la ragazza più simpatica della classe.", "✓"), ("Questo è il più migliore ristorante.", "il ristorante migliore"),
          ("Il film è molto bellissimo.", "bellissimo"), ("Giulia cucina migliore di me.", "cucina meglio di me")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Il mio migliore amico / La mia migliore amica (50–75 parole).</b> Com'è? In che cosa siete uguali e in che cosa diversi? Che cosa fa meglio di te? Usa <i>più… di, quanto, -issimo, meglio / migliore</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge la descrizione; l'insegnante fa domande di paragone. Unità 14: <i>La spesa sostenibile</i> (ne partitivo, ci locativo).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("13.1", "Che tipo sei? (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("13.2", "Ascolta e ripeti")}
<p>{" · ".join(S132)}</p>
{sub("13.3", "Dettato")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S133))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 13 - Che tipo sei")
