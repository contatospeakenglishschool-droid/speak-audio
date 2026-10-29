# Speak! Essenziale A1 - Unità 17 "Che tempo fa?" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from meteo import icon
setup(band="A1 · UNITÀ 17", audio_json=os.path.join(HERE, "audio_it-a1-unita-17.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il sole", "sole"), ("B", "la pioggia", "pioggia"), ("C", "la neve", "neve"), ("D", "la nebbia", "nebbia"),
          ("E", "il vento", "vento"), ("F", "le nuvole", "nuvole"), ("G", "il temporale", "temporale"), ("H", "l'ombrello", "ombrello")]

SCRIPT = [("Narratore", "Dialogo uno. Una mattina di gennaio, sulle scale."), ("Júlia", "Buongiorno, signora Rossi! Che freddo oggi!"),
          ("Signora Rossi", "Buongiorno, Júlia. Sì, fa freddo e c'è la nebbia. A Bologna, in gennaio, c'è spesso la nebbia."),
          ("Júlia", "A Belo Horizonte adesso fa caldo: è estate!"), ("Signora Rossi", "Davvero? Allora in Brasile le stagioni sono al contrario!"),
          ("Narratore", "Dialogo due. Al bar."), ("Giulia", "Júlia, quando arriva tuo fratello?"),
          ("Júlia", "Arriva il quindici febbraio e riparte il sette marzo."),
          ("Giulia", "Che bello, vede il Carnevale in Italia! Ma attenzione: a febbraio fa ancora freddo e a volte nevica."),
          ("Júlia", "Lo so. Bruno ha già comprato un cappotto!"),
          ("Narratore", "Dialogo tre. Davide ha un'idea per il fine settimana."), ("Davide", "Júlia, sabato andiamo a fare una passeggiata sui colli?"),
          ("Júlia", "Volentieri! Che tempo fa sabato?"),
          ("Davide", "Aspetta, guardo le previsioni... Sabato piove. Ma domenica c'è il sole e ci sono diciotto gradi."),
          ("Júlia", "Allora andiamo domenica!"), ("Davide", "Perfetto: domenica, il primo febbraio.")]
