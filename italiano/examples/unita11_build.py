# Speak! Essenziale A1 - Unità 11 "Il fine settimana" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 11", audio_json=os.path.join(HERE, "audio_it-a1-unita-11.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il Duomo", "Duomo"), ("B", "la bistecca", "bistecca"), ("C", "la festa", "festa"), ("D", "la partita", "partita"),
          ("E", "il treno", "treno"), ("F", "la passeggiata", "passeggiata"), ("G", "il museo", "museo"), ("H", "il ponte", "ponte")]

SCRIPT = [("Narratore", "Dialogo uno. Lunedì mattina, allo studio."), ("Marco", "Ciao, Júlia! Com'è andato il fine settimana?"),
          ("Júlia", "Benissimo! Sabato sono andata a Firenze con i miei genitori. Ho visto il Duomo e ho mangiato la bistecca fiorentina."),
          ("Marco", "E Luca?"), ("Júlia", "Luca è venuto con noi e ha fatto la guida!"), ("Marco", "E domenica?"),
          ("Júlia", "Domenica sono rimasta a casa e ho dormito tanto."),
          ("Narratore", "Dialogo due. Al bar."), ("Giulia", "Davide, che cosa hai fatto sabato sera?"),
          ("Davide", "Sono uscito con gli amici. Sono andato a una festa e sono tornato a casa alle tre!"),
          ("Giulia", "Alle tre? E domenica hai studiato?"), ("Davide", "No… non ho studiato. Ho guardato la partita del Napoli."),
          ("Giulia", "E il Napoli ha vinto?"), ("Davide", "No, ha perso!"),
          ("Narratore", "Dialogo tre. Sulle scale."), ("Signora Rossi", "Buongiorno, signora Souza. I Suoi genitori sono partiti?"),
          ("Júlia", "Sì, sono partiti ieri sera. Hanno preso il treno per Roma."), ("Signora Rossi", "E Bologna è piaciuta?"),
          ("Júlia", "Moltissimo! Hanno visto le torri, i portici… e hanno mangiato tantissimo!"), ("Signora Rossi", "E Lei è stanca?"),
          ("Júlia", "Un po'. Ieri ho lavorato tutto il giorno.")]
