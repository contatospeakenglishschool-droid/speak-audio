# Speak! Essenziale A1 - Unità 05 "La mia giornata" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 05", audio_json=os.path.join(HERE, "audio_it-a1-unita-05.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "fare colazione", "colazione"), ("B", "andare in bicicletta", "bicicletta"), ("C", "lavorare", "lavorare"), ("D", "pranzare", "pranzare"),
          ("E", "andare in palestra", "palestra"), ("F", "uscire con gli amici", "uscire"), ("G", "guardare la TV", "TV"), ("H", "dormire", "dormire")]

SCRIPT = [("Narratore", "Dialogo uno. Allo studio, la mattina."), ("Marco", "Júlia, scusa, che ore sono?"), ("Júlia", "Sono le nove e un quarto."),
          ("Marco", "Le nove e un quarto? Sono in ritardo! La riunione è alle nove!"), ("Júlia", "Tranquillo, Marco. La riunione è alle dieci."), ("Marco", "Ah, meno male!"),
          ("Narratore", "Dialogo due. In pausa pranzo."), ("Marco", "A che ora finisci di lavorare, di solito?"), ("Júlia", "Finisco alle sei. Poi vado in palestra."),
          ("Marco", "In palestra? Io non vado mai in palestra! La sera esco con gli amici o guardo la TV."), ("Júlia", "E la mattina? A che ora parti da casa?"),
          ("Marco", "Parto alle otto e mezza, in bicicletta."),
          ("Narratore", "Dialogo tre. La sera, sulle scale."), ("Júlia", "Ciao, Davide! Esci?"), ("Davide", "Sì, esco con gli amici. Andiamo in piazza Santo Stefano."),
          ("Júlia", "Divertiti! Io dormo presto: la mattina apro lo studio alle otto."),
          ("Davide", "Alle otto? Io la mattina dormo fino alle dieci! Ma la sera studio fino all'una."), ("Júlia", "All'una?"), ("Davide", "Sì. Di notte capisco meglio!")]
S052 = ["Che ore sono?", "Sono le otto.", "È l'una.", "È mezzogiorno.", "Sono le sette e mezza.", "Sono le nove e un quarto.", "Sono le sei meno un quarto.", "A che ora?", "Alle otto e mezza."]
S053 = ["esco", "esci", "finisco", "finisci", "capisco", "capisci", "uscire", "Esci stasera?", "Finisco alle sei."]


