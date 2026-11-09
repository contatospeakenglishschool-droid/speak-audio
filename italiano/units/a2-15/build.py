# Speak! Ponte A2 - Unità 15 "Sto lavorando!" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 15", audio_json=os.path.join(HERE, "audio_it-a2-unita-15.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "passare l'aspirapolvere", "aspirapolvere"), ("B", "lavare i piatti", "lavare i piatti"), ("C", "stendere il bucato", "stendere"),
          ("D", "fare il letto", "fare il letto"), ("E", "lavare i pavimenti", "pavimenti"), ("F", "stirare", "stirare"),
          ("G", "buttare la spazzatura", "spazzatura"), ("H", "apparecchiare la tavola", "apparecchiare")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-15"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["15.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S152 = [x.split(": ", 1)[1] for x in _r["15.2 Ripeti"].split("\n")]
S153 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["15.3 Adesso o tra poco"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 15", "Sto lavorando!", "Le faccende di casa · <b>stare + gerundio · stare per + infinito</b>",
                       [("SAI FARE", "parlare delle faccende di casa, dire che cosa stai facendo in questo momento e che cosa stai per fare"),
                        ("LINGUA", "Che cosa stai facendo? · Sto pulendo la casa. · Stiamo arrivando! · Sto per uscire. · Sta per cadere!"),
                        ("PRONUNCIA", "l'accento del gerundio: pulèndo, facèndo, arrivàndo")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: le faccende di casa", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi l'azione sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali faccende fai tu a casa? Quali non fai mai?</li><li>Quale faccenda ti piace di più? Quale odi?</li><li>Quando fai le pulizie: il sabato, la sera, mai?</li></ol>""",
    24, """<ol><li>A: <i>le faccende (di casa)</i> = i lavori di casa; <i>fare le pulizie</i> = pulire tutta la casa. <i>Il bucato</i> = i vestiti lavati; <i>stendere</i> = metterli ad asciugare.</li>
<li>B: accettare il presente (<i>Lavo i piatti ogni sera</i>): il gerundio arriva a pagina 2.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: le faccende di casa</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Una telefonata · la vicina alla porta · gli ospiti arrivano</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>stare + gerundio · stare per + infinito</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Forma, gerundi irregolari, pronomi, adesso o tra poco?</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'accento del gerundio · adesso o tra poco?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Che cosa stanno facendo? · che cosa sta per succedere? · gli elettrodomestici</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Indovina l'azione · una telefonata nel momento sbagliato</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine maggio, sabato. Stasera Giulia e Davide vengono a cena da Júlia, che pulisce tutta la casa. Marco telefona: sta bevendo un caffè sul balcone e sta per andare in palestra; nel pomeriggio aiuta Júlia e porta il vino. Suona la signora Rossi: l'aspirapolvere fa rumore da un'ora e Briciola (il fratello Franco è al mare) sta abbaiando. Júlia spegne l'aspirapolvere e lava i pavimenti; la sua maglietta sta per cadere dal balcone. Alle otto Davide telefona: stanno cercando parcheggio. Marco sta aprendo il vino, Júlia sta per buttare la pasta, Giulia porta una torta con le fragole del mercato (unità 14).</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese il gerundio si usa moltissimo (<i>estou morando, estou tendo, vou estar enviando</i>). In italiano <i>stare + gerundio</i> è solo per un'azione <b>proprio in corso</b>: <i>abito a Bologna</i> (non <i>sto abitando</i>), <i>ho un problema</i> (non <i>sto avendo</i>). <i>Stare per</i> = <i>estar prestes a / estar quase</i>: dopo <i>per</i> va l'<b>infinito</b> (<i>sto per uscire</i>, non <i>sto per uscendo</i>). Attenzione a <i>facendo</i> (con una c).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia il bucato si stende quasi sempre <b>sul balcone</b> o allo stendino: l'asciugatrice è poco comune. Nei condomini ci sono spesso regole sul rumore: niente lavori rumorosi la domenica e nelle ore di riposo (di solito 13–15 e dopo le 22). La raccolta differenziata è obbligatoria: carta, plastica, vetro, organico.</div>
<div class="box"><h4>AUDIO</h4>Traccia 15.1 I tre dialoghi (lento e naturale) · Traccia 15.2 Ascolta e ripeti · Traccia 15.3 Adesso o tra poco?</div>""")

    # Page 2
    p1 = [("Júlia sta", "pulendo la casa / passando l'aspirapolvere"), ("Marco sta", "bevendo un caffè sul balcone"), ("Marco sta per", "uscire / andare in palestra")]
    p1l = "".join(f"<li>{a} {A(x, 'min-width:70mm')}</li>" for a, x in p1)
    todo = ["lavare i piatti", "fare il letto", "stendere il bucato", "stirare", "fare la spesa"]
    todo_ok = {"lavare i piatti", "stendere il bucato", "fare la spesa"}
    tdl = " &nbsp; ".join((R("☑") if T and t in todo_ok else "☐") + f" {t}" for t in todo)
    vf = [("La signora Rossi sente il rumore da un'ora.", "V"), ("Franco sta dormendo.", "F"), ("Briciola sta abbaiando.", "V"),
          ("Júlia continua a passare l'aspirapolvere.", "F"), ("La maglietta di Júlia sta per cadere.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    p3 = [("Che cosa stanno facendo Davide e Giulia?", "Stanno cercando parcheggio."), ("Che cosa sta facendo Marco?", "Sta aprendo il vino."),
          ("Che cosa sta per fare Júlia?", "Sta per buttare la pasta.")]
    p3l = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in p3)
    b.page(f"""{sec(2, "Ascolto: un sabato di pulizie", "10 min")}
{audiocard(["15.1 · SLOW", "15.1 · NATURAL"])}
{sub("A", "Prima parte. Una telefonata. Completa le frasi.", "4 min", "15.1 · SLOW")}
<ol style="line-height:1.6">{p1l}</ol>
<p style="margin:1mm 0 0">Che cosa deve ancora fare Júlia? Segna tre faccende.</p>
<p style="margin:.5mm 0 0">{tdl}</p>
{sub("B", "Seconda parte. Alla porta. Vero (V) o falso (F)?", "3 min", "15.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Terza parte. Alle otto di sera. Rispondi.", "3 min")}
<ol style="line-height:1.6">{p3l}</ol>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Accettare risposte brevi (<i>pulendo</i>); B e C con la versione <b>naturale</b>.</li>
<li>B: frase 2: dorme Briciola? No: Franco è al mare e Briciola <i>sta abbaiando</i>. Chiedere: <i>Perché Briciola sta dalla signora Rossi?</i></li></ol>""")

    # Page 3
    rules = [("<i>Sto pulendo la casa.</i> L'azione è", ["in corso, adesso", "finita"], "in corso, adesso"),
             ("<i>Sto per uscire.</i> L'azione", ["comincia tra pochissimo", "è in corso"], "comincia tra pochissimo"),
             ("Nella forma <i>stare + gerundio</i> cambia", ["solo stare", "stare e il gerundio"], "solo stare"),
             ("I verbi in <i>-are</i> fanno il gerundio in", ["-ando", "-endo"], "-ando"),
             ("Il gerundio di <i>fare</i> è", ["facendo", "fando"], "facendo"),
             ("Dopo <i>stare per</i> c'è", ["l'infinito", "il gerundio"], "l'infinito")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Shh! Il bambino", ["sta dormendo", "sta per dormire"], "sta dormendo", "."),
          ("Prendi l'ombrello: ", ["sta per piovere", "sta piovendo"], "sta per piovere", ", il cielo è nero."),
          ("Corri! Il treno", ["sta per partire", "sta partendo"], "sta per partire", "tra un minuto."),
          ("Non posso parlare: ", ["sto guidando", "sto per guidare"], "sto guidando", ". Ti richiamo!")]
    ccl = "".join(f"<li>{a} {ch(o, r)}{z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: stare + gerundio, stare per", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Che cosa <b>stai facendo</b>? — <b>Sto pulendo</b> tutta la casa. · <b>Sto passando</b> l'aspirapolvere. · <b>Sto bevendo</b> un caffè.<br>
2. Che cosa <b>sta succedendo</b>? · Briciola <b>sta abbaiando</b>. · <b>Stanno suonando</b> alla porta. · <b>Stiamo arrivando</b>!<br>
3. <b>Sto per uscire</b>: vado in palestra. · La Sua maglietta <b>sta per cadere</b>! · <b>Sto per buttare</b> la pasta. · <b>Stiamo per suonare</b>!</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Adesso o tra poco? Scegli.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>stare + gerundio</b> = azione in corso adesso: <i>sto pulendo</i>. Gerundio: <i>-are → <b>-ando</b></i>, <i>-ere / -ire → <b>-endo</b></i>; <i>fare → facendo, bere → bevendo, dire → dicendo</i>. <b>stare per + infinito</b> = azione tra pochissimo: <i>sto per uscire</i>. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: chiedere l'equivalente in portoghese di <i>sto per uscire</i> (<i>estou quase saindo / estou prestes a sair</i>): in italiano mai il gerundio dopo <i>per</i>.</li>
<li>C: frase 2: il cielo è nero ma non piove ancora → <i>sta per piovere</i>.</li></ol>""")

    grammar_ref_it.stare_gerundio(b)

    # Page 5
    ans3 = ["adesso", "tra poco", "adesso", "tra poco", "adesso", "tra poco"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Sto abitando a Bologna da un anno.</td><td><b>Abito a Bologna da un anno.</b></td><td>Situazione lunga: presente.</td></tr>
<tr><td>Sto avendo un problema.</td><td><b>Ho un problema.</b></td><td><i>avere, essere</i>: no gerundio.</td></tr>
<tr><td>Sto per uscendo.</td><td><b>Sto per uscire.</b></td><td>Dopo <i>per</i>: infinito.</td></tr>
<tr><td>Che cosa stai fando?</td><td><b>Che cosa stai facendo?</b></td><td><i>fare → facendo</i>.</td></tr>
<tr><td>Le ragazze stanno arrivande.</td><td><b>Le ragazze stanno arrivando.</b></td><td>Il gerundio non cambia.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["15.2", "15.3"])}
{sub("A", "Ascolta e ripeti. Il gerundio ha l'accento su -àndo / -èndo: pulèndo, facèndo, arrivàndo.", "2 min", "15.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S152)}</div>
{sub("B", "Adesso (stare + gerundio) o tra poco (stare per)? Ascolta e scegli.", "2 min", "15.3")}
{twocol([f'<li value="{i+1}">{ch(["adesso", "tra poco"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>sto abitando, sto lavorando in uno studio</i> sono calchi del portoghese; in italiano: <i>abito, lavoro</i>. <i>Sto lavorando</i> va bene solo se l'azione è adesso (<i>Non posso uscire: sto lavorando!</i>).</li>
<li>4A: far battere le mani sulla sillaba accentata: <i>pu-LEN-do, fa-CEN-do</i>; non dire <i>fàcendo</i>.</li></ol>""")

    # Page 6
    qa = [("Davide / lavare i piatti", "Davide sta lavando i piatti."), ("io / stendere il bucato", "Sto stendendo il bucato."),
          ("Marco e Júlia / apparecchiare la tavola", "Marco e Júlia stanno apparecchiando la tavola."), ("tu / fare il letto?", "Stai facendo il letto?"),
          ("noi / bere un caffè", "Stiamo bevendo un caffè.")]
    qal = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in qa)
    sp = [("Sono le 19:59. Il film…", "sta per cominciare."), ("Sono le 6:59. La sveglia…", "sta per suonare."),
          ("La pasta è quasi pronta. Júlia…", "sta per mangiare."), ("Il telefono è al 2%. Si…", "sta per spegnere.")]
    spl = "".join(f"<li>{s} {A(a, 'min-width:42mm')}</li>" for s, a in sp)
    wb = [("lavare i piatti", "la lavastoviglie"), ("lavare i vestiti", "la lavatrice"), ("passare l'aspirapolvere", "l'aspirapolvere"), ("stirare", "il ferro da stiro")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:30mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Che cosa stanno facendo adesso? Scrivi la frase con stare + gerundio.", "4 min")}
<ol style="line-height:1.45">{qal}</ol>
{sub("B", "Che cosa sta per succedere? Completa con stare per.", "3 min")}
<ol style="line-height:1.7">{spl}</ol>
{sub("C", "Gli elettrodomestici. Che cosa usi per…?", "2 min")}
<div class="bank">il ferro da stiro &nbsp;·&nbsp; la lavastoviglie &nbsp;·&nbsp; la lavatrice &nbsp;·&nbsp; l'aspirapolvere</div>
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 2: <i>stendere → stendendo</i>; frase 4 è una domanda (<i>Stai facendo…?</i>). B: <i>stare per</i> + infinito; <i>si sta per spegnere</i> = <i>sta per spegnersi</i>.</li>
<li>C: chiedere: <i>Hai la lavastoviglie? Chi stira a casa tua?</i></li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Indovina! Mima un'azione di casa (o di ogni giorno). L'insegnante indovina: Stai stirando? Poi cambiate.", "4 min")}
<div class="box" style="margin-top:1mm"><h4>IDEE</h4>stirare · lavare i piatti · stendere il bucato · fare il letto · cucinare la pasta · leggere il giornale · fare la doccia · dormire · scrivere un messaggio · guidare</div>
{sub("B", "Una telefonata nel momento sbagliato. L'insegnante ti chiama sei volte. Rispondi: che cosa stai facendo? Che cosa stai per fare?", "5 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Pronto? · Scusa, adesso non posso: sto… · Sto per… · Ti richiamo tra cinque minuti! · Che cosa stai facendo? · Niente di speciale. · Vuoi una mano? · Stanno suonando alla porta!</div>
{sub("C", "Le faccende a casa tua. Chi fa che cosa? Quale faccenda odi? Che cosa stanno facendo adesso le persone della tua famiglia?", "3 min")}
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>B: chiamare in momenti diversi: <i>sabato alle 8, lunedì alle 13, venerdì alle 23…</i> Lo studente inventa; pretendere una frase con <i>stare + gerundio</i> e una con <i>stare per</i>.</li>
<li>C: per le persone lontane va bene immaginare: <i>Adesso mia madre sta lavorando, credo.</i></li></ol>""")

    # Page 8
    pc = [("A2 · 14", "So usare ne con le quantità e ci con i luoghi."), ("A2 · 15", "So parlare delle faccende di casa."),
          ("A2 · 15", "So dire che cosa sto facendo adesso (sto pulendo)."), ("A2 · 15", "So dire che cosa sto per fare (sto per uscire)."),
          ("A2 · 15", "So rispondere al telefono in un momento difficile.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Sto abitando a Bologna.", "Abito a Bologna."), ("Shh, Franco sta dormendo.", "✓"),
          ("Sto per uscendo.", "Sto per uscire."), ("Che cosa stai fando?", "Che cosa stai facendo?"),
          ("Le ragazze stanno arrivande.", "stanno arrivando"), ("Sta per piovere.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Sabato mattina a casa mia (50–75 parole).</b> Scrivi un messaggio a un amico: che cosa stai facendo adesso? Che cosa stanno facendo le altre persone di casa? Che cosa stai per fare? Usa <i>stare + gerundio</i> e <i>stare per</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il messaggio; l'insegnante chiede <i>E adesso, che cosa stai facendo?</i> Unità 16: <i>La città che vorrei</i> (che e cui).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("15.1", "I tre dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("15.2", "Ascolta e ripeti")}
<p>{" · ".join(S152)}</p>
{sub("15.3", "Adesso o tra poco?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S153))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 15 - Sto lavorando")
