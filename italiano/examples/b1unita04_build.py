# Speak! Progresso B1 - Unità 04 "Me ne vado!" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 04", audio_json=os.path.join(HERE, "audio_it-b1-unita-04.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-04"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["04.1 Me ne vado!"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S042 = [x.split(": ", 1)[1] for x in _r["04.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 04", "Me ne vado!", "Una giornataccia · <b>i verbi pronominali</b>",
                       [("SAI FARE", "sfogarti dopo una giornata storta, mostrare comprensione, consolare e dare consigli"),
                        ("LINGUA", "Me ne vado. · Non te la prendere. · Ce l'ho con lui. · Ce l'ho fatta. · Me la sono cavata."),
                        ("PRONUNCIA", "i pronomi senza accento: «me ne vado», «ce l'ho»")])
    kw = [("una giornata in cui va tutto male", "una giornataccia"), ("dare il lavoro finito al cliente", "consegnare"),
          ("un cambiamento in un progetto", "una modifica"), ("un segno di sporco su un vestito", "una macchia"),
          ("lanciare via qualcosa", "buttare"), ("un esame in cui si parla con il professore", "un esame orale"),
          ("la persona che dirige un ufficio", "il capo"), ("una bevanda calda che calma", "la camomilla")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: giornate storte", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Guarda la foto. Che cosa è successo a questa donna, secondo te?</li><li>Qual è stata la tua ultima giornata storta?</li><li>Che cosa fai la sera, dopo una giornata difficile al lavoro?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">buttare · il capo · la camomilla · consegnare · un esame orale · una giornataccia · una macchia · una modifica</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Quando sei arrabbiato/a, ti sfoghi con qualcuno o stai da solo/a?", "1 min")}""",
    25, """<ol><li>A: lasciare parlare lo studente; se dice <i>sono andato via, mi sono arrabbiato</i>, va benissimo: alla pagina 3 scopre <i>me ne sono andato, me la sono presa</i>.</li>
<li>B: <i>giornataccia</i>: il suffisso <i>-accio</i> = negativo (<i>tempaccio, parolaccia</i>). <i>Sfogarsi</i> = <i>desabafar</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione sulle giornate storte · parole chiave del dialogo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Me ne vado! La giornataccia di Júlia</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>I verbi pronominali: andarsene, prendersela, cavarsela, avercela, farcela</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>I verbi pronominali (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Le emozioni al lavoro · falsi amici · i pronomi senza accento</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il messaggio di Júlia a Camila · trasformare le frasi</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La mia giornataccia · monologo · gioco di ruolo: un collega si sfoga</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Mercoledì 20 gennaio, sera. Il cliente di Milano, che lunedì aveva approvato il progetto, chiama e vuole cambiare tutto; il capo chiede le modifiche entro venerdì. Júlia chiude il computer con un colpo, chiede scusa a Marco («non me la prendo con te, ce l'ho con lui») e Marco la manda a casa: «ce la caviamo». Poi in tintoria: la macchia di vino sul vestito c'è ancora, Júlia se la prende con la ragazza e se ne va senza salutare. Al bar Davide racconta il suo esame orale di fisica: non sapeva niente, se l'è cavata con un sorriso e un disegno alla lavagna (24). Júlia non ce l'ha con Camila; Giulia le offre una camomilla.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese non ha verbi come <i>andarsene</i> o <i>prendersela</i>: lo studente li capisce poco e usa sempre <i>andare via, arrabbiarsi</i>. Errori tipici: <i>mi ne vado</i> (davanti a <i>ne / la</i>: <i>me, te, se, ce</i>), <i>me la ho presa</i> (ausiliare <b>essere</b>), <i>ce la ho</i> (si dice <i>ce l'ho</i>). Falso amico forte: <i>estou brava</i> = <i>sono arrabbiata / ce l'ho con…</i>; in italiano <i>brava</i> vuol dire <i>competente</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>All'università italiana molti esami sono <b>orali</b>: lo studente parla con il professore per 15-30 minuti. I voti vanno da 18 a 30 (il massimo è <i>30 e lode</i>): il 24 di Davide è un voto discreto. Al bar, quando il barista non fa pagare, si dice <i>offre la casa</i>. La camomilla è la bevanda classica per calmarsi la sera.</div>
<div class="box"><h4>AUDIO</h4>Traccia 04.1 Me ne vado! (prima naturale, poi lenta) · Traccia 04.2 Ripeti: i verbi pronominali</div>""")

    # Pagina 2 - Ascolto
    gi = [("un cliente difficile", True), ("una vacanza al mare", False), ("un vestito ancora macchiato", True), ("un esame", True), ("un trasloco", False), ("una camomilla", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Il cliente di Milano vuole cambiare tutto il progetto.", "V"), ("Júlia deve consegnare le modifiche lunedì.", "F"),
          ("In tintoria hanno tolto la macchia.", "F"), ("Júlia è stata gentile con la ragazza della tintoria.", "F"),
          ("Davide ha preso ventiquattro all'esame.", "V"), ("Júlia ce l'ha con Camila per il vestito.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Me ne vado!", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["04.1 · NATURAL", "04.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Mercoledì sera: prima allo studio, poi al bar di Giulia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "04.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Perché Júlia chiede scusa a Marco? {R("Era nervosa e sembrava arrabbiata con lui, ma ce l'ha con il cliente.") if T else ""}</li>
<li>Giulia dice: «Se il cliente vuole un progetto diverso, glielo fai diverso». È un buon consiglio? {R("Risposta libera: pragmatico, un po' ironico.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Ehi, piano! · Dai… · I clienti sono fatti così. · Che faccia! · Giornataccia? · Che figuraccia. · Le giornate storte capitano a tutti. · Offre la casa. · Che cosa farei senza di te?</i></div>""",
    27, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: cliente difficile, vestito macchiato, esame, camomilla.</li>
<li>B: 2 entro venerdì · 3 la macchia c'è ancora · 4 se l'è presa con lei e se n'è andata senza salutare · 6 non ce l'ha con Camila: è stato un incidente.</li>
<li>Espressioni: <i>Che faccia!</i> = <i>que cara é essa?</i>; <i>offre la casa</i> = <i>é por conta da casa</i>.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Adesso <u>me ne vado</u>.", "vado via"), ("Non <u>me la prendo</u> con te.", "non mi arrabbio con te"),
          ("<u>Ce l'ho</u> con lui.", "sono arrabbiata con lui"), ("Venerdì! Non <u>ce la faccio</u>.", "non riesco"),
          ("Non so come, ma <u>me la sono cavata</u>.", "sono riuscito in una situazione difficile")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:60mm')}</li>" for s, a in ex)
    bank3 = "non mi arrabbio con te · non riesco · sono arrabbiata con lui · sono riuscito in una situazione difficile · vado via"
    rules = [("Davanti a <i>ne</i> e <i>la</i>, il pronome <i>mi</i> diventa", ["me", "mi"], "me", ": <i>me ne vado, me la prendo</i>."),
             ("Al passato prossimo <i>prendersela</i> e <i>andarsene</i> usano l'ausiliare", ["essere", "avere"], "essere", "."),
             ("Al passato prossimo <i>farcela</i> usa l'ausiliare", ["avere", "essere"], "avere", ": <i>ce l'ho fatta</i>."),
             ("L'imperativo di <i>andarsene</i> con <i>tu</i> è", ["Vattene!", "Te ne vai!"], "Vattene!", "")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".").replace(" </li>", "</li>") for a, o, r, z in rules)
    cc = [("Ieri Júlia", ["se l'è presa", "l'ha presa"], "se l'è presa", "con la ragazza della tintoria."),
          ("Non", ["te la", "ti la"], "te la", "prendere, è solo un esame!"),
          ("Alla fine Davide", ["ce l'ha fatta", "ce l'è fatta"], "ce l'ha fatta", "a passare l'esame.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: i verbi pronominali", "8 min")}
{sub("A", "Frasi dal dialogo. Che cosa vuol dire il verbo sottolineato? Usa le parole del riquadro.", "3 min")}
<div class="bank">{bank3}</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la forma giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>I <b>verbi pronominali</b> hanno pronomi fissi che cambiano il significato: <i>andar<b>sene</b></i> (andare via), <i>prender<b>sela</b></i> (offendersi), <i>cavar<b>sela</b></i> (riuscire in una situazione difficile), <i>aver<b>cela</b> con</i> (essere arrabbiato con), <i>far<b>cela</b></i> (riuscire). Davanti a <i>ne / la</i>: <b>me, te, se, ce, ve</b>. Passato prossimo con <b>essere</b> (<i>me la sono presa</i>), ma <i>ce l'<b>ho</b> fatta</i>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: far notare che il significato non si capisce dalle singole parole: <i>avercela</i> non è «averla qui». Sono espressioni da imparare intere.</li>
<li>C: frase 1: <i>prendersela</i> → <i>essere</i> e participio sempre <i>-a</i> (accordo con <i>la</i>): <i>Davide se l'è presa</i>.</li></ol>""")

    grammar_ref_it.verbi_pronominali(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["perdere", "alzare", "sbattere", "fare", "mantenere", "sfogarsi"]
    rgt = ["la porta", "con un'amica", "la calma", "la pazienza", "la voce", "una scenata"]
    ans = {"perdere": "la pazienza", "alzare": "la voce", "sbattere": "la porta", "fare": "una scenata",
           "mantenere": "la calma", "sfogarsi": "con un'amica"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: le emozioni al lavoro", "4 min")}
{sub("A", "Unisci le due parti delle espressioni.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>In quali situazioni perdi la pazienza?</li><li>Hai mai sbattuto la porta?</li><li>Con chi ti sfoghi dopo una giornataccia?</li><li>Come mantieni la calma al lavoro?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Sono brava con il cliente.</td><td><b>Ce l'ho con il cliente.</b></td><td><i>brava</i> = competente, non <i>arrabbiata</i>.</td></tr>
<tr><td>Mi ne vado.</td><td><b>Me ne vado.</b></td><td>davanti a <i>ne</i>: <i>mi → me</i>.</td></tr>
<tr><td>Me la ho presa con lui.</td><td><b>Me la sono presa con lui.</b></td><td><i>prendersela</i> vuole <i>essere</i>.</td></tr>
<tr><td>Ha fatto una scena al capo.</td><td><b>Ha fatto una scenata al capo.</b></td><td><i>fazer uma cena</i> = <i>fare una scenata</i>.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: i pronomi senza accento", "4 min")}
<p class="small" style="margin:.3mm 0">I pronomi <i>me, te, ce, ne, la</i> non hanno accento: si legano al verbo come una sola parola. L'accento è solo sul verbo: <i>me ne <b>va</b>do · ce l'<b>ho</b> · non te la <b>pren</b>dere</i>. Attenzione: <i><b>vat</b>tene</i> ha l'accento sulla prima sillaba.</p>
{audiocard(["04.2"])}
{sub("A", "Ascolta e ripeti. Sottolinea la sillaba con l'accento. Poi dì le frasi con un tono arrabbiato e poi con un tono calmo.", "4 min", "04.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S042))}</p>""",
    29, """<ol><li>A: perdere d · alzare e · sbattere a · fare f · mantenere c · sfogarsi b. <i>Sfogarsi</i> = <i>desabafar</i>.</li>
<li>Pronuncia: accenti: <i>va</i>do · <i>pren</i>dere · <i>ho</i> · <i>fac</i>cio · ca<i>va</i>ta · <i>vat</i>tene. Il cambio di tono fa sentire come cambia il significato emotivo.</li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["ce l'abbiamo fatta", "ce l'abbiamo fatto"], "ce l'abbiamo fatta"), (["me la sono presa", "mi la sono presa"], "me la sono presa"),
          (["ce l'ho", "ce la ho"], "ce l'ho"), (["me ne sono andata", "mi ne sono andata"], "me ne sono andata"),
          (["se l'è presa", "l'ha presa"], "se l'è presa"), (["se l'è cavata", "l'ha cavata"], "se l'è cavata"),
          (["ce la facevo", "la facevo"], "ce la facevo"), (["ce ne andiamo", "ci ne andiamo"], "ce ne andiamo")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Sono arrabbiato con il mio vicino.", "Ce l'ho con il mio vicino."), ("Non riesco a finire tutto.", "Non ce la faccio a finire tutto."),
          ("Davide è andato via presto.", "Davide se n'è andato presto."), ("Non ti offendere!", "Non te la prendere!"),
          ("Bruno è riuscito a rispondere al professore.", "Bruno se l'è cavata con il professore."), ("Siamo riusciti a prendere il treno!", "Ce l'abbiamo fatta a prendere il treno!")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:55mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Giovedì notte Júlia scrive a Camila. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Júlia:</b> Ciao Cami! Giornata lunghissima, ma {p[0]}: domani consegniamo le modifiche. Ieri invece {p[1]} con tutti, anche con la povera ragazza della tintoria… Sì, la macchia c'è ancora, ma tranquilla: non {p[2]} con te! Stasera {p[3]} dallo studio alle undici. Marco è stato bravissimo: quando il capo {p[4]} con noi per un piccolo errore, lui {p[5]} con una battuta. Io a mezzanotte non {p[6]} più. Sabato {p[7]} tutti a Modena a mangiare le tigelle? Me lo merito!</div>
{sub("B", "Di' la stessa cosa con un verbo pronominale.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: per ogni scelta chiedere: <i>che verbo è? essere o avere?</i> Gap 1 e 7: <i>farcela</i> (ausiliare <i>avere</i>, participio <i>fatta</i>). Gap 4: <i>andarsene da un posto</i> = andare via.</li>
<li>B: frase 3: <i>se ne è andato → se n'è andato</i>. Accettare anche le forme senza <i>a + infinito</i>.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: sfogarsi e consolare", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>sfogarsi</th><th>mostrare comprensione</th><th>dare consigli</th><th>calmare</th></tr>
<tr><td><i>Che giornataccia! · Non ce la faccio più! · Ce l'ho con… · Mi ha fatto arrabbiare.</i></td><td><i>Ti capisco. · Che nervi! · Ci credo che te la sei presa. · Hai ragione.</i></td><td><i>Al posto tuo… · Perché non…? · Lascia perdere. · Parlagliene domani.</i></td><td><i>Dai, non te la prendere. · Vedrai che ce la fai. · Te la caverai. · Respira!</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi parla per due minuti della tua giornataccia peggiore.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>dov'eri e che cosa è successo</li><li>con chi te la sei presa</li><li>te ne sei andato/a o sei rimasto/a?</li><li>come te la sei cavata alla fine</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. L'insegnante è un tuo collega e ha avuto una giornataccia. Ascolta, mostra comprensione e dai consigli. Poi scambiatevi i ruoli.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Non ce la faccio più! · Il capo ce l'ha con me, ne sono sicuro/a. · Mi ha dato tre progetti per lunedì. · Domani me ne vado da questa azienda! · Forse hai ragione… Alla fine ringraziare con «Che cosa farei senza di te?».") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>È meglio sfogarsi subito o aspettare di essere calmi?</li><li>Hai mai detto «me ne vado!» a un lavoro? Lo faresti?</li><li>In Brasile, al lavoro, si mostra la rabbia o si nasconde?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>mi ne</i> e l'ausiliare di <i>prendersela</i>. Opzione fluidità (3-2-1): lo stesso racconto in 2 minuti, poi in 1 minuto.</li>
<li>B: le battute dell'insegnante sono in rosso; esagerare un po' la rabbia per far usare allo studente le espressioni per calmare.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare andarsene, prendersela, cavarsela, avercela e farcela.",
          "So sfogarmi, mostrare comprensione e consolare qualcuno."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Una settimana difficile.</b> Scrivi un messaggio a un amico o a un'amica: racconta una settimana difficile, con chi te la sei presa e come ce l'hai fatta alla fine. Prima leggi il messaggio di Marco a suo fratello Luca.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Ciao Luca, come va a Firenze? Qui settimana pesante. Mercoledì il cliente di Milano ha chiamato e ha chiesto di cambiare tutto il progetto. Júlia se l'è presa moltissimo: ha chiuso il computer così forte che ho avuto paura per lo schermo! Poi se n'è andata a casa, e ha fatto bene. Io all'inizio ce l'avevo con il capo, perché ci ha dato solo due giorni. Ieri abbiamo lavorato fino a mezzanotte, ma alla fine ce l'abbiamo fatta: stamattina abbiamo consegnato le modifiche. Il cliente ha risposto solo «Perfetto, grazie». Due parole, dopo tutto quel lavoro! Comunque ce la siamo cavata, e domani ce ne andiamo tutti a Modena a festeggiare. Vieni anche tu? Un abbraccio, Marco</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno quattro verbi pronominali &nbsp;☐ un passato con <i>essere</i> (<i>me la sono presa, me ne sono andato/a</i>) &nbsp;☐ <i>ce l'ho fatta</i> &nbsp;☐ un'espressione dell'ascolto &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far notare nel modello i passati <i>se l'è presa, se n'è andata</i> (essere) e <i>ce l'abbiamo fatta</i> (avere). Correggere soprattutto <i>me / mi</i> e l'ausiliare. Prossima unità: <i>Il Made in Italy</i> (il congiuntivo presente).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("04.1", "Me ne vado! (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("04.2", "Ripeti: i verbi pronominali")}
<p>{" · ".join(S042)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 04 - Me ne vado")
