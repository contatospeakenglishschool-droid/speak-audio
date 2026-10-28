# Speak! Essenziale A1 - Unità 13 "Una giornata tipo" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 13", audio_json=os.path.join(HERE, "audio_it-a1-unita-13.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "svegliarsi", "svegliarsi"), ("B", "alzarsi", "alzarsi"), ("C", "farsi la doccia", "doccia"), ("D", "lavarsi i denti", "denti"),
          ("E", "vestirsi", "vestirsi"), ("F", "pettinarsi", "pettinarsi"), ("G", "rilassarsi", "rilassarsi"), ("H", "addormentarsi", "addormentarsi")]

SCRIPT = [("Narratore", "Dialogo uno. Allo studio, la mattina."), ("Marco", "Júlia, tu arrivi sempre presto! A che ora ti svegli?"),
          ("Júlia", "Mi sveglio alle sei e mezza. Mi alzo subito, mi faccio la doccia e mi vesto velocemente."),
          ("Marco", "Io invece mi sveglio alle otto e mi alzo lentamente… molto lentamente!"), ("Júlia", "E fai colazione?"),
          ("Marco", "Raramente. Prendo un caffè al bar e basta."),
          ("Narratore", "Dialogo due. Davide racconta la sua giornata tipo."),
          ("Davide", "Di solito mi sveglio tardi, verso le dieci. Mi lavo, mi vesto e vado all'università in bicicletta. Il pomeriggio studio in biblioteca. La sera mi rilasso con gli amici e mi addormento verso l'una."),
          ("Narratore", "Dialogo tre. Al bar."), ("Júlia", "Giulia, a che ora ti alzi?"), ("Giulia", "Mi alzo alle cinque!"), ("Júlia", "Alle cinque?"),
          ("Giulia", "Sì. Mi preparo velocemente e alle sei apro il bar. Il pomeriggio mi riposo un'ora."), ("Júlia", "E la domenica?"),
          ("Giulia", "La domenica mi sveglio tranquillamente alle undici. Finalmente!")]
