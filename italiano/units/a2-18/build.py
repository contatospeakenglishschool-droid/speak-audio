# Speak! Ponte A2 - Unità 18 "Ti scrivo" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 18", audio_json=os.path.join(HERE, "audio_it-a2-unita-18.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la e-mail", "mail"), ("B", "la lettera", "lettera"), ("C", "la rastrelliera", "rastrelliera"), ("D", "il divano letto", "divano"),
          ("E", "il concerto", "concerto"), ("F", "la collina", "collina"), ("G", "il caldo", "caldo"), ("H", "scrivere al computer", "scrivere")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-18"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["18.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S182 = [x.split(": ", 1)[1] for x in _r["18.2 Ripeti"].split("\n")]
S183 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["18.3 Formale o informale"].split("\n")]

MAIL = """<b>Da:</b> Júlia · <b>A:</b> Sara · <b>Oggetto:</b> Festa della Musica!<br><br>Ciao Sara!<br>
Come stai? Qui a Bologna fa già caldo: <b>infatti</b> ieri c'erano 32 gradi! Ti scrivo per invitare te e Luca: sabato 20 e domenica 21 giugno c'è la Festa della Musica e in Bolognina, vicino al giardino del nostro progetto, suonano tanti gruppi. Domenica sera Giulia fa una cena al bar, <b>quindi</b> non dobbiamo cucinare! So che Luca lavora molto, <b>però</b> un weekend libero lo trova, no? Potete dormire da me: ho solo un divano letto, <b>comunque</b> è comodo. Marco, <b>invece</b>, vuole portarvi in collina in bici… Fammi sapere!<br>Un abbraccio,<br>Júlia"""


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 18", "Ti scrivo", "E-mail formali e informali · <b>infatti · invece · quindi · però · comunque</b>",
                       [("SAI FARE", "leggere e scrivere una mail informale a un amico e una mail formale semplice, collegare le idee in un testo"),
                        ("LINGUA", "Gentile ragionier Ferri, Le scrivo per… · Ciao Sara! Ti scrivo per… · però, invece, infatti, quindi, comunque"),
                        ("PRONUNCIA", "l'intonazione dei connettivi: Infatti! · Però… · Comunque,")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: scrivere", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quante e-mail scrivi alla settimana? A chi? Sono formali o informali?</li><li>Scrivi ancora lettere o cartoline? Quando?</li><li>Come cominci e come finisci una mail di lavoro nella tua lingua?</li></ol>""",
    24, """<ol><li>A: <i>la rastrelliera</i> = il posto per le bici (unità 16); <i>il divano letto</i> = un divano che diventa letto. Si dice <i>la mail</i> o <i>la e-mail</i>.</li>
<li>B: domanda 3: raccogliere <i>Prezado…, Att.</i>: li confrontiamo con l'italiano a pagina 4.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: scrivere, l'estate</td><td>1</td></tr>
<tr><td>2 Lettura e ascolto</td><td>10 min</td><td>La mail di Júlia a Sara · la mail all'amministratore · la telefonata di Luca</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>I connettivi: infatti, invece, quindi, però, comunque</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>I connettivi · la mail formale e informale</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Intonazione dei connettivi · formale o informale?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Scegli il connettivo · dal tu al Lei · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare e scrivere</td><td>12 min</td><td>Un invito al telefono · una mail formale</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Giugno, fa già caldo. Júlia scrive a Sara e invita lei e Luca alla Festa della Musica (sabato 20 e domenica 21 giugno): concerti in Bolognina vicino al giardino del progetto, cena al bar di Giulia, il divano letto di Júlia, Marco che vuole portarli in collina in bici. Allo studio Júlia scrive anche una mail formale all'amministratore (il ragionier Ferri) per chiedere una rastrelliera in cortile (unità 17): Marco la corregge (<i>Gentile…, Lei, Cordiali saluti</i>, niente <i>abbraccio</i>!). La sera Luca telefona: sabato lavora, però vengono domenica 21 e dormono da Júlia.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Nelle mail di lavoro i brasiliani scrivono <i>Prezado</i> (→ <b>Gentile</b>), chiudono con <i>Att.</i> o <i>abraço</i> (→ <b>Cordiali saluti</b>) e passano dal <i>Lei</i> al <i>tu</i>. Falsi amici: <b>comunque</b> non è <i>como</i> (= <i>de qualquer forma</i>); <b>invece di</b> + infinito (non <i>invece</i> + infinito). Il testo è spesso una catena di <i>e… e… ma…</i>: i connettivi lo rendono più chiaro.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>La <b>Festa della Musica</b> si fa il 21 giugno in molte città italiane: concerti gratis nelle piazze e nei parchi. Nelle mail formali gli italiani usano spesso il <b>titolo</b>: <i>dottore / dottoressa</i> (per i laureati), <i>ragioniere</i>, <i>ingegnere</i>, <i>avvocato</i>, <i>professore</i>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 18.1 I due dialoghi (lento e naturale) · Traccia 18.2 Ascolta e ripeti · Traccia 18.3 Formale o informale?</div>""")

    # Page 2
    vf = [("A Bologna fa freddo.", "F"), ("La Festa della Musica è il 20 e il 21 giugno.", "V"), ("Domenica sera cucina Júlia.", "F"), ("Marco vuole fare un giro in bici in collina.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    p1 = [("Il saluto:", "Gentile ragionier Ferri,"), ("Il problema: nel cortile non c'è", "una rastrelliera"),
          ("La conseguenza: i bambini", "non possono giocare"), ("La firma:", "Cordiali saluti + nome e cognome")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:56mm')}</td></tr>" for a, x in p1)
    p2 = [("Quando arrivano Luca e Sara?", "Domenica (21) mattina."), ("Perché non sabato?", "Luca lavora."), ("Dove dormono?", "Da Júlia, sul divano letto.")]
    p2l = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in p2)
    b.page(f"""{sec(2, "Lettura e ascolto: due mail", "10 min")}
{sub("A", "Leggi la mail di Júlia a Sara. Vero (V) o falso (F)?", "4 min")}
<div class="msg" style="max-width:none;padding:2mm 3.5mm;font-size:9pt;line-height:1.48">{MAIL}</div>
<table style="margin:1mm 0 0">{vfr}</table>
{audiocard(["18.1 · SLOW", "18.1 · NATURAL"])}
{sub("B", "Prima parte. Júlia scrive all'amministratore e Marco la aiuta. Completa.", "3 min", "18.1 · SLOW")}
<table style="margin:0;width:92%">{p1l}</table>
{sub("C", "Seconda parte. Luca telefona. Rispondi.", "3 min", "18.1 · NATURAL")}
<ol style="line-height:1.55">{p2l}</ol>""",
    27, """<ol><li>A: far sottolineare i cinque connettivi in grassetto: che cosa fa ognuno? (spiega, conseguenza, contrasto…). Si lavora a pagina 3.</li>
<li>B: la mail all'amministratore è formale: chiedere quali parole Júlia deve cambiare (<i>Ciao → Gentile, abbraccio → Cordiali saluti</i>).</li></ol>""")

    # Page 3
    rules = [("<i>Fa caldo: <b>infatti</b> ieri c'erano 32 gradi.</i> <i>Infatti</i>", ["conferma e spiega", "dice il contrario"], "conferma e spiega"),
             ("<i>Le bici sono per terra, <b>quindi</b> i bambini non giocano.</i> <i>Quindi</i> dà", ["la conseguenza", "la causa"], "la conseguenza"),
             ("<i>Vuole venire, <b>però</b> sabato lavoro.</i> <i>Però</i> =", ["ma", "allora"], "ma"),
             ("<i>In Brasile, <b>invece</b>, si scrive un abbraccio.</i> <i>Invece</i> fa", ["un confronto", "una conclusione"], "un confronto"),
             ("<i>Sabato lavoro. <b>Comunque</b> possiamo venire domenica.</i> <i>Comunque</i> =", ["in ogni caso", "come"], "in ogni caso"),
             ("<i><b>Invece di</b> tornare la sera…</i> Dopo <i>invece di</i> c'è", ["l'infinito", "il presente"], "l'infinito")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Il treno è in ritardo,", ["quindi", "infatti"], "quindi", "arrivo alle dieci."), ("Giulia è stanca:", ["infatti", "invece"], "infatti", "lavora dalle sei."),
          ("Io bevo il caffè; Marco,", ["invece", "quindi"], "invece", "beve il tè."), ("Non so se vengo.", ["Comunque", "Infatti"], "Comunque", "ti chiamo stasera.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: i connettivi", "10 min")}
{sub("A", "Studia le frasi della mail e dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Fa già caldo: <b>infatti</b> ieri c'erano 32 gradi. · Nel cortile non c'è una rastrelliera. <b>Infatti</b> le bici sono tutte per terra…<br>
2. …<b>quindi</b> i bambini non possono giocare. · Giulia fa una cena, <b>quindi</b> non dobbiamo cucinare.<br>
3. Sara vuole venire, <b>però</b> sabato io lavoro. · È un divano, <b>però</b> è un divano letto.<br>
4. Marco, <b>invece</b>, vuole portarvi in collina. · In Brasile, <b>invece</b>, si scrive un abbraccio. · <b>Invece di</b> tornare la sera…<br>
5. Ho solo un divano letto, <b>comunque</b> è comodo. · <b>Comunque</b> possiamo venire domenica.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli il connettivo corretto.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>infatti</b> = conferma, spiega · <b>quindi</b> = conseguenza · <b>però</b> = ma · <b>invece</b> = confronto, il contrario (<b>invece di</b> + infinito) · <b>comunque</b> = in ogni caso. Tutto (e la mail formale e informale): pagina 4.</div>""",
    22, """<ol><li>B: <i>comunque</i> è un falso amico: non vuol dire <i>como</i>. Far tradurre la frase 5 in portoghese: <i>De qualquer forma, podemos vir domingo.</i></li>
<li>C: frase 3: <i>invece</i> può stare dopo il soggetto, tra virgole.</li></ol>""")

    grammar_ref_it.connettivi_email(b)

    # Page 5
    ans3 = ["formale", "informale", "formale", "informale", "formale", "informale"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Prezado signor Ferri,</td><td><b>Gentile signor Ferri,</b></td><td><i>Prezado</i> non esiste.</td></tr>
<tr><td>Gentile signor Ferri, come stai?</td><td><b>Gentile signor Ferri, come sta?</b></td><td>Formale: <i>Lei</i>.</td></tr>
<tr><td>Un abbraccio, Júlia (all'amministratore)</td><td><b>Cordiali saluti, Júlia …</b></td><td>Formale: niente abbracci.</td></tr>
<tr><td>Invece tornare, dormite da me.</td><td><b>Invece di tornare, dormite da me.</b></td><td><i>invece di</i> + infinito.</td></tr>
<tr><td>Comunque si dice "mail"?</td><td><b>Come si dice "mail"?</b></td><td><i>comunque</i> ≠ <i>come</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["18.2", "18.3"])}
{sub("A", "Ascolta e ripeti. Dopo il connettivo c'è una piccola pausa (la virgola): Comunque, … · Però, …", "2 min", "18.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S182)}</div>
{sub("B", "Formale o informale? Ascolta e scegli.", "2 min", "18.3")}
{twocol([f'<li value="{i+1}">{ch(["formale", "informale"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>Gentile</i> va bene per uomo e donna (<i>Gentile signora, Gentile signore</i>); <i>Egregio</i> è più formale, solo per lettere ufficiali.</li>
<li>4A: <i>Infatti!</i> da solo, con intonazione che scende = <i>Pois é! / Exatamente!</i> Farlo usare come reazione: <i>Fa caldo oggi! — Infatti!</i></li></ol>""")

    # Page 6
    cn = [("Ho studiato molto, ___ ho passato l'esame.", "quindi"), ("Volevo uscire, ___ pioveva.", "però"), ("Luca è stanco: ___ ha lavorato dodici ore.", "infatti"),
          ("Io amo il mare; Sara, ___, preferisce la montagna.", "invece"), ("Non so se il ristorante è aperto. ___ proviamo!", "Comunque")]
    cnl = "".join(f"<li>{s.replace('___', A(a, 'min-width:16mm'))}</li>" for s, a in cn)
    tl = [("Ciao Marta!", "Gentile signora Bianchi,"), ("Ti scrivo per chiederti un'informazione.", "Le scrivo per chiederLe un'informazione."),
          ("Puoi mandarmi il programma?", "Potrebbe mandarmi il programma?"), ("Un abbraccio, Júlia", "Cordiali saluti, Júlia …")]
    tll = "".join(f"<li>{a}<div class='wline'>{R(f)}</div></li>" for a, f in tl)
    wb = [("rispondere", "la risposta"), ("firmare", "la firma"), ("allegare", "l'allegato"), ("salutare", "il saluto")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Completa con infatti, invece, quindi, però o comunque.", "3 min")}
<ol style="line-height:1.7">{cnl}</ol>
{sub("B", "Dal tu al Lei. Riscrivi la mail in modo formale (alla signora Bianchi).", "4 min")}
<ol style="line-height:1.4">{tll}</ol>
{sub("C", "Le parole della mail. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>B: frase 2: <i>chiederLe</i> con la L maiuscola si vede nelle mail molto formali; accettare <i>chiederle</i>.</li>
<li>C: <i>l'allegato</i> = il file nella mail: <i>Le invio in allegato…</i></li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare e scrivere", "12 min")}
{sub("A", "Un invito al telefono. L'insegnante ti invita a una festa (o a un concerto, a una cena). Non puoi in quel momento: spiega con però e proponi un'altra soluzione con comunque o invece. Poi cambiate.", "5 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Grazie per l'invito! · Mi piacerebbe, però… · Sabato non posso, infatti… · Comunque possiamo… · Invece di… perché non…? · Quindi ci vediamo…? · D'accordo, a domenica!</div>
{sub("B", "Una mail formale. Scrivi all'amministratore del tuo palazzo (o alla segreteria della tua scuola): presentati, spiega il problema con infatti e quindi, fai una richiesta, chiudi in modo formale.", "7 min")}
<div class="box" style="margin-top:1mm;font-size:8.8pt"><h4>MODELLO</h4>Gentile … , · Le scrivo perché … · Infatti … , quindi … · Potrebbe … ? · La ringrazio e resto in attesa di una Sua risposta. · Cordiali saluti, (nome e cognome)</div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: pretendere almeno tre connettivi diversi. Riprende il dialogo con Luca.</li>
<li>B: l'insegnante legge la mail e "risponde" a voce come l'amministratore, in <i>Lei</i>.</li></ol>""")

    # Page 8
    pc = [("A2 · 17", "So usare il si impersonale e dire le regole."), ("A2 · 18", "So capire una mail informale."),
          ("A2 · 18", "So scrivere una mail formale semplice (Gentile…, Cordiali saluti)."), ("A2 · 18", "So usare infatti, invece, quindi, però, comunque."),
          ("A2 · 18", "So accettare o rifiutare un invito con gentilezza.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Prezado signor Rossi,", "Gentile signor Rossi,"), ("Piove, quindi resto a casa.", "✓"),
          ("Invece andare in macchina, vado in bici.", "Invece di andare"), ("Gentile dottoressa, come stai?", "come sta?"),
          ("Comunque si scrive questa parola?", "Come si scrive"), ("Sono stanca, però vengo alla festa.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Ti scrivo (50–75 parole).</b> Scrivi una mail informale a un amico italiano: invitalo a un evento nella tua città, spiega che cosa si fa e dove può dormire. Usa almeno tre connettivi.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge la mail; l'insegnante risponde a voce come l'amico. Unità 19: <i>Ripasso 2</i> (unità 11–18).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("18.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("18.2", "Ascolta e ripeti")}
<p>{" · ".join(S182)}</p>
{sub("18.3", "Formale o informale?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S183))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 18 - Ti scrivo")
