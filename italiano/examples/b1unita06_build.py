# Speak! Progresso B1 - Unità 06 "Può darsi che…" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 06", audio_json=os.path.join(HERE, "audio_it-b1-unita-06.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-06"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["06.1 Può darsi che..."].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S062 = [x.split(": ", 1)[1] for x in _r["06.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 06", "Può darsi che…", "Ipotesi e pettegolezzi · <b>il congiuntivo passato</b>",
                       [("SAI FARE", "fare ipotesi su un fatto passato, esprimere preoccupazione e certezza, tranquillizzare qualcuno"),
                        ("LINGUA", "Può darsi che abbia perso il telefono. · Spero che non sia successo niente. · Penso di averlo visto."),
                        ("PRONUNCIA", "l'intonazione del dubbio e della certezza")])
    kw = [("chiacchiere sulla vita degli altri", "i pettegolezzi"), ("un'idea su una cosa che non sappiamo con sicurezza", "un'ipotesi"),
          ("essere in ansia per qualcuno", "preoccuparsi"), ("una cosa che nessuno riesce a spiegare", "un mistero"),
          ("il contrario di accendere", "spegnere"), ("discutere in modo arrabbiato", "litigare"),
          ("non ricordare più", "dimenticare"), ("trovare la soluzione", "risolvere")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: chiacchiere al bar", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Guarda la foto. Di che cosa parlano, secondo te?</li><li>Quando un amico non risponde ai messaggi per giorni, che cosa pensi?</li><li>Ti preoccupi facilmente per le persone che ami?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">dimenticare · un'ipotesi · litigare · un mistero · i pettegolezzi · preoccuparsi · risolvere · spegnere</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Ti piacciono i pettegolezzi? Dove se ne sentono di più: al lavoro, in famiglia, sui social?", "1 min")}""",
    25, """<ol><li>A: lasciare parlare lo studente; se dice <i>penso che ha perso</i> o <i>forse abbia</i>, annotarlo: oggi si vede il congiuntivo passato e la differenza con <i>forse</i>.</li>
<li>B: <i>pettegolezzi</i> = <i>fofocas</i>. <i>Spegnere</i> = <i>desligar</i> (≠ <i>slegare</i> = <i>desamarrar</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione su pettegolezzi e preoccupazioni · parole chiave</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Può darsi che… Il mistero di Bruno</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>Il congiuntivo passato · che + congiuntivo o di + infinito</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il congiuntivo passato (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Le espressioni del pettegolezzo · falsi amici · dubbio e certezza</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il messaggio di Chiara · fare ipotesi</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Ipotesi su una foto · gioco di ruolo: un amico sparito</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Giovedì 28 gennaio, sera, al bar di Giulia. Bruno non risponde ai messaggi da tre giorni e Júlia è preoccupata. Le ipotesi: ha perso il telefono (impossibile, «ci dorme insieme»), si è innamorato (ma sta con Chiara da più di un anno), ha litigato con Chiara. Davide pensa di averlo visto martedì in via Zamboni con dei libri; Stefano dice che non è venuto al calcetto. Giulia capisce: gennaio = esami. Bruno arriva stanco ma felice: ha spento il telefono per tre giorni (anzi, l'ha spento Chiara) e ha preso 26 in Storia medievale. Stasera offre lui.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese usa <i>que</i> anche quando il soggetto è lo stesso (<i>acho que vi o Bruno</i>): lo studente dice <i>penso che ho visto</i> invece di <i>penso di aver visto</i>. Con <i>pode ser que tenha perdido</i> il parallelo aiuta (<i>può darsi che abbia perso</i>), ma molti usano l'indicativo. Dopo <i>forse</i> invece serve l'indicativo (<i>forse ha perso</i>), mentre il portoghese usa il subjuntivo (<i>talvez tenha perdido</i>). Falsi amici: <i>desligar</i> → <i>spegnere</i>; <i>desaparecer</i> → <i>sparire</i>; <i>suspeita</i> → <i>sospetto</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Nelle università italiane ci sono tre sessioni d'esame: invernale (gennaio-febbraio), estiva (giugno-luglio) e autunnale (settembre). Lo studente può rifiutare un voto e ripetere l'esame. Il bar sotto casa è il centro delle notizie del quartiere: il barista sa tutto di tutti. <i>Acqua in bocca!</i> = non dirlo a nessuno.</div>
<div class="box"><h4>AUDIO</h4>Traccia 06.1 Può darsi che… (prima naturale, poi lenta) · Traccia 06.2 Ripeti: il congiuntivo passato</div>""")

    # Pagina 2 - Ascolto
    gi = [("il silenzio di Bruno", True), ("il compleanno di Giulia", False), ("il calcetto", True), ("un viaggio a Roma", False), ("gli esami", True), ("Chiara", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Bruno non risponde ai messaggi da una settimana.", "F"), ("Davide pensa di aver visto Bruno martedì.", "V"),
          ("Bruno e Chiara si sono lasciati.", "F"), ("Martedì Bruno non è andato al calcetto.", "V"),
          ("Júlia aveva dimenticato gli esami di Bruno.", "V"), ("All'esame Bruno ha preso ventotto.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Può darsi che…", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["06.1 · NATURAL", "06.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Giovedì sera, al bar di Giulia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "06.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Quali ipotesi fanno gli amici su Bruno? Quale ti sembrava la più probabile? {R("Ha perso il telefono; si è innamorato; ha litigato con Chiara.") if T else ""}</li>
<li>Perché, secondo te, Chiara ha spento il telefono di Bruno? {R("Per farlo studiare senza distrazioni.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Ancora niente? · Succede. · Infatti. · Aspetta un attimo. · Non è che…? · Ecco il mistero risolto. · Cioè… · Promesso. · Offro io.</i></div>""",
    29, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: il silenzio di Bruno, il calcetto, gli esami, Chiara.</li>
<li>B: 1 da tre giorni · 3 stanno ancora insieme, hanno studiato insieme · 6 ventisei.</li>
<li>Espressioni: <i>Non è che ha gli esami?</i> = <i>será que ele não está em provas?</i>: domanda-ipotesi, con l'indicativo.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Spero che non gli <u>sia successo</u> niente.", "congiuntivo passato"), ("Non credo che <u>sia</u> normale.", "congiuntivo presente"),
          ("Può darsi che <u>abbia perso</u> il telefono.", "congiuntivo passato"), ("Penso <u>di averlo visto</u> martedì.", "di + infinito passato"),
          ("Credo <u>di averlo dimenticato</u>.", "di + infinito passato")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:38mm')}</li>" for s, a in ex)
    bank3 = "congiuntivo passato · congiuntivo presente · di + infinito passato"
    rules = [("Il congiuntivo passato si forma con il congiuntivo di", ["avere / essere", "stare / essere"], "avere / essere", "+ participio passato."),
             ("Per un fatto già successo si usa il congiuntivo", ["passato", "presente"], "passato", "."),
             ("Se il soggetto delle due parti è lo stesso, si usa", ["di + infinito", "che + congiuntivo"], "di + infinito", "."),
             ("Dopo <i>forse</i> si usa", ["l'indicativo", "il congiuntivo"], "l'indicativo", ": <i>forse ha perso il telefono</i>.")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".") for a, o, r, z in rules)
    cc = [("Davide pensa", ["di aver visto", "che ha visto"], "di aver visto", "Bruno in via Zamboni."),
          ("È possibile che Bruno", ["sia andato", "è andato"], "sia andato", "in biblioteca."),
          ("Sono contenta", ["che tu abbia passato", "di aver passato"], "che tu abbia passato", "l'esame, Bruno!")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il congiuntivo passato", "8 min")}
{sub("A", "Frasi dal dialogo. Che forma è la parte sottolineata? Usa le parole del riquadro.", "3 min")}
<div class="bank">{bank3}</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la forma giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>congiuntivo presente di avere / essere + participio</b>: <i>abbia perso, sia successo, si sia innamorato</i>. Si usa per un fatto <b>già successo</b> dopo <i>spero, penso, può darsi, è possibile, è strano, sono contento che…</i>. Con lo <b>stesso soggetto</b>: <b>di + infinito</b> (passato: <i>di aver visto, di essere arrivato</i>). Dopo <i>forse</i>: indicativo. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: per ogni frase chiedere: <i>chi pensa? chi ha fatto l'azione? quando?</i> Frasi 4 e 5: io penso, io ho visto → <i>di</i>.</li>
<li>C: frase 3: io sono contenta, tu hai passato → soggetti diversi → <i>che tu abbia passato</i>. <i>Di aver passato</i> vorrebbe dire che l'esame l'ho passato io.</li></ol>""")

    grammar_ref_it.congiuntivo_passato(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["Acqua in bocca!", "Fatti gli affari tuoi!", "Si dice in giro che…", "Me l'ha detto un uccellino.", "Ci metterei la mano sul fuoco.", "Chi lo sa?"]
    rgt = ["Non dico chi me l'ha detto.", "Nessuno lo sa.", "Non dirlo a nessuno!", "Ne sono sicurissimo/a.", "Le persone raccontano che…", "Non sono cose che ti riguardano!"]
    ans = {"Acqua in bocca!": "Non dirlo a nessuno!", "Fatti gli affari tuoi!": "Non sono cose che ti riguardano!", "Si dice in giro che…": "Le persone raccontano che…",
           "Me l'ha detto un uccellino.": "Non dico chi me l'ha detto.", "Ci metterei la mano sul fuoco.": "Ne sono sicurissimo/a.", "Chi lo sa?": "Nessuno lo sa."}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: le parole del pettegolezzo", "4 min")}
{sub("A", "Unisci le espressioni al loro significato.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Sai mantenere un segreto?</li><li>Ci sono pettegolezzi al tuo lavoro?</li><li>Su chi ci metteresti la mano sul fuoco?</li><li>Quando dici «fatti gli affari tuoi»?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Penso che ho visto Bruno.</td><td><b>Penso di aver visto Bruno.</b></td><td>stesso soggetto → <i>di</i> + infinito.</td></tr>
<tr><td>Forse abbia perso il telefono.</td><td><b>Forse ha perso il telefono.</b></td><td><i>forse</i> + indicativo.</td></tr>
<tr><td>Bruno è disparito.</td><td><b>Bruno è sparito / scomparso.</b></td><td><i>desaparecer</i> = <i>sparire</i>.</td></tr>
<tr><td>Ho slegato il telefono.</td><td><b>Ho spento il telefono.</b></td><td><i>slegare</i> = <i>desamarrar</i>.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: dubbio e certezza", "4 min")}
<p class="small" style="margin:.3mm 0">Con un'<b>ipotesi</b> la voce resta sospesa e un po' più lenta (<i>Può darsi che… abbia perso il telefono</i>). Con una <b>certezza</b> la voce scende alla fine, decisa (<i>Ha perso il telefono.</i>).</p>
{audiocard(["06.2"])}
{sub("A", "Ascolta e ripeti. Poi l'insegnante dice una frase con tono sicuro o con tono di dubbio: tu dici quale hai sentito.", "4 min", "06.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S062))}</p>""",
    29, """<ol><li>A: Acqua in bocca c · Fatti gli affari tuoi f · Si dice in giro e · Me l'ha detto un uccellino a · Ci metterei la mano sul fuoco d · Chi lo sa b.</li>
<li>Pronuncia: per il gioco finale usare le stesse frasi, una volta con certezza (<i>Ha perso il telefono.</i>) e una volta con dubbio (<i>Forse… ha perso il telefono?</i>).</li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["di aver esagerato", "che ho esagerato"], "di aver esagerato"), (["ti sia arrabbiata", "ti sei arrabbiata"], "ti sia arrabbiata"),
          (["ha studiato", "abbia studiato"], "ha studiato"), (["abbia dato", "ha dato"], "abbia dato"),
          (["ci abbia visti", "ci ha visti"], "ci abbia visti"), (["di essere", "che sono"], "di essere"),
          (["ha", "abbia"], "ha"), (["veniate", "venite"], "veniate")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Il tuo collega oggi non è venuto al lavoro.", "Può darsi che si sia ammalato."), ("La tua vicina riceve fiori ogni giorno.", "È possibile che abbia un ammiratore."),
          ("Il bar di Giulia stamattina è chiuso.", "Può darsi che Giulia sia andata dal medico."), ("Marco arriva allo studio sorridente.", "È possibile che il cliente abbia approvato il progetto."),
          ("Un tuo amico non risponde da una settimana.", "risposta libera")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:58mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Venerdì mattina Chiara scrive a Júlia. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Chiara:</b> Ciao Júlia! Bruno mi dice che ieri eravate tutti preoccupati: scusami! Penso {p[0]} con il telefono. Spero che tu non {p[1]} con lui: è colpa mia. È vero che in questi giorni {p[2]} tantissimo, e sono contenta che il professore gli {p[3]} ventisei. Davide pensa che abbiamo litigato? Può darsi che qualcuno {p[4]} discutere in biblioteca: era solo una data sbagliata! Credo {p[5]} un po' troppo severa con lui. Forse Bruno {p[6]} ragione: la prossima volta un messaggio a sua sorella glielo lascio mandare! Sabato vi invito a cena da me: spero che {p[7]} tutti!</div>
{sub("B", "Che cosa può essere successo? Fai un'ipotesi con «può darsi che» o «è possibile che».", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: per ogni scelta chiedere: <i>fatto sicuro o ipotesi? stesso soggetto?</i> Gap 3: <i>è vero che</i> → indicativo. Gap 5: <i>ci abbia visti</i>, participio accordato con <i>ci</i> (anche <i>visto</i> è accettabile). Gap 7: <i>forse</i> + indicativo.</li>
<li>B: accettare ogni ipotesi logica; chiedere almeno due ipotesi per frase.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: ipotesi e preoccupazioni", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>fare ipotesi</th><th>essere sicuri</th><th>preoccuparsi</th><th>tranquillizzare</th></tr>
<tr><td><i>Può darsi che… · È possibile che… · Forse… · Non è che…?</i></td><td><i>Sono sicuro/a che… · Ci metterei la mano sul fuoco. · Di sicuro… · Senz'altro.</i></td><td><i>Ho paura che… · Spero che non… · Non è da lui / da lei. · Sono in ansia.</i></td><td><i>Dai, non ti preoccupare. · Succede. · Vedrai che… · Ci sarà una spiegazione.</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Guarda la foto. Prepara per un minuto, poi racconta per due minuti la storia di queste persone.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>chi sono, secondo te?</li><li>che cosa è successo prima? (almeno tre ipotesi)</li><li>dove vanno e perché?</li><li>qual è l'ipotesi più probabile?</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. Un'amica che avete in comune non risponde da giorni. L'insegnante è preoccupato/a: fai ipotesi e tranquillizzalo/a.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Marta non risponde da quattro giorni! · Non è da lei. · Penso di averla vista lunedì con una valigia… · Ho paura che le sia successo qualcosa. · Hai ragione, forse… · Alla fine: Ah, mi ha appena scritto! È in Sardegna con il suo nuovo ragazzo!") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>I pettegolezzi sono sempre negativi?</li><li>È giusto spegnere il telefono per giorni senza avvisare?</li><li>Ti preoccupi di più tu o la tua famiglia quando non rispondi?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>penso che ho…</i> e <i>forse abbia…</i>. Opzione: l'insegnante propone ipotesi assurde e lo studente reagisce (<i>Ma no, non credo che…</i>).</li>
<li>B: le battute dell'insegnante sono in rosso; insistere sulla preoccupazione per far usare le espressioni per tranquillizzare.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare il congiuntivo passato e di + infinito passato.",
          "So fare ipotesi e tranquillizzare qualcuno."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Un mistero risolto.</b> Racconta a un amico una situazione in cui avete fatto tante ipotesi e poi avete scoperto la verità. Prima leggi il messaggio di Giulia a Camila.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Ciao Camila! Ieri sera ti sei persa il mistero della settimana. Bruno non rispondeva da tre giorni e Júlia diceva: «Spero che non gli sia successo niente!». Io ho fatto la prima ipotesi: «Può darsi che abbia perso il telefono». Davide pensava di averlo visto in via Zamboni con dei libri. Poi è arrivata l'ipotesi romantica: «È possibile che si sia innamorato!». Ma no, sta con Chiara da più di un anno! Allora può darsi che abbiano litigato… Alla fine ho capito io: gennaio, università, esami! Bruno è arrivato al bar stanchissimo: aveva spento il telefono per studiare e ha preso ventisei. Sono contenta che sia andato tutto bene, ma credo di aver bevuto troppi caffè per l'ansia! Un bacio, Giulia</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno quattro congiuntivi passati &nbsp;☐ un'ipotesi con <i>può darsi che</i> &nbsp;☐ <i>di</i> + infinito passato (<i>credo di aver…</i>) &nbsp;☐ il finale: la verità &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far notare che nel racconto al passato le ipotesi sono tra virgolette (discorso diretto): il congiuntivo dopo un verbo al passato (<i>pensavo che fosse</i>) arriva nell'unità 12. Prossima unità: <i>Cerco qualcuno che…</i> (il congiuntivo nelle frasi relative).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("06.1", "Può darsi che… (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("06.2", "Ripeti: il congiuntivo passato")}
<p>{" · ".join(S062)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 06 - Può darsi che")
