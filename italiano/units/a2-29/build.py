# Speak! Ponte A2 - Unità 29 "Il giardino è pronto" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 29", audio_json=os.path.join(HERE, "audio_it-a2-unita-29.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il giardino", "giardino"), ("B", "la panchina", "panchina"), ("C", "il taglio del nastro", "nastro"), ("D", "il palco", "palco"),
          ("E", "la rastrelliera", "rastrelliera"), ("F", "l'altalena", "altalena"), ("G", "il chiosco", "chiosco"), ("H", "l'aiuola", "aiuola")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-29"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["29.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S292 = [x.split(": ", 1)[1] for x in _r["29.2 Ripeti"].split("\n")]
S293 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["29.3 Fatto o desiderio"].split("\n")]


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
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 29", "Il giardino è pronto", "Desideri, necessità, emozioni · <b>voglio che · è importante che · ho paura che</b>",
                       [("SAI FARE", "dire che cosa vuoi dagli altri, dire che cosa è necessario, esprimere contentezza e paura, fare un breve discorso"),
                        ("LINGUA", "Voglio che tutto sia perfetto. · Bisogna che il tecnico venga. · Ho paura che piova. · Sono contenta che siate qui."),
                        ("PRONUNCIA", "il congiuntivo: che sia, che vada, che faccia")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: un giardino per tutti", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>C'è un parco o un giardino vicino a casa tua? Ci vai spesso?</li><li>Che cosa fai al parco? Con chi?</li><li>Che cosa manca nei parchi della tua città?</li></ol>""",
    28, """<ol><li>A: <i>il taglio del nastro</i> = il momento in cui si apre ufficialmente un posto nuovo (l'inaugurazione); <i>la rastrelliera</i> = il posto per le bici; <i>l'aiuola</i> = lo spazio con i fiori.</li>
<li>B: domanda 3: accettare <i>Spero che ci siano più panchine</i> (congiuntivo, unità 09) o <i>Mancano le panchine</i>; non correggere ancora.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il giardino pubblico</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Gli ultimi controlli · l'inaugurazione</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Il congiuntivo dopo voglio che, è importante che, ho paura che</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il congiuntivo presente (2) · forme irregolari</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Il congiuntivo · fatto o desiderio?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Il congiuntivo · infinito o che? · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Sindaco per un giorno · speranze e paure</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine settembre. Il giardino in Bolognina, il progetto di Marco e Júlia scelto dal Comune a marzo (unità 09), è finito: panchine (l'idea della signora Rossi, unità 16), aiuole, alberi per l'ombra (unità 22), la rastrelliera all'ingresso, il palco e il chiosco del caffè brasiliano. Venerdì gli ultimi controlli: <i>è importante che il palco sia pronto</i>, <i>bisogna che il tecnico venga domattina</i>, <i>ho paura che piova</i>; Júlia farà il discorso (<i>è meglio che sia corto</i>). Sabato l'inaugurazione: arriva la signora Rossi con Franco e Briciola (<i>sono contenta che abbiate messo tante panchine</i>, <i>spero che i ragazzi non facciano troppo rumore</i>); Giulia offre il caffè brasiliano a tutti; Júlia fa il discorso.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Qui il portoghese aiuta: <i>quero que você venha, é importante que seja, tenho medo que chova</i> usano il <i>subjuntivo</i> come l'italiano (<i>venga, sia, piova</i>). Il problema è la forma: lo studente dice <i>voglio che vieni, è importante che sei</i>, oppure inventa <i>vadi, facci</i>. Con lo stesso soggetto, come in portoghese, si usa l'infinito: <i>Voglio andare</i>, non <i>voglio che io vada</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia l'inaugurazione di un parco, di una scuola o di una piazza è una piccola festa: c'è il <b>taglio del nastro</b> con il sindaco o un assessore, spesso suona la <b>banda</b> del paese o del quartiere e ci sono i bambini delle scuole. Molti giardini pubblici hanno i cancelli e <b>chiudono la sera</b>, d'estate verso mezzanotte.</div>
<div class="box"><h4>AUDIO</h4>Traccia 29.1 I due dialoghi (lento e naturale) · Traccia 29.2 Ascolta e ripeti · Traccia 29.3 Fatto o desiderio?</div>""")

    # Page 2
    p1 = [("Le panchine e le aiuole sono", "finite"), ("La rastrelliera per le bici è", "all'ingresso"),
          ("Domani alle dieci suona", "la banda del quartiere"), ("Al palco manca", "la luce"), ("Il discorso deve durare al massimo", "cinque minuti")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("La signora Rossi arriva con Franco e Briciola.", "V"), ("Le panchine sono state un'idea di Giulia.", "F"), ("Il giardino chiude a mezzanotte.", "V"),
          ("Oggi Giulia vende il caffè brasiliano.", "F"), ("Júlia fa il discorso alle dieci e mezza.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: l'inaugurazione", "10 min")}
{audiocard(["29.1 · SLOW", "29.1 · NATURAL"])}
{sub("A", "Prima parte. Venerdì, gli ultimi controlli. Completa.", "4 min", "29.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Sabato, l'inaugurazione. Vero (V) o falso (F)?", "4 min", "29.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa spera Júlia nel discorso?", "2 min")}
<div class="wline">{R("Spera che il giardino diventi il posto dove il quartiere si incontra.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Il giardino nasce nell'unità 09; le panchine sono la richiesta della signora Rossi nell'unità 16.</li>
<li>B: frase 4: oggi Giulia <i>lo offre</i>, cioè è gratis. Frase 5: Marco ripete <i>cinque minuti!</i>: battuta per il discorso lungo.</li></ol>""")

    # Page 3
    rules = [("<i>Voglio che tutto <b>sia</b> perfetto.</i> <i>Sia</i> è", ["congiuntivo", "indicativo"], "congiuntivo"),
             ("Dopo <i>voglio che, è importante che, bisogna che</i> si usa", ["il congiuntivo", "l'indicativo"], "il congiuntivo"),
             ("Dopo <i>sono contenta che, ho paura che</i> si usa", ["il congiuntivo", "l'indicativo"], "il congiuntivo"),
             ("Dopo <i>so che, sono sicuro che</i> (un fatto) si usa", ["l'indicativo", "il congiuntivo"], "l'indicativo"),
             ("<i>Voglio fare il discorso.</i> Stesso soggetto: si usa", ["l'infinito", "che + congiuntivo"], "l'infinito"),
             ("<i>Venire</i> al congiuntivo: <i>che il tecnico</i>", ["venga", "viene"], "venga")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Bisogna che il tecnico", ["venga", "viene"], "venga", "domattina."), ("Sono contenta che", ["abbiate", "avete"], "abbiate", "messo tante panchine."),
          ("Ho paura che domani", ["piova", "piove"], "piova", "."), ("So che il palco", ["è", "sia"], "è", "pronto.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" .", ".") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: voglio che… · ho paura che…", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Voglio che</b> tutto <b>sia</b> perfetto. · Vuoi <b>che</b> lo <b>faccia</b> io? · <b>Voglio che</b> tutti <b>assaggino</b> il caffè.<br>
2. <b>È importante che</b> <b>sia</b> pronto. · <b>Bisogna che</b> il tecnico <b>venga</b>. · <b>È meglio che</b> <b>sia</b> corto.<br>
3. <b>Ho paura che</b> <b>piova</b>. · <b>Sono contenta che</b> <b>abbiate</b> messo tante panchine. · <b>Spero che</b> non <b>facciano</b> rumore.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Dopo <b>volere che, è importante che, bisogna che, è meglio che</b> (desiderio, necessità) e <b>sono contento che, ho paura che, spero che</b> (emozioni) → <b>congiuntivo</b>: <i>sia, abbia, venga, faccia, vada, possa</i>. Fatto sicuro (<i>so che, sono sicuro che</i>) → indicativo. Stesso soggetto → infinito (<i>voglio andare</i>). Tutto: pagina 4.</div>""",
    22, """<ol><li>A: ripasso veloce dell'unità 09 (<i>penso che sia, spero che scelga</i>): qui si aggiungono volontà, necessità ed emozioni.</li>
<li>B: frase 5: in portoghese è uguale (<i>quero fazer</i>, non <i>quero que eu faça</i>).</li></ol>""")

    grammar_ref_it.congiuntivo_volonta(b)

    # Page 5
    opts3 = [["indicativo", "congiuntivo"]] * 6
    ans3 = ["indicativo", "congiuntivo", "congiuntivo", "indicativo", "congiuntivo", "indicativo"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Voglio che vieni.</td><td><b>Voglio che venga.</b></td><td>Volere che + congiuntivo.</td></tr>
<tr><td>Spero che fa bel tempo.</td><td><b>Spero che faccia bel tempo.</b></td><td><i>fare → faccia</i>.</td></tr>
<tr><td>È importante che vadi.</td><td><b>È importante che tu vada.</b></td><td><i>andare → vada</i> (non <i>vadi</i>).</td></tr>
<tr><td>Voglio che io faccio il discorso.</td><td><b>Voglio fare il discorso.</b></td><td>Stesso soggetto: infinito.</td></tr>
<tr><td>So che venga domani.</td><td><b>So che viene domani.</b></td><td>Un fatto: indicativo.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["29.2", "29.3"])}
{sub("A", "Ascolta e ripeti. Nel congiuntivo la vocale finale è chiara: che sia, che vada, che faccia.", "2 min", "29.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S292)}</div>
{sub("B", "Fatto o desiderio? Ascolta: il verbo è all'indicativo o al congiuntivo?", "2 min", "29.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    33, """<ol><li>Errori: riga 3: <i>vadi, facci, stii</i> sono errori frequenti anche tra gli italiani giovani: l'unica forma corretta è <i>vada, faccia, stia</i>.</li>
<li>4A: far sentire la differenza <i>viene / venga</i>, <i>è / sia</i>, <i>piove / piova</i>.</li>
<li>4B: guardare la parola prima di <i>che</i>: <i>so, sono sicuro, secondo me</i> = fatto; <i>voglio, è importante, ho paura</i> = congiuntivo.</li></ol>""")

    # Page 6
    cg = [("Voglio che tu (venire)", "venga", "alla festa."), ("È importante che voi (essere)", "siate", "puntuali."),
          ("Bisogna che Marco (fare)", "faccia", "la spesa."), ("Ho paura che il tecnico non (potere)", "possa", "venire."),
          ("Sono contenta che i miei amici (stare)", "stiano", "bene.")]
    cgl = "".join(f"<li>{a} {A(r, 'min-width:20mm')} {z}</li>" for a, r, z in cg)
    io = [("Voglio (io / andare) al mare.", "Voglio andare al mare."), ("Voglio (tu / andare) dal medico.", "Voglio che tu vada dal medico."),
          ("Ho paura (io / sbagliare).", "Ho paura di sbagliare."), ("Ho paura (Bruno / sbagliare).", "Ho paura che Bruno sbagli.")]
    iol = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in io)
    wb = [("inaugurare", "l'inaugurazione"), ("costruire", "la costruzione"), ("progettare", "il progetto"), ("preoccuparsi", "la preoccupazione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Completa con il congiuntivo.", "3 min")}
<ol style="line-height:1.7">{cgl}</ol>
{sub("B", "Infinito o che + congiuntivo? Scrivi la frase.", "4 min")}
<ol style="line-height:1.4">{iol}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: <i>stare → stia, stiano</i>; <i>potere → possa</i>. Accettare <i>che voi siate</i> anche senza <i>voi</i>.</li>
<li>B: <i>avere paura <b>di</b></i> + infinito; <i>volere</i> + infinito senza preposizione (unità 20).</li>
<li>C: <i>Il progetto del giardino è finito: domani c'è l'inaugurazione.</i></li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Sindaco per un giorno. Sei il sindaco (o la sindaca) della tua città. Che cosa vuoi che cambi? Di' all'insegnante cinque cose. L'insegnante è un cittadino: è d'accordo o ha paura di qualcosa. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Voglio che ci siano più… · È importante che i bambini possano… · Bisogna che il Comune faccia… · È meglio che… · Ho paura che costi troppo. · Spero che… · Sono contento/a che…</div>
{sub("B", "Speranze e paure. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Che cosa è importante che ci sia in un parco?</li><li>Quando organizzi una festa, di che cosa hai paura?</li><li>Che cosa speri che succeda nella tua città quest'anno?</li><li>Che cosa vuoi che facciano i tuoi vicini? E che cosa non vuoi?</li><li>Hai mai fatto un discorso in pubblico? Com'è andata?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: l'insegnante reagisce con <i>Sono contento che…</i> / <i>Ho paura che…</i>, così lo studente sente molte forme; correggere soprattutto <i>vada, faccia, venga, ci siano</i>.</li>
<li>B: domanda 5: passato prossimo + imperfetto (unità 03).</li></ol>""")

    # Page 8
    pc = [("A2 · 27", "So riportare notizie con dice che."), ("A2 · 29", "So dire che cosa voglio che facciano gli altri."),
          ("A2 · 29", "So dire che cosa è importante o necessario."), ("A2 · 29", "So dire sono contento che, ho paura che."),
          ("A2 · 29", "So scegliere tra indicativo e congiuntivo.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Voglio che vieni alla festa.", "Voglio che venga alla festa."), ("È importante che tu arrivi presto.", "✓"),
          ("Spero che fa bel tempo.", "Spero che faccia bel tempo."), ("Voglio che io parlo con il sindaco.", "Voglio parlare con il sindaco."),
          ("So che Marco sia stanco.", "So che Marco è stanco."), ("Ho paura che piova.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio al Comune (50–75 parole).</b> Scrivi al Comune della tua città: che cosa vuoi che facciano nel tuo quartiere? Perché è importante? Di che cosa hai paura? Usa <i>voglio che, è importante che, ho paura che, spero che</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    23, """<p>Prossima lezione: lo studente legge il messaggio; l'insegnante risponde come il sindaco (<i>Sono contento che Lei mi abbia scritto…</i>: solo in ascolto). Unità 30: <i>Benvenuto a Bologna!</i> (dare consigli: ti consiglio di…, dovresti…, l'imperativo con i pronomi).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("29.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("29.2", "Ascolta e ripeti")}
<p>{" · ".join(S292)}</p>
{sub("29.3", "Fatto o desiderio?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S293))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 29 - Il giardino è pronto")