S132 = ["velocemente", "lentamente", "tranquillamente", "normalmente", "raramente", "finalmente", "Mi vesto velocemente."]
S133 = ["Di solito mi sveglio alle sette.", "Mi alzo subito.", "Mi faccio la doccia.", "Mi vesto e faccio colazione.", "La sera mi rilasso.", "Mi addormento verso mezzanotte."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 13", "Una giornata tipo", "Le abitudini di ogni giorno · <b>mi sveglio, mi alzo, mi vesto</b>",
                       [("SAI FARE", "descrivere la tua giornata tipo nei dettagli e dire con che frequenza fai le cose"), ("LINGUA", "verbi riflessivi · velocemente, lentamente · sempre, spesso, raramente"),
                        ("PRONUNCIA", "l'accento degli avverbi in -mente · frasi della routine")])
    words = ["addormentarsi", "alzarsi", "farsi la doccia", "lavarsi i denti", "pettinarsi", "rilassarsi", "svegliarsi", "vestirsi"]
    b.page(f"""{sec(1, "Riscaldamento: la mattina e la sera", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi l'azione sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "E tu? Metti in ordine la tua mattina (1–6). Poi racconta all'insegnante.", "4 min")}
<div class="two"><div class="bank" style="background:#fff;line-height:1.9">☐ mi sveglio &nbsp; ☐ mi alzo &nbsp; ☐ faccio colazione<br>☐ mi faccio la doccia &nbsp; ☐ mi vesto &nbsp; ☐ esco di casa</div>
<div class="wline">{R("Risposta libera. Esempio: 1 mi sveglio, 2 mi alzo, 3 mi faccio la doccia, 4 mi vesto, 5 faccio colazione, 6 esco di casa.")}</div></div>""",
    24, """<ol><li>A: i verbi sono all'infinito con <b>-si</b>: <i>alzar<b>si</b>, sveglia<b>rsi</b></i>. Nella frase il <i>si</i> diventa <i>mi / ti / si</i> (pagina 3).</li>
<li>B: lo studente racconta con <i>prima… poi… dopo…</i> L'unità 5 ha già <i>vado, esco, finisco</i>: ripassarli.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 azioni della routine (riflessive) con foto · la mia mattina</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Le giornate di Júlia, Marco, Davide e Giulia: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Verbi riflessivi · avverbi in <i>-mente</i> · avverbi di frequenza</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>L'accento degli avverbi in <i>-mente</i> · frasi della routine</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Riflessivi · avverbi · frequenza</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Quiz: sei mattiniero o nottambulo? · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 10–13) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Marco scopre perché Júlia arriva sempre presto allo studio: si sveglia alle sei e mezza! Lui invece si alza lentamente e raramente fa colazione. Davide racconta la sua giornata da studente (si addormenta verso l'una). Giulia si alza alle cinque per aprire il bar, ma la domenica si sveglia alle undici: «Finalmente!»</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Io alzo alle sette</i> ✗ → <b>Mi alzo alle sette</b>. <i>Me alzo</i> ✗ → <b>Mi alzo</b> (in italiano: <i>mi</i>, non <i>me</i>). <i>Tu si svegli?</i> ✗ → <b>Ti svegli?</b> <i>Velocemento</i> ✗ → <b>velocemente</b>. <i>Io mai mi alzo tardi</i> ✗ → <b>Non mi alzo mai tardi</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 13.1 Tre dialoghi (lento e naturale) · Traccia 13.2 Gli avverbi in -mente · Traccia 13.3 La routine</div>""")

    # Page 2
    tb = [("Júlia", "6:30", "si alza subito, si fa la doccia, si veste velocemente"), ("Marco", "8:00", "si alza lentamente, prende un caffè al bar"),
          ("Davide", "10:00", "si lava, si veste, va all'università in bici"), ("Giulia", "5:00", "si prepara velocemente, apre il bar alle sei")]
    tr_ = "".join(f"<tr><td style='width:22mm'><b>{n}</b></td><td style='width:26mm'>{A(h, 'min-width:16mm')}</td><td>{A(x, 'min-width:70mm')}</td></tr>" for n, h, x in tb)
    tf = [("Marco fa sempre colazione.", "F"), ("Davide la sera si rilassa con gli amici.", "V"), ("Giulia il pomeriggio si riposa un'ora.", "V"), ("La domenica Giulia si alza alle cinque.", "F")]
    tfr = "".join(f'<tr><td>{i+1}. {s}</td><td style="width:24mm;text-align:center;white-space:nowrap">{ch(["V", "F"], a)}</td></tr>' for i, (s, a) in enumerate(tf))
    b.page(f"""{sec(2, "Ascolto: a che ora ti alzi?", "10 min")}
<p>Ognuno ha la sua giornata: Júlia, Marco, Davide e Giulia raccontano le loro abitudini.</p>
{audiocard(["13.1 · SLOW", "13.1 · NATURAL"])}
{sub("A", "Ascolta. A che ora si sveglia o si alza? Che cosa fa?", "5 min", "13.1 · SLOW")}
<table style="margin:0"><tr><th>Chi?</th><th>Ora</th><th>Che cosa fa?</th></tr>{tr_}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "3 min", "13.1 · NATURAL")}
<table class="ck" style="margin:0">{tfr}</table>
{sub("C", "Chi ha la giornata più simile alla tua? Perché?", "2 min")}
<div class="wline">{R("Risposta libera: «La mia giornata è come quella di Júlia, perché anche io mi alzo presto.»")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi. Far notare la terza persona: <i>Júlia <b>si</b> alza</i>.</li>
<li>B: versione <b>naturale</b>. 1 → <i>raramente</i>; 4 → <i>la domenica si sveglia alle undici</i>. <i>E basta</i> = niente altro.</li></ol>""")

    # Page 3
    rf = [("io", "mi", "alzo", "vesto"), ("tu", "ti", "alzi", "vesti"), ("lui / lei / Lei", "si", "alza", "veste")]
    trf = "".join(f"<tr><td>{p}</td><td><b>{x}</b></td><td>{y}</td><td>{z}</td></tr>" for p, x, y, z in rf)
    av = [("veloce", "velocemente"), ("lento", "lentamente"), ("tranquillo", "tranquillamente"), ("normale", "normalmente"), ("raro", "raramente")]
    tav = "".join(f"<tr><td>{a}</td><td><b>{x}</b></td></tr>" for a, x in av)
    fq = "<b>sempre</b> 100% · <b>di solito</b> · <b>spesso</b> · <b>qualche volta</b> · <b>raramente</b> · <b>non… mai</b> 0%"
    rules = [("", "Mi alzo alle sette.", "Io alzo alle sette."), ("Tu a che ora", "ti svegli", "si svegli"), ("Marco si veste", "lentamente", "lentomente"), ("", "Non mi alzo mai tardi.", "Mai mi alzo tardi.")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: verbi riflessivi · avverbi", "10 min")}
<div class="two"><div>{sub("A", "I verbi riflessivi.", "3 min")}
<table style="margin:0"><tr><th></th><th></th><th>alzarsi</th><th>vestirsi</th></tr>{trf}</table>
<p class="small" style="margin-top:1mm">Anche: svegliarsi, lavarsi, farsi la doccia, prepararsi, riposarsi, rilassarsi, addormentarsi.</p></div>
<div>{sub("B", "Aggettivo → avverbio in -mente.", "3 min")}<table style="margin:0">{tav}</table>
<p class="small" style="margin-top:1mm">-o → <b>-amente</b> (lento → lentamente) · -e → <b>-emente</b> (veloce → velocemente) · -le → <b>-lmente</b> (normale → normalmente)</p></div></div>
{sub("C", "La frequenza.", "1 min")}
<div class="bank" style="background:#fff">{fq}</div>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>REGOLA</h4>Il pronome <b>mi / ti / si</b> va prima del verbo: <i>Mi sveglio. Non mi sveglio.</i> Con <b>farsi la doccia</b>: <i>mi faccio, ti fai, si fa la doccia</i>. Gli avverbi in <i>-mente</i> vanno dopo il verbo: <i>Mi vesto <b>velocemente</b></i>.</div>""",
    25, """<ol><li>A: <i>Lei si alza</i> (formale) e <i>lei si alza</i> (Giulia) hanno la stessa forma. <i>Svegliarsi</i> ≠ <i>alzarsi</i>: prima apro gli occhi, poi esco dal letto.</li>
<li>B/C: chiedere subito: <i>Fai colazione velocemente o tranquillamente? Spesso o raramente?</i></li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Io alzo alle sette.</td><td><b>Mi alzo alle sette.</b></td><td><i>alzarsi</i> ha il pronome.</td></tr>
<tr><td>Me sveglio presto.</td><td><b>Mi sveglio presto.</b></td><td>In italiano: <i>mi</i>.</td></tr>
<tr><td>Tu si vesti velocemente?</td><td><b>Ti vesti velocemente?</b></td><td>tu = <i>ti</i>.</td></tr>
<tr><td>Mi vesto velocemento.</td><td><b>Mi vesto velocemente.</b></td><td>Avverbi: <i>-mente</i>.</td></tr>
<tr><td>Io mai mi sveglio tardi.</td><td><b>Non mi sveglio mai tardi.</b></td><td><i>non</i> + verbo + <i>mai</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["13.2", "13.3"])}
{sub("A", "Gli avverbi in -mente. Ascolta e ripeti: l'accento è su MEN.", "2 min", "13.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S132)}</div>
{sub("B", "La routine. Ascolta e ripeti.", "3 min", "13.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S133)}</div>""",
    38, """<ol><li>Errori: <i>me</i> e <i>se</i> vengono dal portoghese. In italiano: <i>mi, ti, si</i>.</li>
<li>4A: veloce<b>MEN</b>te, lenta<b>MEN</b>te: l'accento è sempre su <i>-men-</i>. Battere le mani sulla sillaba forte.</li>
<li>4B: <i>mi alzo</i> si pronuncia quasi come una parola sola: «mialzo».</li></ol>""")

    # Page 5
    rw = [("Io", "mi sveglio", "alle sette.", "svegliarsi"), ("Tu a che ora", "ti alzi", "?", "alzarsi"), ("Marco", "si fa", "la doccia la sera.", "farsi"),
          ("Giulia", "si prepara", "velocemente.", "prepararsi"), ("Io la sera", "mi rilasso", "con un libro.", "rilassarsi"), ("Signora, Lei", "si riposa", "il pomeriggio?", "riposarsi")]
    rl = "".join(f'<li>{a} {A(v, "min-width:24mm")} {c} <span class="small">({n})</span></li>' for a, v, c, n in rw)
    aw = [("tranquillo", "tranquillamente"), ("lento", "lentamente"), ("veloce", "velocemente"), ("normale", "normalmente"), ("raro", "raramente"), ("finale", "finalmente")]
    al_ = [f'<li value="{i+1}">{a} → {A(x, "min-width:30mm")}</li>' for i, (a, x) in enumerate(aw)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con il verbo riflessivo.", "3 min")}
<ol>{rl}</ol>
{sub("B", "Scrivi l'avverbio.", "2 min")}
{twocol(al_, 4)}
{sub("C", "E tu? Scrivi 3 frasi con sempre, spesso, raramente o non… mai.", "3 min")}
<div class="wline">{R("Esempio: Mi alzo sempre alle sette. Mi faccio spesso la doccia la sera. Non mi addormento mai prima di mezzanotte.")}</div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: 3 <i>farsi la doccia</i>: <i>si fa</i> (verbo <i>fare</i> irregolare). B: 6 <i>finalmente</i> = alla fine, dopo tanto tempo.</li>
<li>C: lo studente legge; l'insegnante reagisce: <i>Anche io! / Io no, io…</i></li></ol>""")

    # Page 6
    qz = [("A che ora ti svegli nei giorni di lavoro?", "prima delle 7", "dopo le 7"), ("Ti alzi subito?", "sì, subito", "no, lentamente"), ("Fai colazione?", "sempre", "raramente / mai"),
          ("Ti fai la doccia la mattina o la sera?", "la mattina", "la sera"), ("A che ora ti addormenti?", "prima delle 23", "dopo mezzanotte"), ("La domenica ti svegli presto?", "sì, sempre", "no, mai")]
    qr = "".join(f"<tr><td>{i+1}. {q}</td><td style='width:34mm'>☐ {a}</td><td style='width:34mm'>☐ {bb}</td></tr>" for i, (q, a, bb) in enumerate(qz))
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Quiz: sei mattiniero o nottambulo? Fai le domande all'insegnante e segna. Poi rispondi tu.", "7 min")}
<table style="margin:1mm 0 2mm"><tr><th>Domanda</th><th>☀ mattiniero</th><th>☾ nottambulo</th></tr>{qr}</table>
<div class="box"><h4>RISULTATO</h4>Più risposte ☀ = sei <b>mattiniero</b> (come Júlia e Giulia). Più risposte ☾ = sei <b>nottambulo</b> (come Davide).</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Com'è la tua giornata tipo?</li><li>Che cosa fai velocemente e che cosa fai tranquillamente?</li><li>Che cosa fai spesso il fine settimana?</li><li>Che cosa non fai mai la mattina?</li></ol>""",
    26, """<ol><li>A: <i>mattiniero</i> = persona che si alza presto; <i>nottambulo</i> = persona che va a dormire tardi. L'insegnante risponde con frasi complete (<i>Mi sveglio alle sei e mezza</i>).</li>
<li>B: correggere la posizione di <i>mi / ti / si</i> e di <i>non… mai</i>.</li></ol>""")

    # Page 7
    pc = [("Unità 10", "So comprare il cibo al mercato."), ("Unità 11", "So raccontare il mio fine settimana."), ("Unità 12", "So spiegare una ricetta semplice."),
          ("Unità 13", "So descrivere la mia giornata con i verbi riflessivi."), ("Unità 13", "So usare gli avverbi in -mente e di frequenza.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Io sveglio alle sei.", "Mi sveglio alle sei."), ("Me faccio la doccia la sera.", "Mi faccio la doccia la sera."), ("Tu si alzi presto?", "Tu ti alzi presto?"),
          ("Marco si veste lentomente.", "Marco si veste lentamente."), ("Io mai mi addormento presto.", "Non mi addormento mai presto."), ("Giulia mi riposa il pomeriggio.", "Giulia si riposa il pomeriggio.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La mia giornata tipo.</b> Scrivi 6 frasi sulla tua giornata con almeno 4 verbi riflessivi e 2 avverbi (<i>velocemente, spesso…</i>).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante fa domande sulla giornata dello studente: <i>E dopo? Ti vesti velocemente?</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("13.1", "A che ora ti alzi? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("13.2", "Gli avverbi in -mente")}
<p>{" · ".join(S132)}</p>
{sub("13.3", "La routine")}
<p>{" ".join(S133)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 13 - Una giornata tipo")
