# Speak! Ponte A2 - Unità 35 "Due anni a Bologna" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 35", audio_json=os.path.join(HERE, "audio_it-a2-unita-35.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'arrivo", "arrivo"), ("B", "i ricordi", "ricordi"), ("C", "la pentola", "pentola"), ("D", "il pão de queijo", "pão de queijo"),
          ("E", "il microfono", "microfono"), ("F", "il locale pieno", "locale"), ("G", "la Sicilia", "Sicilia"), ("H", "l'agenda", "agenda")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-35"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["35.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S352 = [x.split(": ", 1)[1] for x in _r["35.2 Ripeti"].split("\n")]
S353 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["35.3 Quando"].split("\n")]


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
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 35", "Due anni a Bologna", "Il passato, il presente e il futuro · <b>non conoscevo · sono andata · abito qui da · vorrei · spero che</b>",
                       [("SAI FARE", "raccontare com'era prima e com'è adesso, fare un bilancio, parlare di progetti e speranze, rispondere a un'intervista"),
                        ("LINGUA", "Due anni fa non conoscevo nessuno. · Abito qui da due anni. · L'anno prossimo vorrei… · Spero che vengano."),
                        ("PRONUNCIA", "parlare senza fermarsi: le parole si legano")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: prima e adesso", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Com'era la tua vita due anni fa? Che cosa è cambiato?</li><li>Hai mai vissuto in un'altra città o in un altro Paese?</li><li>Qual è il tuo ricordo più bello di quest'anno?</li></ol>""",
    28, """<ol><li>A: <i>il pão de queijo</i> si dice così anche in italiano (o <i>panino al formaggio brasiliano</i>); <i>il locale</i> = il bar, il ristorante; <i>l'agenda</i> = il quaderno degli appuntamenti.</li>
<li>B: domanda 1: <i>era / avevo / abitavo</i> (imperfetto) + <i>è cambiato</i> (passato prossimo): è il tema di tutta l'unità.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: due anni di storia</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il primo venerdì brasiliano · l'intervista</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Tutti i tempi dell'A2 · da, fa, tra</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>I tempi e i modi dell'A2 · da + presente</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Le parole si legano · passato, presente o futuro?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>La storia di Júlia · da, fa, tra, per · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>L'intervista · il mio italiano</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA (E FINISCE L'A2)</h4>Venerdì 27 novembre: il primo venerdì brasiliano al bar di Giulia (unità 34). Più di sessanta persone, la feijoada finisce alle nove; Marco ammette: <i>avevate ragione voi</i>. La signora Rossi vuole un'altra tapioca di Camila, al cocco, e la ricetta. Giulia vuole farlo ogni mese: il prossimo sarà con il pão de queijo. Poi Davide intervista Júlia per il suo progetto, come un anno fa (unità A1 26): il primo giorno non conosceva nessuno; adesso parla italiano ogni giorno, lavora con Marco, è orgogliosa del giardino (unità 29); i ricordi dell'anno (Venezia, Rimini, la maratona); l'anno prossimo vorrebbe visitare finalmente la Sicilia (il desiderio dell'unità A1 26) e spera che i genitori vengano in primavera. <i>Abito qui da due anni e Bologna è casa mia.</i></div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Moro aqui há dois anos</i> diventa <i>ho abitato qui da due anni</i> o <i>abito qui per due anni</i>: in italiano <b>da</b> + <b>presente</b>. <i>Há dois anos</i> nel senso di <i>tempo fa</i> è <i>due anni <b>fa</b></i>; <i>daqui a um mês</i> è <i>tra un mese</i>. Nel racconto lo studente mette tutto al passato prossimo: ricordare l'imperfetto per com'era prima (<i>non conoscevo, non capivo</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Bologna è una delle città italiane con più studenti e lavoratori stranieri, e molti dopo gli studi restano a vivere qui. Chi arriva in Italia dice spesso che il primo anno è il più difficile (la lingua, la burocrazia, gli amici) e che dal secondo anno ci si sente <i>a casa</i>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 35.1 I due dialoghi (lento e naturale) · Traccia 35.2 Ascolta e ripeti · Traccia 35.3 Passato, presente o futuro?</div>""")

    # Page 2
    p1 = [("Al primo venerdì brasiliano ci sono più di", "sessanta persone"), ("La feijoada è finita alle", "nove"), ("La signora Rossi vuole la tapioca con", "il cocco"),
          ("Il mese prossimo fanno", "il pão de queijo"), ("Marco ammette:", "«Avevate ragione voi.»")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("Il primo giorno Júlia non conosceva nessuno.", "V"), ("Adesso Júlia lavora con Davide.", "F"), ("A Júlia è piaciuta la settimana a Rimini.", "V"),
          ("L'anno prossimo Júlia vuole visitare la Sardegna.", "F"), ("Júlia spera che i genitori vengano in primavera.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: il venerdì brasiliano", "10 min")}
{audiocard(["35.1 · SLOW", "35.1 · NATURAL"])}
{sub("A", "Prima parte. Il primo venerdì brasiliano. Completa.", "4 min", "35.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Davide intervista Júlia. Vero (V) o falso (F)?", "4 min", "35.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Júlia si sente bolognese? Perché?", "2 min")}
<div class="wline">{R("Un po' sì: abita lì da due anni e Bologna è casa sua, ma beve ancora il caffè brasiliano.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. È l'ultima unità con una storia nuova dell'A2: chiedere allo studente che cosa ricorda dei personaggi.</li>
<li>B: frase 2: lavora con <b>Marco</b>; frase 4: la <b>Sicilia</b>.</li></ol>""")

    # Page 3
    rules = [("<i>Non <b>conoscevo</b> nessuno</i> (com'era prima) è", ["imperfetto", "passato prossimo"], "imperfetto"),
             ("<i><b>Sono andata</b> a Venezia</i> racconta", ["un fatto finito", "una situazione"], "un fatto finito"),
             ("<i>Abito qui <b>da</b> due anni</i>: la cosa è", ["ancora vera", "finita"], "ancora vera"),
             ("Con <i>da</i> + tempo, se la cosa continua, si usa", ["il presente", "il passato prossimo"], "il presente"),
             ("<i><b>Vorrei</b> visitare la Sicilia</i> è", ["un desiderio", "un fatto"], "un desiderio"),
             ("<i>Spero che i miei genitori <b>vengano</b></i>: dopo <i>spero che</i>", ["congiuntivo", "futuro"], "congiuntivo")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Abito a Bologna", ["da", "per"], "da", "due anni."), ("Sono arrivata due anni", ["fa", "da"], "fa", "."),
          ("", ["Tra", "Fa"], "Tra", "un mese è Natale."), ("Quando sono arrivata,", ["pioveva", "ha piovuto"], "pioveva", ".")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" .", ".") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: prima, adesso, dopo", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Prima:</b> Ero stanchissima, non <b>conoscevo</b> nessuno e non <b>capivo</b> niente. · <b>Avevate</b> ragione voi.<br>
2. <b>Fatti:</b> La feijoada <b>è finita</b> alle nove. · Che cosa ti <b>è piaciuto</b> di più? · <b>Adesso:</b> <b>Parlo</b> italiano tutti i giorni. · <b>Abito</b> qui <b>da</b> due anni.<br>
3. <b>Dopo:</b> La <b>proverò</b> a casa. · Che cosa <b>farai</b>? · <b>Vorrei</b> visitare la Sicilia. · <b>Spero che</b> i miei genitori <b>vengano</b>. · Penso che <b>dovremmo</b> farlo ogni mese.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Prima: <b>imperfetto</b> (com'era) · fatti: <b>passato prossimo</b> · adesso: <b>presente</b> (anche con <b>da</b>: <i>abito qui da due anni</i>) · progetti: <b>futuro</b> · desideri: <b>condizionale</b> (<i>vorrei</i>) · speranze e opinioni: <b>congiuntivo</b> (<i>spero che vengano</i>). Tempo: <b>fa</b> (passato), <b>da</b> (ancora vero), <b>tra</b> (futuro). Tutto: pagina 4.</div>""",
    22, """<ol><li>A: far sottolineare i verbi con tre colori: passato, presente, futuro.</li>
<li>B: frasi 3–4: l'errore principale dell'unità (<i>ho abitato da due anni</i>): insistere sul presente.</li></ol>""")

    grammar_ref_it.tempi_a2(b)

    # Page 5
    opts3 = [["passato", "presente", "futuro"]] * 6
    ans3 = ["passato", "presente", "futuro", "passato", "futuro", "presente"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Abito qui per due anni.</td><td><b>Abito qui da due anni.</b></td><td>Ancora vero: <i>da</i>.</td></tr>
<tr><td>Ho abitato qui da due anni.</td><td><b>Abito qui da due anni.</b></td><td><i>Da</i> + presente.</td></tr>
<tr><td>Sono arrivata da due anni.</td><td><b>Sono arrivata due anni fa.</b></td><td>Passato: <i>fa</i>.</td></tr>
<tr><td>Quando sono arrivata, ha piovuto.</td><td><b>Quando sono arrivata, pioveva.</b></td><td>Lo sfondo: imperfetto.</td></tr>
<tr><td>Spero che vengono.</td><td><b>Spero che vengano.</b></td><td>Congiuntivo.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["35.2", "35.3"])}
{sub("A", "Ascolta e ripeti. Nel parlato le parole si legano: non‿conoscevo‿nessuno. Ripeti tutta la frase senza fermarti.", "2 min", "35.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S352)}</div>
{sub("B", "Passato, presente o futuro? Ascolta e scegli.", "2 min", "35.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: righe 1–3: disegnare una linea del tempo: <i>fa</i> = un punto nel passato; <i>da</i> = dal passato fino a oggi; <i>tra</i> = un punto nel futuro.</li>
<li>4A: prima lentamente, poi più veloce: l'obiettivo è la fluidità, non la perfezione.</li>
<li>4B: 1 conoscevo · 2 lavoro · 3 visiterò · 4 sono andata · 5 verranno · 6 mi sento.</li></ol>""")

    # Page 6
    cz = [("Due anni fa (arrivare, io)", "sono arrivata", "a Bologna."), ("All'inizio non (capire, io)", "capivo", "niente."),
          ("Poi (conoscere, io)", "ho conosciuto", "Giulia e Davide."), ("Adesso (lavorare, io)", "lavoro", "con Marco."),
          ("L'anno prossimo (visitare, io)", "visiterò", "la Sicilia.")]
    czl = "".join(f"<li>{a} {A(r, 'min-width:28mm')} {z}</li>" for a, r, z in cz)
    tm = [("Abito a Bologna ___ due anni.", "da"), ("Sono arrivata due anni ___.", "fa"), ("___ un mese è Natale.", "Tra"),
          ("Ho abitato a Recife ___ vent'anni.", "per"), ("Studio italiano ___ settembre.", "da")]
    tml = "".join(f"<li>{s.split('___')[0]}{A(r, 'min-width:12mm')}{s.split('___')[1]}</li>" for s, r in tm)
    wb = [("ricordare", "il ricordo"), ("cambiare", "il cambiamento"), ("sognare", "il sogno"), ("crescere", "la crescita")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "La storia di Júlia. Scrivi il verbo al tempo giusto.", "3 min")}
<ol style="line-height:1.7">{czl}</ol>
{sub("B", "Da, fa, tra o per?", "4 min")}
<ol style="line-height:1.7">{tml}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 1: Júlia è una donna: <i>sono arrivat<b>a</b></i>. Frase 5: anche <i>vorrei visitare</i> è corretto.</li>
<li>B: frase 4: <i>per</i> = periodo finito (adesso non abita più a Recife).</li>
<li>C: <i>Il mio sogno è…</i> · <i>Che cambiamento!</i></li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "L'intervista. L'insegnante è Davide e ti fa un'intervista: com'era la tua vita due anni fa? Che cosa hai fatto quest'anno? Com'è adesso? Che cosa farai o vorresti fare? Poi cambiate: tu intervisti l'insegnante.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Due anni fa… · All'inizio… · Poi… · Adesso… · Da un anno… · Quest'anno mi è piaciuto… · L'anno prossimo… · Vorrei… · Spero che… · Mi sento a casa.</div>
{sub("B", "Il mio italiano. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Quando hai cominciato a studiare italiano? Da quanto tempo lo studi?</li><li>Che cosa non capivi all'inizio?</li><li>Che cosa sai fare adesso che prima non sapevi fare?</li><li>Che cosa vorresti fare in italiano tra un anno?</li><li>Qual è il personaggio della storia che ti piace di più? Perché?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: è un piccolo esame orale dell'A2: annotare gli errori ricorrenti e riprenderli nel Ripasso 4.</li>
<li>B: domanda 1: <i>Lo studio da…</i> (presente!). Domanda 5: ripasso dei personaggi.</li></ol>""")

    # Page 8
    pc = [("A2 · 34", "So chiedere e dare un'opinione."), ("A2 · 35", "So raccontare com'era prima e com'è adesso."),
          ("A2 · 35", "So usare da, fa, tra, per."), ("A2 · 35", "So parlare dei miei progetti e delle mie speranze."),
          ("A2 · 35", "So usare i tempi dell'A2 in una conversazione.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Abito qui per due anni.", "Abito qui da due anni."), ("Due anni fa non parlavo italiano.", "✓"),
          ("Quando sono arrivata, ha piovuto.", "Quando sono arrivata, pioveva."), ("Spero che i miei genitori vengono.", "Spero che i miei genitori vengano."),
          ("Sono a Bologna fa due anni.", "Sono a Bologna da due anni."), ("L'anno prossimo visiterò la Sicilia.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Il mio percorso con l'italiano (50–75 parole).</b> Racconta: com'era il tuo italiano all'inizio, che cosa hai fatto per impararlo, che cosa sai fare adesso, che cosa vorresti fare in futuro. Usa l'imperfetto, il passato prossimo, il presente con <i>da</i> e il condizionale.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il testo; l'insegnante fa domande con tutti i tempi. Unità 36: <i>Ripasso 4</i> (unità 29–35), fine dell'A2.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("35.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("35.2", "Ascolta e ripeti")}
<p>{" · ".join(S352)}</p>
{sub("35.3", "Passato, presente o futuro?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S353))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 35 - Due anni a Bologna")
