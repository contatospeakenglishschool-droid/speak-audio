# Speak! Ponte A2 - Unità 24 "Il mio quartiere" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 24", audio_json=os.path.join(HERE, "audio_it-a2-unita-24.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il quartiere", "quartiere"), ("B", "il cortile", "cortile"), ("C", "i vicini", "vicini"), ("D", "la saracinesca", "saracinesca"),
          ("E", "la tavolata", "tavolata"), ("F", "l'anguria", "anguria"), ("G", "le lasagne", "lasagne"), ("H", "la strada vuota", "strada")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-24"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["24.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S242 = [x.split(": ", 1)[1] for x in _r["24.2 Ripeti"].split("\n")]
S243 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["24.3 Si o no"].split("\n")]


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
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 24", "Il mio quartiere", "I vicini e il quartiere · <b>qualche · qualcuno · qualcosa · ogni · ognuno · nessuno · niente</b>",
                       [("SAI FARE", "parlare del quartiere e dei vicini, organizzare una festa in cui ognuno porta qualcosa, dire che non c'è nessuno o niente"),
                        ("LINGUA", "Non c'è nessuno. · Ogni negozio è chiuso. · Ognuno porta qualcosa. · Porto qualche birra. · Non ho niente da fare."),
                        ("PRONUNCIA", "l'accento: qualcùno, nessùno, ognùno, qualcòsa")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: il quartiere", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Com'è il tuo quartiere? Che negozi ci sono?</li><li>Conosci i tuoi vicini? Parli con loro?</li><li>Nel tuo palazzo o nella tua via si fanno feste insieme?</li></ol>""",
    28, """<ol><li>A: <i>la saracinesca</i> = la chiusura di metallo dei negozi; <i>la tavolata</i> = un tavolo lungo con tante persone; <i>l'anguria</i> (anche <i>il cocomero</i> in Toscana e a Roma).</li>
<li>B: domanda 2: se lo studente non conosce i vicini, aspettare <i>Non conosco nessuno</i>: primo contatto con la lingua dell'unità.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il quartiere</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La vigilia di Ferragosto · il pranzo in cortile</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Gli indefiniti</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Con un nome · da soli · doppia negazione</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'accento degli indefiniti · sì o no?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Completa · rispondi di no · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Organizziamo una festa · il mio quartiere</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>14 agosto, vigilia di Ferragosto. Il quartiere è vuoto: <i>non c'è nessuno</i>, <i>ogni negozio</i> ha il cartello "chiuso per ferie", anche il bar di Giulia. Nel palazzo è rimasto <i>qualcuno</i>: la signora Rossi, Júlia, il signor Neri del terzo piano (voce generica, personaggio di una sola unità) e Briciola; Franco è al mare con la figlia. La signora Rossi organizza un pranzo in cortile: <i>ognuno porta qualcosa</i> (lei le lasagne, Júlia qualche dolce brasiliano). Bruno <i>non ha niente da fare</i> (Chiara è dai genitori) e porta qualche birra. Il signor Neri porta un'anguria; Bruno mangia tre porzioni di lasagne. <i>Nessuno le fa così.</i> Decidono di rifarlo ogni anno.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>La doppia negazione è come in portoghese (<i>não tem ninguém</i> → <b>non c'è nessuno</b>). Gli errori: il plurale dopo <i>qualche</i> (pensano ad <i>alguns</i>: <i>qualche birre</i> → <b>qualche birra</b>) e dopo <i>ogni</i> (pensano a <i>todos</i>: <i>ogni negozi</i> → <b>ogni negozio</b>), e <i>non</i> dopo <i>nessuno</i> all'inizio: <i>nessuno non viene</i> → <b>nessuno viene</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il <b>15 agosto</b> (Ferragosto) è festa nazionale. Molti italiani sono in ferie nelle due settimane centrali di agosto: tanti negozi chiudono con il cartello <b>"chiuso per ferie"</b> e le città si svuotano. Chi resta fa grigliate, pranzi in cortile o va al fiume; la sera spesso ci sono fuochi d'artificio. Nei palazzi italiani il rapporto con i vicini è importante: ci si saluta sulle scale e ci si aiuta (chiavi, piante, posta).</div>
<div class="box"><h4>AUDIO</h4>Traccia 24.1 I due dialoghi (lento e naturale) · Traccia 24.2 Ascolta e ripeti · Traccia 24.3 Sì o no?</div>""")

    # Page 2
    p1 = [("Nel quartiere non c'è", "nessuno"), ("Ogni negozio ha il cartello", "\"chiuso per ferie\""), ("Nel palazzo è rimasto il signor Neri del", "terzo piano"),
          ("Al pranzo in cortile ognuno porta", "qualcosa"), ("La signora Rossi fa", "le lasagne")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:42mm')}</td></tr>" for a, x in p1)
    vf = [("Bruno domani ha molte cose da fare.", "F"), ("Nel frigo di Bruno non c'è niente.", "V"), ("Bruno porta qualche birra.", "V"),
          ("Il signor Neri porta un dolce.", "F"), ("Bruno mangia tre porzioni di lasagne.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Ferragosto in cortile", "10 min")}
{audiocard(["24.1 · SLOW", "24.1 · NATURAL"])}
{sub("A", "Prima parte. Il 14 agosto, nel cortile. Completa.", "4 min", "24.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. La telefonata e il pranzo. Vero (V) o falso (F)?", "4 min", "24.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa decidono alla fine?", "2 min")}
<div class="wline">{R("Di rifare il pranzo di Ferragosto ogni anno.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. <i>La vigilia</i> = il giorno prima di una festa (la vigilia di Natale, unità 05).</li>
<li>B: frase 4: il signor Neri porta un'<b>anguria</b>; il dolce lo porta Júlia.</li></ol>""")

    # Page 3
    rules = [("<i>Ogni negozio <b>è</b> chiuso.</i> Dopo <i>ogni</i> il nome è", ["singolare", "plurale"], "singolare"),
             ("<i>Porto <b>qualche</b> birra.</i> <i>Qualche</i> vuol dire", ["alcune", "una"], "alcune"),
             ("<i>C'è <b>qualcuno</b>. · Porta <b>qualcosa</b>.</i> <i>Qualcuno</i> è una persona, <i>qualcosa</i> è", ["una cosa", "un posto"], "una cosa"),
             ("<i><b>Non</b> c'è <b>nessuno</b>. · <b>Non</b> ho <b>niente</b>.</i> Quando <i>nessuno</i> e <i>niente</i> sono dopo il verbo, c'è anche", ["non", "no"], "non"),
             ("<i><b>Nessuno</b> le fa così.</i> Quando <i>nessuno</i> è all'inizio, <i>non</i>", ["non si usa", "si usa"], "non si usa"),
             ("<i><b>Ognuno</b> porta qualcosa.</i> <i>Ognuno</i> vuol dire", ["ogni persona", "nessuna persona"], "ogni persona")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Ho comprato qualche", ["dolce", "dolci"], "dolce", "brasiliano."), ("", ["Ogni", "Ognuno"], "Ogni", "estate andiamo al mare."),
          ("Non ho visto", ["nessuno", "qualcuno"], "nessuno", "sulle scale."), ("C'è", ["qualcosa", "qualcuno"], "qualcosa", "da mangiare?")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: gli indefiniti", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Ogni</b> anno la città si svuota. · <b>Ogni</b> negozio ha il cartello. · Posso fare <b>qualche</b> dolce. · Porto <b>qualche</b> birra.<br>
2. C'è ancora <b>qualcuno</b>. · <b>Qualcuno</b> vuole ancora lasagne? · <b>Ognuno</b> porta <b>qualcosa</b>. · Porta <b>qualcosa</b> da bere.<br>
3. <b>Non</b> c'è <b>nessuno</b>. · <b>Non</b> ho <b>niente</b> da fare. · Nel frigo <b>non</b> c'è <b>niente</b>. · <b>Nessuno</b> le fa così.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>ogni</b> e <b>qualche</b> + nome <b>singolare</b>. <b>qualcuno</b> (persona), <b>qualcosa</b> (cosa), <b>ognuno</b> (ogni persona). Dopo il verbo: <b>non</b> + verbo + <b>nessuno / niente</b>; all'inizio: <b>Nessuno</b> viene (senza <i>non</i>). Tutto: pagina 4.</div>""",
    22, """<ol><li>B: regola 2: <i>qualche birra</i> = <i>alcune birre</i>: scrivere le due frasi alla lavagna; il significato è plurale, la forma singolare.</li>
<li>C: frase 4: <i>qualcosa da mangiare / da bere / da fare</i>: struttura molto utile.</li></ol>""")

    grammar_ref_it.indefiniti(b)

    # Page 5
    ans3 = ["sì", "no", "sì", "no", "no", "sì"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Porto qualche birre.</td><td><b>Porto qualche birra.</b></td><td><i>qualche</i> + singolare.</td></tr>
<tr><td>Ogni negozi sono chiusi.</td><td><b>Ogni negozio è chiuso.</b></td><td><i>ogni</i> + singolare.</td></tr>
<tr><td>C'è nessuno.</td><td><b>Non c'è nessuno.</b></td><td>Doppia negazione.</td></tr>
<tr><td>Nessuno non viene.</td><td><b>Nessuno viene.</b></td><td>All'inizio: senza <i>non</i>.</td></tr>
<tr><td>Ognuno portano qualcosa.</td><td><b>Ognuno porta qualcosa.</b></td><td><i>ognuno</i> + verbo singolare.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["24.2", "24.3"])}
{sub("A", "Ascolta e ripeti. L'accento è sulla penultima sillaba: qualcùno, nessùno, ognùno, qualcòsa.", "2 min", "24.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S242)}</div>
{sub("B", "Sì o no? Ascolta: c'è qualcuno o qualcosa (sì) o non c'è (no)? Scegli.", "2 min", "24.3")}
{twocol([f'<li value="{i+1}">{ch(["sì", "no"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>ognuno</i> è singolare come <i>cada um</i>: <i>ognuno <b>porta</b></i>.</li>
<li>4A: <i>niente</i> e <i>nessuno</i> si pronunciano con la <i>e</i> chiusa; non dire <i>nada</i>!</li>
<li>4B: numero 5: <i>ogni negozio è chiuso</i> = non c'è niente aperto → <b>no</b>.</li></ol>""")

    # Page 6
    fl = [("C'è ___ in casa? Sento una voce.", "qualcuno"), ("Vuoi ___ da bere?", "qualcosa"), ("___ giorno vado al lavoro in bici.", "Ogni"),
          ("Ho letto ___ libro quest'estate.", "qualche"), ("___ porta un piatto alla festa.", "Ognuno"), ("Non ho capito ___.", "niente")]
    fll = [f'<li value="{i+1}">{s.replace("___", A(a, "min-width:18mm"))}</li>' for i, (s, a) in enumerate(fl)]
    ng = [("C'è qualcuno al bar?", "No, non c'è nessuno."), ("Hai mangiato qualcosa?", "No, non ho mangiato niente."),
          ("Hai visto qualche vicino?", "No, non ho visto nessun vicino."), ("Qualcuno ha chiamato?", "No, nessuno ha chiamato.")]
    ngl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in ng)
    wb = [("abitare", "l'abitante"), ("pranzare", "il pranzo"), ("salutare", "il saluto"), ("aiutare", "l'aiuto")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Completa con qualcuno, qualcosa, qualche, ogni, ognuno, niente.", "3 min")}
{twocol(fll, 4)}
{sub("B", "Rispondi di no.", "4 min")}
<ol style="line-height:1.45">{ngl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 1: <i>sento una voce</i> → persona → <i>qualcuno</i>. Frase 4: <i>qualche libro</i> = alcuni libri.</li>
<li>B: frase 3: <i>nessun vicino</i> (come <i>un</i>: <i>nessun</i> + maschile). Frase 4: <i>nessuno</i> all'inizio, senza <i>non</i>.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Organizziamo una festa! Tu e l'insegnante organizzate una festa per i vicini del palazzo. Decidete quando, dove e che cosa porta ognuno. Chi invitate? C'è qualcuno che non può venire?", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Ognuno porta… · Io porto qualche… · Qualcuno può portare…? · Non c'è niente da bere! · Non conosco nessuno al secondo piano. · Ogni vicino… · Chi porta qualcosa da mangiare?</div>
{sub("B", "Il mio quartiere. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>C'è qualcosa che ti piace molto nel tuo quartiere?</li><li>C'è qualcosa che non ti piace?</li><li>Conosci qualcuno nel tuo palazzo? Chi?</li><li>Che cosa fai ogni domenica nel quartiere?</li><li>Nella tua città d'estate le persone vanno via? Dove?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: l'insegnante può fare il vicino che si lamenta di tutto (come la signora Rossi in primavera) per provocare <i>nessuno, niente</i>.</li>
<li>B: domanda 5: confrontare con le ferie brasiliane (dicembre-gennaio, Carnevale).</li></ol>""")

    # Page 8
    pc = [("A2 · 23", "So esprimere entusiasmo con che…!, quanto…!, com'è…!"), ("A2 · 24", "So parlare del mio quartiere e dei vicini."),
          ("A2 · 24", "So usare qualche, ogni + nome singolare."), ("A2 · 24", "So usare qualcuno, qualcosa, ognuno."),
          ("A2 · 24", "So dire non c'è nessuno / non ho niente.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Porto qualche birre.", "Porto qualche birra."), ("Non c'è nessuno al bar.", "✓"),
          ("Ogni negozi sono chiusi.", "Ogni negozio è chiuso."), ("C'è niente nel frigo.", "Non c'è niente nel frigo."),
          ("Nessuno non è venuto.", "Nessuno è venuto."), ("Ognuno porta qualcosa.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Il mio quartiere (50–75 parole).</b> Dove abiti? Che cosa c'è nel quartiere? Conosci qualcuno? Che cosa fai ogni settimana? C'è qualcosa che manca? Usa almeno quattro indefiniti.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il testo; l'insegnante chiede <i>Conosci qualcuno che…?</i> Unità 25: <i>Me lo presti?</i> (pronomi combinati, ricettivo).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("24.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("24.2", "Ascolta e ripeti")}
<p>{" · ".join(S242)}</p>
{sub("24.3", "Sì o no?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S243))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 24 - Il mio quartiere")
