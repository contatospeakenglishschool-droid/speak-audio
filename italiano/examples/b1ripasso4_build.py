# Speak! Progresso B1 - Ripasso 4 (Unità 31-39), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Progresso"
setup(band="B1 · RIPASSO 4", audio_json=os.path.join(HERE, "audio_it-b1-ripasso-4.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

# photo memory: unit order (Ripasso exception to the warm-up shuffle rule); bank alphabetical
PHOTOS = [("A", "l'impalcatura", "Unità 32"), ("B", "la maratona", "Unità 33"), ("C", "il portone", "Unità 34"), ("D", "l'album di foto", "Unità 35"),
          ("E", "la corona d'alloro", "Unità 36"), ("F", "la pergola", "Unità 37"), ("G", "il tabellone delle partenze", "Unità 38"), ("H", "il brindisi", "Unità 39")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-ripasso-4"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S13 = lines("R4.1 Conversazione"), lines("R4.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R4.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Pagina 1
    cover = cover_html(T, "LIVELLO B1 · RIPASSO 4", "Ripasso 4", "Unità 31–39 · l'ultimo blocco del B1",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 31–39"),
                        ("LINGUA", "tuttavia · purché · così… che · va fatto · passato remoto · finita la festa · mi ha chiesto di · ne vale la pena · tutti i tempi"),
                        ("PRONUNCIA", "dettato di frasi · allo studio e al bar")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la grammatica di quell'unità.", "5 min")}
<div class="bank">l'album di foto · il brindisi · la corona d'alloro · l'impalcatura · la maratona · la pergola · il portone · il tabellone delle partenze</div>
{photo_grid(T, PHOTOS)}""",
    30, """<p>Le foto A–H vengono dalle unità 32–39, in ordine (l'unità 31 torna nell'ascolto e nella grammatica). Esempi: <i>Montano l'impalcatura prima che arrivino i clienti (32). Era così stanco che non parlava (33). Il portone va restaurato (34). Mio padre nacque nel 1924 (35). Finita la festa, siamo andati a casa (36). Galli mi ha chiesto di disegnare la pergola (37). Il volo è caro, ma ne vale la pena (38). Se non fossi venuta, non avrei conosciuto… (39).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>32–39</td><td>1</td></tr>
<tr><td>2 Ascolto: bentornati!</td><td>12 min</td><td>31–39</td><td>2</td></tr>
<tr><td>3 Grammatica: connettivi, congiunzioni + congiuntivo, frasi consecutive, va fatto, passato remoto</td><td>10 min</td><td>31–35</td><td>3</td></tr>
<tr><td>4 Grammatica: participio assoluto, richieste e domande riferite, ne vale la pena, tutti i tempi</td><td>12 min</td><td>36–39</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>31–39</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>9 min</td><td>31–39</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>31–39</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano, anche quelli dei compiti delle unità 31–39. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 3 dell'unità.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Settembre: il turismo in città (31); il progetto del dottor Galli, un palazzo che diventa un albergo (32). Ottobre: la seconda maratona di Davide, 3:31 (33). Novembre: il sopralluogo con la Soprintendenza (34); la storia della famiglia Rossi (35); la laurea di Davide (36). Dicembre: Galli e la pergola (37); Natale in Brasile? Sì (38); l'aperitivo di saluto (39). Oggi, lunedì 3 gennaio 2028: Júlia e Bruno sono tornati dal Brasile; la signora Rossi racconta come suo padre comprò la bottega.</div>
<div class="box"><h4>I 6 ERRORI DA CONTROLLARE</h4>1. <i>Mi ha chiesto per mandare</i> → <b>di mandare</b> 2. <i>purché mi dici</i> → <b>dica</b> 3. <i>vanno fatto</i> → <b>vanno fatte</b> 4. <i>ma vale la pena</i> (cosa già detta) → <b>ne vale la pena</b> 5. <i>Se avrei saputo</i> → <b>Se avessi saputo</b> 6. <i>così stanco come non…</i> → <b>così stanco che</b></div>
<div class="box"><h4>AUDIO</h4>Traccia R4.1 Conversazione (naturale e lenta) · Traccia R4.2 Dettato di frasi · Traccia R4.3 Due dialoghi</div>""")

    # Pagina 2
    topics = [("il viaggio in Brasile", True), ("il caldo di Natale", True), ("la foto per Chiara", True), ("la richiesta della mamma", True),
              ("la bottega del padre della signora Rossi", True), ("l'e-mail di Galli", True), ("la pergola e Marco", True), ("il nuovo lavoro di Davide", False)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Júlia e Bruno sono tornati ieri sera.", "V"), ("All'aeroporto la mamma aveva un cartello.", "V"),
          ("A Natale in Brasile faceva freddo.", "F: faceva così caldo che hanno mangiato il gelato in piscina."), ("La mamma ha cucinato per dieci persone.", "F: per venti."),
          ("La mamma vuole che Júlia torni a Pasqua.", "V"), ("Il padre della signora Rossi ha pagato la bottega in un anno.", "F: in dieci anni."),
          ("Galli accetta la pergola, a patto che il legno sia chiaro.", "V"), ("Marco vuole ancora la pergola più bassa.", "V")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: bentornati!", "12 min")}
<p>Lunedì 3 gennaio, mattina. Júlia e Bruno sono tornati dal Brasile e passano dal Bar Giulia.</p>
{audiocard(["R4.1 · NATURAL", "R4.1 · SLOW"])}
{sub("A", "Ascolta la versione naturale. Di che cosa parlano? Segna (✓) sette argomenti. Un argomento è in più.", "3 min", "R4.1 · NATURAL")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "4 min")}
<table style="table-layout:fixed"><tr><td>connettivi (31)</td><td>{R("Eppure la mamma ha cucinato per venti persone. · Piuttosto che litigare…")}</td></tr>
<tr><td>congiunzioni + congiuntivo (32)</td><td>{R("purché non mangi tutto lui · a patto che il legno sia chiaro · affinché il cantiere possa partire")}</td></tr>
<tr><td>frasi consecutive (33)</td><td>{R("Ha pianto così tanto che piangeva anche il papà. · Faceva talmente caldo che…")}</td></tr>
<tr><td>andare + participio (34)</td><td>{R("va fatta più bassa")}</td></tr>
<tr><td>passato remoto (35)</td><td>{R("partì · gliela vendette · la pagò")}</td></tr>
<tr><td>participio assoluto / riferire (36–37)</td><td>{R("Arrivati all'aeroporto… · Mi ha chiesto di tornare a Pasqua.")}</td></tr>
<tr><td>valerne la pena, tenerci (38)</td><td>{R("Ne è valsa la pena. · Ci tengo alla cucina della mamma.")}</td></tr></table>""",
    24, """<p>A: argomento in più = <span class="red">il nuovo lavoro di Davide</span> (oggi non se ne parla). B: lo studente corregge a voce. C: tutta la conversazione è un esempio dell'unità 39 (tempi del racconto): far trovare un trapassato o un imperfetto di scena.</p>""")

    # Pagina 3
    cn = [("Il turismo porta lavoro; ", ["tuttavia", "dunque"], "tuttavia", ", gli affitti salgono."), ("Ha studiato poco, ", ["eppure", "dunque"], "eppure", " ha preso trenta."),
          ("", ["Piuttosto che", "Dunque"], "Piuttosto che", " vietare, costruiamo case per studenti.")]
    cnl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cn)
    cg = [("Ti lascio le chiavi prima che tu (partire) ___.", ["parta"]), ("È uscito senza che nessuno lo (vedere) ___.", ["vedesse"]),
          ("Va bene, purché (voi, finire) ___ entro Pasqua.", ["finiate"])]
    cgl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in cg)
    cs = [("Era ", ["così", "molto"], "così", " stanco che non riusciva a parlare."), ("C'era un vento ", ["tale", "tanto"], "tale", " che non si poteva correre."),
          ("Era stanco ", ["al punto da", "al punto che di"], "al punto da", " non riuscire a parlare.")]
    csl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cs)
    pr = [("Le finestre (andare + fare) ___ di legno.", ["vanno fatte"]), ("Il portone si (dovere) ___ restaurare.", ["deve"]),
          ("Mio padre (nascere) ___ nel 1924.", ["nacque"]), ("I miei genitori si (sposare) ___ nel 1950.", ["sposarono"])]
    prl = "".join(f"<li>{fill(s, a, '22mm')}</li>" for s, a in pr)
    b.page(f"""{sec(3, "Grammatica: unità 31–35", "10 min")}
<div class="two"><div>{sub("A", "Unità 31. I connettivi. Scegli.", "2 min")}<ol>{cnl}</ol></div>
<div>{sub("B", "Unità 32. Congiunzioni + congiuntivo.", "2 min")}<ol>{cgl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 33. Le frasi consecutive. Scegli.", "3 min")}<ol>{csl}</ol></div>
<div>{sub("D", "Unità 34 e 35. Va fatto e il passato remoto.", "3 min")}<ol>{prl}</ol></div></div>""",
    26, """<p>A: <i>tuttavia</i> = però; <i>eppure</i> = e nonostante questo; <i>piuttosto che</i> + infinito. B: <i>prima che, senza che, purché</i> + congiuntivo; al passato il congiuntivo imperfetto (<i>vedesse</i>). C: <i>così / talmente + aggettivo + che</i>; <i>un… tale che</i>; <i>al punto da</i> + infinito. D: <i>andare</i> + participio concorda con il soggetto; con i modali <i>si deve</i> + infinito; passato remoto irregolare <i>nacque</i>.</p>""")

    # Pagina 4
    pa = [("___ (finire) la festa, Giulia ha chiuso il bar.", ["Finita"]), ("___ (arrivare) a casa, Júlia ha chiamato la mamma.", ["Arrivata"]),
          ("___ (fare) le foto, le ha mandate alla Soprintendenza.", ["Fatte"])]
    pal = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in pa)
    ri = [("«Mandami il disegno!» → Mi ha chiesto ___ mandargli il disegno.", ["di"]), ("«Ti piace?» → Mi ha chiesto ___ mi piaceva.", ["se"]),
          ("«Non toccate niente!» → Ci ha detto ___ toccare niente.", ["di non"])]
    ril = "".join(f"<li>{fill(s, a, '14mm')}</li>" for s, a in ri)
    vc = [("Il viaggio era lungo, ma ", ["ne è valsa", "ha valso"], "ne è valsa", " la pena."), ("Scusa, ma questo che ", ["c'entra", "entra"], "c'entra", "?"),
          ("Non ", ["me la sento", "mi sento"], "me la sento", " di dirglielo.")]
    vcl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in vc)
    tp = [("Quando sono arrivata, (piovere) ___.", ["pioveva"]), ("Se non (venire) ___ a Bologna, non avrei conosciuto Giulia.", ["fossi venuta"]),
          ("Abito qui ___ tre anni.", ["da"])]
    tpl = "".join(f"<li>{fill(s, a, '20mm')}</li>" for s, a in tp)
    mk = [("Mi ha chiesto per mandare le foto.", "Mi ha chiesto di mandare le foto."), ("Ti aiuto, purché mi dici la verità.", "Ti aiuto, purché mi dica la verità."),
          ("Le finestre vanno fatto di legno.", "Le finestre vanno fatte di legno."), ("Il volo è caro, ma vale la pena.", "Il volo è caro, ma ne vale la pena."),
          ("Se avrei saputo, sarei venuta.", "Se avessi saputo, sarei venuta."), ("Era così stanco come non parlava.", "Era così stanco che non parlava.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 36–39", "12 min")}