S112 = ["fatto", "letto", "scritto", "detto", "messo", "Ho fatto una passeggiata.", "Ho letto un libro."]
S113 = ["Com'è andato il fine settimana?", "Che cosa hai fatto sabato?", "Sabato scorso sono andata a Firenze.", "Ieri sera sono uscito con gli amici.",
        "Due giorni fa ho visto un film.", "Domenica sono rimasto a casa."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 11", "Il fine settimana", "Raccontare che cosa hai fatto · <b>il passato prossimo</b>",
                       [("SAI FARE", "raccontare il tuo fine settimana e chiedere che cosa ha fatto un'altra persona"), ("LINGUA", "ho mangiato · sono andato/a · fatto, visto, preso · ieri, sabato scorso, fa"),
                        ("PRONUNCIA", "le doppie dei participi: fatto, letto, scritto · domande sul passato")])
    words = ["il Duomo", "il museo", "il ponte", "il treno", "la bistecca", "la festa", "la partita", "la passeggiata"]
    qs = [("Ho visto", "un film / la partita"), ("Ho mangiato", "la pizza / la bistecca"), ("Sono andato/a", "al mare / a una festa"),
          ("Ho fatto", "una passeggiata"), ("Ho letto", "un libro"), ("Ho preso", "il treno")]
    ql = [f'<li value="{i+1}">{q} {A(a, "min-width:34mm")}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: il fine settimana", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Che cosa hai fatto? Completa con una parola (o due) della lista A.", "4 min")}
{twocol(ql, 4)}""",
    29, """<ol><li>A: foto A e H: <b>il Duomo</b> e <b>il Ponte Vecchio</b> di Firenze. Chiedere: <i>Sei mai stato/a a Firenze?</i> (solo da capire).</li>
<li>B: prima esposizione al passato: lo studente completa senza regola. Accettare ogni risposta logica (<i>ho preso il treno / ho visto il museo</i>…).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 parole del fine settimana con foto · prime frasi al passato</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il fine settimana di Júlia, Davide e i genitori: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Passato prossimo con <i>avere</i> ed <i>essere</i> · participi irregolari · marcatori di tempo</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Le doppie dei participi · domande sul passato</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Participi · <i>avere</i> o <i>essere</i>? · il mio fine settimana</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Il fine settimana di Luca (domande al passato) · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 07–11) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Lunedì Júlia racconta a Marco il fine settimana: sabato è andata a Firenze con i genitori e Luca ha fatto la guida; domenica è rimasta a casa. Al bar Davide racconta la festa (è tornato alle tre!) e la partita del Napoli, che ha perso. Sulle scale la signora Rossi chiede dei genitori di Júlia: sono partiti ieri sera per Roma.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Ho andato</i> ✗ → <b>Sono andata</b> (movimento = <i>essere</i>). <i>Sono mangiato</i> ✗ → <b>Ho mangiato</b>. <i>Ho faciuto</i> ✗ → <b>Ho fatto</b>. <i>Fui a Firenze</i> ✗ → <b>Sono andata a Firenze</b> (per una storia recente si usa il passato prossimo). <i>Sabato passato</i> ✗ → <b>sabato scorso</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 11.1 Tre dialoghi (lento e naturale) · Traccia 11.2 Le doppie dei participi · Traccia 11.3 Parlare del passato</div>""")

    # Page 2
    who = [("Júlia, sabato", "è andata a Firenze, ha visto il Duomo, ha mangiato la bistecca"), ("Júlia, domenica", "è rimasta a casa e ha dormito"),
           ("Davide, sabato sera", "è uscito, è andato a una festa, è tornato alle tre"), ("Davide, domenica", "ha guardato la partita del Napoli"),
           ("I genitori di Júlia, ieri sera", "sono partiti per Roma in treno")]
    wr = "".join(f"<tr><td style='width:44mm'><b>{n}</b></td><td>{A(x, 'min-width:90mm')}</td></tr>" for n, x in who)
    tf = [("Luca è venuto a Firenze con Júlia.", "V"), ("Davide ha studiato domenica.", "F"), ("Il Napoli ha vinto.", "F"), ("Ieri Júlia ha lavorato tutto il giorno.", "V")]
    tfr = "".join(f'<tr><td>{i+1}. {s}</td><td style="width:24mm;text-align:center;white-space:nowrap">{ch(["V", "F"], a)}</td></tr>' for i, (s, a) in enumerate(tf))
    b.page(f"""{sec(2, "Ascolto: com'è andato il fine settimana?", "10 min")}
