# Speak! Ponte A2 - Unità 03 "Che cosa è successo?" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
from fumetto import fumetto
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 03", audio_json=os.path.join(HERE, "audio_it-a2-unita-03.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'ombrello", "ombrello"), ("B", "la pozzanghera", "pozzanghera"), ("C", "il cane", "cane"), ("D", "la biblioteca", "biblioteca"),
          ("E", "il cerotto", "cerotto"), ("F", "le chiavi", "chiavi"), ("G", "la porta", "porta"), ("H", "la sveglia", "sveglia")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-03"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["03.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S032 = [x.split(": ", 1)[1] for x in _r["03.2 Ripeti frasi del racconto"].split("\n")]
S033 = [x.split(": ", 1)[1] for x in _r["03.3 Imperfetto o passato prossimo"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 03", "Che cosa è successo?", "Raccontare una storia · <b>imperfetto e passato prossimo insieme</b>",
                       [("SAI FARE", "raccontare un piccolo incidente o una storia divertente, con lo sfondo e i fatti"),
                        ("LINGUA", "Mentre attraversavo la piazza, all'improvviso un cane è uscito. · Quando si è svegliato, la porta era chiusa."),
                        ("PRONUNCIA", "il ritmo del racconto · imperfetto o passato prossimo?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: una giornata storta", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1].split("'")[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali di queste cose ci sono in una «giornata storta»? Perché?</li><li>Hai mai perso le chiavi o dimenticato l'ombrello? Che cosa hai fatto?</li><li>Qual è stata la tua ultima giornata storta?</li></ol>""",
    22, """<ol><li>A: <i>una giornata storta</i> = una giornata in cui va tutto male. <i>La pozzanghera</i>: l'acqua sulla strada dopo la pioggia. <i>La sveglia</i>: l'orologio che suona la mattina.</li>
<li>B: le domande 2 e 3 sono al passato prossimo (A1). Ascoltare se lo studente usa già l'imperfetto per lo sfondo.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: una giornata storta</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La caduta di Júlia · Bruno chiuso in biblioteca · il signore con il cappello</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Imperfetto e passato prossimo insieme · mentre, all'improvviso, quando</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Sfondo e fatti · tre combinazioni · parole che aiutano · i tempi del passato</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Il ritmo del racconto · imperfetto o passato prossimo?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>La storia di Bruno · mentre / all'improvviso · i verbi degli incidenti</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La giornata storta di Davide (fumetto) · la tua storia</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Un lunedì di novembre Júlia arriva allo studio alle dieci, bagnata: pioveva, andava in bicicletta e, mentre attraversava piazza Maggiore, un cane è uscito da sotto un portico e lei è caduta in una pozzanghera. Un signore anziano con un cappello grigio l'ha aiutata: il cane, Briciola, era suo. A pranzo Davide racconta che Bruno, sabato sera, si è addormentato in biblioteca e si è svegliato alle dieci con la porta chiusa: Júlia guardava un film e non ha risposto al telefono; Davide ha chiamato il custode. La sera la signora Rossi rivela che il signore era suo fratello Franco, e porta una torta per chiedere scusa.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>La logica è la stessa del portoghese (<i>eu atravessava a praça quando um cachorro saiu</i>), quindi lo studente capisce subito. Gli errori sono di forma: <i>ho caduto</i> (→ <b>sono caduta</b>), <i>mi sono fatto male</i> con l'accordo sbagliato, e il passato prossimo dopo <i>mentre</i> (<i>mentre ho attraversato</i>). Attenzione anche a <i>quando ero arrivata</i>: il trapassato non serve qui.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Bologna ha quasi 40 km di <b>portici</b>: con la pioggia molte persone camminano sotto i portici, ma le biciclette vanno sulla strada. Nelle università italiane il voto degli esami va da 18 a <b>30</b> (e <i>30 e lode</i> è il massimo). Le biblioteche universitarie a Bologna sono spesso in palazzi antichi; alcune restano aperte la sera, fino a mezzanotte, nel periodo degli esami.</div>
<div class="box"><h4>AUDIO</h4>Traccia 03.1 Tre dialoghi (lento e naturale) · Traccia 03.2 Frasi del racconto · Traccia 03.3 Imperfetto o passato prossimo?</div>""")

    # Page 2
    st = [("Che tempo faceva?", "pioveva"), ("Che cosa faceva Júlia?", "andava allo studio in bicicletta"), ("Che cosa è successo all'improvviso?", "un cane è uscito da un portico e lei è caduta in una pozzanghera"),
          ("Chi l'ha aiutata? Com'era?", "un signore anziano, gentilissimo, con un cappello grigio e un ombrello enorme")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:60mm')}</li>" for q, a in st)
    order = [("Bruno studiava per l'esame di storia.", 1), ("Davide ha telefonato al custode.", 5), ("Bruno si è addormentato sul libro.", 2),
             ("Bruno ha telefonato a Júlia, ma lei non ha risposto.", 4), ("Bruno si è svegliato alle dieci: la porta era chiusa.", 3), ("Bruno è uscito a mezzanotte.", 6)]
    ol = "".join(f"<tr><td style='width:12mm;text-align:center'>{A(str(n), 'min-width:7mm')}</td><td>{s}</td></tr>" for s, n in order)
    b.page(f"""{sec(2, "Ascolto: che mattina!", "10 min")}
<p>Júlia arriva tardi allo studio, Bruno passa una serata strana in biblioteca e la signora Rossi ha una sorpresa.</p>
{audiocard(["03.1 · SLOW", "03.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "4 min", "03.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Metti in ordine la storia di Bruno (1–6).", "4 min", "03.1 · NATURAL")}
<table style="margin:0">{ol}</table>
{sub("C", "Dialogo 3. Chi era il signore con il cappello? E chi era Briciola?", "2 min")}
<div class="wline">{R("il fratello della signora Rossi, Franco · Briciola era il suo cane")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Risposte 1, 2, 4 = sfondo (imperfetto); 3 = fatti (passato prossimo).</li>
<li>B: versione <b>naturale</b>. <i>Il custode</i> apre e chiude l'edificio.</li></ol>""")

    # Page 3
    rules = [("Nella frase 1, <i>pioveva</i> e <i>andavo</i> descrivono", ["lo sfondo della storia", "un fatto nuovo"], "lo sfondo della storia"),
             ("<i>Un cane è uscito</i> e <i>sono caduta</i> sono", ["lo sfondo", "i fatti che fanno andare avanti la storia"], "i fatti che fanno andare avanti la storia"),
             ("Dopo <b>mentre</b> usiamo di solito", ["l'imperfetto", "il passato prossimo"], "l'imperfetto"),
             ("Dopo <b>all'improvviso</b> e <b>a un certo punto</b> usiamo", ["l'imperfetto", "il passato prossimo"], "il passato prossimo"),
             ("Nella frase 5 ci sono due azioni nello stesso momento: usiamo", ["due imperfetti", "due passati prossimi"], "due imperfetti"),
             ("Nella frase 6, tre azioni una dopo l'altra: usiamo", ["l'imperfetto", "il passato prossimo"], "il passato prossimo")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    b.page(f"""{sec(3, "Grammatica: imperfetto e passato prossimo", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Pioveva</b> e io <b>andavo</b> allo studio in bicicletta.<br>
2. Mentre <b>attraversavo</b> piazza Maggiore, all'improvviso un cane <b>è uscito</b> e io <b>sono caduta</b>.<br>
3. <b>Era</b> gentilissimo: <b>aveva</b> un cappello grigio. &nbsp; 4. A un certo punto Bruno <b>si è addormentato</b>.<br>
5. Io <b>guardavo</b> un film, mentre Bruno <b>studiava</b>. &nbsp; 6. <b>Si è svegliato</b>, <b>ha telefonato</b> e alla fine <b>è uscito</b> a mezzanotte.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Sfondo o fatto? Scrivi S (sfondo) o F (fatto).", "3 min")}
<div class="two"><ol style="margin:0"><li>Erano le dieci di sera. {A("S", "min-width:7mm")}</li><li>La porta era chiusa. {A("S", "min-width:7mm")}</li><li>Davide ha chiamato il custode. {A("F", "min-width:7mm")}</li></ol>
<ol start="4" style="margin:0"><li>Briciola guardava Júlia. {A("S", "min-width:7mm")}</li><li>Il signore l'ha aiutata. {A("F", "min-width:7mm")}</li><li>Faceva freddo. {A("S", "min-width:7mm")}</li></ol></div>
<div class="box sand"><h4>REGOLA</h4>Nel racconto l'<b>imperfetto</b> descrive lo <b>sfondo</b> (tempo, ora, luoghi, persone, azioni in corso: <i>pioveva, era tardi, studiava</i>) e il <b>passato prossimo</b> racconta i <b>fatti</b> (<i>è uscito, è caduta, ha telefonato</i>). <b>Mentre</b> + imperfetto · <b>all'improvviso / a un certo punto / alla fine</b> + passato prossimo. Tutto su come usarli insieme: pagina 4.</div>""",
    20, """<ol><li>B: disegnare la linea del tempo: una barra lunga (<i>attraversavo</i>) e un punto che la interrompe (<i>è uscito</i>).</li>
<li>C: domanda utile: <i>Che cosa è successo dopo?</i> Se c'è una risposta, è un fatto (F).</li></ol>""")

    grammar_ref_it.imperfetto_passato_prossimo(b)

    # Page 5
    ans3 = ["imperfetto", "passato prossimo", "imperfetto", "passato prossimo", "imperfetto", "passato prossimo"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho caduto dalla bicicletta.</td><td><b>Sono caduta dalla bicicletta.</b></td><td><i>cadere</i> → <i>essere</i>.</td></tr>
<tr><td>Mentre ho attraversato la piazza…</td><td><b>Mentre attraversavo la piazza…</b></td><td><i>mentre</i> + imperfetto.</td></tr>
<tr><td>All'improvviso il cane usciva.</td><td><b>All'improvviso il cane è uscito.</b></td><td>Un fatto: passato prossimo.</td></tr>
<tr><td>Quando sono arrivata, la porta è stata chiusa.</td><td><b>Quando sono arrivata, la porta era chiusa.</b></td><td>Descrizione: imperfetto.</td></tr>
<tr><td>Júlia si è fatto male.</td><td><b>Júlia si è fatta male.</b></td><td>Riflessivo: accordo con il soggetto.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["03.2", "03.3"])}
{sub("A", "Il ritmo del racconto. Ascolta e ripeti. La voce resta in alto sullo sfondo e scende sul fatto.", "2 min", "03.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S032)}</div>
{sub("B", "Imperfetto o passato prossimo? Ascolta e scegli.", "2 min", "03.3")}
{twocol([f'<li value="{i+1}">{ch(["imperfetto", "passato prossimo"], a)}</li>' for i, a in enumerate(ans3)], 3)}""",
    28, """<ol><li>Errori: nel 4, <i>era chiusa</i> descrive com'era la porta (sfondo); <i>è stata chiusa</i> vuol dire che qualcuno l'ha chiusa in quel momento.</li>
<li>4B: dopo la scelta, lo studente trasforma la frase nell'altro tempo: <i>Marco leggeva → Marco ha letto</i>.</li></ol>""")

    # Page 6
    gb = [("Sabato sera Bruno ", ["era", "è stato"], "era", " in biblioteca. "), ("", ["Studiava", "Ha studiato"], "Studiava", " per l'esame di storia e "),
          ("", ["era", "è stato"], "era", " stanchissimo. A un certo punto "), ("", ["si addormentava", "si è addormentato"], "si è addormentato", " sul libro. Quando "),
          ("", ["si svegliava", "si è svegliato"], "si è svegliato", ", "), ("", ["erano", "sono state"], "erano", " le dieci e le luci "),
          ("", ["erano", "sono state"], "erano", " spente. Bruno "), ("", ["telefonava", "ha telefonato"], "ha telefonato", " a Júlia, ma lei "),
          ("", ["guardava", "ha guardato"], "guardava", " un film. Alla fine Bruno "), ("", ["usciva", "è uscito"], "è uscito", " a mezzanotte.")]
    gbt = "".join(f"{a}<i>{ch(o, r)}</i>{z}" for a, o, r, z in gb)
    mx = [("Mentre Marco faceva colazione,", "è arrivato un messaggio di Júlia."), ("Mentre Giulia preparava i caffè,", "un cliente ha rotto una tazza."),
          ("Mentre la signora Rossi cucinava,", "è andata via la luce."), ("Mentre Davide correva al parco,", "ha perso le chiavi di casa.")]
    left = "".join(f"<li>{a}</li>" for a, _ in mx)
    order = ["c", "a", "d", "b"]
    rgt = [mx[1][1], mx[3][1], mx[0][1], mx[2][1]]
    right = "".join(f"<li>{x}</li>" for x in rgt)
    wb = [("cadere", "andare per terra all'improvviso"), ("farsi male", "sentire dolore dopo un incidente"), ("rompere", "fare in due o più pezzi un oggetto"),
          ("perdere", "non trovare più una cosa"), ("dimenticare", "non ricordare: «Ho … l'ombrello!»"), ("addormentarsi", "cominciare a dormire"),
          ("scivolare", "cadere sul pavimento bagnato o sul ghiaccio"), ("succedere", "«Che cosa è …?» = che cosa è capitato?")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:19mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "La storia di Bruno. Scegli il tempo giusto.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9.2pt;line-height:1.9">{gbt}</div>
{sub("B", "Mentre… all'improvviso. Unisci le due parti (1–4 con a–d).", "2 min")}
<div class="two"><ol style="margin:0">{left}</ol><ol type="a" style="margin:0">{right}</ol></div>
<p class="small" style="margin:.5mm 0">{R("1 c · 2 a · 3 d · 4 b") if T else ""}</p>
{sub("C", "I verbi degli incidenti. Scrivi il verbo giusto.", "3 min")}
<div class="bank">addormentarsi · cadere · dimenticare · farsi male · perdere · rompere · scivolare · succedere</div>
{twocol(wbl, 4)}""",
    20, """<ol><li>A: rileggere la storia ad alta voce. B: <i>mentre</i> + imperfetto, poi il fatto.</li>
<li>C: <i>Che cosa hai rotto l'ultima volta?</i></li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "La giornata storta di Davide. Guarda il fumetto e racconta la storia all'insegnante. Usa l'imperfetto per lo sfondo e il passato prossimo per i fatti.", "5 min")}
{fumetto()}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Era lunedì… · Davide dormiva / ha dormito troppo · la sveglia non ha suonato · pioveva · aspettava l'autobus · l'autobus era in ritardo · all'improvviso · è arrivato un messaggio · la lezione era annullata · alla fine è tornato a casa</div>
{sub("B", "La tua storia. Racconta all'insegnante una giornata storta o una storia divertente. Rispondi alle sue domande.", "5 min")}
<ol style="line-height:1.6"><li>Quando è successo? Dov'eri? Che tempo faceva?</li><li>Che cosa facevi? Con chi eri?</li><li>Che cosa è successo all'improvviso?</li><li>Che cosa hai fatto? Com'è finita?</li></ol>
{sub("C", "Poi l'insegnante racconta la sua storia. Fai tu le domande.", "2 min")}""",
    22, """<ol><li>A: modello: <i>Era lunedì e la sveglia non ha suonato. Pioveva e l'autobus era in ritardo. Mentre aspettava, è arrivato un messaggio: la lezione era annullata! Alla fine è tornato a letto.</i></li>
<li>B: annotare gli errori di tempo e correggerli alla fine, chiedendo: <i>Sfondo o fatto?</i></li></ol>""")

    # Page 8
    pc = [("A2 · 01", "So usare mi, ti, gli, le e fare paragoni."), ("A2 · 02", "So raccontare com'era la mia infanzia con l'imperfetto."),
          ("A2 · 03", "So raccontare una storia con lo sfondo e i fatti."), ("A2 · 03", "So usare mentre, all'improvviso, a un certo punto, alla fine."),
          ("A2 · 03", "So chiedere: Che cosa è successo? Ti sei fatto/a male?")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Mentre ho cucinato, è arrivata mia sorella.", "Mentre cucinavo, è arrivata…"), ("Era tardi e faceva freddo.", "✓"),
          ("All'improvviso il telefono suonava.", "…il telefono ha suonato."), ("Ho caduto per le scale.", "Sono caduto/a per le scale."),
          ("Mentre io leggevo, mio marito guardava la TV.", "✓"), ("Quando sono uscita, è piovuto molto.", "Quando sono uscita, pioveva molto.")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:44mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Che cosa è successo? (50–75 parole).</b> Racconta un piccolo incidente o una storia divertente. Comincia con lo sfondo (<i>Era…, pioveva…, ero…</i>), poi racconta i fatti con <i>all'improvviso, a un certo punto, alla fine</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge la storia; l'insegnante fa domande (<i>E poi? Com'è finita?</i>). Unità 04: <i>Dal medico</i>.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("03.1", "Che mattina! (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("03.2", "Frasi del racconto")}
<p>{" ".join(S032)}</p>
{sub("03.3", "Imperfetto o passato prossimo?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S033))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 03 - Che cosa è successo")
