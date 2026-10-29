# Speak! Essenziale A1 - Unità 16 "In treno" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 16", audio_json=os.path.join(HERE, "audio_it-a1-unita-16.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il treno", "treno"), ("B", "la stazione", "stazione"), ("C", "il binario", "binario"), ("D", "il biglietto", "biglietto"),
          ("E", "l'autobus", "autobus"), ("F", "la macchina", "macchina"), ("G", "la bicicletta", "bicicletta"), ("H", "l'aereo", "aereo")]

SCRIPT = [("Narratore", "Dialogo uno. Alla biglietteria della stazione di Bologna."), ("Júlia", "Buongiorno, un biglietto per Firenze, per favore."),
          ("Impiegata", "Solo andata o andata e ritorno?"), ("Júlia", "Andata e ritorno. A che ora parte il prossimo treno?"),
          ("Impiegata", "Parte alle dieci e quindici dal binario sei e arriva a Firenze alle dieci e cinquantadue."), ("Júlia", "Perfetto. Quanto costa?"),
          ("Impiegata", "Sono ventisei euro."), ("Júlia", "Ecco a Lei. Grazie!"),
          ("Altoparlante", "Il treno per Firenze Santa Maria Novella delle ore dieci e quindici è in partenza dal binario sei."),
          ("Narratore", "Dialogo due. Al telefono, in treno."), ("Luca", "Pronto, Júlia? Sei in treno?"),
          ("Júlia", "Sì, sono partita alle dieci e quindici. Arrivo alle dieci e cinquantadue."),
          ("Luca", "Benissimo. Ti aspetto al binario. Poi andiamo in centro a piedi: sono dieci minuti."),
          ("Júlia", "Va bene. Il mio treno del ritorno parte alle diciotto e trenta."), ("Luca", "Allora abbiamo quasi otto ore per vedere Firenze!"),
          ("Narratore", "Dialogo tre. Lunedì, allo studio."), ("Marco", "Allora, Júlia, com'è andata a Firenze?"),
          ("Júlia", "Benissimo! Luca mi ha fatto vedere il Duomo e Ponte Vecchio. Siamo andati dappertutto a piedi."), ("Marco", "E il viaggio?"),
          ("Júlia", "All'andata tutto bene, ma il treno del ritorno è partito con quaranta minuti di ritardo!"), ("Marco", "Eh, succede spesso. Benvenuta in Italia!")]
S162 = ["città", "lunedì", "però", "caffè", "perché", "più", "Lunedì vado in città, però prima prendo un caffè."]
S163 = ["Un biglietto per Firenze, per favore.", "Solo andata o andata e ritorno?", "A che ora parte il prossimo treno?", "Da quale binario parte?",
        "A che ora arriva a Firenze?", "Il treno è in ritardo."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 16", "In treno", "Viaggiare in treno · <b>a che ora parte? Dal binario 6</b>",
                       [("SAI FARE", "comprare un biglietto, chiedere orari e binari e dire come ti sposti"),
                        ("LINGUA", "partire da / arrivare a · un biglietto per… · in treno, a piedi · l'ora ufficiale (18:30)"),
                        ("PRONUNCIA", "l'accento finale: città, lunedì, perché · alla biglietteria")])
    words = ["l'aereo", "l'autobus", "la bicicletta", "il biglietto", "il binario", "la macchina", "la stazione", "il treno"]
    rd = [("Da Roma a New York vado", "in aereo"), ("Per fare duecento metri vado", "a piedi"), ("Da Bologna a Firenze vado", "in treno"),
          ("In città, con tante persone, vado", "in autobus"), ("Per fare sport vado al lavoro", "in bici"), ("Con la mia patente vado", "in macchina")]
    rl = [f'<li value="{i+1}">{a} {A(x, "min-width:22mm")}.</li>' for i, (a, x) in enumerate(rd)]
    b.page(f"""{sec(1, "Riscaldamento: i mezzi di trasporto", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le parole sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Come vai? Completa.", "4 min")}
<div class="bank" style="background:#fff">a piedi · in aereo · in autobus · in bici · in macchina · in treno</div>
{twocol(rl, 4)}""",
    24, """<ol><li>A: <i>la macchina</i> = l'auto. <i>Il biglietto</i> si compra alla <b>biglietteria</b> (lo sportello) o alla macchinetta automatica.</li>
<li>B: <b>in</b> + mezzo di trasporto, senza articolo (<i>in treno, in bici</i>), ma <b>a piedi</b>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: mezzi di trasporto e stazione</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Júlia va a Firenze: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>partire / arrivare · da, a, per, in · l'ora ufficiale</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>L'accento finale · alla biglietteria</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il tabellone delle partenze · preposizioni · orari</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Gioco di ruolo alla biglietteria · i tuoi viaggi</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 13–16) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Júlia va a trovare Luca, il fratello di Marco, a Firenze. Alla biglietteria compra un biglietto di andata e ritorno: il treno parte alle 10:15 dal binario 6. In treno telefona a Luca, che la aspetta al binario. Lunedì racconta a Marco la giornata: il Duomo, Ponte Vecchio, tutto a piedi… e quaranta minuti di ritardo al ritorno.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Il treno sale alle otto</i> ✗ → <b>il treno parte alle otto</b>. <i>Un biglietto a Firenze</i> ✗ → <b>un biglietto per Firenze</b>. <i>Vado di autobus</i> ✗ → <b>vado in autobus</b>. <i>Vado in piedi</i> ✗ → <b>vado a piedi</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Negli orari, nei biglietti e negli annunci si usa l'<b>ora ufficiale</b> (24 ore): <i>le diciotto e trenta</i>. Tra amici si dice <i>le sei e mezza</i>. I treni veloci (alta velocità) collegano Bologna e Firenze in meno di 40 minuti; per i treni regionali bisogna spesso <b>convalidare</b> il biglietto prima di salire.</div>
<div class="box"><h4>AUDIO</h4>Traccia 16.1 Tre dialoghi (lento e naturale) · Traccia 16.2 L'accento finale · Traccia 16.3 Alla biglietteria</div>""")

    # Page 2
    tt = [("Biglietto", "andata e ritorno"), ("Partenza da Bologna", "10:15"), ("Binario", "6"), ("Arrivo a Firenze", "10:52"), ("Prezzo", "26 euro"), ("Treno del ritorno", "18:30")]
    ttr = "".join(f"<tr><td style='width:50mm'><b>{a}</b></td><td>{A(x, 'min-width:40mm')}</td></tr>" for a, x in tt)
    vf = [("Luca aspetta Júlia al binario.", "V"), ("Dalla stazione al centro vanno in autobus.", "F"), ("Júlia ha visto il Duomo e Ponte Vecchio.", "V"),
          ("Il treno del ritorno è partito in orario.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: un giorno a Firenze", "10 min")}
