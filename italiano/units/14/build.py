# Speak! Essenziale A1 - Unità 14 "La famiglia" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 14", audio_json=os.path.join(HERE, "audio_it-a1-unita-14.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "madre e figlia", "madre e figlia"), ("B", "padre e figlio", "padre e figlio"), ("C", "i nonni", "nonni"), ("D", "fratello e sorella", "fratello e sorella"),
          ("E", "marito e moglie", "marito e moglie"), ("F", "il cane", "cane"), ("G", "il gatto", "gatto"), ("H", "il pranzo della domenica", "pranzo")]

SCRIPT = [("Narratore", "Dialogo uno. Al bar, Júlia mostra delle foto."), ("Júlia", "Guarda, Giulia: questa è la mia famiglia. Questi sono i miei genitori."),
          ("Giulia", "Che belli! Come si chiama tua madre?"),
          ("Júlia", "Mia madre si chiama Lúcia e mio padre si chiama Roberto. E questo è mio fratello Bruno: è il più giovane della famiglia."),
          ("Giulia", "E questo cane?"), ("Júlia", "È il nostro cane, Biscotto. È il più simpatico di tutti!"),
          ("Narratore", "Dialogo due. Al telefono."), ("Marco", "Júlia, domenica c'è il pranzo a casa dei miei genitori. Vieni?"), ("Júlia", "Volentieri! Chi c'è?"),
          ("Marco", "Mia madre, mio padre, Luca e mia nonna. Mia nonna è la persona più simpatica della famiglia. E fa le tagliatelle più buone di Bologna!"),
          ("Narratore", "Dialogo tre. Lunedì, sulle scale."), ("Davide", "Allora, Júlia, com'è andato il pranzo dalla famiglia di Marco?"),
          ("Júlia", "Benissimo! Mi sono divertita tantissimo. La nonna di Marco mi ha insegnato a fare le tagliatelle."), ("Davide", "E quanto è durato?"),
          ("Júlia", "Mi sono seduta a tavola all'una e mi sono alzata alle cinque!"), ("Davide", "Ah, il pranzo della domenica in Italia è così!")]
