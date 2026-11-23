# Speak! Progresso B1 - Ripasso 3 (Unità 21-29), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Progresso"
setup(band="B1 · RIPASSO 3", audio_json=os.path.join(HERE, "audio_it-b1-ripasso-3.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la scrivania", "Unità 22"), ("B", "i crisantemi", "Unità 23"), ("C", "il portico", "Unità 24"), ("D", "l'autobus", "Unità 25"),
          ("E", "l'arancina", "Unità 26"), ("F", "il colloquio", "Unità 27"), ("G", "il cortile", "Unità 28"), ("H", "la moto", "Unità 29")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-ripasso-3"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S13 = lines("R3.1 Conversazione"), lines("R3.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R3.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Pagina 1
    cover = cover_html(T, "LIVELLO B1 · RIPASSO 3", "Ripasso 3", "Unità 21–29 · il terzo blocco del B1",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 21–29"),
                        ("LINGUA", "il cui · registro formale · se l'avessi saputo · dopo aver… · avrà finito · passato remoto · qualsiasi · vorrei che · fare + infinito"),
                        ("PRONUNCIA", "dettato di frasi · allo studio e dal meccanico")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la grammatica di quell'unità.", "5 min")}
<div class="bank">l'arancina · l'autobus · il colloquio · il cortile · i crisantemi · la moto · il portico · la scrivania</div>
{photo_grid(T, PHOTOS)}""",
    30, """<p>Le foto A–H vengono dalle unità 22–29, in ordine (l'unità 21 torna nell'ascolto e nella grammatica). Esempi: <i>Se l'avessi saputo, non avrei portato i crisantemi (23). Dopo aver studiato sotto i portici… (24). Davide si sarà addormentato sull'autobus (25). Mangiai un'arancina (26). Ho fatto controllare la moto (29).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>22–29</td><td>1</td></tr>
<tr><td>2 Ascolto: il pranzo di Ferragosto</td><td>12 min</td><td>21–29</td><td>2</td></tr>
<tr><td>3 Grammatica: relativi, registro formale, periodo ipotetico (3), infinito passato, futuro anteriore</td><td>10 min</td><td>21–25</td><td>3</td></tr>
<tr><td>4 Grammatica: passato remoto, qualsiasi / chiunque, vorrei che, fare + infinito</td><td>12 min</td><td>26–29</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>21–29</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>9 min</td><td>21–29</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>21–29</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano, anche quelli dei compiti delle unità 21–29. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 3 dell'unità.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Giugno: smart working e tre nuovi clienti allo studio (21); la lettera formale per la scrivania rotta (22); Camila conosce i genitori di Pietro, con i crisantemi (23); Bruno accetta il 24 (24); Davide si addormenta sull'autobus e Giulia sogna la Sardegna (25). Luglio: Bruno e Chiara a Palermo (26); Camila assunta da settembre (27); l'assemblea di condominio (28). Agosto: la moto di Davide senza benzina (29). Oggi, domenica 15 agosto: il pranzo di Ferragosto nel nuovo giardino del cortile, con il vino dell'amministratore; Camila è in montagna dai genitori di Pietro.</div>
<div class="box"><h4>I 6 ERRORI DA CONTROLLARE</h4>1. <i>Se l'avrei saputo</i> → <b>Se l'avessi saputo</b> 2. <i>Dopo aver arrivato</i> → <b>Dopo essere arrivato</b> 3. <i>Qualsiasi cosa succede</i> → <b>succeda</b> 4. <i>Vorrei che tu vieni</i> → <b>venissi</b> 5. <i>Ho tagliato i capelli</i> (dal parrucchiere) → <b>Mi sono fatto/a tagliare</b> 6. <i>La ragazza che il fratello…</i> → <b>il cui fratello</b></div>
<div class="box"><h4>AUDIO</h4>Traccia R3.1 Conversazione (naturale e lenta) · Traccia R3.2 Dettato di frasi · Traccia R3.3 Due dialoghi</div>""")

    # Pagina 2
    topics = [("il giardino nel cortile", True), ("la moto di Davide", True), ("il viaggio in Sicilia", True), ("Camila in montagna", True),
              ("il signore del quarto piano", True), ("il vino dell'amministratore", True), ("i dolci siciliani", True), ("le vacanze di Giulia in Sardegna", False)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Il giardino è pronto da due mesi.", "F: due settimane fa era tutto grigio."), ("Davide ha aiutato Júlia a piantare le piante.", "V"),
          ("Davide ha fatto controllare la moto.", "V"), ("Bruno ha portato le arancine.", "F: ha portato i cannoli."),
          ("Camila pranza con i genitori di Pietro.", "V"), ("Il signore del quarto piano viene al pranzo.", "F: non verrà, non ci sente."),
          ("Ferri porta il vino.", "V"), ("La signora Rossi vuole che Ferri porti il vino anche l'anno prossimo.", "V")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: il pranzo di Ferragosto", "12 min")}
<p>Domenica 15 agosto. Nel cortile del palazzo di Júlia c'è il pranzo di Ferragosto.</p>
{audiocard(["R3.1 · NATURAL", "R3.1 · SLOW"])}
{sub("A", "Ascolta la versione naturale. Di che cosa parlano? Segna (✓) sette argomenti. Un argomento è in più.", "3 min", "R3.1 · NATURAL")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "4 min")}
<table style="table-layout:fixed"><tr><td>relativi / registro formale (21–22)</td><td>{R("quello la cui radio si sente · Gentili condòmini, come deciso in assemblea…")}</td></tr>
<tr><td>periodo ipotetico / infinito passato (23–24)</td><td>{R("Se avessi saputo…, sarei venuta anch'io. · Dopo aver lavorato due giorni…")}</td></tr>
<tr><td>futuro anteriore (25)</td><td>{R("A quest'ora avrà già mangiato tre piatti di polenta.")}</td></tr>
<tr><td>passato remoto (26)</td><td>{R("Ruggero II fu incoronato re a Palermo.")}</td></tr>
<tr><td>chiunque / vorrei che (27–28)</td><td>{R("chiunque abbia fame · qualsiasi cosa avanzi · Vorrei che lo portasse…")}</td></tr>
<tr><td>fare + infinito (29)</td><td>{R("Ho fatto portare le piante. · Me la sono fatta controllare.")}</td></tr></table>""",
    24, """<p>A: argomento in più = <span class="red">le vacanze di Giulia in Sardegna</span> (Giulia ci va a settembre, ma oggi non se ne parla). B: lo studente corregge a voce. C: accettare anche <i>da sola non ce l'avrei fatta</i> (23) e <i>Pensavo che venisse</i> (concordanza).</p>""")

    # Pagina 3
    ci = [("La ragazza ___ fratello lavora con me si chiama Chiara.", ["il cui"]), ("___ arriva tardi alla riunione porta le paste.", ["Chi"]),
          ("Questo è lo studio in ___ lavoro.", ["cui"])]
    cil = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in ci)
    cc = [("Vi sarei grata se ", ["poteste", "potreste"], "poteste", " rispondere."), ("In attesa di un ", ["Suo", "tuo"], "Suo", " riscontro."),
          ("", ["Distinti saluti.", "Un abbraccio."], "Distinti saluti.", " (lettera formale)")]
    ccl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cc)
    mg = [("Se l'(sapere) ___, non avrei portato i crisantemi.", ["avessi saputo"]), ("Se fosse partita prima, (arrivare) ___ in tempo.", ["sarebbe arrivata"]),
          ("Se avesse studiato quel capitolo, (prendere) ___ di più.", ["avrebbe preso"])]
    mgl = "".join(f"<li>{fill(s, a, '24mm')}</li>" for s, a in mg)
    pi = [("Dopo ", ["essere arrivati", "aver arrivato"], "essere arrivati", ", abbiamo chiamato."), ("Prima di ", ["uscire", "essere uscito"], "uscire", ", chiudi la porta."),
          ("Quando ", ["avrò finito", "finirei"], "avrò finito", " gli esami, comprerò la moto."), ("Non risponde: ", ["si sarà addormentato", "si addormentasse"], "si sarà addormentato", ".")]
    pil = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in pi)
    b.page(f"""{sec(3, "Grammatica: unità 21–25", "10 min")}
<div class="two"><div>{sub("A", "Unità 21. I pronomi relativi.", "2 min")}<ol>{cil}</ol></div>
<div>{sub("B", "Unità 22. La lettera formale. Scegli.", "2 min")}<ol>{ccl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 23. Il periodo ipotetico (3).", "3 min")}<ol>{mgl}</ol></div>
<div>{sub("D", "Unità 24 e 25. Infinito passato e futuro anteriore. Scegli.", "3 min")}<ol>{pil}</ol></div></div>""",
    26, """<p>A: <i>il cui</i> + nome senza altro articolo; <i>chi</i> = la persona che. B: <i>Vi sarei grata se poteste</i> (congiuntivo imperfetto), <i>Suo</i> maiuscolo. C: congiuntivo trapassato + condizionale passato. D: <i>essere</i> con i verbi di movimento; <i>prima di</i> + infinito presente; futuro anteriore per un'azione finita prima o per una supposizione sul passato.</p>""")

    # Pagina 4
    gr = [("Ruggero II (essere) ___ incoronato nel 1130.", ["fu"]), ("Federico II (nascere) ___ a Jesi.", ["nacque"]), ("Gli artisti (lavorare) ___ insieme.", ["lavorarono"])]
    grl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in gr)
    ps = [("Vorrei che il cortile (diventare) ___ un giardino.", ["diventasse"]), ("Sarebbe ora che l'amministratore (mettere) ___ la rastrelliera.", ["mettesse"]),
          ("Mi piacerebbe (avere) ___ un giardino.", ["avere"])]
    psl = "".join(f"<li>{fill(s, a, '20mm')}</li>" for s, a in ps)
    cs = [("Qualsiasi cosa ", ["succeda", "succede"], "succeda", ", ti aiuto."), ("", ["Chiunque", "Qualsiasi"], "Chiunque", " arrivi è il benvenuto.")]
    csl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cs)
    ii = [("La moto? ___ (fare + controllare, io) domani.", ["La faccio controllare"]), ("Júlia si è ___ (tagliare) i capelli.", ["fatta tagliare"]),
          ("L'amministratore ha ___ (mettere) la rastrelliera.", ["fatto mettere"])]
    iil = "".join(f"<li>{fill(s, a, '30mm')}</li>" for s, a in ii)
    mk = [("Se l'avrei saputo, sarei venuta.", "Se l'avessi saputo, sarei venuta."), ("Dopo aver arrivato, ho chiamato.", "Dopo essere arrivato, ho chiamato."),
          ("Qualsiasi cosa succede, ti aiuto.", "Qualsiasi cosa succeda, ti aiuto."), ("Vorrei che tu vieni.", "Vorrei che tu venissi."),
          ("Ho tagliato i capelli dal parrucchiere.", "Mi sono fatta tagliare i capelli."), ("La ragazza che il fratello lavora con me.", "La ragazza il cui fratello lavora con me.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 26–29", "12 min")}
