# Speak! Essenziale A1 - Unità 08 "In albergo" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 08", audio_json=os.path.join(HERE, "audio_it-a1-unita-08.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la camera doppia", "camera doppia"), ("B", "la camera singola", "camera singola"), ("C", "la chiave", "chiave"), ("D", "la reception", "reception"),
          ("E", "l'ascensore", "ascensore"), ("F", "la colazione", "colazione"), ("G", "la valigia", "valigia"), ("H", "il parcheggio", "parcheggio")]

SCRIPT = [("Narratore", "Dialogo uno. Al telefono con l'albergo."), ("Receptionist", "Hotel Due Torri, buongiorno!"),
          ("Júlia", "Buongiorno. Vorrei prenotare una camera doppia per tre notti, dal dieci al tredici dicembre."), ("Receptionist", "Certo. A che nome?"),
          ("Júlia", "Souza. È per i miei genitori: vengono dal Brasile."), ("Receptionist", "Perfetto. La camera costa novanta euro a notte, con la colazione inclusa."),
          ("Júlia", "C'è il parcheggio?"), ("Receptionist", "No, mi dispiace. Ma ci sono dei parcheggi vicino alla stazione."),
          ("Júlia", "E dall'aeroporto come ci arrivano?"), ("Receptionist", "Ci arrivano in autobus. C'è un autobus ogni dieci minuti."),
          ("Narratore", "Dialogo due. Allo studio."), ("Marco", "Allora, vengono i tuoi genitori?"), ("Júlia", "Sì! Arrivano il dieci, dal Brasile. Vengo anche io all'aeroporto."),
          ("Marco", "E dove dormono?"), ("Júlia", "All'Hotel Due Torri, nel centro."), ("Marco", "Bello! E poi andate a Firenze?"),
          ("Júlia", "Sì, ci andiamo sabato. Luca dice che ci va tutti i giorni!"),
          ("Narratore", "Dialogo tre. In albergo."), ("Receptionist", "Buonasera. Ha una prenotazione?"), ("Júlia", "Sì, a nome Souza. Per i miei genitori."),
          ("Receptionist", "Ecco la chiave: camera ventuno, al secondo piano."), ("Júlia", "C'è l'ascensore?"), ("Receptionist", "Sì, è in fondo al corridoio, accanto alla scala."),
          ("Júlia", "E a che ora è la colazione?"), ("Receptionist", "Dalle sette alle dieci, nella sala al primo piano.")]
