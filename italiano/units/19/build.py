# Speak! Essenziale A1 - Unità 19 "Ti va di...?" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 19", audio_json=os.path.join(HERE, "audio_it-a1-unita-19.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "andare al cinema", "cinema"), ("B", "vedere una partita", "partita"), ("C", "fare un aperitivo", "aperitivo"), ("D", "andare a una festa", "festa"),
          ("E", "andare a un concerto", "concerto"), ("F", "vedere una mostra", "mostra"), ("G", "fare una passeggiata", "passeggiata"), ("H", "cenare fuori", "cena")]

SCRIPT = [("Narratore", "Dialogo uno. Bruno è a Bologna. Marco telefona a Júlia."), ("Marco", "Ciao, Júlia! Ti va di andare al cinema venerdì sera, con Bruno?"),
          ("Júlia", "Mi dispiace, venerdì non posso: devo lavorare fino a tardi. Ma sabato sono libera."),
          ("Marco", "Allora sabato volete venire a una partita di basket? Bologna è la città del basket!"),
          ("Júlia", "Volentieri! Bruno vuole proprio vedere una partita. A che ora ci vediamo?"), ("Marco", "Alle otto, davanti al palazzetto."), ("Júlia", "Perfetto, a sabato!"),
          ("Narratore", "Dialogo due. Al bar."), ("Júlia", "Giulia, giovedì sera facciamo un aperitivo a casa mia. Vuoi venire?"),
          ("Giulia", "Che gentile, grazie! Ma giovedì non posso: devo chiudere il bar tardi. Possiamo fare mercoledì?"),
          ("Júlia", "Mercoledì va benissimo. Alle sette?"), ("Giulia", "Alle sette. Porto io il vino!"),
          ("Narratore", "Dialogo tre. Stasera, sulle scale."), ("Davide", "Júlia! Ti va di venire a una festa stasera? Viene anche la mia band."),
          ("Júlia", "Grazie, Davide, ma stasera non posso. Sono stanca e domani devo alzarmi alle sei e mezza."), ("Davide", "Dai! Puoi venire solo per un'ora!"),
          ("Júlia", "No, davvero. Magari un'altra volta. Ma Bruno vuole venire, sicuramente!"), ("Davide", "Benissimo, allora passo a prendere Bruno alle dieci.")]