def clocks(T, A, items, w="41.5mm"):
    return '<div class="clk">' + "".join(f'<div class="c" style="width:{w}"><b style="font-size:14pt;color:{TEAL}">{t}</b><div class="wline" style="font-size:8.5pt">{A(a, "min-width:0;border:0;font-size:7.6pt;line-height:1.25") if T else "&nbsp;"}</div></div>' for t, a in items) + "</div>"


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 05", "La mia giornata", "La routine e il tempo libero · <b>che ore sono?</b>",
                       [("SAI FARE", "dire e chiedere l'ora; parlare della tua giornata"), ("LINGUA", "dormire · finisco · vado · esco · non… mai · i / gli / le"),
                        ("PRONUNCIA", "l'ora · sc: esco / esci, finisco / finisci")])
    words = ["andare in bicicletta", "andare in palestra", "dormire", "fare colazione", "guardare la TV", "lavorare", "pranzare", "uscire con gli amici"]
    tm = [("08:00", "Sono le otto."), ("13:00", "È l'una."), ("12:00", "È mezzogiorno."), ("07:30", "Sono le sette e mezza."), ("09:15", "Sono le nove e un quarto."), ("17:45", "Sono le sei meno un quarto.")]
    b.page(f"""{sec(1, "Riscaldamento: la giornata", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi l'azione sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Che ore sono? Scrivi l'ora in lettere.", "4 min")}
{clocks(T, A, tm, "26.5mm")}""",
    29, """<ol><li>A: chiedere subito: <i>A che ora fai colazione? Vai in palestra?</i> Per ora basta la risposta breve: <i>Sì / No / Alle otto</i>.</li>
<li>B: scoprire le regole insieme (tabella a pagina 3): <i>Sono le…</i>, ma <i>È l'una / È mezzogiorno</i>. Nella conversazione si usa 1–12: 17:45 = <i>le sei meno un quarto</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 azioni della giornata con foto · l'ora</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Le giornate di Júlia, Marco e Davide: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>L'ora · verbi in <i>-ire</i> (dormire / finire) · <i>andare</i>, <i>uscire</i> · <i>non… mai</i> · articoli <i>i, gli, le</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Dire l'ora · il suono <i>sc</i></td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Verbi · l'ora · <i>non… mai</i></td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La giornata di Giulia (domande con <i>a che ora?</i>) · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 02–05) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Marco arriva allo studio alle nove e un quarto e pensa di essere in ritardo, ma la riunione è alle dieci. A pranzo Júlia racconta che finisce alle sei e poi va in palestra; Marco non va mai in palestra, la sera esce o guarda la TV. La sera Davide esce con gli amici: dorme fino alle dieci e studia fino all'una, perché «di notte capisce meglio».</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Sono l'una</i> ✗ → <b>È l'una</b>. <i>Io mai vado</i> ✗ → <b>Non vado mai</b>. <i>Io finio</i> ✗ → <b>Io finisco</b>. <i>Io usco</i> ✗ → <b>Io esco</b>. <i>Vado a la palestra</i> ✗ → <b>Vado in palestra</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 05.1 Tre dialoghi (lento e naturale) · Traccia 05.2 L'ora · Traccia 05.3 Il suono <i>sc</i></div>""")

    # Page 2
    tab = [("Marco arriva allo studio alle", "9:15"), ("La riunione è alle", "10:00"), ("Júlia finisce di lavorare alle", "18:00"),
           ("Marco parte da casa alle", "8:30"), ("Júlia apre lo studio alle", "8:00"), ("Davide studia fino all'", "1:00")]
    tl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")}</li>' for i, (a, x) in enumerate(tab)]
    tf = [("Júlia va in palestra dopo il lavoro.", "V"), ("Marco va spesso in palestra.", "F"), ("Marco va allo studio in bicicletta.", "V"), ("Davide la mattina dorme fino alle otto.", "F")]
    tfr = "".join(f'<tr><td>{i+1}. {s}</td><td style="width:24mm;text-align:center;white-space:nowrap">{ch(["V", "F"], a)}</td></tr>' for i, (s, a) in enumerate(tf))
    b.page(f"""{sec(2, "Ascolto: tre giornate diverse", "10 min")}
<p>Júlia parla con Marco allo studio, la mattina e in pausa pranzo. La sera incontra Davide sulle scale.</p>
{audiocard(["05.1 · SLOW", "05.1 · NATURAL"])}
{sub("A", "Ascolta. A che ora? Scrivi l'ora.", "4 min", "05.1 · SLOW")}
{twocol(tl, 4)}
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "4 min", "05.1 · NATURAL")}
<table class="ck" style="margin:0">{tfr}</table>
{sub("C", "Perché Davide studia di notte?", "2 min")}
<div class="wline">{R("Perché dice che di notte capisce meglio.")}</div>""",
    28, """<ol><li>A: versione <b>lenta</b>. Accettare anche le ore in lettere (<i>le nove e un quarto</i>).</li>
<li>B: versione <b>naturale</b>. Correggere le false: 2 → <i>non va mai in palestra</i>; 4 → <i>fino alle dieci</i>. <i>Meno male!</i> = per fortuna.</li>
<li>C: <i>capisco</i> = verbo <i>capire</i> con <i>-isc-</i> (pagina 3). <i>Divertiti!</i> = buon divertimento: solo da capire.</li></ol>""")

    # Page 3
    ore = [("È l'una.", "1:00"), ("Sono le due / le tre…", "2:00 / 3:00"), ("… e un quarto", ":15"), ("… e mezza", ":30"), ("… meno un quarto", ":45 (alle 6 meno un quarto = 5:45)"),
           ("È mezzogiorno. / È mezzanotte.", "12:00 / 24:00")]
    vb = [("io", "dormo", "finisco", "vado", "esco"), ("tu", "dormi", "finisci", "vai", "esci"), ("lui / lei / Lei", "dorme", "finisce", "va", "esce")]
    rules = [("13:00", "È l'una.", "Sono l'una."), ("Una cosa che non faccio:", "Non vado mai in palestra.", "Mai vado in palestra."),
             ("finire, io:", "finisco", "finio"), ("uscire, io:", "esco", "usco")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    to = "".join(f"<tr><td><b>{a}</b></td><td class='small'>{n}</td></tr>" for a, n in ore)
    tv = "".join(f"<tr><td>{p}</td><td><b>{w}</b></td><td><b>{x}</b></td><td><b>{y}</b></td><td><b>{z}</b></td></tr>" for p, w, x, y, z in vb)
    b.page(f"""{sec(3, "Grammatica: l'ora · verbi in -ire · andare e uscire", "10 min")}
{sub("A", "Che ore sono? / A che ora…?", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th>Che ore sono?</th><th></th></tr>{to}</table></div>
<div class="box" style="margin:0"><h4>A CHE ORA?</h4><b>alle</b> otto · <b>alle</b> sei e mezza<br><b>all'</b>una · <b>a</b> mezzogiorno<br><i>fino alle dieci</i> · <i>dalle nove alle sei</i><br>Gli articoli al plurale: <b>il → i</b> (i giorni) · <b>lo / l' → gli</b> (gli amici, gli studenti) · <b>la / l' → le</b> (le ore, le amiche)</div></div>
{sub("B", "Verbi in -ire e verbi irregolari.", "3 min")}
<table style="margin:0"><tr><th></th><th>dormire</th><th>finire (-isc-)</th><th>andare</th><th>uscire</th></tr>{tv}</table>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>NON… MAI</h4>In italiano servono due negazioni: <b>non</b> + verbo + <b>mai</b>. <i>Marco <b>non</b> va <b>mai</b> in palestra.</i> Come <i>dormire</i>: <i>partire, aprire, sentire</i>. Come <i>finire</i>: <i>capire, preferire, pulire</i>.</div>""",
    20, """<ol><li>A: <i>alle</i> = <i>a + le</i> (le preposizioni articolate arrivano nell'unità 7). B: <i>-isc-</i> solo con io, tu, lui/lei.</li>
<li><i>andare</i> e <i>uscire</i> sono irregolari: imparare a memoria. <i>Vado in palestra / in ufficio</i> ma <i>a casa / a scuola</i>.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Sono l'una.</td><td><b>È l'una.</b></td><td>Una = singolare.</td></tr>
<tr><td>Io mai vado in palestra.</td><td><b>Non vado mai in palestra.</b></td><td><i>non</i> + verbo + <i>mai</i>.</td></tr>
<tr><td>Io finio alle sei.</td><td><b>Io finisco alle sei.</b></td><td><i>finire</i> ha <i>-isc-</i>.</td></tr>
<tr><td>Io usco con gli amici.</td><td><b>Io esco con gli amici.</b></td><td><i>uscire</i> è irregolare.</td></tr>
<tr><td>Vado a la palestra.</td><td><b>Vado in palestra.</b></td><td><i>in</i> palestra, <i>in</i> ufficio.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["05.2", "05.3"])}
{sub("A", "L'ora. Ascolta e ripeti.", "2 min", "05.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S052)}</div>
{sub("B", "Il suono sc. Ascolta e ripeti: sco = «sk», sci / sce = un suono solo.", "3 min", "05.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S053)}</div>""",
    38, """<ol><li>Errori: <i>Io mai vado</i> viene dal portoghese. In italiano la doppia negazione è obbligatoria.</li>
<li>4A: dettare 4 orari allo studente (es. 7:30, 1:00, 12:00, 4:45) e poi invertire i ruoli.</li>
<li>4B: <b>esco, finisco, capisco</b> = «sk»; <b>esci, finisci, capisci</b> = suono simile al <i>ch</i> portoghese. Lo stesso verbo cambia suono: <i>esco / esci</i>.</li></ol>""")

    # Page 5
    vw = [("Io", "dormo", "otto ore.", "dormire"), ("Tu a che ora", "finisci", "?", "finire"), ("Marco", "va", "allo studio in bicicletta.", "andare"),
          ("Io la sera", "esco", "con gli amici.", "uscire"), ("Davide non", "capisce", "la domanda.", "capire"), ("Tu", "vai", "in palestra?", "andare")]
    vl = "".join(f'<li>{a} {A(v, "min-width:18mm")} {c} <span class="small">({inf})</span></li>' for a, v, c, inf in vw)
    tm = [("10:30", "Sono le dieci e mezza."), ("15:15", "Sono le tre e un quarto."), ("12:00", "È mezzogiorno."), ("01:00", "È l'una."), ("19:45", "Sono le otto meno un quarto."), ("06:00", "Sono le sei.")]
    nm = [("Marco va in palestra.", "Marco non va mai in palestra."), ("Davide studia la mattina.", "Davide non studia mai la mattina."), ("Io guardo la TV.", "Io non guardo mai la TV.")]
    nl = "".join(f'<li>{a}<div class="wline">{R(x)}</div></li>' for a, x in nm)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con il verbo.", "3 min")}
<ol>{vl}</ol>
{sub("B", "Che ore sono? Scrivi l'ora in lettere.", "3 min")}
{clocks(T, A, tm, "26.5mm")}
{sub("C", "Trasforma con non… mai.", "2 min")}
<ol>{nl}</ol>""",
    25, """<ol><li>B: 15:15 e 19:45: nella conversazione si usa l'orologio da 1 a 12. Accettare anche <i>le quindici e quindici</i> (orario ufficiale: treni, televisione).</li>
<li>C: chiedere poi allo studente: <i>Che cosa non fai mai?</i></li></ol>""")

    # Page 6
    ag = [("6:00", "apre il bar"), ("7:00", "fa colazione al banco"), ("13:30", "pranza"), ("15:00", "va a casa e dorme un po'"), ("17:00", "torna al bar"), ("20:00", "chiude il bar"), ("23:00", "va a dormire")]
    at = "".join(f"<tr><td style='width:28mm'>{A(t, 'min-width:16mm')}</td><td>Giulia {a}.</td></tr>" for t, a in ag)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "La giornata di Giulia. L'insegnante ha gli orari. Fai domande con «A che ora…?» e completa.", "7 min")}
<table style="margin:1mm 0 2mm"><tr><th>A che ora?</th><th>Che cosa fa?</th></tr>{at}</table>
<div class="bank" style="background:#fff">A che ora apre il bar? · A che ora pranza? · Che cosa fa alle tre? · E la sera?</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>A che ora esci di casa la mattina?</li><li>A che ora finisci di lavorare o di studiare?</li><li>Che cosa fai la sera? Esci o resti a casa?</li><li>C'è una cosa che non fai mai?</li></ol>""",
    30, """<ol><li>A: l'insegnante legge gli orari in rosso solo quando lo studente fa la domanda giusta. Poi lo studente racconta la giornata di Giulia: <i>Alle sei apre il bar…</i></li>
<li>B: correggere <i>esco, finisco, non… mai</i>. Chiedere di confrontare la sua giornata con quella di Giulia.</li></ol>""")

    # Page 7
    pc = [("Unità 03", "So dire che lavoro faccio e dove abito."), ("Unità 04", "So ordinare al bar e chiedere il prezzo."),
          ("Unità 05", "So dire e chiedere l'ora."), ("Unità 05", "So parlare della mia giornata."), ("Unità 05", "So usare non… mai.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Sono l'una e mezza.", "È l'una e mezza."), ("Io mai guardo la TV.", "Io non guardo mai la TV."), ("Io finio alle cinque.", "Io finisco alle cinque."),
          ("Marco usce con gli amici.", "Marco esce con gli amici."), ("Vado a la palestra alle sette.", "Vado in palestra alle sette."), ("Tu a che ora va al lavoro?", "Tu a che ora vai al lavoro?")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La mia giornata.</b> Scrivi 5–6 frasi sulla tua giornata con l'ora: <i>Alle sette faccio colazione…</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi lo studente legge la sua giornata e l'insegnante fa domande: <i>E dopo? A che ora pranzi?</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("05.1", "Tre giornate diverse (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("05.2", "L'ora")}
<p>{" ".join(S052)}</p>
{sub("05.3", "Il suono sc")}
<p>{" · ".join(S053)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 05 - La mia giornata")