S082 = ["al secondo piano", "alla stazione", "dall'aeroporto", "dalle sette alle dieci", "nella sala", "in fondo al corridoio", "sulla scrivania"]
S083 = ["Vorrei prenotare una camera doppia.", "Per tre notti, dal dieci al tredici.", "Quanto costa a notte?", "La colazione è inclusa?", "C'è il parcheggio?", "A che ora è la colazione?"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 08", "In albergo", "Prenotare una camera · <b>al, dal, nel, sul…</b>",
                       [("SAI FARE", "prenotare una camera e chiedere informazioni in albergo"), ("LINGUA", "preposizioni articolate · vengo, vieni, viene · ci (= lì) · dei, degli, delle"),
                        ("PRONUNCIA", "le preposizioni con la doppia: alla, dalla, nella · frasi per prenotare")])
    words = ["il parcheggio", "l'ascensore", "la camera doppia", "la camera singola", "la chiave", "la colazione", "la reception", "la valigia"]
    qs = [("Vuoi sapere il prezzo.", "Quanto costa la camera?"), ("Vuoi mangiare in albergo la mattina.", "La colazione è inclusa?"), ("Arrivi in macchina.", "C'è il parcheggio?"),
          ("La valigia è pesante e la camera è al quarto piano.", "C'è l'ascensore?"), ("Vuoi usare internet.", "C'è il Wi-Fi?")]
    ql = [f'<li value="{i+1}">{q} {R("→ " + a) if T else ""}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: in albergo", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Che cosa chiedi alla reception?", "4 min")}
<ol>{"".join(ql)}</ol>""",
    29, """<ol><li>A: <b>camera doppia</b> = per due persone; <b>singola</b> = per una persona. <b>La camera</b> in albergo (non <i>il quarto</i>!).</li>
<li>B: accettare domande diverse se corrette. Chiedere: <i>Quando viaggi, che cosa è importante per te in albergo?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 parole dell'albergo con foto · domande alla reception</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Júlia prenota l'albergo per i genitori: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Preposizioni articolate · <i>venire</i> · <i>ci</i> di luogo · partitivo plurale</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Preposizioni con la doppia · frasi per prenotare</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Preposizioni · <i>venire</i> · <i>ci</i></td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Telefonata all'albergo (gioco di ruolo in due parti)</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 05–08) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>I genitori di Júlia vengono dal Brasile a dicembre. Júlia telefona all'Hotel Due Torri e prenota una camera doppia per tre notti (90 € a notte, colazione inclusa). Allo studio racconta tutto a Marco: sabato vanno a Firenze. Poi va in albergo a controllare la prenotazione: camera 21, al secondo piano.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Vorrei reservare</i> ✗ → <b>Vorrei prenotare</b>. <i>Il secondo andar</i> ✗ → <b>il secondo piano</b>. <i>Vengo de Brasile</i> ✗ → <b>Vengo dal Brasile</b>. <i>A il piano</i> ✗ → <b>al piano</b>. <i>Inclusiva / incluida</i> ✗ → <b>inclusa</b>.</div>
<div class="box"><h4>PROSSIMA LEZIONE</h4>Il numero 09 è il <b>Ripasso 1</b> (unità 01–08). Avvisare lo studente.</div>
<div class="box"><h4>AUDIO</h4>Traccia 08.1 Tre dialoghi (lento e naturale) · Traccia 08.2 Preposizioni · Traccia 08.3 Prenotare</div>""")

    # Page 2
    fm = [("Nome", "Souza"), ("Camera", "doppia"), ("Notti", "3"), ("Date", "dal 10 al 13 dicembre"), ("Prezzo", "90 € a notte"), ("Colazione", "inclusa"), ("Parcheggio", "no (vicino alla stazione)")]
    fr = "".join(f"<tr><td style='width:34mm'><b>{a}</b></td><td>{A(x, 'min-width:70mm')}</td></tr>" for a, x in fm)
    gp = [("dal dieci", "al", "tredici dicembre"), ("vengono", "dal", "Brasile"), ("vicino", "alla", "stazione"), ("camera ventuno,", "al", "secondo piano"),
          ("in fondo", "al", "corridoio"), ("", "dalle", "sette alle dieci")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:14mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: una camera per i genitori", "10 min")}
<p>A dicembre i genitori di Júlia vengono in Italia. Júlia telefona a un albergo nel centro di Bologna.</p>
{audiocard(["08.1 · SLOW", "08.1 · NATURAL"])}
{sub("A", "Ascolta il dialogo 1. Completa la scheda della prenotazione.", "4 min", "08.1 · SLOW")}
<div class="ad" style="max-width:130mm"><b class="t">HOTEL DUE TORRI · PRENOTAZIONE</b><table style="margin:1mm 0 0">{fr}</table></div>
{sub("B", "Ascolta di nuovo e completa con al, alla, dal, dalle.", "4 min", "08.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Che cosa fanno Júlia e i genitori sabato?", "2 min")}
<div class="wline">{R("Vanno a Firenze.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Le date: <i>dal dieci al tredici</i>; i mesi arrivano con calma, qui basta <i>dicembre</i>.</li>
<li>B: versione <b>naturale</b>. Far notare: <i>al = a + il</i>, <i>alla = a + la</i>, <i>dal = da + il</i>, <i>dalle = da + le</i> (pagina 3). C: <i>ci andiamo</i> = andiamo a Firenze.</li></ol>""")

    # Page 3
    arts = ["il", "lo", "la", "l'", "i", "gli", "le"]
    rows = [("a", ["al", "allo", "alla", "all'", "ai", "agli", "alle"]), ("da", ["dal", "dallo", "dalla", "dall'", "dai", "dagli", "dalle"]),
            ("di", ["del", "dello", "della", "dell'", "dei", "degli", "delle"]), ("in", ["nel", "nello", "nella", "nell'", "nei", "negli", "nelle"]),
            ("su", ["sul", "sullo", "sulla", "sull'", "sui", "sugli", "sulle"])]
    tpa = "<tr><th></th>" + "".join(f"<th style='text-align:center'>{a}</th>" for a in arts) + "</tr>" + "".join(f"<tr><td><b>{p}</b></td>" + "".join(f"<td style='text-align:center'>{x}</td>" for x in xs) + "</tr>" for p, xs in rows)
    vn = [("io", "vengo"), ("tu", "vieni"), ("lui / lei / Lei", "viene"), ("loro", "vengono")]
    tvn = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in vn)
    rules = [("Vengo", "dal Brasile", "de Brasile"), ("La camera è", "al secondo piano", "a il secondo piano"), ("Ci sono", "dei parcheggi", "degli parcheggi"), ("«Vai a Firenze?» «Sì,", "ci vado", "vado ci")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        end = "»" if "«" in s else ""
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b>{end}</li>"
    b.page(f"""{sec(3, "Grammatica: preposizioni articolate · venire · ci", "10 min")}
{sub("A", "Le preposizioni articolate: preposizione + articolo.", "4 min")}
<table style="margin:0;font-size:9pt">{tpa}</table>
<div class="two" style="margin-top:1mm"><div>{sub("B", "venire", "2 min")}<table style="margin:0">{tvn}</table></div>
<div><div class="box" style="margin-top:3mm"><h4>CI = LÌ</h4>«Vai a Firenze?» – «Sì, <b>ci</b> vado sabato.» · «Come arrivano all'albergo?» – «<b>Ci</b> arrivano in autobus.» <b>Ci</b> va prima del verbo.</div>
<div class="box"><h4>DEI, DEGLI, DELLE = ALCUNI</h4>Ci sono <b>dei</b> parcheggi · <b>degli</b> alberghi · <b>delle</b> camere libere.</div></div></div>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>""",
    25, """<ol><li>A: non serve imparare tutta la tabella a memoria: le più frequenti sono <i>al, alla, del, della, nel, nella, dal</i>. Lo studente trova la regola: stessa logica degli articoli (unità 4 e 5).</li>
<li>B: <i>loro vengono</i>: solo da capire (i plurali dei verbi arrivano più avanti).</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Vorrei reservare una camera.</td><td><b>Vorrei prenotare una camera.</b></td><td>In italiano: <i>prenotare</i>.</td></tr>
<tr><td>È al secondo andar.</td><td><b>È al secondo piano.</b></td><td>Il livello = <i>piano</i>.</td></tr>
<tr><td>Vengo de Brasile.</td><td><b>Vengo dal Brasile.</b></td><td><i>da + il = dal</i>.</td></tr>
<tr><td>La camera è a il primo piano.</td><td><b>…è al primo piano.</b></td><td><i>a + il = al</i>.</td></tr>
<tr><td>La colazione è incluida.</td><td><b>La colazione è inclusa.</b></td><td><i>incluso / inclusa</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["08.2", "08.3"])}
{sub("A", "Le preposizioni con la doppia. Ascolta e ripeti: alla, dalla, nella hanno la doppia L.", "2 min", "08.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S082)}</div>
{sub("B", "Prenotare. Ascolta e ripeti.", "3 min", "08.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S083)}</div>""",
    38, """<ol><li>Errori: <i>reservare</i> non esiste in italiano: si dice <i>prenotare</i> (anche al ristorante e dal medico).</li>
<li>4A: <i>al / alla</i>: la seconda ha la doppia L e una vocale in più. Ripetere lentamente <i>a-lla, da-lla, ne-lla</i>.</li>
<li>4B: telefonare in una lingua straniera è difficile: ripetere le frasi più volte, poi fare la telefonata a pagina 6.</li></ol>""")

    # Page 5
    pw = ["al", "alla", "dal", "nella", "dalle", "sul", "dell'", "agli"]
    ps = [("La camera è", "terzo piano."), ("Vado", "stazione."), ("Marco viene", "lavoro alle sette."), ("La colazione è", "sala al primo piano."),
          ("La reception è aperta", "otto alle venti."), ("La chiave è", "tavolo."), ("Il numero", "albergo è 051 22 30."), ("Do la chiave", "amici di Júlia.")]
    pl5 = [f'<li value="{i+1}">{a} {A(pw[i], "min-width:16mm")} {c}</li>' for i, (a, c) in enumerate(ps)]
    vw = [("Io", "vengo", "dal Brasile."), ("Tu", "vieni", "al cinema stasera?"), ("Marco", "viene", "allo studio in bicicletta."), ("Signora, Lei", "viene", "da Roma?")]
    vl = "".join(f'<li>{a} {A(v, "min-width:18mm")} {c}</li>' for a, v, c in vw)
    cq = [("Vai a Firenze sabato?", "Sì, ci vado sabato."), ("Vai in palestra oggi?", "No, non ci vado oggi."), ("Vai allo studio in bicicletta?", "Sì, ci vado in bicicletta.")]
    cl = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in cq)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con la preposizione articolata.", "3 min")}