S192 = ["posso, possiamo", "devo, dobbiamo", "voglio, vogliamo", "puoi, vuoi", "possono, vogliono", "Vogliamo uscire, ma dobbiamo lavorare."]
S193 = ["Ti va di andare al cinema?", "Vuoi venire a cena da me?", "Volentieri! A che ora ci vediamo?", "Mi dispiace, non posso: devo lavorare.", "Magari un'altra volta.",
        "Ci vediamo alle otto davanti al cinema."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 19", "Ti va di…?", "Invitare, accettare e rifiutare · <b>volentieri! / mi dispiace, non posso</b>",
                       [("SAI FARE", "invitare una persona, accettare o rifiutare con gentilezza e fissare un appuntamento"),
                        ("LINGUA", "volere, potere, dovere + infinito · ti va di…? · ci vediamo alle… davanti a…"),
                        ("PRONUNCIA", "i verbi modali: possiamo, dobbiamo, vogliamo · invitare e rispondere")])
    words = [w for _, w, _ in PHOTOS]
    rs = [("Volentieri!", "✓"), ("Mi dispiace, non posso.", "✗"), ("Che bella idea!", "✓"), ("Magari un'altra volta.", "✗"), ("Perfetto, a sabato!", "✓"), ("Purtroppo devo lavorare.", "✗")]
    rl = [f'<li value="{i+1}">{s} &nbsp; {ch(["✓", "✗"], a)}</li>' for i, (s, a) in enumerate(rs)]
    b.page(f"""{sec(1, "Riscaldamento: il tempo libero", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le espressioni sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Un amico ti invita. Accetti (✓) o rifiuti (✗)?", "4 min")}
{twocol(rl, 4)}""",
    24, """<ol><li>A: dopo la scrittura, l'insegnante chiede: <i>Ti va di andare al cinema?</i> Lo studente risponde liberamente.</li>
<li>B: <i>Magari un'altra volta</i> è un modo gentile di dire di no. In italiano un «no» diretto senza spiegazione sembra scortese.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto del tempo libero · accettare o rifiutare</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Tre inviti: al telefono, al bar, sulle scale</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>volere, potere, dovere + infinito · invitare, rispondere, fissare l'appuntamento</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>I verbi modali · invitare e rispondere</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>I verbi modali · l'agenda di Júlia · di o niente?</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Inviti con l'agenda · la tua settimana</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Bruno è a Bologna. Marco invita Júlia e Bruno al cinema venerdì, ma Júlia deve lavorare: allora vanno sabato a una partita di basket (alle otto, davanti al palazzetto). Júlia invita Giulia a un aperitivo giovedì; Giulia non può e propone mercoledì. Davide invita Júlia a una festa: lei è stanca e dice di no… ma Bruno va con Davide.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Posso di venire?</i> ✗ → <b>Posso venire?</b> (modale + infinito, senza <i>di</i>). <i>Ti va uscire?</i> ✗ → <b>Ti va di uscire?</b> <i>Doviamo</i> ✗ → <b>dobbiamo</b>. <i>Sì, voglio!</i> come risposta a un invito ✗ → <b>Sì, volentieri!</b></div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>L'<b>aperitivo</b> (dalle 18 alle 20 circa) è un momento sociale importante: un drink con qualcosa da mangiare, al bar o a casa. Bologna è chiamata «Basket City»: ha due squadre storiche di basket. Per insistere gli italiani dicono <b>Dai!</b>; per rifiutare con gentilezza, <b>Magari un'altra volta</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 19.1 Tre dialoghi (lento e naturale) · Traccia 19.2 I verbi modali · Traccia 19.3 Invitare e rispondere</div>""")

    # Page 2
    ag = [("Venerdì", "Júlia deve lavorare fino a tardi"), ("Sabato, alle 20:00", "partita di basket con Marco, davanti al palazzetto"),
          ("Giovedì", "Giulia deve chiudere il bar tardi"), ("Mercoledì, alle 19:00", "aperitivo con Giulia a casa di Júlia"), ("Stasera, alle 22:00", "Davide passa a prendere Bruno per la festa")]
    agr = "".join(f"<tr><td style='width:40mm'><b>{a}</b></td><td>{A(x, 'min-width:96mm')}</td></tr>" for a, x in ag)
    vf = [("Marco invita Júlia al cinema venerdì sera.", "V"), ("Júlia accetta il cinema.", "F"), ("Giulia può venire giovedì.", "F"), ("Júlia va alla festa di Davide.", "F"), ("Bruno va alla festa.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: tre inviti", "10 min")}