<p>Júlia va a Firenze a trovare Luca, il fratello di Marco. Prima compra il biglietto alla stazione di Bologna.</p>
{audiocard(["16.1 · SLOW", "16.1 · NATURAL"])}
{sub("A", "Ascolta il dialogo uno e completa le informazioni del viaggio.", "4 min", "16.1 · SLOW")}
<table style="margin:0">{ttr}</table>
{sub("B", "Ascolta i dialoghi due e tre. Vero (V) o falso (F)?", "4 min", "16.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Quanto tempo ha Júlia per vedere Firenze?", "2 min")}
<div class="wline">{R("Quasi otto ore: arriva alle 10:52 e riparte alle 18:30.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Nell'audio l'ora è detta in modo ufficiale: <i>le dieci e quindici, le diciotto e trenta</i>. Lo studente scrive in cifre.</li>
<li>B: versione <b>naturale</b>. 2: vanno <b>a piedi</b>. 4: è partito con <b>quaranta minuti di ritardo</b>. <i>Dappertutto</i> = in tutti i posti.</li></ol>""")

    # Page 3
    pr = [("partire <b>da</b>", "Il treno parte da Bologna."), ("arrivare <b>a</b>", "Arriva a Firenze alle 10:52."), ("un biglietto <b>per</b>", "Un biglietto per Firenze, per favore."),
          ("<b>dal</b> binario", "Parte dal binario 6."), ("<b>in</b> + mezzo", "in treno, in autobus, in macchina, in aereo, in bici"), ("<b>a</b> piedi", "Andiamo in centro a piedi.")]
    tpr = "".join(f"<tr><td style='width:40mm'>{p}</td><td><i>{e}</i></td></tr>" for p, e in pr)
    oo = [("10:15", "le dieci e quindici", "le dieci e un quarto"), ("18:30", "le diciotto e trenta", "le sei e mezza (di sera)"), ("21:45", "le ventuno e quarantacinque", "le dieci meno un quarto")]
    too = "".join(f"<tr><td><b>{a}</b></td><td>{x}</td><td>{y}</td></tr>" for a, x, y in oo)
    rules = [("Il treno", "parte alle otto", "sale alle otto"), ("Vorrei un biglietto", "per Milano", "a Milano"),
             ("Vado al lavoro", "in autobus", "di autobus"), ("Il treno parte", "dal binario 3", "del binario 3")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: partire e arrivare · preposizioni · l'ora ufficiale", "10 min")}
<div class="two"><div>{sub("A", "Partire e arrivare.", "2 min")}<table style="margin:0"><tr><th></th><th>partire</th><th>arrivare</th></tr>
<tr><td>io</td><td><b>parto</b></td><td><b>arrivo</b></td></tr><tr><td>tu</td><td><b>parti</b></td><td><b>arrivi</b></td></tr>
<tr><td>lui / lei / Lei</td><td><b>parte</b></td><td><b>arriva</b></td></tr><tr><td>noi</td><td><b>partiamo</b></td><td><b>arriviamo</b></td></tr></table>
<p class="small" style="margin-top:1mm">Passato prossimo con <b>essere</b>: <i>sono partita, è arrivato</i>.</p></div>
<div>{sub("C", "L'ora ufficiale (24 ore).", "2 min")}<table style="margin:0"><tr><th></th><th>ufficiale</th><th>tra amici</th></tr>{too}</table>
<p class="small" style="margin-top:1mm"><i>A che ora parte? — <b>Alle</b> 10:15.</i></p></div></div>
{sub("B", "Le preposizioni del viaggio.", "3 min")}
<table style="margin:0">{tpr}</table>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>""",
    24, """<ol><li>A: <i>partire</i> e <i>arrivare</i> usano <b>essere</b> al passato prossimo, con l'accordo (unità 10): <i>Júlia è partita, il treno è partito</i>.</li>
<li>B: <i>da + il = dal</i> (preposizioni articolate, unità 8). <i>Salire</i> = entrare nel treno: <i>salgo sul treno</i>.</li>
<li>C: nella lingua parlata si usano tutte e due le forme; negli annunci e sui biglietti solo l'ora ufficiale.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Il treno sale alle otto.</td><td><b>Il treno parte alle otto.</b></td><td><i>Salire</i> = entrare nel treno.</td></tr>
<tr><td>Un biglietto a Firenze.</td><td><b>Un biglietto per Firenze.</b></td><td>Destinazione del biglietto: <i>per</i>.</td></tr>
<tr><td>Vado di autobus.</td><td><b>Vado in autobus.</b></td><td>Mezzo di trasporto: <i>in</i>.</td></tr>
<tr><td>Vado in piedi.</td><td><b>Vado a piedi.</b></td><td>Eccezione: <i>a piedi</i>.</td></tr>
<tr><td>Il treno arriva in Firenze.</td><td><b>Il treno arriva a Firenze.</b></td><td>Città: <i>a</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["16.2", "16.3"])}
{sub("A", "L'accento finale. Ascolta e ripeti: l'ultima sillaba è forte (CITTÀ, PERCHÉ).", "2 min", "16.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S162)}</div>
{sub("B", "Alla biglietteria. Ascolta e ripeti.", "3 min", "16.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S163)}</div>""",
    38, """<ol><li>Errori: <i>il treno arriva a Firenze</i> (città), ma <i>arriva in stazione, in Toscana</i> (luoghi e regioni).</li>
<li>4A: quando l'ultima sillaba è forte, l'accento <b>si scrive</b>: <i>città, lunedì, però, più</i>. Sulla <i>e</i> può essere aperto (<i>caffè</i>) o chiuso (<i>perché</i>).</li>
<li>4B: far ripetere le domande con l'intonazione che sale (<i>A che ora parte?</i>).</li></ol>""")

    # Page 5
    board = [("9:40", "Milano Centrale", "3", "ritardo 10'"), ("9:55", "Ravenna", "7", "in orario"), ("10:15", "Firenze S.M.N.", "6", "in orario"),
             ("10:30", "Venezia S. Lucia", "2", "ritardo 5'"), ("10:45", "Rimini", "4", "in orario")]
    K = "background:#1F2A30;border-color:#33424A;"
    bd = "".join(f"<tr><td style='{K}color:#F2C14E;font-weight:700'>{o}</td><td style='{K}color:#fff'>{d}</td><td style='{K}color:#fff;text-align:center;font-weight:700'>{bn}</td><td style='{K}color:{'#F2C14E' if 'ritardo' in n else '#9FD8A8'}'>{n}</td></tr>" for o, d, bn, n in board)
    tab = f"""<table style="margin:1mm 0 2mm;background:#1F2A30;color:#fff;border-radius:2mm;overflow:hidden"><tr><th style="background:#11181C;color:#fff">Ora</th><th style="background:#11181C;color:#fff">Destinazione</th><th style="background:#11181C;color:#fff">Binario</th><th style="background:#11181C;color:#fff">Note</th></tr>{bd}</table>"""
    qs = [("A che ora parte il treno per Ravenna?", "Alle 9:55."), ("Da quale binario parte il treno per Rimini?", "Dal binario 4."),
          ("Quali treni sono in ritardo?", "Il treno per Milano e il treno per Venezia."), ("Per Venezia: a che ora parte, e da quale binario?", "Alle 10:30 dal binario 2 (con 5 minuti di ritardo).")]
    ql = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in qs)
    pp = [("Il treno parte", "da", "Bologna."), ("Arriva", "a", "Firenze alle 11."), ("Un biglietto", "per", "Roma, per favore."),
          ("Vado al lavoro", "in", "bici."), ("Torno a casa", "a", "piedi."), ("Parte", "dal", "binario 3.")]
    ppl = [f'<li value="{i+1}">{a} {A(x, "min-width:12mm")} {c}</li>' for i, (a, x, c) in enumerate(pp)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "PARTENZE · Bologna Centrale. Guarda il tabellone e rispondi.", "4 min")}
{tab}
<ol>{ql}</ol>
{sub("B", "Completa con da, dal, a, per, in.", "2 min")}
{twocol(ppl, 4)}""",
    24, """<ol><li>A: far leggere gli orari ad alta voce in modo ufficiale: <i>le nove e quaranta, le dieci e trenta</i>. <i>10'</i> = dieci minuti.</li>
