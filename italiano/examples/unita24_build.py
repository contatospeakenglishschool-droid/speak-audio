# Speak! Essenziale A1 - Unità 24 "Lo sport" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
setup(band="A1 · UNITÀ 24", audio_json=os.path.join(HERE, "audio_it-a1-unita-24.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il calcio", "calcio"), ("B", "il nuoto", "nuoto"), ("C", "la pallavolo", "pallavolo"), ("D", "il tennis", "tennis"),
          ("E", "la corsa", "corsa"), ("F", "il ciclismo", "ciclismo"), ("G", "lo yoga", "yoga"), ("H", "lo sci", "sci")]

SCRIPT = [("Narratore", "Dialogo uno. Allo studio."), ("Marco", "Júlia, che sport fai?"),
          ("Júlia", "Faccio nuoto due volte alla settimana. E qualche volta corro ai Giardini Margherita."), ("Marco", "Brava! E sai giocare a calcio?"),
          ("Júlia", "Certo, sono brasiliana! Gioco spesso con le mie amiche."),
          ("Marco", "Perfetto! Giovedì sera giochiamo a calcetto con i colleghi e manca una persona. Vieni?"), ("Júlia", "Volentieri! A che ora?"),
          ("Marco", "Alle otto, al campo vicino allo studio. Ah, l'ingegnere Ferri gioca in porta!"),
          ("Narratore", "Dialogo due. Sulle scale."), ("Davide", "Júlia, vai in piscina? Posso venire con te?"), ("Júlia", "Certo! Ma tu sai nuotare?"),
          ("Davide", "Ehm… no, non so nuotare. Sono di Napoli, vado sempre al mare, ma non nuoto mai! Gioco solo a pallavolo sulla spiaggia."),
          ("Júlia", "Allora fai un corso! In piscina c'è un corso per adulti il martedì e il giovedì."),
          ("Davide", "Il giovedì gioco a basket con l'università. Il martedì va bene."), ("Júlia", "Perfetto! In un mese sai nuotare."),
          ("Narratore", "Dialogo tre. Al bar."), ("Giulia", "Buongiorno, signora Rossi! Come mai in tuta?"),
          ("Signora Rossi", "Ogni mattina cammino un'ora in collina. E il lunedì e il mercoledì faccio yoga."), ("Giulia", "Ogni mattina? Io non faccio mai sport!"),
          ("Signora Rossi", "Mai? Neanche una passeggiata?"), ("Giulia", "Raramente. Però guardo sempre il Bologna in televisione!"),
          ("Signora Rossi", "Guardare il calcio non è uno sport, cara!"), ("Giulia", "Per me sì: soffro tantissimo!")]
