# Speak! Progresso B1 - Unità 02 "Me lo dai?" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 02", audio_json=os.path.join(HERE, "audio_it-b1-unita-02.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-02"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["02.1 Me lo dai?"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S022 = [x.split(": ", 1)[1] for x in _r["02.2 Ripeti"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    # Pagina 1 - Riscaldamento
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 02", "Me lo dai?", "Favori tra amici · <b>i pronomi combinati</b>",
                       [("SAI FARE", "chiedere, accettare e rifiutare un favore; parlare di oggetti prestati senza ripetere i nomi"),
                        ("LINGUA", "Me la presti? · Te lo tengo io. · Portaglielo tu. · Gliele ho date. · Ce ne dai un po'?"),
                        ("PRONUNCIA", "l'accento non si sposta: TRATtamela, PORtaglielo")])
    kw = [("dare una cosa che poi torna indietro", "prestare"), ("dare l'acqua alle piante", "annaffiare"),
          ("dare indietro una cosa a chi la possiede", "restituire"), ("andare a prendere un pacco o la posta", "ritirare"),
          ("la ruota della bici senza aria", "una gomma a terra"), ("promettere in modo solenne", "giurare"),
          ("usare un'occasione favorevole", "approfittare"), ("andare con qualcuno in un posto", "accompagnare")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: un favore", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Quando parti, a chi lasci le chiavi di casa? Perché proprio a quella persona?</li><li>Qual è l'ultimo favore che hai chiesto? E l'ultimo che hai fatto?</li><li>Che cosa presti facilmente? Che cosa non presti mai?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">accompagnare · annaffiare · approfittare · giurare · prestare · restituire · ritirare · una gomma a terra</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Ti hanno mai restituito una cosa rotta o sporca? Che cosa hai detto?", "1 min")}""",
    25, """<ol><li>A: conversazione libera; annotare gli errori per la pagina 8. Se lo studente dice <i>presto a lui</i> senza oggetto, non correggere ancora: è il tema della lezione.</li>
<li>B: <i>prestare</i> = <i>emprestar</i> (dare); <i>chiedere in prestito</i> = <i>pedir emprestado</i>. <i>Restituire</i> = <i>devolver</i> (non <i>ritornare</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione sui favori · parole chiave del dialogo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Me lo dai? Júlia parte per Milano e tutti chiedono qualcosa</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>I pronomi combinati: me lo, glielo, ce ne, dammelo</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>I pronomi combinati (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Prestare e restituire · scelta delle parole · l'accento con i pronomi</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>I messaggi tra Júlia e Davide · rispondere con i pronomi</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Chiedere e rifiutare un favore · monologo · gioco di ruolo</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Giovedì 14 gennaio, sera. Júlia parte la mattina dopo per Milano con Marco: tre giorni di lavoro da un cliente. A casa sua ci sono Davide, Bruno e Camila, e ognuno ha un favore da chiedere o da fare. Davide le annaffia le piante, tiene le chiavi e ritirerà un pacco di libri; porterà alla signora Rossi il libro di ricette brasiliane che Júlia le aveva promesso a Natale. Bruno si fa prestare la bici (l'ultima volta l'aveva riportata con una gomma a terra). Camila chiede il vestito nero lungo per la cena di sabato con Pietro; prenderà le chiavi da Davide. Júlia regala ai ragazzi un pacchetto del caffè che Camila le ha portato da Recife. Alla fine Bruno promette di accompagnarla alla stazione… finché scopre che il treno è alle 6:40.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese parlato l'oggetto si omette (<i>Me empresta? — Empresto.</i>) o si usa il pronome tonico (<i>dou pra ele</i>): lo studente dice <i>mi presti?</i>, <i>do a lui</i> e evita i pronomi combinati. Inoltre scrive <i>gli lo</i> separato, dimentica il raddoppio in <i>dammelo</i> e accorda il participio con l'indiretto. Obiettivo dell'unità: usare in modo naturale <i>me lo, te lo, glielo</i> e le forme attaccate all'imperativo.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In molti condomini italiani è normale lasciare una copia delle chiavi a un vicino di fiducia. I favori tra vicini sono una forma di scambio: chi riceve un favore di solito ricambia con un piccolo regalo (un dolce, una bottiglia di vino) e dice <i>Ti devo un favore!</i>. Da Bologna a Milano in Frecciarossa ci vuole circa un'ora: per questo molti professionisti fanno avanti e indietro in giornata.</div>
<div class="box"><h4>AUDIO</h4>Traccia 02.1 Me lo dai? (prima naturale, poi lenta) · Traccia 02.2 Ripeti: l'accento con i pronomi</div>""")

    # Pagina 2 - Ascolto
    gi = [("le piante di Júlia", True), ("un viaggio a Recife", False), ("una bicicletta", True), ("un vestito", True), ("un esame di Davide", False), ("un libro di ricette", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Davide deve annaffiare le piante ogni giorno.", "F"), ("Júlia aspetta un pacco con dei libri.", "V"),
          ("Bruno vuole la bici perché l'autobus è sempre pieno.", "V"), ("Camila prende le chiavi da Júlia sabato.", "F"),
          ("Júlia aveva promesso il libro alla signora Rossi.", "V"), ("Bruno accompagna volentieri Júlia alla stazione.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Me lo dai?", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["02.1 · NATURAL", "02.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Giovedì sera, a casa di Júlia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "02.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Júlia dice a Bruno: «Trattamela bene!». Perché? {R("L'ultima volta lui gliel'aveva riportata con una gomma a terra.") if T else ""}</li>
<li>Alla fine Bruno dice: «Forse è meglio se te la porta Davide». Che cosa vuol dire, davvero? {R("Che non ha voglia di alzarsi così presto: è uno scherzo.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Ti posso chiedere un favore? · Figurati! Dimmi. · Non c'è problema. · Già che ci siamo… · Tanto… · Allora approfitto anch'io. · Sei un tesoro! · Guarda che…</i></div>""",
    27, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: le piante, la bici, il vestito, il libro di ricette.</li>
<li>B: 1 basta una volta, sabato · 4 le prende da Davide · 6 scopre che il treno è alle 6:40 e cambia idea.</li>
<li>Espressioni: <i>già che ci siamo</i> = <i>já que estamos nisso</i>; <i>tanto</i> = <i>de qualquer jeito</i>; <i>guarda che…</i> introduce un avvertimento.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Te le do subito.", "te = a Davide · le = le chiavi"), ("Me la presti?", "me = a Bruno · la = la bici"),
          ("Gliele ho appena date.", "glie = a Davide · le = le chiavi"), ("Portaglielo tu.", "glie = alla signora · lo = il libro"),
          ("Ve ne do un pacchetto.", "ve = a voi · ne = del caffè")]
    exl = "".join(f"<li><i>{s}</i> {A(a, 'min-width:58mm')}</li>" for s, a in ex)
    rules = [("Il pronome indiretto va", ["prima", "dopo"], "prima", "del diretto."),
             ("<i>Mi, ti, ci, vi</i> diventano", ["me, te, ce, ve", "mi, ti, ci, vi"], "me, te, ce, ve", ": <i>me lo, ce ne</i>."),
             ("<i>Gli, le</i> e <i>Le</i> diventano <i>glie-</i> e si scrive tutto", ["attaccato", "separato"], "attaccato", ": <i>glielo</i>."),
             ("Con l'imperativo (tu) e l'infinito i pronomi vanno", ["dopo, attaccati", "prima, separati"], "dopo, attaccati", ": <i>portaglielo</i>."),
             ("Al passato prossimo il participio si accorda con il pronome", ["diretto", "indiretto"], "diretto", ": <i>gliele ho date</i>.")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".") for a, o, r, z in rules)
    cc = [("Il libro? Davide", ["gli l'ha portato", "gliel'ha portato"], "gliel'ha portato", "stamattina."),
          ("Ti piace il mio vestito?", ["Te lo presto!", "Ti lo presto!"], "Te lo presto!", ""),
          ("Le foto della festa?", ["Mandamele", "Mandami le"], "Mandamele", "stasera, per favore!")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" </li>", "</li>") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: i pronomi combinati", "8 min")}
{sub("A", "Frasi dal dialogo. A chi? Che cosa? Scrivi che cosa sostituisce ogni pronome.", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la forma giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>indiretto + diretto</b> (o <b>ne</b>): <i>mi, ti, ci, vi</i> → <b>me, te, ce, ve</b> + <i>lo, la, li, le, ne</i>; <i>gli, le, Le</i> → <b>glielo, gliela, glieli, gliele, gliene</b>. Prima del verbo coniugato; <b>dopo e attaccati</b> all'infinito e all'imperativo (<i>portaglielo, dammelo</i>). Al passato: <i>me <b>l'</b>ha data, gliel<b>e</b> ho dat<b>e</b></i>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: per ogni frase chiedere <i>a chi?</i> e <i>che cosa?</i>; scrivere alla lavagna <i>mi + lo → me lo</i>. Far notare che <i>glie-</i> vale per Davide (lui) e per la signora Rossi (lei).</li>
<li>C: 3 <i>Mandamele</i>: con <i>tu</i> l'imperativo prende i pronomi attaccati. Chiedere allo studente la versione negativa: <i>Non mandarmele! / Non me le mandare!</i></li></ol>""")

    grammar_ref_it.pronomi_combinati_b1(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["fare", "dare una", "chiedere in prestito", "tenere d'occhio", "accompagnare", "restituire"]
    rgt = ["la casa di un vicino", "un favore a qualcuno", "i soldi entro venerdì", "mano a un amico", "qualcuno alla stazione", "la bici a un'amica"]
    ans = {"fare": "un favore a qualcuno", "dare una": "mano a un amico", "chiedere in prestito": "la bici a un'amica",
           "tenere d'occhio": "la casa di un vicino", "accompagnare": "qualcuno alla stazione", "restituire": "i soldi entro venerdì"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: prestare e restituire", "4 min")}
{sub("A", "Unisci le due parti delle espressioni.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante. Usa i pronomi quando puoi.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Presti i tuoi libri? Te li restituiscono?</li><li>Chi ti dà una mano quando hai un problema?</li><li>Hai mai chiesto in prestito una macchina?</li><li>Chi tiene d'occhio la tua casa quando parti?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho prestato la bici da Júlia.</td><td><b>Júlia mi ha prestato la bici.</b></td><td><i>prestare</i> = solo dare; chi riceve <i>chiede in prestito</i>.</td></tr>
<tr><td>Quando mi ritorni la bici?</td><td><b>Quando me la restituisci / riporti?</b></td><td><i>ritornare</i> = <i>voltar</i>, non <i>devolver</i>.</td></tr>
<tr><td>Lo do per te.</td><td><b>Te lo do.</b></td><td><i>pra você</i> = <i>a te</i> → pronome <i>te</i>.</td></tr>
<tr><td>Mi presti? — Sì, presto.</td><td><b>Me la presti? — Sì, te la presto.</b></td><td>in italiano il pronome diretto non si omette.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: l'accento con i pronomi", "4 min")}
<p class="small" style="margin:.3mm 0">Quando attacchiamo i pronomi, l'accento <b>non si sposta</b>: <i><b>TRAT</b>ta → <b>TRAT</b>tamela · <b>POR</b>ta → <b>POR</b>taglielo</i>. Attenzione al suono <b>gl</b> (come <i>lh</i> in <i>filho</i>): <i>glielo, gliele</i>.</p>
{audiocard(["02.2"])}
{sub("A", "Ascolta e ripeti. Poi chiedi tre oggetti all'insegnante, che ti risponde con i pronomi.", "4 min", "02.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S022))}</p>""",
    29, """<ol><li>A: fare 1 b · dare una d · chiedere in prestito f · tenere d'occhio a · accompagnare e · restituire c. <i>Tenere d'occhio</i> = <i>ficar de olho</i> (uguale!).</li>
<li>Pronuncia: battere il ritmo sul tavolo: la sillaba forte è la stessa del verbo da solo. Gioco finale: <i>Mi presti la penna? — Te la presto. — Me la ridai? — Te la ridò.</i></li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["me lo tieni", "me la tieni"], "me lo tieni"), (["gliel'hai portato", "gli l'hai portato"], "gliel'hai portato"),
          (["daglielo", "dalle lo"], "daglielo"), (["prendetene", "prendetelo"], "prendetene"),
          (["te le ho annaffiate", "te li ho annaffiati"], "te le ho annaffiate"), (["te l'ho messo", "te la ho messa"], "te l'ho messo"),
          (["gliel'ho dato", "gliele ho dato"], "gliel'ho dato"), (["me l'ha riportata", "me l'ha riportato"], "me l'ha riportata")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Mi presti la penna?", "Sì, te la presto."), ("Hai dato le chiavi a Davide?", "Sì, gliele ho date."),
          ("Puoi spiegare la regola a Camila?", "Sì, posso spiegargliela. / Gliela posso spiegare."), ("Ci porti il dolce stasera?", "Sì, ve lo porto."),
          ("Mi dai due biglietti?", "Sì, te ne do due."), ("Hai restituito la bici a Júlia?", "No, non gliel'ho ancora restituita.")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:52mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Sabato Júlia scrive a Davide da Milano, e lui risponde. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Júlia:</b> Ciao Davide! Qui a Milano tutto bene, la presentazione è andata benissimo. Il pacco è arrivato? Se sì, {p[0]} fino a domenica? E il libro di ricette: {p[1]} alla signora Rossi? Camila passa da te oggi per le chiavi: se ti chiede anche il caricabatterie del telefono, è sul mio comodino, {p[2]} pure. Ah, il caffè: Camila me ne ha portati tre pacchetti, {p[3]} un altro voi, se volete!<br>
<b>Davide:</b> Tutto a posto! Le piante? {p[4]} stamattina. Il pacco è arrivato ieri: {p[5]} sul tavolo della cucina. Il libro? {p[6]} venerdì mattina: era contentissima. E Bruno? Non me ne parlare… La bici ce l'ha ancora, ma ieri sera ha detto che domenica {p[7]} pulita. Vedremo!</div>
{sub("B", "Rispondi alle domande con i pronomi combinati.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0;column-count:2">{dxl}</ol>""",
    26, """<ol><li>A: per ogni scelta chiedere <i>a chi? che cosa?</i> Gap 3: <i>daglielo</i> (a lei, a Camila; imperativo tu → attaccato). Gap 4: <i>prendetene</i> (ne = di quei pacchetti). Gap 5–8: accordo del participio con il diretto (<i>le piante → annaffiate, la bici → riportata</i>). Ultima frase: Davide usa il futuro nel discorso riportato informale.</li>
<li>B: accettare le due posizioni con i verbi modali. Poi lo studente fa le domande all'insegnante.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: favori e risposte", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>chiedere</th><th>accettare</th><th>rifiutare con gentilezza</th><th>ringraziare</th></tr>
<tr><td><i>Ti posso chiedere un favore? · Mi faresti un favore? · Ti dispiace se…? · Me lo presti?</i></td><td><i>Certo! · Figurati! · Ci penso io. · Te lo do volentieri.</i></td><td><i>Mi dispiace, ma… · Vorrei, però… · Questa volta non posso. · Non è che non voglio, è che…</i></td><td><i>Grazie, sei un tesoro! · Ti devo un favore. · Non so come ringraziarti.</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi parla per due minuti del favore più grande che hai fatto o ricevuto.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>chi te l'ha chiesto o a chi l'hai chiesto</li><li>che cosa era successo prima</li><li>com'è andata e com'è finita</li><li>come avete ringraziato</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. L'insegnante è un vicino che parte per un mese e ti chiede molti favori. Accettane alcuni e rifiutane uno con gentilezza. Usa i pronomi!", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Mi annaffi le piante? · Mi tieni il gatto? · Mi ritiri la posta? · Me la porti al quarto piano? (la valigia) · Mi presti la tua macchina per il viaggio? · Mi dai il tuo numero, per le emergenze? Lo studente risponde: Te le annaffio io · Mi dispiace, ma non te la posso prestare…") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Presti soldi agli amici? Perché sì o perché no?</li><li>È facile per te dire di no a un favore?</li><li>In Brasile e in Italia si chiedono favori ai vicini allo stesso modo?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto pronomi omessi (<i>l'ho prestato</i> → <i>gliel'ho prestato</i>). Opzione fluidità (3-2-1): lo stesso racconto in 2 minuti, poi in 1 minuto.</li>
<li>B: le richieste dell'insegnante sono in rosso; insistere perché lo studente non ripeta i nomi degli oggetti. Il rifiuto deve avere un motivo: <i>Mi dispiace, ma la uso per andare al lavoro.</i></li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare i pronomi combinati (me lo, glielo, ce ne, dammelo).",
          "So chiedere, accettare e rifiutare un favore con gentilezza."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Istruzioni per un amico.</b> Parti per una settimana e un amico ti tiene la casa. Scrivigli un biglietto: che cosa deve fare, dove trova le cose, come lo ringrazi. Prima leggi il biglietto di Júlia.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Caro Davide, grazie ancora! Ti lascio qualche istruzione. Le piante: annaffiale sabato, ma non troppo; quella grande vicino alla finestra ha sempre sete, dagliene un bicchiere in più. Se trovi lettere nella cassetta, mettimele sul tavolo. Il pacco con i libri: se arriva, tienimelo tu fino a domenica. Sabato passa Camila per il vestito nero: è nell'armadio della camera, daglielo pure. In frigo c'è un formaggio che scade venerdì: mangialo tu, te lo regalo! Le chiavi riportamele domenica sera, quando torno. Da Milano ti porto qualcosa di buono, promesso. Ti devo un favore! Un abbraccio, Júlia</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno cinque pronomi combinati &nbsp;☐ due imperativi con i pronomi attaccati (<i>dammelo, portaglielo</i>) &nbsp;☐ un passato prossimo con accordo (<i>gliel'ho data</i>) &nbsp;☐ un'espressione per ringraziare &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi. Il registro continua in tutte le unità del B1.</li>
<li>C: il modello è il biglietto che Júlia ha lasciato a Davide giovedì sera. Correggere soprattutto la posizione dei pronomi e l'accordo. Prossima unità: <i>Avrei dovuto…</i> (il condizionale passato).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("02.1", "Me lo dai? (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "Ripeti: l'accento con i pronomi")}
<p>{" · ".join(S022)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 02 - Me lo dai?")
