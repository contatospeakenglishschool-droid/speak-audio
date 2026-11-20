# Speak! Progresso B1 - Ripasso 2 (Unità 11-19), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Progresso"
setup(band="B1 · RIPASSO 2", audio_json=os.path.join(HERE, "audio_it-b1-ripasso-2.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "lo spritz", "Unità 12"), ("B", "la focaccia", "Unità 13"), ("C", "la schedina", "Unità 14"), ("D", "il tabellone", "Unità 15"),
          ("E", "l'edicola", "Unità 16"), ("F", "le tagliatelle", "Unità 17"), ("G", "il dolce", "Unità 18"), ("H", "la montagna", "Unità 19")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-ripasso-2"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S13 = lines("R2.1 Conversazione"), lines("R2.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R2.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Pagina 1
    cover = cover_html(T, "LIVELLO B1 · RIPASSO 2", "Ripasso 2", "Unità 11–19 · il secondo blocco del B1",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 11–19"),
                        ("LINGUA", "come se · pensavo che fosse · magari · se vincessi · gerundio · passivo · benché · mi chiedo se · ha detto che sarebbe"),
                        ("PRONUNCIA", "dettato di frasi · allo studio e al bar")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la grammatica di quell'unità.", "5 min")}
<div class="bank">il dolce · l'edicola · la focaccia · la montagna · la schedina · lo spritz · il tabellone · le tagliatelle</div>
{photo_grid(T, PHOTOS)}""",
    30, """<p>Le foto A–H vengono dalle unità 12–19, in ordine (l'unità 11 torna nell'ascolto e nella grammatica). Esempi: <i>Pensavo che lo spritz fosse dolce (12). Magari ci fosse ancora un po' di focaccia! (13) Se vincessi, comprerei… (14) Guardando il tabellone, ho visto il ritardo (15). Il giornale si compra in edicola (16). Benché siano pesanti, le tagliatelle mi piacciono (17). Non so se il dolce le piacerà (18). Pietro ha detto che sarebbero andati in montagna (19).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>12–19</td><td>1</td></tr>
<tr><td>2 Ascolto: le novità di fine maggio</td><td>12 min</td><td>11–19</td><td>2</td></tr>
<tr><td>3 Grammatica: congiuntivo imperfetto, concordanza, desideri, periodo ipotetico</td><td>10 min</td><td>11–14</td><td>3</td></tr>
<tr><td>4 Grammatica: gerundio, passivo, concessive, interrogative indirette, discorso indiretto</td><td>12 min</td><td>15–19</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>11–19</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>9 min</td><td>11–19</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>11–19</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano, anche quelli dei compiti delle unità 11–19. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 3 dell'unità.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Marzo: videochiamata con i genitori, che annunciano la visita (11); il primo aperitivo serale e gli stereotipi (12); il picnic di primavera e i desideri (13); Davide e la schedina mai giocata (14). Aprile: arrivano Lúcia e Roberto (15); Júlia sul giornale per la biblioteca della Bolognina (16); il pranzo dalla signora Rossi (17); Chiara conosce i genitori di Bruno (18). Maggio: i genitori sono tornati in Brasile, la visita in montagna di Camila è rimandata, Elena lascia il bar (19). Oggi, lunedì 31 maggio: Júlia non sa se tornare in Brasile a Natale, lo studio ha tre nuovi clienti, Camila va in montagna con Pietro il 12 giugno e Giulia cerca un barista per l'estate: forse il cugino di Pietro.</div>
<div class="box"><h4>I 6 ERRORI DA CONTROLLARE</h4>1. <i>Se vincerei</i> → <b>Se vincessi</b> 2. <i>Pensavo che è</i> → <b>Pensavo che fosse</b> 3. <i>Benché è</i> → <b>Benché sia</b> 4. <i>Ha detto che verrebbe</i> → <b>sarebbe venuto</b> 5. <i>Non so cosa che dire</i> → <b>Non so che cosa dire</b> 6. <i>È venuta rinnovata</i> → <b>È stata rinnovata</b></div>
<div class="box"><h4>AUDIO</h4>Traccia R2.1 Conversazione (naturale e lenta) · Traccia R2.2 Dettato di frasi · Traccia R2.3 Due dialoghi</div>""")

    # Pagina 2
    topics = [("la videochiamata con i genitori", True), ("il Natale in Brasile", True), ("i nuovi clienti dello studio", True), ("il tirocinio di Camila", True),
              ("la montagna con Pietro", True), ("la partenza di Elena", True), ("un barista per l'estate", True), ("il compleanno di Davide", False)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Ieri sera Júlia ha parlato con i genitori fino a mezzanotte.", "V"), ("Júlia ha già deciso di tornare in Brasile per Natale.", "F: non lo sa ancora."),
          ("Dopo l'articolo, lo studio ha tre nuovi clienti.", "V"), ("Il tirocinio di Camila finisce a settembre.", "F: finisce a luglio."),
          ("Camila e Pietro vanno in montagna il 12 giugno.", "V"), ("La madre di Pietro sta ancora male.", "F: sta bene."),
          ("Davide aiuterà Giulia al bar a giugno.", "F: ha gli esami."), ("Camila chiederà a Pietro se conosce qualcuno.", "V")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: le novità di fine maggio", "12 min")}
<p>Lunedì 31 maggio, mattina. Al bar di Giulia, Júlia, Camila e Davide fanno colazione.</p>
{audiocard(["R2.1 · NATURAL", "R2.1 · SLOW"])}
{sub("A", "Ascolta la versione naturale. Di che cosa parlano? Segna (✓) sette argomenti. Un argomento è in più.", "3 min", "R2.1 · NATURAL")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "4 min")}
<table style="table-layout:fixed"><tr><td>come se / concordanza (11–12)</td><td>{R("come se fossimo ancora insieme · sperava che io tornassi · pensavo che fosse una scusa")}</td></tr>
<tr><td>magari / periodo ipotetico (13–14)</td><td>{R("Magari mi offrissero un contratto! · Se fossi il tuo capo, te lo offrirei.")}</td></tr>
<tr><td>gerundio (15)</td><td>{R("Guardando gli annunci, …")}</td></tr>
<tr><td>passivo (16)</td><td>{R("lo studio è stato contattato da tre nuovi clienti")}</td></tr>
<tr><td>concessiva / indiretta (17–18)</td><td>{R("Benché tu abbia tanto lavoro… · Mi chiedo se sia il momento giusto.")}</td></tr>
<tr><td>discorso indiretto (19)</td><td>{R("Ha detto che guardava tutte le partite…")}</td></tr></table>""",
    24, """<p>A: argomento in più = <span class="red">il compleanno di Davide</span>. B: lo studente corregge a voce. C: accettare anche <i>Se non avessi gli esami, ti aiuterei</i> (14) e <i>Te l'avevo detto</i> (pronomi combinati, B1 02).</p>""")

    # Pagina 3
    ci = [("Mia madre parla come se (essere) ___ ancora qui.", ["fosse"]), ("Mi guardava come se non (capire) ___ niente.", ["capisse"]),
          ("Era stanco, come se non (dormire) ___ da giorni.", ["dormisse"])]
    cil = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in ci)
    cc = [("Pensavo che l'aperitivo ", ["fosse", "sia"], "fosse", " solo vino."), ("Oggi penso che Bologna ", ["sia", "fosse"], "sia", " la mia città."),
          ("Credevo ", ["di essere", "che fossi"], "di essere", " in ritardo.")]
    ccl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cc)
    mg = [("Vorrei che tu (venire) ___ con noi.", ["venissi"]), ("Magari (fare) ___ sempre così bello!", ["facesse"]), ("Vorrei (avere) ___ più ferie.", ["avere"])]
    mgl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in mg)
    pi = [("Se ", ["avessi", "avrei"], "avessi", " tempo, viaggerei."), ("Se vinco stasera, ", ["ti offro", "ti offrissi"], "ti offro", " la cena."),
          ("Se fossi in te, non ", ["giocherei", "giocassi"], "giocherei", "."), ("Che cosa ", ["faresti", "facessi"], "faresti", " se potessi?")]
    pil = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in pi)
    b.page(f"""{sec(3, "Grammatica: unità 11–14", "10 min")}
<div class="two"><div>{sub("A", "Unità 11. Come se + congiuntivo imperfetto.", "2 min")}<ol>{cil}</ol></div>
<div>{sub("B", "Unità 12. La concordanza dei tempi. Scegli.", "2 min")}<ol>{ccl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 13. Vorrei che, magari.", "3 min")}<ol>{mgl}</ol></div>
<div>{sub("D", "Unità 14. Il periodo ipotetico. Scegli.", "3 min")}<ol>{pil}</ol></div></div>""",
    26, """<ol><li>A: <i>come se</i> vuole sempre il congiuntivo imperfetto (o trapassato). B: verbo principale al passato → congiuntivo imperfetto; stesso soggetto → <i>di</i> + infinito.</li>
<li>C: <i>vorrei</i> + infinito con lo stesso soggetto. D: tipo 1 (probabile) → presente; tipo 2 → <i>se</i> + congiuntivo imperfetto + condizionale; mai il condizionale dopo <i>se</i>.</li></ol>""")

    # Pagina 4
    gr = [("(Pulire) ___ la casa, ho rotto un bicchiere.", ["Pulendo"]), ("(Avere) ___ dormito poco, sono stanca.", ["Avendo"]), ("Ho visto Marco e, (vedere) ___, l'ho salutato.", ["vedendolo"])]
    grl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in gr)
    ps = [("La biblioteca (rinnovare) ___ l'anno scorso.", ["è stata rinnovata"]), ("I libri (prestare) ___ anche con un'app.", ["vengono prestati"]),
          ("In edicola (vendersi) ___ i giornali.", ["si vendono"])]
    psl = "".join(f"<li>{fill(s, a, '26mm')}</li>" for s, a in ps)
    cs = [("Benché ", ["piova", "piove"], "piova", ", usciamo."), ("Anche se ", ["sono", "sia"], "sono", " stanca, vengo.")]
    csl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cs)
    ii = [("«Dove abiti?» → Mi ha chiesto dove ___.", ["abitavo"]), ("«Verrò domani.» → Ha detto che ___ il giorno dopo.", ["sarebbe venuto/a"]),
          ("«Chiamami!» → Mi ha chiesto ___.", ["di chiamarlo/a"])]
    iil = "".join(f"<li>{fill(s, a, '22mm')}</li>" for s, a in ii)
    mk = [("Se vincerei, comprerei una casa.", "Se vincessi, comprerei una casa."), ("Pensavo che è timida.", "Pensavo che fosse timida."),
          ("Benché è tardi, restiamo.", "Benché sia tardi, restiamo."), ("La biblioteca è venuta rinnovata.", "La biblioteca è stata rinnovata."),
          ("Non so cosa che dire.", "Non so che cosa dire."), ("Ha detto che verrebbe.", "Ha detto che sarebbe venuto.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 15–19", "12 min")}
