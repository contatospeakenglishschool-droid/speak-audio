# Speak! Essenziale A1 - Unità 30 "All'università" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from modulo import modulo
setup(band="A1 · UNITÀ 30", audio_json=os.path.join(HERE, "audio_it-a1-unita-30.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "gli studenti", "studenti"), ("B", "il modulo", "modulo"), ("C", "il passaporto", "passaporto"), ("D", "la tessera", "tessera"),
          ("E", "l'aula", "aula"), ("F", "la chiocciola", "chiocciola"), ("G", "il medico", "medico"), ("H", "la pallavolo", "pallavolo")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-30"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["30.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S302 = [x.split(": ", 1)[1] for x in _r["30.2 Ripeti alfabeto"].split("\n")]
S303 = [x.split(": ", 1)[1] for x in _r["30.3 Dettato di parole"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split()[-1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 30", "All'università", "Bruno si iscrive · <b>l'alfabeto e le domande: chi, che cosa, quale, quanto…</b>",
                       [("SAI FARE", "compilare un modulo, dare i tuoi dati personali e dire come si scrive il tuo nome"),
                        ("LINGUA", "Come si scrive? · Dove è nato? · Qual è il Suo indirizzo? · Quali corsi avete?"),
                        ("PRONUNCIA", "l'alfabeto italiano · dettato di parole")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: il primo giorno", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Hai studiato all'università? Che cosa? Dove?</li><li>Quali documenti hai nel portafoglio?</li><li>Ti piace fare sport con altre persone? Quale?</li></ol>""",
    22, """<ol><li>A: <i>la tessera</i> = la carta (dell'università, della palestra, della biblioteca). <i>La chiocciola</i> è il simbolo @ (e anche l'animale lento!).</li>
<li>B: domanda 1: ripasso del passato prossimo; accettare risposte brevi.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: l'università e i documenti</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>In segreteria (il modulo) · al centro sportivo · l'errore sulla tessera</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Le parole interrogative · l'alfabeto e come si scrive</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>L'alfabeto · dettato di parole</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Domande e risposte · la domanda giusta</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>In segreteria (gioco di ruolo) · come si scrive?</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Bruno si iscrive al corso di laurea in Storia. In segreteria l'impiegata compila con lui il modulo: Bruno Souza, nato a Belo Horizonte il 14 marzo 2006, per ora abita da Júlia in via Santo Stefano; la sua e-mail è bruno.souza@studio.unibo.it; le lezioni cominciano il 28 settembre. Al centro sportivo universitario chiede i corsi del martedì e del giovedì e sceglie il calcetto (30 euro al mese), ma servono la tessera e il certificato medico. La sera mostra la tessera a Júlia: c'è scritto «Sousa», con la esse! Domani torna in segreteria per cambiarla.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Le lettere italiane si chiamano in modo diverso: <i>gê</i> → <b>gi</b>, <i>jota</i> → <b>i lunga</b>, <i>agá</i> → <b>acca</b>, <i>erre</i> uguale, <i>zê</i> → <b>zeta</b>, <i>ípsilon</i> → <b>ipsilon</b> (o <i>i greca</i>). <i>Qual é?</i> → <b>qual è</b> (senza apostrofo!). <i>Onde você nasceu?</i> → <b>Dove è nato?</b> (con <i>essere</i>). Il plurale di <i>quale</i> è <b>quali</b>: <i>Quali corsi…?</i></div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>L'Università di Bologna (<b>Alma Mater Studiorum</b>, 1088) ha più di 90.000 studenti. Ci si iscrive online e poi, a volte, in <b>segreteria studenti</b>. Ogni studente ha un'e-mail <i>nome.cognome@studio.unibo.it</i> e paga le tasse in rate secondo il reddito della famiglia. Per fare sport al <b>CUS</b> (Centro Universitario Sportivo) e in palestra in Italia serve un <b>certificato medico</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 30.1 Tre dialoghi (lento e naturale) · Traccia 30.2 L'alfabeto · Traccia 30.3 Dettato di parole</div>""")

    # Page 2
    vf = [("Al centro sportivo ci sono corsi di nuoto, pallavolo e calcetto.", "V"), ("Il calcetto costa quaranta euro al mese.", "F"),
          ("Bruno ha già la tessera dell'università.", "F"), ("Per fare sport serve il certificato medico.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: in segreteria", "10 min")}
<p>Bruno si iscrive all'università, va al centro sportivo e la sera c'è una sorpresa sulla tessera.</p>
{audiocard(["30.1 · SLOW", "30.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e completa il modulo di Bruno.", "5 min", "30.1 · SLOW")}
{modulo(T)}
{sub("B", "Dialogo 2. Vero (V) o falso (F)?", "3 min", "30.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. Che errore c'è sulla tessera di Bruno?", "2 min")}
<div class="wline">{R("Hanno scritto «Sousa» con la esse, non con la zeta.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>, anche due volte. L'e-mail si legge: <i>bruno punto souza chiocciola studio punto unibo punto it</i>.</li>
<li>B: versione <b>naturale</b>. 2: <b>trenta</b> euro. 3: arriva tra una settimana. Far notare che al centro sportivo si usa il <i>tu</i>, in segreteria il <i>Lei</i>.</li></ol>""")

    # Page 3
    qw = [("<b>chi?</b> → una persona", "<b>Chi</b> è il tuo medico?"), ("<b>che cosa?</b> (che? cosa?) → una cosa, un'azione", "<b>Che cosa</b> ti piace? · <b>Che cosa</b> fai adesso?"),
          ("<b>come?</b> → il modo, il nome", "<b>Come</b> si chiama? · <b>Come</b> si scrive?"), ("<b>dove? di dove?</b> → il luogo, l'origine", "<b>Dove</b> è nato? · <b>Di dove</b> sei?"),
          ("<b>quando?</b> → il momento", "<b>Quando</b> è nato? · <b>Quando</b> cominciano le lezioni?"),
          ("<b>quale? quali?</b> → una scelta", "<b>Qual è</b> il Suo indirizzo? · <b>Quali</b> corsi avete?"),
          ("<b>quanto? quanta? quanti? quante?</b> → la quantità, il prezzo", "<b>Quanto</b> costa? · <b>Quanti</b> anni hai? · <b>Quante</b> lezioni?")]
    qwr = "".join(f"<tr><td style='width:66mm'>{a}</td><td>{x}</td></tr>" for a, x in qw)
    ck = [("", ["Qual è", "Qual'è"], "Qual è", " il tuo numero di telefono?"), ("", ["Quale", "Quali"], "Quali", " lingue parli?"),
          ("", ["Quanti", "Quante"], "Quante", " ore studi al giorno?"), ("", ["Chi", "Che cosa"], "Chi", " è il tuo professore?")]
    ckl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in ck)
    b.page(f"""{sec(3, "Grammatica: le domande e l'alfabeto", "10 min")}
{sub("A", "Leggi la spiegazione: le parole interrogative.", "4 min")}
<table style="margin:0">{qwr}</table>
<div class="box sand" style="margin-top:2mm"><h4>REGOLA</h4><b>quale</b> → plurale <b>quali</b>; davanti a <i>è</i> diventa <b>qual è</b> (senza apostrofo). <b>quanto</b> cambia come un aggettivo: <i>quanto tempo, quanta pasta, quanti anni, quante ore</i>. Per la nascita usiamo <b>essere nato/a</b>: <i>Sono nato a…, sono nata il…</i> · Per scrivere: <b>Come si scrive?</b> → si dicono le lettere: <i>esse, o, u, zeta, a</i>; due lettere uguali = <b>doppia</b>: <i>Rossi = erre, o, doppia esse, i</i>.</div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "L'alfabeto. Le 21 lettere italiane e le 5 straniere.", "4 min")}
<div class="bank" style="font-size:9.2pt;line-height:1.7">A a · B bi · C ci · D di · E e · F effe · G gi · H acca · I i · L elle · M emme · N enne · O o · P pi · Q cu · R erre · S esse · T ti · U u · V vu · Z zeta<br>
<b>straniere:</b> J i lunga · K kappa · W doppia vu · X ics · Y ipsilon &nbsp;&nbsp; <b>simboli:</b> @ chiocciola · . punto · - trattino · _ trattino basso</div>""",
    24, """<ol><li>A: far trovare le domande nei dialoghi. Con il <i>Lei</i>: <i>Come si chiama? Dove è nato?</i>; con il <i>tu</i>: <i>Come ti chiami? Dove sei nato?</i></li>
<li>C: le lettere J, K, W, X, Y si usano solo nelle parole straniere (<i>jeans, kiwi, web, taxi, yogurt</i>).</li></ol>""")

    # Page 4
    dw = ["BOLOGNA", "ZAMBONI", "ROSSI", "CHIARA", "GIULIA", "STORIA"]
    dl = [f'<li value="{i+1}">{A(w, "min-width:34mm")}</li>' for i, w in enumerate(dw)]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Qual'è il tuo indirizzo?</td><td><b>Qual è il tuo indirizzo?</b></td><td>Senza apostrofo.</td></tr>
<tr><td>Quale corsi avete?</td><td><b>Quali corsi avete?</b></td><td>Plurale: <i>quali</i>.</td></tr>
<tr><td>Quanto anni hai?</td><td><b>Quanti anni hai?</b></td><td><i>anni</i> è maschile plurale.</td></tr>
<tr><td>Dove ha nato?</td><td><b>Dove è nato?</b></td><td><i>nascere</i> → <i>essere</i>.</td></tr>
<tr><td>Sono nato nel 14 marzo.</td><td><b>Sono nato il 14 marzo.</b></td><td>La data: <i>il</i> + giorno.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["30.2", "30.3"])}
{sub("A", "L'alfabeto. Ascolta e ripeti.", "2 min", "30.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S302)}</div>
{sub("B", "Dettato. Ascolta le lettere e scrivi la parola.", "3 min", "30.3")}
{twocol(dl, 4)}""",
    34, """<ol><li>Errori: anche i nomi delle lettere sono un problema (in portoghese <i>gê, agá, jota</i>): fare un piccolo gioco con G, H, J, Z.</li>
<li>4B: le parole sono 1 Bologna, 2 Zamboni, 3 Rossi (doppia esse), 4 Chiara, 5 Giulia, 6 Storia.</li></ol>""")

    # Page 5
    mt = [("Come si chiama?", "Mi chiamo Bruno Souza."), ("Dove è nato?", "A Belo Horizonte."), ("Quando è nato?", "Il 14 marzo 2006."),
          ("Che cosa studia?", "Storia."), ("Quanto costa il calcetto?", "Trenta euro al mese."), ("Chi è il tuo medico?", "Il dottor Bianchi.")]
    left = "".join(f"<li>{q}</li>" for q, _ in mt)
    order = [3, 0, 5, 1, 4, 2]
    rgt = [mt[i][1] for i in order]
    right = "".join(f"<div style='margin:0 0 .4mm'><b>{l}.</b> {x}</div>" for l, x in zip("abcdef", rgt))
    key = " · ".join(f"{i+1} {'abcdef'[order.index(i)]}" for i in range(6))
    fq = [("Abito in via Santo Stefano.", "Dove abiti?"), ("Ho vent'anni.", "Quanti anni hai?"), ("Il mio numero è 347 218 9506.", "Qual è il tuo numero?"),
          ("Gioco a calcetto il martedì.", "Quando giochi a calcetto?"), ("Preferisco il nuoto.", "Quale sport preferisci?")]
    fql = "".join(f"<li>{A(q, 'min-width:50mm')} — {a}</li>" for a, q in fq)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Unisci la domanda (1–6) alla risposta (a–f).", "3 min")}
<div class="two"><ol style="margin:0">{left}</ol><div>{right}</div></div>
<p class="small" style="margin:.5mm 0">{R(key) if T else ""}</p>
{sub("B", "La domanda giusta. Scrivi la domanda per ogni risposta (con il tu).", "5 min")}
<ol style="line-height:1.9">{fql}</ol>""",
    22, """<ol><li>A: la 6 usa il <i>tu</i>, le altre il <i>Lei</i>: chiedere quale.</li>
<li>B: accettare anche altre domande corrette (<i>Quanti anni hai? / Che età hai?</i>). Poi lo studente risponde con i suoi dati.</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "In segreteria. L'insegnante è l'impiegato/a e compila il modulo con i tuoi dati. Rispondi e di' come si scrivono il nome, il cognome e la città. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt"><h4>PAROLE UTILI</h4>Buongiorno, vorrei iscrivermi a… · Come si chiama? · Come si scrive? · Con la doppia… · Dove è nato/a? · Quando è nato/a? · Qual è il Suo indirizzo? · Qual è la Sua e-mail? · Può ripetere, per favore? · Più piano, per favore.</div>
{sub("B", "Come si scrive? Pensa a tre parole italiane (una città, un piatto, un nome). Di' le lettere: l'insegnante scrive. Poi cambiate.", "4 min")}
<div class="wline"></div>
{sub("C", "Il tuo centro sportivo ideale. Quali corsi ci sono? Quando? Quanto costa? Chi viene con te?", "2 min")}""",
    24, """<ol><li>A: l'insegnante sbaglia apposta una lettera (come la signora con <i>Sousa</i>): lo studente deve correggere: <i>No, con la zeta!</i></li>
<li>B: buone parole da dettare: <i>Firenze, gnocchi, Ghirlandaio, Bergamo, zucchine</i>.</li></ol>""")

    # Page 7
    pc = [("Unità 29", "So dire i numeri grandi e chiedere quanto costa."), ("Unità 30", "So dire l'alfabeto e come si scrive il mio nome."),
          ("Unità 30", "So fare domande con chi, che cosa, dove, quando, quale, quanto."), ("Unità 30", "So dare i miei dati personali e compilare un modulo."),
          ("Unità 30", "So dire dove e quando sono nato/a.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Qual'è la tua città?", "Qual è la tua città?"), ("Quale libri leggi?", "Quali libri leggi?"), ("Quanto sorelle hai?", "Quante sorelle hai?"),
          ("Dove hai nato?", "Dove sei nato/a?"), ("Che cosa è il tuo professore?", "Chi è il tuo professore?"), ("Quando sei nata?", "✓ corretta")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> Una frase è corretta.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il mio modulo.</b> Scrivi i tuoi dati come nel modulo di Bruno (cognome, nome, luogo e data di nascita, nazionalità, indirizzo, e-mail). Poi scrivi 5 domande per conoscere un nuovo compagno di corso.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente fa le sue 5 domande all'insegnante. Unità 31: <i>Il telefono nuovo</i> (la SIM, le offerte, mi serve / mi servono).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("30.1", "In segreteria (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("30.2", "L'alfabeto")}
<p>{" · ".join(S302)}</p>
{sub("30.3", "Dettato di parole")}
<p>{" · ".join(S303)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 30 - All'università")
