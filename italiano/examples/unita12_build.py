# Speak! Essenziale A1 - Unità 12 "In cucina" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 12", audio_json=os.path.join(HERE, "audio_it-a1-unita-12.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la cipolla", "cipolla"), ("B", "le carote", "carote"), ("C", "la pentola", "pentola"), ("D", "la carne macinata", "carne"),
          ("E", "le uova", "uova"), ("F", "il sale", "sale"), ("G", "il coltello", "coltello"), ("H", "il ragù", "ragù")]

SCRIPT = [("Narratore", "Dialogo uno. Allo studio."), ("Júlia", "Marco, sabato voglio cucinare il ragù. Come si fa?"),
          ("Marco", "Allora: si tagliano la cipolla, la carota e il sedano. Si mette l'olio nella pentola e si cuociono le verdure."),
          ("Júlia", "E la carne?"), ("Marco", "La metti dopo, con un po' di vino rosso. Poi si aggiunge il pomodoro e si cuoce per tre ore."),
          ("Júlia", "Tre ore?"), ("Marco", "Sì! Il vero ragù si fa così."),
          ("Narratore", "Dialogo due. Al supermercato."), ("Júlia", "Davide, le carote dove sono?"), ("Davide", "Le carote? Le trovi lì, accanto alle patate."),
          ("Júlia", "E la carne macinata?"), ("Davide", "La prendi al banco della carne."), ("Júlia", "Quante bottiglie di passata di pomodoro compro?"),
          ("Davide", "Ne compri due. E il vino?"), ("Júlia", "Il vino lo porta Marco!"),
          ("Narratore", "Dialogo tre. Sabato sera, a casa di Júlia."), ("Giulia", "Mmm, che profumo! Hai fatto tu il ragù?"),
          ("Júlia", "Sì, con la ricetta di Marco."), ("Giulia", "Posso assaggiare?"), ("Júlia", "Certo! Ne vuoi un po'?"),
          ("Giulia", "Sì, grazie… È buonissimo! Brava, Júlia!")]