<div class="two"><div>{sub("A", "Unità 36. Il participio assoluto.", "2 min")}<ol>{pal}</ol>{sub("B", "Unità 37. Riferisci: di, di non o se.", "2 min")}<ol>{ril}</ol></div>
<div>{sub("C", "Unità 38. Scegli.", "1 min")}<ol>{vcl}</ol>{sub("D", "Unità 39. Tutti i tempi.", "3 min")}<ol>{tpl}</ol></div></div>
{sub("E", "Unità 31–39. Correggi gli errori.", "3 min")}
<ol style="column-count:2">{mkl}</ol>""",
    26, """<p>A: il participio concorda con il nome (<i>finita la festa, fatte le foto</i>) o con il soggetto dei verbi con <i>essere</i> (<i>arrivata</i>). B: imperativo → <i>di</i> + infinito; domanda sì / no → <i>se</i>. C: <i>ne è valsa</i> (essere, femminile). D: imperfetto per la scena, periodo ipotetico dell'irrealtà, <i>da</i> + presente. E: unità 37, 32, 34, 38, 39, 33.</p>""")

    # Pagina 5
    cats = [("Città e turismo", "gli affitti brevi · la ferramenta · il turista · la valigia"), ("Lavoro e cantiere", "il preventivo · il sopralluogo · il parere · la pergola"),
            ("Sport e feste", "la maratona · la laurea · il papiro · il brindisi"), ("Viaggi e decisioni", "lo scalo · andata e ritorno · la scadenza · la priorità")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("restaurare", "il restauro"), ("vietare", "il divieto"), ("consegnare", "la consegna"), ("decidere", "la decisione"),
          ("laurearsi", "la laurea"), ("partire", "la partenza")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    md = [("Fai gli auguri prima di Natale:", "Buone feste!"), ("Una cosa non ha niente a che fare:", "Che c'entra?"),
          ("Una cosa è molto importante per te:", "Ci tengo!"), ("Un amico ha finito la laurea:", "Congratulazioni, dottore!")]
    mdl = "".join(f"<li>{a} {A(x, 'min-width:30mm')}</li>" for a, x in md)
    od = [("il preventivo · il sopralluogo · il parere · il papiro", "il papiro (non è un documento dello studio)"), ("nacque · fu · venne · sarà", "sarà (non è passato remoto)"),
          ("affinché · purché · prima che · eppure", "eppure (non vuole il congiuntivo)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 31–39. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">gli affitti brevi · andata e ritorno · il brindisi · la ferramenta · la laurea · la maratona · il papiro · il parere · la pergola · il preventivo · la priorità · la scadenza · lo scalo · il sopralluogo · il turista · la valigia</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}
<div class="two"><div>{sub("C", "Unità 36, 38 e 39. Che cosa dici?", "1 min")}<ol>{mdl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>A e B: parole dalle unità 31–39. C: espressioni delle unità 36, 38 e 39. D: chiedere sempre perché.</p>""")

    # Pagina 6
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Marco", "Júlia, ha telefonato Galli. Ti ha chiesto per mandargli il disegno nuovo.", "di mandargli"), ("Júlia", "Di nuovo? Va bene, ma lo mando solo a patto che non lo cambia più.", "cambi"),
          ("Marco", "Giusto. E ricordati: le foto degli affreschi vanno mandato entro venerdì.", "mandate"), ("Júlia", "Le ho già mandate. Finito il disegno, vado a casa!", "")]
    d2 = [("Giulia", "Davide, che faccia! Tutto bene?", ""), ("Davide", "Sono così stanco come non riesco a pensare. Ho mandato il curriculum a tre studi.", "che"),
          ("Giulia", "Se l'avrei saputo, ti avrei presentato un mio cliente architetto.", "avessi saputo"), ("Davide", "Davvero? Allora domani ti porto il curriculum, purché tu non lo dici a nessuno!", "dica")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "9 min")}
{audiocard(["R4.2", "R4.3"])}
{sub("A", "Unità 31–39. Dettato. Ascolta e scrivi le frasi.", "4 min", "R4.2")}
<ol style="line-height:1.25;column-count:1">{dal}</ol>
{sub("B", "Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R4.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 1: allo studio</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 2: al bar</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un altro cliente, un'altra notizia.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase; ogni frase ripassa un'unità, dalla 31 alla 39, in ordine.</li>
<li>B: dialogo 1: <i>chiedere di</i> (37), <i>a patto che</i> + congiuntivo (32), <i>vanno mandate</i> (34). Dialogo 2: <i>così… che</i> (33), periodo ipotetico (39), <i>purché</i> + congiuntivo (32). L'audio ha le versioni corrette.</li></ol>""")

    # Pagina 7
    cd = [("31", "So esprimere un'opinione e contrapporre idee (tuttavia, eppure, piuttosto)."), ("32", "So mettere condizioni e scopi (affinché, purché, prima che)."),
          ("33", "So raccontare le conseguenze (così… che, tanto che)."), ("34", "So spiegare regole e obblighi (va fatto, si deve)."),
          ("35", "So capire e raccontare una storia di famiglia al passato remoto."), ("36", "So raccontare una sequenza con il participio (finita la festa…)."),
          ("37", "So riferire richieste e domande (mi ha chiesto di… / se…)."), ("38", "So valutare una decisione (ne vale la pena, ci tengo)."),
          ("39", "So raccontare un periodo della mia vita con tutti i tempi.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Rileggi le correzioni dei tuoi compiti: quali errori fai ancora? Scrivi due cose da migliorare.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p><b>Il mio anno.</b> Scrivi una mail a un amico italiano e fai il bilancio del tuo anno:</p>
<ol style="line-height:1.4"><li>un fatto importante e com'è andata (<i>così… che</i>, <i>finito/a…</i>);</li><li>una cosa che qualcuno ti ha chiesto o consigliato (<i>mi ha chiesto di… / se…</i>);</li><li>una decisione: <i>ne è valsa la pena?</i> Che cosa avresti fatto se…?</li><li>un progetto per l'anno nuovo, con una condizione (<i>purché, a patto che</i>).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare con lo studente le righe «Non ancora» e decidere che cosa ripassare (pagina 3 dell'unità corrispondente). È l'ultima lezione del <b>B1 Progresso</b>: rileggere insieme i progressi dell'anno prima di passare al livello successivo.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R4.1", "Bentornati! (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R4.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R4.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 40 - Ripasso 4")
