# Speak! Ponte A2 - Unità 04 "Dal medico" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
from corpo import corpo
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 04", audio_json=os.path.join(HERE, "audio_it-a2-unita-04.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il mal di testa", "mal di testa"), ("B", "i fazzoletti", "fazzoletti"), ("C", "il mal di schiena", "mal di schiena"), ("D", "il termometro", "termometro"),
          ("E", "lo sciroppo", "sciroppo"), ("F", "le pastiglie", "pastiglie"), ("G", "il ghiaccio", "ghiaccio"), ("H", "la farmacia", "farmacia")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-04"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["04.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S042 = [x.split(": ", 1)[1] for x in _r["04.2 Ripeti imperativo e pronomi"].split("\n")]
S043 = [x.split(": ", 1)[1] for x in _r["04.3 Tu o voi"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 04", "Dal medico", "La salute e i consigli · <b>l'imperativo informale</b>",
                       [("SAI FARE", "dire che cosa ti fa male e dare consigli a un amico malato"),
                        ("LINGUA", "Mi fa male la testa. · Resta a casa! Non uscire! · Chiamalo! Riposati!"),
                        ("PRONUNCIA", "l'accento dell'imperativo con i pronomi · tu o voi?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: non sto bene", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali di queste cose hai a casa? Dove le tieni?</li><li>Quando sei stato/a male l'ultima volta? Che cosa avevi?</li><li>Quando hai il raffreddore, vai dal medico o in farmacia?</li></ol>""",
    22, """<ol><li>A: <i>mal di</i> + parte del corpo, senza articolo: <i>ho mal di testa, mal di gola, mal di schiena</i>. <i>Le pastiglie</i> = le compresse. In farmacia c'è la croce verde.</li>
<li>B: domanda 2: imperfetto per la descrizione (<i>avevo la febbre</i>), ripasso dell'unità 03.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: malattie e medicine</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Marco ha l'influenza · la schiena di Davide · Marco torna allo studio</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>L'imperativo informale: tu, voi, negativo, pronomi</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Forme · irregolari · pronomi attaccati · negativo</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'accento con i pronomi · tu o voi?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Consigli per Marco · imperativo + pronome · il corpo</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Che cosa ti fa male? (gioco di ruolo) · consigli a due amici</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine novembre: Marco ha l'influenza (mal di testa, mal di gola, febbre a 38,5). Júlia gli telefona e gli dà consigli: resta a casa, bevi acqua calda con il miele, non prendere gli antibiotici, chiama il medico. Al bar Davide racconta che ha giocato a calcetto con Bruno sotto la pioggia: è scivolato e ora ha mal di schiena, e a Bruno fanno male le ginocchia. Giulia li sgrida (<i>fate stretching, non giocate sotto la pioggia!</i>) e gli dice di non portare il divano di Bruno al quarto piano. Tre giorni dopo Marco torna allo studio: è solo influenza. Vuole abbracciare Júlia, ma lei risponde: <i>Non avvicinarti!</i></div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Nel parlato brasiliano l'imperativo è spesso uguale al presente (<i>toma o remédio, não pega isso</i>), quindi lo studente dice <i>non prendi!</i> invece di <b>non prendere!</b> Altri errori frequenti: <i>dor de cabeça</i> → <i>dolore di testa</i> (→ <b>mal di testa</b>); <i>me dá</i> → <i>mi dai</i> (→ <b>dammi</b>); <i>mi fa male le gambe</i> (→ <b>mi fanno male</b>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia ognuno ha un <b>medico di base</b> (il medico di famiglia) del Servizio Sanitario Nazionale: la visita è gratuita, ma bisogna prendere un appuntamento. Gli antibiotici si comprano in farmacia solo con la <b>ricetta</b>. La farmacia ha la <b>croce verde</b> e di notte c'è sempre una farmacia di turno. Molti italiani hanno paura del <i>colpo d'aria</i>: per questo la sciarpa è importantissima!</div>
<div class="box"><h4>AUDIO</h4>Traccia 04.1 Tre dialoghi (lento e naturale) · Traccia 04.2 Imperativo e pronomi · Traccia 04.3 Tu o voi?</div>""")

    # Page 2
    st = [("Perché Marco non è allo studio?", "è a letto, sta malissimo: ha l'influenza"), ("Che cosa gli fa male? Che cosa ha?", "la testa; ha mal di gola, la febbre a 38,5, la tosse e il naso chiuso"),
          ("Che cosa deve bere?", "tanta acqua calda con il miele"), ("Perché Júlia dice «non prenderli»?", "sono antibiotici: prima deve chiamare il medico")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    vf = [("Davide si è fatto male giocando a calcetto.", "V"), ("A Bruno fa male la schiena.", "F"), ("Giulia dice: «Fate stretching prima della partita».", "V"),
          ("Júlia consiglia a Davide di mettersi il ghiaccio.", "V"), ("Giulia dice a Davide di aiutare Bruno con il divano.", "F")]
    vfl = "".join(f"<tr><td>{s}</td><td style='width:14mm;text-align:center'>{A(v, 'min-width:7mm')}</td></tr>" for s, v in vf)
    b.page(f"""{sec(2, "Ascolto: sto malissimo!", "10 min")}
<p>Marco è a letto con l'influenza, Davide ha mal di schiena e Júlia dà tanti consigli.</p>
{audiocard(["04.1 · SLOW", "04.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "4 min", "04.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Vero (V) o falso (F)?", "4 min", "04.1 · NATURAL")}
<table style="margin:0">{vfl}</table>
{sub("C", "Dialogo 3. Che cosa ha detto il medico? E perché Júlia non abbraccia Marco?", "2 min")}
<div class="wline">{R("è solo influenza, niente antibiotici · Marco non è ancora guarito bene")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Far notare <i>che cosa <b>ti fa</b> male?</i> e <i>mi fa male <b>la</b> testa</i>: il verbo funziona come <i>piacere</i>.</li>
<li>B: versione <b>naturale</b>. 2: <i>gli fanno male le ginocchia</i> (plurale). Correggere le frasi false.</li></ol>""")

    # Page 3
    rules = [("Per il <b>tu</b> dei verbi in <b>-are</b> l'imperativo finisce in", ["-a", "-i"], "-a"),
             ("Per il <b>tu</b> dei verbi in <b>-ere</b> e <b>-ire</b> l'imperativo finisce in", ["-a", "-i"], "-i"),
             ("Il negativo di <b>tu</b> è <b>non +</b>", ["l'infinito", "la forma del presente"], "l'infinito"),
             ("L'imperativo di <b>voi</b> (<i>fate, giocate</i>) è uguale al", ["presente", "passato prossimo"], "presente"),
             ("Con l'imperativo affermativo i pronomi (<i>lo, mi, ti…</i>) vanno", ["prima del verbo", "dopo il verbo, attaccati"], "dopo il verbo, attaccati"),
             ("Con <i>da', di', fa', va', sta'</i> la consonante del pronome", ["si raddoppia", "resta uguale"], "si raddoppia")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("(restare) ", "Resta", " a letto!"), ("(bere) ", "Bevi", " tanta acqua!"), ("(non uscire) ", "Non uscire", "!"),
          ("(dormire) ", "Dormi", " molto!"), ("(non mangiare) ", "Non mangiare", " il gelato!"), ("(fare) ", "Fa' / Fai", " una passeggiata!")]
    ccl = [f'<li value="{i+1}">{a}{A(c, "min-width:22mm")}{z}</li>' for i, (a, c, z) in enumerate(cc)]
    b.page(f"""{sec(3, "Grammatica: l'imperativo informale", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Oggi <b>resta</b> a casa! <b>Bevi</b> tanta acqua e <b>riposati</b>. &nbsp; 2. <b>Non venire</b> allo studio! <b>Non uscire</b> con questo freddo!<br>
3. Ragazzi, <b>fate</b> stretching e <b>non giocate</b> sotto la pioggia!<br>
4. <b>Chiama</b> il medico e <b>chiedigli</b> un appuntamento. · Gli antibiotici? <b>Non prenderli</b>! · Il divano? <b>Non portarlo</b>!<br>
5. <b>Dammi</b> un abbraccio! · <b>Dillo</b> anche a Bruno! · <b>Mettiti</b> la sciarpa!</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Un consiglio a Marco. Scrivi l'imperativo di tu.", "3 min")}
{twocol(ccl, 3)}
<div class="box sand"><h4>REGOLA</h4><b>tu</b>: <i>resta!</i> (-are) · <i>bevi! dormi!</i> (-ere, -ire) · negativo: <b>non + infinito</b> (<i>non uscire!</i>). <b>voi</b> e <b>noi</b> = presente: <i>fate! giocate! andiamo!</i> · negativo: <i>non giocate!</i> I pronomi vanno <b>dopo</b> e si attaccano: <i>chiamalo, riposati, dammi</i>. Tutte le forme e gli irregolari: pagina 4.</div>""",
    20, """<ol><li>B: chiedere allo studente di trovare nei dialoghi due esempi per ogni regola.</li>
<li>C: 6: <i>fa'</i> e <i>fai</i> sono corretti. Attenzione: <i>dormi!</i> e <i>bevi!</i> sono uguali al presente; solo i verbi in <i>-are</i> cambiano.</li></ol>""")

    grammar_ref_it.imperativo_informale(b)

    # Page 5
    ans3 = ["voi", "tu", "voi", "tu", "voi", "tu"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Non prendi l'antibiotico!</td><td><b>Non prendere l'antibiotico!</b></td><td><i>tu</i> negativo: <i>non</i> + infinito.</td></tr>
<tr><td>Mi fa male le gambe.</td><td><b>Mi fanno male le gambe.</b></td><td>Come <i>piacere</i>: plurale → <i>fanno</i>.</td></tr>
<tr><td>Ho dolore di testa.</td><td><b>Ho mal di testa.</b></td><td><i>mal di</i> + parte del corpo.</td></tr>
<tr><td>Ti riposa!</td><td><b>Riposati!</b></td><td>Il pronome va dopo, attaccato.</td></tr>
<tr><td>Dami il termometro.</td><td><b>Dammi il termometro.</b></td><td><i>da'</i> + <i>mi</i>: doppia <i>m</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["04.2", "04.3"])}
{sub("A", "L'accento non si sposta. Ascolta e ripeti. La sillaba forte resta la stessa: RIposa → RIposati.", "2 min", "04.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S042)}</div>
{sub("B", "Tu o voi? Ascolta e scegli.", "2 min", "04.3")}
{twocol([f'<li value="{i+1}">{ch(["tu", "voi"], a)}</li>' for i, a in enumerate(ans3)], 3)}""",
    28, """<ol><li>Errori: <i>mi fa male</i> + singolare, <i>mi fanno male</i> + plurale, come <i>mi piace / mi piacciono</i>.</li>
<li>4A: lo studente batte le mani sulla sillaba forte. 4B: poi trasforma: <i>Bevete! → Bevi!</i>, <i>Riposati! → Riposatevi!</i></li></ol>""")

    # Page 6
    pr = [("Chiama il medico!", "Chiamalo!"), ("Prendi lo sciroppo!", "Prendilo!"), ("Non mangiare le caramelle!", "Non mangiarle! / Non le mangiare!"),
          ("Scrivi a me un messaggio!", "Scrivimi un messaggio!"), ("Di' la verità al medico!", "Dilla al medico!"), ("Ragazzi, bevete la spremuta!", "Bevetela!")]
    prl = "".join(f"<li>{a} → {A(c, 'min-width:40mm')}</li>" for a, c in pr)
    parts = ["la testa", "l'occhio", "l'orecchio", "il naso", "la bocca", "il collo", "il braccio", "la mano", "la pancia", "la gamba", "il ginocchio", "il piede"]
    num = {w: i + 1 for i, w in enumerate(parts)}
    shown = sorted(parts, key=lambda w: w.split()[-1].split("'")[-1])
    cell = lambda w: f"<td style='width:9mm;text-align:center'>{A(str(num[w]), 'min-width:7mm')}</td><td>{w}</td>"
    pl = "".join(f"<tr>{cell(shown[i])}{cell(shown[i + 6])}</tr>" for i in range(6))
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Imperativo e pronomi. Riscrivi la frase con il pronome.", "4 min")}
<ol style="line-height:1.75">{prl}</ol>
{sub("B", "Il corpo. Scrivi il numero giusto accanto alla parola.", "3 min")}
<div class="two" style="align-items:center"><div>{corpo("66mm")}</div><table style="margin:0;font-size:9.4pt;table-layout:fixed">{pl}</table></div>
{sub("C", "Plurali speciali. Completa.", "2 min")}
<p style="line-height:1.8;margin:0">il braccio → le {A("braccia", "min-width:16mm")} · il ginocchio → le {A("ginocchia", "min-width:16mm")} · il dito → le {A("dita", "min-width:12mm")} · la mano → le {A("mani", "min-width:12mm")} · l'orecchio → le {A("orecchie", "min-width:16mm")}</p>""",
    20, """<ol><li>A: nel 3 vanno bene le due posizioni; con l'affermativo il pronome va sempre dopo (<i>bevetela</i>).</li>
<li>B–C: l'insegnante tocca una parte del corpo, lo studente dice <i>mi fa male… / mi fanno male…</i></li></ol>""")

    # Page 7
    cards = [("1", "Hai mal di denti e domani hai un esame."), ("2", "Hai il raffreddore e stasera c'è una festa."),
             ("3", "Ti fanno male i piedi dopo una passeggiata di 20 km."), ("4", "Non dormi bene da una settimana."),
             ("5", "Hai mangiato troppo a pranzo e ti fa male la pancia."), ("6", "Passi otto ore al computer e ti fanno male gli occhi.")]
    cl = "".join(f'<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>{n}.</b> {t}</div>' for n, t in cards)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Che cosa ti fa male? Scegli una carta e racconta il problema. L'insegnante ti dà due consigli. Poi cambiate: l'insegnante sceglie una carta e tu dai i consigli.", "6 min")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;margin-top:1mm">{cl}</div>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Che cosa ti fa male? · Che cosa hai? · Da quanto tempo? · Poverino/a! · Resta… · Prendi… · Bevi… · Non bere… · Non mangiare… · Va' dal medico! · Mettiti… · Chiamalo! · Riposati!</div>
{sub("B", "Consigli a due amici (voi). Bruno e Davide vogliono correre la maratona di Bologna fra un mese. Dagli quattro consigli: due affermativi e due negativi.", "4 min")}
<div class="wline">{R("Allenatevi ogni giorno! Dormite otto ore! Non mangiate fritto! Non correte sotto la pioggia!")}</div><div class="wline"></div>
{sub("C", "E tu? Che cosa fai quando hai il raffreddore o l'influenza? Ci sono rimedi della nonna nella tua famiglia?", "2 min")}""",
    22, """<ol><li>A: lo studente deve usare almeno un pronome (<i>prendilo, chiamalo, mettiti…</i>). Annotare gli errori del negativo e correggerli alla fine.</li>
<li>C: rimedi italiani: brodo di pollo, latte caldo con il miele, la sciarpa contro il colpo d'aria.</li></ol>""")

    # Page 8
    pc = [("A2 · 02", "So raccontare com'era la mia infanzia con l'imperfetto."), ("A2 · 03", "So raccontare una storia con lo sfondo e i fatti."),
          ("A2 · 04", "So dire che cosa mi fa male e nominare le parti del corpo."), ("A2 · 04", "So dare consigli con l'imperativo (tu, voi), anche negativo."),
          ("A2 · 04", "So usare l'imperativo con i pronomi: chiamalo, riposati, dammi.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Non bevi il caffè la sera!", "Non bere il caffè…"), ("Mi fanno male le orecchie.", "✓"),
          ("Ragazzi, non uscire con la pioggia!", "…non uscite…"), ("Lo chiama subito!", "Chiamalo subito!"),
          ("Ho dolore di gola.", "Ho mal di gola."), ("Mettiti la sciarpa, fa freddo!", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:44mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio a un amico malato (50–75 parole).</b> Un amico ha l'influenza e ti scrive: <i>Sto malissimo!</i> Rispondi: chiedi che cosa gli fa male e dagli almeno cinque consigli con l'imperativo (due negativi e uno con un pronome).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il messaggio; l'insegnante risponde come l'amico malato. Unità 05: <i>Vorrei, potrei…</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("04.1", "Sto malissimo! (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("04.2", "Imperativo e pronomi")}
<p>{" · ".join(S042)}</p>
{sub("04.3", "Tu o voi?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S043))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 04 - Dal medico")