S172 = ["freddo", "caldo", "tempo", "vento", "nuvoloso", "autunno", "Oggi fa freddo e c'è vento."]
S173 = ["Che tempo fa oggi?", "Fa caldo e c'è il sole.", "Piove e fa freddo.", "In inverno a volte nevica.", "Ci sono diciotto gradi.", "Il mio compleanno è il primo maggio."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 17", "Che tempo fa?", "Il tempo, le stagioni e le date · <b>fa freddo, c'è il sole</b>",
                       [("SAI FARE", "parlare del tempo e delle stagioni, dire le date e il tuo compleanno"),
                        ("LINGUA", "fa caldo / c'è il sole / piove · in inverno, a dicembre · il primo maggio, il due giugno"),
                        ("PRONUNCIA", "la O finale: freddo, caldo, vento · parlare del tempo")])
    words = ["il sole", "la pioggia", "la neve", "la nebbia", "il vento", "le nuvole", "il temporale", "l'ombrello"]
    rd = [("Dicembre, gennaio, febbraio: in Italia è", "inverno"), ("Marzo, aprile, maggio: in Italia è", "primavera"),
          ("Giugno, luglio, agosto: in Italia è", "estate"), ("Settembre, ottobre, novembre: in Italia è", "autunno"),
          ("A dicembre in Brasile è", "estate"), ("A luglio in Brasile è", "inverno")]
    rl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}.</li>' for i, (a, x) in enumerate(rd)]
    b.page(f"""{sec(1, "Riscaldamento: il tempo e le stagioni", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le parole sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1].lstrip("l'")))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Che stagione è? Completa. Due parole si usano due volte.", "4 min")}
<div class="bank" style="background:#fff">autunno · estate · inverno · primavera</div>
{twocol(rl, 4)}""",
    24, """<ol><li>A: <i>la pioggia</i> (nome) → <i>piove</i> (verbo); <i>la neve</i> → <i>nevica</i>. Chiedere: <i>Che tempo fa oggi?</i></li>
<li>B: 5–6: in Brasile le stagioni sono al contrario. I mesi si scrivono con la lettera <b>minuscola</b>: <i>gennaio, dicembre</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto del tempo · le stagioni</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Nebbia, Carnevale e una passeggiata: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Che tempo fa? · mesi e stagioni · le date</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>La O finale · parlare del tempo</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Le previsioni in Italia · le date · fa / c'è / ho</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Il tempo in Brasile e in Italia · le tue stagioni</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 14–17) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>È gennaio: a Bologna fa freddo e c'è la nebbia, mentre a Belo Horizonte è estate. Bruno, il fratello di Júlia, arriva il 15 febbraio e riparte il 7 marzo: vede il Carnevale in Italia (e ha già comprato un cappotto). Davide propone una passeggiata sui colli: sabato piove, quindi vanno domenica, il primo febbraio.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>È freddo oggi</i> ✗ → <b>fa freddo</b>. <i>Fa sole</i> ✗ → <b>c'è il sole</b>. <i>Sono freddo</i> ✗ → <b>ho freddo</b> (la persona). <i>L'uno maggio</i> ✗ → <b>il primo maggio</b>. <i>In 1995</i> ✗ → <b>nel 1995</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In autunno e in inverno la <b>nebbia</b> è tipica della Pianura Padana (Bologna, Milano). Gli italiani guardano spesso <b>il meteo</b> (le previsioni del tempo) al telegiornale o sull'app. Le temperature sono in gradi Celsius, come in Brasile.</div>
<div class="box"><h4>AUDIO</h4>Traccia 17.1 Tre dialoghi (lento e naturale) · Traccia 17.2 La O finale · Traccia 17.3 Parlare del tempo</div>""")

    # Page 2
    tt = [("A Bologna in gennaio", "fa freddo, c'è la nebbia"), ("A Belo Horizonte adesso", "fa caldo, è estate"), ("Bruno arriva", "il 15 febbraio"),
          ("Bruno riparte", "il 7 marzo"), ("Sabato", "piove"), ("Domenica", "c'è il sole, 18 gradi")]
    ttr = "".join(f"<tr><td style='width:52mm'><b>{a}</b></td><td>{A(x, 'min-width:62mm')}</td></tr>" for a, x in tt)
    gp = [("A Bologna, in gennaio, c'è spesso la", "nebbia", "."), ("In Brasile le stagioni sono al", "contrario", "!"),
          ("A febbraio fa ancora freddo e a volte", "nevica", "."), ("Domenica è il", "primo", "febbraio.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: nebbia, Carnevale e una passeggiata", "10 min")}