S242 = ["caro, carro", "coro, corro", "sera, serra", "tori, torri", "correre, la corsa", "Corro ogni sera ai Giardini."]
S243 = ["Che sport fai?", "Faccio nuoto due volte alla settimana.", "Gioco a calcio con i colleghi.", "Sai nuotare? No, non so nuotare.", "Non faccio mai sport.",
        "Cammino ogni mattina."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 24", "Lo sport", "Sport e tempo libero · <b>gioco a calcio, faccio nuoto, non so sciare</b>",
                       [("SAI FARE", "parlare degli sport che fai, di quello che sai fare e di quante volte lo fai"),
                        ("LINGUA", "giocare a / fare · sapere + infinito · sempre, spesso, qualche volta, raramente, non… mai"),
                        ("PRONUNCIA", "R e RR: caro / carro, coro / corro · parlare di sport")])
    words = [w for _, w, _ in PHOTOS]
    gf = [("calcio", "gioco a"), ("nuoto", "faccio"), ("pallavolo", "gioco a"), ("yoga", "faccio"), ("tennis", "gioco a"), ("sci", "faccio")]
    gfl = [f'<li value="{i+1}">{A(v, "min-width:22mm")} {s}</li>' for i, (s, v) in enumerate(gf)]
    b.page(f"""{sec(1, "Riscaldamento: che sport?", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi lo sport sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Gioco a o faccio? Completa.", "4 min")}
{twocol(gfl, 4)}""",
    26, """<ol><li>A: <i>lo yoga, lo sci</i> (articolo <i>lo</i> davanti a Y e S + consonante). <i>La pallavolo</i> è femminile. Chiedere: <i>Qual è lo sport più popolare in Brasile? E in Italia?</i></li>
<li>B: con gli sport di squadra e con la palla si usa <b>giocare a</b>; con gli altri <b>fare</b>. La regola è a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto di sport · gioco a / faccio</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il calcetto dei colleghi · il corso di nuoto · la signora Rossi in tuta</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>giocare a / fare · sapere + infinito · gli avverbi di frequenza</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>R e RR · parlare di sport</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>La settimana sportiva · completare le frasi</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Sai…? Trova qualcuno · la tua settimana · lo sport in Brasile</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Júlia fa nuoto due volte alla settimana e qualche volta corre ai Giardini Margherita. Marco la invita al calcetto dei colleghi del giovedì (in porta c'è l'ingegnere Ferri, unità 20). Davide è di Napoli ma non sa nuotare: farà il corso per adulti il martedì, perché il giovedì gioca a basket. La signora Rossi cammina ogni mattina e fa yoga; Giulia non fa mai sport… ma «soffre» guardando il Bologna in TV.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Gioco calcio</i> ✗ → <b>gioco a calcio</b>. <i>Pratico nuoto</i> → più naturale <b>faccio nuoto</b>. <i>Posso nuotare</i> per un'abilità ✗ → <b>so nuotare</b>. <i>Mai faccio sport</i> ✗ → <b>non faccio mai sport</b>. <i>Vado all'accademia</i> ✗ → <b>vado in palestra</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il <b>calcetto</b> (calcio a cinque) è lo sport degli amici e dei colleghi, la sera dopo il lavoro. Il calcio è una passione: si «tifa» per la squadra della propria città (il <b>Bologna</b>, il Napoli…). In Italia la <b>pallavolo</b> è molto popolare, soprattutto tra le ragazze, e d'inverno molti vanno a sciare sulle Alpi e sugli Appennini.</div>
<div class="box"><h4>AUDIO</h4>Traccia 24.1 Tre dialoghi (lento e naturale) · Traccia 24.2 R e RR · Traccia 24.3 Parlare di sport</div>""")

    # Page 2
    who = [("Júlia", "nuoto · corsa · calcio", "due volte alla settimana (nuoto)"), ("Davide", "pallavolo · basket", "il giovedì (basket)"),
           ("Signora Rossi", "camminare · yoga", "ogni mattina · il lunedì e il mercoledì"), ("Giulia", "niente!", "non fa mai sport")]
    whr = "".join(f"<tr><td style='width:28mm'><b>{n}</b></td><td>{A(s, 'min-width:52mm')}</td><td>{A(q, 'min-width:60mm')}</td></tr>" for n, s, q in who)
    vf = [("Il calcetto dei colleghi è giovedì alle otto.", "V"), ("Davide sa nuotare bene.", "F"), ("Il corso di nuoto per adulti è il martedì e il giovedì.", "V"),
          ("La signora Rossi cammina in collina ogni sera.", "F"), ("Giulia guarda sempre il Bologna in TV.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: che sport fai?", "10 min")}
