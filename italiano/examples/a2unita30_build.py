# Speak! Ponte A2 - Unità 30 "Benvenuta a Bologna!" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 30", audio_json=os.path.join(HERE, "audio_it-a2-unita-30.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il passaporto", "passaporto"), ("B", "la fotocopiatrice", "fotocopiatrice"), ("C", "la fermata dell'autobus", "fermata"), ("D", "il mercatino", "mercatino"),
          ("E", "la fila", "fila"), ("F", "il modulo", "modulo"), ("G", "il calcetto", "calcetto"), ("H", "la nostalgia", "nostalgia")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-30"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["30.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S302 = [x.split(": ", 1)[1] for x in _r["30.2 Ripeti"].split("\n")]
S303 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["30.3 Che cosa"].split("\n")]


def _key(w):
    if w.startswith("l'"):
        return w[2:].lower()
    a, _, rest = w.partition(" ")
    return (rest if a in ("la", "il", "i", "gli", "lo", "le") else w).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 30", "Benvenuta a Bologna!", "Consigli per chi arriva · <b>ti consiglio di · dovresti · comprala · dimmi</b>",
                       [("SAI FARE", "dare consigli a una persona appena arrivata, parlare di documenti e uffici, incoraggiare chi si sente solo"),
                        ("LINGUA", "Ti consiglio di andarci presto. · Dovresti fare l'abbonamento. · Comprala usata! · Dimmi tutto. · Non preoccuparti!"),
                        ("PRONUNCIA", "dimmi, dammi, fammi, vacci: la consonante doppia")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: appena arrivati", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quando arrivi in una città nuova, che cosa fai prima?</li><li>Ti piace la burocrazia? Qual è l'ufficio peggiore del tuo Paese?</li><li>Hai mai avuto nostalgia di casa? Quando?</li></ol>""",
    28, """<ol><li>A: <i>la nostalgia</i> = la tristezza per una persona o un posto lontano (in portoghese <i>saudade</i>; in italiano si dice <i>ho nostalgia di casa</i>, <i>mi manca casa</i>); <i>il calcetto</i> = il calcio a cinque; <i>il mercatino</i> = il mercato delle cose usate.</li>
<li>B: domanda 2: <i>la burocrazia</i>, <i>la fila</i>, <i>il modulo</i>: parole utili per la pagina 2.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: i primi giorni in una città nuova</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Bruno conosce Camila · la telefonata</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Dare consigli · l'imperativo con i pronomi</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Ti consiglio di, dovresti · comprala, dimmi</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Dimmi, dammi, fammi · che cosa?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Dai un consiglio · imperativo + pronome · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Benvenuto nella mia città · i consigli della vita</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio ottobre. Il primo ottobre è arrivata la nuova vicina annunciata nelle unità 27 e 28: <b>Camila</b>, una ragazza brasiliana di Recife che studia Ingegneria; abita nell'appartamento del signor Neri, che si è trasferito a Milano. <b>Nuovo personaggio fisso.</b> Júlia la presenta a Bruno, che è arrivato a Bologna un anno fa (unità A1 30) e le dà i consigli che ha imparato: andare presto in segreteria, fare l'abbonamento per studenti o comprare una bici usata al mercatino, chiedere subito il codice fiscale. Una settimana dopo Camila ha perso l'abbonamento e si sente sola: Bruno la invita al calcetto del martedì e sabato al bar di Giulia. Con lui, solo italiano!</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il brasiliano dice <i>me dá, me fala, compra ela</i>: in italiano, con <i>tu</i>, il pronome si attacca alla fine (<i>dammi, dimmi, comprala</i>) e con <i>di', da', fa', va'</i> la consonante raddoppia (<i>dimmi</i>, non <i>dimi</i>). Altri errori frequenti: <i>ti consiglio andare</i> (manca <i>di</i>), <i>dovresti di studiare</i> (<i>di</i> in più) e <i>non ti preoccupi</i> detto a un amico (è la forma di <i>Lei</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Chi arriva in Italia per studiare deve chiedere subito il <b>codice fiscale</b> (all'Agenzia delle Entrate): serve per il telefono, l'affitto, il medico e la banca. Gli studenti che non hanno un passaporto europeo chiedono anche il <b>permesso di soggiorno</b> entro otto giorni dall'arrivo. A Bologna, città universitaria, molti studenti si muovono in bici e la comprano usata.</div>
<div class="box"><h4>AUDIO</h4>Traccia 30.1 I due dialoghi (lento e naturale) · Traccia 30.2 Ascolta e ripeti · Traccia 30.3 Che cosa?</div>""")

    # Page 2
    p1 = [("Camila è di", "Recife"), ("Studia", "Ingegneria"), ("In segreteria alle nove c'è già", "la fila"),
          ("Per l'autobus Bruno consiglia", "l'abbonamento annuale per studenti"), ("Bruno consiglia di comprare la bici", "usata, al mercatino")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("Camila ha perso il passaporto.", "F"), ("Per il duplicato serve un documento.", "V"), ("Camila si sente un po' sola.", "V"),
          ("Bruno gioca a calcetto il giovedì.", "F"), ("Bruno vuole parlare italiano con Camila.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: la nuova vicina", "10 min")}
{audiocard(["30.1 · SLOW", "30.1 · NATURAL"])}
{sub("A", "Prima parte. Júlia presenta Camila a Bruno. Completa.", "4 min", "30.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Camila telefona a Bruno. Vero (V) o falso (F)?", "4 min", "30.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Perché il codice fiscale è così importante?", "2 min")}
<div class="wline">{R("Perché senza il codice fiscale non puoi fare niente: né il contratto del telefono, né l'affitto.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Camila è un personaggio nuovo e tornerà: far notare che è nella stessa situazione di Bruno un anno fa.</li>
<li>B: frase 1: ha perso l'<i>abbonamento</i>. Frase 4: il <i>martedì</i>.</li></ol>""")

    # Page 3
    rules = [("<i>Ti consiglio ___ andarci presto.</i> Serve", ["di", "niente"], "di"),
             ("<i>Dovresti</i> è il verbo <i>dovere</i> al", ["condizionale", "futuro"], "condizionale"),
             ("Dopo <i>dovresti</i> si usa", ["l'infinito senza di", "di + infinito"], "l'infinito senza di"),
             ("<i>Comprala!</i> Con <i>tu</i> il pronome", ["si attacca alla fine", "va prima del verbo"], "si attacca alla fine"),
             ("<i>Dimmi, dammi</i> (di' + mi, da' + mi): la <i>m</i>", ["raddoppia", "non cambia"], "raddoppia"),
             ("<i>Non preoccuparti!</i> si dice", ["a un amico (tu)", "a un professore (Lei)"], "a un amico (tu)")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Il passaporto?", ["Portalo", "Lo porta"], "Portalo", "con te!"), ("Ti consiglio", ["di prendere", "prendere"], "di prendere", "la bici."),
          ("", ["Dammi", "Dami"], "Dammi", "il tuo numero."), ("Signora, non", ["si preoccupi", "preoccuparti"], "si preoccupi", "!")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" !", "!") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: dare consigli", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Ti consiglio di</b> andarci presto. · <b>Dovresti</b> fare l'abbonamento. · <b>Dovresti</b> iscriverti al centro sportivo. · <b>È meglio</b> la bici.<br>
2. Fai una fotocopia e <b>portala</b> con te. · <b>Comprala</b> usata. · Il codice fiscale? <b>Chiedilo</b> subito.<br>
3. <b>Dimmi</b> tutto. · <b>Dammi</b> il tuo numero. · <b>Non preoccuparti!</b> · Con me <b>non parlare</b> portoghese.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Consigli: <b>ti consiglio di</b> + infinito · <b>dovresti</b> + infinito · <b>perché non…?</b> · <b>è meglio</b> + infinito. Imperativo con <i>tu</i>: il pronome si attacca alla fine (<i>comprala, chiedilo, iscriviti</i>); con <i>di', da', fa', va'</i> la consonante raddoppia (<i>dimmi, dammi, fammi, vacci</i>). Con <i>Lei</i> il pronome va prima (<i>la compri, non si preoccupi</i>). Tutto: pagina 4.</div>""",
    22, """<ol><li>A: l'imperativo con i pronomi è nelle unità 04 (tu) e 08 (Lei): qui si usa per dare consigli.</li>
<li>B: frase 6: con <i>Lei</i>: <i>Non si preoccupi!</i> (unità 08).</li></ol>""")

    grammar_ref_it.consigli_imperativo_pronomi(b)

    # Page 5
    opts3 = [["la fotocopia", "il passaporto"], ["la tessera", "il codice fiscale"], ["la bici", "il computer"],
             ["la fila", "l'abbonamento"], ["i documenti", "le foto"], ["il biglietto", "le chiavi"]]
    ans3 = ["la fotocopia", "il codice fiscale", "la bici", "l'abbonamento", "i documenti", "le chiavi"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ti consiglio andare presto.</td><td><b>Ti consiglio di andare presto.</b></td><td><i>Consigliare di</i>.</td></tr>
<tr><td>Dovresti di studiare.</td><td><b>Dovresti studiare.</b></td><td>Dopo <i>dovresti</i>: niente <i>di</i>.</td></tr>
<tr><td>La compra usata! (a un amico)</td><td><b>Comprala usata!</b></td><td>Con <i>tu</i>: attaccato.</td></tr>
<tr><td>Dami il numero.</td><td><b>Dammi il numero.</b></td><td>La <i>m</i> raddoppia.</td></tr>
<tr><td>Non ti preoccupi! (a un amico)</td><td><b>Non preoccuparti!</b></td><td><i>Non ti preoccupi</i> non esiste.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["30.2", "30.3"])}
{sub("A", "Ascolta e ripeti. Con di', da', fa', va' la consonante del pronome è doppia: dimmi, dammi, fammi, vacci.", "2 min", "30.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S302)}</div>
{sub("B", "Che cosa? Ascolta e scegli la cosa giusta.", "2 min", "30.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    30, """<ol><li>Errori: riga 5: con un amico <i>non preoccuparti</i> (o <i>non ti preoccupare</i>); <i>non si preoccupi</i> con <i>Lei</i>.</li>
<li>4A: far tenere la doppia: <i>dim-mi</i>, <i>dam-mi</i>; l'accento resta sul verbo: <i>CÒMprala, CHIÈdilo</i>.</li>
<li>4B: <i>-la → la</i> cosa femminile, <i>-lo</i> → maschile, <i>-meli</i> = a me + loro (maschile plurale), <i>-le</i> → femminile plurale.</li></ol>""")

    # Page 6
    cs = [("Sono sempre stanco. (dormire di più)", "Dovresti dormire di più."), ("Non capisco le lezioni. (parlare con il professore)", "Ti consiglio di parlare con il professore."),
          ("Ho perso l'abbonamento. (chiedere un duplicato)", "Dovresti chiedere un duplicato."), ("Mi sento solo. (venire al bar sabato)", "Perché non vieni al bar sabato?")]
    csl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in cs)
    ip = [("Porta la fotocopia.", "Portala."), ("Chiedi il codice fiscale.", "Chiedilo."), ("Da' a me il tuo numero.", "Dammi il tuo numero."),
          ("Fa' vedere a me la tessera.", "Fammi vedere la tessera."), ("Non perdere le chiavi!", "Non perderle!")]
    ipl = "".join(f"<li>{a} → {A(c, 'min-width:40mm')}</li>" for a, c in ip)
    wb = [("consigliare", "il consiglio"), ("iscriversi", "l'iscrizione"), ("abbonarsi", "l'abbonamento"), ("fotocopiare", "la fotocopia")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Dai un consiglio. Usa dovresti, ti consiglio di o perché non…?", "4 min")}
<ol style="line-height:1.4">{csl}</ol>
{sub("B", "Una parola sola: imperativo + pronome.", "3 min")}
<ol style="line-height:1.7">{ipl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: accettare tutte e tre le strutture; controllare <i>di</i> solo dopo <i>ti consiglio</i>.</li>
<li>B: frase 5: anche <i>Non le perdere!</i> è corretto.</li>
<li>C: <i>fare l'iscrizione / iscriversi all'università</i>.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Benvenuto nella mia città! L'insegnante è uno studente straniero appena arrivato nella tua città. Dagli almeno sei consigli: casa, trasporti, documenti, cibo, amici. Poi cambiate: tu sei appena arrivato in Italia.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Ti consiglio di… · Dovresti… · Perché non…? · È meglio… · Non preoccuparti! · Chiedilo a… · Fallo subito. · Provalo! · Stai attento a… · Dimmi se hai bisogno.</div>
{sub("B", "I consigli della vita. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Hai mai vissuto in un'altra città o in un altro Paese? Chi ti ha aiutato?</li><li>Qual è il consiglio migliore che hai ricevuto? Chi te l'ha dato?</li><li>Che cosa consigli a uno straniero che arriva in Brasile?</li><li>Quando ti senti solo/a o hai nostalgia, che cosa fai?</li><li>Secondo te, che cosa dovrebbe fare Camila per conoscere gente?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: quando l'insegnante è lo straniero, fa domande con <i>Mi consigli di…? Dovrei…?</i>; quando lo straniero è lo studente, l'insegnante dà consigli con l'imperativo + pronomi.</li>
<li>B: domanda 2: <i>te l'ha dato</i> (unità 25), solo in comprensione.</li></ol>""")

    # Page 8
    pc = [("A2 · 29", "So usare voglio che, è importante che + congiuntivo."), ("A2 · 30", "So dare consigli con ti consiglio di e dovresti."),
          ("A2 · 30", "So usare l'imperativo con i pronomi (comprala, dimmi)."), ("A2 · 30", "So aiutare una persona appena arrivata."),
          ("A2 · 30", "So parlare di documenti e uffici.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ti consiglio andare in bici.", "Ti consiglio di andare in bici."), ("Perché non vieni con noi?", "✓"),
          ("Dovresti di studiare di più.", "Dovresti studiare di più."), ("Dami una mano!", "Dammi una mano!"),
          ("La compra usata! (a un amico)", "Comprala usata!"), ("Non preoccuparti!", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Una mail a Camila (50–75 parole).</b> Camila vuole visitare la tua città. Scrivile almeno cinque consigli: dove dormire, come muoversi, che cosa mangiare, che cosa vedere. Usa <i>ti consiglio di, dovresti</i> e due imperativi con il pronome (<i>provalo, visitala…</i>).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge la mail; l'insegnante fa una domanda per ogni consiglio (<i>Perché me lo consigli?</i>). Unità 31: <i>Un po' di storia</i> (i numeri ordinali, i secoli, raccontare la storia con le date).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("30.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("30.2", "Ascolta e ripeti")}
<p>{" · ".join(S302)}</p>
{sub("30.3", "Che cosa?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S303))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 30 - Benvenuta a Bologna!")
