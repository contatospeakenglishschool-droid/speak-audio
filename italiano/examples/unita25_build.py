# Speak! Essenziale A1 - Unità 25 "Feste e auguri" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from invito import invito
setup(band="A1 · UNITÀ 25", audio_json=os.path.join(HERE, "audio_it-a1-unita-25.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il Natale", "Natale"), ("B", "la Pasqua", "Pasqua"), ("C", "il compleanno", "compleanno"), ("D", "il Capodanno", "Capodanno"),
          ("E", "il Carnevale", "Carnevale"), ("F", "Ferragosto", "Ferragosto"), ("G", "il regalo", "regalo"), ("H", "la bandiera", "bandiera")]

SCRIPT = [("Narratore", "Dialogo uno. Al telefono."), ("Giulia", "Pronto, Júlia? Sono Giulia. Sabato prossimo è il mio compleanno!"),
          ("Júlia", "Davvero? Tanti auguri in anticipo! Quanti anni compi?"), ("Giulia", "Trenta! Sabato sera faccio una festa a casa mia. Vieni?"),
          ("Júlia", "Certo! A che ora?"), ("Giulia", "Alle otto. C'è la torta e poi balliamo!"), ("Júlia", "Che cosa porto?"),
          ("Giulia", "Niente! Porta solo Marco."), ("Júlia", "Va bene, domani chiamo Marco. A sabato!"),
          ("Narratore", "Dialogo due. Allo studio."), ("Marco", "Júlia, il quindici agosto è Ferragosto. Lo studio chiude due settimane."),
          ("Júlia", "Due settimane? In Brasile non è così!"),
          ("Marco", "In Italia ad agosto tutti vanno in vacanza. Quest'anno io vado in montagna, nelle Dolomiti, con Luca."),
          ("Júlia", "Che bello! Io ad agosto torno in Brasile a trovare la mia famiglia."), ("Marco", "E a Natale? Resti a Bologna?"),
          ("Júlia", "Non so ancora."), ("Marco", "Sai che cosa diciamo in Italia? Natale con i tuoi, Pasqua con chi vuoi!"),
          ("Júlia", "Infatti a Pasqua sono andata a Napoli con Giulia!"),
          ("Narratore", "Dialogo tre. Sulle scale."), ("Davide", "Júlia, che cosa sono tutte queste bandierine?"),
          ("Júlia", "Sono per la festa junina! In Brasile, a giugno, festeggiamo San Giovanni con musica, balli e dolci tipici."),
          ("Signora Rossi", "San Giovanni? Anche in Italia festeggiamo San Giovanni, il 24 giugno, soprattutto a Firenze e a Torino."),
          ("Júlia", "Domenica prossima faccio una piccola festa sul terrazzo. Venite?"), ("Davide", "Volentieri! Porto la chitarra."),
          ("Signora Rossi", "E io porto la torta di riso, il dolce tipico di Bologna."), ("Júlia", "Grazie! Allora a domenica!"),
          ("Davide", "A domenica! E viva San Giovanni!")]