S142 = ["mio, mia", "miei", "tuoi", "suoi", "uomo", "suocera", "I miei genitori e i tuoi nonni."]
S143 = ["Questa è mia madre.", "Questi sono i miei genitori.", "Mio fratello è il più giovane della famiglia.", "Come si chiama tua sorella?", "Mi sono divertita tantissimo.", "Mi sono alzato tardi."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 14", "La famiglia", "Presentare la famiglia · <b>mio padre, i miei genitori</b>",
                       [("SAI FARE", "presentare la tua famiglia, descrivere le persone e confrontarle"), ("LINGUA", "mio / mia / miei / mie · il più giovane della famiglia · mi sono divertito/a"),
                        ("PRONUNCIA", "i dittonghi: miei, tuoi, suoi · presentare la famiglia")])
    words = ["fratello e sorella", "i nonni", "il cane", "il gatto", "il pranzo della domenica", "madre e figlia", "marito e moglie", "padre e figlio"]
    rd = [("La madre di mia madre è mia", "nonna"), ("Il fratello di mio padre è mio", "zio"), ("Il figlio di mio zio è mio", "cugino"),
          ("La figlia di mia sorella è mia", "nipote"), ("Il marito di mia sorella è mio", "cognato"), ("Mio padre e mia madre sono i miei", "genitori")]
    rl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}.</li>' for i, (a, x) in enumerate(rd)]
    b.page(f"""{sec(1, "Riscaldamento: la famiglia", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le parole sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Chi è? Completa.", "4 min")}
<div class="bank" style="background:#fff">cognato · cugino · genitori · nipote · nonna · zio</div>
{twocol(rl, 4)}""",
    24, """<ol><li>A: <b>i genitori</b> = padre e madre (falso amico: <i>i parenti</i> = tutta la famiglia). Chiedere: <i>Hai fratelli o sorelle?</i></li>
<li>B: <b>nipote</b> = figlio/a del fratello o della sorella, e anche figlio/a del figlio (nonni → nipoti).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto della famiglia · i parenti</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La famiglia di Júlia e il pranzo dalla famiglia di Marco: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Possessivi (con e senza articolo) · superlativo relativo · passato prossimo dei riflessivi</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>I dittonghi · presentare la famiglia</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Possessivi · superlativo · riflessivi al passato</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La famiglia di Marco (domande) · la tua famiglia</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 11–14) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Al bar Júlia mostra a Giulia le foto della sua famiglia: i genitori Lúcia e Roberto, il fratello Bruno (il più giovane) e il cane Biscotto. Marco la invita al pranzo della domenica dai suoi genitori: la nonna fa «le tagliatelle più buone di Bologna». Lunedì Júlia racconta a Davide: si è seduta a tavola all'una e si è alzata alle cinque!</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Il mio padre</i> ✗ → <b>mio padre</b> (parenti al singolare: senza articolo). <i>Mio genitori</i> ✗ → <b>i miei genitori</b>. <i>Mi ho alzato</i> ✗ → <b>Mi sono alzato/a</b> (riflessivi = <i>essere</i>). <i>Il più alto que…</i> ✗ → <b>il più alto della famiglia</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il <b>pranzo della domenica</b> con tutta la famiglia è una tradizione italiana molto forte: può durare tutto il pomeriggio, come in molte famiglie brasiliane.</div>
<div class="box"><h4>AUDIO</h4>Traccia 14.1 Tre dialoghi (lento e naturale) · Traccia 14.2 I dittonghi · Traccia 14.3 Presentare la famiglia</div>""")

    # Page 2
    fm = [("la madre di Júlia", "Lúcia"), ("il padre di Júlia", "Roberto"), ("il fratello di Júlia", "Bruno, il più giovane"), ("il cane", "Biscotto, il più simpatico"), ("al pranzo di Marco", "la madre, il padre, Luca, la nonna")]
    fr = "".join(f"<tr><td style='width:44mm'><b>{a}</b></td><td>{A(x, 'min-width:80mm')}</td></tr>" for a, x in fm)
    gp = [("Questi sono", "i miei", "genitori."), ("Come si chiama", "tua", "madre?"), ("È il più giovane", "della", "famiglia."),
          ("Fa le tagliatelle più buone", "di", "Bologna!"), ("", "Mi sono", "divertita tantissimo.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: le nostre famiglie", "10 min")}