S122 = ["cipolla", "cucina", "chilo", "cucchiaio", "aggiungere", "funghi", "spaghetti", "Si aggiungono i funghi."]
S123 = ["Si taglia la cipolla.", "Si mette l'olio nella pentola.", "Si aggiunge il pomodoro.", "Si cuoce per tre ore.", "La carne? La metti dopo.", "Quante bottiglie? Ne compri due."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 12", "In cucina", "Ricette e spesa · <b>lo, la, li, le · ne · si mette</b>",
                       [("SAI FARE", "capire e spiegare una ricetta semplice; parlare della spesa"), ("LINGUA", "lo / la / li / le · ne (= di questo) · si taglia, si mette, si cuoce"),
                        ("PRONUNCIA", "ci / chi, gi / ghi in cucina · le istruzioni di una ricetta")])
    words = ["il coltello", "il ragù", "il sale", "la carne macinata", "la cipolla", "la pentola", "le carote", "le uova"]
    moka = [("Si mette il caffè nel filtro.", "2"), ("Si mette l'acqua nella parte bassa.", "1"), ("Si mette la moka sul fuoco.", "4"), ("Si chiude la moka.", "3"), ("Si beve il caffè!", "5")]
    ml = "".join(f"<tr><td style='width:16mm;text-align:center'>{A(n, 'min-width:8mm')}</td><td>{s}</td></tr>" for s, n in moka)
    b.page(f"""{sec(1, "Riscaldamento: in cucina", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Il caffè con la moka. Metti le frasi in ordine (1–5).", "4 min")}
<table style="margin:0">{ml}</table>""",
    22, """<ol><li>A: <b>le uova</b> = plurale irregolare (<i>l'uovo → le uova</i>). <b>Il ragù</b> = salsa di carne tipica di Bologna, con le tagliatelle.</li>
<li>B: prima esposizione al <b>si</b> impersonale: lo studente capisce dal contesto. Chiedere: <i>Tu come fai il caffè?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 parole della cucina con foto · il caffè con la moka</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La ricetta del ragù, la spesa e la cena: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Pronomi diretti <i>lo, la, li, le</i> · <i>ne</i> · <i>si</i> impersonale</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td><i>ci / chi, gi / ghi</i> · istruzioni di una ricetta</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Pronomi · <i>ne</i> · una ricetta brasiliana con il <i>si</i></td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La lista della spesa (domande con i pronomi) · la tua ricetta</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 08–12) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Dopo la cena con i tortellini di Marco, Júlia vuole cucinare da sola. Marco le spiega la ricetta del ragù (tre ore!). Al supermercato Davide l'aiuta a trovare le carote e la carne. Sabato sera Giulia assaggia il ragù: «È buonissimo!»</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Compro lo</i> ✗ → <b>Lo compro</b> (il pronome va prima del verbo). <i>Compro due</i> ✗ → <b>Ne compro due</b>. <i>Lo compro le carote</i> ✗ → <b>Le compro</b>. <i>Se mette</i> ✗ → <b>Si mette</b>. <i>Gli spaghetti</i> si dice con <b>gh</b>, non «spagueti».</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>A Bologna il ragù si mangia con le <b>tagliatelle</b>, non con gli spaghetti: gli «spaghetti alla bolognese» quasi non esistono in Italia!</div>
<div class="box"><h4>AUDIO</h4>Traccia 12.1 Tre dialoghi (lento e naturale) · Traccia 12.2 ci / chi, gi / ghi · Traccia 12.3 La ricetta</div>""")

    # Page 2
    st = [("si tagliano", "la cipolla, la carota e il sedano"), ("si mette", "l'olio nella pentola"), ("si cuociono", "le verdure"), ("si mette", "la carne, con un po' di vino rosso"), ("si aggiunge", "il pomodoro"), ("si cuoce", "per tre ore")]
    stl = "".join(f"<tr><td style='width:10mm;text-align:center'><b>{i+1}</b></td><td>{A(v, 'min-width:26mm')} {c}</td></tr>" for i, (v, c) in enumerate(st))
    gp = [("Le carote?", "Le", "trovi lì, accanto alle patate."), ("La carne?", "La", "prendi al banco della carne."), ("Quante bottiglie? –", "Ne", "compri due."),
          ("Il vino", "lo", "porta Marco!"), ("Certo!", "Ne", "vuoi un po'?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:14mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: il ragù di Júlia", "10 min")}
