# Speak! Ponte A2 - Unità 34 "Che cosa ne pensi?" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 34", audio_json=os.path.join(HERE, "audio_it-a2-unita-34.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la discussione", "discussione"), ("B", "il pollice alzato", "pollice"), ("C", "i pro e i contro", "pro e contro"), ("D", "la feijoada", "feijoada"),
          ("E", "la tapioca", "tapioca"), ("F", "la lavagna", "lavagna"), ("G", "il voto", "voto"), ("H", "i manifesti", "manifesti")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-34"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["34.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S342 = [x.split(": ", 1)[1] for x in _r["34.2 Ripeti"].split("\n")]
S343 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["34.3 D'accordo o no"].split("\n")]


def _key(w):
    if w.startswith("l'"):
        return w[2:].lower()
    a, _, rest = w.partition(" ")
    return (rest if a in ("la", "il", "i", "gli", "lo", "le") else w).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 34", "Che cosa ne pensi?", "Opinioni e discussioni · <b>che ne pensi? · penso di · penso che · sono d'accordo</b>",
                       [("SAI FARE", "chiedere e dare un'opinione, essere d'accordo o no, discutere una proposta, dire che cosa pensi di fare"),
                        ("LINGUA", "Che ne pensate? · Penso che sia un'idea fantastica. · Penso di farla con Camila. · Non sono d'accordo con te. · Non ne so niente."),
                        ("PRONUNCIA", "la voce dell'opinione: Mah… · Secondo me…")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: idee e opinioni", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Ti piace discutere? Con chi discuti di più?</li><li>Conosci un piatto brasiliano che piacerebbe agli italiani?</li><li>Nella tua città ci sono serate a tema (musica, cucina di un Paese…)?</li></ol>""",
    28, """<ol><li>A: <i>i pro e i contro</i> = i vantaggi e gli svantaggi; <i>la lavagna</i> = qui, la lavagna del bar con il menù; <i>i manifesti</i> = i poster sui muri.</li>
<li>B: domanda 2: anticipare <i>secondo me</i> + indicativo e <i>penso che</i> + congiuntivo.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: idee, cibo, opinioni</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>L'idea di Giulia · la signora Rossi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Che ne pensi? · penso di / penso che · accordo</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Le opinioni · ne e ci</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>La voce dell'opinione · d'accordo o no?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Ne o ci? · penso di o penso che? · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Il dibattito · opinioni personali</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Metà novembre. Giulia pensa di fare al bar un <b>venerdì brasiliano</b> una volta al mese: <i>Che ne pensate?</i> Davide è entusiasta (<i>penso che sia un'idea fantastica</i>); Marco non è sicuro (<i>ai bolognesi piacciono i tortellini</i>); Júlia non è d'accordo con lui: a Bologna ci sono tantissimi studenti stranieri. Júlia pensa di cucinare la feijoada con Camila (unità 30), che fa la tapioca. Il giorno dopo la signora Rossi: <i>Ne parla tutto il palazzo!</i> Della cucina brasiliana <i>non ne so niente</i>, ma la feijoada la assaggia: <i>ne prendo solo un po'</i>. Il primo venerdì brasiliano è nell'unità 35.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il brasiliano traduce <i>o que você acha disso?</i> con <i>che pensi di questo?</i>: insegnare il blocco <i>Che ne pensi?</i>. <i>Acho que é</i> diventa <i>penso che è</i> (serve il congiuntivo, oppure <i>secondo me è</i>). <i>Pensar em</i> = <i>pensare a</i> → <i>ci penso</i> (rifletto), non <i>ne penso</i>. <i>Concordo com você</i> → <i>sono d'accordo con te</i> (anche <i>concordo</i> è corretto).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia la discussione è quasi uno sport: al bar si parla di calcio, di politica e soprattutto di cibo. Sul cibo gli italiani hanno opinioni fortissime (la pasta con il pollo, l'ananas sulla pizza…), ma le città universitarie come Bologna hanno sempre più ristoranti e serate di cucina straniera.</div>
<div class="box"><h4>AUDIO</h4>Traccia 34.1 I due dialoghi (lento e naturale) · Traccia 34.2 Ascolta e ripeti · Traccia 34.3 D'accordo o no?</div>""")

    # Page 2
    who = [("Pensa che sia un'idea fantastica.", "Davide"), ("Pensa che sia rischioso.", "Marco"), ("Non è d'accordo con Marco.", "Júlia"),
           ("Fa la tapioca.", "Camila"), ("Vuole assaggiare tutto prima.", "Marco")]
    wl = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:30mm')}</td></tr>" for a, x in who)
    vf = [("Tutto il palazzo parla del venerdì brasiliano.", "V"), ("La signora Rossi conosce bene la cucina brasiliana.", "F"),
          ("La signora Rossi pensa che sia una bella cosa per il quartiere.", "V"), ("La feijoada è un piatto leggero.", "F"), ("La signora Rossi vuole il caffè brasiliano.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: il venerdì brasiliano", "10 min")}
{audiocard(["34.1 · SLOW", "34.1 · NATURAL"])}
{sub("A", "Prima parte. Al bar. Chi lo dice o lo fa? Davide, Marco, Júlia o Camila?", "4 min", "34.1 · SLOW")}
<table style="margin:0;width:94%">{wl}</table>
{sub("B", "Seconda parte. Sulle scale. Vero (V) o falso (F)?", "4 min", "34.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa pensa di fare Giulia? Ogni quanto?", "2 min")}
<div class="wline">{R("Pensa di fare un venerdì brasiliano al bar, una volta al mese.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Ogni personaggio ha un'opinione diversa: chiedere allo studente con chi è d'accordo.</li>
<li>B: frase 2: <i>non ne so niente</i>. Frase 4: <i>un piatto un po' pesante</i>.</li></ol>""")

    # Page 3
    rules = [("<i>Che <b>ne</b> pensate?</i> <i>Ne</i> vuol dire", ["di questo", "a questo"], "di questo"),
             ("<i>Penso che <b>sia</b> un'idea fantastica.</i> Dopo <i>penso che</i>:", ["congiuntivo", "indicativo"], "congiuntivo"),
             ("<i>Secondo me <b>è</b> rischioso.</i> Dopo <i>secondo me</i>:", ["indicativo", "congiuntivo"], "indicativo"),
             ("<i>Penso <b>di farla</b> con Camila.</i> (io penso, io faccio) Si usa", ["di + infinito", "che + congiuntivo"], "di + infinito"),
             ("<i>Non sono d'accordo ___ te.</i>", ["con", "a"], "con"),
             ("<i>Vieni? — <b>Ci</b> penso.</i> <i>Ci penso</i> vuol dire", ["rifletto, decido dopo", "la mia opinione è"], "rifletto, decido dopo")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Che", ["ne", "lo"], "ne", "pensi del film?"), ("Penso", ["di andare", "che vado"], "di andare", "al mare domenica."),
          ("Secondo me Giulia", ["ha", "abbia"], "ha", "ragione."), ("Non", ["ne", "ci"], "ne", "so niente.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: che ne pensi?", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Che ne pensate?</b> · E Lei <b>che ne pensa</b>, signora? · <b>Ne</b> parliamo domani. · Non <b>ne</b> so niente.<br>
2. <b>Penso che sia</b> un'idea fantastica. · <b>Credo che sia</b> una bella cosa. · <b>Secondo me è</b> rischioso. · <b>Penso di fare</b> un venerdì brasiliano.<br>
3. <b>Non sono d'accordo con te.</b> · <b>Avete ragione voi.</b> · Siamo tutti <b>d'accordo</b>. · Mah, io <b>non sono sicuro</b>. · <b>Ci penso.</b></div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Chiedere: <b>Che ne pensi?</b> (<i>ne</i> = di questo). Rispondere: <b>secondo me</b> + indicativo · <b>penso che / credo che</b> + congiuntivo · <b>penso di</b> + infinito (stesso soggetto o intenzione). Accordo: <b>sono d'accordo con te, hai ragione</b> · <b>non sono d'accordo, io la penso diversamente</b>. <b>Ci penso</b> = ci rifletto (<i>pensare a</i>). Tutto: pagina 4.</div>""",
    22, """<ol><li>A: il congiuntivo dopo <i>penso che</i> è dell'unità 09 e 29: qui basta <i>sia</i>; per gli altri verbi lo studente può usare <i>secondo me</i>.</li>
<li>B: frase 6: <i>Ci penso</i> è anche un modo gentile di dire «forse no».</li></ol>""")

    grammar_ref_it.opinioni_ne(b)

    # Page 5
    opts3 = [["d'accordo", "non d'accordo"]] * 6
    ans3 = ["d'accordo", "non d'accordo", "d'accordo", "non d'accordo", "d'accordo", "non d'accordo"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Penso che è una buona idea.</td><td><b>Penso che sia una buona idea.</b></td><td>Congiuntivo.</td></tr>
<tr><td>Penso che faccio una festa.</td><td><b>Penso di fare una festa.</b></td><td>Stesso soggetto: <i>di</i>.</td></tr>
<tr><td>Sono d'accordo a te.</td><td><b>Sono d'accordo con te.</b></td><td><i>D'accordo con</i>.</td></tr>
<tr><td>Che pensi di questo?</td><td><b>Che ne pensi?</b></td><td><i>Ne</i> = di questo.</td></tr>
<tr><td>Vieni? — Non so, ne penso.</td><td><b>Non so, ci penso.</b></td><td><i>Pensare a</i> → <i>ci</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["34.2", "34.3"])}
{sub("A", "Ascolta e ripeti. Quando diamo un'opinione, la voce si ferma un attimo prima: Mah… · Secondo me… · Penso che…", "2 min", "34.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S342)}</div>
{sub("B", "D'accordo o no? Ascolta e scegli.", "2 min", "34.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: riga 4: <i>Che pensi di questo?</i> si capisce, ma un italiano dice <i>Che ne pensi?</i>.</li>
<li>4A: <i>Mah…</i> e <i>Beh…</i> danno tempo per pensare e rendono l'opinione più gentile.</li>
<li>4B: 1 Sono d'accordo · 2 Non è vero · 3 Hai ragione · 4 Per niente d'accordo · 5 Esatto · 6 La penso diversamente.</li></ol>""")

    # Page 6
    nc = [("Che ___ pensi della mia idea?", "ne"), ("Vieni alla festa? — Non so, ___ penso.", "ci"), ("Il concerto? Tutti ___ parlano.", "ne"),
          ("Pensi ancora all'esame? — Sì, ___ penso sempre.", "ci"), ("Sai qualcosa di calcio? — No, non ___ so niente.", "ne")]
    ncl = "".join(f"<li>{s.split('___')[0]}{A(r, 'min-width:12mm')}{s.split('___')[1]}</li>" for s, r in nc)
    pd = [("(io) fare una festa sabato", "Penso di fare una festa sabato."), ("(tu) avere ragione", "Penso che tu abbia ragione."),
          ("(io) cambiare lavoro", "Penso di cambiare lavoro."), ("(il bar) essere troppo piccolo", "Penso che il bar sia troppo piccolo.")]
    pdl = "".join(f"<li>Penso… {q}<div class='wline'>{R(a)}</div></li>" for q, a in pd)
    wb = [("discutere", "la discussione"), ("proporre", "la proposta"), ("decidere", "la decisione"), ("scegliere", "la scelta")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Ne o ci?", "3 min")}
<ol style="line-height:1.7">{ncl}</ol>
{sub("B", "Penso di o penso che? Scrivi la frase.", "4 min")}
<ol style="line-height:1.4">{pdl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: <i>parlare di, sapere di, pensare di</i> (opinione) → <i>ne</i>; <i>pensare a</i> → <i>ci</i>.</li>
<li>B: frase 2: <i>tu abbia</i>: con il congiuntivo singolare si mette il soggetto.</li>
<li>C: <i>Che ne pensi della proposta di Giulia? È una buona scelta?</i></li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Il dibattito. Leggi le proposte. Per ognuna l'insegnante chiede «Che ne pensi?»: dai la tua opinione e spiega perché. L'insegnante a volte è d'accordo, a volte no: difendi la tua idea!", "6 min")}
<ol style="line-height:1.5;margin-top:1mm"><li>La domenica il centro della città è chiuso alle macchine.</li><li>Tutti possono lavorare da casa due giorni alla settimana.</li><li>Nelle scuole niente compiti per il fine settimana.</li><li>Un «venerdì brasiliano» in un bar della tua città.</li></ol>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Che ne pensi? · Secondo me… · Penso che sia… · Sono d'accordo con te. · Hai ragione, ma… · Non sono d'accordo. · Io la penso diversamente. · Mah, dipende. · I pro e i contro.</div>
{sub("B", "Opinioni personali. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.5"><li>A chi chiedi un'opinione prima di una decisione importante?</li><li>Cambi facilmente idea?</li><li>Che ne pensi della cucina italiana fuori dall'Italia?</li><li>Che piatto brasiliano faresti assaggiare alla signora Rossi?</li></ol>""",
    22, """<ol><li>A: l'insegnante prende sempre la posizione contraria (anche se non la pensa così) per far discutere lo studente.</li>
<li>B: domanda 4: <i>faresti</i> = condizionale (unità 05).</li></ol>""")

    # Page 8
    pc = [("A2 · 33", "So usare i verbi reciproci e mentre / quando."), ("A2 · 34", "So chiedere un'opinione (Che ne pensi?)."),
          ("A2 · 34", "So usare penso di e penso che."), ("A2 · 34", "So dire se sono d'accordo o no."),
          ("A2 · 34", "So usare ne = di questo e ci penso.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Penso che è una buona idea.", "Penso che sia una buona idea."), ("Che ne pensi?", "✓"),
          ("Penso che faccio una festa.", "Penso di fare una festa."), ("Sono d'accordo a te.", "Sono d'accordo con te."),
          ("Vieni? — Non so, ne penso.", "Non so, ci penso."), ("Non ne so niente.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. La mia opinione (50–75 parole).</b> Scrivi a Giulia che cosa pensi del venerdì brasiliano: sei d'accordo? Quali sono i pro e i contro? Che piatto pensi di proporre? Usa <i>secondo me, penso che, penso di</i> e <i>sono d'accordo / non sono d'accordo</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il messaggio; l'insegnante risponde come Giulia (<i>Che bella idea! Ci penso.</i>). Unità 35: <i>Due anni a Bologna</i> (fine della storia A2: tutti i tempi insieme).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("34.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("34.2", "Ascolta e ripeti")}
<p>{" · ".join(S342)}</p>
{sub("34.3", "D'accordo o no?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S343))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 34 - Che cosa ne pensi?")
