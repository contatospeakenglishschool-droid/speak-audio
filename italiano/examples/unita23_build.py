# Speak! Essenziale A1 - Unità 23 "Fai così!" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from parco import themap
setup(band="A1 · UNITÀ 23", audio_json=os.path.join(HERE, "audio_it-a1-unita-23.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "gira a destra", "gira"), ("B", "attraversa", "attraversa"), ("C", "prendi l'autobus", "autobus"), ("D", "mescola", "mescola"),
          ("E", "metti in frigo", "metti"), ("F", "non fumare", "fumare"), ("G", "spegni la luce", "spegni"), ("H", "apri la finestra", "finestra")]

SCRIPT = [("Narratore", "Dialogo uno. Venerdì sera, a casa di Júlia."), ("Júlia", "Giulia, mi insegni a fare il tiramisù? Al Portico ho mangiato un tiramisù buonissimo!"),
          ("Giulia", "Certo, è facile! Prima separa le uova."), ("Júlia", "Così?"),
          ("Giulia", "Brava. Adesso sbatti i tuorli con lo zucchero. Poi aggiungi il mascarpone e mescola bene."), ("Júlia", "E la panna?"),
          ("Giulia", "No, non usare la panna! Il tiramisù vero non ha la panna."), ("Júlia", "Va bene. E adesso?"),
          ("Giulia", "Bagna i savoiardi nel caffè, ma non troppo! Fai uno strato di savoiardi e uno di crema. Alla fine metti il cacao."), ("Júlia", "Lo mangiamo subito?"),
          ("Giulia", "No! Metti il tiramisù in frigo per sei ore. E non toccare!"),
          ("Narratore", "Dialogo due. Sabato, al telefono."), ("Davide", "Pronto, Marco? Dove siete?"),
          ("Marco", "Io e Giulia siamo davanti ai Giardini Margherita. Ma voi dove siete?"), ("Davide", "Allora: entrate dal cancello grande e andate sempre dritto."),
          ("Marco", "Dritto… e poi?"), ("Davide", "Al laghetto girate a sinistra. Passate il bar e cercate un grande albero. Siamo lì, sotto l'albero!"),
          ("Marco", "Portiamo qualcosa da bere?"), ("Davide", "No, non comprate niente, abbiamo tutto. E Júlia ha portato il tiramisù!"), ("Marco", "Allora arriviamo subito!"),
          ("Narratore", "Dialogo tre. Domenica, sulle scale."), ("Signora Rossi", "Davide, scusa, un momento!"), ("Davide", "Buongiorno, signora Rossi. Mi dica."),
          ("Signora Rossi", "Per favore, non lasciare la bicicletta nell'ingresso. Metti la bici in cortile."), ("Davide", "Ha ragione, scusi."),
          ("Signora Rossi", "E butta la plastica il martedì, non il lunedì!"), ("Davide", "Va bene, signora."),
          ("Signora Rossi", "Stasera tu e i tuoi compagni studiate da te, vero? Allora, ragazzi, non fate rumore dopo le undici e chiudete bene il portone."),
          ("Davide", "Certo, signora. Non si preoccupi."), ("Signora Rossi", "Bravo. E la prossima volta porta anche a me un po' di tiramisù!")]
S232 = ["scendi", "spegni", "sbatti", "stai attento", "studia", "Scendi alla prossima fermata e stai attento!"]
S233 = ["Gira a destra e vai sempre dritto.", "Non girare a sinistra.", "Prendete l'autobus tredici.", "Non comprate niente!", "Mescola bene e aspetta.",
        "Metti il tiramisù in frigo."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 23", "Fai così!", "Dare istruzioni · <b>gira a destra, mescola bene, non fate rumore</b>",
                       [("SAI FARE", "dare e capire istruzioni: una ricetta, la strada per arrivare, le regole di casa"),
                        ("LINGUA", "l'imperativo con tu e voi · la forma negativa: non girare, non comprate · fai, vai, stai"),
                        ("PRONUNCIA", "S + consonante: scendi, spegni, stai · dare istruzioni")])
    words = [w for _, w, _ in PHOTOS]
    wh = [("In cucina", "mescola · metti in frigo"), ("Per strada", "gira a destra · attraversa · prendi l'autobus"), ("A casa", "spegni la luce · apri la finestra"),
          ("Il divieto", "non fumare")]
    whl = "".join(f"<tr><td style='width:28mm'><b>{a}</b></td><td>{A(x, 'min-width:90mm')}</td></tr>" for a, x in wh)
    b.page(f"""{sec(1, "Riscaldamento: le istruzioni", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le istruzioni sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.replace("non ", "")))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Dove senti queste istruzioni? Scrivi le istruzioni delle foto nel posto giusto.", "4 min")}
<table style="margin:0">{whl}</table>""",
    28, """<ol><li>A: sono tutte istruzioni all'<b>imperativo</b> con <i>tu</i>: <i>gira, attraversa, prendi, mescola, metti, spegni, apri</i>. <i>Non fumare</i> = divieto (non + infinito): pagina 3.</li>
<li>B: accettare altre soluzioni logiche (<i>spegni la luce</i> anche in ufficio).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: istruzioni in cucina, per strada, a casa</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La ricetta del tiramisù · la strada nel parco · le regole del palazzo</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>imperativo tu / voi · la forma negativa · fai, vai, stai</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>S + consonante · dare istruzioni</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>La mappa del parco · trasformare le istruzioni</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Una ricetta brasiliana · la strada per casa tua · le regole</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Dopo la cena al Portico (unità 22) Júlia vuole imparare il tiramisù: Giulia le spiega la ricetta (senza panna!). Sabato c'è un picnic ai Giardini Margherita: Davide spiega a Marco e Giulia la strada nel parco, e Júlia porta il tiramisù. Domenica la signora Rossi ricorda a Davide le regole del palazzo: la bici in cortile, la plastica il martedì, niente rumore dopo le undici… e un po' di tiramisù anche per lei.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Non gira!</i> ✗ → con <i>tu</i> il negativo è <b>non + infinito</b>: <b>non girare</b>. <i>Gire a destra</i> ✗ → <b>gira</b> (in portoghese <i>vire</i>). <i>Mescla</i> ✗ → <b>mescola</b>. <i>Iscendi</i> ✗ → <b>scendi</b>, senza la «i» davanti. A due persone: <i>non comprare</i> ✗ → <b>non comprate</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il <b>tiramisù</b> è nato in Veneto, a Treviso (la città del nonno di Júlia, unità 02). I <b>Giardini Margherita</b> sono il grande parco di Bologna, con un laghetto. Nei palazzi italiani la <b>raccolta differenziata</b> ha un calendario: la plastica, la carta e il vetro si buttano in giorni diversi. Molti imperativi sono anche parole per parlare: <b>senti, guarda, scusa, dai!</b></div>
<div class="box"><h4>AUDIO</h4>Traccia 23.1 Tre dialoghi (lento e naturale) · Traccia 23.2 S + consonante · Traccia 23.3 Dare istruzioni</div>""")

    # Page 2
    ord_ = [("Bagna i savoiardi nel caffè.", "4"), ("Separa le uova.", "1"), ("Metti il cacao.", "5"), ("Sbatti i tuorli con lo zucchero.", "2"),
            ("Aggiungi il mascarpone e mescola.", "3"), ("Metti il tiramisù in frigo per sei ore.", "6")]
    ordr = "".join(f"<tr><td>{s}</td><td style='width:16mm;text-align:center'>{A(n, 'min-width:9mm')}</td></tr>" for s, n in ord_)
    vf = [("Nel tiramisù di Giulia c'è la panna.", "F"), ("Marco e Giulia comprano qualcosa da bere.", "F"), ("Gli amici sono sotto un grande albero.", "V"),
          ("Davide deve mettere la bici in cortile.", "V"), ("La plastica si butta il lunedì.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: fai così!", "10 min")}
<p>Una ricetta, la strada in un parco e le regole del palazzo.</p>
{audiocard(["23.1 · SLOW", "23.1 · NATURAL"])}
{sub("A", "Dialogo uno. Metti in ordine la ricetta del tiramisù (1–6).", "4 min", "23.1 · SLOW")}
<table style="margin:0">{ordr}</table>
{sub("B", "Dialoghi due e tre. Vero (V) o falso (F)?", "4 min", "23.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa non devono fare Davide e i suoi compagni stasera?", "2 min")}
<div class="wline">{R("Non devono fare rumore dopo le undici.")}</div>""",
    30, """<ol><li>A: versione <b>lenta</b>. I <i>tuorli</i> = la parte gialla dell'uovo; i <i>savoiardi</i> = i biscotti del tiramisù.</li>
<li>B: versione <b>naturale</b>. 2: <b>non comprate niente</b>. 5: la plastica <b>il martedì</b>. La signora Rossi dà del <i>tu</i> a Davide (è giovane), Davide le dà del <i>Lei</i> (<i>mi dica, scusi, non si preoccupi</i>).</li></ol>""")

    # Page 3
    ver = [("girare", "gir<b>a</b>!", "gir<b>ate</b>!"), ("prendere", "prend<b>i</b>!", "prend<b>ete</b>!"), ("sentire", "sent<b>i</b>!", "sent<b>ite</b>!"),
           ("fare", "<b>fai</b>!", "<b>fate</b>!"), ("andare", "<b>vai</b>!", "<b>andate</b>!"), ("stare", "<b>stai</b>!", "<b>state</b>!")]
    tver = "".join(f"<tr><td><b>{a}</b></td><td>{x}</td><td>{y}</td></tr>" for a, x, y in ver)
    neg = [("tu", "non + infinito", "Non <b>girare</b>! · Non <b>usare</b> la panna! · Non <b>toccare</b>!"), ("voi", "non + forma voi", "Non <b>girate</b>! · Non <b>comprate</b> niente! · Non <b>fate</b> rumore!")]
    tneg = "".join(f"<tr><td style='width:12mm'><b>{a}</b></td><td style='width:34mm'>{x}</td><td>{y}</td></tr>" for a, x, y in neg)
    rules = [("Bruno, ", "gira", "gire", " a sinistra!"), ("Ragazzi, ", "prendete", "prendi", " l'autobus 13."), ("Júlia, non ", "usare", "usa", " la panna!"),
             ("Marco e Giulia, non ", "comprate", "comprare", " niente!"), ("Davide, ", "metti", "mette", " la bici in cortile."), ("Giulia, ", "vai", "va", " sempre dritto.")]
    rl = "".join(f"<li>{a}<i>{ch([r, w] if i % 2 == 0 else [w, r], r)}</i>{z}</li>" for i, (a, r, w, z) in enumerate(rules))
    b.page(f"""{sec(3, "Grammatica: l'imperativo", "10 min")}
{sub("A", "L'imperativo con tu e voi.", "4 min")}
<table style="margin:0"><tr><th style="width:30mm"></th><th>tu</th><th>voi</th></tr>{tver}</table>
<p class="small" style="margin-top:1mm"><b>-are → -a</b> (gira, mescola, aspetta) · <b>-ere / -ire → -i</b> (prendi, metti, apri) · con <i>voi</i> = come il presente: <i>girate, prendete, aprite</i></p>
{sub("B", "La forma negativa.", "3 min")}
<table style="margin:0">{tneg}</table>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
{twocol([f'<li value="{i+1}">' + x[4:] for i, x in enumerate(rl.split("</li>")[:-1])], 4)}""",
    28, """<ol><li>A: l'imperativo con <i>tu</i> dei verbi in <i>-are</i> finisce in <b>-a</b> (non in <i>-i</i>!): <i>gira, mangia</i>. Con <i>voi</i> è uguale al presente. <i>Fai, vai, stai</i> si scrivono anche <i>fa', va', sta'</i>.</li>
<li>B: con <i>tu</i> il negativo non usa l'imperativo ma l'<b>infinito</b>: <i>non girare</i>. Con <i>voi</i> basta mettere <i>non</i>.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Non gira a destra!</td><td><b>Non girare a destra!</b></td><td>Tu negativo: <i>non + infinito</i>.</td></tr>
<tr><td>Gire a sinistra.</td><td><b>Gira a sinistra.</b></td><td>Verbi in <i>-are</i>: <i>-a</i>.</td></tr>
<tr><td>Mescla bene.</td><td><b>Mescola bene.</b></td><td>Il verbo è <i>mescolare</i>.</td></tr>
<tr><td>Ragazzi, non comprare niente!</td><td><b>Ragazzi, non comprate niente!</b></td><td>A più persone: <i>voi</i>.</td></tr>
<tr><td>Pega l'autobus 13.</td><td><b>Prendi l'autobus 13.</b></td><td><i>pegar</i> → <i>prendere</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["23.2", "23.3"])}
{sub("A", "S + consonante. Ascolta e ripeti: non mettere la «i» davanti: Scendi (non «iscendi»).", "2 min", "23.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S232)}</div>
{sub("B", "Dare istruzioni. Ascolta e ripeti.", "3 min", "23.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S233)}</div>""",
    40, """<ol><li>Errori: l'influenza del portoghese è forte con <i>vire, pegue, misture</i>. Fare ripetere la forma corretta con il gesto (girare la mano, mescolare).</li>
<li>4A: i brasiliani dicono spesso «isscendi», «isstudia». Far tenere la S lunga, come un serpente, e poi la consonante: <i>sss-cendi</i>. Davanti a <i>b, d, g, v</i> la S è sonora: <i>sbatti</i>.</li></ol>""")

    # Page 5
    dirs = [("Entrate dal cancello e andate sempre dritto. Al laghetto girate a sinistra e passate il bar.", "A"),
            ("Entra dal cancello e gira subito a destra.", "D"), ("Vai sempre dritto, passa il laghetto e continua fino alla fine.", "C"),
            ("Vai dritto e al laghetto gira a destra. Vai fino alla fine.", "B")]
    dl = [f'<li value="{i+1}">{s} {A(x, "min-width:9mm")}</li>' for i, (s, x) in enumerate(dirs)]
    tr = [("Gira a destra.", "voi", "Girate a destra."), ("Prendi l'autobus.", "voi", "Prendete l'autobus."), ("Usa la panna.", "tu, negativo", "Non usare la panna."),
          ("Tocca il tiramisù.", "tu, negativo", "Non toccare il tiramisù."), ("Fate rumore.", "voi, negativo", "Non fate rumore.")]
    trl = "".join(f"<li>{a} <span class='small'>({n})</span> → {A(x, 'min-width:46mm')}</li>" for a, n, x in tr)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "La mappa del parco. Leggi le istruzioni: dove arrivi? Scrivi la lettera.", "3 min")}
<div style="margin:1mm 0 2mm">{themap(150)}</div>
<ol>{"".join(dl)}</ol>
{sub("B", "Bruno è al cancello. Scrivi le istruzioni (tu) per arrivare al bar.", "2 min")}
<div class="wline">{R("Entra dal cancello e vai dritto. Al laghetto gira a sinistra: il bar è lì.")}</div>
{sub("C", "Trasforma le istruzioni.", "3 min")}
<ol>{trl}</ol>""",
    22, """<ol><li>A: A = il grande albero degli amici (dialogo due), B = il campo da tennis, C = la fontana, D = i giochi per i bambini.</li>
<li>B: accettare altre istruzioni corrette. C: ricordare che con <i>voi</i> il negativo è solo <i>non</i> + la forma normale.</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Una ricetta brasiliana. Spiega all'insegnante come si fa un piatto facile (il brigadeiro, la tapioca, il pão de queijo…). Usa l'imperativo con tu.", "5 min")}
<div class="bank" style="background:#fff">prima · poi · adesso · alla fine &nbsp;|&nbsp; prendi · metti · aggiungi · mescola · aspetta · non usare…</div>
{sub("B", "La strada per casa tua. Dall'ultima fermata dell'autobus o della metro, spiega all'insegnante come arrivare a casa tua.", "4 min")}
<p class="small">Scendi alla fermata… · attraversa la strada · gira a destra / a sinistra · vai sempre dritto · suona il campanello…</p>
{sub("C", "Le regole. Scrivi tre regole per i tuoi figli, i tuoi colleghi o il tuo gatto (tu o voi). Poi leggile all'insegnante.", "3 min")}
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    26, """<ol><li>A: l'insegnante fa domande (<i>E poi? Quanto zucchero?</i>) e ripete gli imperativi giusti. Correggere <i>-a</i> / <i>-i</i>.</li>
<li>C: esempi: <i>Ragazzi, non giocate in casa! Gatto, non dormire sul divano!</i> Si può ridere: è il momento giusto per il negativo.</li></ol>""")

    # Page 7
    pc = [("Unità 22", "So ordinare al ristorante."), ("Unità 23", "So capire e dare una ricetta."), ("Unità 23", "So spiegare la strada."),
          ("Unità 23", "So dire le regole con tu e voi."), ("Unità 23", "So fare l'imperativo negativo.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Non gira a sinistra!", "Non girare a sinistra!"), ("Bruno, prende l'autobus 13!", "Bruno, prendi l'autobus 13!"), ("Ragazzi, non usare il telefono!", "Ragazzi, non usate il telefono!"),
          ("Gire alla seconda strada.", "Gira alla seconda strada."), ("Júlia, mescla bene!", "Júlia, mescola bene!"), ("Davide, non lascia la bici qui!", "Davide, non lasciare la bici qui!")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La tua ricetta.</b> Scrivi la ricetta del tuo piatto preferito (6 istruzioni con tu). Usa prima, poi, adesso, alla fine.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge la ricetta e l'insegnante la «prepara» con i gesti. Poi si passa allo sport (unità 24).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("23.1", "Fai così! (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("23.2", "S + consonante")}
<p>{" · ".join(S232)}</p>
{sub("23.3", "Dare istruzioni")}
<p>{" ".join(S233)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 23 - Fai così")
