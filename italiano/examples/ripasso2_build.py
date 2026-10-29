# Speak! Essenziale A1 - Ripasso 2 (Unità 10-17), tutto in italiano - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · RIPASSO 2", audio_json=os.path.join(HERE, "audio_it-a1-ripasso-2.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il mercato", "Unità 10"), ("B", "il ponte", "Unità 11"), ("C", "il ragù", "Unità 12"), ("D", "svegliarsi", "Unità 13"),
          ("E", "i nonni", "Unità 14"), ("F", "il divano", "Unità 15"), ("G", "il binario", "Unità 16"), ("H", "la neve", "Unità 17")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-ripasso-2"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S23 = lines("R2.1 Conversazione"), lines("R2.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R2.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec

    # Page 1: cover + photo memory
    cover = cover_html(T, "LIVELLO A1 · RIPASSO 2", "Ripasso 2", "Unità 10–17 · la spesa · il passato · la cucina · la famiglia · la casa · il treno · il tempo",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 10–17 e decidere che cosa ripassare"),
                        ("LINGUA", "del, della · passato prossimo · lo, la, ne · mi alzo · mio padre · c'è / ci sono · partire da · fa freddo"),
                        ("PRONUNCIA", "ore, date e quantità · al mercato e alla stazione")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la parola.", "5 min")}
<div class="bank">il binario · il divano · il mercato · il ponte · il ragù · i nonni · la neve · svegliarsi</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Esempio:</b> il ragù → <i>Il ragù si cuoce per tre ore.</i></p>""",
    22, """<p>Le foto A–H vengono dalle unità 10–17, in ordine. Accettare qualsiasi frase corretta: <i>Al mercato compro la frutta. Sabato scorso sono andato sul ponte. Mi sveglio alle sette. I miei nonni abitano a Recife. Il treno parte dal binario 6. In inverno nevica.</i> Correggere il passato prossimo e i possessivi.</p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>10–17</td><td>1</td></tr>
<tr><td>2 Ascolto: Júlia e Giulia al bar</td><td>10 min</td><td>10–17</td><td>2</td></tr>
<tr><td>3 Grammatica: partitivo, dovere/sapere, passato prossimo, pronomi, riflessivi</td><td>10 min</td><td>10–13</td><td>3</td></tr>
<tr><td>4 Grammatica: possessivi, c'è / ci sono, luogo, viaggio, tempo</td><td>10 min</td><td>14–17</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>10–17</td><td>5</td></tr>
<tr><td>6 Pronuncia e italiano sociale</td><td>8 min</td><td>10, 16, 17</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>10–17</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Febbraio. Domani arriva Bruno, il fratello di Júlia. Al bar Júlia racconta a Giulia i programmi: il treno da Milano (unità 16), la spesa al Mercato delle Erbe (10), il ragù (12), la camera nella casa nuova (15), le abitudini di Bruno (13), il pranzo dalla famiglia di Marco (14), le previsioni del tempo (17) e il viaggio a Firenze con i genitori a dicembre (11).</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>Ho andato</i> → <b>Sono andato/a</b> 2. <i>Il mio padre</i> → <b>Mio padre</b> 3. <i>Compro lo</i> → <b>Lo compro</b> 4. <i>Io alzo alle sette</i> → <b>Mi alzo alle sette</b> 5. <i>È freddo</i> → <b>Fa freddo</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia R2.1 Conversazione (lenta e naturale) · Traccia R2.2 Dettato di ore, date e numeri · Traccia R2.3 Due dialoghi</div>""")

    # Page 2: listening
    topics = [("un viaggio in treno", True), ("la spesa", True), ("una ricetta", True), ("la casa", True), ("il lavoro allo studio", False),
              ("le abitudini di Bruno", True), ("un pranzo in famiglia", True), ("il tempo", True), ("un viaggio passato", True)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Bruno arriva in aereo.", "F: arriva in treno da Milano."), ("Il treno arriva alle 10:20.", "V"), ("Júlia deve comprare un chilo di parmigiano.", "F: mezzo chilo."),
          ("Il ragù si cuoce per tre ore.", "V"), ("La camera di Bruno è accanto alla cucina.", "F: è accanto al bagno."), ("Bruno si sveglia presto.", "F: si sveglia tardi."),
          ("Domenica piove e fa freddo.", "V"), ("A dicembre Júlia e i genitori sono andati a Firenze.", "V")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: Júlia e Giulia al bar", "10 min")}
<p>È febbraio. Domani arriva Bruno, il fratello di Júlia. Al bar Júlia e Giulia parlano dei programmi… e degli ultimi mesi.</p>
{audiocard(["R2.1 · SLOW", "R2.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) otto argomenti. Un argomento è in più.", "3 min", "R2.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R2.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>partitivo / quantità</td><td>{R("del prosciutto · mezzo chilo di parmigiano")}</td></tr><tr><td>lo / si impersonale</td><td>{R("lo so fare · si cuoce per tre ore")}</td></tr>
<tr><td>verbo riflessivo</td><td>{R("si sveglia · si addormenta · mi alzo")}</td></tr><tr><td>passato prossimo</td><td>{R("ha comprato · sono venuti · siamo andati · abbiamo mangiato")}</td></tr></table>""",
    18, """<p>A: argomento in più = <span class="red">il lavoro allo studio</span>. B: lo studente corregge a voce le frasi false. C: se serve, lo studente può leggere la trascrizione nell'ultima pagina della guida.</p>""")

    # Page 3: grammar 10-13
    ds = [("io", "devo", "so"), ("tu", "devi", "sai"), ("lui / lei / Lei", "deve", "sa")]
    dsr = "".join(f"<tr><td>{p}</td><td>{A(a, 'min-width:16mm')}</td><td>{A(c, 'min-width:16mm')}</td></tr>" for p, a, c in ds)
    pt = [("pane", "del"), ("acqua", "dell'"), ("zucchero", "dello"), ("frutta", "della")]
    ptl = "".join(f"<li>Vorrei {A(x, 'min-width:12mm')} {n}.</li>" for n, x in pt)
    pp = [("Sabato io", "sono andato/a", "a Firenze.", "andare"), ("Noi", "abbiamo mangiato", "la bistecca.", "mangiare"), ("Davide", "è tornato", "alle tre.", "tornare"),
          ("Tu che cosa", "hai fatto", "ieri?", "fare")]
    ppl = [f'<li value="{i+1}">{a} {A(v, "min-width:30mm")} {c} <span class="small">({n})</span></li>' for i, (a, v, c, n) in enumerate(pp)]
    pr = [("Il parmigiano?", "Lo", "compro al mercato."), ("Le carote?", "Le", "taglio a pezzi."), ("Quante uova?", "Ne", "compro sei."), ("La cipolla?", "La", "metto nella pentola.")]
    prl = "".join(f"<li>{a} {A(x, 'min-width:10mm')} {c}</li>" for a, x, c in pr)
    rf = [("Io", "mi sveglio", "alle sette.", "svegliarsi"), ("Tu a che ora", "ti alzi", "?", "alzarsi"), ("Giulia", "si riposa", "il pomeriggio.", "riposarsi")]
    rfl = "".join(f'<li>{a} {A(v, "min-width:22mm")} {c} <span class="small">({n})</span></li>' for a, v, c, n in rf)
    b.page(f"""{sec(3, "Grammatica: unità 10–13", "10 min")}
<div class="two"><div>{sub("A", "Unità 10. Dovere e sapere.", "1 min")}
<table style="margin:0"><tr><th></th><th>dovere</th><th>sapere</th></tr>{dsr}</table></div>
<div>{sub("B", "Unità 10. Il partitivo.", "1 min")}<ol>{ptl}</ol></div></div>
{sub("C", "Unità 11. Il passato prossimo: avere o essere?", "3 min")}
{twocol(ppl, 3)}
<div class="two"><div>{sub("D", "Unità 12. Lo, la, le o ne?", "2 min")}<ol>{prl}</ol></div>
<div>{sub("E", "Unità 13. I verbi riflessivi.", "2 min")}<ol>{rfl}</ol></div></div>""",
    24, """<ol><li>C: movimento e cambiamento con <b>essere</b> (+ accordo: <i>sono andata</i>); gli altri verbi con <b>avere</b>. <i>Fatto</i> è irregolare.</li>
<li>D: il pronome va <b>prima</b> del verbo. <i>Ne</i> = una parte (<i>ne compro sei</i>).</li></ol>""")

    # Page 4: grammar 14-17
    po = [("Questa è", "mia", "madre."), ("Questi sono", "i miei", "genitori."), ("", "Il mio", "cane si chiama Biscotto."), ("Signora, come sta", "Suo", "marito?")]
    pol = "".join(f"<li>{a} {A(x, 'min-width:16mm')} {c}</li>" for a, x, c in po)
    cs = [("Nel soggiorno", "c'è", "un divano."), ("In camera", "ci sono", "due finestre."), ("La lampada è", "accanto al", "divano."), ("Il gatto è", "sotto il", "letto.")]
    csl = "".join(f"<li>{a} {A(x, 'min-width:18mm')} {c}</li>" for a, x, c in cs)
    vt = [("Il treno parte", "da", "Bologna."), ("Un biglietto", "per", "Roma, per favore."), ("Vado al lavoro", "a", "piedi."),
          ("Oggi", "fa", "freddo."), ("", "C'è", "il sole."), ("Il mio compleanno è", "il primo", "maggio.")]
    vtl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")} {c}</li>' for i, (a, x, c) in enumerate(vt)]
    mk = [("Ho andato a Firenze con i miei genitori.", "Sono andato/a a Firenze con i miei genitori."), ("Il mio padre è medico.", "Mio padre è medico."),
          ("Il prosciutto? Compro lo al mercato.", "Il prosciutto? Lo compro al mercato."), ("Io alzo alle sette.", "Mi alzo alle sette."), ("È freddo oggi.", "Fa freddo oggi.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 14–17", "10 min")}