S252 = ["giugno, ogni", "Bologna, bagno", "signora, sogno", "lasagne, compagno", "Ognissanti, spagnolo", "Ogni anno, a giugno, la signora va in montagna."]
S253 = ["Tanti auguri!", "Buon compleanno!", "Buone feste e buon anno!", "Grazie, altrettanto!", "Sabato prossimo faccio una festa.", "Ad agosto torno in Brasile."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 25", "Feste e auguri", "Le feste italiane · <b>tanti auguri, buon Natale, sabato prossimo faccio una festa</b>",
                       [("SAI FARE", "fare gli auguri, invitare a una festa e parlare dei tuoi progetti"),
                        ("LINGUA", "buon / buona / buone · le date delle feste · presente + domani, sabato prossimo, ad agosto"),
                        ("PRONUNCIA", "GN: giugno, ogni, Bologna · fare gli auguri")])
    words = [w for _, w, _ in PHOTOS]
    au = [("25 dicembre", "Buon Natale!"), ("1° gennaio", "Buon anno!"), ("Un compleanno", "Tanti auguri!"),
          ("Un amico parte", "Buon viaggio!"), ("Inizia agosto", "Buone vacanze!"), ("Vai a una festa", "Buon divertimento!")]
    aul = [f'<li value="{i+1}">{s} → {A(v, "min-width:36mm")}</li>' for i, (s, v) in enumerate(au)]
    b.page(f"""{sec(1, "Riscaldamento: le feste", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Che cosa dici? Scegli gli auguri.", "4 min")}
<div class="bank">Buon anno! &nbsp;·&nbsp; Buon divertimento! &nbsp;·&nbsp; Buon Natale! &nbsp;·&nbsp; Buon viaggio! &nbsp;·&nbsp; Buone vacanze! &nbsp;·&nbsp; Tanti auguri!</div>
{twocol(aul, 3)}""",
    22, """<ol><li>A: <i>Ferragosto</i> = 15 agosto. H: la bandiera italiana, protagonista il 2 giugno, Festa della Repubblica. Chiedere: <i>Quali feste ci sono anche in Brasile?</i></li>
<li>B: <b>Tanti auguri!</b> va bene per tutte le feste e per il compleanno. A Capodanno si dice anche <i>Buon anno nuovo!</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto di feste · gli auguri giusti</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il compleanno di Giulia · Ferragosto · la festa junina</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>buon / buona / buone · le date delle feste · presente per il futuro</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>GN · fare gli auguri</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>L'invito di Giulia · l'agenda di Júlia</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Le feste in Brasile e in Italia · un invito · i tuoi progetti</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>È giugno. Giulia compie trent'anni e invita Júlia (e Marco) alla sua festa di sabato sera. Marco spiega Ferragosto: ad agosto lo studio chiude due settimane e lui va nelle Dolomiti con il fratello Luca; Júlia invece torna in Brasile a trovare la famiglia. Sulle scale Júlia prepara le bandierine per una piccola festa junina sul terrazzo: Davide porta la chitarra, la signora Rossi la torta di riso.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Feliz compleanno</i> ✗ → <b>buon compleanno / tanti auguri</b>. <i>Buono Natale</i> ✗ → <b>buon Natale</b>. <i>Buona vacanze</i> ✗ → <b>buone vacanze</b>. <i>Faccio trent'anni</i> ✗ → <b>compio trent'anni</b>. <i>Il prossimo sabato faccio una festa</i> → più naturale <b>sabato prossimo</b>. GN pronunciato G + N ✗ → come NH: <i>Bologna</i> ≈ «Bolonha».</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>«<b>Natale con i tuoi, Pasqua con chi vuoi</b>»: Natale è la festa della famiglia; a Bologna il pranzo di Natale comincia con i <b>tortellini in brodo</b>. Dolci: <i>panettone</i> e <i>pandoro</i> a Natale, la <i>colomba</i> a Pasqua. Il 6 gennaio arriva la <b>Befana</b>. A <b>Ferragosto</b> (15 agosto) le città si svuotano e molti negozi chiudono. San Giovanni (24 giugno) è il patrono di Firenze, Torino e Genova. Agli auguri si risponde: <b>Grazie, altrettanto!</b></div>
<div class="box"><h4>AUDIO</h4>Traccia 25.1 Tre dialoghi (lento e naturale) · Traccia 25.2 GN · Traccia 25.3 Fare gli auguri</div>""")

    # Page 2
    who = [("Giulia", "il suo compleanno", "sabato prossimo, alle otto di sera"), ("Marco", "Ferragosto: va in montagna", "ad agosto (il 15 agosto)"),
           ("Júlia", "la festa junina", "domenica prossima")]
    whr = "".join(f"<tr><td style='width:24mm'><b>{n}</b></td><td>{A(s, 'min-width:58mm')}</td><td>{A(q, 'min-width:58mm')}</td></tr>" for n, s, q in who)
    vf = [("Giulia compie trent'anni.", "V"), ("La festa di Giulia è sabato a mezzogiorno.", "F"), ("Ad agosto lo studio di Marco chiude due settimane.", "V"),
          ("Ad agosto Júlia va in montagna con Marco e Luca.", "F"), ("In Italia San Giovanni è il 24 giugno.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: tre feste", "10 min")}
