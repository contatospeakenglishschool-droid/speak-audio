# Speak! Progresso B1 - Unità 13 "Magari!" (tutto in italiano) - formato B1 RIDOTTO (2026-11-19), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 13", audio_json=os.path.join(HERE, "audio_it-b1-unita-13.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-13"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["13.1 Magari!"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S132 = [x.split(": ", 1)[1] for x in _r["13.2 Ripeti"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    def talk(qs, title="PARLIAMONE"):
        return f'<div class="box sand" style="margin-top:1.5mm"><h4>{title}</h4><ol style="margin:0;line-height:1.5;font-size:8.9pt">' + "".join(f"<li>{q}</li>" for q in qs) + "</ol></div>"

    # ---------- IN CLASSE ----------
    # Pagina 1 - Riscaldamento
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 13", "Magari!", "Desideri · <b>vorrei che + congiuntivo imperfetto · magari</b>",
                       [("SAI FARE", "esprimere desideri per te e per gli altri, offrire aiuto, accettare e rifiutare con gentilezza"),
                        ("LINGUA", "Vorrei che fosse sempre così. · Magari venisse anche lei! · Vorrei avere più ferie."),
                        ("PRONUNCIA", "«Magari!»: desiderio o forse?")])
    kw = [("i giorni di vacanza dal lavoro", "le ferie"), ("una cosa che vorremmo avere o fare", "un desiderio"),
          ("accompagnare qualcuno a vedere una città", "portare in giro"), ("contento di quello che fa una persona cara", "orgoglioso"),
          ("una persona molto buona e gentile", "un angelo"), ("un pane basso con l'olio, tipico della Liguria", "la focaccia")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: primavera e desideri", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Che cosa ti piace fare quando arriva la primavera?", "Hai un desiderio per quest'anno?", "C'è una persona lontana che vorresti vedere presto?"], "PER COMINCIARE")}</div></div>
{sub("A", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "3 min")}
<div class="bank">un angelo · un desiderio · le ferie · la focaccia · orgoglioso · portare in giro</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Quanti giorni di ferie hai all'anno? Come li usi?", "Di chi sei orgoglioso/a? Perché?"], "USA LE PAROLE")}""",
    26, """<ol><li>Per cominciare: 4 minuti di conversazione libera, non è un test. Se lo studente dice già <i>vorrei che…</i>, annotare la forma che usa.</li>
<li>A: controllo veloce (3 minuti), poi le due domande con le parole nuove. <i>Le ferie</i> è sempre plurale (= <i>as férias</i> del lavoro).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55–60 min", """
<table><tr><th>Fase</th><th>Dove</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>classe</td><td>7 min</td><td>Conversazione · 6 parole chiave · domande con le parole</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>classe</td><td>12 min</td><td>Il picnic del primo giorno di primavera · Parliamone</td><td>2</td></tr>
<tr><td>3 Riferimento grammaticale</td><td>classe</td><td>8 min</td><td>vorrei che + congiuntivo imperfetto · magari (spiegare con gli esempi del dialogo)</td><td>3</td></tr>
<tr><td>4 Pratica</td><td>classe</td><td>10 min</td><td>Completa, scegli · Usalo (a voce)</td><td>4</td></tr>
<tr><td>5 Parlare</td><td>classe</td><td>18 min</td><td>Desideri, offerte e risposte (13.2) · la lista dei desideri</td><td>5</td></tr>
<tr><td>Conclusione</td><td>classe</td><td>3 min</td><td>Due correzioni dagli appunti · domanda «So fare»</td><td>–</td></tr>
<tr><td>Compiti</td><td>casa</td><td>–</td><td>Testo da completare · riscrivere · scrittura (100–150 parole)</td><td>6</td></tr></table>
<div class="box"><h4>IL NUOVO FORMATO B1</h4>Da questa unità le lezioni B1 hanno <b>5 pagine per la classe</b> (riscaldamento, ascolto, riferimento grammaticale, pratica, parlare) e <b>1 pagina per casa</b> (compiti). Ogni pagina della classe finisce con un riquadro di domande: lo studente parla per la maggior parte del tempo. La pratica in più, la scelta delle parole e la scrittura sono a casa. All'inizio della lezione successiva si controllano i compiti in 3–5 minuti.</div>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Domenica 21 marzo, primo giorno di primavera: picnic ai Giardini Margherita con Júlia, Bruno, Chiara, Camila e Davide. Davide vorrebbe che fosse sempre così; Camila pensa ai 32 gradi di Recife. Tra tre settimane arrivano i genitori di Júlia e Bruno (sabato 10 aprile): Júlia vorrebbe una casa più grande e due settimane di ferie (ne ha una); la mamma vorrebbe che Júlia non lavorasse… e che tornasse in Brasile. Davide si offre di portarli in giro mentre Júlia lavora («Magari! Saresti un angelo»); Bruno farà le visite storiche. Camila vorrebbe che venisse sua madre, «magari l'anno prossimo». Davide chiede la focaccia; Chiara: «Vorrei che tu non la finissi tutta».</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>La struttura è uguale al portoghese (<i>queria que você viesse</i>), ma lo studente usa spesso il presente: <i>vorrei che vieni</i>. Con lo stesso soggetto dice <i>vorrei che io avessi</i> invece di <i>vorrei avere</i>. <i>Magari</i> non esiste in portoghese: = <i>tomara!, quem dera!</i> (con il congiuntivo) oppure <i>talvez</i> (con l'indicativo).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>I Giardini Margherita sono il parco più grande del centro di Bologna, aperto nel 1879 e dedicato alla regina Margherita. In primavera si riempiono di studenti e famiglie. In Italia la legge garantisce almeno quattro settimane di ferie all'anno; molti italiani le concentrano ad agosto. La focaccia è ligure, ma oggi si mangia in tutta Italia.</div>
<div class="box"><h4>AUDIO</h4>Traccia 13.1 Magari! (naturale e lenta) · Traccia 13.2 Ripeti: desideri con vorrei che e magari</div>""")

    # Pagina 2 - Ascolto
    gist = ["la visita dei genitori di Júlia e altri desideri", "un viaggio a Recife", "il nuovo lavoro di Davide"]
    who = [("Vorrebbe che fosse sempre primavera.", "Davide"), ("Vorrebbe una casa più grande e più ferie.", "Júlia"),
           ("Vorrebbe che Júlia tornasse in Brasile.", "la mamma"), ("Si offre di portare in giro i genitori.", "Davide"),
           ("Farà le visite storiche.", "Bruno"), ("Vorrebbe che venisse sua madre.", "Camila"), ("Non vuole che Davide finisca la focaccia.", "Chiara")]
    wl = "".join(f"<li>{s} {A(w, 'min-width:16mm')}</li>" for s, w in who)
    b.page(f"""{sec(2, "Ascolto: Magari!", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{audiocard(["13.1 · NATURAL", "13.1 · SLOW"])}
{sub("A", "Picnic ai Giardini Margherita. Ascolta. Di che cosa parlano soprattutto?", "2 min", "13.1")}
<p style="margin:.3mm 0;font-size:8.9pt">{ch(gist, gist[0])}</p></div>{img('B', 40, 27)}</div>
{sub("B", "Ascolta di nuovo. Chi è? Scrivi il nome.", "4 min")}
<ol style="line-height:1.55;font-size:8.8pt;margin:0">{wl}</ol>
{talk(["Davide offre il suo aiuto. Tu faresti lo stesso per un amico?", "Che cosa faresti vedere della tua città a due genitori stranieri?", "Ti manca qualcuno che vive lontano? Chi?"])}""",
    29, """<ol><li>A–B: 6 minuti. Prima la versione naturale; la lenta solo se serve. Frase 3: <i>la mamma</i> di Júlia e Bruno (non parla nel dialogo).</li>
<li>Parliamone: 6 minuti. Lo studente usa già <i>vorrei che</i>? Non correggere ancora: la regola arriva alla pagina 3.</li></ol>""")

    # Pagina 3 - Riferimento grammaticale (in classe)
    _sec = b.sec
    b.sec = lambda n, t, tm="": _sec(3, t, "8 min") if n == "+" else _sec(n, t, tm)
    grammar_ref_it.desideri_magari(b)
    b.sec = _sec

    # Pagina 4 - Pratica
    fs = [("Davide vorrebbe che il sole (restare) ___ tutto l'anno.", "restasse"), ("La mamma vorrebbe che Júlia non (lavorare) ___.", "lavorasse"),
          ("Magari i tuoi genitori ti (sentire) ___ parlare così!", "sentissero"), ("Vorrei che qualcuno mi (passare) ___ la focaccia.", "passasse"),
          ("Magari mia madre (venire) ___ con i tuoi!", "venisse")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:22mm'))}</i></li>" for s, a in fs)
    use = ["Che cosa vorresti che cambiasse nella tua città? <i>Vorrei che…</i>", "Che cosa vorrebbe la tua famiglia da te? <i>I miei vorrebbero che…</i>",
           "Un desiderio impossibile. <i>Magari…!</i>", "Che cosa vorresti avere o fare di più? <i>Vorrei + infinito</i>",
           "Un amico ti offre un biglietto per l'Italia. <i>Magari! …</i> e continua."]
    b.page(f"""{sec(4, "Pratica: vorrei che e magari", "10 min")}
{sub("A", "Completa con il congiuntivo imperfetto.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Scegli.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>Vorrei {ch(["avere", "che io avessi"], "avere")} più ferie.</li>
<li>Spero che i tuoi genitori {ch(["vengano", "venissero"], "vengano")} ad aprile.</li>
<li>Non so, magari {ch(["viene", "venga"], "viene")} l'anno prossimo. (= forse)</li></ol>
<div class="box sand"><h4>REGOLA</h4><b>vorrei che</b> + congiuntivo <b>imperfetto</b> (soggetti diversi) · <b>vorrei</b> + infinito (stesso soggetto) · <b>spero che</b> + congiuntivo presente · <b>Magari!</b> = lo vorrei tanto · <b>magari</b> + congiuntivo imperfetto = se solo… · <b>magari</b> + indicativo = forse. Vedi il <b>Riferimento grammaticale</b> alla pagina 3.</div>
{talk(use, "USALO: RISPONDI A VOCE")}""",
    29, """<ol><li>A–B: 4 minuti. Lo studente ha appena visto il riferimento grammaticale (pagina 3): controllare la forma dopo ogni frase.</li>
<li>Usalo: 6 minuti, tutto a voce. Accettare ogni idea logica; correggere solo la struttura. Chiedere sempre una seconda frase (<i>perché?</i>).</li></ol>""")

    # Pagina 5 - Parlare
    b.page(f"""{sec(5, "Parlare: la lista dei desideri", "18 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>esprimere un desiderio</th><th>offrire aiuto</th><th>accettare</th><th>rifiutare con gentilezza</th></tr>
<tr><td><i>Vorrei che… · Magari…! · Mi piacerebbe tanto… · Il mio sogno è…</i></td><td><i>Se vuoi, ti aiuto io. · Posso…? · Ci penso io! · Lascia fare a me.</i></td><td><i>Davvero? Magari! · Saresti un angelo! · Volentieri, grazie. · Non so come ringraziarti.</i></td><td><i>Grazie, ma non serve. · Sei gentilissimo/a, ma… · Non ti preoccupare. · Ce la faccio.</i></td></tr></table></div>
{audiocard(["13.2"])}
{sub("A", "Ascolta e ripeti. Poi l'insegnante dice frasi con «magari»: è un desiderio (!) o vuol dire «forse» (?)", "4 min", "13.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S132))}</p>
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("B", "La lista dei desideri. A turno, tu e l'insegnante dite un desiderio per ogni categoria. L'altro reagisce e, se può, offre il suo aiuto.", "12 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0;columns:2"><li>per te, quest'anno</li><li>per la tua famiglia</li><li>per la tua città</li><li>per il tuo lavoro o lo studio</li><li>per il mondo</li><li>un desiderio impossibile</li></ol>
<p style="margin:.5mm 0;font-size:8.6pt">{R("Insegnante: Vorrei che a Bologna ci fosse il mare. · Magari avessi tre mesi di ferie! · Vorrei che mia madre imparasse a usare i vocali. · Vorrei che i miei studenti facessero sempre i compiti… · Il mio sogno è vivere in Sicilia.") if T else ""}</p></div>{img('D', 34, 24)}</div>
{talk(["È meglio desiderare tanto o accontentarsi di quello che si ha?", "Un desiderio di quando eri bambino/a si è realizzato?"])}""",
    32, """<ol><li>A: <i>Magari!</i> esclamativo (desiderio) ha la voce alta; <i>magari viene</i> (= forse) è piatto. Frasi per il gioco: <i>Magari! · Magari domani piove · Magari vincessi! · Magari è a casa.</i></li>
<li>B: 10 minuti. Usare le battute in rosso come esempio, poi lasciare parlare lo studente. Dopo ogni desiderio, offrire aiuto per far usare <i>accettare / rifiutare</i>. Ultimi 3 minuti: conclusione (due correzioni e la domanda <i>Sai esprimere un desiderio con vorrei che?</i>).</li></ol>""")

    # ---------- A CASA ----------
    pc = [(["Magari", "Forse"], "Magari"), (["portassi", "porti"], "portassi"), (["vedere", "che vedesse"], "vedere"),
          (["sia", "fosse"], "sia"), (["spiegasse", "spiega"], "spiegasse")]
    p = [ch(o, a) for o, a in pc]
    rw = [("Il mio capo mi dà troppo lavoro. (vorrei che)", "Vorrei che il mio capo mi desse meno lavoro."),
          ("Non ho tempo per studiare. (magari)", "Magari avessi tempo per studiare!"),
          ("Mio fratello non mi chiama mai. (vorrei che)", "Vorrei che mio fratello mi chiamasse più spesso.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Compiti", "a casa")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Lunedì Júlia scrive a Davide. Scegli la forma giusta.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Júlia:</b> Ciao Davide! Grazie ancora per ieri. {p[0]} tutti i vicini fossero come te! Ti scrivo le date: i miei arrivano sabato 10 aprile. Vorrei che tu li {p[1]} al mercato delle Erbe lunedì mattina, mentre sono allo studio. La mamma vorrebbe {p[2]} tutto in un giorno, ma tu non ascoltarla! Spero che il tempo {p[3]} bello. Ah, e papà vorrebbe che qualcuno gli {p[4]} il calcio italiano: è la tua specialità!</div>
{sub("B", "Riscrivi le frasi con le parole tra parentesi.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
<div class="box sand" style="margin:1mm 0"><h4>ATTENZIONE: SCELTA DELLE PAROLE</h4>
<table style="margin:0;font-size:8.1pt"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Vorrei che tu vieni.</td><td><b>Vorrei che tu venissi.</b></td><td><i>vorrei che</i> + congiuntivo imperfetto.</td></tr>
<tr><td>Vorrei che io avessi più ferie.</td><td><b>Vorrei avere più ferie.</b></td><td>stesso soggetto → infinito.</td></tr>
<tr><td>Spero che venisse.</td><td><b>Spero che venga.</b></td><td><i>spero che</i> + congiuntivo presente.</td></tr></table></div>
{sub("C", "Scrittura (100–150 parole, sul quaderno). La mia lista dei desideri: per te, per una persona cara e per la tua città.", "")}
<p class="small" style="margin:.3mm 0"><b>Comincia così:</b> <i>Quest'anno vorrei che…</i> &nbsp;☐ tre <i>vorrei che</i> &nbsp;☐ due <i>magari</i> &nbsp;☐ un <i>vorrei</i> + infinito &nbsp;☐ un <i>spero che</i> &nbsp;☐ 100–150 parole</p>
<p class="small" style="margin:.3mm 0"><b>So fare:</b> So esprimere desideri con vorrei che e magari, e accettare o rifiutare un aiuto. ☐ Facile! ☐ A volte ☐ Non ancora</p>""",
    20, """<p>Controllare A e B in 3 minuti all'inizio della lezione successiva. Leggere la scrittura a casa e scegliere due errori da discutere in classe. Il mercato delle Erbe è il mercato coperto di via Ugo Bassi.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("13.1", "Magari! (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("13.2", "Ripeti: desideri con vorrei che e magari")}
<p>{" · ".join(S132)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 13 - Magari")