<p>Bruno, il fratello di Júlia, è a Bologna. Tutti vogliono uscire con loro… ma non è sempre facile trovare il giorno giusto.</p>
{audiocard(["19.1 · SLOW", "19.1 · NATURAL"])}
{sub("A", "Ascolta e completa l'agenda.", "4 min", "19.1 · SLOW")}
<table style="margin:0">{agr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "4 min", "19.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Perché Júlia non va alla festa?", "2 min")}
<div class="wline">{R("Perché è stanca e domani deve alzarsi alle sei e mezza.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi. <i>Il palazzetto</i> = il palazzo dello sport.</li>
<li>B: versione <b>naturale</b>. 2: Júlia <b>non può</b> (deve lavorare). 3: Giulia propone <b>mercoledì</b>. <i>Passo a prendere Bruno</i> = vengo a casa tua e andiamo insieme.</li></ol>""")

    # Page 3
    mv = [("io", "voglio", "posso", "devo"), ("tu", "vuoi", "puoi", "devi"), ("lui / lei / Lei", "vuole", "può", "deve"), ("noi", "vogliamo", "possiamo", "dobbiamo"),
          ("voi", "volete", "potete", "dovete"), ("loro", "vogliono", "possono", "devono")]
    tmv = "".join(f"<tr><td>{p}</td><td><b>{a}</b></td><td><b>{bb}</b></td><td><b>{c}</b></td></tr>" for p, a, bb, c in mv)
    ex = [("Invitare", "Ti va di + infinito? · Vuoi + infinito? · Perché non…?"), ("Accettare", "Volentieri! · Che bella idea! · Sì, va bene! · Perfetto!"),
          ("Rifiutare", "Mi dispiace, non posso: devo… · Purtroppo… · Peccato! · Magari un'altra volta."),
          ("Fissare l'appuntamento", "A che ora ci vediamo? · Dove ci vediamo? · Ci vediamo alle otto davanti al cinema.")]
    tex = "".join(f"<tr><td style='width:36mm'><b>{a}</b></td><td><i>{x}</i></td></tr>" for a, x in ex)
    rules = [("Venerdì", "non posso venire", "non posso di venire"), ("", "Ti va di uscire?", "Ti va uscire?"), ("Domani noi", "dobbiamo lavorare", "doviamo lavorare"),
             ("I miei amici", "vogliono venire", "vuolono venire")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: volere, potere, dovere · invitare e rispondere", "10 min")}
<div class="two"><div>{sub("A", "Volere, potere, dovere + infinito.", "3 min")}
<table style="margin:0"><tr><th></th><th>volere</th><th>potere</th><th>dovere</th></tr>{tmv}</table></div>
<div><div class="box" style="margin-top:6mm"><h4>COME SI USANO</h4>Modale + <b>infinito</b>, senza preposizione:<br><i>Voglio <b>vedere</b> una partita.<br>Non posso <b>venire</b>.<br>Devo <b>lavorare</b> fino a tardi.</i><br><br>Con un verbo riflessivo:<br><i>Domani devo <b>alzarmi</b> presto.</i></div></div></div>
{sub("B", "Invitare, accettare, rifiutare.", "4 min")}
<table style="margin:0">{tex}</table>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>""",
    24, """<ol><li>A: <i>dovere</i> al singolare è già nell'unità 10; qui si aggiunge il plurale. Attenzione alle forme irregolari: <i>vogliamo, possiamo, dobbiamo, può</i>.</li>
<li>B: <b>Ti va di</b> + infinito vuole la preposizione <i>di</i>; <b>vuoi</b> + infinito no. <i>Ti va?</i> = hai voglia?</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Posso di venire con Bruno?</td><td><b>Posso venire con Bruno?</b></td><td>Modale + infinito, senza <i>di</i>.</td></tr>
<tr><td>Ti va uscire stasera?</td><td><b>Ti va di uscire stasera?</b></td><td><i>Ti va di</i> + infinito.</td></tr>
<tr><td>Noi doviamo lavorare.</td><td><b>Noi dobbiamo lavorare.</b></td><td>Forma irregolare.</td></tr>
<tr><td>— Vuoi venire? — Sì, voglio!</td><td><b>— Sì, volentieri!</b></td><td>Risposta gentile a un invito.</td></tr>
<tr><td>Ci vediamo in frente al bar.</td><td><b>Ci vediamo davanti al bar.</b></td><td><i>davanti a</i> (unità 15).</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["19.2", "19.3"])}
{sub("A", "I verbi modali. Ascolta e ripeti: la doppia (POSSO, DOBBIAMO) e GLI (VOGLIO).", "2 min", "19.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S192)}</div>
{sub("B", "Invitare e rispondere. Ascolta e ripeti.", "3 min", "19.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S193)}</div>""",
    38, """<ol><li>Errori: <i>Sì, voglio!</i> è corretto ma suona troppo diretto come risposta a un invito; <i>volentieri</i> è più naturale.</li>
<li>4A: <i>posso / poso</i>: senza la doppia cambia la parola. <i>Voglio</i>: GLI come in <i>famiglia</i> (unità 10).</li>
<li>4B: far ripetere <i>Volentieri!</i> con entusiasmo e <i>Mi dispiace…</i> con un tono più basso.</li></ol>""")

    # Page 5
    mw = [("Noi", "dobbiamo", "partire alle otto.", "dovere"), ("Voi", "potete", "venire sabato?", "potere"), ("Loro", "vogliono", "vedere la partita.", "volere"),
          ("Tu", "vuoi", "un caffè?", "volere"), ("Marco non", "può", "venire alle nove.", "potere"), ("Io", "devo", "studiare stasera.", "dovere")]
    mwl = [f'<li value="{i+1}">{a} {A(v, "min-width:20mm")} {c} <span class="small">({n})</span></li>' for i, (a, v, c, n) in enumerate(mw)]
    ag5 = [("lunedì", "palestra alle 19"), ("martedì", "libera"), ("mercoledì", "aperitivo con Giulia"), ("giovedì", "lavoro fino alle 21"), ("venerdì", "libera"), ("sabato", "basket con Marco")]
    agc = "".join(f"<td style='text-align:center'><b>{d}</b><br><span class='small'>{x}</span></td>" for d, x in ag5)
    qq = [("Ti va di andare al cinema lunedì?", "Mi dispiace, lunedì non posso: devo andare in palestra."), ("Vuoi cenare da me martedì?", "Volentieri! Martedì sono libera."),
          ("Possiamo vederci giovedì sera?", "Purtroppo giovedì devo lavorare fino alle nove."), ("Ti va di fare una passeggiata venerdì?", "Che bella idea! Venerdì va benissimo.")]
    ql = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in qq)
    dn = [("Ti va", "di", "venire?"), ("Vuoi", "—", "venire?"), ("Posso", "—", "portare Bruno?"), ("Hai voglia", "di", "uscire?")]
    dnl = [f'<li value="{i+1}">{a} {A(x, "min-width:10mm")} {c}</li>' for i, (a, x, c) in enumerate(dn)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con volere, potere o dovere.", "3 min")}
{twocol(mwl, 4)}
{sub("B", "Guarda l'agenda di Júlia. Rispondi agli inviti come Júlia.", "4 min")}
<table style="margin:1mm 0 2mm"><tr>{agc}</tr></table>
<ol>{ql}</ol>
{sub("C", "Di o niente (—)?", "1 min")}
{twocol(dnl, 3)}""",
    22, """<ol><li>B: accettare altre risposte corrette. Per rifiutare, lo studente deve dare una scusa con <i>devo…</i></li>
<li>C: <i>ti va di, hai voglia di</i> + infinito; <i>vuoi, posso, devo</i> + infinito senza preposizione.</li></ol>""")

    # Page 6
    inv = [("andare al cinema", "giovedì sera", "No: giovedì devo andare dal dentista."), ("fare un aperitivo", "venerdì alle 19", "Sì, volentieri! Dove ci vediamo?"),
           ("vedere una mostra", "sabato mattina", "No: sabato lavoro fino alle 14. Possiamo andare nel pomeriggio?")]
    invr = "".join(f"<tr><td><b>{a}</b></td><td>{d}</td><td>{A(r, 'min-width:62mm')}</td></tr>" for a, d, r in inv)
    days = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
    wk = "".join(f"<td style='text-align:center;height:24mm;vertical-align:top'><b>{d}</b></td>" for d in days)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Invita l'insegnante. Usa ti va di…? / vuoi…? L'insegnante risponde: scrivi la risposta. Poi fissate l'appuntamento.", "5 min")}
<table style="margin:1mm 0 2mm"><tr><th>Che cosa?</th><th>Quando?</th><th>Risposta dell'insegnante</th></tr>{invr}</table>
{sub("B", "La tua settimana. Scrivi che cosa devi fare. Poi l'insegnante ti invita: accetta o rifiuta con una scusa.", "5 min")}
<table style="margin:1mm 0 2mm"><tr>{wk}</tr></table>
{sub("C", "Rispondi all'insegnante.", "2 min")}
<ol style="line-height:1.65"><li>Che cosa fai di solito il venerdì sera?</li><li>Quando un amico ti invita e non vuoi andare, che cosa dici?</li></ol>""",
    26, """<ol><li>A: le risposte in rosso sono solo per l'insegnante. Dopo il sì, lo studente chiede: <i>A che ora ci vediamo? Dove?</i></li>
<li>B: l'insegnante fa almeno tre inviti; lo studente deve rifiutare almeno una volta con <i>Mi dispiace, non posso: devo…</i></li></ol>""")

    # Page 7
    pc = [("Unità 16", "So comprare un biglietto del treno."), ("Unità 17", "So parlare del tempo e dire le date."), ("Unità 19", "So invitare una persona."),
          ("Unità 19", "So accettare o rifiutare con gentilezza."), ("Unità 19", "So usare volere, potere, dovere + infinito.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Posso di venire domani?", "Posso venire domani?"), ("Ti va andare al cinema?", "Ti va di andare al cinema?"), ("Noi doviamo lavorare sabato.", "Noi dobbiamo lavorare sabato."),
          ("Loro non possano venire.", "Loro non possono venire."), ("Ci vediamo in frente al bar.", "Ci vediamo davanti al bar."), ("Voi vuolete un caffè?", "Voi volete un caffè?")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Due messaggi.</b> Scrivi un messaggio per invitare un amico (che cosa, quando, dove, a che ora). Poi scrivi la risposta dell'amico: rifiuta con gentilezza e proponi un altro giorno.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante invita lo studente a fare qualcosa nel fine settimana e lo studente risponde senza guardare il libro.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("19.1", "Tre inviti (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("19.2", "I verbi modali")}
<p>{" · ".join(S192)}</p>
{sub("19.3", "Invitare e rispondere")}
<p>{" ".join(S193)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 19 - Ti va di")