<p>Al telefono, allo studio e sulle scale: chi organizza che cosa?</p>
{audiocard(["25.1 · SLOW", "25.1 · NATURAL"])}
{sub("A", "Ascolta e completa: che festa? Quando?", "5 min", "25.1 · SLOW")}
<table style="margin:0"><tr><th></th><th>Che festa?</th><th>Quando?</th></tr>{whr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "3 min", "25.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa portano Davide e la signora Rossi alla festa di Júlia?", "2 min")}
<div class="wline">{R("Davide porta la chitarra e la signora Rossi porta la torta di riso.")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. <i>In anticipo</i> = prima del giorno giusto (in Italia alcuni pensano che porti sfortuna!). <i>Compiere</i> gli anni = festeggiare il compleanno.</li>
<li>B: versione <b>naturale</b>. 2: <b>alle otto di sera</b>. 4: Júlia <b>torna in Brasile</b>. <i>Le bandierine</i> = piccole bandiere colorate. <i>Viva…!</i> = esclamazione di festa.</li></ol>""")

    # Page 3
    bb = [("<b>buon</b> + maschile", "Buon Natale! Buon compleanno! Buon anno! Buon viaggio! Buon divertimento!"),
          ("<b>buona</b> + femminile", "Buona Pasqua! Buona giornata! Buona serata!"),
          ("<b>buone</b> + femminile plurale", "Buone feste! Buone vacanze!"),
          ("per tutto", "<b>Tanti auguri!</b> &nbsp;→&nbsp; risposta: <b>Grazie, altrettanto!</b>")]
    tbb = "".join(f"<tr><td style='width:46mm'>{a}</td><td>{x}</td></tr>" for a, x in bb)
    dt = [("il primo gennaio", "Capodanno"), ("il 6 gennaio", "la Befana"), ("a marzo o ad aprile", "Pasqua"), ("il 2 giugno", "la Festa della Repubblica"),
          ("il 15 agosto", "Ferragosto"), ("il 25 dicembre", "Natale")]
    tdt = "".join(f"<tr><td style='width:30mm'><b>{d}</b></td><td>{f}</td></tr>" for d, f in dt)
    pr = ["<b>domani</b>", "<b>dopodomani</b>", "<b>sabato prossimo</b>", "<b>la settimana prossima</b>", "<b>il mese prossimo</b>", "<b>ad agosto</b> · <b>a Natale</b>"]
    rules = [("", "Buona", "Buon", " Pasqua!"), ("", "Buone", "Buona", " vacanze!"), ("Giulia ", "compie", "fa", " trent'anni sabato."),
             ("", "Sabato prossimo", "Il sabato prossimo", " faccio una festa."), ("", "Buon", "Buono", " compleanno, Giulia!")]
    rl = "".join(f"<li>{a}<i>{ch([r, w] if i % 2 == 0 else [w, r], r)}</i>{z}</li>" for i, (a, r, w, z) in enumerate(rules))
    b.page(f"""{sec(3, "Grammatica: auguri e progetti", "10 min")}
{sub("A", "Gli auguri: buon, buona, buone.", "3 min")}
<table style="margin:0">{tbb}</table>
<div class="two"><div>{sub("B", "Le date delle feste.", "3 min")}
<table style="margin:0">{tdt}</table>
<p class="small" style="margin-top:1mm">Il primo giorno del mese: <b>il primo</b> (il 1°). Gli altri: <b>il</b> + numero.</p></div>
<div>{sub("C", "I progetti: presente + quando.", "2 min")}
<p style="line-height:1.7">{" · ".join(pr)}</p>
<p class="small">Per i progetti spesso usiamo il <b>presente</b>:<br><i>Sabato prossimo <b>faccio</b> una festa.<br>Ad agosto <b>torno</b> in Brasile.</i></p></div></div>
{sub("D", "Scegli l'opzione corretta.", "2 min")}
<ol>{rl}</ol>""",
    28, """<ol><li>A: <i>buon</i> funziona come <i>un</i>: <i>un compleanno → buon compleanno</i>. Al plurale maschile: <i>buoni</i> (<i>buoni regali</i>), ma negli auguri si usa poco.</li>
<li>B–C: il futuro si studia più avanti; per ora il presente + un'espressione di tempo basta. <i>Compiere</i> (non <i>fare</i>) gli anni: <i>compio, compi, compie</i>.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Feliz compleanno!</td><td><b>Buon compleanno! / Tanti auguri!</b></td><td><i>Feliz</i> non è italiano.</td></tr>
<tr><td>Buono Natale!</td><td><b>Buon Natale!</b></td><td>Come <i>un</i>: <i>buon</i>.</td></tr>
<tr><td>Buona vacanze!</td><td><b>Buone vacanze!</b></td><td><i>vacanze</i> è plurale.</td></tr>
<tr><td>Faccio trent'anni.</td><td><b>Compio trent'anni.</b></td><td><i>fazer anos</i> → <i>compiere</i>.</td></tr>
<tr><td>Il sabato prossimo faccio una festa.</td><td><b>Sabato prossimo faccio una festa.</b></td><td><i>il sabato</i> = ogni sabato.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["25.2", "25.3"])}
{sub("A", "GN. Ascolta e ripeti: è come la NH del portoghese (Bologna ≈ Bolonha).", "2 min", "25.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S252)}</div>
{sub("B", "Fare gli auguri. Ascolta e ripeti.", "3 min", "25.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S253)}</div>""",
    40, """<ol><li>Errori: <i>il sabato</i> con l'articolo vuol dire «ogni sabato» (unità 24). Per un sabato preciso: <b>sabato</b>, <b>sabato prossimo</b>.</li>
<li>4A: GN è sempre un suono solo, anche in parole simili al portoghese: <i>ignorante, magnifico</i> (non «ig-no-rante»). <i>Ognissanti</i> = il primo novembre. B: dire gli auguri con intonazione allegra.</li></ol>""")

    # Page 5
    qs = [("Chi compie gli anni? Quanti anni compie?", "Giulia. Compie trent'anni."), ("Quando è la festa? A che ora?", "Sabato 13 giugno, alle otto di sera."),
          ("Che cosa c'è alla festa?", "La torta, la musica: si balla."), ("Che cosa bisogna portare?", "Niente, solo il sorriso!")]
    ql = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in qs)
    ag = [("ven 12 giugno", "cinema con Davide", "Domani"), ("sab 13 giugno", "festa di Giulia", "Dopodomani"), ("gio 18 giugno", "calcetto con i colleghi", "La settimana prossima"),
          ("luglio", "corso di cucina", "Il mese prossimo"), ("agosto", "Brasile!", "Ad agosto")]
    agr = "".join(f"<tr><td style='width:26mm'><b>{d}</b></td><td style='width:42mm'>{x}</td></tr>" for d, x, _ in ag)
    sz = ["va al cinema con Davide.", "va alla festa di Giulia.", "gioca a calcetto con i colleghi.", "fa un corso di cucina.", "torna in Brasile."]
    sl = [f'<li value="{i+1}">{A(w, "min-width:42mm")} Júlia {z}</li>' for i, ((_, _, w), z) in enumerate(zip(ag, sz))]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "L'invito di Giulia. Leggi e rispondi.", "4 min")}