<div class="bank">agli · al · alla · dal · dalle · dell' · nella · sul</div>
{twocol(pl5, 5)}
{sub("B", "Completa con venire.", "2 min")}
<ol>{vl}</ol>
{sub("C", "Rispondi con ci.", "3 min")}
<ol>{cl}</ol>""",
    22, """<ol><li>A: 3 <i>dal lavoro</i> = da + il; 7 <i>dell'albergo</i> = di + l'; 8 <i>agli amici</i> = a + gli.</li>
<li>C: <i>ci</i> sempre prima del verbo, anche con <i>non</i>: <i>non ci vado</i>.</li></ol>""")

    # Page 6
    form = ["Camera (singola / doppia)", "Notti", "Date", "Prezzo a notte", "Colazione", "Parcheggio / Wi-Fi"]
    frm = "".join(f"<tr><td style='width:46mm'><b>{x}</b></td><td><div class='wline' style='min-height:5mm'></div></td></tr>" for x in form)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Parte 1. Telefoni all'Hotel Bella Vista. L'insegnante è il receptionist. Prenota e completa la scheda.", "6 min")}
<div class="two"><div class="ad"><b class="t">TU · LA TUA SITUAZIONE</b>Viaggi con un amico. Arrivate venerdì e partite domenica. Avete la macchina. Volete la colazione.</div>
<div><table style="margin:0">{frm}</table></div></div>
{sub("B", "Parte 2. Adesso tu sei il receptionist dell'Hotel Roma. L'insegnante telefona.", "6 min")}
<div class="ad" style="max-width:130mm"><b class="t">HOTEL ROMA ★★★ · INFORMAZIONI</b>Camera singola: 70 € · Camera doppia: 95 € (a notte)<br>Colazione: 8 € (dalle 7:00 alle 10:30, nella sala al piano terra)<br>Parcheggio: sì, 15 € al giorno · Wi-Fi: gratis · Ascensore: sì<br>A 5 minuti a piedi dalla stazione</div>
<div class="bank" style="background:#fff">Vorrei prenotare… · Per quante notti? · Dal… al… · Quanto costa a notte? · La colazione è inclusa? · C'è il parcheggio? · A che nome?</div>""",
    32, """<ol><li>Parte 1: l'insegnante risponde come Hotel Bella Vista: camera doppia 110 € a notte con colazione inclusa (dalle 7 alle 10); parcheggio sì, gratis; Wi-Fi sì. Venerdì–domenica = <b>2 notti</b>.</li>
<li>Parte 2: l'insegnante telefona per una camera singola per 3 notti e chiede colazione e parcheggio. Lo studente calcola: 70 € × 3 = 210 € (+ 8 € colazione al giorno).</li></ol>""")

    # Page 7
    pc = [("Unità 05", "So dire l'ora e parlare della mia giornata."), ("Unità 06", "So dire che cosa mi piace."), ("Unità 07", "So chiedere e dare indicazioni."),
          ("Unità 08", "So prenotare una camera in albergo."), ("Unità 08", "So usare al, dal, nel, sul…")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Vorrei reservare una camera singola.", "Vorrei prenotare una camera singola."), ("La camera è a il terzo piano.", "La camera è al terzo piano."),
          ("Vengo de São Paulo.", "Vengo da São Paulo."), ("La colazione è incluida?", "La colazione è inclusa?"), ("Il bagno è in la camera.", "Il bagno è nella camera."), ("«Vai al mare?» «Sì, vado ci.»", "Sì, ci vado.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Un'email all'albergo.</b> Scrivi un'email breve all'Hotel Due Torri: vuoi prenotare una camera (tipo, notti, date) e fai due domande.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: <b>Ripasso 1</b>. Controllare le correzioni all'inizio; l'insegnante risponde all'email come receptionist.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("08.1", "Una camera per i genitori (lento e naturale)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("08.2", "Preposizioni")}
<p>{" · ".join(S082)}</p>
{sub("08.3", "Prenotare")}
<p>{" ".join(S083)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 08 - In albergo")
