# Speak! Progresso B1 - Unità 03 "Avrei dovuto…" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 03", audio_json=os.path.join(HERE, "audio_it-b1-unita-03.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-03"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["03.1 Avrei dovuto..."].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S032 = [x.split(": ", 1)[1] for x in _r["03.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 03", "Avrei dovuto…", "Piccoli rimpianti · <b>il condizionale passato</b>",
                       [("SAI FARE", "parlare di rimpianti e desideri non realizzati, criticare con gentilezza, scusarsi e consolare"),
                        ("LINGUA", "Avrei dovuto prenotare. · Avresti potuto dirmelo! · Al posto tuo… · Ha detto che sarebbe venuto."),
                        ("PRONUNCIA", "avremmo / avremo: la doppia che cambia il tempo")])
    kw = [("una cosa che ci dispiace non aver fatto", "un rimpianto"), ("riservare un posto o un biglietto", "prenotare"),
          ("provare imbarazzo", "vergognarsi"), ("il negozio dove lavano i vestiti", "la tintoria"),
          ("dove teniamo i soldi e le carte", "il portafoglio"), ("cominciare a dormire", "addormentarsi"),
          ("l'orologio che ci sveglia", "la sveglia"), ("il contrario di bagnato", "asciutto")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: piccoli rimpianti", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Guarda la foto. A che cosa pensa quest'uomo, secondo te?</li><li>La settimana scorsa: c'è una cosa che non hai fatto e che ti dispiace?</li><li>Sei una persona che prenota in anticipo o all'ultimo momento?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">addormentarsi · asciutto · il portafoglio · la sveglia · la tintoria · prenotare · un rimpianto · vergognarsi</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Hai mai dimenticato il portafoglio in un momento importante? Che cosa è successo?", "1 min")}""",
    25, """<ol><li>A: lasciare parlare lo studente; se usa già <i>dovevo / volevo</i> per i rimpianti, annotarlo: alla pagina 3 si scopre <i>avrei dovuto / avrei voluto</i>.</li>
<li>B: <i>vergognarsi</i> = <i>ter vergonha</i> (riflessivo: <i>mi vergogno</i>). <i>La tintoria</i> = <i>lavanderia a seco</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione sui rimpianti · parole chiave del dialogo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Avrei dovuto… Il fine settimana di Júlia, Camila e Bruno</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>Il condizionale passato: rimpianti, critiche, futuro nel passato</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il condizionale passato (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Scuse e figuracce · scelta delle parole · avremmo / avremo</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il messaggio di Pietro · che cosa avrebbero dovuto fare?</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Un rimpianto · monologo · gioco di ruolo: chiedere scusa</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Lunedì 18 gennaio, mattina, al bar di Giulia. Júlia è tornata da Milano domenica sera: il cliente ha approvato il progetto, ma non ha visto il Cenacolo perché non aveva prenotato. Camila confessa che sabato, a cena con Pietro, ha rovesciato il vino rosso sul vestito nero di Júlia; non l'ha chiamata perché si vergognava; il vestito è in tintoria fino a mercoledì. Pietro aveva detto che avrebbe pagato lui, ma aveva dimenticato il portafoglio: ha pagato Camila, che ha riso per dieci minuti. Bruno riporta la bici lunedì invece di domenica, bagnato dalla testa ai piedi: si era addormentato sul divano e aveva prestato l'ombrello a Davide. Giulia «aveva detto che sarebbe piovuto».</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese usa il condizionale semplice per il futuro nel passato (<i>ele disse que viria</i>): lo studente dice <i>ha detto che verrebbe</i>; in italiano serve il condizionale <b>passato</b> (<i>sarebbe venuto</i>). Per i rimpianti il portoghese dice <i>eu devia ter feito</i> → lo studente traduce <i>dovevo aver fatto</i>; la forma naturale è <i>avrei dovuto fare</i>. Attenzione anche all'ausiliare <i>essere</i> (<i>sarei arrivato, mi sarei arrabbiata</i>) e a <i>avremmo / avremo</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il Cenacolo di Leonardo da Vinci si trova nel refettorio di Santa Maria delle Grazie, a Milano. Per proteggere l'affresco entrano pochi visitatori per volta e per circa un quarto d'ora: i biglietti finiscono settimane prima. In Italia, al primo appuntamento è ancora comune che paghi chi ha invitato, ma tra i giovani si divide spesso il conto (<i>fare alla romana</i>).</div>
<div class="box"><h4>AUDIO</h4>Traccia 03.1 Avrei dovuto… (prima naturale, poi lenta) · Traccia 03.2 Ripeti: il condizionale passato</div>""")

    # Pagina 2 - Ascolto
    gi = [("un viaggio di lavoro", True), ("un vestito macchiato", True), ("un esame di Davide", False), ("una cena", True), ("un nuovo lavoro", False), ("la bici di Júlia", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("A Milano Júlia ha visto il Cenacolo.", "F"), ("Camila ha macchiato il vestito con il vino rosso.", "V"),
          ("Il vestito sarà pronto lunedì.", "F"), ("Alla fine della cena ha pagato Pietro.", "F"),
          ("Bruno ha riportato la bici con un giorno di ritardo.", "V"), ("Bruno aveva prestato l'ombrello a Davide.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Avrei dovuto…", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["03.1 · NATURAL", "03.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Lunedì mattina, al bar di Giulia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "03.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Perché Camila non ha chiamato Júlia sabato sera? {R("Si vergognava; aveva paura della sua reazione.") if T else ""}</li>
<li>Giulia dice: «Io avevo detto che sarebbe piovuto». Con che tono lo dice? {R("Scherzoso, un po' da «te l'avevo detto»; poi offre un cappuccino.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Un rimpianto ce l'ho. · Devo dirti una cosa. · Oddio! · Mi dispiace tantissimo! · Non è la fine del mondo. · Al posto tuo… · Lo so, lo so. · Bagnato dalla testa ai piedi.</i></div>""",
    27, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: viaggio di lavoro, vestito macchiato, cena, bici di Júlia.</li>
<li>B: 1 non c'erano più biglietti · 3 mercoledì · 4 ha pagato Camila (Pietro aveva dimenticato il portafoglio).</li>
<li>Espressioni: <i>Non è la fine del mondo</i> = <i>não é o fim do mundo</i> (uguale); <i>dalla testa ai piedi</i> = <i>da cabeça aos pés</i>.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("<u>Avrei dovuto</u> prenotarli un mese prima.", "un rimpianto"), ("<u>Avrei voluto</u> vedere il Cenacolo.", "un desiderio non realizzato"),
          ("<u>Avresti potuto</u> dirmelo subito.", "una critica"), ("Al posto tuo io <u>mi sarei arrabbiata</u>.", "che cosa avrei fatto io"),
          ("Pietro aveva detto che <u>avrebbe pagato</u> lui.", "un futuro visto dal passato")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:52mm')}</li>" for s, a in ex)
    bank3 = "che cosa avrei fatto io · un desiderio non realizzato · un futuro visto dal passato · un rimpianto · una critica"
    rules = [("Il condizionale passato si forma con il", ["condizionale", "futuro"], "condizionale", "di <i>avere</i> o <i>essere</i> + participio passato."),
             ("<i>Arrivare</i> e <i>arrabbiarsi</i> usano l'ausiliare", ["essere", "avere"], "essere", ": <i>sarei arrivato, mi sarei arrabbiata</i>."),
             ("<i>Avrei dovuto</i> parla di una cosa che", ["non ho fatto", "ho fatto"], "non ho fatto", "."),
             ("Dopo <i>ha detto che</i>, per un'azione futura si usa il condizionale", ["passato", "presente"], "passato", ".")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".") for a, o, r, z in rules)
    cc = [("Ieri Davide ha detto che", ["sarebbe passato", "passerebbe"], "sarebbe passato", "da me."),
          ("", ["Avresti dovuto", "Dovresti"], "Avresti dovuto", "studiare di più: ormai l'esame è finito."),
          ("Sabato, al posto tuo,", ["sarei rimasto", "avrei rimasto"], "sarei rimasto", "a casa.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace("<li> ", "<li>") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il condizionale passato", "8 min")}
{sub("A", "Frasi dal dialogo. Che cosa esprime il verbo sottolineato? Usa le parole del riquadro.", "3 min")}
<div class="bank">{bank3}</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la forma giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>condizionale di avere / essere + participio</b>: <i>avrei dovuto, avresti potuto, sarei arrivato, mi sarei arrabbiata</i>. Si usa per le cose che <b>non sono successe</b> (rimpianti, desideri, critiche, <i>al posto tuo</i>) e per il <b>futuro nel passato</b>: <i>ha detto che <b>sarebbe venuto</b></i> (mai <i>verrebbe</i>). Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: per ogni frase chiedere: <i>è successo o no?</i> Solo il futuro nel passato può essere successo davvero. Con i verbi di movimento si sente anche <i>sarei dovuto partire</i>: accettare entrambe le forme.</li>
<li>C: frase 2: <i>dovresti</i> = consiglio per il futuro; qui l'esame è finito, quindi <i>avresti dovuto</i>.</li></ol>""")

    grammar_ref_it.condizionale_passato(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["chiedere", "fare", "mettere", "perdere", "prenotare", "macchiare"]
    rgt = ["la sveglia alle sette", "il vestito di un'amica", "scusa a qualcuno", "un'occasione importante", "una figuraccia", "in anticipo"]
    ans = {"chiedere": "scusa a qualcuno", "fare": "una figuraccia", "mettere": "la sveglia alle sette", "perdere": "un'occasione importante",
           "prenotare": "in anticipo", "macchiare": "il vestito di un'amica"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: scuse e figuracce", "4 min")}
{sub("A", "Unisci le due parti delle espressioni.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Hai mai fatto una figuraccia al lavoro?</li><li>Hai mai perso un'occasione importante?</li><li>È difficile per te chiedere scusa?</li><li>Che cosa prenoti sempre in anticipo?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ha detto che verrebbe.</td><td><b>Ha detto che sarebbe venuto.</b></td><td>futuro nel passato = condizionale <b>passato</b>.</td></tr>
<tr><td>Dovevo aver prenotato.</td><td><b>Avrei dovuto prenotare.</b></td><td><i>devia ter feito</i> → <i>avrei dovuto fare</i>.</td></tr>
<tr><td>Pretendevo vedere il Cenacolo.</td><td><b>Volevo / Avevo intenzione di vedere…</b></td><td><i>pretendere</i> = esigere, non <i>pretender</i>.</td></tr>
<tr><td>Ho derrubato il bicchiere.</td><td><b>Ho fatto cadere il bicchiere.</b></td><td><i>derrubar</i> = <i>far cadere</i>, <i>rovesciare</i>.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: avremmo / avremo", "4 min")}
<p class="small" style="margin:.3mm 0">La consonante doppia cambia il tempo: <i>avre<b>mm</b>o</i> (condizionale) ≠ <i>avremo</i> (futuro). Lo stesso con <i>sare<b>mm</b>o / saremo</i>. Anche <i>avre<b>bb</b>e, sare<b>bb</b>e</i> hanno la doppia: tenere la consonante più a lungo.</p>
{audiocard(["03.2"])}
{sub("A", "Ascolta e ripeti. Poi l'insegnante dice una frase con «avremo» o «avremmo»: tu dici quale hai sentito.", "4 min", "03.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S032))}</p>""",
    29, """<ol><li>A: chiedere c · fare e · mettere a · perdere d · prenotare f · macchiare b. <i>Fare una figuraccia</i> = <i>pagar mico</i>.</li>
<li>Pronuncia: frasi per il gioco finale: <i>Domani avremo tempo. · Ieri avremmo avuto tempo. · Saremo a Roma. · Saremmo andati a Roma.</i></li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["Avrei dovuto", "Dovrei"], "Avrei dovuto"), (["avrei pagato", "pagherei"], "avrei pagato"),
          (["mi sarei arrabbiato", "mi avrei arrabbiato"], "mi sarei arrabbiato"), (["avresti potuto", "potresti"], "avresti potuto"),
          (["sarebbe stato meglio", "sarebbe meglio"], "sarebbe stato meglio"), (["gliel'avresti detto", "glielo diresti"], "gliel'avresti detto"),
          (["Vorrei", "Avrei voluto"], "Vorrei"), (["pagherò", "avrei pagato"], "pagherò")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Júlia non ha visto il Cenacolo.", "Avrebbe dovuto prenotare prima."), ("Bruno si è bagnato.", "Avrebbe dovuto prendere l'ombrello."),
          ("Pietro non aveva il portafoglio.", "Avrebbe dovuto controllare."), ("Camila non ha detto niente a Júlia.", "Avrebbe dovuto chiamarla subito."),
          ("Bruno non ha riportato la bici domenica.", "Avrebbe dovuto mettere la sveglia."), ("E tu? Un piccolo errore recente.", "risposta libera")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:50mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Domenica mattina Pietro scrive a Camila. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Pietro:</b> Buongiorno Camila… Ieri sera che figuraccia! {p[0]} controllare il portafoglio prima di uscire. Ti avevo detto che {p[1]} io, e invece… Al posto tuo {p[2]}, e tu invece ridevi! {p[3]} lasciarmi lì a lavare i piatti, sai? Per il vestito della tua amica: mia sorella dice che {p[4]} mettere subito il sale sulla macchia. E Júlia? Pensavo che {p[5]} subito. {p[6]} invitarti di nuovo sabato prossimo, in un posto dove il vino è bianco. Ti va? E questa volta {p[7]} io, giuro!</div>
{sub("B", "Che cosa avrebbero dovuto fare? Rispondi con il condizionale passato.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: per ogni scelta chiedere: <i>è successo? è ancora possibile?</i> Gap 6: futuro nel passato con i pronomi (<i>pensavo che gliel'avresti detto</i>). Gap 7: <i>vorrei</i> perché sabato prossimo è ancora possibile. Gap 8: una promessa per il futuro → futuro semplice.</li>
<li>B: accettare ogni risposta logica; chiedere anche <i>Che cosa avresti fatto tu al suo posto?</i></li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: rimpianti e scuse", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>rimpiangere</th><th>criticare con gentilezza</th><th>scusarsi</th><th>consolare</th></tr>
<tr><td><i>Avrei dovuto… · Avrei voluto… · Che stupido/a! · Non lo rifarei.</i></td><td><i>Avresti potuto… · Al posto tuo… · Forse sarebbe stato meglio…</i></td><td><i>Mi dispiace tantissimo. · Scusami, è colpa mia. · Non volevo… · Come posso rimediare?</i></td><td><i>Non è la fine del mondo. · Può capitare. · Dai, non ci pensare! · Succede a tutti.</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi parla per due minuti di un rimpianto, piccolo o grande.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>che cosa è successo e quando</li><li>che cosa avresti dovuto o potuto fare</li><li>che cosa avresti voluto in quel momento</li><li>che cosa hai imparato</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. L'insegnante ti ha prestato una cosa e tu l'hai rovinata. Chiedi scusa, spiega che cosa è successo e proponi una soluzione.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Allora, la mia macchina fotografica? · Che cosa è successo? · Perché non me l'hai detto subito? · Avresti potuto stare più attento/a! · E adesso come facciamo? · Va bene, ma la prossima volta… Alla fine accettare le scuse con un'espressione della tabella.") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Che cosa avresti fatto al posto di Camila?</li><li>Meglio avere rimpianti (cose non fatte) o rimorsi (cose fatte male)?</li><li>Chi deve pagare al primo appuntamento, secondo te?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>dovevo</i> al posto di <i>avrei dovuto</i> e l'ausiliare. Opzione fluidità (3-2-1): lo stesso racconto in 2 minuti, poi in 1 minuto.</li>
<li>B: le battute dell'insegnante sono in rosso; usare almeno un <i>avresti potuto</i> per obbligare lo studente a reagire con le scuse.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare il condizionale passato per rimpianti, critiche e futuro nel passato.",
          "So chiedere scusa e consolare qualcuno."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Lettera a me stesso/a.</b> Scrivi a te stesso/a di dieci anni fa: che cosa avresti dovuto fare, che cosa avresti voluto, che cosa non cambieresti. Prima leggi la lettera di Júlia.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Cara Júlia di ventidue anni, ti scrivo da Bologna. Sì, hai capito bene: tra qualche anno vivrai in Italia! Ti do qualche consiglio, perché ho dei piccoli rimpianti. Avrei dovuto cominciare a studiare l'italiano prima: il primo mese, al bar di Giulia, non capivo niente. Avrei voluto passare più tempo con la mamma e il papà, quando abitavo ancora a Belo Horizonte. All'università avrei potuto fare uno scambio in Europa, ma avevo paura. Al posto tuo sarei stata più coraggiosa. Però non cambierei la cosa più importante: quando mi hanno offerto il lavoro a Bologna, ho detto di sì. Allora pensavo che sarebbe stato difficile, e infatti lo è stato, ma è stata la scelta migliore della mia vita. Un abbraccio dal futuro, Júlia</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno quattro verbi al condizionale passato &nbsp;☐ <i>avrei dovuto / avrei voluto / avrei potuto</i> &nbsp;☐ un futuro nel passato (<i>pensavo che sarebbe…</i>) &nbsp;☐ <i>al posto tuo…</i> &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far notare nel modello il contrasto <i>non cambierei</i> (oggi) / <i>avrei dovuto</i> (allora). Correggere soprattutto l'ausiliare e il futuro nel passato. Prossima unità: <i>Me ne vado!</i> (i verbi pronominali).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("03.1", "Avrei dovuto… (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("03.2", "Ripeti: il condizionale passato")}
<p>{" · ".join(S032)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 03 - Avrei dovuto")
