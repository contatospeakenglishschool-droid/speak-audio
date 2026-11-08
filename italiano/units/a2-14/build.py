# Speak! Ponte A2 - Unità 14 "La spesa sostenibile" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 14", audio_json=os.path.join(HERE, "audio_it-a2-unita-14.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il mercato", "mercato"), ("B", "le fragole", "fragole"), ("C", "le uova", "uova"), ("D", "il formaggio", "formaggio"),
          ("E", "il pane", "pane"), ("F", "il supermercato", "supermercato"), ("G", "la plastica", "plastica"), ("H", "il campo", "campo")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-14"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["14.1 Testo e dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
BLOG = SCRIPT[1][1]
S142 = [x.split(": ", 1)[1] for x in _r["14.2 Ripeti"].split("\n")]
S143 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["14.3 Ci o ne"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split(" ", 1)[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 14", "La spesa sostenibile", "Cibo e abitudini · <b>ne (quanto?) · ci (dove?) · ce n'è, ce ne sono</b>",
                       [("SAI FARE", "leggere un breve testo di un blog, fare la spesa al mercato, parlare delle tue abitudini e dell'ambiente"),
                        ("LINGUA", "Ne prendo mezzo chilo. · Non ne ho più. · Ci vado ogni sabato. · Ce n'è ancora? · Ci ho pensato."),
                        ("PRONUNCIA", "ci e ne nella frase: ci vado, ne prendo, ce n'è")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: fare la spesa", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Dove fai la spesa? Al supermercato o al mercato? Quante volte alla settimana?</li><li>Compri prodotti locali? Quali?</li><li>Che cosa fai per usare meno plastica?</li></ol>""",
    24, """<ol><li>A: <i>l'uovo → le uova</i> (plurale irregolare, femminile). <i>Il mercato contadino</i> = dove vendono direttamente i produttori.</li>
<li>B: domanda 1: <i>Ci vado due volte</i> → annotare le frasi spontanee con <i>ci</i>; le riprendiamo a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: la spesa</td><td>1</td></tr>
<tr><td>2 Lettura e ascolto</td><td>10 min</td><td>Il blog del bar di Giulia · al mercato contadino</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>ne con le quantità · ci con i luoghi · ce n'è / ce ne sono</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Ne · ci · lo, ne o ci?</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>ci e ne nella frase · luogo o quantità?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Rispondi con ne o ci · lo o ne? · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Al mercato (gioco di ruolo) · le mie abitudini</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Metà maggio. Da un mese Giulia compra per il bar solo prodotti a chilometro zero e lo racconta nel blog del bar: latte di una fattoria vicina (trenta litri alla settimana), uova dei colli, pane di un forno in via San Vitale dove va ogni mattina alle sei in bicicletta; le paste del giorno prima a metà prezzo, così non ne butta più. Sabato la signora Rossi porta Júlia al mercato contadino, dove va da vent'anni: Júlia compra mezzo chilo di fragole e due etti di formaggio con la sua borsa di stoffa; le uova sono già finite. La signora Rossi va al supermercato solo per il caffè… brasiliano!</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese non ha <i>ne</i>: lo studente dice <i>prendo due etti</i> (→ <b>ne prendo due etti</b>) o <i>non ho più</i> (→ <b>non ne ho più</b>). Al posto di <i>ci</i> usa <i>lì</i> (<i>vado lì ogni sabato</i>): non è sbagliato, ma <b>ci vado</b> è più naturale. Attenzione a <i>ci ne sono</i> (→ <b>ce ne sono</b>) e a <i>l'uovo → le uova</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In molte città italiane ci sono i <b>mercati contadini</b>, dove gli agricoltori vendono i loro prodotti: a Bologna il più famoso è il Mercato della Terra, il sabato mattina. Nei negozi italiani le buste di plastica si pagano: molti portano la <b>borsa di stoffa</b>. Al banco si chiede in <b>etti</b> (100 grammi): <i>due etti di prosciutto</i>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 14.1 Il blog e il dialogo (lento e naturale) · Traccia 14.2 Ascolta e ripeti · Traccia 14.3 Luogo o quantità?</div>""")

    # Page 2
    vf = [("Giulia va dal fornaio in macchina.", "F"), ("Il bar usa trenta litri di latte alla settimana.", "V"), ("Le paste del giorno prima si buttano.", "F"),
          ("A marzo non ci sono fragole locali.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    sp = [("le fragole", "mezzo chilo"), ("le uova", "niente: sono finite"), ("il formaggio", "due etti")]
    spl = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:42mm')}</td></tr>" for a, x in sp)
    b.page(f"""{sec(2, "Lettura e ascolto: a chilometro zero", "10 min")}
{audiocard(["14.1 · SLOW", "14.1 · NATURAL"])}
{sub("A", "Leggi il blog del bar di Giulia (o ascoltalo). Vero (V) o falso (F)?", "4 min", "14.1 · SLOW")}
<div class="msg" style="max-width:none;padding:2mm 3.5mm;font-size:9.1pt;line-height:1.5"><b style="color:{TEAL}">Il blog del Bar Giulia · La spesa sostenibile</b><br>{BLOG}</div>
<table style="margin:1mm 0 0">{vfr}</table>
{sub("B", "Seconda parte. Sabato al mercato contadino: che cosa compra Júlia? Quanto?", "4 min", "14.1 · NATURAL")}
<table style="margin:0;width:70%">{spl}</table>
{sub("C", "Perché la signora Rossi va al supermercato?", "2 min")}
<div class="wline">{R("Solo per comprare il caffè (brasiliano).")}</div>""",
    22, """<ol><li>A: far sottolineare nel testo tutti i <i>ne</i> e i <i>ci</i>: che cosa sostituiscono? (<i>ne usiamo</i> = di latte, <i>ci vado</i> = al forno).</li>
<li>B: versione <b>naturale</b>. <i>Le ho finite</i> (le uova, tutte) ≠ <i>non ne ho più</i>: ripresa a pagina 4.</li></ol>""")

    # Page 3
    rules = [("<i>Ne usiamo trenta litri.</i> <i>Ne</i> sostituisce", ["di latte (una quantità)", "al forno (un luogo)"], "di latte (una quantità)"),
             ("<i>Ci vado ogni mattina.</i> <i>Ci</i> sostituisce", ["al forno (un luogo)", "di pane (una quantità)"], "al forno (un luogo)"),
             ("<i>Non ne ho più</i> vuol dire", ["ne ho zero", "ne ho molte"], "ne ho zero"),
             ("<i>Ci ho pensato</i>: <i>ci</i> sostituisce", ["a questa cosa (pensare a…)", "un luogo"], "a questa cosa (pensare a…)"),
             ("Davanti a <i>ne</i>, <i>ci</i> diventa", ["ce (ce ne sono)", "ci (ci ne sono)"], "ce (ce ne sono)"),
             ("<i>Ne</i> e <i>ci</i> vanno", ["prima del verbo", "dopo il verbo"], "prima del verbo")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Quanto pane compri? —", ["Ne", "Ci"], "Ne", "compro un chilo."), ("Vai spesso al mercato? — Sì,", ["ci", "ne"], "ci", "vado il sabato."),
          ("Ci sono ancora fragole? — No, non", ["ce ne", "ci ne"], "ce ne", "sono più."), ("Pensi all'ambiente? — Sì,", ["ci", "lo"], "ci", "penso spesso.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: ne e ci", "10 min")}
{sub("A", "Studia le frasi del blog e del dialogo.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Il latte: <b>ne</b> usiamo trenta litri. · Quante <b>ne</b> vuole? — <b>Ne</b> prendo mezzo chilo. · <b>Ne</b> vuole un etto?<br>
2. Oggi non <b>ne</b> ho più. · Così non <b>ne</b> buttiamo più. · Le fragole a marzo? Non <b>ce ne</b> sono! · Il formaggio? <b>Ce n'è</b> ancora?<br>
3. Il forno: <b>ci</b> vado ogni mattina. · Al mercato: <b>ci</b> vengo ogni sabato · <b>ci</b> arrivo alle otto.<br>
4. <b>Ci</b> ho pensato a lungo. · E voi? <b>Ci</b> avete mai pensato?</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>ne</b> = una quantità di qualcosa (<i>ne prendo due etti, non ne ho più</i>). <b>ci</b> = un luogo (<i>ci vado</i>) o la cosa di <i>pensare a</i> (<i>ci penso</i>). <b>ci + ne → ce ne</b>: <i>ce n'è, ce ne sono</i>. Vanno prima del verbo. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: la domanda magica: <i>Quanto? → ne. Dove? → ci.</i></li>
<li>C: frase 4: <i>pensare <b>a</b></i> → <i>ci</i>; <i>lo penso</i> non si dice in questo senso.</li></ol>""")

    grammar_ref_it.ne_ci(b)

    # Page 5
    ans3 = ["luogo", "quantità", "quantità", "luogo", "quantità", "luogo"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Quanto formaggio? Prendo due etti.</td><td><b>Ne prendo due etti.</b></td><td>Una quantità: <i>ne</i>.</td></tr>
<tr><td>Uova? Non ho più.</td><td><b>Non ne ho più.</b></td><td>Zero: <i>non ne… più</i>.</td></tr>
<tr><td>Ci ne sono ancora?</td><td><b>Ce ne sono ancora?</b></td><td><i>ci + ne → ce ne</i>.</td></tr>
<tr><td>Al mercato vado lì ogni sabato.</td><td><b>Al mercato ci vado ogni sabato.</b></td><td>Più naturale con <i>ci</i>.</td></tr>
<tr><td>gli uovi</td><td><b>le uova</b></td><td>Plurale irregolare.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["14.2", "14.3"])}
{sub("A", "Ascolta e ripeti. Ci e ne non hanno accento: si legano al verbo (civàdo, neprèndo).", "2 min", "14.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S142)}</div>
{sub("B", "Luogo (ci) o quantità (ne)? Ascolta e scegli.", "2 min", "14.3")}
{twocol([f'<li value="{i+1}">{ch(["luogo", "quantità"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>gli uovi</i> è frequente; <i>l'uovo</i> al plurale diventa femminile: <i>le uova</i> (come <i>il braccio → le braccia</i>, unità 26).</li>
<li>4A: <i>ci</i> e <i>ne</i> sono parole "deboli": farle pronunciare unite al verbo, senza pausa.</li></ol>""")

    # Page 6
    qa = [("Quanti caffè bevi al giorno? (3)", "Ne bevo tre."), ("Vai spesso al supermercato? (due volte alla settimana)", "Ci vado due volte alla settimana."),
          ("Hai ancora latte? (no)", "No, non ne ho più."), ("Quando torni al mercato? (sabato)", "Ci torno sabato."),
          ("Ci sono ancora uova? (sì, sei)", "Sì, ce ne sono sei.")]
    qal = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in qa)
    ln = [("Le fragole? ___ ho mangiate tutte.", "Le"), ("Le fragole? ___ ho mangiate tre.", "Ne"), ("Il formaggio? ___ compro due etti.", "Ne"),
          ("Il formaggio? ___ compro al mercato.", "Lo")]
    lnl = "".join(f"<li>{s.replace('___', A(a, 'min-width:12mm'))}</li>" for s, a in ln)
    wb = [("sprecare", "lo spreco"), ("produrre", "il prodotto"), ("vendere", "la vendita"), ("coltivare", "la coltivazione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Rispondi con ne o ci.", "4 min")}
<ol style="line-height:1.45">{qal}</ol>
{sub("B", "Tutto o una parte? Lo, la, li, le o ne?", "3 min")}
<ol style="line-height:1.7">{lnl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: con <i>ci sono</i> + quantità: <i>ce ne sono sei</i>. B: con <i>ne</i> + participio c'è l'accordo (<i>ne ho mangiate tre</i>).</li>
<li>C: <i>lo spreco</i> è nel blog (<i>meno sprechi</i>). Chiedere: <i>Come si può evitare lo spreco?</i></li></ol>""")

    # Page 7
    sell = "fragole 4 €/chilo · uova 0,40 € l'una · formaggio 2,50 €/etto · pane 3 €/chilo · miele 8 € il vasetto · asparagi (finiti!)"
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Al mercato contadino. L'insegnante è il contadino o la contadina. Hai 15 euro: compra quattro prodotti. Chiedi quanto costano, di' quanto ne vuoi. Poi cambiate.", "6 min")}
<div class="box" style="margin-top:1mm"><h4>IL BANCO DI OGGI</h4>{sell}</div>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Quanto costano…? · Ne prendo un chilo / due etti / mezzo chilo / sei. · Ce n'è ancora? · Non ne ho più. · Qualcos'altro? · Basta così, grazie. · Quant'è? · Ho la mia borsa.</div>
{sub("B", "Le mie abitudini. Rispondi e fai le stesse domande all'insegnante: Dove fai la spesa? Quante volte ci vai? Quanta acqua bevi al giorno? Quante bottiglie di plastica compri? Che cosa butti?", "6 min")}
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: per gli asparagi l'insegnante risponde <i>Mi dispiace, non ne ho più!</i> Pretendere <i>ne</i> in ogni risposta con una quantità.</li>
<li>B: le risposte devono avere <i>ci</i> (luogo) e <i>ne</i> (quantità): <i>Ci vado una volta alla settimana. Ne bevo due litri.</i></li></ol>""")

    # Page 8
    pc = [("A2 · 13", "So fare paragoni e usare -issimo, meglio, migliore."), ("A2 · 14", "So capire un breve testo di un blog."),
          ("A2 · 14", "So usare ne con le quantità (ne prendo due etti, non ne ho più)."), ("A2 · 14", "So usare ci con i luoghi (ci vado)."),
          ("A2 · 14", "So fare la spesa al mercato.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Quanto pane vuole? Voglio un chilo.", "Ne voglio un chilo."), ("Al mercato ci vado il sabato.", "✓"),
          ("Ci ne sono ancora?", "Ce ne sono ancora?"), ("Latte? Non ho più.", "Non ne ho più."),
          ("Ho comprato dodici uovi.", "dodici uova"), ("Ci ho pensato molto.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Il mio blog (50–75 parole).</b> Scrivi un post per il blog di Giulia: dove fai la spesa, quante volte ci vai, che cosa compri e quanto ne compri, che cosa fai per sprecare meno. Usa <i>ci</i> e <i>ne</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il post; l'insegnante fa domande con <i>quanto? dove?</i> Unità 15: <i>Sto lavorando!</i> (stare + gerundio, stare per).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("14.1", "Il blog e il mercato (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("14.2", "Ascolta e ripeti")}
<p>{" · ".join(S142)}</p>
{sub("14.3", "Luogo o quantità?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S143))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 14 - La spesa sostenibile")