<p>Dopo la cena con i tortellini, Júlia vuole cucinare un piatto bolognese da sola: il ragù.</p>
{audiocard(["12.1 · SLOW", "12.1 · NATURAL"])}
{sub("A", "Ascolta il dialogo 1. Completa la ricetta del ragù.", "4 min", "12.1 · SLOW")}
<table style="margin:0">{stl}</table>
{sub("B", "Ascolta i dialoghi 2 e 3. Completa con lo, la, le, ne.", "4 min", "12.1 · NATURAL")}
{twocol(gl, 3)}
{sub("C", "Che cosa dice Giulia del ragù?", "2 min")}
<div class="wline">{R("Dice che è buonissimo («Brava, Júlia!»).")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Far notare: <i>si taglia</i> + una cosa, <i>si tagliano</i> + più cose (pagina 3).</li>
<li>B: versione <b>naturale</b>. Chiedere: <i>che cosa sostituisce «le»?</i> → <i>le carote</i>; <i>«ne»?</i> → <i>di bottiglie</i>.</li></ol>""")

    # Page 3
    pr = [("il pane", "lo", "Il pane? <b>Lo</b> compro al forno."), ("la carne", "la", "La carne? <b>La</b> prendo al banco."), ("i pomodori", "li", "I pomodori? <b>Li</b> metto dopo."), ("le carote", "le", "Le carote? <b>Le</b> taglio piccole.")]
    tp = "".join(f"<tr><td>{a}</td><td><b>{x}</b></td><td class='small'>{e}</td></tr>" for a, x, e in pr)
    ne = ["Quante uova compri? – <b>Ne</b> compro sei.", "Vuoi del pane? – Sì, <b>ne</b> prendo un po'.", "Hai delle cipolle? – No, non <b>ne</b> ho."]
    si = [("una cosa", "Si <b>taglia</b> la cipolla. · Si <b>mette</b> il sale."), ("più cose", "Si <b>tagliano</b> le carote. · Si <b>cuociono</b> le verdure.")]
    ts = "".join(f"<tr><td class='small'><b>{a}</b></td><td>{e}</td></tr>" for a, e in si)
    rules = [("Il formaggio? ", "Lo compro.", "Compro lo."), ("Le uova? ", "Ne compro sei.", "Compro sei."), ("Le carote? ", "Le taglio.", "Lo taglio."), ("", "Si mette il sale.", "Se mette il sale.")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s}<b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: lo, la, li, le · ne · si", "10 min")}
{sub("A", "I pronomi diretti: non ripetere la parola.", "3 min")}
<table style="margin:0"><tr><th style="width:26mm">la cosa</th><th style="width:14mm">pronome</th><th>esempio</th></tr>{tp}</table>
<div class="two"><div>{sub("B", "Ne = di questo / di questi (quantità).", "2 min")}<div class="bank" style="background:#fff;font-weight:500">{"<br>".join(ne)}</div></div>
<div>{sub("C", "Si + verbo: le istruzioni.", "2 min")}<table style="margin:0">{ts}</table></div></div>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>REGOLA</h4>Il pronome va <b>prima del verbo</b>: <i>Lo compro.</i> Con la negazione: <i>Non lo compro.</i> Con <b>ne</b> si dice la quantità dopo il verbo: <i>Ne compro <b>due</b> / un po' / molti</i>. Nelle ricette si usa <b>si</b> + verbo alla terza persona.</div>""",
    22, """<ol><li>A: il pronome ha lo stesso genere e numero della cosa (<i>la carne → la; le carote → le</i>).</li>
<li>B: senza <i>ne</i> la frase <i>compro due</i> non è completa in italiano. C: <i>si</i> = «la gente, tutti»: forma molto usata nelle ricette e nei cartelli.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Il pane? Compro lo.</td><td><b>Il pane? Lo compro.</b></td><td>Il pronome va prima del verbo.</td></tr>
<tr><td>Quante uova? Compro sei.</td><td><b>Ne compro sei.</b></td><td>Quantità = <i>ne</i>.</td></tr>
<tr><td>Le carote? Lo taglio.</td><td><b>Le carote? Le taglio.</b></td><td>Femminile plurale = <i>le</i>.</td></tr>
<tr><td>Se mette il sale.</td><td><b>Si mette il sale.</b></td><td>In italiano: <i>si</i>.</td></tr>
<tr><td>Si taglia le carote.</td><td><b>Si tagliano le carote.</b></td><td>Più cose = verbo plurale.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["12.2", "12.3"])}
{sub("A", "ci / chi, gi / ghi. Ascolta e ripeti: ci = «tch», chi = «k»; gi = «dj», ghi = «g».", "2 min", "12.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S122)}</div>
{sub("B", "La ricetta. Ascolta e ripeti.", "3 min", "12.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S123)}</div>""",
    38, """<ol><li>Errori: <i>se mette</i> viene dal portoghese. In italiano <i>se</i> = condizione (<i>se piove…</i>); l'impersonale è <b>si</b>.</li>
<li>4A: la <b>h</b> dopo c e g rende il suono duro: <i>chilo</i> («kilo»), <i>funghi</i>, <i>spaghetti</i>. Senza <i>h</i>: <i>cipolla, aggiungere</i>.</li>
<li>4B: lo studente ripete e poi legge la ricetta del ragù a pagina 2 ad alta voce.</li></ol>""")

    # Page 5
    pw = [("Il parmigiano?", "Lo", "compro al mercato."), ("La pasta?", "La", "cuocio per dieci minuti."), ("I funghi?", "Li", "metto alla fine."), ("Le uova?", "Le", "prendo al supermercato."), ("Il caffè?", "Lo", "faccio con la moka.")]
    pl5 = "".join(f'<li>{a} {A(x, "min-width:12mm")} {c}</li>' for a, x, c in pw)
    nq = [("Quante cipolle compri? (2)", "Ne compro due."), ("Vuoi del vino? (un po')", "Sì, ne voglio un po'."), ("Quanti pomodori metti? (sei)", "Ne metto sei.")]
    nl = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in nq)
    br = [("mettere", "Si mette il latte condensato in una pentola."), ("aggiungere", "Si aggiunge il cacao."), ("mescolare", "Si mescola per dieci minuti."), ("fare", "Si fanno le palline.")]
    brl = "".join(f'<li><span class="small">({v})</span> {R(a) if T else "<span class=wline style=display:block></span>"}</li>' for v, a in br)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con lo, la, li, le.", "2 min")}
