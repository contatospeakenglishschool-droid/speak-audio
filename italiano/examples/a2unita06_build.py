# Speak! Ponte A2 - Unità 06 "Un colloquio di lavoro" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 06", audio_json=os.path.join(HERE, "audio_it-a2-unita-06.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il curriculum", "curriculum"), ("B", "il colloquio", "colloquio"), ("C", "la macchina del caffè", "macchina del caffè"), ("D", "il latte art", "latte art"),
          ("E", "gli annunci", "annunci"), ("F", "i colleghi", "colleghi"), ("G", "il grembiule", "grembiule"), ("H", "il portatile", "portatile")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-06"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["06.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S062 = [x.split(": ", 1)[1] for x in _r["06.2 Ripeti conoscere"].split("\n")]
S063 = [x.split(": ", 1)[1] for x in _r["06.3 Suono dolce o duro"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 06", "Un colloquio di lavoro", "Il lavoro e le capacità · <b>sapere e conoscere, ci vuole, i modali al passato</b>",
                       [("SAI FARE", "parlare delle tue capacità e della tua esperienza in un colloquio di lavoro"),
                        ("LINGUA", "So parlare inglese. · Conosco la zona. · Ci vogliono cinque minuti. · Sono dovuto tornare."),
                        ("PRONUNCIA", "conosco o conosci? · sc dolce o duro")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: cercasi personale", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Che lavoro fai? Che cosa usi nel tuo lavoro?</li><li>Hai mai fatto un colloquio di lavoro? Com'è andato?</li><li>Che lavoro non vorresti mai fare? Perché?</li></ol>""",
    22, """<ol><li>A: <i>il curriculum</i> (o <i>CV</i>); <i>gli annunci</i> di lavoro dicono <i>cercasi barista</i>. <i>Il portatile</i> = il computer portatile.</li>
<li>B: domanda 3: ripasso del condizionale (unità 05).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il mondo del lavoro</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Giulia cerca un barista · il colloquio di Matteo · la prova</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Sapere e conoscere · ci vuole / ci vogliono · i modali al passato</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Usi di sapere e conoscere · ci vuole · ausiliare dei modali</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Conosco, conosci · sc dolce o duro</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Modali al passato · quanto tempo ci vuole? · le parole del lavoro</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Il colloquio (gioco di ruolo) · sai…? conosci…?</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Metà gennaio. Dopo le feste il bar di Giulia è sempre pieno: ci vuole una persona in più per il fine settimana. Davide conosce Matteo, il cugino di un collega: sa fare un cappuccino perfetto, sa parlare inglese e spagnolo e ha lavorato due anni in un hotel a Londra. Al colloquio Matteo racconta che è dovuto tornare a Bologna perché sua nonna è stata male. Abita in via Zamboni e conosce bene la zona. Sabato fa la prova: cento cappuccini, e un'ora da solo perché Giulia è dovuta andare in banca. Giulia ha saputo che Matteo vuole imparare il portoghese: Júlia si offre come insegnante.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>La coppia <i>saber / conhecer</i> esiste anche in portoghese, quindi l'uso è chiaro. Gli errori: <i>ci vuole</i> con il plurale (<i>leva cinco minutos</i> → <b>ci vogliono</b> cinque minuti), l'ausiliare dei modali (<i>ho dovuto andata</i> → <b>sono dovuta andare</b>) e la pronuncia di <i>conosci</i> [sci] diversa da <i>conosco</i> [sk].</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Per lavorare in un bar in Italia bisogna fare un corso <b>HACCP</b> (igiene degli alimenti). Spesso il primo giorno è una <b>prova</b>, a volte non pagata. Nei colloqui si usa il <b>Lei</b>. Via Zamboni è il cuore della zona universitaria di Bologna, l'università più antica del mondo occidentale (1088).</div>
<div class="box"><h4>AUDIO</h4>Traccia 06.1 Tre dialoghi (lento e naturale) · Traccia 06.2 Conoscere · Traccia 06.3 Sc dolce o duro?</div>""")

    # Page 2
    st = [("Perché Giulia ha bisogno di aiuto?", "dopo le feste il bar è sempre pieno"), ("Che cosa sa fare Matteo, secondo Davide?", "un cappuccino perfetto; parlare inglese e spagnolo"),
          ("Dove ha lavorato Matteo? Per quanto tempo?", "in un hotel a Londra, due anni")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    vf = [("Matteo è arrivato tardi al colloquio.", "V"), ("È tornato in Italia perché non gli piaceva Londra.", "F"),
          ("Matteo conosce la macchina del caffè di Giulia.", "F"), ("Matteo abita vicino al bar, in via Zamboni.", "V"), ("Il lavoro è dal lunedì al venerdì.", "F")]
    vfl = "".join(f"<tr><td>{s}</td><td style='width:14mm;text-align:center'>{A(v, 'min-width:7mm')}</td></tr>" for s, v in vf)
    b.page(f"""{sec(2, "Ascolto: cercasi barista", "10 min")}
<p>Giulia cerca una persona per il bar, Davide conosce il ragazzo giusto e Matteo fa il colloquio.</p>
{audiocard(["06.1 · SLOW", "06.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "06.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Il colloquio. Vero (V) o falso (F)?", "4 min", "06.1 · NATURAL")}
<table style="margin:0">{vfl}</table>
{sub("C", "Dialogo 3. Com'è andata la prova? Che cosa ha saputo Giulia?", "3 min")}
<div class="wline">{R("benissimo: cento cappuccini · Matteo vuole imparare il portoghese, vorrebbe lavorare a Lisbona")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Far notare <i>sa fare</i> (capacità) e <i>conosco un ragazzo</i> (persona).</li>
<li>B: versione <b>naturale</b>. 2: <i>sua nonna è stata male e <b>è dovuto</b> tornare</i>. Correggere le frasi false.</li></ol>""")

    # Page 3
    rules = [("<i>Sa fare un cappuccino</i>: <b>sapere</b> + infinito indica", ["una capacità", "una persona"], "una capacità"),
             ("Con persone e luoghi (<i>un ragazzo, il quartiere</i>) usiamo", ["sapere", "conoscere"], "conoscere"),
             ("Dopo <i>non so</i> e <i>sai</i> possono venire", ["se, perché, dove", "un nome di persona"], "se, perché, dove"),
             ("Con un plurale (<i>settimane, cinque minuti</i>) diciamo", ["ci vuole", "ci vogliono"], "ci vogliono"),
             ("<i>Sono dovuto tornare</i>: il modale prende l'ausiliare", ["del verbo all'infinito", "sempre avere"], "del verbo all'infinito"),
             ("<i>Ho saputo che…</i> al passato prossimo vuol dire", ["ho scoperto", "sapevo da sempre"], "ho scoperto")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Matteo", "sa", " fare il latte art."), ("Giulia non", "conosce", " Matteo."), ("", "Sai", " dov'è via Zamboni?"),
          ("Júlia", "sa", " parlare tre lingue."), ("", "Conosci", " un buon ristorante?"), ("Non", "so", " perché è tornato.")]
    opts = {"sa": ["sa", "conosce"], "conosce": ["sa", "conosce"], "Sai": ["Sai", "Conosci"], "Conosci": ["Sai", "Conosci"], "so": ["so", "conosco"]}
    ccl = [f'<li value="{i+1}">{a} {ch(opts[c], c)}{z}</li>' for i, (a, c, z) in enumerate(cc)]
    b.page(f"""{sec(3, "Grammatica: sapere, conoscere, ci vuole", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Matteo <b>sa fare</b> un cappuccino perfetto e <b>sa parlare</b> inglese. · <b>Non so</b> perché è tornato. · <b>Sai se</b> ha esperienza?<br>
2. <b>Conosco</b> un ragazzo, Matteo. · <b>Conosco</b> bene la zona universitaria. · Questa macchina non la <b>conosco</b>.<br>
3. <b>Ci vuole</b> una persona in più. · <b>Ci vogliono</b> settimane. · <b>Ci vogliono</b> cinque minuti per imparare.<br>
4. <b>Sono dovuto tornare</b> a Bologna. · Matteo <b>ha dovuto lavorare</b> da solo. · Oggi <b>ho saputo</b> che vuole imparare il portoghese.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Sapere o conoscere? Scegli.", "3 min")}
{twocol(ccl, 4)}
<div class="box sand"><h4>REGOLA</h4><b>sapere</b> + infinito (una capacità) o + <i>che, se, dove, perché</i> (un'informazione). <b>conoscere</b> + persone, luoghi, cose. <b>ci vuole</b> + singolare · <b>ci vogliono</b> + plurale. <b>dovere, potere, volere</b> al passato prossimo prendono l'ausiliare del verbo all'infinito: <i>ho dovuto lavorare · sono dovuta andare</i>. Tutto: pagina 4.</div>""",
    20, """<ol><li>B: domanda chiave per lo studente: <i>è una persona o un posto?</i> → <i>conoscere</i>.</li>
<li>C: 3: <i>sapere dove</i>; ma <i>conosci via Zamboni?</i> (il luogo) è corretto.</li></ol>""")

    grammar_ref_it.sapere_conoscere(b)

    # Page 5
    ans3 = ["duro [sk]", "dolce [sci]", "duro [sk]", "dolce [sci]", "duro [sk]", "dolce [sci]"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>So Matteo da un anno.</td><td><b>Conosco Matteo da un anno.</b></td><td>Persona → <i>conoscere</i>.</td></tr>
<tr><td>Conosco cucinare.</td><td><b>So cucinare.</b></td><td>Capacità → <i>sapere</i>.</td></tr>
<tr><td>Ci vuole due ore.</td><td><b>Ci vogliono due ore.</b></td><td>Plurale → <i>ci vogliono</i>.</td></tr>
<tr><td>Sai Bologna?</td><td><b>Conosci Bologna?</b></td><td>Luogo → <i>conoscere</i>.</td></tr>
<tr><td>Giulia ha dovuto andata in banca.</td><td><b>Giulia è dovuta andare in banca.</b></td><td>Modale + infinito.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["06.2", "06.3"])}
{sub("A", "Conoscere. Ascolta e ripeti: cono-SCO [sk], cono-SCI [sci].", "2 min", "06.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S062)}</div>
{sub("B", "Sc dolce o duro? Ascolta e scegli.", "2 min", "06.3")}
{twocol([f'<li value="{i+1}">{ch(["duro [sk]", "dolce [sci]"], a)}</li>' for i, a in enumerate(ans3)], 4)}
<p class="small" style="margin:1mm 0">Regola: <b>sc + e, i</b> = [sci] (<i>pesce, uscire</i>) · <b>sc + a, o, u</b> = [sk] (<i>tasca, conosco, scuola</i>).</p>""",
    28, """<ol><li>Errori: <i>ho dovuto andare</i> si sente nel parlato; nello scritto meglio <i>sono dovuta andare</i>.</li>
<li>4B: le parole sono 1 conosco, 2 conosci, 3 scuola, 4 pesce, 5 tasca, 6 uscire.</li></ol>""")

    # Page 6
    md = [("Ieri Giulia (dovere) ", "è dovuta", " andare in banca."), ("Matteo (dovere) ", "ha dovuto", " lavorare da solo."),
          ("Volevo venire alla festa, ma non (potere) ", "ho potuto", "."), ("Bruno (volere) ", "ha voluto", " studiare tutta la notte."),
          ("Noi (dovere) ", "siamo dovuti", " partire presto.")]
    mdl = "".join(f"<li>{a}{A(c, 'min-width:24mm')}{z}</li>" for a, c, z in md)
    cv = [("Per arrivare a Roma in treno", "ci vogliono", "due ore e mezza"), ("Per fare un buon ragù", "ci vogliono", "tre ore"),
          ("Per fare un cappuccino", "ci vuole", "un minuto"), ("Per imparare una lingua", "ci vuole", "pazienza")]
    cvl = "".join(f"<li>{a} {ch(['ci vuole', 'ci vogliono'], c)} {z}.</li>" for a, c, z in cv)
    wb = [("il colloquio", "l'incontro per un nuovo lavoro"), ("l'esperienza", "il lavoro che hai già fatto"), ("lo stipendio", "i soldi che ricevi ogni mese"),
          ("il turno", "le ore di lavoro: «il … di sabato»"), ("assumere", "dare un lavoro a una persona"), ("la prova", "il primo giorno per vedere se va bene"),
          ("il cliente", "la persona che compra al bar"), ("il collega", "una persona che lavora con te")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:21mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "I modali al passato. Scrivi il passato prossimo.", "3 min")}
<ol style="line-height:1.75">{mdl}</ol>
{sub("B", "Quanto tempo ci vuole? Scegli. Poi scrivi due frasi su di te.", "3 min")}
<ol style="line-height:1.6">{cvl}</ol>
<div class="wline">{R("Per arrivare al lavoro ci vogliono venti minuti.")}</div>
{sub("C", "Le parole del lavoro. Scrivi la parola giusta.", "3 min")}
<div class="bank">assumere · il cliente · il collega · il colloquio · l'esperienza · la prova · lo stipendio · il turno</div>
{twocol(wbl, 5)}""",
    20, """<ol><li>A: 1 e 5 con <i>essere</i> (andare, partire): accordo del participio. 4: <i>ha voluto</i> = l'ha fatto.</li>
<li>B: far rispondere a voce: <i>Quanto tempo ci vuole per…?</i></li></ol>""")

    # Page 7
    ads = [("CERCASI BARISTA", "Bar in centro · sabato e domenica · inglese · esperienza"),
           ("CERCASI GUIDA TURISTICA", "Bologna · turisti brasiliani · italiano e portoghese · aprile–ottobre"),
           ("CERCASI BABY-SITTER", "tre pomeriggi alla settimana · due bambini di 4 e 7 anni")]
    al = "".join(f'<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b style="color:#176074">{t}</b><br>{d}</div>' for t, d in ads)
    sk = ["(sapere) cucinare un piatto italiano", "(conoscere) Roma", "(sapere) guidare", "(conoscere) un italiano famoso",
          "(sapere) suonare uno strumento", "(conoscere) un buon ristorante qui", "(sapere) quante regioni ha l'Italia", "(conoscere) qualcuno che vive in Italia"]
    skl = [f'<li value="{i+1}">{s}</li>' for i, s in enumerate(sk)]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Il colloquio. Scegli un annuncio. L'insegnante fa il colloquio (con il Lei); tu rispondi. Poi cambiate.", "7 min")}
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5mm;margin-top:1mm">{al}</div>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>DOMANDE UTILI</h4>Che esperienza ha? · Che cosa sa fare? · Sa parlare…? · Conosce…? · Perché vorrebbe questo lavoro? · Quando potrebbe cominciare? · Ha domande? · Quanto è lo stipendio? · Qual è l'orario?</div>
{sub("B", "Sai…? Conosci…? Fai le domande all'insegnante, poi rispondi tu.", "5 min")}
{twocol(skl, 5)}""",
    22, """<ol><li>A: l'insegnante usa il <i>Lei</i>; lo studente racconta l'esperienza con il passato prossimo (<i>ho lavorato…, sono dovuto/a…</i>).</li>
<li>B: lo studente forma la domanda: <i>Sai guidare? Conosci Roma?</i> Rispondere con una frase completa.</li></ol>""")

    # Page 8
    pc = [("A2 · 04", "So dare consigli con l'imperativo (tu, voi)."), ("A2 · 05", "So chiedere in modo gentile con il condizionale."),
          ("A2 · 06", "So usare sapere e conoscere."), ("A2 · 06", "So dire quanto tempo ci vuole: ci vuole / ci vogliono."),
          ("A2 · 06", "So parlare della mia esperienza in un colloquio di lavoro.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("So bene questa città.", "Conosco bene questa città."), ("Sai se Matteo lavora domani?", "✓"),
          ("Ci vuole tre giorni per arrivare.", "Ci vogliono tre giorni…"), ("Conosci nuotare?", "Sai nuotare?"),
          ("Ieri sono dovuta uscire presto.", "✓"), ("Ho conosciuto la notizia oggi.", "Ho saputo la notizia oggi.")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:44mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Rispondi a un annuncio (50–75 parole).</b> Scegli un annuncio della pagina 7 e scrivi un'e-mail: presentati, racconta la tua esperienza, che cosa sai fare, che cosa conosci e quando potresti cominciare.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge l'e-mail; l'insegnante risponde come datore di lavoro e fissa un colloquio. Unità 07: <i>Progetti</i>.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("06.1", "Cercasi barista (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("06.2", "Conoscere")}
<p>{" · ".join(S062)}</p>
{sub("06.3", "Sc dolce o duro?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S063))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 06 - Un colloquio di lavoro")