<p>Júlia mostra a Giulia le foto della sua famiglia. Poi Marco la invita al pranzo della domenica.</p>
{audiocard(["14.1 · SLOW", "14.1 · NATURAL"])}
{sub("A", "Ascolta. Chi è? Scrivi.", "4 min", "14.1 · SLOW")}
<table style="margin:0">{fr}</table>
{sub("B", "Ascolta di nuovo e completa.", "4 min", "14.1 · NATURAL")}
{twocol(gl, 3)}
{sub("C", "Perché Davide dice «il pranzo della domenica in Italia è così»?", "2 min")}
<div class="wline">{R("Perché il pranzo è durato quattro ore: dall'una alle cinque.")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. <i>Il nostro cane</i> = di tutta la famiglia (<i>nostro</i> = solo da capire).</li>
<li>B: versione <b>naturale</b>. Far notare: <i>tua madre</i> (senza articolo) ma <i>i miei genitori</i> (con articolo): pagina 3.</li></ol>""")

    # Page 3
    ps = [("io", "mio", "mia", "miei", "mie"), ("tu", "tuo", "tua", "tuoi", "tue"), ("lui / lei", "suo", "sua", "suoi", "sue"), ("Lei (formale)", "Suo", "Sua", "Suoi", "Sue")]
    tps = "".join(f"<tr><td>{p}</td><td><b>{a}</b></td><td><b>{bb}</b></td><td><b>{c}</b></td><td><b>{d}</b></td></tr>" for p, a, bb, c, d in ps)
    rf = [("io", "mi sono", "alzato / alzata"), ("tu", "ti sei", "divertito / divertita"), ("lui / lei / Lei", "si è", "seduto / seduta")]
    trf = "".join(f"<tr><td>{p}</td><td><b>{x}</b></td><td>{y}</td></tr>" for p, x, y in rf)
    rules = [("", "mio padre", "il mio padre"), ("", "i miei genitori", "miei genitori"), ("Ieri", "mi sono alzata tardi", "mi ho alzata tardi"), ("Bruno è il più giovane", "della famiglia", "que la famiglia")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: possessivi · superlativo · riflessivi al passato", "10 min")}
{sub("A", "Gli aggettivi possessivi.", "3 min")}
<table style="margin:0"><tr><th></th><th>m. sing.</th><th>f. sing.</th><th>m. pl.</th><th>f. pl.</th></tr>{tps}</table>
<div class="box" style="margin-top:1.5mm"><h4>CON O SENZA ARTICOLO?</h4>Parente al <b>singolare</b>: senza articolo → <i>mio padre, tua madre, sua sorella</i>. Parenti al <b>plurale</b> e tutte le altre cose: con l'articolo → <i>i miei genitori, le mie sorelle, il mio cane, la mia casa</i>.</div>
<div class="two"><div>{sub("B", "Il superlativo relativo.", "2 min")}<p><b>il / la più</b> + aggettivo + <b>di</b><br><i>Bruno è <b>il più</b> giovane <b>della</b> famiglia.</i><br><i>La nonna è <b>la più</b> simpatica <b>di</b> tutti.</i></p></div>
<div>{sub("C", "Riflessivi al passato: essere.", "2 min")}<table style="margin:0">{trf}</table></div></div>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>""",
    20, """<ol><li>A: <i>suo / sua</i> = di lui o di lei: dipende dalla cosa, non dalla persona (<i>la sua casa</i> = la casa di Marco o di Giulia).</li>
<li>C: tutti i verbi riflessivi usano <b>essere</b> al passato prossimo, con l'accordo <i>-o / -a</i> (unità 11).</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Il mio padre è medico.</td><td><b>Mio padre è medico.</b></td><td>Parente singolare: senza articolo.</td></tr>
<tr><td>Mio genitori abitano a Recife.</td><td><b>I miei genitori abitano a Recife.</b></td><td>Plurale: <i>i miei</i>.</td></tr>
<tr><td>Signora, tua madre è italiana?</td><td><b>Signora, Sua madre è italiana?</b></td><td>Formale = <i>Suo / Sua</i>.</td></tr>
<tr><td>Mi ho divertito.</td><td><b>Mi sono divertito/a.</b></td><td>Riflessivi = <i>essere</i>.</td></tr>
<tr><td>È il più alto que tutti.</td><td><b>È il più alto di tutti.</b></td><td>Superlativo: <i>di</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["14.2", "14.3"])}
{sub("A", "I dittonghi. Ascolta e ripeti: due vocali in una sillaba (MIEI, TUOI, SUOI).", "2 min", "14.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S142)}</div>
{sub("B", "Presentare la famiglia. Ascolta e ripeti.", "3 min", "14.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S143)}</div>""",
    38, """<ol><li>Errori: in portoghese si dice spesso l'articolo con i parenti; in italiano no, al singolare. È l'errore più frequente di questa unità.</li>
<li>4A: <i>miei</i> si dice in una sillaba («miei»), non «mi-e-i». <i>Tuoi, suoi</i>: la <i>u</i> è breve.</li>
<li>4B: <i>suocera</i> = la madre del marito o della moglie.</li></ol>""")

    # Page 5
    pw = [("Questa è", "mia", "sorella."), ("Questi sono", "i miei", "nonni."), ("", "Il mio", "cane si chiama Biscotto."), ("Come si chiama", "tuo", "fratello?"),
          ("Signor Neri, come sta", "Sua", "moglie?"), ("Marco abita con", "i suoi", "genitori.")]
    pl5 = "".join(f'<li>{a} {A(x, "min-width:18mm")} {c}</li>' for a, x, c in pw)
    sp = [("Bruno / giovane / famiglia", "Bruno è il più giovane della famiglia."), ("la nonna / simpatica / tutti", "La nonna è la più simpatica di tutti."), ("Marco / alto / studio", "Marco è il più alto dello studio.")]
    spl = "".join(f'<li>{a}<div class="wline">{R(x)}</div></li>' for a, x in sp)
    rw = [("Ieri io", "mi sono alzato/a", "alle otto.", "alzarsi"), ("Júlia", "si è divertita", "al pranzo.", "divertirsi"), ("Tu a che ora", "ti sei svegliato/a", "?", "svegliarsi")]
    rl = "".join(f'<li>{a} {A(v, "min-width:30mm")} {c} <span class="small">({n})</span></li>' for a, v, c, n in rw)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con il possessivo (con o senza articolo).", "3 min")}
