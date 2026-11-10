# Speak! Ponte A2 - Unità 27 "Lo sai che…?" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 27", audio_json=os.path.join(HERE, "audio_it-a2-unita-27.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il sole", "sole"), ("B", "il campanello", "campanello"), ("C", "la biblioteca", "biblioteca"), ("D", "gli scatoloni", "scatoloni"),
          ("E", "il frigorifero", "frigorifero"), ("F", "il pettegolezzo", "pettegolezzo"), ("G", "il brindisi", "brindisi"), ("H", "l'esame", "esame")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-27"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["27.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S272 = [x.split(": ", 1)[1] for x in _r["27.2 Ripeti"].split("\n")]
S273 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["27.3 Diretto o indiretto"].split("\n")]


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
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 27", "Lo sai che…?", "Notizie e pettegolezzi · <b>dice che · ha detto che · per me · con te</b>",
                       [("SAI FARE", "dare e chiedere notizie, riportare quello che ha detto un'altra persona, dire la tua opinione"),
                        ("LINGUA", "Lo sai che…? · Mi ha detto che va a Milano. · È per te. · Vieni con me? · Secondo me…"),
                        ("PRONUNCIA", "i pronomi tonici sono forti: per ME, con TE")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: novità?", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quando torni dalle vacanze, chi ti racconta le novità?</li><li>Nel tuo palazzo c'è una persona che sa tutto di tutti?</li><li>Ti piacciono i pettegolezzi? Perché sì o perché no?</li></ol>""",
    28, """<ol><li>A: <i>il pettegolezzo</i> = una notizia (spesso non sicura) sulla vita degli altri; <i>gli scatoloni</i> = le scatole grandi del trasloco; <i>il brindisi</i> = alzare i bicchieri per festeggiare (<i>Cin cin!</i>).</li>
<li>B: domanda 2: in molti palazzi italiani questa persona era la <i>portinaia</i>; nella nostra storia è la signora Rossi.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: notizie, studio, festa</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Le novità del palazzo · Bruno riporta la bici</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Dice che / ha detto che · i pronomi tonici</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il discorso indiretto · me, te, lui, lei…</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>I pronomi tonici · diretto o indiretto?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Riporta le parole · il pronome tonico · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Lo sai che…? · secondo te</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Primi di settembre. Júlia e Marco sono tornati da Rimini (unità 26). Domenica Júlia riporta l'ombrellone e la borsa frigo alla signora Rossi, come aveva promesso (unità 25); la cartolina è sul frigorifero. Le novità del palazzo: il signor Neri (unità 24) a ottobre si trasferisce a Milano da sua figlia, e il padrone di casa dice che c'è <b>una ragazza interessata</b> all'appartamento (nuova vicina in arrivo). Bruno ha detto alla signora Rossi che è andato in biblioteca tutti i giorni, ma secondo lei è andato al mare con Chiara: era abbronzatissimo. La sera Bruno riporta la bici con un regalo (un campanello nuovo, da parte sua e di Chiara) e confessa: due giorni al mare. L'esame è giovedì.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese brasiliano parlato dice <i>com eu, pra eu, entre eu e você</i>: lo studente dice <i>con io, per tu</i>. Nel discorso indiretto omette <i>che</i> o non cambia la persona (<i>Bruno ha detto che io sono andato…</i>). I pronomi tonici con le preposizioni sono già apparsi nell'unità 01: qui si consolidano.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Nei palazzi italiani le notizie girano sulle scale, al bar sotto casa e nelle chat del condominio. Per molti anni il centro delle informazioni era il <b>portiere</b> o la <b>portinaia</b>, che riceveva la posta e conosceva tutti. Oggi il portiere c'è soprattutto nei palazzi grandi delle città; negli altri c'è sempre una vicina come la signora Rossi.</div>
<div class="box"><h4>AUDIO</h4>Traccia 27.1 I due dialoghi (lento e naturale) · Traccia 27.2 Ascolta e ripeti · Traccia 27.3 Diretto o indiretto?</div>""")

    # Page 2
    p1 = [("La signora Rossi ha messo la cartolina sul", "frigorifero"), ("A ottobre il signor Neri si trasferisce a", "Milano"),
          ("Va a vivere da", "sua figlia"), ("Il padrone di casa dice che c'è", "una ragazza interessata")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("Bruno riporta la bici a Júlia.", "V"), ("Il regalo è un casco.", "F"), ("Bruno è andato al mare per due giorni.", "V"),
          ("L'esame di Bruno è venerdì.", "F"), ("Júlia festeggia con Bruno solo se passa l'esame.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: le novità", "10 min")}
{audiocard(["27.1 · SLOW", "27.1 · NATURAL"])}
{sub("A", "Prima parte. Júlia riporta l'ombrellone. Completa.", "4 min", "27.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Bruno riporta la bici. Vero (V) o falso (F)?", "4 min", "27.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Come sa la signora Rossi che Bruno è andato al mare?", "2 min")}
<div class="wline">{R("Perché era abbronzatissimo.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Novità per la storia: arriva una nuova vicina (una ragazza) al posto del signor Neri.</li>
<li>B: frase 2: è un <i>campanello</i>. Far notare <i>Quella donna vede tutto!</i>: Bruno è un po' arrabbiato e un po' divertito.</li></ol>""")

    # Page 3
    rules = [("«Vado a Milano.» → Il signor Neri dice che", ["va", "vado"], "va"),
             ("«Ho studiato.» → Bruno ha detto che", ["ha studiato", "ho studiato"], "ha studiato"),
             ("«Il mio esame è giovedì.» → Dice che", ["il suo esame", "il mio esame"], "il suo esame"),
             ("Dopo <i>dice che</i> il tempo del verbo", ["non cambia", "cambia"], "non cambia"),
             ("Dopo <i>per, con, secondo</i> si usa", ["me, te", "io, tu"], "me, te"),
             ("<i>È per <b>te</b>.</i> Il pronome tonico è", ["forte, con l'accento", "debole, senza accento"], "forte, con l'accento")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Vieni con", ["me", "io"], "me", "al cinema?"), ("Questo regalo è per", ["te", "tu"], "te", "."),
          ("", ["Secondo me", "Secondo io"], "Secondo me", ", Bruno è andato al mare."), ("Giulia ha detto", ["che è stanca", "è stanca"], "che è stanca", ".")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" ,", ",").replace(" .", ".") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: dice che… · per me, con te", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Lo sai che</b> il signor Neri va via? · <b>Mi ha detto che</b> a ottobre si trasferisce a Milano.<br>
2. Il padrone di casa <b>dice che</b> c'è una ragazza interessata. · La signora Rossi <b>dice che</b> eri abbronzatissimo.<br>
3. Questo è per <b>te</b>. — Per <b>me</b>? · <b>Secondo me</b> hai studiato poco. · Vieni con <b>me</b>? — Con <b>te</b>?</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>Dice che / ha detto che</b> + le parole dell'altra persona: cambia la persona (<i>vado → va, mio → suo</i>), il tempo resta uguale. Dopo una preposizione si usano i <b>pronomi tonici</b>: <i>me, te, lui, lei, Lei, noi, voi, loro</i> (<i>per te, con me, secondo me</i>). Tutto: pagina 4.</div>""",
    22, """<ol><li>B: frasi 1–3: scrivere alla lavagna la frase diretta tra virgolette e far cambiare solo la persona.</li>
<li>B: a livello A2 il tempo non cambia (<i>ha detto che va</i>); <i>ha detto che andava</i> è corretto ma si studia al B1.</li></ol>""")

    grammar_ref_it.discorso_indiretto_tonici(b)

    # Page 5
    opts3 = [["diretto", "indiretto"]] * 6
    ans3 = ["diretto", "indiretto", "indiretto", "diretto", "indiretto", "diretto"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Vieni con io?</td><td><b>Vieni con me?</b></td><td>Dopo <i>con</i>: <i>me</i>.</td></tr>
<tr><td>È per tu.</td><td><b>È per te.</b></td><td>Dopo <i>per</i>: <i>te</i>.</td></tr>
<tr><td>Secondo io, sì.</td><td><b>Secondo me, sì.</b></td><td><i>Secondo</i> è una preposizione.</td></tr>
<tr><td>Ha detto vado a Milano.</td><td><b>Ha detto che va a Milano.</b></td><td><i>Che</i> + la persona giusta.</td></tr>
<tr><td>Bruno dice che sono andato al mare.</td><td><b>Bruno dice che è andato al mare.</b></td><td>Parla di sé: <i>lui</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["27.2", "27.3"])}
{sub("A", "Ascolta e ripeti. I pronomi tonici sono forti: per ME, con TE, secondo ME.", "2 min", "27.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S272)}</div>
{sub("B", "Diretto o indiretto? Ascolta e scegli.", "2 min", "27.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: riga 5: chi parla? Se il soggetto è Bruno, nel discorso indiretto il verbo va alla terza persona.</li>
<li>4A: contrasto: <i>ti</i> è debole (<i>ti presto</i>), <i>te</i> dopo la preposizione è forte (<i>per TE</i>).</li>
<li>4B: indizio: <i>dice che / ha detto che</i> = indiretto; verbo alla prima persona = diretto.</li></ol>""")

    # Page 6
    rp = [("«Sono stanca.» (Giulia)", "Giulia dice che è stanca."), ("«Ho fame.» (Marco)", "Marco dice che ha fame."),
          ("«Vado in biblioteca.» (Bruno)", "Bruno ha detto che va in biblioteca."), ("«Il mio computer è lento.» (Bruno)", "Bruno ha detto che il suo computer è lento."),
          ("«Torniamo domenica.» (Júlia e Marco)", "Hanno detto che tornano domenica.")]
    rpl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in rp)
    tn = [("Vieni a cena da", "(noi)?", "noi"), ("Ho un regalo per", "(tu).", "te"), ("Esci con", "(lui) stasera?", "lui"),
          ("Secondo", "(io), Rimini è bellissima.", "me"), ("Non posso vivere senza di", "(voi)!", "voi")]
    tnl = "".join(f"<li>{a} {A(r, 'min-width:16mm')} {z}</li>" for a, z, r in tn)
    wb = [("trasferirsi", "il trasferimento"), ("festeggiare", "la festa"), ("abbronzarsi", "l'abbronzatura"), ("chiacchierare", "la chiacchierata")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Riporta le parole. Usa dice che o ha detto che.", "4 min")}
<ol style="line-height:1.4">{rpl}</ol>
{sub("B", "Completa con il pronome tonico.", "3 min")}
<ol style="line-height:1.7">{tnl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 4: <i>il mio → il suo</i>; frase 5: <i>torniamo → tornano</i>.</li>
<li>B: <i>senza di</i> + pronome tonico (<i>senza di te</i>), ma <i>senza</i> + nome (<i>senza Marco</i>).</li>
<li>C: <i>Facciamo una chiacchierata?</i> = parliamo un po'.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Lo sai che…? L'insegnante racconta tre notizie (vere o inventate). Tu le riporti: «Lei ha detto che…». Poi tu racconti tre novità della tua settimana e l'insegnante le riporta. Chi sbaglia una persona paga un caffè!", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Lo sai che…? · Hai sentito che…? · Mi ha detto che… · Dice che… · Davvero? · Ma dai! · Non ci credo! · Chi te l'ha detto? · Secondo me è vero / non è vero.</div>
{sub("B", "Secondo te… Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Secondo te, Bruno ha studiato o no? Passerà l'esame?</li><li>Che cosa ti hanno detto di bello questa settimana? Chi te l'ha detto?</li><li>Con chi vai in vacanza di solito? Per te è meglio con gli amici o con la famiglia?</li><li>Hai mai detto una piccola bugia come Bruno?</li><li>Nel tuo palazzo o al lavoro chi sa sempre tutto?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: preparare notizie semplici al presente o al passato prossimo (<i>Mia sorella si sposa. Ho comprato una moto.</i>). Correggere soprattutto la persona del verbo.</li>
<li>B: domanda 1: <i>passerà</i>: futuro (unità 22). Domanda 4: <i>Ho detto che…</i>.</li></ol>""")

    # Page 8
    pc = [("A2 · 26", "So usare casetta, lettone, le braccia, le uova."), ("A2 · 27", "So dare e chiedere notizie."),
          ("A2 · 27", "So riportare le parole con dice che / ha detto che."), ("A2 · 27", "So usare per me, con te, secondo me."),
          ("A2 · 27", "So dire la mia opinione.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Vieni con io al bar?", "Vieni con me al bar?"), ("È un regalo per te.", "✓"),
          ("Secondo io, ha ragione.", "Secondo me, ha ragione."), ("Marco ha detto ha fame.", "Marco ha detto che ha fame."),
          ("Giulia dice che il mio bar è chiuso. (= di Giulia)", "Giulia dice che il suo bar è chiuso."), ("Lo sai che Bruno ha un esame?", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Le novità (50–75 parole).</b> Scrivi un messaggio a un amico con tre novità (del lavoro, della famiglia, del palazzo). Comincia con <i>Lo sai che…?</i> e usa <i>mi ha detto che</i> almeno due volte e due pronomi tonici (<i>per me, con lui…</i>).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il messaggio; l'insegnante riporta una novità (<i>Lei ha detto che…</i>). Unità 28: <i>Ripasso 3</i> (unità 20–27).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("27.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("27.2", "Ascolta e ripeti")}
<p>{" · ".join(S272)}</p>
{sub("27.3", "Diretto o indiretto?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S273))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 27 - Lo sai che…?")