<div class="two"><div>{sub("A", "Unità 15. Il gerundio.", "2 min")}<ol>{grl}</ol>{sub("B", "Unità 16. Il passivo e il si passivante.", "2 min")}<ol>{psl}</ol></div>
<div>{sub("C", "Unità 17. Benché o anche se? Scegli.", "1 min")}<ol>{csl}</ol>{sub("D", "Unità 18 e 19. Riferisci.", "3 min")}<ol>{iil}</ol></div></div>
{sub("E", "Unità 11–19. Correggi gli errori.", "3 min")}
<ol style="column-count:2">{mkl}</ol>""",
    26, """<ol><li>A: stesso soggetto; pronomi attaccati (<i>vedendolo</i>). B: <i>venire</i> solo nei tempi semplici; il si concorda con la cosa. C: <i>benché</i> + congiuntivo, <i>anche se</i> + indicativo.</li>
<li>D: verbo al passato → i tempi vanno indietro; ordini → <i>di</i> + infinito. E: chiedere allo studente quale unità ripassa ogni frase (14, 12, 17, 16, 18, 19).</li></ol>""")

    # Pagina 5
    cats = [("Viaggi e aeroporto", "il tabellone · atterrare · la dogana · gli arrivi"), ("Giornali e libri", "l'edicola · una copia · pubblicare · i racconti"),
            ("La famiglia", "un nipote · la coppia · il fidanzato · uscire di casa"), ("Giochi e sogni", "la schedina · l'estrazione · la tabaccheria · un sognatore")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("atterrare", "l'atterraggio"), ("pubblicare", "la pubblicazione"), ("inaugurare", "l'inaugurazione"), ("promettere", "la promessa"),
          ("accogliere", "l'accoglienza"), ("presentare", "la presentazione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    md = [("Lo vorresti tanto:", "Magari!"), ("Sei molto, molto stanco:", "Sono stanco morto."), ("Non dirlo a nessuno:", "Acqua in bocca!"),
          ("Hai fatto un errore e hai imparato:", "Sbagliando s'impara.")]
    mdl = "".join(f"<li>{a} {A(x, 'min-width:30mm')}</li>" for a, x in md)
    od = [("benché · sebbene · nonostante · anche se", "anche se (+ indicativo)"), ("edicola · tabaccheria · libreria · dogana", "dogana (non è un negozio)"),
          ("nipote · fidanzato · coppia · tabellone", "tabellone (non è famiglia)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 11–19. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">gli arrivi · atterrare · la coppia · una copia · la dogana · l'edicola · l'estrazione · il fidanzato · un nipote · pubblicare · i racconti · la schedina · un sognatore · il tabellone · la tabaccheria · uscire di casa</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}
<div class="two"><div>{sub("C", "Unità 13, 15 e 19. Che cosa dici?", "1 min")}<ol>{mdl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>A e B: parole dalle unità 14–18. C: espressioni delle unità 13, 15 e 19. D: chiedere sempre perché.</p>""")

    # Pagina 6
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Marco", "Júlia, hai letto la mail del nuovo cliente?", ""), ("Júlia", "Sì. Vuole sapere se possiamo cominciare a luglio. Benché c'è tanto lavoro, direi di sì.", "ci sia"),
          ("Marco", "D'accordo. Gli ho già scritto che gli manderemmo il progetto entro fine giugno.", "avremmo mandato"),
          ("Júlia", "Perfetto. Se avrei più tempo, lo farei da sola… ma ho bisogno di te!", "avessi")]
    d2 = [("Giulia", "Camila, Pietro conosce qualcuno per il bar?", ""), ("Camila", "Sì, mi ha detto che suo cugino cercherebbe un lavoro per l'estate.", "cercava"),
          ("Giulia", "Magari sa fare il cappuccino!", "sapesse"), ("Camila", "Gliel'ho chiesto: ha lavorato in un bar a Riccione.", ""),
          ("Giulia", "Perfetto. Digli che passa domani mattina!", "di passare")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "9 min")}
{audiocard(["R2.2", "R2.3"])}
{sub("A", "Unità 11–19. Dettato. Ascolta e scrivi le frasi.", "4 min", "R2.2")}
<ol style="line-height:1.25;column-count:1">{dal}</ol>
{sub("B", "Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R2.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 1: allo studio</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 2: al bar</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un altro cliente, un altro lavoro.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase; ogni frase ripassa un'unità, dalla 11 alla 19, in ordine.</li>
<li>B: dialogo 1: <i>benché</i> + congiuntivo (17), futuro nel passato (19), periodo ipotetico (14). Dialogo 2: discorso indiretto (19), <i>magari</i> + congiuntivo imperfetto (13), <i>dire di</i> + infinito (19). L'audio ha le versioni corrette.</li></ol>""")

    # Pagina 7
    cd = [("11", "So usare il congiuntivo imperfetto e come se."), ("12", "So raccontare prime impressioni (pensavo che fosse…)."),
          ("13", "So esprimere desideri con vorrei che e magari."), ("14", "So fare ipotesi e dare consigli (se fossi in te…)."),
          ("15", "So usare il gerundio per dire quando, come e perché."), ("16", "So raccontare una notizia con il passivo."),
          ("17", "So ammettere un'idea e difendere la mia (benché, anche se)."), ("18", "So esprimere dubbi e fare domande gentili."),
          ("19", "So riferire quello che altri hanno detto.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Rileggi le correzioni dei tuoi compiti: quali errori fai ancora? Scrivi due cose da migliorare.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p><b>La mia primavera.</b> Scrivi una mail a un amico italiano e raccontagli gli ultimi tre mesi:</p>
<ol style="line-height:1.4"><li>una persona che hai conosciuto e che cosa pensavi di lei all'inizio (<i>pensavo che…</i>);</li><li>una notizia che ti hanno dato (<i>mi ha detto che sarebbe…</i>);</li><li>un desiderio (<i>magari…</i>) e un'ipotesi (<i>se potessi…</i>);</li><li>una difficoltà superata (<i>benché…</i>) e un dubbio per l'estate (<i>mi chiedo se…</i>).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare con lo studente le righe «Non ancora» e decidere che cosa ripassare (pagina 3 dell'unità corrispondente). Prossima unità: <b>B1 21, Il lavoro che cambia</b> (i pronomi relativi <i>il quale, il cui</i>), inizio del terzo blocco.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R2.1", "Le novità di fine maggio (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R2.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R2.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 20 - Ripasso 2")