<div class="two"><div>{sub("A", "Unità 14. I possessivi: con o senza articolo?", "2 min")}<ol>{pol}</ol></div>
<div>{sub("B", "Unità 15. C'è, ci sono e il luogo.", "2 min")}<ol>{csl}</ol></div></div>
{sub("C", "Unità 16–17. Completa.", "3 min")}
{twocol(vtl, 4)}
{sub("D", "Unità 11–17. Correggi gli errori.", "3 min")}
<ol>{mkl}</ol>""",
    22, """<ol><li>A: parente al singolare senza articolo (<i>mia madre</i>); al plurale e con le altre cose con l'articolo (<i>i miei genitori, il mio cane</i>).</li>
<li>D: chiedere allo studente <i>perché?</i> per ogni correzione. Sono gli errori più frequenti delle unità 11–17.</li></ol>""")

    # Page 5: vocabulary
    qt = [("un etto di", "prosciutto"), ("una bottiglia di", "vino"), ("mezzo chilo di", "pomodori"), ("un litro di", "latte")]
    qtl = "".join(f"<li>{a} {A(x, 'min-width:22mm')}</li>" for a, x in qt)
    fm = [("La madre di mia madre è mia", "nonna"), ("Il figlio di mio zio è mio", "cugino"), ("Il marito di mia sorella è mio", "cognato"), ("La figlia di mio fratello è mia", "nipote")]
    fml = "".join(f"<li>{a} {A(x, 'min-width:18mm')}.</li>" for a, x in fm)
    df = [("Dormi qui.", "la camera da letto"), ("Il treno parte da qui.", "il binario"), ("Compri il biglietto qui.", "la biglietteria"),
          ("Ti guardi qui.", "lo specchio"), ("Prendi il sole qui.", "il balcone"), ("Lo usi quando piove.", "l'ombrello")]
    dfl = [f'<li value="{i+1}">{a} {A(x, "min-width:30mm")}</li>' for i, (a, x) in enumerate(df)]
    od = [("svegliarsi · alzarsi · vestirsi · il binario", "il binario"), ("la pioggia · la neve · il vento · la cucina", "la cucina"),
          ("il divano · la lampada · il letto · il cognato", "il cognato")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
<div class="two"><div>{sub("A", "Unità 10. Le quantità.", "1 min")}
<div class="bank" style="background:#fff">latte · pomodori · prosciutto · vino</div><ol>{qtl}</ol></div>
<div>{sub("B", "Unità 14. La famiglia.", "2 min")}<ol>{fml}</ol></div></div>
{sub("C", "Unità 15–17. Che cos'è?", "2 min")}
{twocol(dfl, 4)}
{sub("D", "Unità 13–17. Qual è la parola diversa?", "2 min")}
<ol>{odl}</ol>""",
    20, """<p>A: accettare altre combinazioni corrette (<i>una bottiglia di latte, un etto di parmigiano</i>). D: chiedere perché: <i>il cognato non è un mobile!</i></p>""")

    # Page 6: pronunciation + social Italian
    da = ["18:40", "binario 9", "2 etti", "1/4", "3°", "650 €", "15/2", "6:30"]
    dal = [f'<li value="{i+1}">{A(x, "min-width:38mm")}</li>' for i, x in enumerate(da)]
    d1 = [("A", "Buongiorno! Vorrei due etti de prosciutto, per favore.", "due etti di prosciutto"), ("B", "Ecco a Lei. Altro?", ""),
          ("A", "Sì, del parmigiano: mezza chilo, per favore.", "mezzo chilo"), ("B", "E il pane? Abbiamo il pane fresco di oggi.", ""), ("A", "Sì, compro lo!", "lo compro")]
    d2 = [("A", "Buongiorno, un biglietto a Milano, per favore.", "per Milano"), ("B", "Solo andata? Il treno parte alle dieci dal binario tre.", ""),
          ("A", "Il treno sale del binario tre?", "parte dal"), ("B", "Sì, ma oggi è in ritardo di venti minuti: è freddo e c'è la neve.", "fa freddo")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Pronuncia e italiano sociale", "8 min")}
{audiocard(["R2.2", "R2.3"])}
{sub("A", "Unità 10, 15–17. Dettato. Ascolta e scrivi le ore, le date e i numeri.", "3 min", "R2.2")}
{twocol(dal, 5)}
{sub("B", "Unità 10 e 16. Ogni dialogo ha degli errori. Correggi. Poi ascolta e controlla.", "3 min", "R2.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: al mercato</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: alla stazione</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: che cosa compri? Dove vai in treno?", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Accettare le date in cifre o in lettere (<i>il primo aprile</i>). Poi lo studente detta all'insegnante la data del suo compleanno e l'ora del suo treno o autobus.</li>
<li>B: 3 errori nel dialogo 1 e 4 nel dialogo 2 (la frase A del dialogo 2 ne ha due: <i>sale</i> e <i>del</i>). L'audio ha le versioni corrette.</li></ol>""")

    # Page 7: reflect
    cd = [("10", "So comprare il cibo al mercato e chiedere le quantità."), ("11", "So raccontare il mio fine settimana con il passato prossimo."), ("12", "So capire e spiegare una ricetta semplice."),
          ("13", "So descrivere la mia giornata tipo con i verbi riflessivi."), ("14", "So presentare la mia famiglia con i possessivi."), ("15", "So descrivere la mia casa e dire dove sono le cose."),
          ("16", "So comprare un biglietto e chiedere orari e binari."), ("17", "So parlare del tempo e dire le date.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Che cosa vuoi ripassare ancora? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>Un messaggio a un amico.</b> Un amico italiano viene a trovarti. Scrivi un messaggio (60–80 parole):</p>
<ol><li>com'è la tua casa e dove dorme (c'è, ci sono, accanto a…);</li><li>che tempo fa adesso nella tua città;</li><li>come arriva da te (in treno, in autobus, a che ora…);</li><li>che cosa hai fatto lo scorso fine settimana.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare le righe «Non ancora» e preparare due brevi attività di ripasso per le prossime lezioni. Il compito usa la grammatica delle unità 10–17: correggerlo con attenzione e conservarlo come esempio di scrittura. Prossima unità: <b>19 · Ti va di…?</b></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R2.1", "Júlia e Giulia al bar (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R2.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R2.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S23)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 18 - Ripasso 2")
