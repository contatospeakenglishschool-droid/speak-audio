# Speak! Essenziale A1 - Unità 28 "Il ritorno" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from chat import chat
setup(band="A1 · UNITÀ 28", audio_json=os.path.join(HERE, "audio_it-a1-unita-28.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la valigia", "valigia"), ("B", "l'aeroporto", "aeroporto"), ("C", "la cena", "cena"), ("D", "il nuoto", "nuoto"),
          ("E", "la spiaggia", "spiaggia"), ("F", "il regalo", "regalo"), ("G", "le chiavi", "chiavi"), ("H", "le piante", "piante")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-28"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["28.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S282 = [x.split(": ", 1)[1] for x in _r["28.2 Ripeti perché per quando"].split("\n")]
S283 = [x.split(": ", 1)[1] for x in _r["28.3 Domanda o risposta"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split()[-1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 28", "Il ritorno", "Settembre: si torna a Bologna · <b>perché…, per + infinito, quando…</b>",
                       [("SAI FARE", "raccontare le vacanze e spiegare perché fai una cosa e a che cosa serve"),
                        ("LINGUA", "Perché sei tornata? Perché Bruno arriva. · Viene per studiare. · Quando gioco, la metto."),
                        ("PRONUNCIA", "perché?, per, quando · domanda o risposta?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: bentornata!", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Dove sei andato/a in vacanza l'ultima volta? Con chi?</li><li>Che cosa metti in valigia? Che cosa porti come regalo?</li><li>Quando parti, chi dà l'acqua alle tue piante?</li></ol>""",
    22, """<ol><li>A: ogni foto racconta il ritorno di Júlia: la valigia, l'aeroporto, la cena in famiglia, il nuoto (promesso nell'unità 24), le chiavi e le piante (unità 23).</li>
<li>B: ripasso del passato prossimo (unità 11 e 21). Ascoltare se lo studente usa già <i>perché</i> e <i>per</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il ritorno dalle vacanze</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Al bar con Giulia · allo studio con Marco · le chiavi di Davide</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>perché + frase · per + infinito · quando + frase</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>perché, per, quando · domanda o risposta?</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Perché o per? · la chat di Bruno</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Le tue vacanze · perché impari l'italiano?</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio settembre: dopo un mese a Belo Horizonte con la famiglia, Júlia torna a Bologna prima della riapertura dello studio, perché sabato arriva Bruno: viene per studiare all'università e all'inizio abita da lei. Marco è tornato dalla Sardegna (in barca con alcuni amici) e ha una notizia: suo fratello Luca si sposa a fine settembre a Firenze, e anche Júlia riceverà l'invito (unità 35). La sera Davide le riporta le chiavi: è passato ogni due giorni per dare l'acqua alle piante. Júlia gli regala una maglietta della nazionale brasiliana. Le unità 28–35 raccontano le prime settimane di Bruno a Bologna, prima del matrimonio (A2 Ponte 01).</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese <i>para</i> + infinito diventa <b>per</b> + infinito: <i>vim para estudar</i> → <b>vengo per studiare</b> (non <i>vengo a studiare</i> con questo senso, né <i>para</i>). <i>Por que? / Porque</i> sono in italiano una sola parola: <b>perché</b>, con l'accento acuto (é). Dopo <i>quando</i> non si usa il futuro del congiuntivo portoghese (<i>quando eu jogar</i>): <b>quando gioco</b> (presente).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia agosto è il mese delle vacanze: molte città si svuotano, molti negozi e uffici chiudono (le <i>ferie</i>) e la gente va al mare o in montagna. A settembre si torna al lavoro e a scuola: il <b>rientro</b>. Le università cominciano tra fine settembre e ottobre. La <b>Sardegna</b> è famosa per il mare trasparente: tanti italiani affittano una barca per vedere le spiagge che si raggiungono solo dal mare.</div>
<div class="box"><h4>AUDIO</h4>Traccia 28.1 Tre dialoghi (lento e naturale) · Traccia 28.2 Perché, per, quando · Traccia 28.3 Domanda o risposta?</div>""")

    # Page 2
    st = [("Quando è arrivata Júlia?", "ieri sera, alle undici"), ("Perché è andata a Belo Horizonte?", "per stare con la sua famiglia"),
          ("Perché è tornata prima?", "perché sabato arriva Bruno"), ("Perché viene Bruno a Bologna?", "per studiare all'università")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:55mm')}</li>" for q, a in st)
    vf = [("Marco è andato in Sardegna da solo.", "F"), ("Ha affittato una barca per vedere le spiagge.", "V"), ("Luca si sposa a fine settembre a Firenze.", "V"),
          ("Davide è passato ogni giorno per dare l'acqua alle piante.", "F"), ("Júlia regala a Davide una maglietta del Brasile.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: com'è andata?", "10 min")}
<p>Júlia è tornata dal Brasile: al bar, allo studio e a casa tutti hanno qualcosa da raccontare.</p>
{audiocard(["28.1 · SLOW", "28.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi.", "4 min", "28.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialoghi 2 e 3. Vero (V) o falso (F)?", "4 min", "28.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Quando mette la maglietta Davide?", "2 min")}
<div class="wline">{R("Quando gioca a calcetto. «Così vinciamo!»")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Le risposte 2 e 4 cominciano con <i>per</i> (lo scopo), la 3 con <i>perché</i> (la causa): lasciarle notare, la regola è a pagina 3.</li>
<li>B: versione <b>naturale</b>. 1: con <b>alcuni amici</b>. 4: <b>ogni due giorni</b>.</li></ol>""")

    # Page 3 (explanation first: 3A spiegazione, 3B controlla, 3C pratica)
    ex = [("<b>Perché…?</b> → la domanda", "<b>Perché</b> sei tornata prima?"), ("<b>perché</b> + frase → la causa", "Sono tornata <b>perché</b> Bruno arriva sabato."),
          ("<b>per</b> + infinito → lo scopo (a che cosa serve)", "Bruno viene <b>per studiare</b>. · Sono passato <b>per dare</b> l'acqua."),
          ("<b>quando</b> + frase → il momento", "<b>Quando siamo arrivati</b>, abbiamo affittato una barca. · <b>Quando gioco</b>, la metto.")]
    exr = "".join(f"<tr><td style='width:62mm'>{a}</td><td>{x}</td></tr>" for a, x in ex)
    ck = [("Sono stata a Belo Horizonte ", ["per", "perché"], "per", " stare con la famiglia."), ("Sono tornata prima ", ["per", "perché"], "perché", " arriva Bruno."),
          ("Ho portato un regalo ", ["per", "perché"], "per", " dire grazie."), ("", ["Quando", "Perché"], "Quando", " gioco a calcetto, metto la maglietta.")]
    ckl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in ck)
    pr = [("Perché studi italiano?", "per", " lavorare in Italia."), ("Perché sei stanca?", "perché", " ho dormito poco."),
          ("Perché vai in farmacia?", "per", " comprare lo sciroppo."), ("Perché non vieni?", "perché", " ho mal di testa."),
          ("Perché vai in banca?", "per", " pagare l'affitto."), ("Perché sei contento?", "perché", " domani parto!")]
    prl = [f'<li value="{i+1}">{q} — {A(c, "min-width:14mm")}{z}</li>' for i, (q, c, z) in enumerate(pr)]
    b.page(f"""{sec(3, "Grammatica: perché, per, quando", "10 min")}
{sub("A", "Leggi la spiegazione.", "4 min")}
<table style="margin:0">{exr}</table>
<div class="box sand" style="margin-top:2mm"><h4>REGOLA</h4><b>perché</b> si usa per la domanda e per la risposta (la causa): dopo c'è un verbo coniugato (<i>arriva, ho dormito</i>). <b>per</b> + <b>infinito</b> spiega lo scopo: <i>per studiare, per dire grazie</i>. <b>quando</b> + verbo coniugato dice il momento; per il futuro usiamo il presente: <i>Quando arrivi, andiamo da Giulia.</i></div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "Pratica. Rispondi con perché o per.", "4 min")}
{twocol(prl, 4)}""",
    24, """<ol><li>A: domanda chiave per lo studente: <i>dopo c'è un infinito?</i> → <b>per</b>. <i>Dopo c'è un verbo coniugato?</i> → <b>perché</b>.</li>
<li>C: far notare che la domanda è sempre <i>Perché…?</i> e la risposta può essere <i>perché…</i> o <i>per…</i></li></ol>""")

    # Page 4
    ans3 = ["domanda", "risposta", "domanda", "risposta", "domanda", "risposta"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Bruno viene perché studiare.</td><td><b>Bruno viene per studiare.</b></td><td>Infinito → <i>per</i>.</td></tr>
<tr><td>Sono tornata per Bruno arriva.</td><td><b>Sono tornata perché Bruno arriva.</b></td><td>Verbo coniugato → <i>perché</i>.</td></tr>
<tr><td>Per che sei tornata?</td><td><b>Perché sei tornata?</b></td><td>Una sola parola.</td></tr>
<tr><td>Quando giocherò, la metto.</td><td><b>Quando gioco, la metto.</b></td><td><i>quando</i> + presente.</td></tr>
<tr><td>Perchè sei qui?</td><td><b>Perché sei qui?</b></td><td>Accento acuto: <i>é</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["28.2", "28.3"])}
{sub("A", "Perché, per, quando. Ascolta e ripeti. Perché ha l'accento sull'ultima sillaba: per-CHÉ.", "2 min", "28.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S282)}</div>
{sub("B", "Domanda o risposta? Ascolta la voce: sale (domanda) o scende (risposta)?", "3 min", "28.3")}
{twocol([f'<li value="{i+1}">{ch(["domanda", "risposta"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    34, """<ol><li>Errori: il primo nasce dal portoghese <i>para</i> + infinito; l'ultimo è un errore di scrittura frequente (<i>perchè</i> con l'accento grave).</li>
<li>4B: le frasi sono 1 Perché sei qui? 2 Perché lavoro qui. 3 Quando parti? 4 Sei tornata. 5 Sei tornata? 6 Quando posso. La 4 e la 5 hanno le stesse parole: cambia solo la voce.</li></ol>""")

    # Page 5
    mt = [("Júlia è tornata prima", "perché Bruno arriva sabato."), ("Marco ha affittato una barca", "per vedere le spiagge più belle."),
          ("Davide è passato ogni due giorni", "per dare l'acqua alle piante."), ("Júlia è stanchissima", "perché è arrivata alle undici di sera.")]
    left = "".join(f"<li>{a}</li>" for a, _ in mt)
    rgt = [mt[2][1], mt[3][1], mt[0][1], mt[1][1]]
    right = "".join(f"<div style='margin:0 0 .4mm'><b>{l}.</b> {x}</div>" for l, x in zip("abcd", rgt))
    cq = [("Perché Bruno porta la chitarra?", "per suonare con Chiara"), ("Quando arriva Bruno?", "sabato alle 18:40"),
          ("Perché Júlia va alla stazione?", "per prendere Bruno"), ("Che cosa fanno quando Bruno arriva?", "vanno a mangiare da Giulia")]
    cql = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in cq)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Unisci le due parti (1–4 con a–d).", "3 min")}
<div class="two"><ol style="margin:0">{left}</ol><div>{right}</div></div>
<p class="small" style="margin:.5mm 0">{R("1 c · 2 d · 3 a · 4 b") if T else ""}</p>
{sub("B", "La chat di Bruno. Leggi i messaggi e rispondi alle domande.", "5 min")}
{chat()}
<ol style="line-height:1.6;margin-top:1.5mm">{cql}</ol>""",
    22, """<ol><li>A: dopo l'esercizio, lo studente trasforma: <i>Perché Júlia è tornata prima?</i> e l'insegnante risponde.</li>
<li>B: Bruno scrive e non parla: è il fratello di Júlia e da adesso abita a Bologna. Chiara è la sua ragazza (unità 20).</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Le tue vacanze. Rispondi all'insegnante. Poi fai tu le stesse domande.", "5 min")}
<ol style="line-height:1.7"><li>Dove sei andato/a? Perché hai scelto quel posto?</li><li>Con chi sei andato/a? Per quanto tempo?</li><li>Che cosa hai fatto quando sei arrivato/a?</li><li>Hai portato un regalo? Per chi?</li></ol>
{sub("B", "Perché? Per… Scegli tre cose e spiega perché le fai o a che cosa servono.", "4 min")}
<div class="bank">studiare italiano · andare in palestra · bere il caffè · usare il telefono · viaggiare · cucinare · leggere · fare una passeggiata</div>
<div class="wline">{R("Studio italiano per lavorare in Italia e perché mi piace la musica italiana.")}</div><div class="wline"></div>
{sub("C", "Quando…? Completa e racconta all'insegnante.", "3 min")}
<ol style="line-height:1.8"><li>Quando sono stanco/a, <span class="wline" style="display:inline-block;width:80mm"></span></li>
<li>Quando torno dalle vacanze, <span class="wline" style="display:inline-block;width:74mm"></span></li></ol>""",
    24, """<ol><li>A: correggere <i>para</i> → <i>per</i> e <i>por que</i> → <i>perché</i>. Per la durata accettare <i>per due settimane</i> e <i>due settimane</i>.</li>
<li>B: incoraggiare una frase con <i>per</i> e una con <i>perché</i> per ogni attività.</li></ol>""")

    # Page 7
    pc = [("Unità 26", "So usare fa, da e tra."), ("Unità 28", "So raccontare le mie vacanze."), ("Unità 28", "So spiegare la causa con perché."),
          ("Unità 28", "So spiegare lo scopo con per + infinito."), ("Unità 28", "So dire il momento con quando.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Vado in Italia perché studiare.", "Vado in Italia per studiare."), ("Sono stanca per ho lavorato molto.", "Sono stanca perché ho lavorato molto."),
          ("Per che sei qui?", "Perché sei qui?"), ("Quando arriverai, mi telefoni?", "Quando arrivi, mi telefoni?"),
          ("Ho comprato i fiori perché fare un regalo a mia madre.", "…per fare un regalo a mia madre."), ("Studio molto perché voglio parlare bene.", "✓ corretta")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> Una frase è corretta.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il mio ritorno.</b> Scrivi 6–8 frasi sulle tue ultime vacanze: dove sei andato/a, perché, che cosa hai fatto quando sei arrivato/a e che cosa hai portato a casa.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il suo testo. Unità 29: <i>Cerco una stanza</i> (Bruno cerca casa: i numeri grandi e l'affitto).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("28.1", "Com'è andata? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("28.2", "Perché, per, quando")}
<p>{" · ".join(S282)}</p>
{sub("28.3", "Domanda o risposta?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S283))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 28 - Il ritorno")
