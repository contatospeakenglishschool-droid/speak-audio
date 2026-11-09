# Speak! Ponte A2 - Unità 21 "Prima di partire" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 21", audio_json=os.path.join(HERE, "audio_it-a2-unita-21.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la valigia", "valigia"), ("B", "la crema solare", "crema solare"), ("C", "il costume", "costume"), ("D", "gli occhiali da sole", "occhiali da sole"),
          ("E", "il biglietto del treno", "biglietto del treno"), ("F", "il caricabatterie", "caricabatterie"), ("G", "i sandali", "sandali"), ("H", "annaffiare le piante", "annaffiare")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-21"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["21.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S212 = [x.split(": ", 1)[1] for x in _r["21.2 Ripeti"].split("\n")]
S213 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["21.3 Prima o dopo"].split("\n")]


def _key(w):
    w = w.split("'")[-1] if "'" in w else (w.split(" ", 1)[1] if w.split(" ", 1)[0] in ("la", "il", "i", "gli", "lo", "le") else w)
    return w.lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 21", "Prima di partire", "Le vacanze e la valigia · <b>prima di + infinito · dopo aver + participio</b>",
                       [("SAI FARE", "preparare la valigia, fare una lista di cose da fare prima di partire, mettere due azioni in ordine, raccontare un piccolo problema in viaggio"),
                        ("LINGUA", "Prima di partire, chiudo il gas. · Prima di andare a letto, metto la sveglia. · Dopo aver chiuso la porta, ho controllato tutto."),
                        ("PRONUNCIA", "l'intonazione delle liste: la crema, il costume, il cappello e gli occhiali")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: in valigia", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Dove vai in vacanza quest'estate? Al mare, in montagna, in città?</li><li>Che cosa metti sempre in valigia? Che cosa dimentichi sempre?</li><li>Fai la valigia all'ultimo momento o una settimana prima?</li></ol>""",
    28, """<ol><li>A: <i>il costume</i> = il costume da bagno; <i>il caricabatterie</i> è invariabile (un caricabatterie, due caricabatterie); <i>annaffiare</i> = dare l'acqua alle piante.</li>
<li>B: domanda 3: aspettare le risposte con <i>prima</i>: <i>La faccio prima di andare a letto</i>. Annotarle: le riprendiamo a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: la valigia</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La sera prima · la mattina alla stazione</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Prima di + infinito · dopo aver + participio</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Prima di · dopo · aver o essere</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'intonazione delle liste · prima o dopo?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Unisci le frasi · la lista di Davide · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Facciamo la valigia · le mie abitudini</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Metà luglio. Giulia e Davide partono per una settimana in Puglia; al bar c'è Matteo, il barista del fine settimana (unità 06). Giovedì sera Júlia li aiuta: la valigia di Giulia non si chiude (sei paia di scarpe!). La lista di Davide: <i>prima di partire</i> chiudere il gas, svuotare il frigorifero, buttare la spazzatura, dare le chiavi a Júlia, che annaffierà le piante due volte alla settimana (come la signora Rossi per Júlia a febbraio, unità 07). Venerdì alle 6:50 Davide telefona dalla stazione: <i>dopo aver chiuso la porta</i> ha controllato tutto tre volte, ma ha lasciato il caricabatterie sul tavolo, Giulia non ha gli occhiali da sole… e le chiavi sono ancora nella sua tasca! Le lascia a Matteo al bar; Júlia passerà a prenderle prima di andare in ufficio.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese dice <i>antes de sair</i> e <i>depois de comer</i>. Lo studente traduce: <i>prima de uscire</i> (→ <b>prima di uscire</b>) e soprattutto <i>dopo di mangiare</i> (→ <b>dopo aver mangiato</b> o <b>dopo pranzo</b>). Con i riflessivi il pronome va <b>dopo</b> l'infinito: <i>prima di me vestir</i> → <b>prima di vestirmi</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Luglio e soprattutto <b>agosto</b> sono i mesi delle vacanze: intorno a <b>Ferragosto</b> (15 agosto) molti negozi e bar chiudono e le città si svuotano. Le mete più amate sono il mare (Puglia, Sardegna, la Riviera romagnola) e la montagna. In treno si parte presto per evitare il caldo; prima di partire molti lasciano le chiavi a un vicino o a un amico per le piante e la posta.</div>
<div class="box"><h4>AUDIO</h4>Traccia 21.1 I due dialoghi (lento e naturale) · Traccia 21.2 Ascolta e ripeti · Traccia 21.3 Prima o dopo?</div>""")

    # Page 2
    p1 = [("La valigia di Giulia non si chiude: ha messo", "sei paia di scarpe"), ("Prima di partire Davide deve chiudere il gas e", "svuotare il frigorifero"),
          ("Júlia annaffia le piante", "due volte alla settimana"), ("Il treno parte alle", "sette e dieci"), ("Giulia mette la sveglia alle", "cinque e mezza")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:48mm')}</td></tr>" for a, x in p1)
    vf = [("Davide telefona a Júlia dal treno.", "F"), ("Dopo aver chiuso la porta, Davide ha controllato tutto.", "V"), ("Davide ha dimenticato il caricabatterie.", "V"),
          ("Giulia ha gli occhiali da sole nella borsa.", "F"), ("Davide lascia le chiavi a Matteo, al bar.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: la valigia non si chiude", "10 min")}
{audiocard(["21.1 · SLOW", "21.1 · NATURAL"])}
{sub("A", "Prima parte. Giovedì sera, a casa di Giulia e Davide. Completa.", "4 min", "21.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Venerdì mattina, alla stazione. Vero (V) o falso (F)?", "4 min", "21.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Quando passa Júlia al bar a prendere le chiavi?", "2 min")}
<div class="wline">{R("Prima di andare in ufficio.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. <i>Un paio, due paia</i>: plurale irregolare (lo vedremo all'unità 26).</li>
<li>B: frase 1: Davide è <b>alla stazione</b>, non ancora sul treno. Chiedere: <i>Che cosa ha dimenticato Davide? E Giulia?</i></li></ol>""")

    # Page 3
    rules = [("<i><b>Prima di</b> partire, chiudo il gas.</i> Che cosa succede prima?", ["chiudo il gas", "parto"], "chiudo il gas"),
             ("Dopo <i>prima</i> c'è sempre", ["di", "a"], "di"),
             ("Dopo <i>prima di</i> il verbo è", ["all'infinito", "coniugato"], "all'infinito"),
             ("<i>Prima di <b>andare</b> a letto, <b>metto</b> la sveglia.</i> Le due azioni sono della", ["stessa persona", "persona diversa"], "stessa persona"),
             ("<i><b>Dopo aver chiuso</b> la porta…</i> Questa azione è", ["già finita", "nel futuro"], "già finita"),
             ("<i>Dopo <b>essere</b> arrivata…</i> Si usa <i>essere</i> con i verbi che nel passato prossimo vogliono", ["essere", "avere"], "essere")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Prima", ["di", "de"], "di", "uscire, controllo i documenti."), ("Metto la crema prima di", ["andare", "vado"], "andare", "al mare."),
          ("Facciamo una passeggiata dopo", ["aver mangiato", "di mangiare"], "aver mangiato", "insieme."), ("Prima di", ["vestirmi", "mi vestire"], "vestirmi", "faccio la doccia.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: prima di / dopo", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Prima di chiudere</b> la valigia, devo decidere quali portare. · <b>Prima di partire</b>: chiudere il gas… · <b>Prima di uscire</b> di casa, controllo i documenti. · <b>Prima di andare</b> a letto, metto la sveglia. · Passo al bar <b>prima di salire</b> sul treno.<br>
2. <b>Dopo aver chiuso</b> la porta, ho controllato tutto tre volte. · <b>Dopo essere arrivata</b> alla stazione, Giulia ha visto che non ha gli occhiali.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>prima di + infinito</b>: <i>Prima di partire, chiudo il gas.</i> (stessa persona; con i riflessivi: <i>prima di vestirmi</i>). Anche <b>prima di + nome</b>: <i>prima di cena</i>. <b>dopo aver / essere + participio</b> per un'azione già finita: <i>Dopo aver chiuso la porta…</i> Tutto: pagina 4.</div>""",
    22, """<ol><li>B: regola 1: far disegnare una freccia del tempo alla lavagna: <i>chiudo il gas → parto</i>. L'azione con <i>prima di</i> viene <b>dopo</b>: confonde molti studenti.</li>
<li>C: frase 3: <i>dopo di mangiare</i> è un calco dal portoghese. Accettare anche <i>Dopo pranzo</i>.</li></ol>""")

    grammar_ref_it.prima_di_dopo(b)

    # Page 5
    ans3 = ["controllo i documenti", "faccio colazione", "metto la sveglia", "chiudo la valigia", "do le chiavi", "arrivo in albergo"]
    opts3 = [["controllo i documenti", "esco"], ["vado alla stazione", "faccio colazione"], ["metto la sveglia", "vado a letto"],
             ["chiamo un taxi", "chiudo la valigia"], ["do le chiavi", "parto"], ["faccio una doccia", "arrivo in albergo"]]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Prima de uscire, chiudo il gas.</td><td><b>Prima di uscire…</b></td><td><i>di</i>, non <i>de</i>.</td></tr>
<tr><td>Prima partire, chiamo un taxi.</td><td><b>Prima di partire…</b></td><td><i>prima</i> + verbo vuole <i>di</i>.</td></tr>
<tr><td>Prima di parto, chiudo il gas.</td><td><b>Prima di partire…</b></td><td>Dopo <i>prima di</i>: infinito.</td></tr>
<tr><td>Dopo di mangiare, esco.</td><td><b>Dopo aver mangiato…</b></td><td>Oppure: <i>Dopo pranzo…</i></td></tr>
<tr><td>Prima di mi vestire…</td><td><b>Prima di vestirmi…</b></td><td>Il pronome va dopo l'infinito.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["21.2", "21.3"])}
{sub("A", "Ascolta e ripeti. Nelle liste la voce sale a ogni parola e scende alla fine, dopo e.", "2 min", "21.2")}
<div class="bank" style="font-weight:600;background:#fff">{"<br>".join(S212)}</div>
{sub("B", "Prima o dopo? Ascolta: quale azione succede prima? Scegli.", "2 min", "21.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: <i>dopo di</i> + nome esiste solo con i pronomi (<i>dopo di me</i>); con un verbo no.</li>
<li>4A: far battere la mano su ogni parola della lista: voce in alto… in alto… e in basso sull'ultima. Utile anche per dettare la lista della spesa.</li>
<li>4B: attenzione al numero 3: <i>prima di andare a letto, metto la sveglia</i> → prima <b>metto la sveglia</b>.</li></ol>""")

    # Page 6
    un = [("Faccio la valigia. Poi parto.", "Prima di partire, faccio la valigia."), ("Chiudo le finestre. Poi esco.", "Prima di uscire, chiudo le finestre."),
          ("Metto la crema. Poi vado al mare.", "Prima di andare al mare, metto la crema."), ("Faccio colazione. Poi mi vesto.", "Prima di vestirmi, faccio colazione.")]
    unl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in un)
    ls = [("chiudere il gas", "Prima di partire chiudo il gas."), ("dare le chiavi a Júlia", "Prima di partire do le chiavi a Júlia."),
          ("buttare la spazzatura", "Prima di partire butto la spazzatura.")]
    lsl = "".join(f"<li>{q} → {A(a, 'min-width:80mm')}</li>" for q, a in ls)
    wb = [("partire", "la partenza"), ("arrivare", "l'arrivo"), ("viaggiare", "il viaggio"), ("prenotare", "la prenotazione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Unisci le due frasi con prima di.", "4 min")}
<ol style="line-height:1.45">{unl}</ol>
{sub("B", "La lista di Davide. Scrivi le frasi (io).", "3 min")}
<ol style="line-height:1.7">{lsl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: accettare anche l'ordine inverso: <i>Faccio la valigia prima di partire.</i> Frase 4: riflessivo → <i>vestirmi</i>.</li>
<li>C: <i>la partenza / l'arrivo</i> si leggono sui tabelloni della stazione (<i>Partenze / Arrivi</i>).</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Facciamo la valigia! Tu e l'insegnante partite insieme per un fine settimana (al mare, in montagna o in una città d'arte). Decidete che cosa portare e che cosa fare prima di partire. Poi raccontate il piano.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Che cosa porti? · Io porto… · Hai messo…? · Non dimenticare… · Prima di partire dobbiamo… · Prima di uscire, controlla… · Chi prenota l'albergo? · A che ora parte il treno? · Buon viaggio!</div>
{sub("B", "Le mie abitudini. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Che cosa fai sempre prima di partire per un viaggio?</li><li>Che cosa fai prima di andare a letto?</li><li>Che cosa fai prima di uscire di casa la mattina?</li><li>Che cosa fai dopo cena?</li><li>Hai mai dimenticato qualcosa di importante prima di partire? Che cosa è successo?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: l'insegnante può fare la persona disordinata (come Giulia, sei paia di scarpe) per provocare la discussione.</li>
<li>B: domanda 5 richiama l'unità 12 (Venezia, l'ombrello dimenticato): passato prossimo + imperfetto. Pretendere <i>prima di</i> + infinito nelle risposte 1–3.</li></ol>""")

    # Page 8
    pc = [("A2 · 20", "So usare i verbi + a / di (cominciare a, decidere di)."), ("A2 · 21", "So parlare delle vacanze e della valigia."),
          ("A2 · 21", "So usare prima di + infinito."), ("A2 · 21", "So capire dopo aver / essere + participio."),
          ("A2 · 21", "So fare una lista di cose da fare prima di partire.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Prima de partire, chiudo il gas.", "Prima di partire, chiudo il gas."), ("Prima di andare a letto, metto la sveglia.", "✓"),
          ("Prima di parto, faccio la valigia.", "Prima di partire, faccio la valigia."), ("Dopo di mangiare, esco.", "Dopo aver mangiato, esco."),
          ("Prima di mi vestire, faccio la doccia.", "Prima di vestirmi, faccio la doccia."), ("Dopo aver chiuso la porta, ho controllato il gas.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. La mia lista prima di partire (50–75 parole).</b> Dove vai? Che cosa metti in valigia? Che cosa devi fare prima di partire (casa, piante, documenti)? Usa almeno quattro volte <i>prima di</i> + infinito.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge la lista; l'insegnante chiede <i>E le chiavi?</i> Unità 22: <i>Che caldo!</i> (futuro di supposizione, se + futuro).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("21.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("21.2", "Ascolta e ripeti")}
<p>{" · ".join(S212)}</p>
{sub("21.3", "Prima o dopo?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S213))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 21 - Prima di partire")
