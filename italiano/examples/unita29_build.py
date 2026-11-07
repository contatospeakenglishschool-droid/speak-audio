# Speak! Essenziale A1 - Unità 29 "Cerco una stanza" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from annunci import annunci
setup(band="A1 · UNITÀ 29", audio_json=os.path.join(HERE, "audio_it-a1-unita-29.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la stanza", "stanza"), ("B", "l'affitto", "affitto"), ("C", "i soldi", "soldi"), ("D", "la luce", "luce"),
          ("E", "internet", "internet"), ("F", "gli annunci", "annunci"), ("G", "il monolocale", "monolocale"), ("H", "il palazzo", "palazzo")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-29"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["29.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S292 = [x.split(": ", 1)[1] for x in _r["29.2 Ripeti i numeri"].split("\n")]
S293 = [x.split(": ", 1)[1] for x in _r["29.3 Dettato dei prezzi"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split()[-1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 29", "Cerco una stanza", "Bruno cerca casa a Bologna · <b>i numeri da 100 a 1.000.000</b>",
                       [("SAI FARE", "leggere un annuncio, chiedere il prezzo di una stanza e capire l'affitto, le spese e la cauzione"),
                        ("LINGUA", "Quanto costa al mese? · trecentocinquanta euro · spese incluse / escluse · mille, duemila"),
                        ("PRONUNCIA", "i numeri grandi · dettato dei prezzi")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: cercasi stanza", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Dove abiti? In una casa, in un appartamento o in una stanza?</li><li>Che cosa è importante per te in una casa?</li><li>Nella tua città le case sono care?</li></ol>""",
    22, """<ol><li>A: <i>l'affitto</i> = i soldi che si pagano ogni mese per la casa. <i>Il monolocale</i> = un appartamento con una sola stanza (e il bagno). <i>La luce</i> qui è anche la bolletta della luce.</li>
<li>B: i numeri grandi arrivano nell'ascolto; qui accettare risposte semplici (<i>sì, molto care</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: la casa e l'affitto</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Gli annunci · la visita della stanza · il consiglio di Davide</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>I numeri da 100 a 1.000.000 · quanto costa / costano</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>I numeri grandi · dettato dei prezzi</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Quattro annunci: fare i conti</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Telefonare per una stanza · i prezzi nella tua città</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Bruno è arrivato sabato e per ora abita da Júlia. Con lei legge gli annunci: una stanza in via San Vitale costa 350 euro al mese, spese escluse; un monolocale in via Mascarella 480 euro (troppo: quasi seimila euro all'anno). Lunedì visita la stanza di via San Vitale: 14 metri quadrati, 350 euro più circa 60 di spese, e 700 euro di cauzione. Al bar Davide gli dice che a Bologna un appartamento costa 300.000 euro e gli dà il numero del suo collega Paolo, che ha una stanza libera in via Zamboni a 380 euro, spese incluse. <b>Da questa unità Bruno parla</b> (voce fissa: Iapetus).</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese i numeri si scrivono separati con <i>e</i> (<i>trezentos e cinquenta</i>): in italiano sono <b>una parola sola e senza «e»</b>: <b>trecentocinquanta</b>. <i>Mil → mila</i> al plurale: <b>duemila</b> (non <i>duemille</i>). <i>Cem</i> → <b>cento</b>, senza <i>un</i>. <i>Um milhão de</i> → <b>un milione di</b>. E <i>quanto custam</i> → <b>quanto costano</b>, con il plurale.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>A Bologna vivono circa 90.000 studenti universitari e trovare una stanza è difficile: molti studenti abitano in appartamenti condivisi, in una <b>stanza singola</b> o <b>doppia</b>. Negli annunci si legge <i>affittasi</i>, <i>spese incluse / escluse</i> (luce, gas, acqua, internet, condominio) e la <b>cauzione</b>, di solito due o tre mesi di affitto, che il proprietario restituisce alla fine del contratto.</div>
<div class="box"><h4>AUDIO</h4>Traccia 29.1 Tre dialoghi (lento e naturale) · Traccia 29.2 I numeri grandi · Traccia 29.3 Dettato dei prezzi</div>""")

    # Page 2
    tb = [("via San Vitale", "350 €", "escluse (50–60 €)"), ("via Mascarella (monolocale)", "480 €", "incluse"), ("via Zamboni (il collega di Davide)", "380 €", "incluse")]
    tbr = "".join(f"<tr><td>{v}</td><td style='width:26mm;text-align:center'>{A(p, 'min-width:16mm')}</td><td style='width:42mm'>{A(s, 'min-width:30mm')}</td></tr>" for v, p, s in tb)
    vf = [("La stanza di via San Vitale è di quattordici metri quadrati.", "V"), ("Le spese sono circa trenta euro al mese.", "F"),
          ("La cauzione è di settecento euro.", "V"), ("Bruno prende subito la stanza.", "F"), ("A Bologna un appartamento costa trecentomila euro.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: quanto costa?", "10 min")}
<p>Bruno legge gli annunci con Júlia, visita una stanza e chiede un consiglio a Davide.</p>
{audiocard(["29.1 · SLOW", "29.1 · NATURAL"])}
{sub("A", "Dialoghi 1 e 3. Ascolta e completa: quanto costano le stanze?", "4 min", "29.1 · SLOW")}
<table style="margin:0"><tr><th>stanza</th><th>al mese</th><th>spese</th></tr>{tbr}</table>
{sub("B", "Dialoghi 2 e 3. Vero (V) o falso (F)?", "4 min", "29.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Qual è il numero di telefono di Paolo?", "2 min")}
<div class="wline">{R("347 218 9506")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Gli studenti scrivono le cifre (350), non le parole: le parole arrivano a pagina 3.</li>
<li>B: versione <b>naturale</b>. 2: circa <b>sessanta</b>. 4: Bruno dice <i>Ci penso e La chiamo domani</i>. C: i numeri di cellulare si dicono spesso cifra per cifra.</li></ol>""")

    # Page 3 (3A spiegazione, 3B controlla, 3C pratica)
    nm = [("100", "cento"), ("200", "duecento"), ("350", "trecentocinquanta"), ("480", "quattrocentottanta"), ("1.000", "mille"),
          ("1.200", "milleduecento"), ("2.000", "duemila"), ("15.000", "quindicimila"), ("300.000", "trecentomila"), ("1.000.000", "un milione")]
    nmr = "".join(f"<tr><td style='width:22mm;text-align:right'><b>{n}</b></td><td>{w}</td></tr>" for n, w in nm)
    ck = [("2.000", ["duemille", "duemila"], "duemila"), ("100 euro", ["cento euro", "un cento euro"], "cento euro"),
          ("650", ["seicento e cinquanta", "seicentocinquanta"], "seicentocinquanta"), ("1.000.000 di persone", ["un milione di persone", "un milione persone"], "un milione di persone")]
    ckl = "".join(f"<li>{n} → {ch(o, r)}</li>" for n, o, r in ck)
    pr = [("420", "quattrocentoventi"), ("700", "settecento"), ("1.500", "millecinquecento"), ("3.000", "tremila"), ("25.000", "venticinquemila"), ("180", "centottanta")]
    prl = [f'<li value="{i+1}">{n} {A(w, "min-width:42mm")}</li>' for i, (n, w) in enumerate(pr)]
    b.page(f"""{sec(3, "Grammatica: i numeri grandi", "10 min")}
{sub("A", "Leggi la spiegazione.", "4 min")}
<div class="two"><table style="margin:0;font-size:9.2pt">{nmr}</table>
<div class="box sand" style="margin:0"><h4>REGOLA</h4>
1. I numeri sono <b>una parola sola</b>, senza «e»: <i>trecentocinquanta</i>.<br>
2. <b>cento</b> e <b>mille</b> senza «un»: <i>cento euro, mille euro</i>.<br>
3. <b>mille</b> → plurale <b>mila</b>: <i>duemila, quindicimila</i>.<br>
4. <b>un milione di</b> + nome: <i>un milione di euro</i>; plurale <i>due milioni</i>.<br>
5. <i>cento + ottanta</i> → <b>centottanta</b> (cade la «o»).<br>
6. Il prezzo: <b>Quanto costa</b> la stanza? · <b>Quanto costano</b> le spese? · <i>al mese, all'anno</i>.</div></div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "Pratica. Scrivi i numeri in lettere.", "4 min")}
{twocol(prl, 4)}""",
    24, """<ol><li>A: nello scritto italiano il punto separa le migliaia (1.500) e la virgola i decimali (3,50 €): come in Brasile.</li>
<li>C: 6: <i>centottanta</i> (cade la «o» di <i>cento</i> davanti a <i>ottanta</i>); anche <i>centotto</i>.</li></ol>""")

    # Page 4
    dict_ans = ["350", "480", "700", "1.200", "15.000", "300.000"]
    dl = [f'<li value="{i+1}">{A(a, "min-width:24mm")} €</li>' for i, a in enumerate(dict_ans)]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>trecento e cinquanta euro</td><td><b>trecentocinquanta euro</b></td><td>Una parola sola.</td></tr>
<tr><td>duemille euro</td><td><b>duemila euro</b></td><td><i>mille</i> → <i>mila</i>.</td></tr>
<tr><td>un cento euro</td><td><b>cento euro</b></td><td>Senza <i>un</i>.</td></tr>
<tr><td>un milione euro</td><td><b>un milione di euro</b></td><td><i>milione di</i> + nome.</td></tr>
<tr><td>Quanto costa le spese?</td><td><b>Quanto costano le spese?</b></td><td>Plurale: <i>costano</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["29.2", "29.3"])}
{sub("A", "I numeri grandi. Ascolta e ripeti. Attenzione: mi-LL-e (doppia L), ma due-mi-L-a e mi-L-ione (una L).", "2 min", "29.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S292)}</div>
{sub("B", "Dettato dei prezzi. Ascolta e scrivi il numero in cifre.", "3 min", "29.3")}
{twocol(dl, 4)}""",
    34, """<ol><li>Errori: il primo è il più frequente, perché in portoghese si dice <i>trezentos e cinquenta</i>.</li>
<li>4B: lasciare 4 secondi tra un numero e l'altro. Dopo, gli studenti leggono i numeri ad alta voce.</li></ol>""")

    # Page 5
    qs = [("Quale stanza costa di più al mese?", "la 2, via Mascarella (480 €)"), ("Quanto costa la stanza 1 con le spese?", "circa 410 €: quattrocentodieci euro"),
          ("Quanto costa la stanza 3 in un anno?", "4.560 €: quattromilacinquecentosessanta euro"), ("Quanto è la cauzione della stanza 2?", "1.440 €: millequattrocentoquaranta euro"),
          ("Quale stanza è più economica, con le spese?", "la 4, Bolognina (circa 310 €)")]
    qsl = "".join(f"<li>{q} {A(a, 'min-width:60mm')}</li>" for q, a in qs)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Quattro annunci. Leggi e fai i conti. Scrivi le risposte anche in lettere.", "8 min")}
{annunci()}
<ol style="line-height:1.75;margin-top:2mm">{qsl}</ol>""",
    22, """<ol><li>A: si può usare la calcolatrice del telefono: l'importante è leggere i risultati ad alta voce. <i>Più economica</i> = costa meno.</li>
<li>Domanda extra: <i>Quale stanza preferisci? Perché?</i> (ripasso di <i>perché</i>, unità 28).</li></ol>""")

    # Page 6
    pc6 = ["un affitto in centro", "un caffè al bar", "un biglietto dell'autobus", "un appartamento in centro", "un'auto nuova", "un telefono nuovo"]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Telefonare per una stanza. Scegli un annuncio della pagina 5 e telefona al proprietario (l'insegnante). Chiedi le informazioni. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt"><h4>PAROLE UTILI</h4>Buongiorno, chiamo per la stanza in via… · È ancora libera? · Quanto costa al mese? · Le spese sono incluse? · Quanto è la cauzione? · Quanti metri quadrati è? · Posso vederla? · Quando? · Grazie, ci penso!</div>
{sub("B", "I prezzi nella tua città. Quanto costa…? Rispondi e fai le domande all'insegnante.", "6 min")}
<table style="margin:1mm 0"><tr><th>Quanto costa…?</th><th style="width:34mm">nella mia città</th><th style="width:34mm">in Italia (l'insegnante)</th></tr>
{"".join(f"<tr><td>{x}</td><td></td><td></td></tr>" for x in pc6)}</table>""",
    24, """<ol><li>A: l'insegnante dà numeri «difficili» (<i>trecentottantacinque, milleduecentocinquanta</i>) e lo studente li ripete per controllare: <i>Scusi, quanto?</i></li>
<li>B: i prezzi in reais si dicono in italiano (<i>duemila reais</i>). In Italia: caffè circa 1,20 €.</li></ol>""")

    # Page 7
    pc = [("Unità 28", "So spiegare perché e a che cosa serve: perché…, per…"), ("Unità 29", "So dire e scrivere i numeri da 100 a 1.000.000."),
          ("Unità 29", "So chiedere il prezzo: quanto costa / costano?"), ("Unità 29", "So leggere un annuncio: spese, cauzione, metri quadrati."),
          ("Unità 29", "So capire un prezzo al telefono.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("550", "cinquecentocinquanta"), ("1.300", "milletrecento"), ("4.000", "quattromila"), ("780", "settecentottanta"), ("60.000", "sessantamila"), ("2.000.000", "due milioni")]
    hl = "".join(f'<li>{n} {A(w, "min-width:45mm")}</li>' for n, w in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Scrivi i numeri in lettere.</b></p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il tuo annuncio.</b> Scrivi un annuncio per la tua casa o per una stanza (vera o inventata): dove, quanti metri quadrati, quanto costa al mese, spese, cauzione e perché è bella.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il suo annuncio e l'insegnante telefona per chiedere informazioni. Unità 30: <i>All'università</i> (Bruno si iscrive: i moduli e i dati personali).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("29.1", "Quanto costa? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("29.2", "I numeri grandi")}
<p>{" · ".join(S292)}</p>
{sub("29.3", "Dettato dei prezzi")}
<p>{" · ".join(S293)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 29 - Cerco una stanza")