<p>È lunedì. I genitori di Júlia sono stati a Bologna per tre giorni. Júlia, Davide e la signora Rossi parlano del fine settimana.</p>
{audiocard(["11.1 · SLOW", "11.1 · NATURAL"])}
{sub("A", "Ascolta. Che cosa hanno fatto? Scrivi.", "5 min", "11.1 · SLOW")}
<table style="margin:0">{wr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "3 min", "11.1 · NATURAL")}
<table class="ck" style="margin:0">{tfr}</table>
{sub("C", "Davide dice «No… non ho studiato». Perché è un po' imbarazzato?", "2 min")}
<div class="wline">{R("Perché Giulia chiede se ha studiato, ma lui ha guardato la partita (e il Napoli ha perso).")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi. Far notare: <i>Júlia è andat<b>a</b></i> / <i>Davide è andat<b>o</b></i> (pagina 3).</li>
<li>B: versione <b>naturale</b>. 2: Davide <i>non ha studiato</i>; 3: il Napoli <i>ha perso</i>. <i>Ha fatto la guida</i> = ha mostrato la città.</li></ol>""")

    # Page 3
    av = [("io", "ho", "mangiato"), ("tu", "hai", "visto"), ("lui / lei / Lei", "ha", "dormito")]
    es = [("io", "sono", "andato / andata"), ("tu", "sei", "uscito / uscita"), ("lui / lei / Lei", "è", "tornato / tornata")]
    ta = "".join(f"<tr><td>{p}</td><td><b>{x}</b></td><td>{y}</td></tr>" for p, x, y in av)
    te = "".join(f"<tr><td>{p}</td><td><b>{x}</b></td><td>{y}</td></tr>" for p, x, y in es)
    irr = [("fare", "fatto"), ("vedere", "visto"), ("prendere", "preso"), ("leggere", "letto"), ("scrivere", "scritto"), ("rimanere", "rimasto"), ("venire", "venuto"), ("perdere", "perso")]
    ti = "".join(f"<tr><td>{a}</td><td><b>{x}</b></td></tr>" for a, x in irr)
    rules = [("Júlia", "è andata", "ha andato"), ("Io", "ho mangiato", "sono mangiato"), ("Davide", "ha fatto", "ha faciuto"), ("Il weekend scorso", "sono rimasta", "ho rimasto")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: il passato prossimo", "10 min")}
{sub("A", "avere o essere + participio.", "4 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">avere + participio</th></tr>{ta}</table>
<p class="small" style="margin-top:1mm">-are → <b>-ato</b> (mangiato) · -ere → <b>-uto</b> (venduto) · -ire → <b>-ito</b> (dormito)</p></div>
<div><table style="margin:0"><tr><th colspan="3">essere + participio (-o / -a)</th></tr>{te}</table>
<p class="small" style="margin-top:1mm">Con <b>essere</b> il participio cambia: Marco è andat<b>o</b>, Júlia è andat<b>a</b>.</p></div></div>
<div class="two"><div>{sub("B", "Participi irregolari.", "2 min")}<table style="margin:0">{ti}</table></div>
<div>{sub("C", "Scegli l'opzione corretta.", "2 min")}<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>AVERE O ESSERE?</h4>Quasi tutti i verbi: <b>avere</b>. Movimento e stato: <b>essere</b>: <i>andare, venire, uscire, tornare, partire, arrivare, rimanere, stare</i>.</div></div></div>
<div class="box sand" style="margin-top:1mm"><h4>QUANDO?</h4><b>ieri</b> · <b>ieri sera</b> · <b>sabato scorso</b> · <b>la settimana scorsa</b> · <b>due giorni fa</b> · <b>il fine settimana</b></div>""",
    23, """<ol><li>A: la regola dell'accordo con <i>essere</i>: per ora basta <i>-o / -a</i> al singolare. <i>Sono partiti</i> (plurale) = solo da capire.</li>
<li>Per i brasiliani: il passato che usano ogni giorno in portoghese corrisponde qui al passato prossimo, non al passato remoto.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho andato a Firenze.</td><td><b>Sono andato/a a Firenze.</b></td><td>Movimento = <i>essere</i>.</td></tr>
<tr><td>Sono mangiato la pizza.</td><td><b>Ho mangiato la pizza.</b></td><td>Quasi tutti i verbi = <i>avere</i>.</td></tr>
<tr><td>Ho faciuto una passeggiata.</td><td><b>Ho fatto una passeggiata.</b></td><td><i>fare → fatto</i>.</td></tr>
<tr><td>Fui al mare sabato.</td><td><b>Sono andato/a al mare sabato.</b></td><td>Passato recente = passato prossimo.</td></tr>
<tr><td>Sabato passato…</td><td><b>Sabato scorso…</b></td><td>In italiano: <i>scorso</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["11.2", "11.3"])}
{sub("A", "Le doppie dei participi. Ascolta e ripeti: tt e ss sono lunghe.", "2 min", "11.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S112)}</div>
{sub("B", "Parlare del passato. Ascolta e ripeti.", "3 min", "11.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S113)}</div>""",
    38, """<ol><li>Errori: <i>fui</i> è un errore tipico: in italiano esiste (<i>passato remoto</i>), ma nel parlato di tutti i giorni si usa il <b>passato prossimo</b>.</li>
<li>4A: <i>fatto</i> ≠ <i>fato</i>, <i>letto</i> ≠ <i>leto</i>: la doppia è più lunga e forte (unità 3).</li>
<li>4B: <i>Com'è andato…?</i> = domanda molto comune il lunedì. Risposte: <i>Benissimo! / Bene / Così così.</i></li></ol>""")

    # Page 5
    iw = [("fare", "fatto"), ("vedere", "visto"), ("prendere", "preso"), ("leggere", "letto"), ("rimanere", "rimasto"), ("venire", "venuto")]
    il_ = [f'<li value="{i+1}">{a} → {A(x, "min-width:22mm")}</li>' for i, (a, x) in enumerate(iw)]
    aw = [("Ieri io", "ho lavorato", "tutto il giorno.", "lavorare"), ("Sabato Júlia", "è andata", "a Firenze.", "andare"), ("Tu", "hai visto", "il Duomo?", "vedere"),
          ("Davide", "è tornato", "a casa alle tre.", "tornare"), ("Domenica io", "ho dormito", "fino alle dieci.", "dormire"), ("Signora, Lei", "è uscita", "ieri sera?", "uscire")]
    al_ = "".join(f'<li>{a} {A(v, "min-width:26mm")} {c} <span class="small">({n})</span></li>' for a, v, c, n in aw)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Scrivi il participio.", "2 min")}
{twocol(il_, 4)}
{sub("B", "Completa con il passato prossimo.", "3 min")}
<ol>{al_}</ol>
{sub("C", "Il mio fine settimana. Scrivi 3 frasi con ieri, sabato scorso o fa.", "3 min")}
<div class="wline">{R("Esempio: Sabato scorso sono andata al cinema. Domenica ho fatto una passeggiata. Ieri sera ho letto un libro.")}</div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>B: 6 <i>Signora, Lei è uscita</i>: il participio è femminile perché è una signora.</li>
<li>C: lo studente legge le frasi; l'insegnante fa una domanda per ogni frase: <i>Con chi? A che ora sei tornato/a?</i></li></ol>""")

    # Page 6
    ag = [("Sabato mattina", "ha giocato a tennis"), ("Sabato pomeriggio", "è andato al cinema"), ("Sabato sera", "ha mangiato una pizza con Marco"),
          ("Domenica mattina", "ha dormito fino alle undici"), ("Domenica pomeriggio", "ha fatto una passeggiata ai Giardini Margherita"), ("Domenica sera", "è tornato a Firenze in treno")]
    at = "".join(f"<tr><td style='width:40mm'><b>{t}</b></td><td>{A(a, 'min-width:80mm')}</td></tr>" for t, a in ag)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Il fine settimana di Luca a Bologna. L'insegnante sa che cosa ha fatto. Fai domande e completa.", "7 min")}
