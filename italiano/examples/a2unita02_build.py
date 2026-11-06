# Speak! Ponte A2 - Unità 02 "Da bambina…" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 02", audio_json=os.path.join(HERE, "audio_it-a2-unita-02.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'album di foto", "album"), ("B", "la bicicletta", "bicicletta"), ("C", "la bambola", "bambola"), ("D", "il pallone", "pallone"),
          ("E", "il giardino", "giardino"), ("F", "la spiaggia", "spiaggia"), ("G", "il televisore", "televisore"), ("H", "la lavagna", "lavagna")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-02"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["02.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S022 = [x.split(": ", 1)[1] for x in _r["02.2 Ripeti accento imperfetto"].split("\n")]
S023 = [x.split(": ", 1)[1] for x in _r["02.3 Ripeti frasi"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 02", "Da bambina…", "Ricordi d'infanzia · <b>l'imperfetto</b>",
                       [("SAI FARE", "raccontare com'era la tua infanzia e che cosa facevi di solito"),
                        ("LINGUA", "Quando ero piccola, abitavo a Belo Horizonte. · Ogni domenica andavamo dal nonno. · C'erano poche macchine."),
                        ("PRONUNCIA", "l'accento dell'imperfetto: parlavo, parlavamo, parlavano")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: le cose dell'infanzia", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1].split("'")[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante. Quali cose ricordi della tua infanzia?", "4 min")}
<ol><li>Quale di queste cose c'era nella tua casa? Quale non c'era?</li><li>Hai ancora un album di foto di quando eri piccolo/a? Dov'è?</li><li>Qual è il tuo primo ricordo?</li></ol>""",
    22, """<ol><li>A: <i>il televisore</i> = l'apparecchio; <i>la televisione</i> = il mezzo (guardare la televisione). <i>Il pallone</i> = la palla grande del calcio.</li>
<li>B: lo studente può rispondere al presente o come riesce: l'imperfetto arriva a pagina 3. Annotare i verbi che usa per riprenderli dopo.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: le cose dell'infanzia · il primo ricordo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>L'album di Júlia · Bologna negli anni Settanta · che cosa volevate fare?</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>L'imperfetto: forma regolare, essere, fare · abitudini e descrizioni</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>L'imperfetto: forma, irregolari, usi, primo contrasto con il passato prossimo</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'accento dell'imperfetto · frasi dei ricordi</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Il racconto della signora Rossi · Bologna allora e oggi · parole dell'infanzia</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Intervista sull'infanzia · una foto di quando eri piccolo/a</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Una domenica di ottobre la madre di Júlia le ha mandato dal Brasile un vecchio album di foto. Júlia lo guarda con Marco: a sei anni era bionda, abitava in una casa con un grande giardino a Belo Horizonte e ogni domenica andava dal nonno Antonio (il nonno di Treviso dell'A1), che parlava in dialetto veneto e faceva la polenta. Arriva la signora Rossi: da bambina abitava proprio in via Santo Stefano, giocava in strada e d'estate andava a Rimini in treno; c'era un solo canale in televisione. Il giorno dopo, al bar, Júlia, Davide e Giulia raccontano che cosa volevano fare da grandi.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>L'uso è quasi uguale al portoghese (<i>eu morava, a gente brincava</i>), quindi il problema è la forma: <i>abitavamo</i> e non <i>abitávamos</i>; l'accento di <i>noi</i> e <i>voi</i> è su <b>-va-</b> (parla<u>va</u>mo), quello di <i>loro</i> torna indietro (<u>par</u>lavano). L'età si dice con <b>avere</b>: <i>avevo sei anni</i>, non <i>ero sei anni</i>. <i>C'era</i> + singolare, <b>c'erano</b> + plurale. Lo studente spesso usa il passato prossimo per le abitudini: <i>ho abitato a…</i></div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Negli anni Settanta in Italia molti bambini giocavano <b>in strada</b> o in cortile. La RAI aveva pochi canali, e quando c'era un programma famoso i vicini lo guardavano insieme. Per molte famiglie del Nord le vacanze erano al mare in <b>Romagna</b> (Rimini, Riccione), con l'ombrellone e la spiaggia attrezzata. Molti nonni parlavano il <b>dialetto</b> della loro regione più dell'italiano.</div>
<div class="box"><h4>AUDIO</h4>Traccia 02.1 Tre dialoghi (lento e naturale) · Traccia 02.2 L'accento dell'imperfetto · Traccia 02.3 Frasi dei ricordi</div>""")

    # Page 2
    tb = [("Dove abitava?", "in una casa con un grande giardino, a Belo Horizonte", "in via Santo Stefano, a Bologna"),
          ("Com'era? / Com'era la città?", "bionda, con i capelli lunghissimi; non era tranquilla", "diversa: pochi turisti, poche macchine"),
          ("Che cosa faceva di solito?", "giocava in giardino con Bruno e il cane; la domenica andava dal nonno", "giocava in strada; d'estate andava a Rimini in treno")]
    tbr = "".join(f"<tr><td style='width:38mm'><b>{q}</b></td><td>{A(a, 'min-width:58mm')}</td><td>{A(c, 'min-width:58mm')}</td></tr>" for q, a, c in tb)
    vf = [("Júlia aveva sei anni nella foto.", "V"), ("Il nonno Antonio faceva la pizza.", "F"), ("La signora Rossi abitava a Rimini.", "F"),
          ("Negli anni Settanta c'era un solo canale in televisione.", "V"), ("Davide era bravo in matematica.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    sogni = [("Júlia", "la cantante"), ("Davide", "il calciatore"), ("Giulia", "la maestra")]
    sl = " &nbsp; ".join(f"<b>{n}</b> voleva fare {A(x, 'min-width:24mm')}" for n, x in sogni)
    b.page(f"""{sec(2, "Ascolto: l'album di Júlia", "10 min")}
<p>La madre di Júlia le ha mandato un vecchio album di foto. Che cosa ricordano Júlia e la signora Rossi?</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Ascolta e completa la tabella.", "5 min", "02.1 · SLOW")}
<table style="margin:0"><tr><th></th><th>Júlia da bambina</th><th>la signora Rossi da bambina</th></tr>{tbr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "3 min", "02.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa volevano fare da grandi?", "2 min")}
<p style="line-height:2">{sl}</p>""",
    20, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi. Ricordare il nonno di Treviso (A1): per questo parlava veneto.</li>
<li>B: versione <b>naturale</b>. 2: faceva la <b>polenta</b>. 3: abitava in <b>via Santo Stefano</b>; a Rimini andava d'estate. C: <i>fare il / la</i> + professione.</li></ol>""")

    # Page 3
    rules = [("Queste frasi parlano", ["del presente", "del passato"], "del passato"),
             ("Le frasi 2, 4 e 5 raccontano", ["una cosa successa una volta", "una cosa che si faceva di solito"], "una cosa che si faceva di solito"),
             ("Le frasi 1, 3 e 6 descrivono", ["com'era una persona o un posto", "un fatto preciso"], "com'era una persona o un posto"),
             ("La forma di <i>io</i> finisce in", ["-vo", "-va"], "-vo"),
             ("Per l'età diciamo", ["ero sei anni", "avevo sei anni"], "avevo sei anni"),
             ("Con un plurale diciamo", ["c'era", "c'erano"], "c'erano")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    tv = [("io", "abit<b>avo</b>", "av<b>evo</b>", "dorm<b>ivo</b>", "<b>ero</b>", "<b>facevo</b>"),
          ("tu", "abit<b>avi</b>", "av<b>evi</b>", "dorm<b>ivi</b>", "<b>eri</b>", "<b>facevi</b>"),
          ("lui / lei / Lei", "abit<b>ava</b>", "av<b>eva</b>", "dorm<b>iva</b>", "<b>era</b>", "<b>faceva</b>"),
          ("noi", "abit<b>avamo</b>", "av<b>evamo</b>", "dorm<b>ivamo</b>", "<b>eravamo</b>", "<b>facevamo</b>"),
          ("voi", "abit<b>avate</b>", "av<b>evate</b>", "dorm<b>ivate</b>", "<b>eravate</b>", "<b>facevate</b>"),
          ("loro", "abit<b>avano</b>", "av<b>evano</b>", "dorm<b>ivano</b>", "<b>erano</b>", "<b>facevano</b>")]
    tvr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in tv)
    b.page(f"""{sec(3, "Grammatica: l'imperfetto", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Avevo</b> sei anni. <b>Ero</b> bionda. &nbsp; 2. Ogni domenica <b>andavamo</b> dal nonno.<br>
3. Il nonno <b>parlava</b> sempre in dialetto veneto. &nbsp; 4. Noi bambini <b>giocavamo</b> in strada fino a sera.<br>
5. D'estate <b>andavamo</b> al mare a Rimini. &nbsp; 6. Non <b>c'erano</b> tanti turisti e <b>c'era</b> solo un canale.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "4 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "La forma. Leggi la tabella ad alta voce e trova le forme dei dialoghi.", "4 min")}
<table style="margin:0;font-size:9pt"><tr><th style="width:28mm"></th><th>abitare</th><th>avere</th><th>dormire</th><th>essere</th><th>fare</th></tr>{tvr}</table>
<div class="box sand"><h4>REGOLA</h4><b>Imperfetto</b> = radice + <b>-avo / -evo / -ivo</b> (<i>abit-avo, av-evo, dorm-ivo</i>). Irregolari: <b>essere</b> (ero, eri, era…), <b>fare</b> (facevo), <b>bere</b> (bevevo), <b>dire</b> (dicevo). Si usa per le <b>abitudini</b> del passato (<i>sempre, di solito, ogni domenica, d'estate</i>) e per le <b>descrizioni</b> (<i>era, aveva, c'era</i>). Tutto sull'imperfetto: pagina 4.</div>""",
    20, """<ol><li>B: <i>Quante volte andavano dal nonno?</i> Ogni domenica = abitudine. L'età con <b>avere</b>.</li>
<li>C: insistere sull'accento: <u>e</u>rano, fa<u>ce</u>vano.</li></ol>""")

    grammar_ref_it.imperfetto(b)

    # Page 5
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Da bambina ho abitato a Belo Horizonte.</td><td><b>Da bambina abitavo a Belo Horizonte.</b></td><td>Descrizione del passato: imperfetto.</td></tr>
<tr><td>Ero sei anni.</td><td><b>Avevo sei anni.</b></td><td>L'età: <i>avere</i>.</td></tr>
<tr><td>Noi abitávamos qui.</td><td><b>Noi abitavamo qui.</b></td><td>Italiano: <i>-avamo</i>, senza <i>s</i>.</td></tr>
<tr><td>C'era molte macchine.</td><td><b>C'erano molte macchine.</b></td><td>Plurale: <i>c'erano</i>.</td></tr>
<tr><td>Il nonno fava la polenta.</td><td><b>Il nonno faceva la polenta.</b></td><td><i>fare → facevo, faceva</i>.</td></tr>
<tr><td>Ogni domenica siamo andati dal nonno.</td><td><b>Ogni domenica andavamo dal nonno.</b></td><td>Abitudine: imperfetto.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["02.2", "02.3"])}
{sub("A", "L'accento dell'imperfetto. Ascolta e ripeti. Attenzione: parlaVAmo, parlaVAte, ma PARlavano.", "2 min", "02.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S022)}</div>
{sub("B", "Frasi dei ricordi. Ascolta e ripeti. Poi cambia una parola e di' una frase vera per te.", "2 min", "02.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S023)}</div>""",
    30, """<ol><li>Errori: l'ultimo è il più frequente anche ad A2: <i>ogni domenica, sempre, di solito</i> = segnali dell'imperfetto.</li>
<li>4A: con <i>loro</i> l'accento va sulla quartultima sillaba: <u>par</u>lavano, a<u>bi</u>tavano, <u>e</u>rano. 4B: esempio: <i>Quando ero piccolo, abitavo a Recife.</i></li></ol>""")

    # Page 6
    racc = [("Quando ero bambina, ", "abitavo", " (abitare) in via Santo Stefano."), ("Non ", "c'erano", " (esserci) tante macchine,"),
            ("così noi bambini ", "giocavamo", " (giocare) in strada fino a sera."), ("Non ", "avevamo", " (avere) molti giocattoli, ma eravamo felici."),
            ("D'estate ", "andavamo", " (andare) a Rimini in treno e mia madre"), ("", "preparava", " (preparare) i panini per tutti."),
            ("La sera i vicini ", "venivano", " (venire) a casa nostra a guardare la televisione:"), ("", "eravamo", " (essere) in quindici in salotto!")]
    rl2 = "".join(f"{a}{A(x, 'min-width:22mm')}{z} " for a, x, z in racc)
    oggi = [("le macchine", "poche", "tante"), ("i turisti", "pochi", "moltissimi"), ("il telefono", "uno in casa", "il cellulare per tutti"),
            ("i bambini", "giocavano in strada", "giocano al parco o a casa"), ("la televisione", "un canale", "centinaia di canali")]
    og = "".join(f"<tr><td><b>{a}</b></td><td>{x}</td><td>{y}</td></tr>" for a, x, y in oggi)
    ex = [("Nel 1975 c'erano poche macchine. Oggi ci sono tante macchine.",), ("Nel 1975 c'erano pochi turisti. Oggi ci sono moltissimi turisti.",),
          ("Nel 1975 c'era un telefono in casa. Oggi c'è un cellulare per tutti.",)]
    exl = "".join(f'<li><div class="wline">{R(e[0])}</div></li>' for e in ex[1:])
    wb = [("l'infanzia", "il periodo della vita quando siamo bambini"), ("il cortile", "lo spazio aperto dentro un palazzo"),
          ("nascondino", "il gioco: uno conta e gli altri si nascondono"), ("la maestra", "l'insegnante della scuola elementare"),
          ("la merenda", "il piccolo pasto del pomeriggio"), ("i giocattoli", "le cose per giocare: bambole, palloni…"),
          ("il dialetto", "la lingua locale di una città o di una regione"), ("da grande", "quando sarò adulto: «Che cosa vuoi fare…?»")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:19mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Il racconto della signora Rossi. Completa con l'imperfetto.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9.2pt;line-height:2.05">{rl2}</div>
{sub("B", "Bologna allora e oggi. Leggi la tabella e scrivi frasi come nell'esempio.", "3 min")}
<table style="margin:0;font-size:9pt"><tr><th style="width:32mm"></th><th>nel 1975</th><th>oggi</th></tr>{og}</table>
<p class="small" style="margin:.8mm 0 0"><b>Esempio:</b> <i>Nel 1975 c'erano poche macchine. Oggi ci sono tante macchine.</i></p>
<ol style="line-height:1.3">{exl}</ol>
{sub("C", "Parole dell'infanzia. Scrivi la parola giusta.", "3 min")}
<div class="bank">la maestra · i giocattoli · il cortile · da grande · il dialetto · l'infanzia · la merenda · nascondino</div>
{twocol(wbl, 4)}""",
    18, """<ol><li>A: <i>esserci</i> = c'è / ci sono → <i>c'era / c'erano</i>. B: frasi 4 e 5 a voce: <i>Nel 1975 i bambini giocavano in strada, oggi giocano al parco.</i></li>
<li>C: chiedere: <i>Che cosa mangiavi a merenda? Giocavi a nascondino?</i></li></ol>""")

    # Page 7
    iv = ["Dove abitavi? Com'era la tua casa?", "Con chi giocavi? Che giochi facevi?", "Com'era la tua scuola? E la tua maestra?", "Che cosa mangiavi a merenda?",
          "Dove andavi in vacanza?", "Che cosa volevi fare da grande?"]
    ivr = "".join(f"<tr><td>{q}</td><td></td><td></td></tr>" for q in iv)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Intervista sull'infanzia. Fai le domande all'insegnante e rispondi anche tu. Prendi appunti.", "6 min")}
<table style="margin:1mm 0 2mm"><tr><th>Quando eri piccolo/a…</th><th style="width:40mm">Io</th><th style="width:40mm">L'insegnante</th></tr>{ivr}</table>
{sub("B", "Una foto di quando eri piccolo/a. Pensa a una foto (o mostrala). Descrivila all'insegnante.", "4 min")}
<div class="box" style="font-size:9pt;margin-top:1mm"><h4>FRASI UTILI</h4>In questa foto avevo… anni. · Eravamo a… · C'era / c'erano… · Mi piaceva… · Di solito… · Ogni estate… · Mio nonno / mia nonna era… · Mi ricordo che…</div>
{sub("C", "Allora e oggi. Rispondi all'insegnante.", "2 min")}
<ol style="line-height:1.6"><li>La tua città è cambiata? Com'era quando eri bambino/a?</li><li>Che cosa facevi da bambino/a che oggi non fai più?</li></ol>""",
    24, """<ol><li>A: l'insegnante risponde con frasi semplici all'imperfetto, come modello. Correggere a fine attività, non durante.</li>
<li>B: se lo studente ha una foto sul telefono, è ancora meglio. C: <i>non… più</i> = un'abitudine finita: <i>Non gioco più a calcio.</i></li></ol>""")

    # Page 8
    pc = [("A2 · 01", "So comprare un vestito e usare mi, ti, gli, le."), ("A2 · 01", "So fare paragoni con più / meno … di."),
          ("A2 · 02", "So coniugare l'imperfetto (anche essere e fare)."), ("A2 · 02", "So raccontare che cosa facevo di solito da bambino/a."),
          ("A2 · 02", "So descrivere una persona o un posto del passato.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Da piccolo ho abitato in campagna.", "Da piccolo abitavo in campagna."), ("Quando ero bambina avevo un cane.", "✓"),
          ("Mia nonna era ottanta anni.", "Mia nonna aveva ottanta anni."), ("Nella mia scuola c'era due cortili.", "…c'erano due cortili."),
          ("Ogni estate andavamo al mare.", "✓"), ("Mio padre fava il pane la domenica.", "Mio padre faceva il pane…")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:44mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Quando ero piccolo/a… (50–75 parole).</b> Racconta la tua infanzia: dove abitavi, com'era la tua casa, che cosa facevi di solito con la tua famiglia e con gli amici, e che cosa volevi fare da grande.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il testo. Unità 03: <i>Che cosa è successo?</i> (imperfetto e passato prossimo insieme).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("02.1", "L'album di Júlia (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "L'accento dell'imperfetto")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "Frasi dei ricordi")}
<p>{" ".join(S023)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 02 - Da bambina")
