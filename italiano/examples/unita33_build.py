# Speak! Essenziale A1 - Unità 33 "Al cinema" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from programma import programma
setup(band="A1 · UNITÀ 33", audio_json=os.path.join(HERE, "audio_it-a1-unita-33.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il cinema", "cinema"), ("B", "il biglietto", "biglietto"), ("C", "i popcorn", "popcorn"), ("D", "lo schermo", "schermo"),
          ("E", "la sala", "sala"), ("F", "lo spettatore", "spettatore"), ("G", "la pizza", "pizza"), ("H", "la locandina", "locandina")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-33"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["33.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S332 = [x.split(": ", 1)[1] for x in _r["33.2 Ripeti"].split("\n")]
S333 = [x.split(": ", 1)[1] for x in _r["33.3 Li o gli"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split()[-1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 33", "Al cinema", "Bruno e Chiara · <b>i generi di film · mi è piaciuto, mi è piaciuta, mi sono piaciuti…</b>",
                       [("SAI FARE", "scegliere un film, comprare i biglietti e dire che cosa ti è piaciuto e che cosa no"),
                        ("LINGUA", "È una commedia · A che ora comincia? · Ti è piaciuto il film? · Mi sono piaciute le scene al parco"),
                        ("PRONUNCIA", "il suono gli: figlio, voglio, biglietto")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: andiamo al cinema?", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Vai spesso al cinema? Con chi?</li><li>Preferisci vedere i film al cinema o a casa?</li><li>Che tipo di film ti piace: commedie, film d'azione, gialli…?</li></ol>""",
    22, """<ol><li>A: <i>i popcorn</i> non cambia al plurale. <i>La locandina</i> = il poster del film. <i>Lo spettatore</i> = la persona che guarda il film (e ha paura!).</li>
<li>B: preparare i generi del dialogo: <i>commedia, horror, giallo, film di fantascienza</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il cinema</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il programma del cinema · in pizzeria · Bruno racconta a Júlia</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>piacere al passato: mi è piaciuto/a, mi sono piaciuti/e</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Il suono gli · li o gli?</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>I generi di film · la mia serata</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Alla cassa · che cosa ti è piaciuto?</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Chiara, la ragazza di Bruno (unità 20: bassa, capelli lunghi e rossi, timida, studia medicina), parla per la prima volta. Venerdì sera i due vanno al cinema Due Torri: niente horror («Non mi piacciono!»), Chiara sceglie la commedia <i>Il cane di Marta</i> alle 19.30 perché vuole ridere dopo una settimana di studio. Biglietti ridotti per studenti: 6 euro l'uno, sala tre, e i popcorn. In pizzeria commentano: il film è piaciuto a tutti e due, ma la fine no. Sabato Bruno racconta tutto a Júlia: sabato prossimo porta Chiara a cena da Marco, che non la conosce (unità 27).</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese <i>eu gostei do filme</i>: la persona è il soggetto. In italiano il soggetto è la cosa: <b>il film mi è piaciuto</b>. Per questo il verbo cambia con la cosa: <b>mi è piaciuta</b> la commedia, <b>mi sono piaciuti</b> gli attori, <b>mi sono piaciute</b> le scene. Non si dice <i>ho piaciuto</i>: il passato prossimo di <i>piacere</i> vuole <b>essere</b>. Il suono <b>gli</b> è come il <i>lh</i> di <i>filho</i>: <i>figlio</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia molti film stranieri sono <b>doppiati</b> in italiano: il doppiaggio italiano è famoso. Nelle grandi città alcuni cinema hanno spettacoli in <b>versione originale</b> con i sottotitoli (V.O.). Molti cinema fanno prezzi <b>ridotti</b> per studenti e in alcuni giorni della settimana. In estate ci sono i <b>cinema all'aperto</b>, per esempio in Piazza Maggiore a Bologna.</div>
<div class="box"><h4>AUDIO</h4>Traccia 33.1 Tre dialoghi (lento e naturale) · Traccia 33.2 Ascolta e ripeti · Traccia 33.3 Li o gli?</div>""")

    # Page 2
    vf = [("A Chiara è piaciuto molto il film.", "V"), ("A Bruno non è piaciuta la protagonista.", "F"),
          ("A tutti e due non è piaciuta la fine.", "V"), ("A Bruno sono piaciuti i popcorn.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: che cosa vediamo?", "10 min")}
<p>Bruno e Chiara vanno al cinema, poi in pizzeria. Il giorno dopo Bruno racconta la serata a Júlia.</p>
{audiocard(["33.1 · SLOW", "33.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e scrivi il genere di ogni film e il prezzo per gli studenti.", "5 min", "33.1 · SLOW")}
{programma(T)}
<p style="margin:1.5mm 0 0">Quale film scelgono? {A("Il cane di Marta", "min-width:36mm")} &nbsp; A che ora? {A("alle 19.30", "min-width:22mm")} &nbsp; Sala: {A("3", "min-width:10mm")}</p>
{sub("B", "Dialogo 2. Vero (V) o falso (F)?", "3 min", "33.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. Che cosa fa Bruno sabato prossimo?", "2 min")}
<div class="wline">{R("Porta Chiara a cena da Marco.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>, anche due volte. Perché la commedia? Chiara vuole ridere: questa settimana ha studiato tanto.</li>
<li>B: versione <b>naturale</b>. 2: la protagonista gli è piaciuta <b>molto</b>. 4: i popcorn sono troppo dolci (ma Chiara li ha mangiati tutti!).</li></ol>""")

    # Page 3
    tb = [("il film (m. sing.)", "Mi <b>è piaciuto</b> il film."), ("la commedia (f. sing.)", "Mi <b>è piaciuta</b> la commedia."),
          ("gli attori (m. plur.)", "Mi <b>sono piaciuti</b> gli attori."), ("le scene (f. plur.)", "Mi <b>sono piaciute</b> le scene."),
          ("+ infinito", "Mi <b>è piaciuto</b> ballare.")]
    tbr = "".join(f"<tr><td style='width:46mm'>{a}</td><td>{x}</td></tr>" for a, x in tb)
    ck = [("Ti ", ["è piaciuto", "è piaciuta"], "è piaciuta", " la pizza?"), ("Mi ", ["è piaciuto", "sono piaciuti"], "sono piaciuti", " i popcorn."),
          ("Non mi ", ["è piaciuta", "sono piaciute"], "sono piaciute", " le canzoni del film."), ("A Chiara ", ["è piaciuto", "ha piaciuto"], "è piaciuto", " il film.")]
    ckl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in ck)
    pr = [("Ti", "è piaciuto", "il concerto?"), ("Mi", "sono piaciute", "le foto di Venezia."), ("Non mi", "è piaciuta", "la fine del film."),
          ("Ci", "sono piaciuti", "i tortellini."), ("Le", "è piaciuto", "cucinare con noi, signora?")]
    prl = "".join(f"<li>{s} {A(v, 'min-width:28mm')} {z}</li>" for s, v, z in pr)
    b.page(f"""{sec(3, "Grammatica: piacere al passato", "10 min")}
{sub("A", "Leggi la spiegazione.", "4 min")}
<table style="margin:0"><tr><th>Che cosa?</th><th>piacere al passato prossimo</th></tr>{tbr}</table>
<div class="box sand" style="margin-top:1.5mm"><h4>REGOLA</h4>Presente: <i>mi piace</i> + una cosa, <i>mi piacciono</i> + più cose. Passato: <b>essere</b> + <b>piaciuto</b>, che cambia come la cosa: <b>-o, -a, -i, -e</b>. La persona va prima: <b>mi, ti, gli</b> (a lui), <b>le</b> (a lei), <b>Le</b> (formale), <b>ci, vi, gli</b> (a loro) · <i>a Bruno è piaciuto, a Chiara è piaciuto</i>. Negativo: <b>non</b> + mi: <i>Non mi è piaciuta la fine.</i></div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "Completa con è piaciuto/a o sono piaciuti/e.", "4 min")}
<ol>{prl}</ol>""",
    24, """<ol><li>A: far trovare nei dialoghi tutte le forme: <i>ti è piaciuto il film, mi è piaciuta la protagonista, mi sono piaciute le scene, ti sono piaciuti i popcorn</i>.</li>
<li>B: 4 <i>ha piaciuto</i> non esiste. In C, <i>ci</i> = a noi; nella 5, <i>Le</i> = a Lei (formale).</li></ol>""")

    # Page 4
    dl = [f'<li value="{i+1}">{A(x, "min-width:14mm")}</li>' for i, x in enumerate(["gli", "li", "gli", "li", "gli", "li"])]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho piaciuto il film.</td><td><b>Mi è piaciuto il film.</b></td><td>Il soggetto è il film.</td></tr>
<tr><td>Mi è piaciuto la commedia.</td><td><b>Mi è piaciuta la commedia.</b></td><td><i>commedia</i> è femminile.</td></tr>
<tr><td>Mi è piaciuto gli attori.</td><td><b>Mi sono piaciuti gli attori.</b></td><td>Plurale: <i>sono piaciuti</i>.</td></tr>
<tr><td>Io non mi è piaciuto.</td><td><b>A me non è piaciuto.</b> / <b>Non mi è piaciuto.</b></td><td>Senza <i>io</i>.</td></tr>
<tr><td>Ho visto un film de terrore.</td><td><b>Ho visto un horror.</b></td><td><i>un film horror</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["33.2", "33.3"])}
{sub("A", "Ascolta e ripeti. gli si pronuncia come lh in portoghese: figlio, famiglia.", "2 min", "33.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S332)}</div>
{sub("B", "Li o gli? Ascolta e scrivi.", "3 min", "33.3")}
{twocol(dl, 4)}""",
    34, """<ol><li>Errori: <i>gostar</i> e <i>piacere</i> funzionano in modo diverso: far girare la frase (<i>il film mi è piaciuto</i>).</li>
<li>4B: 1 bi<b>gli</b>etto · 2 Ita<b>li</b>a · 3 fami<b>gli</b>a · 4 o<b>li</b>o · 5 vo<b>gli</b>o · 6 Giu<b>li</b>a. Attenzione: Ita<b>li</b>a non è <i>Itaglia</i>!</li></ol>""")

    # Page 5
    gen = [("Ridi dall'inizio alla fine.", "una commedia"), ("C'è un detective e un mistero.", "un giallo"), ("Hai paura e non dormi la notte.", "un horror"),
           ("Ci sono astronavi e altri pianeti.", "un film di fantascienza"), ("Due persone si innamorano.", "un film romantico"),
           ("È per bambini, con i disegni.", "un cartone animato")]
    gl = "".join(f"<li>{s} → {A(g, 'min-width:42mm')}</li>" for s, g in gen)
    bank = " &nbsp;·&nbsp; ".join(sorted(g for _, g in gen))
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Che genere è? Leggi e scrivi.", "3 min")}
<div class="bank">{bank}</div>
<ol style="line-height:1.75">{gl}</ol>
{sub("B", "Il mio ultimo film (o la mia ultima serie). Scrivi tre cose che ti sono piaciute e una cosa che non ti è piaciuta.", "5 min")}
<div class="wline">{R("Ho visto… Mi è piaciuto/a… Mi sono piaciuti/e… Non mi è piaciuto/a…")}</div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: aggiungere altri generi se gli studenti li chiedono: <i>film d'azione, documentario, dramma, film d'animazione</i>.</li>
<li>B: correggere l'accordo di <i>piaciuto</i> con la cosa.</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Alla cassa. Guarda il programma a pagina 2. Decidi con l'insegnante che film vedere e a che ora. Poi compra i biglietti (l'insegnante è il cassiere).", "5 min")}
<div class="box" style="font-size:9pt"><h4>PAROLE UTILI</h4>Che cosa vediamo? · C'è… · È una commedia / un giallo… · A che ora comincia? · Gli horror non mi piacciono. · Due biglietti per…, per favore. · Siamo studenti. · Quanto costa? · In che sala?</div>
{sub("B", "Che cosa ti è piaciuto? Fai domande all'insegnante sul suo fine settimana, sull'ultimo viaggio o sull'ultima festa: Ti è piaciuto…? Ti sono piaciuti…?", "4 min")}
<div class="wline"></div>
{sub("C", "La critica del film. Racconta un film che hai visto: che genere è, ti è piaciuto o no, perché?", "3 min")}""",
    24, """<ol><li>A: alla fine cambiare ruoli: lo studente fa il cassiere e dice prezzo e sala.</li>
<li>B: rispondere usando molte forme diverse (<i>mi è piaciuta la città, mi sono piaciuti i musei…</i>).</li></ol>""")

    # Page 7
    pc = [("Unità 32", "So chiedere quale autobus prendere e spiegare un percorso."), ("Unità 33", "So dire i generi di film e scegliere un film."),
          ("Unità 33", "So comprare i biglietti del cinema."), ("Unità 33", "So dire che cosa mi è piaciuto e che cosa no."),
          ("Unità 33", "So pronunciare il suono gli.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ho piaciuto la festa.", "Mi è piaciuta la festa."), ("Mi è piaciuto le canzoni.", "Mi sono piaciute le canzoni."),
          ("Ti è piaciuta i dolci?", "Ti sono piaciuti i dolci?"), ("A Marco non ha piaciuto il vino.", "A Marco non è piaciuto il vino."),
          ("Mi è piaciuto la città.", "Mi è piaciuta la città."), ("Mi sono piaciuti i film italiani.", "✓ corretta")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> Una frase è corretta.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La mia serata.</b> Scrivi un messaggio a un amico su una serata (cinema, concerto, cena): dove sei andato/a, con chi, che cosa ti è piaciuto e che cosa no.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il messaggio; i compagni chiedono <i>Ti è piaciuto…?</i> Unità 34: <i>Al mercatino</i> (questo / quello, i colori, fa uno sconto?).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("33.1", "Al cinema (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("33.2", "Ascolta e ripeti")}
<p>{" · ".join(S332)}</p>
{sub("33.3", "Li o gli?")}
<p>{" · ".join(S333)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 33 - Al cinema")
