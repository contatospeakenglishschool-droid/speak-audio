# Speak! Progresso B1 - Unità 01 "Bentornata!" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 01", audio_json=os.path.join(HERE, "audio_it-b1-unita-01.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-01"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["01.1 Bentornata!"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S012 = [x.split(": ", 1)[1] for x in _r["01.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 01", "Bentornata!", "Ritorni, viaggi e novità · <b>il trapassato prossimo</b>",
                       [("SAI FARE", "capire un racconto naturale, raccontare un viaggio e un ritorno mettendo in ordine i fatti"),
                        ("LINGUA", "L'autobus era già partito. · Non mi aveva ancora scritto. · Mi mancava Bologna. · Pazienza!"),
                        ("PRONUNCIA", "l'accento della frase: aveva‿aspettato")])
    kw = [("tornare in un posto dopo un periodo lontano", "rientrare"), ("non puntuale, dopo l'ora prevista", "in ritardo"),
          ("una festa che il festeggiato non conosce prima", "una festa a sorpresa"), ("sentire la mancanza di qualcuno o qualcosa", "mancare"),
          ("si dice quando non si può fare niente", "Pazienza!"), ("si dice con affetto per una persona sfortunata", "Poverino!"),
          ("alzare i bicchieri e fare un augurio", "brindare"), ("cade la neve", "nevica")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: il ritorno", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Qual è stato il tuo ultimo viaggio lungo? Com'è andato il ritorno?</li><li>Quando torni a casa dopo un viaggio, che cosa ti manca? Che cosa ti mancava prima?</li><li>Guarda la foto. Chi è questa ragazza? Parte o è appena arrivata?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">brindare · una festa a sorpresa · in ritardo · mancare · nevica · Pazienza! · Poverino! · rientrare</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Ti hanno mai fatto una festa a sorpresa? E tu l'hai fatta a qualcuno?", "1 min")}""",
    25, """<ol><li>A: è la prima unità del B1: lasciare parlare lo studente senza correggere troppo; annotare gli errori sul passato per la pagina 8. Domanda 2: <i>mi manca / mi mancava</i> (verbo come <i>piacere</i>).</li>
<li>B: <i>Pazienza!</i> = <i>paciência, fazer o quê</i>; <i>Poverino/a!</i> si usa anche in modo scherzoso.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione · parole chiave del dialogo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Bentornata! Camila racconta il suo Natale a Recife</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>Il trapassato prossimo: che cosa è successo prima?</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il trapassato prossimo (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Il viaggio in aereo · scelta delle parole · l'accento della frase</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il messaggio di Camila · che cosa era successo?</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Raccontare un viaggio · monologo · gioco di ruolo</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA: COMINCIA IL B1</h4>Gennaio del terzo anno di Júlia a Bologna. Camila è partita per Recife il 20 dicembre (Ripasso 4 dell'A2) ed è tornata sabato 9 gennaio: ventidue ore di viaggio, il volo in ritardo a Lisbona. La domenica gli amici la aspettano al bar di Giulia. A Recife la madre le aveva preparato una festa a sorpresa; faceva trentadue gradi, mentre a Bologna nevicava. Dopo due settimane le mancava Bologna. La novità è Pietro, il ragazzo dell'autobus (unità A2 33 e 36): Camila gli aveva dato il suo numero prima di partire; la sera di Natale lui le ha scritto con una foto di piazza Maggiore sotto la neve; si sono scritti quasi ogni giorno; lui era rimasto a Bologna a studiare. All'arrivo l'aspettava all'aeroporto da due ore: ecco perché ha preso un taxi «non da sola». Stasera vanno al cinema. Pietro per ora non parla mai.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Nel portoghese parlato il <i>tinha feito</i> si usa poco: lo studente dice <i>quando sono arrivata, l'autobus è già partito</i>. In italiano, se un'azione è finita <b>prima</b> di un'altra passata, il trapassato è necessario. Attenzione anche a <i>mi mancava Bologna</i> (non <i>ho sentito la mancanza di</i>) e alla posizione di <i>ancora</i>: <i>non mi aveva <b>ancora</b> scritto</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Molti studenti stranieri a Bologna tornano a casa per le vacanze di Natale; i voli dal Brasile all'Italia di solito hanno uno scalo (Lisbona, Madrid, Parigi) e durano più di quindici ore. In Italia si brinda con <i>Salute!</i> o <i>Cin cin!</i>, guardandosi negli occhi.</div>
<div class="box"><h4>AUDIO</h4>Traccia 01.1 Bentornata! (prima naturale, poi lenta) · Traccia 01.2 Ripeti: l'accento della frase</div>
<div class="box"><h4>IL FORMATO B1</h4>Dal B1 l'ascolto si fa prima alla velocità naturale (la versione lenta è solo un aiuto); il monologo dura due minuti; lo studente tiene un registro dei propri errori; i compiti sono di 100–150 parole con un modello e una lista di controllo.</div>""")

    # Pagina 2 - Ascolto
    gi = [("il viaggio di ritorno", True), ("il Natale a Recife", True), ("un esame di Bruno", False), ("un ragazzo", True), ("un nuovo lavoro", False), ("una serata al cinema", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Camila è arrivata a Bologna con l'ultimo autobus.", "F"), ("A Recife la madre aveva organizzato una festa a sorpresa.", "V"),
          ("A Natale a Bologna faceva bel tempo.", "F"), ("Prima di partire Camila aveva dato il suo numero a Pietro.", "V"),
          ("Pietro aveva passato il Natale con i suoi genitori.", "F"), ("Pietro ha aspettato Camila all'aeroporto.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Bentornata!", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["01.1 · NATURAL", "01.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Domenica 10 gennaio, al bar di Giulia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "01.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>All'inizio Camila non parla di Pietro. Perché, secondo te? {R("È timida / vuole fare una sorpresa; Giulia capisce e la provoca.") if T else ""}</li>
<li>Bruno dice: «Ah, ecco perché hai preso un taxi!». Che cosa ha capito? {R("Che Camila ha preso il taxi con Pietro.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Eccola! · Com'è andato il viaggio? · Raccontaci tutto! · Sapete una cosa? · Non me l'aspettavo. · Va bene, ve lo racconto. · E invece… · Ah, ecco perché…</i></div>""",
    22, """<ol><li>A: prima la versione <b>naturale</b>, senza testo; la lenta solo se serve. Argomenti corretti: viaggio, Natale a Recife, un ragazzo, il cinema.</li>
<li>B: 1 ha preso un taxi · 3 nevicava · 5 era rimasto a Bologna a studiare (i genitori erano andati in montagna).</li>
<li>Espressioni utili: farle ripetere con l'intonazione giusta; <i>E invece…</i> introduce una sorpresa.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Quando sono arrivata a Bologna, l'ultimo autobus <u>era già partito</u>.", "1 l'autobus parte · 2 Camila arriva"),
          ("Mia madre <u>aveva preparato</u> una festa a sorpresa.", "1 la madre prepara · 2 Camila arriva"),
          ("Prima di partire <u>gli avevo dato</u> il mio numero.", "1 Camila dà il numero · 2 parte"),
          ("Mi <u>aveva aspettato</u> due ore.", "1 Pietro aspetta · 2 Camila esce")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:54mm')}</li>" for s, a in ex)
    rules = [("Il trapassato prossimo racconta un'azione", ["prima", "dopo"], "prima", "di un altro fatto passato."),
             ("Si forma con l'", ["imperfetto", "presente"], "imperfetto", "di <i>avere</i> o <i>essere</i> + participio passato."),
             ("<i>Partire</i> e <i>andare</i> usano l'ausiliare", ["essere", "avere"], "essere", ": <i>era partito, erano andati</i>."),
             ("<i>Già, ancora, mai</i> vanno", ["tra ausiliare e participio", "alla fine"], "tra ausiliare e participio", ".")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".") for a, o, r, z in rules)
    cc = [("Quando siamo arrivati al cinema, il film", ["è cominciato", "era cominciato"], "era cominciato", "da dieci minuti."),
          ("Non sono andata alla festa perché non mi", ["avevano invitato", "erano invitato"], "avevano invitato", "."),
          ("Bruno era stanco: la notte prima", ["aveva studiato", "ha studiato"], "aveva studiato", "fino alle tre.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" .", ".") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il trapassato prossimo", "8 min")}
{sub("A", "Frasi dal dialogo. Che cosa è successo prima (1) e che cosa dopo (2)?", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli il tempo giusto.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Per un'azione finita <b>prima</b> di un altro momento del passato si usa il <b>trapassato prossimo</b>: <b>imperfetto di avere / essere + participio</b> (<i>avevo dato, era partito, si erano scritti</i>). Ausiliare e accordo come nel passato prossimo. Spesso con <b>già, non… ancora, non… mai, appena</b>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: disegnare una linea del tempo con due punti; lo studente mette le azioni nell'ordine giusto. Poi chiedere: <i>che cosa hanno in comune i verbi sottolineati?</i></li>
<li>C: frase 1: con <i>è cominciato</i> il film comincia quando arriviamo; con <i>era cominciato</i> lo abbiamo perso. Far notare la differenza di significato.</li></ol>""")

    grammar_ref_it.trapassato_prossimo(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    cl = [("perdere", "la coincidenza"), ("fare", "scalo a Lisbona"), ("ritirare", "i bagagli"), ("passare", "il controllo passaporti"),
          ("atterrare", "in orario"), ("il volo", "è stato cancellato")]
    lft = ["perdere", "fare", "ritirare", "passare", "atterrare", "il volo"]
    rgt = ["è stato cancellato", "i bagagli", "il controllo passaporti", "in orario", "la coincidenza", "scalo a Lisbona"]
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(dict(cl)[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: il viaggio in aereo", "4 min")}
{sub("A", "Unisci le due parti delle espressioni.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Hai mai perso una coincidenza? Che cosa hai fatto?</li><li>Il tuo ultimo viaggio: avevi già visto quel posto prima?</li><li>Preferisci un volo diretto o con scalo?</li><li>Ti hanno mai perso i bagagli?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho sentito la mancanza di Bologna.</td><td><b>Mi è mancata Bologna.</b></td><td><i>mancare</i> funziona come <i>piacere</i>: la cosa che manca è il soggetto.</td></tr>
<tr><td>Il volo era atrasato.</td><td><b>Il volo era in ritardo.</b></td><td><i>atraso</i> = <i>ritardo</i>; in italiano non esiste <i>atrasato</i>.</td></tr>
<tr><td>Ho dato un presente a mia madre.</td><td><b>Ho fatto un regalo a mia madre.</b></td><td><i>il presente</i> = il tempo di adesso; il dono è <i>il regalo</i>.</td></tr>
<tr><td>Mi sono rimasta a Bologna.</td><td><b>Sono rimasta a Bologna.</b></td><td><i>rimanere</i> non è riflessivo.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: l'accento della frase", "4 min")}
<p class="small" style="margin:.3mm 0">Nel trapassato l'ausiliare è debole e veloce; l'accento forte va sul participio: <i>mi aveva aspet<b>TA</b>to</i>. Le vocali vicine si legano: <i>aveva‿aspettato, era‿andato</i>.</p>
{audiocard(["01.2"])}
{sub("A", "Ascolta e ripeti. Poi racconta all'insegnante tre cose che avevi già fatto ieri prima delle nove.", "4 min", "01.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S012))}</p>""",
    29, """<ol><li>A: 1 e · 2 f · 3 b · 4 c · 5 d · 6 a. <i>La coincidenza</i> = il volo o il treno successivo da prendere (<i>conexão</i>). <i>Scalo</i> = la fermata intermedia.</li>
<li>Pronuncia: battere il ritmo sul tavolo: solo il participio è forte. Domanda finale: <i>Ieri prima delle nove avevo già fatto colazione, ero già uscito…</i></li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["avevo dimenticato", "ho dimenticato"], "avevo dimenticato"), (["è partito", "era partito"], "era partito"),
          (["mi aveva aspettato", "mi ha aspettato"], "mi aveva aspettato"), (["era", "è stato"], "è stato"),
          (["aveva preparato", "ha preparato"], "aveva preparato"), (["era nevicato", "è nevicato"], "era nevicato"),
          (["non mi aveva ancora scritto", "non mi aveva scritto ancora"], "non mi aveva ancora scritto"), (["mi mancava", "mancavo"], "mi mancava")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Camila era stanchissima quando è arrivata.", "Aveva viaggiato per ventidue ore."), ("Giulia ha trovato il bar pieno di gente.", "Davide aveva invitato tutti / aveva messo un annuncio."),
          ("Bruno non ha superato l'esame.", "Non aveva studiato abbastanza."), ("Júlia è arrivata in ufficio senza chiavi.", "Le aveva dimenticate a casa.")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:50mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Il giorno dopo, Camila scrive alla madre. Scegli il verbo giusto.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Mamma, sono arrivata!</b><br>Ciao mamma! Il viaggio è stato lunghissimo. A Lisbona {p[0]} il caricabatterie in aereo, e quando sono arrivata a Bologna l'ultimo autobus {p[1]}. Ma una persona {p[2]} all'aeroporto: Pietro, il ragazzo di cui ti avevo parlato! Il Natale con voi {p[3]} bellissimo. Non ti ho ancora detto grazie per la festa: non sapevo niente, tu {p[4]} tutto in segreto! Pietro mi ha raccontato che prima del mio arrivo {p[5]} per tre giorni. Mi ha anche confessato che prima di Natale {p[6]} perché era timido. Comunque, Bologna {p[7]}. Ti chiamo stasera. Un bacio, Camila</div>
{sub("B", "Che cosa era successo prima? Spiega con il trapassato prossimo.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: il testo mescola passato prossimo, imperfetto e trapassato: per ogni scelta chiedere <i>prima o dopo?</i> Gap 4: <i>è stato</i> (un fatto concluso, giudizio finale). Gap 6: la neve è caduta <b>prima</b> dell'arrivo di Camila. Gap 7: posizione di <i>ancora</i>.</li>
<li>B: accettare ogni risposta logica con la forma corretta; chiedere un'alternativa con <i>non… ancora</i> o <i>già</i>.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: un ritorno", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>cominciare</th><th>andare avanti</th><th>reagire</th><th>finire</th></tr>
<tr><td><i>Allora, vi racconto… · Sapete una cosa? · Tutto è cominciato quando…</i></td><td><i>E poi… · A un certo punto… · Prima avevo… · E invece… · Per fortuna…</i></td><td><i>Davvero? · Non ci credo! · Poverino/a! · Che bello! · E poi?</i></td><td><i>Insomma… · Alla fine… · Non me l'aspettavo. · Morale della storia…</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi parla per due minuti di un ritorno che ricordi: da un viaggio, dalle vacanze, da un periodo all'estero.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>dov'eri stato/a e per quanto tempo</li><li>com'è andato il viaggio di ritorno</li><li>che cosa era cambiato a casa mentre non c'eri</li><li>che cosa ti mancava e che cosa ti è mancato dopo</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. Sei appena tornato/a da un viaggio. L'insegnante è un amico curioso al bar: rispondi alle sue domande e racconta.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Bentornato/a! Com'è andato il viaggio? · Avevi già visto quel posto? · Che cosa avevi preparato prima di partire? · Ti è successo qualcosa di strano? · Che cosa ti mancava? Reagire con le espressioni della tabella e chiedere sempre «E poi?».") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>È più difficile partire o tornare? Perché?</li><li>Ti piacciono le feste a sorpresa?</li><li>Secondo te, che cosa succederà tra Camila e Pietro?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>era partito / è partito</i> e <i>mi mancava</i>. Opzione fluidità (3-2-1): lo stesso racconto in 2 minuti, poi in 1 minuto.</li>
<li>B: le domande dell'insegnante sono in rosso: farne almeno una con il trapassato per obbligare lo studente a usarlo.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire un racconto informale alla velocità naturale.", "So usare il trapassato prossimo per dire che cosa era successo prima.",
          "So raccontare un viaggio o un ritorno mettendo in ordine i fatti."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Un ritorno indimenticabile.</b> Racconta un ritorno a casa: il viaggio, che cosa era successo mentre non c'eri, come ti sei sentito/a. Prima leggi il testo di Júlia.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>L'anno scorso, a febbraio, sono tornata a Bologna dopo due settimane in Brasile. Il volo era partito da Belo Horizonte con tre ore di ritardo e a Lisbona avevo perso la coincidenza. Quando finalmente sono arrivata a casa, era mezzanotte e pioveva. Ero stanchissima, ma ho avuto una bella sorpresa: la signora Rossi aveva annaffiato tutte le piante, aveva ritirato la posta e mi aveva lasciato un biglietto sulla porta: «Bentornata! Domani caffè da me». La mattina dopo le ho portato il caffè brasiliano che le avevo promesso. In quel momento ho capito che Bologna non era più una città straniera: era casa mia. Mi mancava la mia famiglia, certo, ma avevo anche una famiglia qui.</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno quattro verbi al trapassato &nbsp;☐ <i>già / non… ancora / mai</i> &nbsp;☐ <i>mi mancava / mi è mancato</i> &nbsp;☐ due espressioni utili (<i>e invece, per fortuna…</i>) &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): durante la lezione annotare 3–5 errori reali; qui lo studente scrive che cosa ha detto e la forma migliore: guidarlo prima all'autocorrezione. Questo registro continua in tutte le unità del B1.</li>
<li>C: il modello è il ritorno di Júlia dall'unità A2 08. Correggere soprattutto l'ordine dei tempi e l'ausiliare (<i>era partito</i>, <i>avevo perso</i>). Prossima unità: <i>Me lo dai?</i> (i pronomi combinati).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("01.1", "Bentornata! (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "Ripeti: l'accento della frase")}
<p>{" · ".join(S012)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 01 - Bentornata!")
