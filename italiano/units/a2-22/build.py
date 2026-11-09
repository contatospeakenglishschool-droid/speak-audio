# Speak! Ponte A2 - Unità 22 "Che caldo!" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 22", audio_json=os.path.join(HERE, "audio_it-a2-unita-22.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il termometro", "termometro"), ("B", "il ventilatore", "ventilatore"), ("C", "il condizionatore", "condizionatore"), ("D", "le persiane", "persiane"),
          ("E", "il ventaglio", "ventaglio"), ("F", "la zanzara", "zanzara"), ("G", "il temporale", "temporale"), ("H", "l'ombra", "ombra")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-22"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["22.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S222 = [x.split(": ", 1)[1] for x in _r["22.2 Ripeti"].split("\n")]
S223 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["22.3 Futuro o supposizione"].split("\n")]


def _key(w):
    w = w.split("'")[-1] if "'" in w else (w.split(" ", 1)[1] if w.split(" ", 1)[0] in ("la", "il", "i", "gli", "lo", "le") else w)
    return w.lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 22", "Che caldo!", "Il tempo, il clima e l'ambiente · <b>il futuro di supposizione · se + futuro</b>",
                       [("SAI FARE", "parlare del caldo e del tempo, fare ipotesi su una cosa che non sai, fare previsioni, parlare del cambiamento climatico, dare consigli per l'estate"),
                        ("LINGUA", "Saranno trentacinque gradi. · Sarà in biblioteca. · Se domani farà caldo, lavorerò da casa."),
                        ("PRONUNCIA", "la voce del dubbio: Mah… saranno trentacinque.")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: l'estate in città", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quanti gradi ci sono oggi nella tua città? E d'estate?</li><li>Che cosa fai quando fa molto caldo? Usi il ventilatore o il condizionatore?</li><li>Secondo te, le estati sono più calde di prima?</li></ol>""",
    31, """<ol><li>A: <i>il condizionatore</i> = l'aria condizionata (tutte e due le parole sono comuni); <i>le persiane</i> si chiudono di giorno per tenere fresca la casa; <i>il temporale</i> = pioggia forte con tuoni e lampi.</li>
<li>B: domanda 1: se lo studente non sa, l'insegnante risponde <i>Mah… saranno trenta gradi</i>: primo contatto con la supposizione.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il caldo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>In ufficio senza aria condizionata · sulle scale</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Futuro di supposizione · se + futuro</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Futuri irregolari · futuro o supposizione · se + futuro</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>La voce del dubbio · futuro o supposizione?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Fai un'ipotesi · se… · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Chi sarà? · il clima che cambia</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine luglio, ondata di caldo a Bologna (Giulia e Davide sono ancora in Puglia, unità 21). Alle tre del pomeriggio nell'ufficio di Marco e Júlia l'aria condizionata non funziona: <i>saranno trentacinque gradi</i>. Il tecnico doveva arrivare nel pomeriggio: <i>sarà ancora in pausa pranzo</i>. Júlia: <i>se domani farà ancora così caldo, lavorerò da casa</i>. Marco parla del cambiamento climatico: nel giardino in Bolognina pianteranno più alberi per fare ombra. La sera la signora Rossi (persiane chiuse tutto il giorno) e Júlia fanno ipotesi su Bruno, che non risponde: <i>sarà in biblioteca… sarà al cinema</i>. Domani pioverà, forse. Bruno richiama: era al cinema con Chiara. <i>Lo sapevo!</i></div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Per una supposizione il portoghese dice <i>deve estar</i> o <i>será que…?</i>: lo studente usa <i>deve essere</i> o <i>forse è</i>, corretti ma meno naturali. Il futuro di supposizione (<b>sarà</b>, <b>avrà</b>, <b>ci saranno</b>) sembra strano perché "parla del futuro": spiegarlo con la voce del dubbio. Attenzione anche ai futuri sbagliati <i>esserà, averà</i> (→ <b>sarà, avrà</b>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Pianura Padana d'estate c'è <b>l'afa</b>: caldo umido, spesso più di 35 gradi, e tante <b>zanzare</b> (la zanzara tigre). Molte case non hanno l'aria condizionata: si chiudono le <b>persiane</b> di giorno e si aprono le finestre la notte. Quando fa molto caldo, il Ministero della Salute dà l'<b>allerta caldo</b> (bollino rosso): bere acqua e non uscire nelle ore centrali.</div>
<div class="box"><h4>AUDIO</h4>Traccia 22.1 I due dialoghi (lento e naturale) · Traccia 22.2 Ascolta e ripeti · Traccia 22.3 Futuro o supposizione?</div>""")

    # Page 2
    p1 = [("Secondo Marco, nell'ufficio ci saranno", "trentacinque gradi"), ("E fuori ce ne saranno", "trentotto"),
          ("Il tecnico ha detto che arriverà", "oggi pomeriggio"), ("Se domani farà ancora caldo, Júlia", "lavorerà da casa"),
          ("Nel giardino in Bolognina pianteranno", "più alberi")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:46mm')}</td></tr>" for a, x in p1)
    vf = [("La signora Rossi ha aperto le persiane tutto il giorno.", "F"), ("Bruno non risponde al telefono.", "V"), ("Secondo la signora Rossi, Bruno sarà in biblioteca.", "V"),
          ("Domani, dicono, farà ancora più caldo.", "F"), ("Bruno era al cinema con Chiara.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: che afa!", "10 min")}
{audiocard(["22.1 · SLOW", "22.1 · NATURAL"])}
{sub("A", "Prima parte. In ufficio, alle tre del pomeriggio. Completa.", "4 min", "22.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. La sera, sulle scale. Vero (V) o falso (F)?", "4 min", "22.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che consiglio dà la signora Rossi a Júlia?", "2 min")}
<div class="wline">{R("Di bere molta acqua (e di chiudere le persiane di giorno).")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Chiedere: <i>Marco è sicuro? Come lo sai?</i> (<i>mah…</i> + futuro = non è sicuro).</li>
<li>B: frase 4: domani <b>pioverà</b>, forse (<i>dicono che</i>). <i>Che afa!</i> = che caldo umido.</li></ol>""")

    # Page 3
    rules = [("<i>Mah… <b>saranno</b> trentacinque.</i> Marco parla", ["di adesso", "di domani"], "di adesso"),
             ("Marco è sicuro?", ["no, fa un'ipotesi", "sì, lo sa"], "no, fa un'ipotesi"),
             ("<i><b>Sarà</b> in biblioteca</i> vuole dire", ["forse è in biblioteca", "domani va in biblioteca"], "forse è in biblioteca"),
             ("Per le supposizioni si usano soprattutto", ["essere e avere", "tutti i verbi regolari"], "essere e avere"),
             ("<i>Se domani <b>farà</b> caldo, <b>lavorerò</b> da casa.</i> Dopo <i>se</i> c'è il", ["futuro", "passato prossimo"], "futuro"),
             ("<i>Domani <b>pioverà</b>.</i> Questo è", ["un vero futuro", "una supposizione"], "un vero futuro")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Dov'è Davide? —", ["Sarà", "Sarò"], "Sarà", "ancora in Puglia."), ("Che ore sono? —", ["Saranno", "Sono saranno"], "Saranno", "le dieci."),
          ("Marco non mangia:", ["avrà", "averà"], "avrà", "troppo caldo."), ("Se domani", ["pioverà", "piovuto"], "pioverà", "e farà freddo, resteremo a casa.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il futuro di supposizione", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Quanti gradi <b>ci saranno</b> qui dentro? — Mah… <b>saranno</b> trentacinque. · <b>Sarà</b> ancora in pausa pranzo. · O <b>sarà</b> in un altro ufficio. · <b>Sarà</b> in biblioteca. · No… <b>sarà</b> al cinema con Chiara.<br>
2. Il tecnico <b>arriverà</b> oggi pomeriggio. · Domani <b>pioverà</b>. · Pianteremo più alberi: <b>faranno</b> ombra.<br>
3. <b>Se</b> domani <b>farà</b> ancora così caldo, <b>lavorerò</b> da casa. · <b>Se pioverà</b>, finalmente <b>dormiremo</b>!</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Il <b>futuro</b> serve anche per una <b>supposizione sul presente</b>: <i>Sarà al cinema</i> = forse è al cinema. Soprattutto con <b>sarà / saranno</b>, <b>avrà / avranno</b>, <b>ci sarà / ci saranno</b>. Ipotesi sul futuro: <b>se + futuro, futuro</b>: <i>Se pioverà, dormiremo.</i> Tutto: pagina 4.</div>""",
    22, """<ol><li>B: confrontare alla lavagna <i>Bruno è al cinema</i> (lo so) / <i>Bruno sarà al cinema</i> (penso). Leggerle con voce sicura e voce di dubbio.</li>
<li>C: frase 4: <i>pioverà</i> = futuro di <i>piovere</i>; il verbo del tempo si usa solo alla terza persona.</li></ol>""")

    grammar_ref_it.futuro_supposizione(b)

    # Page 5
    ans3 = ["futuro", "supposizione", "supposizione", "futuro", "supposizione", "futuro"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Esserà in biblioteca.</td><td><b>Sarà in biblioteca.</b></td><td>Futuro irregolare: <i>sarà</i>.</td></tr>
<tr><td>Averà caldo.</td><td><b>Avrà caldo.</b></td><td>Futuro irregolare: <i>avrà</i>.</td></tr>
<tr><td>Quanti gradi saranno?</td><td><b>Quanti gradi ci saranno?</b></td><td><i>esserci</i> → <i>ci saranno</i>.</td></tr>
<tr><td>Fa molto calore.</td><td><b>Fa molto caldo.</b></td><td>Il tempo: <i>fa caldo</i>.</td></tr>
<tr><td>Saranno le nove ore.</td><td><b>Saranno le nove.</b></td><td>L'ora: senza <i>ore</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["22.2", "22.3"])}
{sub("A", "Ascolta e ripeti. Quando non siamo sicuri, la voce è più lenta e scende alla fine: Mah… saranno trentacinque.", "2 min", "22.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S222)}</div>
{sub("B", "Futuro o supposizione? Ascolta e scegli.", "2 min", "22.3")}
{twocol([f'<li value="{i+1}">{ch(["futuro", "supposizione"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>calore</i> esiste (il calore del sole), ma per il tempo si dice <i>fa caldo, ho caldo</i>.</li>
<li>4A: far ripetere la stessa frase due volte: sicura (<i>È in biblioteca.</i>) e con dubbio (<i>Mah… sarà in biblioteca.</i>).</li>
<li>4B: numero 6: <i>se pioverà</i> = ipotesi sul futuro, quindi futuro vero.</li></ol>""")

    # Page 6
    ip = [("Júlia non trova Bruno. (in biblioteca)", "Sarà in biblioteca."), ("Che ore sono? (le undici)", "Saranno le undici."),
          ("Quanti anni ha la signora Rossi? (settantacinque anni)", "Avrà settantacinque anni."), ("Quanta gente c'è al concerto? (mille persone)", "Ci saranno mille persone.")]
    ipl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in ip)
    se = [("Se domani (fare) caldo, (andare) al lago.", "farà · andrò"), ("Se il tecnico non (venire), (lavorare) da casa.", "verrà · lavorerò"),
          ("Se (piovere), finalmente (dormire, noi).", "pioverà · dormiremo")]
    sel = "".join(f"<li>{q} {A(a, 'min-width:42mm')}</li>" for q, a in se)
    wb = [("caldo", "il caldo"), ("piovere", "la pioggia"), ("piantare", "la pianta"), ("prevedere", "la previsione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Fai un'ipotesi con il futuro.", "4 min")}
<ol style="line-height:1.45">{ipl}</ol>
{sub("B", "Se… Scrivi i verbi al futuro.", "3 min")}
<ol style="line-height:1.7">{sel}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 3: età con <i>avere</i> → <i>avrà</i>. Frase 4: <i>c'è gente</i> → <i>ci saranno</i>.</li>
<li>C: <i>le previsioni del tempo</i> = il meteo in TV; frase utile per la parte 6.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Chi sarà? L'insegnante mostra la foto di una persona sconosciuta (da una rivista o dal telefono). Fate ipotesi: chi sarà? Quanti anni avrà? Dove sarà? Che lavoro farà? Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Mah… · Secondo me… · Sarà… · Avrà… · Forse… · Probabilmente… · Ci saranno… gradi · Sarà in vacanza · Avrà caldo · Non lo so, ma…</div>
{sub("B", "Il clima che cambia. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Com'è l'estate nella tua città? Quanti gradi ci sono?</li><li>Che cosa fai per stare fresco o fresca?</li><li>Secondo te, come sarà il clima fra trent'anni?</li><li>Che cosa farai se quest'estate farà molto caldo?</li><li>Che cosa possiamo fare per l'ambiente (alberi, bici, aria condizionata)?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: va bene anche una foto di una via o di una casa: <i>dove sarà? quanto costerà?</i> Pretendere il futuro, non <i>deve essere</i>.</li>
<li>B: domande 3–4: futuro vero e <i>se + futuro</i>. Collegare la domanda 5 al giardino in Bolognina di Marco e Júlia (alberi = ombra).</li></ol>""")

    # Page 8
    pc = [("A2 · 21", "So usare prima di + infinito."), ("A2 · 22", "So parlare del caldo, del tempo e del clima."),
          ("A2 · 22", "So fare una supposizione con il futuro (sarà, avrà)."), ("A2 · 22", "So fare un'ipotesi con se + futuro."),
          ("A2 · 22", "So dare consigli per l'estate.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Esserà al cinema.", "Sarà al cinema."), ("Mah… saranno trentacinque gradi.", "✓"),
          ("Averà sonno.", "Avrà sonno."), ("Quanti gradi saranno qui?", "Quanti gradi ci saranno qui?"),
          ("Oggi fa molto calore.", "Oggi fa molto caldo."), ("Se domani pioverà, resteremo a casa.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. L'estate nella mia città (50–75 parole).</b> Com'è il tempo d'estate? Che cosa fa la gente quando fa caldo? Come sarà il clima fra dieci anni? Che cosa farai se quest'estate farà molto caldo? Usa almeno tre verbi al futuro e una frase con <i>se</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il testo; l'insegnante chiede <i>Quanti gradi ci saranno adesso a Bologna?</i> Unità 23: <i>Che bello!</i> (che…!, quanto…!, bello / buono).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("22.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("22.2", "Ascolta e ripeti")}
<p>{" · ".join(S222)}</p>
{sub("22.3", "Futuro o supposizione?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S223))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 22 - Che caldo!")