<div class="two"><div>{sub("A", "Unità 26. Il passato remoto.", "2 min")}<ol>{grl}</ol>{sub("B", "Unità 28. Vorrei che, sarebbe ora che.", "2 min")}<ol>{psl}</ol></div>
<div>{sub("C", "Unità 27. Qualsiasi, chiunque. Scegli.", "1 min")}<ol>{csl}</ol>{sub("D", "Unità 29. Fare + infinito.", "3 min")}<ol>{iil}</ol></div></div>
{sub("E", "Unità 21–29. Correggi gli errori.", "3 min")}
<ol style="column-count:2">{mkl}</ol>""",
    26, """<p>A: irregolari 1-3-3 (<i>nacque, nacquero</i>). B: stesso soggetto → infinito. C: <i>qualsiasi</i> + nome, <i>chiunque</i> = qualsiasi persona, sempre + congiuntivo. D: pronome prima di <i>fare</i>; <i>farsi</i> con essere. E: unità 23, 24, 27, 28, 29, 21.</p>""")

    # Pagina 5
    cats = [("Lavoro", "lo smart working · il tirocinio · il colloquio · il contratto"), ("Lettere e reclami", "il reclamo · il recesso · la garanzia · in merito a"),
            ("Casa e condominio", "l'assemblea · l'amministratore · il cortile · la rastrelliera"), ("Servizi", "il meccanico · il parrucchiere · la benzina · la revisione")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("reclamare", "il reclamo"), ("garantire", "la garanzia"), ("assumere", "l'assunzione"), ("riparare", "la riparazione"),
          ("controllare", "il controllo"), ("proporre", "la proposta")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    md = [("Chiudi una lettera formale:", "Distinti saluti."), ("Il negozio è chiuso ad agosto:", "Chiuso per ferie."),
          ("Le ultime cose all'assemblea:", "Varie ed eventuali."), ("Fai un favore volentieri:", "Per te, questo e altro.")]
    mdl = "".join(f"<li>{a} {A(x, 'min-width:30mm')}</li>" for a, x in md)
    od = [("il meccanico · il parrucchiere · l'idraulico · l'androne", "l'androne (non è una persona)"), ("fu · nacque · ebbe · sarà", "sarà (non è passato remoto)"),
          ("chiunque · qualsiasi · dovunque · benché", "benché (non è un indefinito)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 21–29. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">l'amministratore · l'assemblea · la benzina · il colloquio · il contratto · il cortile · la garanzia · in merito a · il meccanico · il parrucchiere · la rastrelliera · il reclamo · il recesso · la revisione · lo smart working · il tirocinio</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}
<div class="two"><div>{sub("C", "Unità 22, 25, 27 e 28. Che cosa dici?", "1 min")}<ol>{mdl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>A e B: parole dalle unità 21–29. C: espressioni delle unità 22, 25, 27 e 28. D: chiedere sempre perché.</p>""")

    # Pagina 6
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Marco", "Júlia, il cliente vuole che rifacciamo l'ingresso.", ""), ("Júlia", "Di nuovo? Se l'avrei saputo, non avrei finito i disegni ieri.", "avessi saputo"),
          ("Marco", "Lo so. Vorrei che il capo gli dice di no.", "dicesse"), ("Júlia", "Non lo farà. Qualsiasi cosa chiede il cliente, il capo dice sempre di sì.", "chieda"),
          ("Marco", "Allora ti offro un caffè, e chiunque ci cerchi, siamo in riunione.", "")]
    d2 = [("Davide", "Buongiorno! Vorrei far controllare la moto.", ""), ("Meccanico", "Certo. Quando me la porti?", ""),
          ("Davide", "Domani mattina, dopo avere andato all'università.", "essere andato"), ("Meccanico", "Va bene. Per mezzogiorno l'avrò già controllata.", ""),
          ("Davide", "E vorrei anche che tu cambi l'olio. Grazie per l'altra volta: non mi hai fatto pagato niente!", "cambiassi · pagare")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "9 min")}
{audiocard(["R3.2", "R3.3"])}
{sub("A", "Unità 21–29. Dettato. Ascolta e scrivi le frasi.", "4 min", "R3.2")}
<ol style="line-height:1.25;column-count:1">{dal}</ol>
{sub("B", "Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R3.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 1: allo studio</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 2: dal meccanico</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un altro cliente, un altro servizio.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase; ogni frase ripassa un'unità, dalla 21 alla 29, in ordine.</li>
<li>B: dialogo 1: periodo ipotetico (23), <i>vorrei che</i> + congiuntivo imperfetto (28), <i>qualsiasi</i> + congiuntivo (27). Dialogo 2: infinito passato con <i>essere</i> (24), <i>vorrei che</i> (28), <i>fare</i> + infinito (29). L'audio ha le versioni corrette.</li></ol>""")

    # Pagina 7
    cd = [("21", "So descrivere persone e cose con il quale, il cui, chi."), ("22", "So scrivere una lettera formale o un reclamo."),
          ("23", "So parlare di errori e rimpianti (se l'avessi saputo…)."), ("24", "So mettere in ordine azioni (dopo aver…, prima di…)."),
          ("25", "So fare supposizioni e parlare di azioni finite nel futuro."), ("26", "So capire un racconto storico al passato remoto."),
          ("27", "So incoraggiare e dire «qualsiasi cosa succeda»."), ("28", "So fare proposte gentili (vorrei che, bisognerebbe che)."),
          ("29", "So parlare di servizi e di cose che faccio fare.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Rileggi le correzioni dei tuoi compiti: quali errori fai ancora? Scrivi due cose da migliorare.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p><b>La mia estate.</b> Scrivi una mail a un amico italiano e raccontagli gli ultimi tre mesi:</p>
<ol style="line-height:1.4"><li>una persona che hai conosciuto (<i>il cui… / che…</i>) e una cosa che hai fatto fare (<i>ho fatto riparare…</i>);</li><li>un errore o un rimpianto (<i>se l'avessi saputo…</i>);</li><li>una proposta o un desiderio per il tuo palazzo, il lavoro o la città (<i>vorrei che…</i>);</li><li>che cosa avrai fatto entro dicembre (<i>avrò finito…</i>).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare con lo studente le righe «Non ancora» e decidere che cosa ripassare (pagina 3 dell'unità corrispondente). Prossima unità: <b>B1 31</b>, inizio del quarto e ultimo blocco del B1 (settembre–dicembre).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R3.1", "Il pranzo di Ferragosto (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R3.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R3.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 30 - Ripasso 3")
