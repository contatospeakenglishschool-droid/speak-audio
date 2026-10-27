# Speak! Essenziale A1 - Unità 06 "Mi piace!" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 06", audio_json=os.path.join(HERE, "audio_it-a1-unita-06.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "leggere", "leggere"), ("B", "cucinare", "cucinare"), ("C", "ballare", "ballare"), ("D", "il calcio", "calcio"),
          ("E", "la musica", "musica"), ("F", "il cinema", "cinema"), ("G", "viaggiare", "viaggiare"), ("H", "nuotare", "nuotare")]

SCRIPT = [("Narratore", "Dialogo uno. Allo studio, in pausa pranzo."), ("Marco", "Allora, Júlia, ti piace Bologna?"),
          ("Júlia", "Sì, mi piace molto! Mi piacciono i portici e le piazze."), ("Marco", "E il cibo? Ti piacciono i tortellini?"),
          ("Júlia", "Sì, mi piacciono tantissimo! Ma non mi piace la mortadella."), ("Marco", "Non ti piace la mortadella? Ma sei a Bologna!"),
          ("Narratore", "Dialogo due. Sulle scale."), ("Davide", "Júlia, che cosa ti piace fare nel tempo libero?"),
          ("Júlia", "Mi piace leggere e mi piace ballare. Soprattutto il forró!"), ("Davide", "Il forró? Che cos'è?"),
          ("Júlia", "È una musica brasiliana. E a te che cosa piace?"), ("Davide", "A me piace il calcio. Il Napoli, naturalmente! Ti piace il calcio?"),
          ("Júlia", "No, a me non piace."), ("Davide", "E ti piace cucinare?"), ("Júlia", "Sì, molto!"), ("Davide", "Anche a me!"),
          ("Narratore", "Dialogo tre. Al bar."), ("Giulia", "Júlia, ti piacciono i film italiani?"), ("Júlia", "Sì, mi piace molto il cinema."),
          ("Giulia", "Sabato c'è il cinema all'aperto in piazza Maggiore. A me piacciono i film vecchi, di Fellini."), ("Júlia", "Anche a me!"),
          ("Giulia", "E a Davide piace il cinema?"), ("Júlia", "No, a Davide piace solo il calcio!")]
