# Speak! Ponte A2 - Ripasso 4 (Unità 29-35), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Ponte"
setup(band="A2 · RIPASSO 4", audio_json=os.path.join(HERE, "audio_it-a2-ripasso-4.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la panchina", "Unità 29"), ("B", "il passaporto", "Unità 30"), ("C", "le torri", "Unità 31"), ("D", "la medaglia", "Unità 32"),
          ("E", "le fedi", "Unità 33"), ("F", "la feijoada", "Unità 34"), ("G", "il pão de queijo", "Unità 35"), ("H", "la Sicilia", "Unità 35")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-ripasso-4"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S43 = lines("R4.1 Conversazione"), lines("R4.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R4.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · RIPASSO 4", "Ripasso 4", "Unità 29–35 · giardino · consigli · storia · sfide · coppie · opinioni · due anni · fine dell'A2",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 29–35 e in tutto l'A2"),
                        ("LINGUA", "voglio che + congiuntivo · dovresti, comprala · il XII secolo · ce la faccio, ci metto · ci siamo conosciuti, mentre · che ne pensi? · da due anni"),
                        ("PRONUNCIA", "dettato di frasi · sulle scale e al bar")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la parola.", "5 min")}
<div class="bank">le fedi · la feijoada · la medaglia · la panchina · il pão de queijo · il passaporto · la Sicilia · le torri</div>
{photo_grid(T, PHOTOS)}""",
    30, """<p>Le foto A–H vengono dalle unità 29–35, in ordine. Chiedere una frase con la grammatica dell'unità: <i>È importante che ci siano panchine nei parchi (29). Il passaporto? Portalo sempre con te! (30). Le torri sono del XII secolo, del Millecento (31). Ce l'ha fatta: ha vinto la medaglia! (32). Si sono sposati nel… (33). La feijoada? Che ne pensi? (34). Studio italiano da… (35). L'anno prossimo vorrei visitare la Sicilia (35).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>29–35</td><td>1</td></tr>
<tr><td>2 Ascolto: la festa di Natale</td><td>10 min</td><td>29–35</td><td>2</td></tr>
<tr><td>3 Grammatica: congiuntivo, consigli, ordinali e secoli, farcela</td><td>10 min</td><td>29–32</td><td>3</td></tr>
<tr><td>4 Grammatica: reciproci e mentre, opinioni e ne, da / fa / tra</td><td>10 min</td><td>33–35</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>29–35</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>8 min</td><td>29–35</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>29–35 e tutto l'A2</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 4 dell'unità (l'unità 35 ha la tabella di tutti i tempi dell'A2).</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Fine settembre: l'inaugurazione del giardino in Bolognina (unità 29). Ottobre: arriva Camila, la nuova vicina brasiliana, e Bruno le dà consigli (30); Bruno fa da guida nella Bologna medievale (31); la prima maratona di Davide, 3 ore e 58 (32). Novembre: un anno di Bruno e Chiara e la storia dei genitori di Camila (33); l'idea del venerdì brasiliano (34) e la prima serata, con l'intervista a Júlia: due anni a Bologna (35). Oggi, sabato 19 dicembre: la festa di Natale al bar; domani Camila torna a Recife per le vacanze. Novità: il ragazzo dell'autobus (unità 33) si chiama Pietro e studia Storia dell'arte.</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>Voglio che vieni</i> → <b>Voglio che venga</b> 2. <i>Dami il numero</i> → <b>Dammi il numero</b> 3. <i>Ce l'ho fatto</i> → <b>Ce l'ho fatta</b> 4. <i>Abbiamo conosciuto a una festa</i> → <b>Ci siamo conosciuti</b> 5. <i>Abito qui per due anni</i> → <b>Abito qui da due anni</b></div>
<div class="box"><h4>AUDIO</h4>Traccia R4.1 Conversazione (lenta e naturale) · Traccia R4.2 Dettato di frasi · Traccia R4.3 Due dialoghi</div>""")

    # Page 2
    topics = [("il viaggio di Camila", True), ("i consigli di Bruno", True), ("quanto dura il viaggio", True), ("Bologna", True), ("il ragazzo dell'autobus", True),
              ("il ritorno a gennaio", True), ("un brindisi", True), ("la maratona di Davide", False)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Camila parte per Recife domani.", "V"), ("Camila è a Bologna da un anno.", "F: da due mesi e mezzo."),
          ("Il consiglio migliore di Bruno: comprare una bici usata.", "V"), ("Per arrivare a Recife Camila ci mette dieci ore.", "F: quasi venti ore, con due voli."),
          ("Secondo Camila, Bologna è perfetta per studiare.", "V"), ("Camila e il ragazzo dell'autobus non si sono parlati.", "F: questa volta si sono parlati."),
          ("Il ragazzo si chiama Pietro.", "V"), ("Camila torna tra tre mesi.", "F: tra tre settimane.")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: la festa di Natale", "10 min")}
<p>Sabato 19 dicembre, la festa di Natale al bar di Giulia. Domani Camila parte per Recife: torna a casa per la prima volta.</p>
{audiocard(["R4.1 · SLOW", "R4.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) sette argomenti. Un argomento è in più.", "3 min", "R4.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R4.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>congiuntivo</td><td>{R("Sono contenta che tu sia qui. · Penso che sia… · Voglio che tu ci racconti…")}</td></tr>
<tr><td>imperativo + pronome</td><td>{R("Comprala usata!")}</td></tr><tr><td>farcela / metterci</td><td>{R("Ci metto quasi venti ore. · Ce la farò!")}</td></tr>
<tr><td>verbo reciproco</td><td>{R("Ci siamo rivisti. · Ci siamo parlati.")}</td></tr><tr><td>da / tra + tempo</td><td>{R("sono a Bologna da due mesi e mezzo · torno tra tre settimane")}</td></tr></table>""",
    24, """<p>A: argomento in più = <span class="red">la maratona di Davide</span> (è nel dialogo 2 della pagina 6). B: lo studente corregge a voce. C: altri esempi: <i>ti consiglio di dormire, dovresti bere</i> (30), <i>che ne pensi?, non ne so molto</i> (34), <i>mentre aspettavo… è arrivato</i> (33), <i>la prima festa</i> (31).</p>""")

    # Page 3
    cg = [("Voglio che tu (venire) ___ alla festa.", ["venga"]), ("È importante che il palco (essere) ___ pronto.", ["sia"]),
          ("Ho paura che domani (piovere) ___.", ["piova"]), ("Sono contenta che voi (essere) ___ qui.", ["siate"])]
    cgl = "".join(f"<li>{fill(s, a, '16mm')}</li>" for s, a in cg)
    cs = [("Il codice fiscale? ", ["Chiedilo", "Lo chiedi"], "Chiedilo", " subito! (a un amico)"), ("Sei stanco: ", ["dovresti", "dovresti di"], "dovresti", " dormire."),
          ("Ti consiglio ", ["di andare", "andare"], "di andare", " presto."), ("", ["Dammi", "Dami"], "Dammi", " il tuo numero!")]
    csl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cs)
    os_ = [("il 3° capitolo → il ___ capitolo", ["terzo"]), ("il XII secolo → il ___", ["Millecento"]), ("il Trecento → il ___ secolo", ["XIV"]),
           ("1088 → ___ 1088", ["nel"])]
    osl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in os_)
    fc = [("Secondo te ce la ___ ? (io, farcela)", ["faccio"]), ("Brava, ce l'hai ___!", ["fatta"]), ("Quanto ___ metti ad arrivare?", ["ci"]),
          ("___ vogliono tre ore.", ["Ci"])]
    fcl = "".join(f"<li>{fill(s, a, '14mm')}</li>" for s, a in fc)
    b.page(f"""{sec(3, "Grammatica: unità 29–32", "10 min")}
<div class="two"><div>{sub("A", "Unità 29. Il congiuntivo.", "3 min")}<ol>{cgl}</ol></div>
<div>{sub("B", "Unità 30. Dare consigli. Scegli.", "2 min")}<ol>{csl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 31. Ordinali, secoli, anni.", "2 min")}<ol>{osl}</ol></div>
<div>{sub("D", "Unità 32. Farcela e metterci.", "3 min")}<ol>{fcl}</ol></div></div>""",
    26, """<ol><li>A: <i>venire → venga, essere → sia / siate, piovere → piova</i>. B: con <i>tu</i> il pronome si attacca (<i>chiedilo</i>); <i>dovresti</i> senza <i>di</i>; <i>ti consiglio di</i>.</li>
<li>C: il secolo è uno in più delle centinaia (1100 → XII). D: <i>ce l'ho fatt<b>a</b></i>; con la persona <i>metterci</i>, senza persona <i>ci vuole / ci vogliono</i>.</li></ol>""")

    # Page 4
    rc = [("(conoscersi) Io e Chiara ___ a una festa.", ["ci siamo conosciuti"]), ("(scriversi) Ogni giorno Bruno e Chiara ___.", ["si scrivevano"]),
          ("(sposarsi) I genitori di Camila ___ dopo sei mesi.", ["si sono sposati"])]
    rcl = "".join(f"<li>{fill(s, a, '30mm')}</li>" for s, a in rc)
    mq = [("Mentre ", ["aspettavo", "ho aspettato"], "aspettavo", " l'autobus, è arrivato Pietro."), ("Quando la musica ", ["è finita", "finiva"], "è finita", ", lui le ha chiesto il numero.")]
    mql = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in mq)
    op = [("Che ___ pensi della mia idea?", ["ne"]), ("Penso che ___ una buona idea. (essere)", ["sia"]), ("Penso ___ fare una festa.", ["di"]), ("Sono d'accordo ___ te.", ["con"])]
    opl = "".join(f"<li>{fill(s, a, '12mm')}</li>" for s, a in op)
    dt = [("Abito a Bologna ___ due anni.", ["da"]), ("Sono arrivata due anni ___.", ["fa"]), ("___ tre settimane torno a Bologna.", ["Tra"])]
    dtl = "".join(f"<li>{fill(s, a, '12mm')}</li>" for s, a in dt)
    mk = [("Voglio che vieni.", "Voglio che venga."), ("Dami il numero.", "Dammi il numero."), ("Ce l'ho fatto!", "Ce l'ho fatta!"),
          ("Abbiamo conosciuto a una festa.", "Ci siamo conosciuti a una festa."), ("Abito qui per due anni.", "Abito qui da due anni.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 33–35", "10 min")}