<p>Allo studio, sulle scale e al bar: chi fa sport e chi no?</p>
{audiocard(["24.1 · SLOW", "24.1 · NATURAL"])}
{sub("A", "Ascolta e completa: che sport fanno? Quando?", "5 min", "24.1 · SLOW")}
<table style="margin:0"><tr><th></th><th>Sport</th><th>Quando? Quante volte?</th></tr>{whr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "3 min", "24.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Perché Davide non va al corso di nuoto il giovedì?", "2 min")}
<div class="wline">{R("Perché il giovedì gioca a basket con l'università.")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi. <i>Giocare in porta</i> = fare il portiere. <i>Manca una persona</i> = c'è bisogno di un'altra persona.</li>
<li>B: versione <b>naturale</b>. 2: Davide <b>non sa nuotare</b>. 4: <b>ogni mattina</b>. <i>Come mai…?</i> = perché? <i>In tuta</i> = con i vestiti per lo sport.</li></ol>""")

    # Page 3
    gf2 = [("<b>giocare a</b> + sport con la palla", "giocare a calcio, a tennis, a pallavolo, a basket"), ("<b>fare</b> + gli altri sport", "fare nuoto, yoga, sci, ciclismo, ginnastica"),
           ("<b>andare</b>", "andare in piscina, in palestra, in bici, a correre")]
    tgf = "".join(f"<tr><td style='width:52mm'>{a}</td><td>{x}</td></tr>" for a, x in gf2)
    con = [("io", "gioco", "so"), ("tu", "gio<b>ch</b>i", "sai"), ("lui / lei", "gioca", "sa"), ("noi", "gio<b>ch</b>iamo", "sappiamo"), ("voi", "giocate", "sapete"),
           ("loro", "giocano", "sanno")]
    tcon = "".join(f"<tr><td><b>{p}</b></td><td>{g}</td><td>{s}</td></tr>" for p, g, s in con)
    fr = ["<b>sempre</b>", "<b>spesso</b>", "<b>qualche volta</b>", "<b>raramente</b>", "<b>non</b> … <b>mai</b>"]
    rules = [("Marco gioca ", "a calcio", "calcio", ""), ("Júlia ", "fa", "gioca a", " nuoto."), ("Davide non ", "sa", "può", " nuotare: non ha mai imparato."),
             ("Giulia ", "non fa mai", "mai fa", " sport."), ("Tu ", "giochi", "gioci", " a tennis?")]
    rl = "".join(f"<li>{a}<i>{ch([r, w] if i % 2 == 0 else [w, r], r)}</i>{z}</li>" for i, (a, r, w, z) in enumerate(rules))
    b.page(f"""{sec(3, "Grammatica: parlare di sport", "10 min")}
{sub("A", "Giocare a, fare, andare.", "3 min")}
<table style="margin:0">{tgf}</table>
<div class="two"><div>{sub("B", "Giocare e sapere.", "3 min")}
<table style="margin:0"><tr><th></th><th>giocare</th><th>sapere</th></tr>{tcon}</table>
<p class="small" style="margin-top:1mm"><b>sapere</b> + infinito = un'abilità: <i>So nuotare. Non so sciare.</i><br><b>potere</b> = è possibile: <i>Oggi non posso nuotare, ho il raffreddore.</i></p></div>
<div>{sub("C", "Quante volte?", "2 min")}
<p style="line-height:1.7">{" → ".join(fr)}</p>
<p class="small">Gioco <b>spesso</b> a calcio. · <b>Non</b> faccio <b>mai</b> sport.<br><b>ogni</b> giorno / mattina · <b>due volte alla</b> settimana · <b>il</b> lunedì = ogni lunedì</p></div></div>
{sub("D", "Scegli l'opzione corretta.", "2 min")}
<ol>{rl}</ol>""",
    28, """<ol><li>A: <i>giocare</i> è <b>a</b> + sport (non c'è l'articolo: <i>gioco a calcio</i>). Con <i>fare</i> nessuna preposizione: <i>faccio nuoto</i>.</li>
<li>B: <i>giochi, giochiamo</i> con la H per tenere il suono duro. <i>Sapere</i> e <i>potere</i> in portoghese sono spesso uguali (<i>posso nadar</i>): in italiano no. C: <i>mai</i> va dopo il verbo, con <i>non</i> prima.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Gioco calcio il giovedì.</td><td><b>Gioco a calcio il giovedì.</b></td><td><i>giocare a</i> + sport.</td></tr>
<tr><td>Gioco a nuoto.</td><td><b>Faccio nuoto.</b></td><td>Senza palla: <i>fare</i>.</td></tr>
<tr><td>Davide non può nuotare.</td><td><b>Davide non sa nuotare.</b></td><td>Abilità: <i>sapere</i>.</td></tr>
<tr><td>Mai faccio sport.</td><td><b>Non faccio mai sport.</b></td><td><i>non</i> + verbo + <i>mai</i>.</td></tr>
<tr><td>Vado all'accademia.</td><td><b>Vado in palestra.</b></td><td><i>academia</i> → <i>palestra</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["24.2", "24.3"])}
{sub("A", "R e RR. Ascolta e ripeti: la RR è più lunga e più forte. Attenzione, cambia il significato!", "2 min", "24.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S242)}</div>
{sub("B", "Parlare di sport. Ascolta e ripeti.", "3 min", "24.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S243)}</div>""",
    40, """<ol><li>Errori: <i>academia</i> in italiano è l'università o un'istituzione culturale (<i>l'Accademia di Belle Arti</i>). Per fare ginnastica: <b>la palestra</b>.</li>
<li>4A: <i>caro</i> = che costa molto / affettuoso, <i>carro</i> = un veicolo; <i>coro</i> = gruppo che canta, <i>corro</i> = verbo <i>correre</i>; <i>sera / serra</i>; <i>tori / torri</i>. La R italiana vibra (unità 07); la RR vibra più a lungo. Mai la R «aspirata» del portoghese di Rio.</li></ol>""")

    # Page 5
    days = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
    wk = [("Júlia", ["nuoto", "", "", "calcetto", "nuoto", "corsa", ""]), ("Davide", ["", "corso di nuoto", "", "basket", "", "pallavolo", ""]),
          ("Sig.ra Rossi", ["camminare + yoga", "camminare", "camminare + yoga", "camminare", "camminare", "camminare", "camminare"]),
          ("Giulia", ["", "", "", "", "", "", "il Bologna in TV"])]
    cell = lambda t: f"<td style='font-size:8pt;text-align:center;background:{'#E3F0F2' if t else '#fff'}'>{t}</td>"
    wkr = "".join(f"<tr><td style='width:22mm'><b>{n}</b></td>{''.join(cell(t) for t in r)}</tr>" for n, r in wk)
    qs = [("Quante volte alla settimana Júlia fa nuoto?", "Due volte alla settimana."), ("Che cosa fa Davide il giovedì?", "Gioca a basket."),
          ("Quando cammina la signora Rossi?", "Ogni giorno (ogni mattina)."), ("Giulia fa sport?", "No, non fa mai sport. Guarda il Bologna in TV.")]
    ql = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in qs)
    cp = [("Marco e i colleghi", "giocano", "giocare"), ("Io non", "so", "sapere"), ("Voi", "fate", "fare"), ("Tu", "giochi", "giocare"), ("Noi non", "sappiamo", "sapere")]
    cpz = ["a calcetto il giovedì.", "sciare.", "yoga la mattina?", "a tennis con Luca?", "nuotare."]
    cpl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")} {z} <span class="small">({v})</span></li>' for i, ((a, x, v), z) in enumerate(zip(cp, cpz))]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "La settimana sportiva. Guarda la tabella e rispondi.", "5 min")}
<table style="margin:1mm 0 2mm"><tr><th></th>{"".join(f"<th style='text-align:center'>{d}</th>" for d in days)}</tr>{wkr}</table>
<ol>{ql}</ol>
{sub("B", "Completa con il verbo.", "3 min")}
{twocol(cpl, 4)}""",
    22, """<ol><li>A: far rispondere con frasi complete. Domanda extra: <i>Chi fa sport più spesso?</i> (la signora Rossi!).</li>
<li>B: attenzione a <i>giochi</i> con la H e a <i>sappiamo</i> con la doppia P.</li></ol>""")

    # Page 6
    fs = ["nuotare", "sciare", "giocare a tennis", "andare in bici", "ballare la samba", "giocare a scacchi"]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Sai…? Fai le domande all'insegnante e rispondi anche tu: sì, so… / no, non so…", "4 min")}
<table style="margin:1mm 0 2mm"><tr><th>Sai…?</th><th style="width:24mm">Io</th><th style="width:24mm">L'insegnante</th></tr>
{"".join(f"<tr><td>{x}</td><td></td><td></td></tr>" for x in fs)}</table>
{sub("B", "La tua settimana. Racconta all'insegnante che sport fai e quante volte (sempre, spesso, qualche volta, mai). Se non fai sport, che cosa fai nel tempo libero?", "4 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Rispondi all'insegnante.", "4 min")}
<ol style="line-height:1.65"><li>Per quale squadra tifi? Guardi le partite in TV o allo stadio?</li><li>Qual è lo sport più popolare in Brasile, dopo il calcio?</li><li>Che sport vuoi provare in Italia?</li></ol>""",
    26, """<ol><li>A: se lo studente risponde <i>posso</i>, correggere con <i>so</i>.</li>
<li>C: <i>tifare per</i> = essere sostenitore di una squadra; <i>il tifoso</i>. Lo studente può parlare della sua squadra brasiliana.</li></ol>""")

    # Page 7
    pc = [("Unità 23", "So dare istruzioni."), ("Unità 24", "So dire che sport faccio."), ("Unità 24", "So usare giocare a / fare."),
          ("Unità 24", "So dire che cosa so fare."), ("Unità 24", "So dire quante volte faccio una cosa.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Gioco tennis il sabato.", "Gioco a tennis il sabato."), ("Mia sorella gioca a yoga.", "Mia sorella fa yoga."), ("Non posso sciare, non ho mai imparato.", "Non so sciare."),
          ("Mai guardo il calcio.", "Non guardo mai il calcio."), ("Vado all'accademia tre volte alla settimana.", "Vado in palestra tre volte alla settimana."),
          ("Tu gioci a pallavolo?", "Tu giochi a pallavolo?")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Io e lo sport.</b> Scrivi 6 frasi: che sport fai o guardi, quante volte, che cosa sai fare e che cosa non sai fare.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il testo. Poi si parla delle feste italiane e degli auguri (unità 25).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("24.1", "Che sport fai? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("24.2", "R e RR")}
<p>{" · ".join(S242)}</p>
{sub("24.3", "Parlare di sport")}
<p>{" ".join(S243)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 24 - Lo sport")
