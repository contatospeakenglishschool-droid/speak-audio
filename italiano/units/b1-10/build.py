# Speak! Progresso B1 - Ripasso 1 (Unità 01-09), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Progresso"
setup(band="B1 · RIPASSO 1", audio_json=os.path.join(HERE, "audio_it-b1-ripasso-1.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "le chiavi", "Unità 02"), ("B", "la macchia", "Unità 03"), ("C", "la camomilla", "Unità 04"), ("D", "l'aceto balsamico", "Unità 05"),
          ("E", "la biblioteca", "Unità 06"), ("F", "il cappuccino", "Unità 07"), ("G", "la mensa", "Unità 08"), ("H", "la maschera", "Unità 09")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-ripasso-1"]
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

    # Pagina 1
    cover = cover_html(T, "LIVELLO B1 · RIPASSO 1", "Ripasso 1", "Unità 01–09 · il primo blocco del B1",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 01–09"),
                        ("LINGUA", "trapassato · te lo do · avrei dovuto · me ne vado · congiuntivo · mica · da + infinito"),
                        ("PRONUNCIA", "dettato di frasi · al telefono e al bar")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la grammatica di quell'unità.", "5 min")}
<div class="bank">l'aceto balsamico · la biblioteca · la camomilla · il cappuccino · le chiavi · la macchia · la maschera · la mensa</div>
{photo_grid(T, PHOTOS)}""",
    30, """<p>Le foto A–H vengono dalle unità 02–09, in ordine (l'unità 01 torna nell'ascolto e nella grammatica). Esempi: <i>Le chiavi? Te le do domani (02). Avrei dovuto togliere subito la macchia (03). Non te la prendere: bevi una camomilla (04). È importante che l'aceto sia DOP (05). Può darsi che Bruno sia andato in biblioteca (06). Cerco qualcuno che sappia fare il cappuccino (07). La mensa non è mica cara (08). Una maschera da comprare a Venezia (09).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>02–09</td><td>1</td></tr>
<tr><td>2 Ascolto: ritorno da Venezia</td><td>12 min</td><td>01–09</td><td>2</td></tr>
<tr><td>3 Grammatica: trapassato, pronomi combinati, condizionale passato, verbi pronominali</td><td>10 min</td><td>01–04</td><td>3</td></tr>
<tr><td>4 Grammatica: congiuntivo, relative, negazione, da + infinito</td><td>12 min</td><td>05–09</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>01–09</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>9 min</td><td>01–09</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>01–09</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano e usi i registri «I miei errori» delle unità 01–09. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 4 dell'unità.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Gennaio: Camila torna da Recife (01); Júlia parte per Milano e lascia chiavi, bici e vestito agli amici (02); al ritorno, i piccoli disastri del fine settimana: il vestito macchiato, il portafoglio di Pietro, Bruno bagnato (03); il cliente vuole cambiare tutto e Júlia ha una giornataccia (04); gita a Modena, all'acetaia (05); il mistero di Bruno, sparito per gli esami (06). Febbraio: Giulia cerca un barista e Bruno un coinquilino (07); la visita di Tommaso (08); martedì grasso e il granchio di Júlia con i biglietti per Venezia (09). Oggi, lunedì 15 febbraio: tutte le novità al bar. Elena sarà la nuova barista, Tommaso il coinquilino di Bruno, Camila ha avuto il tirocinio, il vestito è di nuovo pulito.</div>
<div class="box"><h4>I 6 ERRORI DA CONTROLLARE</h4>1. <i>Ha detto che verrebbe</i> → <b>sarebbe venuto</b> 2. <i>Mi ne vado</i> → <b>Me ne vado</b> 3. <i>Penso che è</i> → <b>Penso che sia</b> 4. <i>Penso che ho visto</i> → <b>Penso di aver visto</b> 5. <i>Anche io no</i> → <b>Neanch'io</b> 6. <i>Qualcosa per bere</i> → <b>Qualcosa da bere</b></div>
<div class="box"><h4>AUDIO</h4>Traccia R1.1 Conversazione (naturale e lenta) · Traccia R1.2 Dettato di frasi · Traccia R1.3 Due dialoghi</div>""")

    # Pagina 2
    topics = [("il viaggio a Venezia", True), ("il tirocinio di Camila", True), ("la nuova barista", True), ("il nuovo coinquilino di Bruno", True), ("il vestito nero", True),
              ("San Valentino", True), ("un caffè offerto", True), ("il progetto di Milano", False)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("A Venezia c'erano moltissimi turisti.", "F: erano già partiti quasi tutti."), ("Júlia non ha controllato la data dei biglietti.", "V"),
          ("Camila comincia il tirocinio a marzo.", "V"), ("La nuova barista è un'amica di Davide.", "V"),
          ("Tommaso ha detto di no a Bruno.", "F: ha detto di sì."), ("La macchia sul vestito c'è ancora.", "F: non c'è più."),
          ("Per San Valentino Pietro ha aspettato Camila alla stazione.", "V"), ("Júlia ha festeggiato San Valentino al ristorante.", "F: in treno, con un panino.")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: ritorno da Venezia", "12 min")}
<p>Lunedì 15 febbraio, mattina. Al bar di Giulia, Júlia e Camila raccontano il fine settimana a Venezia.</p>
{audiocard(["R1.1 · NATURAL", "R1.1 · SLOW"])}
{sub("A", "Ascolta la versione naturale. Di che cosa parlano? Segna (✓) sette argomenti. Un argomento è in più.", "3 min", "R1.1 · NATURAL")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "4 min")}
<table style="table-layout:fixed"><tr><td>trapassato prossimo (01)</td><td>{R("i turisti erano già partiti")}</td></tr>
<tr><td>pronomi combinati (02)</td><td>{R("Te l'avevo detto! · Gliel'ho promesso. · Me l'hanno ridato.")}</td></tr>
<tr><td>condizionale passato (03)</td><td>{R("Avrei dovuto controllare. · Pensavo che sarebbe rimasto macchiato.")}</td></tr>
<tr><td>verbo pronominale (04)</td><td>{R("Non te la prendere. · Ce l'avete fatta.")}</td></tr>
<tr><td>congiuntivo (06–07)</td><td>{R("Può darsi che impari… · Non c'è nessuno che faccia…")}</td></tr>
<tr><td>mica / da + infinito (08–09)</td><td>{R("Mica male! · Un ragazzo da sposare!")}</td></tr></table>""",
    24, """<p>A: argomento in più = <span class="red">il progetto di Milano</span> (è nel dialogo 1 della pagina 6). B: lo studente corregge a voce. C: accettare anche <i>non me ne parlare</i> (04) e <i>mi hanno presa</i> (accordo del participio con il pronome, 02).</p>""")

    # Pagina 3
    tp = [("Quando siamo arrivate, i turisti (partire) ___ già.", ["erano partiti"]), ("Non ho mangiato perché (pranzare) ___ prima.", ["avevo pranzato"]),
          ("Camila mi ha detto che (perdere) ___ il treno.", ["aveva perso"])]
    tpl = "".join(f"<li>{fill(s, a, '24mm')}</li>" for s, a in tp)
    pc = [("Le chiavi? ___ do domani. (a te)", ["Te le"]), ("Il libro? ___ ho dato ieri. (a lei)", ["Gliel'"]), ("Il caffè? ___ porto due pacchetti. (a voi, ne)", ["Ve ne"])]
    pcl = "".join(f"<li>{fill(s, a, '14mm')}</li>" for s, a in pc)
    cp = [("Ieri ", ["avrei dovuto", "dovrei"], "avrei dovuto", " prenotare."), ("Ha detto che ", ["sarebbe venuto", "verrebbe"], "sarebbe venuto", " alle otto."),
          ("Al posto tuo ", ["mi sarei arrabbiata", "mi avrei arrabbiata"], "mi sarei arrabbiata", ".")]
    cpl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cp)
    vp = [("È tardi: ___ vado. (andarsene)", ["me ne"]), ("Non ___ prendere! (prendersela, tu)", ["te la"]), ("All'esame Davide ___ è cavata bene.", ["se l'"]),
          ("Sono stanca: non ___ faccio più. (farcela)", ["ce la"])]
    vpl = "".join(f"<li>{fill(s, a, '14mm')}</li>" for s, a in vp)
    b.page(f"""{sec(3, "Grammatica: unità 01–04", "10 min")}
<div class="two"><div>{sub("A", "Unità 01. Il trapassato prossimo.", "3 min")}<ol>{tpl}</ol></div>
<div>{sub("B", "Unità 02. I pronomi combinati.", "2 min")}<ol>{pcl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 03. Il condizionale passato. Scegli.", "2 min")}<ol>{cpl}</ol></div>
<div>{sub("D", "Unità 04. I verbi pronominali.", "3 min")}<ol>{vpl}</ol></div></div>""",
    26, """<ol><li>A: trapassato = l'azione prima di un'altra azione passata. B: <i>mi, ti, ci, vi → me, te, ce, ve</i>; <i>gli / le → glie-</i>; <i>ne</i> con le quantità.</li>
<li>C: futuro nel passato → condizionale <b>passato</b>; <i>arrabbiarsi</i> → <i>essere</i>. D: <i>prendersela</i> e <i>cavarsela</i> al passato con <i>essere</i> (<i>se l'è cavata</i>); <i>farcela</i> con <i>avere</i>.</li></ol>""")

    # Pagina 4
    cg = [("Spero che il pacco (arrivare) ___ presto.", ["arrivi"]), ("È importante che voi lo (sapere) ___.", ["sappiate"]), ("So che il parmigiano (venire) ___ da Parma.", ["viene"])]
    cgl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in cg)
    cs = [("Può darsi che Bruno ", ["abbia perso", "ha perso"], "abbia perso", " il telefono."), ("Penso ", ["di aver visto", "che ho visto"], "di aver visto", " Bruno martedì."),
          ("Forse ", ["è andato", "sia andato"], "è andato", " in biblioteca.")]
    csl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in cs)
    rl = [("Cerco qualcuno che ", ["sappia", "sa"], "sappia", " cucinare."), ("Conosco una ragazza che ", ["cerca", "cerchi"], "cerca", " lavoro.")]
    rll = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in rl)
    ng = [("Non fumo. — ___ (eu também não)", ["Neanch'io"]), ("La stanza non è ___ piccola.", ["mica"]), ("Hai sete? Vuoi qualcosa ___ bere?", ["da"])]
    ngl = "".join(f"<li>{fill(s, a, '18mm')}</li>".replace("(eu também não)", "(= anch'io non fumo)") for s, a in ng)
    mk = [("Ha detto che verrebbe.", "Ha detto che sarebbe venuto."), ("Mi ne vado.", "Me ne vado."), ("Penso che è una buona idea.", "Penso che sia una buona idea."),
          ("Cerco qualcuno che ha esperienza.", "Cerco qualcuno che abbia esperienza."), ("Anche io no.", "Neanch'io."), ("Una città per vedere.", "Una città da vedere.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 05–09", "12 min")}