<div class="two"><div>{sub("A", "Unità 33. I verbi reciproci.", "2 min")}<ol>{rcl}</ol>{sub("B", "Unità 33. Mentre e quando. Scegli.", "1 min")}<ol>{mql}</ol></div>
<div>{sub("C", "Unità 34. Opinioni e ne.", "2 min")}<ol>{opl}</ol>{sub("D", "Unità 35. Da, fa, tra.", "1 min")}<ol>{dtl}</ol></div></div>
{sub("E", "Unità 29–35. Correggi gli errori.", "2 min")}
<ol>{mkl}</ol>""",
    26, """<ol><li>A: reciproci al passato con <i>essere</i> + participio accordato; l'abitudine all'imperfetto (<i>si scrivevano</i>). B: <i>mentre</i> + imperfetto = sfondo; il fatto al passato prossimo.</li>
<li>C: <i>ne</i> = di questo; <i>penso di</i> + infinito, <i>penso che</i> + congiuntivo. D: <i>da</i> + presente se la cosa continua.</li></ol>""")

    # Page 5
    cats = [("Il giardino", "la panchina · l'aiuola · la rastrelliera"), ("La burocrazia", "il modulo · la fila · il codice fiscale"),
            ("La storia", "il secolo · la torre · il portico"), ("Lo sport", "il traguardo · la medaglia · il cronometro")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("inaugurare", "l'inaugurazione"), ("consigliare", "il consiglio"), ("correre", "la corsa"), ("ricordare", "il ricordo"), ("decidere", "la decisione"), ("iscriversi", "l'iscrizione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    df = [("Gli anni dal 1301 al 1400:", "il Trecento"), ("Gli anelli del matrimonio:", "le fedi"), ("La linea di arrivo di una gara:", "il traguardo"),
          ("Il numero per le tasse e i contratti:", "il codice fiscale")]
    dfl = "".join(f"<li>{a} {A(x, 'min-width:24mm')}</li>" for a, x in df)
    od = [("conoscersi · sposarsi · vedersi · svegliarsi", "svegliarsi (non è reciproco)"), ("primo · terzo · undicesimo · undici", "undici (non è ordinale)"),
          ("sono d'accordo · hai ragione · esatto · non è vero", "non è vero (disaccordo)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 29–32. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">l'aiuola · il codice fiscale · il cronometro · la fila · la medaglia · il modulo · la panchina · il portico · la rastrelliera · il secolo · la torre · il traguardo</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 4)}
<div class="two"><div>{sub("C", "Che cos'è?", "1 min")}<ol>{dfl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>B: parole dalle unità 29, 30, 32, 35 e 34. C: unità 31, 33, 32, 30. D: chiedere sempre perché.</p>""")

    # Page 6
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Signora Rossi", "Júlia, a Natale vai in Brasile?", ""), ("Júlia", "No, quest'anno resto qui. Ma spero che i miei genitori vengono in primavera.", "vengano"),
          ("Signora Rossi", "Allora la vigilia vieni da me! Voglio che tu assaggia i miei tortellini.", "assaggi"), ("Júlia", "Volentieri! Che cosa porto?", ""),
          ("Signora Rossi", "Il caffè brasiliano: porta lo, mi raccomando!", "portalo")]
    d2 = [("Marco", "Davide, ti iscrivi alla maratona anche l'anno prossimo?", ""), ("Davide", "Certo! Quest'anno ho messo tre ore e cinquantotto minuti. L'anno prossimo voglio farcelo in tre ore e mezza.", "ci ho messo · farcela"),
          ("Marco", "Secondo me è troppo. Che pensa di questo Giulia?", "Che ne pensa Giulia?"), ("Davide", "Dice che sono matto. Ma mi aiuta sempre!", "")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "8 min")}
{audiocard(["R4.2", "R4.3"])}
{sub("A", "Unità 29–35. Dettato. Ascolta e scrivi le frasi.", "3 min", "R4.2")}
<ol style="line-height:1.3">{dal}</ol>
{sub("B", "Unità 29, 30, 32 e 34. Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R4.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: sulle scale</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: al bar</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un'altra festa, un'altra sfida.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Ogni frase ripassa un'unità, dalla 29 alla 35. Controllare <i>sia</i>, <i>comprarla</i> (pronome attaccato), <i>nell'undicesimo</i>, <i>fatta</i>, <i>da</i>.</li>
<li>B: dialogo 1: <i>vengano, assaggi</i> (29), <i>portalo</i> (30). Dialogo 2: <i>ci ho messo, farcela</i> (32), <i>Che ne pensa</i> (34). L'audio ha le versioni corrette.</li></ol>""")

    # Page 7
    cd = [("29", "So dire che cosa voglio, che cosa è importante, di che cosa ho paura (+ congiuntivo)."), ("30", "So dare consigli (dovresti, ti consiglio di, comprala)."),
          ("31", "So usare ordinali, secoli e date."), ("32", "So dire ce la faccio e quanto tempo ci metto."),
          ("33", "So raccontare come si sono conosciute due persone (mentre, quando)."), ("34", "So chiedere e dare un'opinione (che ne pensi?)."),
          ("35", "So raccontare prima, adesso e dopo (da, fa, tra).")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Hai finito l'A2! Che cosa vuoi ripassare prima del B1? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>Il mio anno.</b> Scrivi una mail a Camila (50–75 parole) e raccontale:</p>
<ol><li>una cosa che hai fatto quest'anno e quanto tempo ci hai messo (<i>ci ho messo…, ce l'ho fatta</i>);</li><li>un consiglio per il suo viaggio (<i>ti consiglio di…, dovresti…</i>);</li><li>che cosa pensi di fare l'anno prossimo (<i>penso di…, vorrei…</i>);</li><li>una cosa che speri (<i>spero che…</i>).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Complimenti: con questo ripasso finisce l'A2 Ponte. Guardare le righe «Non ancora» di questo ripasso e dei ripassi 1–3 e preparare un piano di ripasso personale. Il livello B1 (Progresso) è in preparazione.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R4.1", "La festa di Natale (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R4.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R4.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S43)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 36 - Ripasso 4")
