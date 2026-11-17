# Speak! Progresso B1 - Unità 05 "Il Made in Italy" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 05", audio_json=os.path.join(HERE, "audio_it-b1-unita-05.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-05"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["05.1 Il Made in Italy"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S052 = [x.split(": ", 1)[1] for x in _r["05.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 05", "Il Made in Italy", "Prodotti tipici e marchi · <b>il congiuntivo presente</b>",
                       [("SAI FARE", "presentare e consigliare un prodotto, esprimere opinioni, desideri, paure e necessità"),
                        ("LINGUA", "Spero che ti piaccia. · È importante che lo sappiate. · Ho paura che si rompa. · Basta che…"),
                        ("PRONUNCIA", "le doppie del congiuntivo: «faccia», «sappia», «abbia»")])
    kw = [("il posto dove si produce l'aceto balsamico", "un'acetaia"), ("un grande contenitore di legno", "una botte"),
          ("diventare vecchio", "invecchiare"), ("il foglietto con le informazioni sul prodotto", "un'etichetta"),
          ("il controllo delle merci alla frontiera", "la dogana"), ("mandare per posta", "spedire"),
          ("provare un cibo per sentire il sapore", "assaggiare"), ("una scatola che si spedisce", "un pacco")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: il Made in Italy", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Quali prodotti italiani conosci? Ne compri qualcuno in Brasile?</li><li>Che cosa ti fa pensare la parola «Made in Italy»: moda, cibo, macchine…?</li><li>Quando compri un prodotto, leggi l'etichetta?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">un'acetaia · assaggiare · una botte · la dogana · un'etichetta · invecchiare · un pacco · spedire</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Hai mai spedito un pacco all'estero? Che cosa c'era dentro?", "1 min")}""",
    25, """<ol><li>A: lasciare parlare lo studente; annotare se usa già <i>penso che sia / spero che</i> (A2 09, 29): oggi si completa il quadro del congiuntivo.</li>
<li>B: <i>acetaia</i>: da <i>aceto</i>, con il suffisso dei luoghi di produzione (<i>-aia</i>: <i>pagliaio, risaia</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione sul Made in Italy · parole chiave del dialogo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Il Made in Italy: visita a un'acetaia di Modena</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>Il congiuntivo presente: tutte le persone, irregolari, quando si usa</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il congiuntivo presente (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Le parole della qualità · falsi amici · le doppie del congiuntivo</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il biglietto di Marco a suo padre · completare con il congiuntivo</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Un prodotto tipico brasiliano · gioco di ruolo: spedire un regalo</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Sabato 23 gennaio Júlia, Marco e Camila vanno a Modena, come avevano deciso giovedì (le modifiche per il cliente sono state consegnate). Prima delle tigelle visitano un'acetaia. La guida spiega che il balsamico tradizionale invecchia almeno dodici anni e che all'estero molti prodotti hanno un nome italiano ma non vengono dall'Italia: bisogna cercare la sigla DOP (come per il <i>parmesão</i> brasiliano). Júlia vorrebbe mandare una bottiglia ai genitori ma ha paura che si rompa: l'acetaia spedisce in tutto il mondo. Marco ne compra una per il padre (che preferisce «il balsamico della nonna»); Camila ne ha già tre nella borsa per gli amici di Recife.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese ha il <i>subjuntivo</i> (<i>espero que você goste</i>), quindi l'idea è facile; ma il brasiliano parlato usa spesso l'indicativo (<i>acho que é</i>) e lo studente dice <i>penso che è</i>. Problema di forma: <i>sapete / sappiate, venite / veniate</i>. Falsi amici: <i>presente</i> ≠ <i>regalo</i>; <i>squisito</i> = buonissimo (≠ <i>esquisito</i> = strano); <i>legittimo</i> = legale (≠ <i>legítimo</i> = autentico, originale).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>DOP (Denominazione di Origine Protetta) e IGP sono marchi europei che proteggono i prodotti legati a un territorio. L'Aceto Balsamico Tradizionale di Modena DOP invecchia almeno 12 anni (<i>extravecchio</i>: 25). All'estero il fenomeno dell'<i>Italian sounding</i> (nomi, colori e bandiere italiane su prodotti non italiani) vale più delle esportazioni vere. Le tigelle sono piccoli pani rotondi dell'Appennino modenese, con salumi e formaggi.</div>
<div class="box"><h4>AUDIO</h4>Traccia 05.1 Il Made in Italy (prima naturale, poi lenta) · Traccia 05.2 Ripeti: il congiuntivo presente</div>""")

    # Pagina 2 - Ascolto
    gi = [("l'età dell'aceto", True), ("il prezzo della benzina", False), ("i prodotti falsi all'estero", True), ("una partita di calcio", False), ("un regalo per i genitori", True), ("spedire un pacco", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("L'aceto balsamico tradizionale invecchia almeno dodici anni.", "V"), ("In Brasile il balsamico del supermercato è molto caro.", "F"),
          ("La guida consiglia di cercare la sigla DOP.", "V"), ("Júlia ha paura che il pacco arrivi in ritardo.", "F"),
          ("L'acetaia spedisce anche all'estero.", "V"), ("Camila non ha comprato niente.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Il Made in Italy", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["05.1 · NATURAL", "05.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Sabato a Modena, in un'acetaia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "05.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Perché, secondo te, all'estero tanti prodotti hanno un nome italiano? {R("Il nome italiano fa pensare alla qualità e fa vendere di più.") if T else ""}</li>
<li>Marco dice: «Spero che gli piaccia». È sicuro del suo regalo? Perché? {R("No: il padre dice che il balsamico migliore è quello di sua nonna.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Benvenuti! · Prima di cominciare… · Ecco. · Bella idea! · Basta che… · Peccato che… · E poi… · Va bene, ma…</i></div>""",
    29, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: età dell'aceto, prodotti falsi, regalo per i genitori, spedire un pacco.</li>
<li>B: 2 costa pochissimo · 4 ha paura che la bottiglia si rompa · 6 ne ha già tre nella borsa.</li>
<li>Espressioni: <i>basta che, peccato che</i> (= <i>basta que, pena que</i>) vogliono il congiuntivo.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Penso che <u>sia</u> più vecchio di mio nipote.", "un'opinione"), ("Vogliamo che il mondo <u>conosca</u> il prodotto vero.", "una volontà"),
          ("Ho paura che la bottiglia <u>si rompa</u>.", "un'emozione"), ("È necessario che i clienti <u>leggano</u> l'etichetta.", "una necessità"),
          ("È giusto che i miei amici <u>conoscano</u> il Made in Italy.", "un giudizio")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:28mm')}</li>" for s, a in ex)
    bank3 = "un'emozione · un giudizio · una necessità · un'opinione · una volontà"
    fx = [("leggere → loro", "leggano"), ("sapere → voi", "sappiate"), ("dare → voi", "diate"),
          ("potere → io", "possa"), ("piacere → lui", "piaccia"), ("finire → loro", "finiscano")]
    fxl = "".join(f"<li>{v} {A(r, 'min-width:20mm')}</li>" for v, r in fx)
    cc = [("So che il parmigiano", ["viene", "venga"], "viene", "da Parma e Reggio Emilia."),
          ("Spero che il pacco", ["arriva", "arrivi"], "arrivi", "prima di Carnevale."),
          ("Secondo me il balsamico", ["è", "sia"], "è", "troppo caro.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il congiuntivo presente", "8 min")}
{sub("A", "Frasi dal dialogo. Che cosa esprime la prima parte della frase? Usa le parole del riquadro.", "3 min")}
<div class="bank">{bank3}</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scrivi la forma del congiuntivo. Cerca le forme nel dialogo o alla pagina 4.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0;column-count:2">{fxl}</ol>
{sub("C", "Indicativo o congiuntivo? Scegli.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Il <b>congiuntivo presente</b> si usa dopo verbi ed espressioni di <b>opinione</b> (<i>penso che</i>), <b>volontà</b> (<i>voglio che</i>), <b>emozione</b> (<i>spero, ho paura, peccato che</i>), <b>necessità</b> (<i>è importante, bisogna, basta che</i>) e <b>giudizio</b> (<i>è giusto, è strano che</i>). Per i fatti sicuri si usa l'indicativo: <i>so che, è vero che, secondo me</i>. Desinenze: <i>-are</i> → <b>-i</b>, <i>-ere / -ire</i> → <b>-a</b>; noi <b>-iamo</b>, voi <b>-iate</b>, loro <b>-ino / -ano</b>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: far notare che il verbo al congiuntivo è sempre nella seconda parte, dopo <i>che</i>, e che i soggetti sono diversi (<i>io penso / lui è</i>). Con lo stesso soggetto si usa <i>di</i> + infinito: lo vediamo nell'unità 06.</li>
<li>C: frase 3: <i>secondo me</i> vuole l'indicativo; con <i>penso che</i> sarebbe <i>sia</i>.</li></ol>""")

    grammar_ref_it.congiuntivo_sistema(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["fatto a mano", "artigianale", "a chilometro zero", "contraffatto", "di marca", "di prima qualità"]
    rgt = ["falso, una copia illegale", "il migliore possibile", "prodotto vicino a dove si compra", "non fatto da una macchina", "di un'azienda famosa", "prodotto in un piccolo laboratorio"]
    ans = {"fatto a mano": "non fatto da una macchina", "artigianale": "prodotto in un piccolo laboratorio", "a chilometro zero": "prodotto vicino a dove si compra",
           "contraffatto": "falso, una copia illegale", "di marca": "di un'azienda famosa", "di prima qualità": "il migliore possibile"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: le parole della qualità", "4 min")}
{sub("A", "Unisci le espressioni alle definizioni.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Compri spesso prodotti di marca?</li><li>Che cosa compri a chilometro zero?</li><li>Hai mai comprato una cosa contraffatta?</li><li>Quale oggetto fatto a mano ti piace?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho comprato un presente per mia madre.</td><td><b>Ho comprato un regalo per mia madre.</b></td><td><i>presente</i> = il tempo di oggi.</td></tr>
<tr><td>Questo vino è esquisito (= strano).</td><td><b>Questo vino è strano.</b></td><td><i>squisito</i> = buonissimo!</td></tr>
<tr><td>È un parmigiano legittimo.</td><td><b>È un parmigiano autentico / originale.</b></td><td><i>legittimo</i> = permesso dalla legge.</td></tr>
<tr><td>Spero che ti piace.</td><td><b>Spero che ti piaccia.</b></td><td><i>sperare che</i> + congiuntivo.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: le doppie del congiuntivo", "4 min")}
<p class="small" style="margin:.3mm 0">Molti congiuntivi irregolari hanno una consonante doppia: <i>fa<b>cc</b>ia, sa<b>pp</b>ia, a<b>bb</b>ia, pia<b>cc</b>ia, po<b>ss</b>a</i>. La doppia distingue anche il congiuntivo dall'indicativo: <i>sa<b>pp</b>iate</i> (congiuntivo) ≠ <i>sapete</i> (indicativo).</p>
{audiocard(["05.2"])}
{sub("A", "Ascolta e ripeti. Poi l'insegnante dice una frase con «sapete» o «sappiate»: tu dici se è indicativo o congiuntivo.", "4 min", "05.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S052))}</p>""",
    29, """<ol><li>A: fatto a mano d · artigianale f · a chilometro zero c · contraffatto a · di marca e · di prima qualità b.</li>
<li>Pronuncia: frasi per il gioco finale: <i>So che lo sapete. · Voglio che lo sappiate. · Penso che abbiate ragione. · Avete ragione.</i></li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["preferisci", "preferisca"], "preferisci"), (["ti piaccia", "ti piace"], "ti piaccia"),
          (["tenga", "tieni"], "tenga"), (["usi", "usa"], "usi"), (["assaggi", "assaggia"], "assaggi"),
          (["possa", "posso"], "possa"), (["viene", "venga"], "viene"), (["decidiate", "decidete"], "decidiate")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Spero che voi (venire) … a Modena con noi.", "veniate"), ("È strano che loro non (sapere) … che cos'è la DOP.", "sappiano"),
          ("Voglio che tu (dire) … la verità: ti piace?", "dica"), ("Bisogna che noi (partire) … presto.", "partiamo"),
          ("Peccato che le tigelle (finire) … così presto!", "finiscano"), ("Ho paura che il pacco (essere) … troppo pesante.", "sia")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:22mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Marco mette un biglietto nel pacco per suo padre. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><i>Caro papà, ti mando questa bottiglia da Modena. So che tu {p[0]} il balsamico della bisnonna, ma spero che anche questo {p[1]}. La guida dice che è importante che tu lo {p[2]} lontano dal sole e che non lo {p[3]} per cucinare: basta una goccia sul parmigiano o sulle fragole. Voglio che la mamma lo {p[4]} per prima: è lei l'esperta! Peccato che io non {p[5]} venire a Firenze questo fine settimana. Luca dice che {p[6]} lui a Bologna sabato prossimo. E per Pasqua bisogna che voi {p[7]} la data del pranzo presto! Un abbraccio, Marco</i></div>
{sub("B", "Completa con il congiuntivo del verbo tra parentesi.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: per ogni scelta chiedere: <i>è un fatto sicuro o un'opinione, un desiderio…?</i> Gap 1 e 7: <i>so che</i> e <i>dice che</i> riportano fatti → indicativo. Gap 3: <i>tenere → tenga</i> (come <i>venire → venga</i>).</li>
<li>B: far dire anche il soggetto con <i>io, tu, lui</i>: <i>voglio che <b>tu</b> dica</i>.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: consigliare un prodotto", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>consigliare</th><th>dare un'opinione</th><th>desideri e speranze</th><th>paure e dubbi</th></tr>
<tr><td><i>È importante che tu provi… · Bisogna che… · Basta che… · Ti consiglio di…</i></td><td><i>Penso che sia… · Mi sembra che… · Non credo che… · Secondo me è…</i></td><td><i>Spero che… · Voglio che… · Preferisco che… · Sono contento/a che…</i></td><td><i>Ho paura che… · Peccato che… · È strano che… · Non so se…</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi presenta per due minuti un prodotto tipico del Brasile (o della tua regione) a un amico italiano.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>che cos'è e dove si produce</li><li>perché è importante che lo provi</li><li>come si usa o si mangia</li><li>come riconoscere il prodotto vero</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. Sei in un negozio di prodotti tipici a Bologna e vuoi spedire un regalo in Brasile. L'insegnante è il commesso.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Buongiorno, posso aiutarLa? · Per chi è il regalo? · Le consiglio il Parmigiano di 24 mesi: è importante che sia sottovuoto. · Per la spedizione bisogna che compili questo modulo. · Ha paura che si rompa qualcosa? Lo imballiamo noi. · Sono 48 euro, più la spedizione.") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>È giusto che i prodotti tipici siano protetti dalla legge?</li><li>Vale la pena pagare di più per un prodotto originale?</li><li>Quale prodotto brasiliano dovrebbe avere un marchio come la DOP?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>penso che è</i> e le forme di <i>voi / loro</i>. Opzione fluidità (3-2-1): la stessa presentazione in 2 minuti, poi in 1 minuto.</li>
<li>B: le battute dell'insegnante sono in rosso; registro formale (<i>Lei</i>). Idee per lo studente: caffè, cachaça, formaggio della Serra da Canastra, castagne di Pará (lo studente spiega anche che cosa sono).</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare il congiuntivo presente con tutte le persone.",
          "So presentare e consigliare un prodotto."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Una recensione.</b> Scrivi una recensione online di un negozio, di un mercato o di un prodotto che conosci bene. Prima leggi la recensione di Camila.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>★★★★★ Un'esperienza da non perdere! Sabato ho visitato quest'acetaia con due amici e la consiglio a tutti. La guida è stata bravissima: ci ha spiegato che l'aceto tradizionale invecchia almeno dodici anni nelle botti. Penso che sia un posto unico in Emilia. Alla fine abbiamo assaggiato una goccia di aceto sul parmigiano: squisito! I prezzi sono alti, ma è giusto che un prodotto così costi tanto. Un consiglio: è importante che prenotiate la visita in anticipo, soprattutto il sabato. E se abitate all'estero, nessun problema: basta che diate l'indirizzo e la spedizione la fanno loro. Ho paura che le mie tre bottiglie non arrivino a Pasqua… ma spero di tornarci presto. Camila, Recife</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno cinque congiuntivi con persone diverse &nbsp;☐ un'opinione (<i>penso che…</i>) &nbsp;☐ una necessità (<i>è importante che, basta che</i>) &nbsp;☐ un consiglio finale &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far sottolineare nel modello tutti i congiuntivi (<i>sia, costi, prenotiate, diate, arrivino</i>) e far notare <i>spero di tornarci</i>: stesso soggetto → <i>di</i> + infinito. Prossima unità: <i>Può darsi che…</i> (il congiuntivo passato).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("05.1", "Il Made in Italy (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("05.2", "Ripeti: il congiuntivo presente")}
<p>{" · ".join(S052)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 05 - Il Made in Italy")