<li>B: 5 <i>a piedi</i> (eccezione); 6 <i>da + il = dal</i>.</li></ol>""")

    # Page 6
    vv = [("A che ora parte il treno?", "alle 8:20"), ("Da quale binario?", "dal binario 5"), ("A che ora arriva a Venezia?", "alle 9:45"),
          ("Quanto costa? (andata e ritorno)", "50 euro (andata: 25 euro)")]
    vvr = "".join(f"<tr><td style='width:66mm'><b>{q}</b></td><td>{A(a, 'min-width:56mm')}</td></tr>" for q, a in vv)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Alla biglietteria. Tu sei il viaggiatore e vuoi andare a Venezia domani mattina. L'insegnante è l'impiegato. Fai le domande e completa.", "4 min")}
<table style="margin:1mm 0 2mm">{vvr}</table>
{sub("B", "Adesso tu sei l'impiegato. L'insegnante vuole andare a Roma. Rispondi con queste informazioni.", "4 min")}
<div class="box"><h4>BOLOGNA → ROMA TERMINI</h4>Partenza: <b>11:05</b>, binario <b>1</b> · Arrivo: <b>13:20</b> · Solo andata: <b>59 euro</b> · Andata e ritorno: <b>118 euro</b></div>
<div class="bank" style="background:#fff">Buongiorno, mi dica. · Solo andata o andata e ritorno? · Sono … euro. · Ecco il biglietto. Buon viaggio!</div>
{sub("C", "I tuoi viaggi. Rispondi all'insegnante.", "4 min")}
<ol style="line-height:1.65"><li>Come vai al lavoro o a scuola? Quanto tempo ci vuole?</li><li>Prendi spesso il treno, l'autobus o l'aereo?</li><li>Racconta un viaggio: dove sei andato/a? Con che mezzo? A che ora sei partito/a?</li></ol>""",
    26, """<ol><li>A: le risposte in rosso sono solo per l'insegnante. L'insegnante usa il <i>Lei</i> (<i>Mi dica</i>, <i>Ecco a Lei</i>).</li>
<li>B: l'insegnante chiede anche <i>Il treno è in orario?</i> Lo studente può inventare: <i>Sì, è in orario</i> / <i>No, ha dieci minuti di ritardo</i>.</li>
<li>C: correggere <i>in treno / a piedi</i> e il passato prossimo con <i>essere</i> (<i>sono partito/a</i>).</li></ol>""")

    # Page 7
    pc = [("Unità 13", "So descrivere la mia giornata tipo."), ("Unità 14", "So presentare la mia famiglia."), ("Unità 15", "So descrivere la mia casa."),
          ("Unità 16", "So comprare un biglietto e chiedere orari e binari."), ("Unità 16", "So dire come mi sposto: in treno, a piedi…")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Il treno sale alle otto.", "Il treno parte alle otto."), ("Vorrei un biglietto a Milano.", "Vorrei un biglietto per Milano."),
          ("Vado al lavoro di autobus.", "Vado al lavoro in autobus."), ("Torno a casa in piedi.", "Torno a casa a piedi."),
          ("Il treno arriva in Firenze alle dieci.", "Il treno arriva a Firenze alle dieci."), ("Il treno parte del binario due.", "Il treno parte dal binario due.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Un viaggio.</b> Scrivi 6 frasi su un viaggio: dove sei andato/a, con che mezzo, a che ora sei partito/a e arrivato/a, che cosa hai visto.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante legge ad alta voce tre orari ufficiali (<i>le quindici e venti…</i>) e lo studente li scrive in cifre.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("16.1", "Un giorno a Firenze (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("16.2", "L'accento finale")}
<p>{" · ".join(S162)}</p>
{sub("16.3", "Alla biglietteria")}
<p>{" ".join(S163)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 16 - In treno")