<div class="two"><div>{sub("A", "Unità 05. Il congiuntivo presente.", "2 min")}<ol>{cgl}</ol>{sub("B", "Unità 06. Ipotesi. Scegli.", "2 min")}<ol>{csl}</ol></div>
<div>{sub("C", "Unità 07. Le relative. Scegli.", "1 min")}<ol>{rll}</ol>{sub("D", "Unità 08 e 09. Completa.", "2 min")}<ol>{ngl}</ol></div></div>
{sub("E", "Unità 01–09. Correggi gli errori.", "3 min")}
<ol style="column-count:2">{mkl}</ol>""",
    26, """<ol><li>A: <i>so che</i> = fatto sicuro → indicativo. B: <i>forse</i> + indicativo; stesso soggetto → <i>di</i> + infinito passato. C: persona ideale → congiuntivo; persona reale → indicativo.</li>
<li>D: <i>neanch'io</i>; <i>mica</i> dopo il verbo con <i>non</i>; <i>qualcosa da</i> + infinito. E: chiedere allo studente quale unità ripassa ogni frase.</li></ol>""")

    # Pagina 5
    cats = [("Il lavoro", "il capo · consegnare · un colloquio · un turno"), ("Le emozioni", "vergognarsi · prendersela · sfogarsi · preoccuparsi"),
            ("La casa", "il coinquilino · il riscaldamento · ammobiliato · la caparra"), ("Il cibo", "le sfrappole · l'acetaia · assaggiare · la mensa")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("prenotare", "la prenotazione"), ("modificare", "la modifica"), ("spedire", "la spedizione"), ("preoccuparsi", "la preoccupazione"),
          ("annunciare", "l'annuncio"), ("sorridere", "il sorriso")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    md = [("Lo dici prima di un esame:", "In bocca al lupo!"), ("Hai sbagliato:", "Ho preso un granchio."), ("Non dirlo a nessuno:", "Acqua in bocca!"),
          ("È costato moltissimo:", "Un occhio della testa.")]
    mdl = "".join(f"<li>{a} {A(x, 'min-width:30mm')}</li>" for a, x in md)
    od = [("squisito · buonissimo · delizioso · strano", "strano (non è positivo)"), ("mica · affatto · neanche · infatti", "infatti (non nega)"),
          ("cercasi · affittasi · vendesi · chiamasi", "chiamasi (non si usa negli annunci)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 01–09. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">l'acetaia · ammobiliato · assaggiare · il capo · la caparra · il coinquilino · un colloquio · consegnare · la mensa · preoccuparsi · prendersela · il riscaldamento · le sfrappole · sfogarsi · un turno · vergognarsi</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}
<div class="two"><div>{sub("C", "Unità 06 e 09. Che cosa dici?", "1 min")}<ol>{mdl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>B: parole dalle unità 03, 04, 05, 06, 07 e 08. C: modi di dire delle unità 06 e 09. D: chiedere sempre perché (<i>squisito ≠ esquisito</i>, unità 05).</p>""")

    # Pagina 6
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Marco", "Júlia, il cliente di Milano ha risposto?", ""), ("Júlia", "Sì, ha detto che le modifiche gli sono piaciute. Pensavo che si lamenterebbe ancora.", "si sarebbe lamentato"),
          ("Marco", "Hai visto? Ti avevi preoccupata per niente.", "Ti eri preoccupata"), ("Júlia", "Hai ragione. Ma la prossima volta il progetto lo gli mandi tu!", "glielo mandi")]
    d2 = [("Davide", "Allora, Tommaso viene a vivere da te?", ""), ("Bruno", "Sì, da marzo. Sono contento che ha detto di sì.", "abbia detto"),
          ("Davide", "E Paolo? Gli dispiace andarse?", "andarsene"), ("Bruno", "Per niente! Non vede il momento di partire per l'Erasmus.", "non vede l'ora"),
          ("Davide", "Beato lui!", "")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "9 min")}
{audiocard(["R1.2", "R1.3"])}
{sub("A", "Unità 01–09. Dettato. Ascolta e scrivi le frasi.", "4 min", "R1.2")}
<ol style="line-height:1.25;column-count:1">{dal}</ol>
{sub("B", "Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R1.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 1: al telefono</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.5"><b style="color:{TEAL}">Dialogo 2: al bar</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un altro cliente, un altro coinquilino.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase; ogni frase ripassa un'unità, dalla 01 alla 09, in ordine.</li>
<li>B: dialogo 1: futuro nel passato (03), <i>preoccuparsi</i> al trapassato con <i>essere</i> (01), <i>glielo</i> (02). Dialogo 2: <i>sono contento che</i> + congiuntivo passato (06), <i>andarsene</i> (04), <i>non vedere l'ora</i> (09). L'audio ha le versioni corrette.</li></ol>""")

    # Pagina 7
    cd = [("01", "So raccontare che cosa era successo prima (trapassato)."), ("02", "So prestare e chiedere cose con i pronomi combinati."),
          ("03", "So parlare di rimpianti e del futuro nel passato."), ("04", "So usare andarsene, prendersela, cavarsela, avercela, farcela."),
          ("05", "So usare il congiuntivo presente con tutte le persone."), ("06", "So fare ipotesi (può darsi che + congiuntivo passato)."),
          ("07", "So descrivere la persona o la cosa che cerco."), ("08", "So usare mica, affatto, neanche."), ("09", "So spiegare un modo di dire e usare da + infinito.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck" style="font-size:8.4pt"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Rileggi i tuoi registri «I miei errori»: quali errori fai ancora? Scrivi due cose da migliorare.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p><b>Le mie ultime settimane.</b> Scrivi una mail a un amico italiano e raccontagli le tue ultime settimane:</p>
<ol style="line-height:1.4"><li>una cosa che non avevi mai fatto prima (<i>non avevo mai…</i>);</li><li>un piccolo rimpianto (<i>avrei dovuto…</i>) e una giornata storta (<i>me la sono presa…</i>);</li><li>una notizia che speri (<i>spero che…</i>) e un'ipotesi (<i>può darsi che…</i>);</li><li>una cosa da fare presto (<i>ho tanto da…</i>) e un modo di dire che hai imparato.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare con lo studente le righe «Non ancora» e decidere che cosa ripassare (pagina 4 dell'unità corrispondente). Prossima unità: <b>B1 11, Comunicare a distanza</b> (il congiuntivo imperfetto), inizio del secondo blocco.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R1.1", "Ritorno da Venezia (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R1.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R1.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 10 - Ripasso 1")
