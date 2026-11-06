# Speak! Ponte A2 - Unità 05 "Vorrei, potrei…" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 05", audio_json=os.path.join(HERE, "audio_it-a2-unita-05.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il panettone", "panettone"), ("B", "la videochiamata", "videochiamata"), ("C", "il biglietto aereo", "biglietto aereo"), ("D", "sciare", "sciare"),
          ("E", "il treno", "treno"), ("F", "la riunione", "riunione"), ("G", "il cappuccino", "cappuccino"), ("H", "l'albero di Natale", "albero di Natale")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-05"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["05.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S052 = [x.split(": ", 1)[1] for x in _r["05.2 Ripeti le doppie"].split("\n")]
S053 = [x.split(": ", 1)[1] for x in _r["05.3 Presente o condizionale"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 05", "Vorrei, potrei…", "Richieste gentili, desideri e consigli · <b>il condizionale presente</b>",
                       [("SAI FARE", "chiedere un favore in modo gentile, parlare dei tuoi desideri e dare consigli"),
                        ("LINGUA", "Potresti farmi un favore? · Mi piacerebbe sciare. · Al tuo posto, io…"),
                        ("PRONUNCIA", "le doppie del condizionale · presente o condizionale?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: aspettando il Natale", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1] if not w.startswith("l'albero") else "albero"))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali di queste cose ci sono nel tuo dicembre?</li><li>Che cosa fai di solito a Natale? Con chi lo passi?</li><li>Fai spesso videochiamate? Con chi?</li></ol>""",
    22, """<ol><li>A: <i>il panettone</i> è il dolce di Natale di Milano; a Verona c'è il <i>pandoro</i>. <i>Sciare</i> è un verbo: <i>io scio</i>.</li>
<li>B: domande al presente; nell'ascolto arriva il condizionale per i desideri (<i>mi piacerebbe…</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: dicembre e Natale</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Un favore per Marco · i desideri per Natale · il consiglio della signora Rossi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Il condizionale presente: forme e usi</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Forme regolari · irregolari · cinque usi</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Le doppie: vorrei, potremmo · presente o condizionale?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Più gentile! · Al tuo posto… · parole della lezione</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Ti dispiacerebbe…? (gioco di ruolo) · che cosa faresti?</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio dicembre. Allo studio Marco chiede a Júlia due favori: preparare la presentazione per un cliente di Milano e andarlo a prendere alla stazione. Júlia accetta, ma alle dieci <i>avrebbe</i> il dentista: ci va alle undici. Al bar Giulia, Davide e Júlia parlano del Natale: Davide vorrebbe sciare in Trentino, Giulia vorrebbe chiudere il bar e dormire, Júlia vorrebbe tornare in Brasile, ma il biglietto costa 1800 euro. Davide propone una cena tutti insieme la vigilia. La sera la signora Rossi consiglia a Júlia una videochiamata e un volo a febbraio, e la invita a pranzo il giorno di Natale con Franco e Briciola. Júlia chiede di portare anche Bruno.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>L'uso è uguale al portoghese (<i>eu gostaria, você poderia</i>). Gli errori sono di forma: <i>parlarei, comprarei</i> (→ <b>parlerei, comprerei</b>), <i>poterei</i> (→ <b>potrei</b>), <i>mi piacerei</i> (→ <b>mi piacerebbe</b>). Al bar molti brasiliani dicono <i>voglio un caffè</i>: in italiano suona troppo diretto, meglio <b>vorrei</b> o <b>prendo</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>A Natale gli italiani mangiano <b>panettone</b> o <b>pandoro</b>. La <b>vigilia</b> (24 dicembre) in molte famiglie si fa la cena di pesce; il 25 c'è il grande pranzo, spesso con i tortellini in brodo a Bologna. Dicono: <i>Natale con i tuoi, Pasqua con chi vuoi</i>. Il 26 è Santo Stefano, un altro giorno di festa.</div>
<div class="box"><h4>AUDIO</h4>Traccia 05.1 Tre dialoghi (lento e naturale) · Traccia 05.2 Le doppie del condizionale · Traccia 05.3 Presente o condizionale?</div>""")

    # Page 2
    st = [("Che cosa deve preparare Júlia?", "la presentazione per il cliente di Milano"), ("Che cosa le servirebbe? Perché?", "il computer di Marco: il suo è lentissimo"),
          ("Perché Júlia non può andare alla stazione alle dieci?", "alle dieci avrebbe il dentista: ci va alle undici")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    who = [("Mi piacerebbe andare in montagna a sciare.", "Davide"), ("Vorrei chiudere il bar e dormire.", "Giulia"),
           ("Il biglietto costa milleottocento euro!", "Júlia"), ("Io non lo comprerei mai a quel prezzo!", "Davide"), ("Io porterei il panettone.", "Giulia")]
    wl = "".join(f"<tr><td>{s}</td><td style='width:26mm;text-align:center'>{A(w, 'min-width:18mm')}</td></tr>" for s, w in who)
    b.page(f"""{sec(2, "Ascolto: potresti farmi un favore?", "10 min")}
<p>Marco ha bisogno di aiuto, gli amici parlano del Natale e la signora Rossi ha un consiglio e un invito.</p>
{audiocard(["05.1 · SLOW", "05.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "05.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Chi lo dice? Davide, Giulia o Júlia?", "4 min", "05.1 · NATURAL")}
<table style="margin:0">{wl}</table>
{sub("C", "Dialogo 3. Quali consigli dà la signora Rossi? E che cosa propone a Júlia?", "3 min")}
<div class="wline">{R("una videochiamata la vigilia e un volo a febbraio · il pranzo di Natale da lei")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Far notare <i>avrei il dentista</i>: il condizionale rende il «no» più gentile.</li>
<li>B: versione <b>naturale</b>. Poi chiedere: <i>E a te, che cosa piacerebbe fare a Natale?</i></li></ol>""")

    # Page 3
    rules = [("<i>Potresti…?</i> e <i>Ti dispiacerebbe…?</i> servono per", ["chiedere in modo gentile", "dare un ordine"], "chiedere in modo gentile"),
             ("<i>Mi piacerebbe</i> e <i>vorrei tanto</i> esprimono", ["un desiderio", "un fatto del passato"], "un desiderio"),
             ("<i>Dovrebbe…</i> e <i>al suo posto, io…</i> servono per", ["dare un consiglio", "raccontare una storia"], "dare un consiglio"),
             ("Le desinenze sono <i>io -ei, tu -esti, lui -ebbe</i>; per <b>noi</b>:", ["-emmo", "-emo"], "-emmo"),
             ("Nei verbi in <b>-are</b> (<i>comprare, portare</i>) la <b>a</b> diventa", ["e", "i"], "e"),
             ("<i>potere, dovere, avere</i> diventano <i>potrei, dovrei, avrei</i>: perdono", ["una vocale", "una consonante"], "una vocale")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("(io, volere) ", "vorrei"), ("(tu, potere) ", "potresti"), ("(lei, preferire) ", "preferirebbe"),
          ("(noi, andare) ", "andremmo"), ("(voi, dovere) ", "dovreste"), ("(loro, venire) ", "verrebbero")]
    ccl = [f'<li value="{i+1}">{a}{A(c, "min-width:26mm")}</li>' for i, (a, c) in enumerate(cc)]
    b.page(f"""{sec(3, "Grammatica: il condizionale presente", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Potresti</b> farmi un favore? · <b>Ti dispiacerebbe</b> andare alla stazione? · <b>Mi servirebbe</b> il tuo computer.<br>
2. <b>Mi piacerebbe</b> tanto andare in montagna. · <b>Vorrei</b> chiudere il bar e dormire!<br>
3. Al suo posto, io <b>farei</b> una videochiamata. · <b>Dovrebbe</b> cercare un volo per febbraio.<br>
4. <b>Potremmo</b> fare una cena tutti insieme! · Io <b>porterei</b> il panettone. · Io non lo <b>comprerei</b> mai!</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scrivi il condizionale.", "3 min")}
{twocol(ccl, 4)}
<div class="box sand"><h4>REGOLA</h4>Il <b>condizionale presente</b> serve per <b>chiedere in modo gentile</b> (<i>potresti…?</i>), esprimere un <b>desiderio</b> (<i>mi piacerebbe</i>), dare un <b>consiglio</b> (<i>dovresti</i>) e fare una <b>proposta</b> (<i>potremmo</i>). Desinenze: <b>-ei, -esti, -ebbe, -emmo, -este, -ebbero</b>; <i>-are</i> → <b>-erei</b>. Irregolari: <i>vorrei, potrei, dovrei, andrei, avrei, sarei, farei</i>. Tutte le forme: pagina 4.</div>""",
    20, """<ol><li>B: far trovare allo studente un esempio nei dialoghi per ogni regola.</li>
<li>C: 3: <i>preferire</i> è regolare (<i>preferirebbe</i>). 6: <i>venire → verrei</i>, doppia <b>r</b>.</li></ol>""")

    grammar_ref_it.condizionale_presente(b)

    # Page 5
    ans3 = ["condizionale", "presente", "condizionale", "presente", "condizionale", "presente"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Voglio un cappuccino. (al bar)</td><td><b>Vorrei un cappuccino.</b></td><td>Più gentile.</td></tr>
<tr><td>Io comprarei un biglietto.</td><td><b>Io comprerei un biglietto.</b></td><td><i>-are</i> → <i>-erei</i>.</td></tr>
<tr><td>Poteresti aiutarmi?</td><td><b>Potresti aiutarmi?</b></td><td>Irregolare: <i>potr-</i>.</td></tr>
<tr><td>Mi piacerei andare in montagna.</td><td><b>Mi piacerebbe andare in montagna.</b></td><td>Come <i>piacere</i>: 3ª persona.</td></tr>
<tr><td>Al tuo posto, io vado dal medico.</td><td><b>Al tuo posto, io andrei dal medico.</b></td><td>Consiglio: condizionale.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["05.2", "05.3"])}
{sub("A", "Le doppie del condizionale. Ascolta e ripeti: vo-RR-ei, piace-RE-BB-e, potre-MM-o.", "2 min", "05.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S052)}</div>
{sub("B", "Presente o condizionale? Ascolta e scegli.", "2 min", "05.3")}
{twocol([f'<li value="{i+1}">{ch(["presente", "condizionale"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>voglio</i> non è sbagliato, ma al bar o in negozio suona brusco. Vanno bene <i>vorrei</i> o <i>prendo</i>.</li>
<li>4B: poi lo studente trasforma le frasi al presente: <i>Puoi aiutarmi? → Potresti aiutarmi?</i></li></ol>""")

    # Page 6
    pg = [("Dammi il sale!", "Mi daresti il sale?"), ("Voglio un tè.", "Vorrei un tè."), ("Chiudi la porta!", "Potresti chiudere la porta?"),
          ("Mi presti la penna?", "Mi presteresti la penna?"), ("Aiutami con la valigia!", "Ti dispiacerebbe aiutarmi con la valigia?")]
    pgl = "".join(f"<li>{a} → {A(c, 'min-width:54mm')}</li>" for a, c in pg)
    pb = [("Sono sempre stanco.", "Dovresti andare a letto prima."), ("Il mio italiano non migliora.", "Al tuo posto, guarderei film in italiano."),
          ("Ho litigato con mia sorella.", "Dovresti telefonarle e chiederle scusa."), ("Non ho soldi per le vacanze.", "Al tuo posto, resterei a casa e risparmierei.")]
    left = "".join(f"<li>{a}</li>" for a, _ in pb)
    rgt = [pb[2][1], pb[0][1], pb[3][1], pb[1][1]]
    right = "".join(f"<div style='margin:0 0 .4mm'><b>{l}.</b> {x}</div>" for l, x in zip("abcd", rgt))
    wb = [("il volo", "il viaggio in aereo"), ("prenotare", "riservare un posto"), ("la vigilia", "il 24 dicembre"),
          ("il favore", "«Potresti farmi un …?»"), ("mancare", "«Mi … la mia famiglia»"), ("offrire", "«Ti … un caffè!»"),
          ("il consiglio", "«Al tuo posto, io…»"), ("risparmiare", "non spendere i soldi")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:19mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Più gentile! Riscrivi con il condizionale.", "3 min")}
<ol style="line-height:1.75">{pgl}</ol>
{sub("B", "Al tuo posto… Unisci il problema (1–4) al consiglio (a–d).", "3 min")}
<div class="two"><ol style="margin:0">{left}</ol><div>{right}</div></div>
<p class="small" style="margin:.5mm 0">{R("1 b · 2 d · 3 a · 4 c") if T else ""}</p>
{sub("C", "Le parole della lezione. Scrivi la parola giusta.", "3 min")}
<div class="bank">il consiglio · il favore · mancare · offrire · prenotare · risparmiare · la vigilia · il volo</div>
{twocol(wbl, 5)}""",
    20, """<ol><li>A: per la 5 vanno bene anche <i>Potresti aiutarmi…?</i> e <i>Mi aiuteresti…?</i></li>
<li>B: poi lo studente dà un altro consiglio per ogni problema. C: <i>mancare</i> funziona come <i>piacere</i>.</li></ol>""")

    # Page 7
    cards = [("1", "Il tuo computer non funziona e domani hai una riunione."), ("2", "Devi andare all'aeroporto alle 5 di mattina."),
             ("3", "Hai una festa sabato e non hai sedie per tutti."), ("4", "Vai in vacanza: chi dà da mangiare al tuo gatto?"),
             ("5", "Il frigorifero è vuoto e sei a letto con la febbre."), ("6", "Vuoi fare una sorpresa a un amico: ti serve aiuto.")]
    cl = "".join(f'<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>{n}.</b> {t}</div>' for n, t in cards)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Ti dispiacerebbe…? Scegli una carta e chiedi un favore all'insegnante in modo gentile. L'insegnante accetta o dice di no con una scusa. Poi cambiate.", "5 min")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;margin-top:1mm">{cl}</div>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Potresti…? · Ti dispiacerebbe…? · Mi faresti un favore? · Mi servirebbe… · Certo! · Volentieri! · Nessun problema. · Mi dispiace, ma… avrei / dovrei… · Potrei… invece?</div>
{sub("B", "Che cosa faresti? Rispondi e fai le stesse domande all'insegnante.", "5 min")}
<ol style="line-height:1.6"><li>Dove ti piacerebbe passare il prossimo Natale? Con chi?</li><li>Con 10.000 euro, che cosa faresti?</li><li>In quale città italiana vorresti vivere? Perché?</li><li>Quale persona famosa vorresti conoscere? Che cosa le chiederesti?</li></ol>
{sub("C", "Un consiglio. L'insegnante racconta un problema: tu dai due consigli (dovresti… · al tuo posto, io…).", "2 min")}""",
    22, """<ol><li>A: per il «no» gentile usare il condizionale: <i>Mi dispiace, ma sabato avrei un impegno.</i></li>
<li>B: annotare le forme sbagliate (<i>comprarei, poterei</i>) e correggerle alla fine.</li></ol>""")

    # Page 8
    pc = [("A2 · 03", "So raccontare una storia con lo sfondo e i fatti."), ("A2 · 04", "So dare consigli con l'imperativo (tu, voi)."),
          ("A2 · 05", "So chiedere un favore in modo gentile: potresti…? ti dispiacerebbe…?"), ("A2 · 05", "So parlare dei miei desideri: vorrei, mi piacerebbe."),
          ("A2 · 05", "So dare un consiglio: dovresti…, al tuo posto io…")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Io mangiarei una pizza.", "Io mangerei una pizza."), ("Potresti chiudere la finestra?", "✓"),
          ("Mi piacerebbero visitare Roma.", "Mi piacerebbe visitare Roma."), ("Loro verrebero volentieri alla festa.", "Loro verrebbero…"),
          ("Al tuo posto, io studierei di più.", "✓"), ("Voleresti un caffè?", "Vorresti un caffè?")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:44mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Il mio Natale ideale (50–75 parole).</b> Dove ti piacerebbe passarlo? Con chi? Che cosa mangeresti e che cosa faresti? Usa almeno cinque verbi al condizionale.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il testo; l'insegnante fa domande (<i>E chi inviteresti?</i>). Unità 06: <i>Un colloquio di lavoro</i>.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("05.1", "Potresti farmi un favore? (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("05.2", "Le doppie del condizionale")}
<p>{" · ".join(S052)}</p>
{sub("05.3", "Presente o condizionale?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S053))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 05 - Vorrei, potrei")