<div class="two"><div>{invito()}</div><div><ol>{ql}</ol></div></div>
{sub("B", "L'agenda di Júlia. Oggi è giovedì 11 giugno. Completa con: domani, dopodomani, la settimana prossima, il mese prossimo, ad agosto.", "4 min")}
<div class="two"><div><table style="margin:0">{agr}</table></div><div><ol style="line-height:1.7">{"".join(sl)}</ol></div></div>""",
    22, """<ol><li>A: far leggere l'invito ad alta voce. <i>Bisogna</i> = è necessario. <i>Solo il sorriso</i> = non serve portare niente.</li>
<li>B: tutte le frasi sono al <b>presente</b>, anche se parlano del futuro. Lo studente può poi dire la sua agenda della settimana.</li></ol>""")

    # Page 6
    fs = ["Natale", "Capodanno", "Carnevale", "Pasqua", "la festa junina", "il tuo compleanno"]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Le feste in Brasile e in Italia. Completa la tabella e parla con l'insegnante: quando è? Che cosa fai?", "4 min")}
<table style="margin:1mm 0 2mm"><tr><th>Festa</th><th style="width:30mm">Quando?</th><th style="width:62mm">Che cosa fai? Che cosa mangi?</th></tr>
{"".join(f"<tr><td>{x}</td><td></td><td></td></tr>" for x in fs)}</table>
{sub("B", "Un invito. Invita l'insegnante a una festa: che festa è, quando, a che ora, dove, che cosa portare. L'insegnante accetta (Volentieri!) o no (Mi dispiace, non posso…).", "4 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Rispondi all'insegnante.", "4 min")}
<ol style="line-height:1.65"><li>Qual è la tua festa preferita? Perché?</li><li>Come festeggi il tuo compleanno?</li><li>Che cosa fai sabato prossimo? E ad agosto?</li></ol>""",
    26, """<ol><li>A: confrontare: in Brasile Natale è d'estate, in Italia d'inverno (unità 17). Parole utili: <i>il cenone, i fuochi d'artificio, le maschere</i>.</li>
<li>B: poi invertire i ruoli: l'insegnante invita e lo studente risponde. C: correggere <i>faccio … anni</i> con <i>compio</i>.</li></ol>""")

    # Page 7
    pc = [("Unità 24", "So dire che sport faccio."), ("Unità 25", "So fare gli auguri."), ("Unità 25", "So dire le date delle feste."),
          ("Unità 25", "So invitare e rispondere a un invito."), ("Unità 25", "So parlare dei miei progetti.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Buono compleanno, Marco!", "Buon compleanno, Marco!"), ("Buona feste a tutti!", "Buone feste a tutti!"), ("Mia nonna fa ottant'anni domani.", "Mia nonna compie ottant'anni domani."),
          ("Il sabato prossimo vado a una festa.", "Sabato prossimo vado a una festa."), ("Buon Pasqua!", "Buona Pasqua!"),
          ("La settimana scorsa vado in vacanza.", "La settimana prossima vado in vacanza.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il tuo invito.</b> Scrivi un messaggio a un amico italiano: invitalo a una festa (che festa, quando, a che ora, dove) e racconta due progetti per l'estate.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge il suo invito. Poi Júlia racconta il suo primo anno in Italia (unità 26).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("25.1", "Tre feste (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("25.2", "GN")}
<p>{" · ".join(S252)}</p>
{sub("25.3", "Fare gli auguri")}
<p>{" ".join(S253)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 25 - Feste e auguri")
