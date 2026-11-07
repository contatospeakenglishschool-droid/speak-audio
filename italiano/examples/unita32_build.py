# Speak! Essenziale A1 - Unità 32 "In autobus" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from linea import linea
setup(band="A1 · UNITÀ 32", audio_json=os.path.join(HERE, "audio_it-a1-unita-32.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'autobus", "autobus"), ("B", "la fermata", "fermata"), ("C", "la macchinetta", "macchinetta"), ("D", "l'autista", "autista"),
          ("E", "il binario", "binario"), ("F", "a piedi", "piedi"), ("G", "il pulsante", "pulsante"), ("H", "il calcetto", "calcetto")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-32"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["32.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S322 = [x.split(": ", 1)[1] for x in _r["32.2 Ripeti"].split("\n")]
S323 = [x.split(": ", 1)[1] for x in _r["32.3 Dettato"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split()[-1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 32", "In autobus", "Bruno va al calcetto · <b>prendere e scendere · da… a… · prima, poi, dopo</b>",
                       [("SAI FARE", "comprare un abbonamento, chiedere quale autobus prendere e dove scendere, spiegare un percorso"),
                        ("LINGUA", "Quale autobus prendo? · Scende alla sesta fermata · dalle sei alle undici · Prima…, poi…, dopo…"),
                        ("PRONUNCIA", "sc dolce e sc duro: scendo, scusi, scheda")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: in città", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Come vai al lavoro o a scuola? In autobus, in macchina, a piedi?</li><li>Quanto costa il biglietto dell'autobus nella tua città?</li><li>Ti piace viaggiare in autobus? Perché?</li></ol>""",
    22, """<ol><li>A: <i>la macchinetta</i> per convalidare il biglietto (si dice anche <i>obliteratrice</i>). <i>Andare a piedi</i>, ma <i>andare in autobus, in treno, in macchina</i>.</li>
<li>B: ripasso dei numeri e dei prezzi.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: l'autobus e la città</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>A piedi in via Zamboni · l'abbonamento · sull'autobus 20</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>prendere e scendere · da… a… · prima, poi, dopo</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>sc dolce e sc duro</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il percorso in ordine · completa le frasi</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>In biglietteria · sull'autobus · il mio percorso</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Sabato Bruno va a vedere la stanza di Paolo e chiede a Júlia quale autobus prendere: ma via Zamboni è a dieci minuti a piedi! Prima dritto fino alle Due Torri, poi a destra. Per il centro sportivo invece serve l'autobus: lunedì Bruno compra in biglietteria un abbonamento mensile per studenti (27 euro) con la nuova tessera, finalmente «con la zeta». Il 20 parte da via Rizzoli, passa ogni dodici minuti dalle 6 alle 23 e il viaggio dura venticinque minuti. Martedì, sull'autobus, un passeggero gli dice di scendere alla sesta fermata, dopo la Fiera: è Stefano, che gioca a calcetto con lui.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Pegar o ônibus</i> → <b>prendere l'autobus</b>; <i>descer do ônibus</i> → <b>scendere dall'autobus</b>; <i>descer no ponto</i> → <b>scendere alla fermata</b>. <i>De… até…</i> → <b>da… a…</b>, con l'articolo per le ore: <b>dalle</b> sei <b>alle</b> undici. <i>Depois</i> → <b>poi</b> (poi giri) o <b>dopo</b> (dopo cinque minuti, dopo la Fiera). Attenzione: <b>sc</b> + e/i è dolce (<i>scendo</i>), <b>sch</b> è duro (<i>scheda</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia il biglietto dell'autobus si compra prima di salire: in <b>tabaccheria</b>, in edicola, alle macchinette o con l'app; spesso anche a bordo con la carta contactless. Il biglietto si <b>convalida</b> (si timbra) appena sali; senza biglietto convalidato il controllore fa la <b>multa</b>. Gli studenti hanno abbonamenti a prezzo ridotto. Per scendere si <b>prenota la fermata</b> con il pulsante.</div>
<div class="box"><h4>AUDIO</h4>Traccia 32.1 Tre dialoghi (lento e naturale) · Traccia 32.2 Ascolta e ripeti · Traccia 32.3 Dettato di parole</div>""")

    # Page 2
    vf = [("Per andare in via Zamboni Bruno prende l'autobus.", "F"), ("Prima va fino alle Due Torri, poi gira a destra.", "V"),
          ("Il passeggero dice: «Scenda alla terza fermata».", "F"), ("Anche il passeggero gioca a calcetto il martedì.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: quale autobus prendo?", "10 min")}
<p>Bruno va a vedere la stanza in via Zamboni, compra l'abbonamento e prende l'autobus per il centro sportivo.</p>
{audiocard(["32.1 · SLOW", "32.1 · NATURAL"])}
{sub("A", "Dialogo 2. Ascolta e completa le informazioni sulla linea 20.", "5 min", "32.1 · SLOW")}
{linea(T)}
{sub("B", "Dialoghi 1 e 3. Vero (V) o falso (F)?", "3 min", "32.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. A quale fermata scende Bruno? Come si chiama il passeggero?", "2 min")}
<div class="wline">{R("Alla sesta fermata, dopo la Fiera: Centro Sportivo. Si chiama Stefano.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>, anche due volte. Far notare <i>dalle sei alle undici di sera</i> = <i>dalle 6 alle 23</i>.</li>
<li>B: versione <b>naturale</b>. 1: via Zamboni è a dieci minuti <b>a piedi</b>. 3: alla <b>sesta</b> fermata. Stefano passa dal <i>Lei</i> al <i>tu</i>: <i>Dai, prenota la fermata!</i></li></ol>""")

    # Page 3
    conj = [("io", "prendo", "scendo"), ("tu", "prendi", "scendi"), ("lui / lei / Lei", "prende", "scende"),
            ("noi", "prendiamo", "scendiamo"), ("voi", "prendete", "scendete"), ("loro", "prendono", "scendono")]
    cjr = "<tr><th></th>" + "".join(f"<th>{p}</th>" for p, _, _ in conj) + "</tr>" + "".join(
        f"<tr><td><b>{v}</b></td>" + "".join(f"<td><b>{c[i]}</b></td>" for c in conj) + "</tr>" for v, i in [("prendere", 1), ("scendere", 2)])
    ex = [("<b>prendere</b> + mezzo", "<b>Prendo</b> l'autobus, il treno, la metro, un taxi."),
          ("<b>scendere</b> a / da", "<b>Scendo alla</b> fermata Fiera. · <b>Scendo dall'</b>autobus."),
          ("<b>da… a…</b> (inizio → fine)", "<b>da</b> via Rizzoli <b>al</b> centro sportivo · <b>dalle</b> 6 <b>alle</b> 23 · <b>da</b> lunedì <b>a</b> venerdì"),
          ("<b>prima → poi → dopo</b> (l'ordine)", "<b>Prima</b> vai dritto, <b>poi</b> giri a destra. <b>Dopo</b> cinque minuti sei da Paolo.")]
    exr = "".join(f"<tr><td style='width:52mm'>{a}</td><td>{x}</td></tr>" for a, x in ex)
    ck = [("Bruno ", ["prende", "prendi"], "prende", " il 20 in via Rizzoli."), ("Scusi, dove ", ["scendo", "scende"], "scendo", " io?"),
          ("L'autobus passa ", ["da le / a le", "dalle / alle"], "dalle / alle", " 6 … 23."), ("", ["Prima", "Dopo"], "Prima", " compro il biglietto, poi salgo.")]
    ckl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in ck)
    pr = [("(noi)", "prendiamo", "prendere", "il treno per Firenze."), ("Ragazzi, dove", "scendete", "scendere", "?"),
          ("Júlia e Bruno", "prendono", "prendere", "un taxi."), ("(tu)", "Scendi", "scendere", "alla prossima fermata?")]
    prl = "".join(f"<li>{s} {A(v, 'min-width:24mm')} ({inf}) {z}</li>" for s, v, inf, z in pr)
    b.page(f"""{sec(3, "Grammatica: prendere, scendere, da… a…", "10 min")}
{sub("A", "Leggi la spiegazione.", "4 min")}
<table style="margin:0">{cjr}</table>
<table style="margin:1.5mm 0 0">{exr}</table>
<div class="box sand" style="margin-top:1.5mm"><h4>REGOLA</h4><i>prendere</i> e <i>scendere</i> sono verbi regolari in <b>-ere</b>. Con le ore usiamo <b>dalle… alle…</b> (da + le, a + le); con i luoghi <b>dal / dalla / dall'</b> e <b>al / alla / all'</b>. <b>poi</b> = dopo questo (nella sequenza); <b>dopo</b> + tempo o cosa: <i>dopo cinque minuti, dopo la Fiera</i>.</div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "Completa con prendere o scendere.", "3 min")}
<ol>{prl}</ol>""",
    24, """<ol><li>A: far trovare nei dialoghi: <i>quale autobus prendo, prende il venti, scende alla fermata, prima vai dritto, poi giri, dopo cinque minuti</i>.</li>
<li>B: 3 <i>da le / a le</i> non esiste: si uniscono sempre (<i>dalle, alle</i>).</li></ol>""")

    # Page 4
    dl = [f'<li value="{i+1}">{A(w, "min-width:30mm")}</li>' for i, w in enumerate(["scendo", "scusi", "scheda", "uscita", "tedeschi", "piscina"])]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Prendo l'autobus da via Rizzoli fino il centro.</td><td><b>Prendo l'autobus da via Rizzoli al centro.</b></td><td><i>da… a…</i></td></tr>
<tr><td>Scendo nella fermata Fiera.</td><td><b>Scendo alla fermata Fiera.</b></td><td><i>scendere a</i></td></tr>
<tr><td>da le sei a le undici</td><td><b>dalle sei alle undici</b></td><td>Preposizione + articolo.</td></tr>
<tr><td>Vado di autobus.</td><td><b>Vado in autobus.</b></td><td><i>in</i> + mezzo.</td></tr>
<tr><td>Vado in piedi.</td><td><b>Vado a piedi.</b></td><td>Espressione fissa.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["32.2", "32.3"])}
{sub("A", "Ascolta e ripeti. sce, sci = suono dolce · sca, sco, scu, sche, schi = suono duro [sk].", "2 min", "32.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S322)}</div>
{sub("B", "Dettato. Ascolta e scrivi la parola.", "3 min", "32.3")}
{twocol(dl, 4)}""",
    34, """<ol><li>Errori: <i>vado de ônibus</i> → <i>vado in autobus</i>; <i>vou a pé</i> → <i>vado a piedi</i>.</li>
<li>4: in <i>scendo, piscina, uscita</i> il suono è dolce, come «x» in <i>xícara</i>; in <i>scheda, tedeschi</i> è duro: «s» + «k».</li></ol>""")

    # Page 5
    route = [("Poi prendi il 20 in via Rizzoli.", 2), ("Prima vai a piedi fino alle Due Torri.", 1), ("Dopo venticinque minuti scendi al capolinea.", 4),
             ("Alla Fiera prenoti la fermata con il pulsante.", 3), ("Dopo la partita torni a casa con lo stesso autobus.", 5)]
    rl = "".join(f"<li>{A(str(n), 'min-width:8mm')} {s}</li>" for s, n in route)
    gaps = [("L'autobus passa", "dalle", "6", "alle", "23."), ("Il negozio è aperto", "dalle", "9", "alle", "19."),
            ("Bruno ha lezione", "dal", "lunedì", "al", "giovedì."), ("Il treno va", "da", "Bologna", "a", "Firenze.")]
    gl = "".join(f"<li>{a} {A(d, 'min-width:12mm')} {x} {A(c, 'min-width:12mm')} {z}</li>" for a, d, x, c, z in gaps)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Il percorso di Bruno. Metti le frasi in ordine (1–5).", "3 min")}
<ol style="list-style:none;padding-left:0;line-height:1.8">{rl}</ol>
{sub("B", "Completa con da, dal, dalle… e a, al, alle…", "2 min")}
<ol style="line-height:1.8">{gl}</ol>
{sub("C", "Scrivi come vai dalla tua casa a scuola (o al lavoro). Usa prima, poi, dopo.", "3 min")}
<div class="wline">{R("Prima vado a piedi alla fermata, poi prendo il… e scendo in… Dopo dieci minuti…")}</div><div class="wline"></div>""",
    22, """<ol><li>A: ordine: 2 · 1 · 4 · 3 · 5 (prima → poi → … → dopo).</li>
<li>B: 3: con i giorni si dice anche <i>da lunedì a giovedì</i> (senza articolo): accettare entrambi.</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "In biglietteria. L'insegnante è l'impiegato/a. Compra un abbonamento o un biglietto e chiedi: quale autobus prendo? dove scendo? ogni quanto passa? Poi cambiate.", "5 min")}
<div class="box" style="font-size:9pt"><h4>PAROLE UTILI</h4>Vorrei un abbonamento mensile / un biglietto. · Quanto costa? · Quale autobus prendo per…? · Dove scendo? · Ogni quanto passa? · Il viaggio dura… · Scusi, questo autobus va a…? · Prenoto la fermata.</div>
{sub("B", "Sull'autobus. Sei un turista: chiedi a un passeggero se l'autobus va al Duomo, alla stazione, al museo… e a quale fermata devi scendere.", "3 min")}
<div class="wline"></div>
{sub("C", "Il mio percorso. Spiega all'insegnante come arrivare dalla scuola a casa tua: prima…, poi…, dopo…", "4 min")}""",
    24, """<ol><li>A: usare i dati della linea 20 o di una linea reale della città degli studenti.</li>
<li>C: l'insegnante disegna il percorso alla lavagna mentre lo studente parla, poi controlla insieme a lui.</li></ol>""")

    # Page 7
    pc = [("Unità 31", "So dire che cosa mi serve e chiedere il permesso con posso…?"), ("Unità 32", "So comprare un biglietto o un abbonamento."),
          ("Unità 32", "So chiedere quale autobus prendere e dove scendere."), ("Unità 32", "So dire orari e percorsi con da… a…"),
          ("Unità 32", "So spiegare un percorso con prima, poi, dopo.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Vado di treno a Milano.", "Vado in treno a Milano."), ("Scendo nella fermata Stazione.", "Scendo alla fermata Stazione."),
          ("La banca è aperta da le 8 a le 13.", "La banca è aperta dalle 8 alle 13."), ("Noi prendono l'autobus.", "Noi prendiamo l'autobus."),
          ("Vado in piedi all'università.", "Vado a piedi all'università."), ("Prima mangio, poi studio.", "✓ corretta")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> Una frase è corretta.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il mio autobus.</b> Scrivi un messaggio a un amico italiano che viene a trovarti: quale autobus prende, dove scende, ogni quanto passa e quanto costa il biglietto. Usa prima, poi, dopo.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il messaggio e l'insegnante segue il percorso sulla mappa. Unità 33: <i>Al cinema</i> (Bruno e Chiara; mi è piaciuto / mi è piaciuta).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("32.1", "In autobus (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("32.2", "Ascolta e ripeti")}
<p>{" · ".join(S322)}</p>
{sub("32.3", "Dettato")}
<p>{" · ".join(S323)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 32 - In autobus")
