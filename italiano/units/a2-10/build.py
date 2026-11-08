# Speak! Ponte A2 - Ripasso 1 (Unità 01-09), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Ponte"
setup(band="A2 · RIPASSO 1", audio_json=os.path.join(HERE, "audio_it-a2-ripasso-1.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il vestito", "Unità 01"), ("B", "l'album di foto", "Unità 02"), ("C", "il cane", "Unità 03"), ("D", "il termometro", "Unità 04"),
          ("E", "il panettone", "Unità 05"), ("F", "il colloquio", "Unità 06"), ("G", "il Carnevale", "Unità 07"), ("H", "l'ufficio postale", "Unità 08"),
          ("I", "il parco", "Unità 09")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-ripasso-1"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S13 = lines("R1.1 Conversazione"), lines("R1.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R1.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: cover + photo memory
    cover = cover_html(T, "LIVELLO A2 · RIPASSO 1", "Ripasso 1", "Unità 01–09 · vestiti · ricordi · incidenti · salute · favori · lavoro · progetti · uffici · opinioni",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 01–09 dell'A2"),
                        ("LINGUA", "gli, le · più… di · imperfetto · passato prossimo · imperativo · condizionale · sapere / conoscere · futuro · Lei · penso che sia"),
                        ("PRONUNCIA", "dettato di frasi · alla posta e al bar")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la parola.", "5 min")}
<div class="bank">l'album di foto · il cane · il Carnevale · il colloquio · il panettone · il parco · il termometro · l'ufficio postale · il vestito</div>
{photo_grid(T, PHOTOS)}""",
    22, """<p>Le foto A–I vengono dalle unità 01–09, in ordine. Esempio: <i>il cane → Mentre attraversavo la piazza, è uscito un cane.</i> Chiedere una frase con il tempo dell'unità: <i>Il vestito blu mi sta bene (01). Da bambina guardavo l'album (02). Hai la febbre? Prendi il termometro! (04). Mi piacerebbe mangiare il panettone (05). A Carnevale andrò in Brasile (07). Penso che il parco sia bello (09).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>01–09</td><td>1</td></tr>
<tr><td>2 Ascolto: sei mesi di foto</td><td>10 min</td><td>01–09</td><td>2</td></tr>
<tr><td>3 Grammatica: pronomi, imperfetto, passato, imperativo, condizionale</td><td>10 min</td><td>01–05</td><td>3</td></tr>
<tr><td>4 Grammatica: sapere / conoscere, futuro, Lei, congiuntivo</td><td>10 min</td><td>06–09</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>01–09</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>8 min</td><td>01–09</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>01–09</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 4 dell'unità.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Settembre: Júlia compra un vestito blu per il matrimonio di Luca e Sara e una cravatta per Bruno (unità 1). Ottobre: l'album delle foto di quando era bambina (2). Novembre: cade dalla bici per colpa di Briciola, il cane di Franco (3); Marco ha l'influenza (4). Dicembre: favori, desideri e la cena della vigilia (5). Gennaio: Matteo fa il colloquio al bar di Giulia (6); Júlia prepara il viaggio per il Carnevale (7). Febbraio: torna e rinnova il permesso di soggiorno alla posta (8). Marzo: il Comune sceglie il progetto del giardino in Bolognina (9). Fine marzo: Giulia stampa le foto di questi sei mesi e le guarda con Júlia.</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>Ero sei anni</i> → <b>Avevo sei anni</b> 2. <i>A Giulia gli piace</i> → <b>A Giulia piace / Le piace</b> 3. <i>Mi fa male le gambe</i> → <b>Mi fanno male</b> 4. <i>So Matteo</i> → <b>Conosco Matteo</b> 5. <i>Penso che è cara</i> → <b>Penso che sia cara</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia R1.1 Conversazione (lenta e naturale) · Traccia R1.2 Dettato di frasi · Traccia R1.3 Due dialoghi</div>""")

    # Page 2: listening
    topics = [("il matrimonio", True), ("l'infanzia", True), ("un incidente", True), ("la salute", True), ("il permesso di soggiorno", False),
              ("il Natale", True), ("il lavoro di Matteo", True), ("il Carnevale", True), ("i progetti per l'estate", True), ("il giardino", True)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Al matrimonio Bruno portava la cravatta.", "V"), ("Da bambina Júlia aveva i capelli neri.", "F: era bionda."),
          ("Júlia è caduta dalla bici per colpa di un cane.", "V"), ("Marco aveva la febbre a 39.", "F: a 38 e mezzo."),
          ("Alla vigilia Giulia ha portato il panettone.", "V"), ("Matteo fa un cappuccino perfetto in cinque minuti.", "F: in due minuti."),
          ("I lavori al giardino cominceranno a settembre.", "F: a maggio; a settembre c'è l'inaugurazione."), ("Júlia vuole mandare le foto a sua madre.", "V")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: sei mesi di foto", "10 min")}
<p>Fine marzo. Al bar, Giulia mostra a Júlia le foto che ha stampato: sono sei mesi di ricordi.</p>
{audiocard(["R1.1 · SLOW", "R1.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) nove argomenti. Un argomento è in più.", "3 min", "R1.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R1.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>imperfetto + passato prossimo</td><td>{R("Mentre attraversavo piazza Maggiore, è uscito un cane.")}</td></tr>
<tr><td>imperativo + pronome</td><td>{R("Non dirlo a Davide!")}</td></tr><tr><td>condizionale</td><td>{R("Mi piacerebbe… · Potresti farmi una copia?")}</td></tr>
<tr><td>futuro</td><td>{R("cominceranno · ci sarà · resterò")}</td></tr><tr><td>congiuntivo</td><td>{R("Penso che la gente sia molto contenta.")}</td></tr></table>""",
    18, """<p>A: argomento in più = <span class="red">il permesso di soggiorno</span> (unità 8: non ne parlano). B: lo studente corregge a voce le frasi false. C: se serve, lo studente può leggere la trascrizione nell'ultima pagina della guida.</p>""")

    # Page 3: grammar 01-05
    pr = [("Il blu ___ sta benissimo! (a te)", ["ti"]), ("A Bruno ___ ho comprato una cravatta.", ["gli"]), ("A Giulia ___ piace il verde.", ["le"]),
          ("Il blu è più caro ___ verde.", ["del"])]
    prl = "".join(f"<li>{fill(s, a, '10mm')}</li>" for s, a in pr)
    imp = [("essere", "ero", "eravamo"), ("avere", "avevo", "avevamo"), ("fare", "facevo", "facevamo"), ("abitare", "abitavo", "abitavamo")]
    impr = "".join(f"<tr><td><b>{v}</b></td><td>{A(a, 'min-width:18mm')}</td><td>{A(c, 'min-width:20mm')}</td></tr>" for v, a, c in imp)
    pp = [("Mentre ", ["attraversavo", "ho attraversato"], "attraversavo", " la piazza, all'improvviso "), ("", ["usciva", "è uscito"], "è uscito", " un cane. "),
          ("Bruno ", ["dormiva", "ha dormito"], "dormiva", " in biblioteca quando "), ("", ["chiudevano", "hanno chiuso"], "hanno chiuso", " la porta.")]
    ppt = "".join(f"{a}{ch(o, r)}{z}" for a, o, r, z in pp)
    im = [("Hai la febbre? (riposarsi) ___!", ["Riposati"]), ("(dare a me) ___ il termometro, per favore!", ["Dammi"]),
          ("Il medico? (chiamare il medico) ___ subito!", ["Chiamalo"]), ("L'antibiotico? Non (prenderlo) ___!", ["prenderlo"])]
    iml = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in im)
    cd = [("(potere, tu) ___ aiutarmi?", ["Potresti"]), ("Mi (piacere) ___ sciare.", ["piacerebbe"]), ("Al tuo posto, io (andare) ___ dal medico.", ["andrei"]),
          ("(volere, io) ___ un cappuccino, per favore.", ["Vorrei"])]
    cdl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in cd)
    b.page(f"""{sec(3, "Grammatica: unità 01–05", "10 min")}
<div class="two"><div>{sub("A", "Unità 01. Pronomi e paragoni.", "2 min")}<ol>{prl}</ol></div>
<div>{sub("B", "Unità 02. L'imperfetto.", "2 min")}<table style="margin:0"><tr><th></th><th>io</th><th>noi</th></tr>{impr}</table></div></div>
{sub("C", "Unità 03. Imperfetto o passato prossimo? Scegli.", "2 min")}
<div class="box" style="margin-top:1mm;line-height:1.9">{ppt}</div>
<div class="two"><div>{sub("D", "Unità 04. L'imperativo con i pronomi.", "2 min")}<ol>{iml}</ol></div>
<div>{sub("E", "Unità 05. Il condizionale.", "2 min")}<ol>{cdl}</ol></div></div>""",
    26, """<ol><li>A: <i>gli</i> = a lui, <i>le</i> = a lei; con <i>a Giulia</i> non si ripete <i>le</i>. B: <i>essere</i> è l'unico irregolare: <i>ero, eri, era…</i></li>
<li>C: imperfetto = lo sfondo (che cosa succedeva), passato prossimo = il fatto (che cosa è successo). D: il pronome si attacca all'imperativo: <i>riposati, chiamalo, dammi</i> (doppia m). E: <i>-are</i> → <i>-erei</i>: <i>comprerei</i>.</li></ol>""")

    # Page 4: grammar 06-09
    sc = [("___ Matteo da un anno.", ["Conosco"]), ("Matteo ___ fare il latte art.", ["sa"]), ("Per arrivare in centro ___ venti minuti.", ["ci vogliono"]),
          ("Ieri Giulia ___ andare in banca.", ["è dovuta"])]
    scl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in sc)
    fu = [("Júlia (partire) ___ il 5 febbraio.", ["partirà"]), ("Noi (andare) ___ a Firenze.", ["andremo"]), ("(essere) ___ un anno pieno di novità.", ["Sarà"]),
          ("Se finisco presto, ti (chiamare) ___.", ["chiamerò"])]
    ful = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in fu)
    lf = [("firma qui", "firmi qui"), ("prendi il numero", "prenda il numero"), ("vai dritto", "vada dritto"), ("non preoccuparti", "non si preoccupi")]
    lfr = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:28mm')}</td></tr>" for a, x in lf)
    cg = [("Penso che Bologna ___ cara. (essere)", ["sia"]), ("Spero che il Comune ___ noi. (scegliere)", ["scelga"]),
          ("Secondo me il progetto ___ bello. (essere)", ["è"]), ("Davide spera ___ la maratona. (vincere)", ["di vincere"])]
    cgl = "".join(f"<li>{fill(s, a, '16mm')}</li>" for s, a in cg)
    mk = [("Ero sei anni.", "Avevo sei anni."), ("A Giulia gli piace il blu.", "A Giulia piace il blu. / Le piace il blu."), ("Mi fa male le gambe.", "Mi fanno male le gambe."),
          ("So Matteo da un anno.", "Conosco Matteo da un anno."), ("Penso che Bologna è cara.", "Penso che Bologna sia cara.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 06–09", "10 min")}
<div class="two"><div>{sub("A", "Unità 06. Sapere, conoscere, ci vuole.", "2 min")}<ol>{scl}</ol></div>
<div>{sub("B", "Unità 07. Il futuro.", "2 min")}<ol>{ful}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 08. Dal tu al Lei.", "2 min")}<table style="margin:0"><tr><th>tu</th><th>Lei</th></tr>{lfr}</table></div>
<div>{sub("D", "Unità 09. Indicativo, congiuntivo o di + infinito?", "2 min")}<ol>{cgl}</ol></div></div>
{sub("E", "Unità 01–09. Correggi gli errori.", "2 min")}
<ol>{mkl}</ol>""",
    26, """<ol><li>A: <i>sapere</i> + infinito o un'informazione, <i>conoscere</i> + persone e luoghi; <i>ci vuole</i> + singolare, <i>ci vogliono</i> + plurale; modale + <i>andare</i> → ausiliare <i>essere</i>.</li>
<li>C: il Lei usa la forma del congiuntivo: <i>firmi, prenda, vada</i>. D: dopo <i>secondo me</i> l'indicativo; stesso soggetto → <i>di</i> + infinito.</li></ol>""")

    # Page 5: vocabulary
    cats = [("I vestiti", "la gonna · la cravatta · la taglia"), ("Il corpo e la salute", "la schiena · il termometro · la febbre"),
            ("Il lavoro", "il curriculum · il colloquio · lo stipendio"), ("Gli uffici", "il modulo · la firma · il permesso di soggiorno")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("partire", "la partenza"), ("arrivare", "l'arrivo"), ("firmare", "la firma"), ("spedire", "la spedizione"), ("iscriversi", "l'iscrizione"), ("allenarsi", "l'allenamento")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    df = [("Il dolce di Natale.", "il panettone"), ("Il dolce di Pasqua.", "la colomba"), ("La misura dei vestiti.", "la taglia"), ("Serve per misurare la febbre.", "il termometro")]
    dfl = "".join(f"<li>{a} {A(x, 'min-width:24mm')}</li>" for a, x in df)
    od = [("la giacca · la gonna · la camicia · la schiena", "la schiena"), ("il raffreddore · l'influenza · il colloquio · la tosse", "il colloquio"),
          ("partirò · sarò · andrei · farò", "andrei (condizionale)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 01–08. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">il colloquio · la cravatta · il curriculum · la febbre · la firma · la gonna · il modulo · il permesso di soggiorno · la schiena · lo stipendio · la taglia · il termometro</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 4)}
<div class="two"><div>{sub("C", "Che cos'è?", "1 min")}<ol>{dfl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>B: <i>-are</i> → <i>-enza</i> o <i>-o</i>; <i>-ire</i> → <i>-izione</i>; <i>-arsi</i> → <i>-amento</i>. Sono parole delle unità 07 e 08 (<i>la partenza, l'arrivo, la firma</i>). C: unità 05 e 07. D: chiedere sempre perché.</p>""")

    # Page 6: dictation + social Italian
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Impiegato", "Buongiorno, mi dica.", ""), ("Júlia", "Buongiorno. Vorrei spedire questa busta in Brasile.", ""),
          ("Impiegato", "Dia mi la busta, per favore. Sono quattro euro e cinquanta. Firma qui.", "Mi dia · Firmi"),
          ("Júlia", "Ecco. Quanto tempo ci vuole?", ""), ("Impiegato", "Ci vuole circa due settimane. Non si preoccupi, arriverà.", "Ci vogliono")]
    d2 = [("Davide", "Ahi! Ho dolore di schiena.", "Ho mal di schiena"), ("Júlia", "Ancora? Secondo me corri troppo. Dovresti riposarti.", ""),
          ("Davide", "Ma la maratona è a ottobre! Se non mi alleno, non arriverò alla fine.", ""), ("Júlia", "Allora va' dal medico. E domani non corri!", "non correre"),
          ("Davide", "Va bene. Penso che tu hai ragione.", "abbia")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "8 min")}
{audiocard(["R1.2", "R1.3"])}
{sub("A", "Unità 01–09. Dettato. Ascolta e scrivi le frasi.", "3 min", "R1.2")}
<ol style="line-height:1.3">{dal}</ol>
{sub("B", "Unità 04, 06, 08 e 09. Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R1.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: all'ufficio postale</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: al bar</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un'altra cosa da spedire, un altro dolore.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Ogni frase ripassa un'unità, dalla 01 alla 09. Controllare le doppie (<i>attraversavo, riposati, sia</i>) e gli accenti del futuro (<i>resterò</i>).</li>
<li>B: dialogo 1 (Lei): <i>Mi dia</i>, <i>Firmi</i>, <i>Ci vogliono</i> + plurale. Dialogo 2: <i>mal di schiena</i>, <i>non correre</i> (tu negativo), <i>penso che tu abbia</i>. L'audio ha le versioni corrette.</li></ol>""")

    # Page 7: reflect
    cd = [("01", "So comprare vestiti e fare paragoni (più… di)."), ("02", "So raccontare la mia infanzia con l'imperfetto."),
          ("03", "So raccontare un incidente (imperfetto e passato prossimo)."), ("04", "So dare consigli con l'imperativo e i pronomi."),
          ("05", "So chiedere un favore e dire un desiderio (condizionale)."), ("06", "So parlare delle mie capacità (sapere, conoscere)."),
          ("07", "So parlare dei miei progetti con il futuro."), ("08", "So parlare con il Lei in un ufficio."), ("09", "So dare la mia opinione (penso che…).")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Che cosa vuoi ripassare ancora? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>Sei mesi in foto.</b> Scegli tre foto degli ultimi mesi e scrivi un testo (50–75 parole):</p>
<ol><li>che cosa è successo e com'era (passato prossimo e imperfetto);</li><li>un desiderio (mi piacerebbe…);</li><li>un progetto (futuro);</li><li>un'opinione (penso che…).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare le righe «Non ancora» e preparare due brevi attività prima dell'unità 11. Il compito usa la grammatica delle unità 01–09: lo studente può portare le foto e raccontarle a voce nella prossima lezione. Prossima lezione: <b>Unità 11 · Ti va di uscire?</b></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R1.1", "Sei mesi di foto (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R1.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R1.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 10 - Ripasso 1")