<ol>{pl5}</ol>
{sub("B", "Rispondi con ne.", "2 min")}
<ol>{nl}</ol>
{sub("C", "Una ricetta brasiliana: il brigadeiro. Scrivi le istruzioni con si + verbo.", "4 min")}
<ol>{brl}</ol>""",
    22, """<ol><li>A: <i>cuocio</i> = io (da <i>cuocere</i>): solo da capire.</li>
<li>C: accettare altre ricette semplici. Lo studente spiega la ricetta all'insegnante, che fa domande: <i>Quanto cacao si mette?</i> → <i>Se ne mettono due cucchiai</i> (solo da capire).</li></ol>""")

    # Page 6
    lst = [("il latte", "Lo compro io."), ("le uova", "Le compri tu?"), ("il pane", "Lo prendo al forno."), ("le cipolle", "Ne compro tre."), ("la pasta", "La prendo io."), ("i pomodori", "Ne compro un chilo.")]
    lr = "".join(f"<tr><td style='width:30mm'><b>{x}</b></td><td style='width:16mm;text-align:center'>☐</td><td class='small'>{R(e)}</td></tr>" for x, e in lst)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "La lista della spesa. Stasera tu e l'insegnante cucinate insieme. Dividete la spesa: fai domande e rispondi con lo, la, li, le, ne.", "6 min")}
<table style="margin:1mm 0 2mm"><tr><th>Che cosa?</th><th style="text-align:center">Chi?</th><th>esempio</th></tr>{lr}</table>
<div class="bank" style="background:#fff">Il latte, lo compri tu? · Sì, lo compro io. / No, lo compri tu. · Quante… compro? · Ne compri…</div>
{sub("B", "La tua ricetta. Spiega all'insegnante come si fa un piatto che sai cucinare.", "6 min")}
<ol style="line-height:1.65"><li>Come si chiama il piatto? È brasiliano?</li><li>Che cosa serve? Quanto ne serve?</li><li>Come si fa? (si mette… si aggiunge… si cuoce…)</li><li>Con che cosa si mangia?</li></ol>""",
    26, """<ol><li>A: gli esempi in rosso servono solo all'insegnante. Lo studente segna nella colonna «Chi?» chi compra che cosa (io / tu).</li>
<li>B: correggere il <i>si</i> (singolare / plurale) e la posizione dei pronomi.</li></ol>""")

    # Page 7
    pc = [("Unità 08", "So prenotare una camera in albergo."), ("Unità 10", "So comprare il cibo al mercato."), ("Unità 11", "So raccontare il mio fine settimana."),
          ("Unità 12", "So capire e spiegare una ricetta semplice con si."), ("Unità 12", "So usare lo, la, li, le e ne.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Il pane? Compro lo al forno.", "Il pane? Lo compro al forno."), ("Quante mele vuoi? Voglio tre.", "Ne voglio tre."), ("Le uova? Li compro io.", "Le uova? Le compro io."),
          ("Se aggiunge il sale.", "Si aggiunge il sale."), ("Si taglia le cipolle.", "Si tagliano le cipolle."), ("La pasta? Non compro la.", "La pasta? Non la compro.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La ricetta della tua famiglia.</b> Scrivi una ricetta semplice (5–6 frasi) con <i>si</i> + verbo e almeno un pronome (<i>lo, la, le, ne</i>).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi lo studente legge la ricetta e l'insegnante fa domande: <i>Le cipolle, quando le metti? Quanto sale ci metti?</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("12.1", "Il ragù di Júlia (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("12.2", "ci / chi, gi / ghi")}
<p>{" · ".join(S122)}</p>
{sub("12.3", "La ricetta")}
<p>{" ".join(S123)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 12 - In cucina")
