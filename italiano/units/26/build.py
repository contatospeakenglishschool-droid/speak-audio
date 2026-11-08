# Speak! Essenziale A1 - Unità 26 "Un anno in Italia" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from linea import timeline
setup(band="A1 · UNITÀ 26", audio_json=os.path.join(HERE, "audio_it-a1-unita-26.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "le valigie", "valigie"), ("B", "i portici", "portici"), ("C", "il ragù", "ragù"), ("D", "Firenze", "Firenze"),
          ("E", "Capri", "Capri"), ("F", "Venezia", "Venezia"), ("G", "il brindisi", "brindisi"), ("H", "il contratto", "contratto")]

SCRIPT = [("Narratore", "Dialogo uno. Un anno dopo, Davide intervista di nuovo Júlia per il suo progetto."),
          ("Davide", "Allora, Júlia, da quanto tempo abiti a Bologna?"), ("Júlia", "Abito a Bologna da un anno. Sono arrivata a giugno dell'anno scorso."),
          ("Davide", "Che cosa hai fatto quest'anno?"),
          ("Júlia", "Tantissime cose! Ho conosciuto persone fantastiche, ho imparato a fare il ragù e ho cambiato casa."),
          ("Davide", "E hai visitato l'Italia?"), ("Júlia", "Sì, sono andata a Firenze, a Napoli e a Capri. Ma non ho ancora visto Venezia!"),
          ("Davide", "E adesso, com'è la tua giornata?"),
          ("Júlia", "Come prima: mi sveglio alle sei e mezza e vado allo studio. Ma adesso il giovedì gioco anche a calcetto!"),
          ("Davide", "Tu? Ma a dicembre hai detto: il calcio non mi piace per niente!"), ("Júlia", "Eh, le persone cambiano!"),
          ("Narratore", "Dialogo due. Allo studio."), ("Marco", "Júlia, ho una bella notizia. Lo studio vuole rinnovare il tuo contratto per altri due anni!"),
          ("Júlia", "Davvero? Che bello!"), ("Marco", "Allora resti a Bologna?"),
          ("Júlia", "Certo! L'anno prossimo voglio fare un corso di italiano avanzato. E voglio vedere Venezia e la Sicilia."), ("Marco", "E Bruno?"),
          ("Júlia", "Bruno torna a settembre: vuole studiare qui all'università. Tra tre mesi è di nuovo a Bologna."),
          ("Marco", "All'università… o da Chiara?"), ("Júlia", "Ah, non lo so!"),
          ("Narratore", "Dialogo tre. Al bar, una sorpresa."), ("Giulia", "Sorpresa! Buon anniversario, Júlia: un anno a Bologna!"), ("Júlia", "Oh, che bello! Grazie!"),
          ("Signora Rossi", "Un anno fa sei arrivata con due valigie e un dizionario."),
          ("Júlia", "È vero! E il primo giorno ho detto «arrivederci» a Giulia, invece di «ciao»!"), ("Giulia", "E adesso parli italiano benissimo!"),
          ("Davide", "Un brindisi! Alla nostra brasiliana di Bologna!"), ("Marco", "Cin cin!"), ("Júlia", "Grazie, amici. Adesso Bologna è casa mia.")]
S262 = ["capisco, capisci", "conosco, conosci", "scuola, sciare", "pesce, uscire", "conosciuto, ho conosciuto", "Capisci? Ho conosciuto persone fantastiche."]
S263 = ["Abito a Bologna da un anno.", "Sono arrivata un anno fa.", "Ho già visto Firenze.", "Non ho ancora visto Venezia.", "Tra tre mesi Bruno torna.",
        "L'anno prossimo voglio vedere la Sicilia."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 26", "Un anno in Italia", "Il primo anno di Júlia a Bologna · <b>sono arrivata un anno fa, abito qui da un anno</b>",
                       [("SAI FARE", "raccontare un anno della tua vita: che cosa hai fatto, che cosa fai adesso e che cosa vuoi fare"),
                        ("LINGUA", "passato prossimo + presente + progetti · fa / da / tra · già, non… ancora"),
                        ("PRONUNCIA", "SC: capisco / capisci · raccontare la tua storia")])
    words = [w for _, w, _ in PHOTOS]
    gn = [("visto Firenze", "ha già"), ("visto Venezia", "non ha ancora"), ("imparato a fare il ragù", "ha già"), ("visto la Sicilia", "non ha ancora"),
          ("cambiato casa", "ha già"), ("fatto un corso di italiano avanzato", "non ha ancora")]
    gnl = [f'<li value="{i+1}">Júlia {A(v, "min-width:27mm")} {s}.</li>' for i, (s, v) in enumerate(gn)]
    b.page(f"""{sec(1, "Riscaldamento: un anno di Júlia", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Che cosa ricordi? Completa con ha già o non ha ancora.", "4 min")}
{twocol(gnl, 3)}""",
    22, """<ol><li>A: ogni foto è un ricordo delle unità passate (il ragù: 12; Firenze: 11 e 16; Capri: 21). Chiedere: <i>Ti ricordi quando…?</i></li>
<li>B: lo studente usa la memoria; si controlla dopo l'ascolto. La regola di <i>già / non… ancora</i> è a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto dell'anno di Júlia · ha già / non ha ancora</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>L'intervista di Davide · il contratto · la festa a sorpresa</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>passato, presente e progetti · fa / da / tra · già, non… ancora</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>SC · raccontare la tua storia</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>La linea del tempo di Júlia · fa, da o tra?</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Hai già…? · il tuo anno · tu e l'italiano</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA (E FINISCE IL PRIMO ANNO)</h4>È passato un anno. Davide intervista di nuovo Júlia per il suo progetto (come nel Ripasso 1): Júlia racconta che cosa ha fatto e ammette che adesso gioca a calcetto, anche se a dicembre «il calcio non le piaceva per niente». Lo studio le rinnova il contratto per altri due anni: l'anno prossimo vuole vedere Venezia e la Sicilia, e Bruno torna a settembre per studiare (o per Chiara, unità 20?). Al bar gli amici le fanno una festa a sorpresa: «Adesso Bologna è casa mia.»</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese usa <i>há</i> per due idee: <i>moro aqui há um ano</i> → <b>abito qui da un anno</b> (presente + da); <i>cheguei há um ano</i> → <b>sono arrivata un anno fa</b>. <i>Em três meses</i> → <b>tra tre mesi</b> (non <i>in</i>). <i>Já vi</i> → <b>ho già visto</b> (già dopo l'ausiliare). SC + E/I suona come «ch» in <i>chá</i>: <i>capisci</i> ≈ «capíxi».</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Bologna ha tre soprannomi: <b>la Dotta</b> (l'università più antica del mondo occidentale, del 1088), <b>la Grassa</b> (la cucina: ragù, tortellini, mortadella) e <b>la Rossa</b> (il colore dei tetti e dei portici). Ogni anno arrivano migliaia di studenti e lavoratori stranieri. Nel brindisi si dice <b>Cin cin!</b> o <b>Salute!</b> e ci si guarda negli occhi.</div>
<div class="box"><h4>AUDIO</h4>Traccia 26.1 Tre dialoghi (lento e naturale) · Traccia 26.2 SC · Traccia 26.3 Raccontare la tua storia</div>""")

    # Page 2
    tl = [("Un anno fa", "è arrivata a Bologna (con due valigie e un dizionario)"), ("Quest'anno", "ha conosciuto persone, ha imparato il ragù, ha cambiato casa"),
          ("Adesso", "si sveglia alle sei e mezza · il giovedì gioca a calcetto"), ("L'anno prossimo", "vuole fare un corso avanzato · vedere Venezia e la Sicilia")]
    tlr = "".join(f"<tr><td style='width:30mm'><b>{n}</b></td><td>{A(s, 'min-width:120mm')}</td></tr>" for n, s in tl)
    vf = [("Júlia abita a Bologna da un anno.", "V"), ("Júlia ha già visto Venezia.", "F"), ("Lo studio vuole rinnovare il contratto per un anno.", "F"),
          ("Bruno torna a settembre per studiare.", "V"), ("Il primo giorno Júlia ha detto «ciao» a Giulia.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: un anno a Bologna", "10 min")}
<p>Un'intervista, una bella notizia e una sorpresa: com'è stato il primo anno di Júlia?</p>
{audiocard(["26.1 · SLOW", "26.1 · NATURAL"])}
{sub("A", "Ascolta e completa la storia di Júlia.", "5 min", "26.1 · SLOW")}
<table style="margin:0">{tlr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "3 min", "26.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa dice Júlia alla fine? Perché?", "2 min")}
<div class="wline">{R("«Adesso Bologna è casa mia.» Perché ha amici, lavoro e una vita a Bologna.")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi. <i>Rinnovare il contratto</i> = continuare il contratto. Ricordare l'intervista del Ripasso 1: <i>il calcio non mi piace per niente!</i></li>
<li>B: versione <b>naturale</b>. 2: <b>non ha ancora</b> visto Venezia. 3: <b>due anni</b>. 5: ha detto <b>arrivederci</b> (unità 01). <i>Cin cin</i> = si dice nel brindisi.</li></ol>""")

    # Page 3
    tt = [("<b>il passato</b> · passato prossimo", "<i>Sono arrivata</i> un anno fa. <i>Ho conosciuto</i> Marco. <i>Sono andata</i> a Napoli."),
          ("<b>il presente</b> · abitudini, adesso", "<i>Mi sveglio</i> alle sei e mezza. Il giovedì <i>gioco</i> a calcetto."),
          ("<b>il futuro</b> · progetti", "Bruno <i>torna</i> a settembre. L'anno prossimo <i>voglio vedere</i> Venezia.")]
    ttr = "".join(f"<tr><td style='width:52mm'>{a}</td><td>{x}</td></tr>" for a, x in tt)
    fdt = [("<b>fa</b> → passato", "Sono arrivata un anno <b>fa</b>."), ("<b>da</b> → dal passato a oggi", "Abito qui <b>da</b> un anno."),
           ("<b>tra</b> → futuro", "Bruno torna <b>tra</b> tre mesi.")]
    fdtr = "".join(f"<tr><td style='width:34mm'>{a}</td><td>{x}</td></tr>" for a, x in fdt)
    rules = [("Abito a Bologna ", "da", "fa", " un anno."), ("Sono arrivata un anno ", "fa", "da", "."), ("Bruno torna ", "tra", "fa", " tre mesi."),
             ("", "Non ho ancora visto", "Ho non ancora visto", " Venezia."), ("", "Ho già mangiato", "Già ho mangiato", " i tortellini.")]
    rl = "".join(f"<li>{a}<i>{ch([r, w] if i % 2 == 0 else [w, r], r)}</i>{z}</li>" for i, (a, r, w, z) in enumerate(rules))
    b.page(f"""{sec(3, "Grammatica: raccontare un anno", "10 min")}
{sub("A", "Passato, presente, futuro.", "3 min")}
<table style="margin:0">{ttr}</table>
<div class="two"><div>{sub("B", "Fa, da, tra.", "3 min")}
<table style="margin:0">{fdtr}</table>
<p class="small" style="margin-top:1mm">Attenzione: <b>da</b> + presente: <i>Studio italiano <b>da</b> sei mesi.</i> (non <i>ho studiato</i>)</p></div>
<div>{sub("C", "Già e non… ancora.", "2 min")}
<p>Ho <b>già</b> visto Firenze.<br><b>Non</b> ho <b>ancora</b> visto Venezia.</p>
<p class="small"><b>già</b> e <b>ancora</b> vanno tra <i>avere / essere</i> e il participio: <i>sono <b>già</b> andata</i>.</p></div></div>
{sub("D", "Scegli l'opzione corretta.", "2 min")}
<ol>{rl}</ol>""",
    28, """<ol><li>A: è il ripasso del primo anno di Júlia: passato prossimo (unità 11, 21), presente e riflessivi (unità 13), modali (unità 19), presente per i progetti (unità 25).</li>
<li>B: è il punto più difficile per i brasiliani, perché <i>há</i> traduce sia <b>fa</b> sia <b>da</b>. Domanda chiave: <i>Da quanto tempo…?</i> → <i>Da</i> + tempo. C: in portoghese <i>já</i> va prima del verbo; in italiano dopo l'ausiliare.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho abitato a Bologna da un anno.</td><td><b>Abito a Bologna da un anno.</b></td><td>Abito ancora lì: presente.</td></tr>
<tr><td>Sono arrivata fa un anno.</td><td><b>Sono arrivata un anno fa.</b></td><td><i>fa</i> va dopo il tempo.</td></tr>
<tr><td>Bruno torna in tre mesi.</td><td><b>Bruno torna tra tre mesi.</b></td><td><i>em três meses</i> → <i>tra</i>.</td></tr>
<tr><td>Già ho visto Firenze.</td><td><b>Ho già visto Firenze.</b></td><td><i>già</i> dopo l'ausiliare.</td></tr>
<tr><td>Ho andato a Napoli.</td><td><b>Sono andata a Napoli.</b></td><td><i>andare</i> → <i>essere</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["26.2", "26.3"])}
{sub("A", "SC. Ascolta e ripeti: SC + E / I = «ch» (come in chá); SC + A / O / U = «sk».", "2 min", "26.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S262)}</div>
{sub("B", "Raccontare la tua storia. Ascolta e ripeti.", "3 min", "26.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S263)}</div>""",
    40, """<ol><li>Errori: <i>Ho andato</i> è un errore che ritorna spesso: ripassare i verbi con <i>essere</i> (unità 11): <i>andare, venire, arrivare, partire, tornare, restare</i>.</li>
<li>4A: nei verbi in -ISC e in <i>conoscere</i> il suono cambia: <i>capi<b>sc</b>o</i> (sk) ma <i>capi<b>sc</b>i</i> (ch). Così anche <i>cono<b>sc</b>o / cono<b>sc</b>i / cono<b>sc</b>iuto</i>.</li></ol>""")

    # Page 5
    tq = [("giugno · Júlia / arrivare a Bologna", "A giugno Júlia è arrivata a Bologna."), ("luglio · Júlia / andare al cinema in piazza Maggiore", "A luglio Júlia è andata al cinema in piazza Maggiore."),
          ("dicembre · i genitori / venire a Bologna", "A dicembre i genitori sono venuti a Bologna."), ("febbraio · Bruno / arrivare", "A febbraio è arrivato Bruno."),
          ("Pasqua · Júlia e Giulia / andare a Napoli", "A Pasqua Júlia e Giulia sono andate a Napoli.")]
    tql = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in tq)
    fd = [("Júlia abita a Bologna", "da", "un anno."), ("I genitori sono venuti sei mesi", "fa", "."), ("Júlia gioca a calcetto", "da", "un mese."),
          ("Bruno torna a Bologna", "tra", "tre mesi."), ("Júlia è andata a Napoli due mesi", "fa", ".")]
    fdl = [f'<li value="{i+1}">{a} {A(x, "min-width:13mm")}{"" if z == "." else " "}{z}</li>' for i, (a, x, z) in enumerate(fd)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "La linea del tempo di Júlia. Guarda e scrivi le frasi al passato prossimo.", "5 min")}
{timeline()}
<ol>{tql}</ol>
{sub("B", "Oggi è giugno. Completa con fa, da o tra.", "3 min")}
{twocol(fdl, 3)}""",
    22, """<ol><li>A: attenzione all'accordo con <i>essere</i>: <i>è arrivata, sono venuti, sono andate</i>.</li>
<li>B: far spiegare ogni scelta: è finito (fa)? continua oggi (da)? deve ancora succedere (tra)?</li></ol>""")

    # Page 6
    hg = ["visto Venezia", "mangiato i tortellini", "visto un film italiano", "cucinato la pasta fresca", "letto un libro in italiano", "parlato italiano in Italia"]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Hai già…? Fai le domande all'insegnante e rispondi anche tu: sì, ho già… / no, non ho ancora…", "4 min")}
<table style="margin:1mm 0 2mm"><tr><th>Hai già…?</th><th style="width:24mm">Io</th><th style="width:24mm">L'insegnante</th></tr>
{"".join(f"<tr><td>{x}</td><td></td><td></td></tr>" for x in hg)}</table>
{sub("B", "Il tuo anno. Racconta all'insegnante: tre cose che hai fatto quest'anno, una cosa che fai adesso ogni settimana e due progetti per l'anno prossimo.", "4 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Tu e l'italiano. Rispondi all'insegnante.", "4 min")}
<ol style="line-height:1.65"><li>Da quanto tempo studi italiano? Perché hai cominciato?</li><li>Che cosa hai imparato in questo libro? Che cosa è ancora difficile?</li><li>Che cosa vuoi fare in italiano tra un anno?</li></ol>""",
    26, """<ol><li>A: correggere <i>già ho…</i> → <i>ho già…</i>. B: lo studente usa i tre tempi; l'insegnante fa domande: <i>Quando? Con chi? Perché?</i></li>
<li>C: un buon momento per festeggiare il primo anno di Júlia. Dopo il Ripasso 3 l'A1 continua con le unità 28–35: le prime settimane di Bruno a Bologna.</li></ol>""")

    # Page 7
    pc = [("Unità 25", "So fare gli auguri."), ("Unità 26", "So raccontare che cosa ho fatto quest'anno."), ("Unità 26", "So usare fa, da e tra."),
          ("Unità 26", "So usare già e non… ancora."), ("Unità 26", "So parlare dei miei progetti.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Studio italiano fa sei mesi.", "Studio italiano da sei mesi."), ("Mio fratello è partito da due giorni.", "Mio fratello è partito due giorni fa."),
          ("Vado in Italia in un mese.", "Vado in Italia tra un mese."), ("Già ho mangiato la pizza napoletana.", "Ho già mangiato la pizza napoletana."),
          ("Ho tornato a casa alle dieci.", "Sono tornato/a a casa alle dieci."), ("Ho abitato qui da due anni.", "Abito qui da due anni.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il mio anno.</b> Scrivi 8 frasi: da quanto tempo studi italiano, che cosa hai fatto quest'anno, che cosa fai adesso e che cosa vuoi fare l'anno prossimo.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il suo testo. Poi il Ripasso 3 (unità 19–26).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("26.1", "Un anno a Bologna (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("26.2", "SC")}
<p>{" · ".join(S262)}</p>
{sub("26.3", "Raccontare la tua storia")}
<p>{" ".join(S263)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 26 - Un anno in Italia")