S062 = ["piace", "piacciono", "leggere", "cinema", "musica", "sabato", "Mi piacciono i tortellini.", "Mi piace leggere."]
S063 = ["Ti piace il cinema?", "Anche a me!", "A me no.", "Non mi piace il calcio.", "Neanche a me.", "A me sì!", "Le piace Bologna, signora?"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 06", "Mi piace!", "Gusti e tempo libero · <b>anche a me!</b>",
                       [("SAI FARE", "dire che cosa ti piace e non ti piace; reagire ai gusti degli altri"), ("LINGUA", "mi piace / mi piacciono · ti piace? Le piace? · anche a me / neanche a me"),
                        ("PRONUNCIA", "l'accento: piàcciono, lèggere, cìnema · reagire con l'intonazione")])
    words = ["ballare", "cucinare", "il calcio", "il cinema", "la musica", "leggere", "nuotare", "viaggiare"]
    qs = [("il calcio", "piace"), ("i film italiani", "piacciono"), ("leggere", "piace"), ("le lasagne", "piacciono"), ("la pizza", "piace"), ("viaggiare e ballare", "piace")]
    ql = [f'<li value="{i+1}">Mi {A(a, "min-width:24mm")} {q}.</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: il tempo libero", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Piace o piacciono? Guarda la parola dopo e completa.", "4 min")}
{twocol(ql, 4)}""",
    28, """<ol><li>A: chiedere subito per ogni foto: <i>Ti piace?</i> Lo studente risponde solo <i>Sì / No</i>: la frase completa arriva a pagina 3.</li>
<li>B: scoperta della regola: una cosa o un verbo → <b>piace</b>; più cose → <b>piacciono</b>. Frase 6: due verbi → sempre <i>piace</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 attività del tempo libero · piace o piacciono?</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>I gusti di Júlia, Davide e Giulia: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td><i>mi piace / mi piacciono</i> · <i>ti piace? Le piace?</i> · <i>anche a me / neanche a me</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>L'accento sulla terzultima · reagire con l'intonazione</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td><i>piace / piacciono</i> · reagire · scrivere i propri gusti</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Che cosa abbiamo in comune? · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 03–06) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>A pranzo Júlia dice a Marco che le piacciono Bologna, i portici e i tortellini… ma non la mortadella! Marco non ci crede. Sulle scale Júlia e Davide parlano di tempo libero: a lei piace ballare il forró, a lui piace il calcio (il Napoli); a tutti e due piace cucinare. Al bar Giulia invita Júlia al cinema all'aperto in piazza Maggiore.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese il soggetto è la persona; in italiano il soggetto è la cosa: <b>mi piace</b> la pizza, <b>mi piacciono</b> i tortellini. <i>Io piaccio la pizza</i> ✗. <i>Mi piace di leggere</i> ✗ → <b>Mi piace leggere</b>. E per rispondere: <i>Anche io</i> ✗ → <b>Anche a me</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Ogni estate in <b>piazza Maggiore</b>, a Bologna, c'è un grande cinema all'aperto gratuito («Sotto le stelle del cinema»), con molti film classici italiani.</div>
<div class="box"><h4>AUDIO</h4>Traccia 06.1 Tre dialoghi (lento e naturale) · Traccia 06.2 L'accento · Traccia 06.3 Reagire</div>""")

    # Page 2
    lk = [("Júlia", "i portici e le piazze", "mi piace"), ("Júlia", "la mortadella", "non mi piace"), ("Júlia", "ballare il forró", "mi piace"),
          ("Davide", "il calcio", "mi piace"), ("Júlia", "il calcio", "non mi piace"), ("Giulia", "i film vecchi di Fellini", "mi piace")]
    lr = "".join(f'<tr><td style="width:22mm"><b>{p}</b></td><td>{t}</td><td style="width:50mm;text-align:center;white-space:nowrap">{ch(["✓", "✗"], "✓" if a == "mi piace" else "✗")}</td></tr>' for p, t, a in lk)
    gp = [("Mi", "piacciono", "i portici e le piazze."), ("Non mi", "piace", "la mortadella."), ("Che cosa ti piace", "fare", "nel tempo libero?"),
          ("A me piace", "il calcio", "."), ("", "Anche", "a me!")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:22mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: che cosa ti piace?", "10 min")}
<p>Júlia parla di gusti con Marco a pranzo, con Davide sulle scale e con Giulia al bar.</p>
{audiocard(["06.1 · SLOW", "06.1 · NATURAL"])}
{sub("A", "Ascolta. Piace (✓) o non piace (✗)?", "4 min", "06.1 · SLOW")}
<table style="margin:0">{lr}</table>
{sub("B", "Ascolta di nuovo e completa.", "4 min", "06.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Perché Marco dice «Ma sei a Bologna!»?", "2 min")}
<div class="wline">{R("Perché la mortadella è un cibo tipico di Bologna e a Júlia non piace.")}</div>""",
    28, """<ol><li>A: versione <b>lenta</b>. Lo studente segna ✓ o ✗. <i>Tantissimo</i> = moltissimo.</li>
<li>B: versione <b>naturale</b>. 5: <i>Anche a me!</i> = Davide è d'accordo con Júlia (cucinare).</li>
<li>C: a Bologna la mortadella si chiama anche «la Bologna». Chiedere: <i>E a te piace la mortadella?</i></li></ol>""")

    # Page 3
    pf = [("una cosa", "Mi piace il cinema."), ("un verbo", "Mi piace leggere. Mi piace ballare e cucinare."), ("più cose", "Mi piacciono i tortellini.")]
    pp = [("a me", "mi piace", "Mi piace il calcio."), ("a te", "ti piace", "Ti piace il calcio?"), ("a lui / a lei / a Davide", "gli / le piace", "A Davide piace il calcio."), ("a Lei (formale)", "Le piace", "Le piace Bologna, signora?")]
    re_ = [("Mi piace il cinema. ✓", "Anche a me! ✓", "A me no. ✗"), ("Non mi piace il calcio. ✗", "Neanche a me. ✗", "A me sì! ✓")]
    rules = [("", "Mi piacciono i film.", "Mi piace i film."), ("", "Mi piace leggere.", "Mi piace di leggere."),
             ("«Mi piace ballare.» – «", "Anche a me!", "Anche io!"), ("«Non mi piace la mortadella.» – «", "Neanche a me.", "Anche a me no.")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        end = "»" if s.endswith("«") else ""
        return f"<li>{s}<b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b>{end}</li>"
    tf = "".join(f"<tr><td class='small'><b>{a}</b></td><td>{e}</td></tr>" for a, e in pf)
    tp = "".join(f"<tr><td class='small'>{a}</td><td><b>{x}</b></td><td class='small'>{e}</td></tr>" for a, x, e in pp)
    tr_ = "".join(f"<tr><td>{a}</td><td><b>{x}</b></td><td><b>{y}</b></td></tr>" for a, x, y in re_)
    b.page(f"""{sec(3, "Grammatica: piacere · anche a me / neanche a me", "10 min")}
{sub("A", "Piace o piacciono?", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="2">piacere</th></tr>{tf}</table></div>
<div><table style="margin:0"><tr><th>A chi?</th><th></th><th>Esempio</th></tr>{tp}</table></div></div>
{sub("B", "Reagire: sono d'accordo o no?", "3 min")}
<table style="margin:0"><tr><th>Frase</th><th>Sono d'accordo</th><th>Non sono d'accordo</th></tr>{tr_}</table>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>REGOLA</h4>Con <b>piacere</b> il soggetto è la cosa che piace: <i>La pizza</i> (soggetto) <i>mi piace</i>. Per questo: una cosa → <b>piace</b>, più cose → <b>piacciono</b>. Per dire «molto»: <i>mi piace <b>molto</b> / <b>tantissimo</b></i>; per dire «zero»: <i>non mi piace <b>per niente</b></i>.</div>""",
    20, """<ol><li>A: <i>gli piace / le piace</i> (a lui / a lei) = solo da riconoscere; all'A1 basta <i>A Davide piace…</i></li>
<li>B: fare 4–5 frasi veloci sui gusti dell'insegnante; lo studente reagisce con le quattro risposte.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Io piaccio la pizza.</td><td><b>Mi piace la pizza.</b></td><td>Il soggetto è la pizza.</td></tr>
<tr><td>Mi piace i tortellini.</td><td><b>Mi piacciono i tortellini.</b></td><td>Più cose = <i>piacciono</i>.</td></tr>
<tr><td>Mi piace di leggere.</td><td><b>Mi piace leggere.</b></td><td>Senza <i>di</i>.</td></tr>
<tr><td>«Mi piace ballare.» – «Anche io!»</td><td><b>«Anche a me!»</b></td><td>Si risponde con <i>a me</i>.</td></tr>
<tr><td>Ti piace, signora?</td><td><b>Le piace, signora?</b></td><td>Formale = <i>Le</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["06.2", "06.3"])}
{sub("A", "L'accento. Ascolta e ripeti. In queste parole l'accento è sulla terzultima sillaba: PIÀcciono, LÈggere, CÌnema.", "2 min", "06.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S062)}</div>
{sub("B", "Reagire. Ascolta e ripeti con l'intonazione giusta.", "3 min", "06.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S063)}</div>""",
    38, """<ol><li>Errori: l'errore principale è pensare con la struttura del portoghese (persona = soggetto). Ripetere spesso: <i>la cosa è il soggetto</i>.</li>
<li>4A: i brasiliani tendono a dire «piacCIOno» o «legGEre». Battere le mani sulla sillaba forte: <b>PIÀ</b>-ccio-no, <b>LÈ</b>-gge-re, <b>SÀ</b>-ba-to, <b>MÙ</b>-si-ca.</li>
<li>4B: <i>Anche a me!</i> con entusiasmo ↗; <i>Neanche a me</i> con voce bassa ↘.</li></ol>""")

    # Page 5
    gw = ["piace", "piacciono", "piace", "piacciono", "piace", "piace"]
    gs = [("Mi", "la musica brasiliana."), ("Ti", "i portici di Bologna?"), ("A Davide", "il calcio."), ("Non mi", "le lasagne."), ("Signora, Le", "Bologna?"), ("A Júlia", "ballare e leggere.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:22mm")} {c}</li>' for i, (a, c) in enumerate(gs)]
    rx = [("Mi piace viaggiare.", "✓", "Anche a me!"), ("Non mi piace nuotare.", "✓", "A me sì!"), ("Mi piacciono i film di Fellini.", "✗", "A me no."), ("Non mi piace la mortadella.", "✗", "Neanche a me.")]
    rl = "".join(f'<li>{s} &nbsp;<b>Tu: {f}</b> → {A(a, "min-width:32mm")}</li>' for s, f, a in rx)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con piace o piacciono.", "3 min")}
{twocol(gl5, 4)}
{sub("B", "Reagisci. Guarda il segno: ✓ = ti piace, ✗ = non ti piace.", "2 min")}
<ol style="line-height:1.9">{rl}</ol>
{sub("C", "E tu? Scrivi 3 cose che ti piacciono e 2 cose che non ti piacciono.", "3 min")}
<div class="wline">{R("Esempio: Mi piace cucinare. Mi piacciono i film italiani. Mi piace il mare. Non mi piace il calcio. Non mi piacciono le lasagne.")}</div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: 6: <i>ballare e leggere</i> = verbi → <i>piace</i>. B: la risposta dipende dalla frase (positiva o negativa) e dalla faccia.</li>
<li>C: poi l'insegnante reagisce alle frasi dello studente e lo studente reagisce a quelle dell'insegnante.</li></ol>""")

    # Page 6
    sv = ["cucinare", "il calcio", "ballare", "i film italiani", "viaggiare", "la mortadella", "leggere", "le serie TV", "nuotare", "la musica classica"]
    svr = "".join(f"<tr><td>{x}</td><td style='text-align:center'>☐</td><td style='text-align:center'>☐</td><td style='text-align:center'>☐</td></tr>" for x in sv)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Che cosa abbiamo in comune? Fai domande all'insegnante e segna. Poi l'insegnante fa domande a te.", "7 min")}
<table style="margin:1mm 0 2mm"><tr><th></th><th style="width:26mm;text-align:center">A me</th><th style="width:30mm;text-align:center">All'insegnante</th><th style="width:30mm;text-align:center">In comune?</th></tr>{svr}</table>
<div class="bank" style="background:#fff">Ti piace…? / Ti piacciono…? · Sì, molto! · No, per niente. · Anche a me! · Neanche a me. · A me sì! · A me no.</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Che cosa ti piace fare nel fine settimana?</li><li>Ti piace il cibo italiano? Che cosa ti piace di più?</li><li>Che musica ti piace?</li><li>C'è una cosa tipica del Brasile che ti piace molto?</li></ol>""",
    26, """<ol><li>A: alla fine lo studente dice 3 frasi: <i>A me e all'insegnante piace…</i> oppure <i>Anche all'insegnante piace…</i> Correggere <i>piace / piacciono</i>.</li>
<li>B: domanda 4 per far parlare del Brasile (cibo, musica, feste). Reagire sempre con <i>Anche a me!</i> o <i>A me no</i>.</li></ol>""")

    # Page 7
    pc = [("Unità 04", "So ordinare al bar e chiedere il prezzo."), ("Unità 05", "So dire l'ora e parlare della mia giornata."),
          ("Unità 06", "So dire che cosa mi piace e non mi piace."), ("Unità 06", "So usare piace e piacciono."), ("Unità 06", "So reagire: anche a me / neanche a me.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Io piaccio il calcio.", "Mi piace il calcio."), ("Mi piace i portici di Bologna.", "Mi piacciono i portici di Bologna."), ("Mi piace di cucinare.", "Mi piace cucinare."),
          ("«Mi piace il cinema.» – «Anche io!»", "Anche a me!"), ("Signora, ti piace Bologna?", "Signora, Le piace Bologna?"), ("«Non mi piace nuotare.» – «Anche a me no.»", "Neanche a me.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio a Giulia.</b> Rispondi all'invito al cinema: di' che cosa ti piace (film, musica, cibo) e che cosa non ti piace (4–5 frasi).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. L'insegnante legge il messaggio come Giulia e reagisce: <i>Anche a me! / A me no…</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("06.1", "Che cosa ti piace? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("06.2", "L'accento")}
<p>{" · ".join(S062)}</p>
{sub("06.3", "Reagire")}
<p>{" ".join(S063)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 06 - Mi piace")