<ol>{pl5}</ol>
{sub("B", "Scrivi frasi con il superlativo.", "2 min")}
<ol>{spl}</ol>
{sub("C", "Completa con il passato prossimo del verbo riflessivo.", "3 min")}
<ol>{rl}</ol>""",
    22, """<ol><li>A: 3 <i>il mio cane</i> (non è un parente); 6 <i>i suoi genitori</i> = di Marco.</li>
<li>B: <i>di + lo studio = dello studio</i> (preposizioni articolate, unità 8).</li></ol>""")

    # Page 6
    fm6 = [("la nonna", "Teresa", "82", "pensionata, fa le tagliatelle"), ("il padre", "Giorgio", "60", "medico"), ("la madre", "Anna", "58", "insegnante"),
           ("il fratello", "Luca", "35", "capotreno a Firenze"), ("Marco", "Marco", "31", "architetto")]
    fr6 = "".join(f"<tr><td><b>{r}</b></td><td>{A(n, 'min-width:18mm')}</td><td>{A(e, 'min-width:10mm')}</td><td>{A(j, 'min-width:44mm')}</td></tr>" for r, n, e, j in fm6)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "La famiglia di Marco. L'insegnante ha le informazioni. Fai domande e completa. Poi: chi è il più giovane? Chi è la più anziana?", "7 min")}
<table style="margin:1mm 0 2mm"><tr><th>Chi?</th><th>Nome</th><th>Anni</th><th>Lavoro</th></tr>{fr6}</table>
<div class="bank" style="background:#fff">Come si chiama sua nonna? · Quanti anni ha suo padre? · Che lavoro fa sua madre? · Chi è il più giovane della famiglia?</div>
{sub("B", "La tua famiglia. Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Com'è la tua famiglia? Hai fratelli o sorelle?</li><li>Chi è il più giovane? E il più simpatico?</li><li>Nella tua famiglia fate il pranzo della domenica?</li><li>Hai un animale? Come si chiama?</li></ol>""",
    26, """<ol><li>A: le soluzioni in rosso sono solo per l'insegnante. Il più giovane è <b>Marco</b> (31 anni); la più anziana è la <b>nonna Teresa</b> (82). Far usare <i>suo / sua</i> nelle domande.</li>
<li>B: correggere l'articolo con i possessivi. Lo studente può mostrare una foto vera della famiglia sul telefono.</li></ol>""")

    # Page 7
    pc = [("Unità 11", "So raccontare il mio fine settimana."), ("Unità 12", "So spiegare una ricetta semplice."), ("Unità 13", "So descrivere la mia giornata tipo."),
          ("Unità 14", "So presentare la mia famiglia con i possessivi."), ("Unità 14", "So dire chi è il più giovane / il più simpatico.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Il mio fratello si chiama Pedro.", "Mio fratello si chiama Pedro."), ("Mie sorelle abitano a Salvador.", "Le mie sorelle abitano a Salvador."), ("Signora, come sta tua figlia?", "Signora, come sta Sua figlia?"),
          ("Domenica mi ho alzato tardi.", "Domenica mi sono alzato/a tardi."), ("Mia nonna è la più anziana que la famiglia.", "Mia nonna è la più anziana della famiglia."), ("Questa è la mia madre.", "Questa è mia madre.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La mia famiglia.</b> Scrivi 6 frasi sulla tua famiglia: chi sono, come si chiamano, che lavoro fanno, chi è il più giovane.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante fa domande sulla famiglia dello studente: <i>Tua sorella è più grande o più piccola di te?</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("14.1", "Le nostre famiglie (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("14.2", "I dittonghi")}
<p>{" · ".join(S142)}</p>
{sub("14.3", "Presentare la famiglia")}
<p>{" ".join(S143)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 14 - La famiglia")
