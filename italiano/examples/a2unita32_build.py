# Speak! Ponte A2 - Unità 32 "Ce la faccio!" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 32", audio_json=os.path.join(HERE, "audio_it-a2-unita-32.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la maratona", "maratona"), ("B", "il traguardo", "traguardo"), ("C", "il cronometro", "cronometro"), ("D", "la medaglia", "medaglia"),
          ("E", "le scarpe da corsa", "scarpe da corsa"), ("F", "il pettorale", "pettorale"), ("G", "la borraccia", "borraccia"), ("H", "i cartelli", "cartelli")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-32"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["32.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S322 = [x.split(": ", 1)[1] for x in _r["32.2 Ripeti"].split("\n")]
S323 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["32.3 Che cosa vuol dire"].split("\n")]


def _key(w):
    if w.startswith("l'"):
        return w[2:].lower()
    a, _, rest = w.partition(" ")
    return (rest if a in ("la", "il", "i", "gli", "lo", "le") else w).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 32", "Ce la faccio!", "Sfide e traguardi · <b>ce la faccio · ce l'ho fatta · ci metto un'ora · ce n'è</b>",
                       [("SAI FARE", "parlare di una sfida, dire quanto tempo ci vuole, incoraggiare una persona, raccontare un successo"),
                        ("LINGUA", "Ce la faccio? — Certo che ce la fai! · Non ce la faccio più. · Ce l'hai fatta! · Quanto ci hai messo? · Ce n'è un piatto."),
                        ("PRONUNCIA", "ce la faccio, ce l'ho fatta: tutto insieme")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: la gara", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Fai sport? Quale? Quante volte alla settimana?</li><li>Hai mai partecipato a una gara? Com'è andata?</li><li>Secondo te, chi corre una maratona è un po' matto?</li></ol>""",
    28, """<ol><li>A: <i>il traguardo</i> = la linea di arrivo (anche un obiettivo: <i>un traguardo importante</i>); <i>il pettorale</i> = il numero sulla maglietta; <i>la borraccia</i> = la bottiglia per l'acqua dello sport.</li>
<li>B: domanda 2: <i>partecipare a</i>; anticipare <i>ce l'ho fatta / non ce l'ho fatta</i> se lo studente racconta.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: la maratona</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La sera prima · al 30° km · all'arrivo</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Farcela · metterci · ce n'è</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Ce la faccio, ce l'ho fatta · ci metto, ci vuole</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Tutto insieme · che cosa vuol dire?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Farcela · quanto ci metti? · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Ce l'ho fatta! · sfide e tempi</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine ottobre. È il giorno della prima maratona di Davide: si allena da febbraio, ogni mattina alle sei (unità A2 07). Sabato sera, al bar, ha paura: <i>Secondo voi ce la faccio?</i> Per dieci chilometri ci mette cinquanta minuti; il suo obiettivo è finire in meno di quattro ore. Non ci sono più panini, ma c'è ancora la pasta: <i>ce n'è un piatto pieno</i>. Domenica Júlia e Marco lo aspettano al trentesimo chilometro con i cartelli: <i>Non ce la faccio più!</i> — <i>Dai, ne mancano solo dodici!</i> All'arrivo Giulia: <i>Ce l'hai fatta!</i> Tre ore e cinquantotto minuti. Il giorno dopo il bar lo apre lei.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese dice <i>consegui, dá pra fazer?</i> e <i>demorei três horas, leva uma hora</i>. Lo studente traduce parola per parola: <i>ho demorato tre ore</i>, <i>prende un'ora</i>, <i>ho messo tre ore</i> (senza <i>ci</i>). Con <i>farcela</i> sbaglia il pronome (<i>ce lo faccio</i>) e il participio (<i>ce l'ho fatto</i>). Insegnare le frasi come blocchi fissi.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia le maratone sono sempre più popolari: le più famose sono quelle di Roma (marzo), Venezia (ottobre) e Firenze (novembre). La sera prima molti corridori mangiano un grande piatto di pasta. Lungo il percorso la gente fa il tifo con i cartelli e grida <i>Forza! Dai! Vai così!</i></div>
<div class="box"><h4>AUDIO</h4>Traccia 32.1 I dialoghi (lento e naturale) · Traccia 32.2 Ascolta e ripeti · Traccia 32.3 Che cosa vuol dire?</div>""")

    # Page 2
    p1 = [("Davide si allena da", "febbraio"), ("Per dieci chilometri ci mette", "cinquanta minuti"), ("Per trenta chilometri ci ha messo", "tre ore"),
          ("Il suo obiettivo: finire in meno di", "quattro ore"), ("Júlia e Marco lo aspettano al", "trentesimo chilometro")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("Al trentesimo chilometro Davide sta benissimo.", "F"), ("Mancano dodici chilometri.", "V"), ("Davide ci ha messo più di quattro ore.", "F"),
          ("Giulia è orgogliosa di Davide.", "V"), ("Il giorno dopo Davide apre il bar.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: la prima maratona", "10 min")}
{audiocard(["32.1 · SLOW", "32.1 · NATURAL"])}
{sub("A", "Prima parte. Sabato sera, al bar. Completa.", "4 min", "32.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Domenica, la gara. Vero (V) o falso (F)?", "4 min", "32.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Quanto ci ha messo Davide? Che cosa vuole fare l'anno prossimo?", "2 min")}
<div class="wline">{R("Tre ore e cinquantotto minuti. Vuole rifare la maratona.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. La maratona di Davide è un progetto dell'unità A2 07 (allenamento da febbraio, sveglia alle sei).</li>
<li>B: frase 1: <i>Non ce la faccio più</i>. Frase 5: il bar lo apre <i>Giulia</i>.</li></ol>""")

    # Page 3
    rules = [("<i>Ce la faccio</i> vuol dire", ["riesco", "faccio una cosa"], "riesco"),
             ("<i>Non ce la faccio più</i> vuol dire", ["sono stanchissimo", "ho finito il lavoro"], "sono stanchissimo"),
             ("Al passato prossimo: <i>Ce l'hai</i>", ["fatta", "fatto"], "fatta"),
             ("<i>Ci ho messo tre ore</i> dice", ["il tempo che ho usato", "dove ho messo una cosa"], "il tempo che ho usato"),
             ("<i>Quanto ci metti?</i> chiede", ["il tempo", "il prezzo"], "il tempo"),
             ("<i>Ci sono panini? — Non ce ne sono più.</i> <i>Ne</i> =", ["i panini", "il bar"], "i panini")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Secondo te", ["ce la faccio", "ce lo faccio"], "ce la faccio", "?"), ("Brava,", ["ce l'hai fatta", "ce l'hai fatto"], "ce l'hai fatta", "!"),
          ("Per arrivare al lavoro", ["ci metto", "metto"], "ci metto", "mezz'ora."), ("C'è pane? — No, non", ["ce n'è", "ce ne sono"], "ce n'è", "più.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" ?", "?").replace(" !", "!") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: ce la faccio · ci metto", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Secondo voi <b>ce la faccio</b>? — Certo che <b>ce la fai</b>! · <b>Ce la puoi fare!</b> · <b>Non ce la faccio più!</b> · <b>Ce l'hai fatta!</b><br>
2. Quanto <b>ci metti</b> a fare dieci chilometri? — <b>Ci metto</b> cinquanta minuti. · Quanto <b>ci hai messo</b>? · <b>Ci ho messo</b> tre ore.<br>
3. Ci sono ancora panini? — No, non <b>ce ne sono</b> più. · C'è ancora un po' d'acqua? — Sì, <b>ce n'è</b> una bottiglia.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>Farcela</b> = riuscire: <i>ce la faccio, ce la fai, ce la fa…</i>; passato <i>ce l'ho fatt<b>a</b></i>. <b>Metterci</b> = usare tempo: <i>ci metto un'ora, ci ho messo tre ore</i> (oppure <i>ci vuole un'ora, ci vogliono tre ore</i>). <b>Ce n'è / ce ne sono</b> = c'è / ci sono + <i>ne</i> (unità 14). Tutto: pagina 4.</div>""",
    22, """<ol><li>A: far ripetere i blocchi ad alta voce, come espressioni fisse: non analizzare i pronomi.</li>
<li>B: frase 3: <i>fatta</i> perché c'è <i>la</i> (<i>ce l'</i> = <i>ce la</i>), come <i>la mostra? l'ho vista</i> (unità 11).</li></ol>""")

    grammar_ref_it.farcela_metterci(b)

    # Page 5
    opts3 = [["sono stanco", "ho tempo"], ["è durato tre ore", "ho messo tre cose"], ["siamo riusciti", "abbiamo fatto una torta"],
             ["è finito", "è arrivato"], ["quanto tempo?", "quanti soldi?"], ["ci sono tre cose", "voglio tre cose"]]
    ans3 = ["sono stanco", "è durato tre ore", "siamo riusciti", "è finito", "quanto tempo?", "ci sono tre cose"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ce lo faccio!</td><td><b>Ce la faccio!</b></td><td><i>Farcela</i>: sempre <i>la</i>.</td></tr>
<tr><td>Ce l'ho fatto!</td><td><b>Ce l'ho fatta!</b></td><td>Participio con la <i>a</i>.</td></tr>
<tr><td>Ho messo tre ore.</td><td><b>Ci ho messo tre ore.</b></td><td>Il tempo: <i>metterci</i>.</td></tr>
<tr><td>Ci vuole tre ore.</td><td><b>Ci vogliono tre ore.</b></td><td>Plurale: <i>vogliono</i>.</td></tr>
<tr><td>Ho demorato un'ora.</td><td><b>Ci ho messo un'ora.</b></td><td><i>Demorar</i> ≠ <i>dimorare</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["32.2", "32.3"])}
{sub("A", "Ascolta e ripeti. Si dice tutto insieme, come una parola sola: celafàccio, celhofàtta.", "2 min", "32.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S322)}</div>
{sub("B", "Che cosa vuol dire? Ascolta e scegli.", "2 min", "32.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: riga 5: <i>dimorare</i> in italiano esiste ma vuol dire <i>abitare</i> (raro). Per il tempo: <i>metterci</i> o <i>volerci</i>.</li>
<li>4A: l'accento è solo sul verbo; <i>ce la</i> e <i>ci</i> sono deboli.</li>
<li>4B: frase 6: <i>Ce ne sono tre</i> = ci sono tre (panini, bottiglie…).</li></ol>""")

    # Page 6
    fc = [("Marco,", "(tu)", "ce la fai", "a portare la valigia?"), ("Siamo stanchi: non", "(noi)", "ce la facciamo", "più."),
          ("Giulia", "(lei, passato)", "ce l'ha fatta", ": ha finito il corso."), ("Ragazzi,", "(voi)", "ce la fate", "a venire alle otto?"),
          ("Brava, Júlia!", "(tu, passato)", "Ce l'hai fatta", "!")]
    fcl = "".join(f"<li>{a} {A(r, 'min-width:26mm')} {z} <span class='small'>{h}</span></li>".replace(" :", ":").replace(" !", "!") for a, h, r, z in fc)
    qt = [("Quanto ci metti ad andare al lavoro? (20 minuti)", "Ci metto venti minuti."), ("Quanto ci hai messo a finire il libro? (una settimana)", "Ci ho messo una settimana."),
          ("Quanto ci mette Davide a fare 10 km? (50 minuti)", "Ci mette cinquanta minuti."), ("Quanto ci vuole da Bologna a Firenze in treno? (40 minuti)", "Ci vogliono quaranta minuti.")]
    qtl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in qt)
    wb = [("correre", "la corsa"), ("allenarsi", "l'allenamento"), ("arrivare", "l'arrivo"), ("partire", "la partenza")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Completa con farcela.", "3 min")}
<ol style="line-height:1.7">{fcl}</ol>
{sub("B", "Rispondi con ci metto, ci ho messo o ci vuole / ci vogliono.", "4 min")}
<ol style="line-height:1.4">{qtl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 3: <i>ce l'ha fatta</i> = è riuscita. Ricordare la <i>a</i> finale del participio.</li>
<li>B: con la persona → <i>metterci</i>; senza persona → <i>ci vuole / ci vogliono</i>.</li>
<li>C: <i>la partenza e l'arrivo della maratona</i>.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Ce l'ho fatta! Racconta all'insegnante una sfida della tua vita: un esame, uno sport, un lavoro, una lingua. Quanto tempo ci hai messo? Quando hai pensato «non ce la faccio più»? Chi ti ha detto «ce la puoi fare»? L'insegnante fa domande. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Ci ho messo… · All'inizio non ce la facevo. · Volevo smettere, ma… · Alla fine ce l'ho fatta! · Sono orgoglioso/a di me. · Ce la puoi fare! · Forza! · Dai! · Vai così!</div>
{sub("B", "Sfide e tempi. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Quanto ci metti ad arrivare al lavoro o a scuola?</li><li>Che cosa ci vuole per imparare bene una lingua?</li><li>Qual è la cosa più difficile che hai fatto? Ce l'hai fatta subito?</li><li>Quando non ce la fai più, che cosa fai?</li><li>Correresti una maratona? Perché sì o perché no?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: modello dell'insegnante: <i>Per l'esame di guida ci ho messo tre mesi. La prima volta non ce l'ho fatta…</i>; imperfetto + passato prossimo (unità 03).</li>
<li>B: domanda 5: <i>correresti</i> = condizionale (unità 05).</li></ol>""")

    # Page 8
    pc = [("A2 · 31", "So usare gli ordinali e i secoli."), ("A2 · 32", "So dire ce la faccio e non ce la faccio più."),
          ("A2 · 32", "So dire quanto tempo ci metto (ci vuole)."), ("A2 · 32", "So usare ce n'è e ce ne sono."),
          ("A2 · 32", "So incoraggiare una persona (Forza! Ce la puoi fare!).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ce lo faccio!", "Ce la faccio!"), ("Ce l'abbiamo fatta!", "✓"), ("Ho messo due ore per arrivare.", "Ci ho messo due ore per arrivare."),
          ("Ci vuole tre giorni.", "Ci vogliono tre giorni."), ("Non ce la faccio più.", "✓"), ("Ho demorato molto.", "Ci ho messo molto.")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Ce l'ho fatta! (50–75 parole).</b> Racconta una sfida che hai vinto: che cosa volevi fare, quanto tempo ci hai messo, quando hai pensato di non farcela, chi ti ha aiutato. Usa <i>ce l'ho fatta, ci ho messo, non ce la facevo</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il testo; l'insegnante chiede <i>E quanto ci hai messo?</i> Unità 33: <i>Ci siamo conosciuti così</i> (i verbi reciproci: ci siamo conosciuti; mentre + imperfetto, quando + passato prossimo).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("32.1", "I dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("32.2", "Ascolta e ripeti")}
<p>{" · ".join(S322)}</p>
{sub("32.3", "Che cosa vuol dire?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S323))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 32 - Ce la faccio!")