<table style="margin:1mm 0 2mm">{at}</table>
<div class="bank" style="background:#fff">Che cosa ha fatto Luca sabato mattina? · Dove è andato? · Con chi? · A che ora è tornato?</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Com'è andato il tuo fine settimana?</li><li>Che cosa hai fatto sabato scorso?</li><li>Sei uscito/a? Dove sei andato/a?</li><li>Hai visto un film o una serie? Ti è piaciuto/a?</li></ol>""",
    28, """<ol><li>A: l'insegnante risponde con frasi complete (<i>Ha giocato a tennis</i>) solo se la domanda è corretta. Alla fine lo studente racconta tutto il fine settimana di Luca.</li>
<li>B: correggere la scelta <i>avere / essere</i> e l'accordo <i>-o / -a</i>. <i>Ti è piaciuto?</i> = solo da capire.</li></ol>""")

    # Page 7
    pc = [("Unità 07", "So chiedere e dare indicazioni."), ("Unità 08", "So prenotare una camera in albergo."), ("Unità 10", "So comprare il cibo al mercato."),
          ("Unità 11", "So raccontare che cosa ho fatto nel fine settimana."), ("Unità 11", "So scegliere tra avere ed essere nel passato prossimo.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Sabato ho andato al mare.", "Sabato sono andato/a al mare."), ("Ieri sono mangiato una pizza.", "Ieri ho mangiato una pizza."), ("Ho faciuto una passeggiata.", "Ho fatto una passeggiata."),
          ("Domenica passata ho visto un film.", "Domenica scorsa ho visto un film."), ("Júlia è tornato a casa.", "Júlia è tornata a casa."), ("Fui a Roma due giorni fa.", "Sono andato/a a Roma due giorni fa.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio a Giulia.</b> Racconta il tuo ultimo fine settimana (5–6 frasi): dove sei andato/a, che cosa hai fatto, con chi.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante legge il messaggio come Giulia e fa domande: <i>E poi? A che ora sei tornato/a?</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("11.1", "Com'è andato il fine settimana? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("11.2", "Le doppie dei participi")}
<p>{" · ".join(S112)}</p>
{sub("11.3", "Parlare del passato")}
<p>{" ".join(S113)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 11 - Il fine settimana")
