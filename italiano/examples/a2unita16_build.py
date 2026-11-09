# Speak! Ponte A2 - Unità 16 "La città che vorrei" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 16", audio_json=os.path.join(HERE, "audio_it-a2-unita-16.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la piazza", "piazza"), ("B", "la pista ciclabile", "pista"), ("C", "la panchina", "panchina"), ("D", "la biblioteca", "biblioteca"),
          ("E", "il marciapiede", "marciapiede"), ("F", "l'ufficio postale", "ufficio"), ("G", "il parco giochi", "parco"), ("H", "la fermata dell'autobus", "fermata")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-16"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["16.1 Testi e dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
TEXTS = SCRIPT[1:4]
S162 = [x.split(": ", 1)[1] for x in _r["16.2 Ripeti"].split("\n")]
S163 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["16.3 Che, chi, cui o qui"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split(" ", 1)[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 16", "La città che vorrei", "Luoghi e servizi della città · <b>che · cui (in cui, con cui, di cui…)</b>",
                       [("SAI FARE", "leggere brevi opinioni, descrivere luoghi e servizi, dire come vorresti il tuo quartiere"),
                        ("LINGUA", "la città che vorrei · un ufficio che apre il pomeriggio · la via in cui abito · un'idea di cui parla da anni"),
                        ("PRONUNCIA", "che, chi, cui, qui: quattro parole brevi")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: la città", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali di questi posti ci sono nel tuo quartiere? Quali mancano?</li><li>Che cosa ti piace della tua città? Che cosa non ti piace?</li><li>Come ti muovi in città: a piedi, in bici, in autobus, in macchina?</li></ol>""",
    24, """<ol><li>A: <i>il marciapiede</i> (calçada) ≠ <i>la strada</i>; <i>il parco giochi</i> = per i bambini. Attenzione: <i>la fermata</i> (dell'autobus) ≠ <i>la stazione</i> (del treno).</li>
<li>B: annotare le frasi con <i>che</i> spontanee; le riprendiamo a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: luoghi e servizi</td><td>1</td></tr>
<tr><td>2 Lettura e ascolto</td><td>10 min</td><td>Tre risposte al Comune · il progetto del giardino</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>che · preposizione + cui</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>che, cui, in cui / dove, il quale</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>che, chi, cui, qui</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Unisci le frasi · quale preposizione? · le persone della città</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Indovina la parola · il quartiere che vorrei</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine maggio. Per il progetto del giardino in Bolognina (unità 09) il Comune chiede ai cittadini: <i>com'è la città che vorreste?</i> Rispondono anche i nostri amici. La signora Rossi vuole marciapiedi senza buche, panchine e un ufficio postale aperto il pomeriggio; Davide vuole piste ciclabili senza macchine e un posto sicuro per la bici; Giulia vuole un quartiere vivo la sera, con una biblioteca aperta fino alle dieci e una piazza in cui i ragazzi suonano. Nello studio Marco e Júlia mettono le idee nel progetto: panchine, rastrelliere vicino all'entrata, un piccolo palco… e un chiosco con il caffè brasiliano.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Nel portoghese parlato si dice <i>a rua que eu moro, a pessoa que eu falei</i>: lo studente trasferisce e dice <i>la via che abito, la signora che parlo</i>. In italiano la preposizione del verbo va davanti a <b>cui</b>: <i>la via <b>in cui</b> abito, la signora <b>con cui</b> parlo</i>. Al contrario, senza preposizione si usa <b>che</b>, mai <i>cui</i> (<i>il libro che leggo</i>). Pronuncia: <i>cui</i> [kùi] ≠ <i>qui</i> [kuì].</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Molti comuni italiani fanno <b>bilanci partecipativi</b>: i cittadini propongono e votano progetti per il quartiere. Bologna è divisa in sei <b>quartieri</b> (Navile, dove c'è la Bolognina, Porto-Saragozza, Santo Stefano…) e ha i famosi <b>portici</b>: 62 km di marciapiedi coperti, patrimonio UNESCO dal 2021.</div>
<div class="box"><h4>AUDIO</h4>Traccia 16.1 Le risposte e il dialogo (lento e naturale) · Traccia 16.2 Ascolta e ripeti · Traccia 16.3 Che, chi, cui o qui?</div>""")

    # Page 2
    who = {"Signora Rossi": "R", "Davide": "D", "Giulia": "G"}
    txt = "".join(f"<div class='msg' style='max-width:none;padding:1.5mm 3.5mm;font-size:8.9pt;line-height:1.45;margin:0 0 1.2mm'><b style='color:{TEAL}'>{n} ({who[n]})</b> · {t}</div>" for n, t in TEXTS)
    wish = [("negozi e vita la sera", "G"), ("panchine per riposare", "R"), ("un posto sicuro per la bici", "D"), ("un ufficio postale aperto il pomeriggio", "R"),
            ("una biblioteca aperta fino alle dieci", "G"), ("niente macchine sulla pista ciclabile", "D")]
    wl = [f'<li value="{i+1}">{s} {ch(["R", "D", "G"], a)}</li>' for i, (s, a) in enumerate(wish)]
    gd = [("per la signora Rossi:", "panchine"), ("per Davide:", "rastrelliere vicino all'entrata"), ("per Giulia:", "un piccolo palco"), ("per Júlia:", "un chiosco (con il caffè brasiliano)")]
    gdl = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:62mm')}</td></tr>" for a, x in gd)
    b.page(f"""{sec(2, "Lettura e ascolto: la città che vorrei", "10 min")}
{audiocard(["16.1 · SLOW", "16.1 · NATURAL"])}
{sub("A", "Il Comune chiede: com'è la città che vorreste? Leggi tre risposte (o ascoltale).", "2 min", "16.1 · SLOW")}
{txt}
{sub("B", "Chi lo vuole? La signora Rossi (R), Davide (D) o Giulia (G)?", "3 min")}
{twocol(wl, 4)}
{sub("C", "Seconda parte. Nello studio di Marco. Che cosa mettono nel giardino?", "5 min", "16.1 · NATURAL")}
<table style="margin:0;width:82%">{gdl}</table>""",
    22, """<ol><li>A: far sottolineare <i>che</i> e <i>cui</i> nei tre testi: quante volte c'è <i>in cui</i>?</li>
<li>C: versione <b>naturale</b>. Domanda extra: <i>Chi è la signora con cui Júlia parla sulle scale?</i> (la signora Rossi, la vicina).</li></ol>""")

    # Page 3
    rules = [("<i>Un ufficio postale <b>che</b> apre il pomeriggio.</i> Chi apre?", ["l'ufficio postale (soggetto)", "io"], "l'ufficio postale (soggetto)"),
             ("<i>L'idea <b>che</b> mi piace.</i> <i>Che</i> si usa", ["senza preposizione", "dopo una preposizione"], "senza preposizione"),
             ("<i>La via <b>in cui</b> abito.</i> Perché <i>in</i>? Perché si dice", ["abitare in", "abitare a"], "abitare in"),
             ("<i>La signora <b>con cui</b> parli.</i> Dopo una preposizione si usa", ["cui", "che"], "cui"),
             ("<i>Che</i> e <i>cui</i> per il femminile e il plurale", ["non cambiano", "cambiano"], "non cambiano"),
             ("<i>La via in cui abito</i> = <i>la via</i>", ["dove abito", "che abito"], "dove abito")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("È la città", ["che", "in cui"], "in cui", "sono nata."), ("È un film", ["che", "di cui"], "che", "ho visto tre volte."),
          ("Ecco l'amico", ["con cui", "che"], "con cui", "vado in palestra."), ("È un problema", ["di cui", "che"], "di cui", "parliamo spesso.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: che e cui", "10 min")}
{sub("A", "Studia le frasi dei testi e del dialogo.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. la città <b>che</b> vorrei · un ufficio postale <b>che</b> apre il pomeriggio · macchine <b>che</b> parcheggiano sulla pista · l'idea <b>che</b> mi piace di più<br>
2. una città <b>in cui</b> gli anziani escono senza paura · la via <b>in cui</b> abito · una piazza <b>in cui</b> i ragazzi possono suonare<br>
3. la signora <b>con cui</b> parli sulle scale · un'idea <b>di cui</b> parla da anni · panchine <b>su cui</b> riposare</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Che o preposizione + cui? Scegli.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>che</b> = soggetto o oggetto, senza preposizione: <i>l'ufficio che apre, l'idea che mi piace</i>. <b>preposizione + cui</b> = quando il verbo vuole una preposizione: <i>abitare <b>in</b> → in cui, parlare <b>con</b> → con cui, parlare <b>di</b> → di cui</i>. Non cambiano mai. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: la domanda magica: <i>il verbo vuole una preposizione? (abitare <b>in</b>, parlare <b>con</b>) → prep. + cui. No? → che.</i></li>
<li>C: frase 1: <i>nascere <b>in</b></i> una città → <i>in cui</i> (o <i>dove</i>).</li></ol>""")

    grammar_ref_it.che_cui(b)

    # Page 5
    ans3 = ["chi", "cui", "che", "qui", "cui", "chi"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>La via che abito è tranquilla.</td><td><b>La via in cui abito è tranquilla.</b></td><td><i>abitare <b>in</b></i>.</td></tr>
<tr><td>È la ragazza che esco.</td><td><b>È la ragazza con cui esco.</b></td><td><i>uscire <b>con</b></i>.</td></tr>
<tr><td>Il film che ti ho parlato.</td><td><b>Il film di cui ti ho parlato.</b></td><td><i>parlare <b>di</b></i>.</td></tr>
<tr><td>Il libro cui leggo.</td><td><b>Il libro che leggo.</b></td><td>Nessuna preposizione: <i>che</i>.</td></tr>
<tr><td>Le persone chi abitano qui.</td><td><b>Le persone che abitano qui.</b></td><td><i>chi</i> = domanda (<i>Chi è?</i>).</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["16.2", "16.3"])}
{sub("A", "Ascolta e ripeti. Che [ke] · chi [ki] · cui [kùi] · qui [kuì].", "2 min", "16.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S162)}</div>
{sub("B", "Che, chi, cui o qui? Ascolta e scegli.", "2 min", "16.3")}
{twocol([f'<li value="{i+1}">{ch(["che", "chi", "cui", "qui"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>chi</i> non è un relativo dopo un nome (<i>le persone <b>che</b></i>); <i>chi</i> = la persona che / domanda.</li>
<li>4A: <i>cui</i> ha l'accento sulla <b>u</b> (kùi), <i>qui</i> sulla <b>i</b> (kuì). Far ripetere a coppie: <i>cui – qui, che – chi</i>.</li></ol>""")

    # Page 6
    jn = [("Ho un'amica. L'amica abita a Roma.", "Ho un'amica che abita a Roma."), ("Questo è il bar. Prendo il caffè in questo bar.", "Questo è il bar in cui prendo il caffè."),
          ("Ecco il collega. Lavoro con questo collega.", "Ecco il collega con cui lavoro."), ("È un libro. Tutti parlano di questo libro.", "È un libro di cui tutti parlano."),
          ("Ho visto la piazza. Hanno rifatto la piazza.", "Ho visto la piazza che hanno rifatto.")]
    jnl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in jn)
    pp = [("la ragazza ___ cui ho scritto", "a"), ("il motivo ___ cui sono qui", "per"), ("il tavolo ___ cui ho messo le chiavi", "su"),
          ("gli amici ___ cui vado al mare", "con")]
    ppl = [f'<li value="{i+1}">{s.replace("___", A(a, "min-width:12mm"))}</li>' for i, (s, a) in enumerate(pp)]
    wb = [("la città", "il cittadino / la cittadina"), ("abitare", "l'abitante"), ("la bicicletta", "il / la ciclista"), ("passare (a piedi)", "il passante")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:34mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Unisci le due frasi con che o preposizione + cui.", "4 min")}
<ol style="line-height:1.45">{jnl}</ol>
{sub("B", "Quale preposizione? a, con, per o su?", "3 min")}
{twocol(ppl, 3)}
{sub("C", "Le persone della città. Costruisci le parole.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 5: <i>rifare la piazza</i> (oggetto, nessuna preposizione) → <i>che</i>. B: far dire il verbo con la preposizione: <i>scrivere <b>a</b>, mettere <b>su</b></i>.</li>
<li>C: <i>il cittadino</i> è nel testo del Comune (<i>i cittadini</i>). <i>Il / la ciclista</i>: stessa forma per uomo e donna.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Indovina la parola! Spiega una parola senza dirla: È un posto in cui… · È una persona che… · È una cosa che… · È una cosa con cui… L'insegnante indovina. Poi cambiate.", "5 min")}
<div class="box" style="margin-top:1mm"><h4>PAROLE DA SPIEGARE</h4>la biblioteca · il / la ciclista · la panchina · l'ufficio postale · il parco giochi · la fermata · il vicino di casa · la bicicletta · il mercato · il bar</div>
{sub("B", "Il quartiere che vorrei. Il Comune chiede anche a te. Parla con l'insegnante: Che cosa c'è nel tuo quartiere? Che cosa manca? Com'è il quartiere in cui vorresti abitare?", "7 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Vorrei un quartiere in cui… · Mi piacerebbe una piazza che… · Nel mio quartiere manca… · Ci sono troppe macchine che… · un posto in cui i bambini possono… · un servizio di cui ho bisogno: …</div>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: modello: <i>È un posto in cui prendi in prestito i libri.</i> (la biblioteca) · <i>È una persona che abita vicino a te.</i> (il vicino).</li>
<li>B: pretendere almeno tre frasi relative, una con <i>che</i> e due con <i>preposizione + cui</i>. Ripresa nei compiti.</li></ol>""")

    # Page 8
    pc = [("A2 · 15", "So dire che cosa sto facendo e che cosa sto per fare."), ("A2 · 16", "So nominare luoghi e servizi della città."),
          ("A2 · 16", "So usare che (la città che vorrei)."), ("A2 · 16", "So usare preposizione + cui (la via in cui abito)."),
          ("A2 · 16", "So dire come vorrei il mio quartiere.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("La via che abito è rumorosa.", "La via in cui abito"), ("È l'idea che mi piace di più.", "✓"),
          ("Il ragazzo che esco si chiama Leo.", "con cui esco"), ("Il libro cui leggo è bello.", "Il libro che leggo"),
          ("Il film che ti ho parlato.", "di cui ti ho parlato"), ("È una piazza in cui c'è sempre musica.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. La città che vorrei (50–75 parole).</b> Rispondi anche tu al Comune: com'è la via in cui abiti? Che cosa manca? Come vorresti il tuo quartiere? Usa <i>che</i> e almeno due <i>preposizione + cui</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il testo; la classe (o l'insegnante) "vota" l'idea migliore. Unità 17: <i>Qui si fa così</i> (si impersonale, è vietato / è obbligatorio).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("16.1", "Le risposte e il dialogo (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("16.2", "Ascolta e ripeti")}
<p>{" · ".join(S162)}</p>
{sub("16.3", "Che, chi, cui o qui?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S163))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 16 - La citta che vorrei")