<p>È gennaio. Júlia parla del tempo con la signora Rossi, con Giulia al bar e con Davide.</p>
{audiocard(["17.1 · SLOW", "17.1 · NATURAL"])}
{sub("A", "Ascolta e completa.", "4 min", "17.1 · SLOW")}
<table style="margin:0">{ttr}</table>
{sub("B", "Ascolta di nuovo e completa.", "4 min", "17.1 · NATURAL")}
<ol>{"".join(gl)}</ol>
{sub("C", "Perché Bruno, il fratello di Júlia, ha comprato un cappotto?", "2 min")}
<div class="wline">{R("Perché a febbraio in Italia fa ancora freddo e a volte nevica.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi (<i>freddo, nebbia</i>). <i>I colli</i> = le colline vicino a Bologna.</li>
<li>B: versione <b>naturale</b>. <i>Il primo febbraio</i>: per il giorno 1 si usa l'ordinale (pagina 3).</li></ol>""")

    # Page 3
    w = [("fa", "caldo · freddo · bel tempo · brutto tempo"), ("c'è", "il sole · il vento · la nebbia · un temporale"), ("piove · nevica", "(verbi)"),
         ("è", "nuvoloso · sereno"), ("ci sono", "18 gradi · 2 gradi")]
    tw = "".join(f"<tr><td style='width:28mm'><b>{a}</b></td><td>{x}</td></tr>" for a, x in w)
    st = [("in inverno", "dicembre · gennaio · febbraio"), ("in primavera", "marzo · aprile · maggio"), ("in estate", "giugno · luglio · agosto"),
          ("in autunno", "settembre · ottobre · novembre")]
    tst = "".join(f"<tr><td><b>{a}</b></td><td>{x}</td></tr>" for a, x in st)
    rules = [("Oggi", "fa freddo", "è freddo"), ("Il mio compleanno è", "il primo maggio", "l'uno maggio"),
             ("Domani", "c'è il sole", "fa sole"), ("Sono nata", "nel 1995", "in 1995")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: che tempo fa? · mesi e stagioni · le date", "10 min")}
{sub("A", "Che tempo fa?", "3 min")}
<table style="margin:0">{tw}</table>
<div class="two"><div>{sub("B", "Le stagioni e i mesi.", "2 min")}<table style="margin:0">{tst}</table>
<p class="small" style="margin-top:1mm"><b>a</b> / <b>in</b> + mese: <i>a dicembre, in agosto</i>.</p></div>
<div>{sub("C", "Le date.", "2 min")}<p><i>Che giorno è oggi?</i> — <b>È il due dicembre.</b><br>
Giorno 1 = <b>il primo</b>: <i>il primo maggio</i><br>Gli altri giorni = numeri: <i>il due giugno, il quindici agosto</i><br>
Anno: <b>nel</b> 1995, <b>nel</b> 2026<br><span class="small">Ordinali: primo, secondo, terzo</span></p></div></div>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>""",
    24, """<ol><li>A: il tempo usa <b>fare</b> (<i>fa caldo</i>), non <i>essere</i>. Ma la persona: <b>ho</b> caldo / <b>ho</b> freddo.</li>
<li>C: la data si scrive giorno / mese / anno, come in Brasile: <i>2/12</i> = il due dicembre.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Oggi è molto freddo.</td><td><b>Oggi fa molto freddo.</b></td><td>Il tempo: <i>fare</i>.</td></tr>
<tr><td>Fa sole.</td><td><b>C'è il sole.</b></td><td><i>c'è</i> + sole, vento, nebbia.</td></tr>
<tr><td>Sono freddo.</td><td><b>Ho freddo.</b></td><td>La persona: <i>avere</i>.</td></tr>
<tr><td>L'uno maggio.</td><td><b>Il primo maggio.</b></td><td>Giorno 1: <i>primo</i>.</td></tr>
<tr><td>Sono nato in 1998.</td><td><b>Sono nato nel 1998.</b></td><td>Anno: <i>nel</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["17.2", "17.3"])}
{sub("A", "La O finale. Ascolta e ripeti: la O resta O (FREDDO, non «freddu»).", "2 min", "17.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S172)}</div>
{sub("B", "Parlare del tempo. Ascolta e ripeti.", "3 min", "17.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S173)}</div>""",
    38, """<ol><li>Errori: <i>sono freddo</i> in italiano vuol dire che la persona è fredda (di carattere)!</li>
<li>4A: molti brasiliani chiudono la <i>o</i> e la <i>e</i> finali («freddu», «tempu», «parte» come «parti»). In italiano le vocali finali sono chiare e piene.</li>
<li>4B: <i>gradi</i>: <i>ci sono diciotto gradi</i>; con 1 grado: <i>c'è un grado</i>.</li></ol>""")

    # Page 5
    fc = [("Milano", "nebbia", "6"), ("Venezia", "pioggia", "9"), ("Roma", "sole", "17"), ("Napoli", "vento", "15"), ("Torino", "neve", "1"), ("Palermo", "nuvoloso", "20")]
    cells = "".join(f"<td style='text-align:center;padding:1.5mm'><b>{c}</b><br>{icon(k)}<br><b>{g}°</b></td>" for c, k, g in fc)
    fct = f"<table style='margin:1mm 0 2mm'><tr>{cells}</tr></table>"
    ws = [("Milano", "A Milano c'è la nebbia e ci sono sei gradi."), ("Roma", "A Roma c'è il sole e ci sono diciassette gradi."),
          ("Torino", "A Torino nevica e c'è un grado."), ("Venezia", "A Venezia piove e ci sono nove gradi.")]
    wl = "".join(f'<li>{c}<div class="wline">{R(x)}</div></li>' for c, x in ws)
    dt = [("1/5", "il primo maggio"), ("25/12", "il venticinque dicembre"), ("2/6", "il due giugno"), ("15/8", "il quindici agosto")]
    dtl = [f'<li value="{i+1}">{a} {A(x, "min-width:42mm")}</li>' for i, (a, x) in enumerate(dt)]
    fh = [("Oggi", "fa", "caldo."), ("", "C'è", "il sole."), ("", "Ci sono", "trenta gradi!"), ("Io", "ho", "caldo.")]
    fhl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")} {c}</li>' for i, (a, x, c) in enumerate(fh)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Le previsioni per domani. Guarda e scrivi: che tempo fa?", "4 min")}
{fct}
<ol>{wl}</ol>
{sub("B", "Scrivi le date in lettere.", "2 min")}
{twocol(dtl, 3)}
{sub("C", "Completa con fa, c'è, ci sono, ho.", "2 min")}
{twocol(fhl, 3)}""",
    22, """<ol><li>A: accettare anche <i>a Torino c'è la neve</i>. Domanda extra: <i>Che tempo fa a Napoli? E a Palermo?</i> (c'è vento / è nuvoloso).</li>
<li>B: 2/6 è la Festa della Repubblica; 15/8 è Ferragosto.</li></ol>""")

    # Page 6
    br = [("Recife", "sole", "31"), ("São Paulo", "nuvoloso", "21"), ("Porto Alegre", "pioggia", "14"), ("Belo Horizonte", "temporale", "26")]
    brc = "".join(f"<td style='text-align:center;padding:1.5mm'><b>{c}</b><br>{icon(k)}<br><b>{g}°</b></td>" for c, k, g in br)
    it = [("Che tempo fa a Bologna?", "c'è la nebbia, 4 gradi"), ("E a Firenze?", "piove, 8 gradi"), ("E a Bari?", "c'è il sole, 16 gradi"), ("E a Cortina?", "nevica, −3 gradi")]
    itr = "".join(f"<tr><td style='width:52mm'><b>{q}</b></td><td>{A(a, 'min-width:58mm')}</td></tr>" for q, a in it)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Oggi in Brasile. Descrivi il tempo all'insegnante.", "3 min")}
<table style="margin:1mm 0 2mm"><tr>{brc}</tr></table>
{sub("B", "Oggi in Italia. Fai le domande all'insegnante e completa.", "4 min")}
<table style="margin:1mm 0 2mm">{itr}</table>
{sub("C", "Le tue stagioni. Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Che tempo fa oggi nella tua città?</li><li>Qual è la tua stagione preferita? Perché?</li><li>Quando è il tuo compleanno? Che tempo fa di solito?</li><li>Che cosa fai quando piove?</li></ol>""",
    26, """<ol><li>A: <i>A Recife c'è il sole e ci sono trentun gradi.</i> Per Belo Horizonte: <i>c'è un temporale</i>.</li>
<li>B: le risposte in rosso sono solo per l'insegnante. Cortina d'Ampezzo è in montagna, nelle Dolomiti.</li>
<li>C: correggere <i>fa / c'è</i> e la data del compleanno (<i>il primo…</i>).</li></ol>""")

    # Page 7
    pc = [("Unità 14", "So presentare la mia famiglia."), ("Unità 15", "So descrivere la mia casa."), ("Unità 16", "So comprare un biglietto del treno."),
          ("Unità 17", "So dire che tempo fa e parlare delle stagioni."), ("Unità 17", "So dire le date e il mio compleanno.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Oggi è molto caldo.", "Oggi fa molto caldo."), ("Domani fa sole.", "Domani c'è il sole."), ("Sono freddo, chiudo la finestra.", "Ho freddo, chiudo la finestra."),
          ("Il mio compleanno è l'uno marzo.", "Il mio compleanno è il primo marzo."), ("Sono nato in 1998.", "Sono nato nel 1998."), ("In inverno a Torino neva.", "In inverno a Torino nevica.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il tempo nella mia città.</b> Scrivi 6 frasi: che tempo fa nella tua città in estate e in inverno, qual è la tua stagione preferita e quando è il tuo compleanno.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante chiede: <i>Che giorno è oggi? Che tempo fa?</i> La prossima unità è il <b>Ripasso 2</b> (unità 10–17).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("17.1", "Nebbia, Carnevale e una passeggiata (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("17.2", "La O finale")}
<p>{" · ".join(S172)}</p>
{sub("17.3", "Parlare del tempo")}
<p>{" ".join(S173)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 17 - Che tempo fa")
