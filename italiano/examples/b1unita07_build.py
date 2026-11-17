# Speak! Progresso B1 - Unità 07 "Cerco qualcuno che…" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 07", audio_json=os.path.join(HERE, "audio_it-b1-unita-07.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-07"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["07.1 Cerco qualcuno che..."].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S072 = [x.split(": ", 1)[1] for x in _r["07.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 07", "Cerco qualcuno che…", "Annunci · <b>il congiuntivo nelle relative</b>",
                       [("SAI FARE", "capire e scrivere un annuncio, descrivere la persona ideale, fare un colloquio"),
                        ("LINGUA", "Cerco qualcuno che abbia esperienza. · Conosco una ragazza che cerca lavoro."),
                        ("PRONUNCIA", "c dura e c dolce: «cerco», «cerchi», «conosci»")])
    kw = [("un testo per cercare o offrire qualcosa", "un annuncio"), ("un foglio con un avviso sulla porta", "un cartello"),
          ("una persona che vive nella stessa casa", "un coinquilino"), ("quello che sai fare perché l'hai già fatto", "l'esperienza"),
          ("che arriva sempre all'ora giusta", "puntuale"), ("che tiene le cose in ordine", "ordinato"),
          ("le ore di lavoro di una persona: mattina, sera…", "un turno"), ("l'incontro per un posto di lavoro", "un colloquio")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: annunci", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Hai mai risposto a un annuncio di lavoro o di casa? Com'è andata?</li><li>Hai mai avuto un coinquilino? Com'era?</li><li>Che cosa non sopporti in una persona con cui vivi o lavori?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">un annuncio · un cartello · un coinquilino · un colloquio · l'esperienza · ordinato · puntuale · un turno</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Dove si cercano lavoro e casa in Brasile: siti, social, amici, cartelli?", "1 min")}""",
    25, """<ol><li>A: lasciare parlare lo studente; annotare se dice <i>cerco qualcuno che ha…</i>: alla pagina 3 si scopre il congiuntivo nelle relative.</li>
<li>B: <i>coinquilino</i> = <i>colega de apartamento</i>; <i>colloquio</i> = <i>entrevista de emprego</i> (l'<i>intervista</i> è quella dei giornalisti).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione su lavoro, casa e coinquilini · parole chiave</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Cerco qualcuno che… Due annunci al bar di Giulia</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>Il congiuntivo nelle frasi relative · indicativo o congiuntivo?</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il congiuntivo nelle relative e la lingua degli annunci (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Le parole degli annunci · falsi amici · c dura e c dolce</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>L'annuncio di Bruno · la mia persona ideale</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Il lavoro ideale · gioco di ruolo: colloquio al bar di Giulia</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Martedì 2 febbraio, mattina. Sulla porta del bar c'è il cartello «Cercasi barista»: da marzo Giulia apre anche la sera con l'aperitivo. Júlia e Bruno l'aiutano a scrivere l'annuncio online: qualcuno che abbia esperienza, che sappia fare un cappuccino come si deve, che parli un po' d'inglese e soprattutto che sia puntuale. Davide conosce Elena, una compagna di ingegneria che d'estate ha fatto la barista a Rimini: Giulia vuole vederla domani mattina. Anche Bruno scrive un annuncio: a marzo Paolo parte per l'Erasmus e lui cerca un coinquilino che non fumi, non faccia feste e lavi i piatti. Giulia: «Tu cerchi un coinquilino che ti faccia il caffè, io un barista: siamo uguali!»</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese ha la stessa regola (<i>procuro alguém que tenha</i>), ma nel parlato spesso si usa l'indicativo (<i>que tem</i>): lo studente dice <i>cerco qualcuno che ha</i>. Errore opposto per ipercorrezione: <i>conosco una ragazza che cerchi</i>. Falsi amici: <i>entrevista</i> → <i>colloquio</i>; <i>esperto</i> (sveglio, furbo) ≠ <i>esperto</i> (che sa molto di una cosa); <i>currículo</i> → <i>curriculum, CV</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>L'Università di Bologna è una delle università europee con più studenti Erasmus, in entrata e in uscita. Molti giovani lavorano con contratti a tempo determinato o part-time nei bar e nei ristoranti. Nei negozi italiani si vedono ancora spesso i cartelli <i>Cercasi personale</i>, e per un posto da barista il colloquio si fa direttamente al bancone. L'aperitivo serale (dalle 18 alle 21 circa) è un momento importante per i bar di Bologna.</div>
<div class="box"><h4>AUDIO</h4>Traccia 07.1 Cerco qualcuno che… (prima naturale, poi lenta) · Traccia 07.2 Ripeti: il congiuntivo nelle relative</div>""")

    # Pagina 2 - Ascolto
    gi = [("un annuncio per il bar", True), ("un nuovo lavoro per Júlia", False), ("l'aperitivo serale", True), ("una ragazza che cerca lavoro", True), ("una festa a casa di Bruno", False), ("un coinquilino per Bruno", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Giulia cerca un barista perché da marzo apre anche la sera.", "V"), ("Per Giulia la cosa più importante è che il barista sia simpatico.", "F"),
          ("L'ultimo barista arrivava sempre in ritardo.", "V"), ("Elena ha già lavorato come barista.", "V"),
          ("Bruno cerca un coinquilino perché Paolo va a vivere con la ragazza.", "F"), ("Paolo lavava sempre i piatti.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Cerco qualcuno che…", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["07.1 · NATURAL", "07.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Martedì mattina, al bar di Giulia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "07.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Perché Júlia consiglia a Bruno di scrivere «una persona tranquilla e ordinata»? {R("È più gentile e positivo di una lista di divieti.") if T else ""}</li>
<li>Giulia dice: «Siamo uguali!». Perché? {R("Tutti e due cercano qualcuno che faccia il caffè.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Cercasi… · Mi aiutate? · come si deve · Già che ci siamo… · Davvero? · Mandamela domani! · Questo però non lo scriviamo! · Siamo uguali!</i></div>""",
    29, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: annuncio per il bar, aperitivo serale, ragazza che cerca lavoro, coinquilino per Bruno.</li>
<li>B: 2 la cosa più importante è che sia puntuale · 5 Paolo parte per l'Erasmus · 6 non li ha mai lavati.</li>
<li>Espressioni: <i>come si deve</i> = <i>como deve ser, direito</i>; <i>già che ci siamo</i> = <i>já que estamos aqui</i>.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Cerco qualcuno che <u>abbia</u> un po' di esperienza.", "congiuntivo"), ("Conosco una ragazza che <u>cerca</u> un lavoro serale.", "indicativo"),
          ("Non voglio uno che <u>stia</u> tutto il giorno al telefono.", "congiuntivo"), ("Non c'è nessuno che <u>lavi</u> i piatti volentieri.", "congiuntivo"),
          ("Conosco una persona che li <u>lava</u> benissimo.", "indicativo")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:26mm')}</li>" for s, a in ex)
    rules = [("Per una persona reale, che conosco, si usa", ["l'indicativo", "il congiuntivo"], "l'indicativo", "."),
             ("Per una persona ideale, che cerco e forse non esiste, si usa", ["il congiuntivo", "l'indicativo"], "il congiuntivo", "."),
             ("Dopo <i>non c'è nessuno che</i> si usa", ["il congiuntivo", "l'indicativo"], "il congiuntivo", "."),
             ("<i>Cercasi barista</i> vuol dire", ["si cerca un barista", "un barista cerca lavoro"], "si cerca un barista", ".")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" .", ".") for a, o, r, z in rules)
    cc = [("Nel nostro studio abbiamo una stagista che", ["parla", "parli"], "parla", "tre lingue."),
          ("Vorrei una casa che", ["abbia", "ha"], "abbia", "un balcone."),
          ("Non ho trovato nessuna stanza che", ["costi", "costa"], "costi", "meno di 400 euro.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il congiuntivo nelle relative", "8 min")}
{sub("A", "Frasi dal dialogo. Il verbo sottolineato è all'indicativo o al congiuntivo?", "3 min")}
<div class="bank">indicativo · congiuntivo</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la forma giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Dopo <i>che</i> relativo: <b>indicativo</b> per una persona o una cosa <b>reale</b> (<i>conosco una ragazza che <b>cerca</b> lavoro</i>); <b>congiuntivo</b> per una persona o una cosa <b>ideale</b>, cercata, che forse non esiste (<i>cerco qualcuno che <b>abbia</b> esperienza · non c'è nessuno che <b>lavi</b> i piatti</i>). Negli annunci: <i>cercasi, affittasi, vendesi</i>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: per ogni frase chiedere: <i>questa persona esiste? la conosci?</i> Se sì → indicativo.</li>
<li>C: frase 1: la stagista esiste (<i>abbiamo</i>) → indicativo. Frase 3: <i>nessuna stanza</i> → congiuntivo.</li></ol>""")

    grammar_ref_it.congiuntivo_relative(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["ammobiliato", "spese incluse", "a tempo determinato", "le referenze", "la caparra", "la retribuzione"]
    rgt = ["con una data di fine", "lo stipendio", "con i mobili", "i soldi lasciati all'inizio come garanzia", "luce, gas e acqua nel prezzo", "informazioni da un ex datore di lavoro"]
    ans = {"ammobiliato": "con i mobili", "spese incluse": "luce, gas e acqua nel prezzo", "a tempo determinato": "con una data di fine",
           "le referenze": "informazioni da un ex datore di lavoro", "la caparra": "i soldi lasciati all'inizio come garanzia", "la retribuzione": "lo stipendio"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: le parole degli annunci", "4 min")}
{sub("A", "Unisci le parole degli annunci alle definizioni.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Preferisci una casa ammobiliata o vuota?</li><li>Hai mai avuto un contratto a tempo determinato?</li><li>In Brasile si lascia una caparra per una casa?</li><li>Chi ti darebbe delle buone referenze?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Cerco qualcuno che ha esperienza.</td><td><b>Cerco qualcuno che abbia esperienza.</b></td><td>persona ideale → congiuntivo.</td></tr>
<tr><td>Domani ho un'intervista per il bar.</td><td><b>Domani ho un colloquio per il bar.</b></td><td><i>intervista</i> = dei giornalisti.</td></tr>
<tr><td>Bruno è esperto: trova sempre una soluzione.</td><td><b>Bruno è sveglio / furbo.</b></td><td><i>esperto</i> = che conosce bene un settore.</td></tr>
<tr><td>Conosco una ragazza che cerchi lavoro.</td><td><b>Conosco una ragazza che cerca lavoro.</b></td><td>persona reale → indicativo.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: c dura e c dolce", "4 min")}
<p class="small" style="margin:.3mm 0"><b>c</b> + <i>a, o, u</i> e <b>ch</b> + <i>e, i</i> = suono duro [k]: <i>cerco, cerchi, cerchiamo</i>. <b>c</b> + <i>e, i</i> = suono dolce [tʃ]: <i><b>c</b>ercasi, <b>c</b>inque</i>. <b>sc</b> + <i>e, i</i> = [ʃ]: <i>cono<b>sc</b>i</i>, ma <i>cono<b>sc</b>o</i> = [sk].</p>
{audiocard(["07.2"])}
{sub("A", "Ascolta e ripeti. Poi leggi ad alta voce: cerco · cerchi · cercasi · conosco · conosci · cuoco · cuochi · amiche · amici.", "4 min", "07.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S072))}</p>""",
    29, """<ol><li>A: ammobiliato c · spese incluse e · a tempo determinato a · le referenze f · la caparra d · la retribuzione b.</li>
<li>Pronuncia: errore tipico: <i>conosci</i> letto [konoski]; <i>cerchi</i> letto [tʃerʃi]. Far notare che al plurale l'ortografia cambia per tenere il suono: <i>cuoco → cuochi</i>, ma <i>amico → amici</i>.</li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["studi", "studia"], "studi"), (["lavori", "lavora"], "lavori"), (["fumi", "fuma"], "fumi"), (["sia", "è"], "sia"),
          (["gioco", "giochi"], "gioco"), (["è", "sia"], "è"), (["ha", "abbia"], "ha"), (["faccia", "fa"], "faccia")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Cerco un lavoro che…", "es. mi permetta di viaggiare"), ("Vorrei un capo che…", "es. sia flessibile"),
          ("Non c'è nessuno nella mia famiglia che…", "es. sappia cucinare come mia nonna"), ("Ho bisogno di un coinquilino che…", "es. non faccia rumore"),
          ("Conosco una persona che…", "indicativo: es. parla cinque lingue"), ("Mi serve una casa che…", "es. abbia un giardino")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:58mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Leggi l'annuncio di Bruno e scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>AFFITTASI STANZA SINGOLA – via Zamboni, Bologna.</b> Da marzo, in un appartamento per due persone. Cerco un coinquilino o una coinquilina che {p[0]} all'Unibo o che {p[1]} a Bologna, che non {p[2]} e che {p[3]} tranquillo/a e ordinato/a. Io mi chiamo Bruno, studio Storia e {p[4]} a calcetto il martedì. La stanza {p[5]} luminosa e {p[6]} un tappeto blu e una lampada verde. Nel palazzo non c'è nessuno che {p[7]} rumore la sera. 380 € al mese, spese incluse. È gradita la conoscenza del caffè brasiliano! Astenersi perditempo.</div>
{sub("B", "La tua persona o la tua cosa ideale. Completa le frasi.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: gap 1-4 e 8: la persona cercata o inesistente → congiuntivo. Gap 5-7: Bruno e la stanza esistono → indicativo. Il tappeto blu e la lampada verde sono quelli comprati al mercatino nell'unità A1 34.</li>
<li>B: frase 5: attenzione, <i>conosco</i> → indicativo. Chiedere sempre «perché?» per allungare la risposta.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: annunci e colloqui", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>dire che cosa cerchi</th><th>i requisiti</th><th>chiedere informazioni</th><th>presentarsi</th></tr>
<tr><td><i>Cerco qualcuno che… · Ho bisogno di una persona che… · L'ideale sarebbe…</i></td><td><i>È richiesta esperienza. · È importante che… · È gradito/a… · Non è necessario che…</i></td><td><i>Quali sono gli orari? · Com'è lo stipendio? · È a tempo determinato? · Le spese sono incluse?</i></td><td><i>Ho visto il Suo annuncio. · Ho esperienza come… · Sono una persona… · Sono disponibile da…</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi parla per due minuti del tuo lavoro ideale (o del tuo coinquilino ideale).", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>che cosa fai e dove</li><li>orari e stipendio</li><li>come sono il capo e i colleghi</li><li>che cosa non vuoi assolutamente</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. Hai letto l'annuncio di Giulia e fai il colloquio per il posto di barista. L'insegnante è Giulia.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante (Giulia): Buongiorno, si accomodi. · Ha esperienza come barista? · Cerco qualcuno che possa lavorare il sabato sera: Lei può? · Parla inglese? · Come si prepara un buon cappuccino? · Ha domande per me? · Bene, Le faccio sapere entro venerdì.") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>È meglio vivere da soli o con dei coinquilini?</li><li>In un colloquio conta di più l'esperienza o la personalità?</li><li>Esiste il lavoro perfetto, secondo te?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>che ha / che sa</i> al posto di <i>che abbia / che sappia</i>.</li>
<li>B: le battute dell'insegnante sono in rosso; registro formale (<i>Lei</i>). Poi scambiare i ruoli: lo studente è Giulia e cerca un barista.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So scegliere tra indicativo e congiuntivo nelle frasi relative.",
          "So capire e scrivere un annuncio."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Un annuncio.</b> Scrivi un annuncio: cerchi un collega, un coinquilino, un insegnante o un servizio. Prima leggi l'annuncio finale di Giulia.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i><b>CERCASI BARISTA – Bar Giulia, centro di Bologna.</b> Da marzo il nostro bar apre anche la sera con l'aperitivo e cerchiamo una persona dinamica e sorridente che possa lavorare cinque sere a settimana, dal mercoledì alla domenica, dalle 17 alle 23. Cerchiamo qualcuno che abbia almeno un po' di esperienza, che sappia preparare un buon cappuccino e i cocktail più semplici e che parli un po' d'inglese. È importante che sia puntuale e che ami il contatto con le persone. Offriamo un contratto part-time di sei mesi, con possibilità di rinnovo, e un ambiente familiare. È gradita la conoscenza di altre lingue. Passate al bar con il curriculum, la mattina dalle 9 alle 11. Astenersi perditempo!</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno quattro relative con il congiuntivo &nbsp;☐ un'espressione degli annunci (<i>cercasi, è gradito, si richiede</i>) &nbsp;☐ orari o prezzo &nbsp;☐ come rispondere &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far sottolineare nel modello le relative (<i>che possa, che abbia, che sappia, che parli</i>) e notare <i>è importante che sia</i> (unità 05). Prossima unità: <i>Mica male!</i> (la negazione rafforzata).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("07.1", "Cerco qualcuno che… (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("07.2", "Ripeti: il congiuntivo nelle relative")}
<p>{" · ".join(S072)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 07 - Cerco qualcuno che")
