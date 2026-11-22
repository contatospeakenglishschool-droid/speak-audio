# Speak! Progresso B1 - Unità 23 "Se l'avessi saputo…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 23", audio_json=os.path.join(HERE, "audio_it-b1-unita-23.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-23", "23.1 Se l'avessi saputo", "23.2 Ripeti")

C = dict(
    nn="23", title="Se l'avessi saputo…", subtitle="Errori e rimpianti · <b>se + congiuntivo trapassato, condizionale passato</b>",
    cover=[("SAI FARE", "parlare di errori e rimpianti, immaginare un passato diverso, dare la colpa con gentilezza"),
           ("LINGUA", "Se l'avessi saputo, avrei… · Se me l'avessi chiesto… · Se non ci fossi andata, non…"),
           ("PRONUNCIA", "avremo / avremmo, avesse / aveste: le doppie che cambiano il senso")],
    t1="errori e rimpianti",
    start=["Guarda la foto. A chi porteresti questi fiori? In quale occasione?", "Hai mai fatto una brutta figura con i genitori di qualcuno?",
           "C'è una regola culturale italiana che ti ha sorpreso?"],
    kw=[("una cosa di cui ti dispiace, nel passato", "il rimpianto"), ("una situazione imbarazzante davanti agli altri", "la brutta figura"),
        ("fiori che in Italia si portano al cimitero", "i crisantemi"), ("scarpe aperte per l'estate", "i sandali"),
        ("sentirsi male per le parole di qualcuno", "offendersi"), ("una camminata lunga e tranquilla", "la passeggiata")],
    use_words=["Racconta una brutta figura che hai fatto (o che ha fatto un amico).", "Hai un piccolo rimpianto? Quale?"],
    n1=["A: <i>fare una brutta figura</i> = <i>pagar mico</i>; <i>offendersi</i> è riflessivo (<i>si è offesa</i>)."],
    aims=["Se l'avessi saputo…: il weekend in montagna di Camila · Parliamone", "Il periodo ipotetico dell'irrealtà: se + congiuntivo trapassato",
          "Rimpianti e brutte figure (23.2) · avremo / avremmo", "Il messaggio di Camila · che cosa avresti fatto? · scrittura (100–150 parole)"],
    story="Domenica 13 giugno, sera, bar Giulia. Camila è appena tornata dalla montagna, dove ha conosciuto i genitori di Pietro (sull'Appennino). Due errori: alla mamma ha portato dei crisantemi gialli (in Italia si portano al cimitero: «Se l'avessi saputo, avrei portato una torta!»; Giulia: «Se me l'avessi chiesto, te l'avrei detto io») ed è andata in sandali, ma il papà li ha portati a fare una passeggiata di tre ore sui sassi (adesso ha male ai piedi). Finale felice: la mamma ha riso tantissimo, le ha chiesto di darle del tu e l'ha invitata di nuovo a Ferragosto. Júlia: il negozio ha risposto alla lettera, la scrivania arriva mercoledì. Domani, lunedì 14, arrivano la nuova collega allo studio e il cugino di Pietro al bar, per l'estate.",
    prob="La struttura è uguale al portoghese (<i>se eu tivesse sabido, teria levado</i>), quindi lo studente capisce subito. Errori tipici: il condizionale dopo <i>se</i> (<i>se l'avrei saputo</i>), la conseguenza al condizionale presente (<i>se avessi saputo, porterei</i>), l'accordo del participio con <i>essere</i> (<i>se fossi andato</i> detto da una donna) e la pronuncia di <i>avremmo</i> uguale a <i>avremo</i>. Cultura: i crisantemi, normali in Brasile, in Italia sono i fiori dei morti.",
    real="In Italia i <b>crisantemi</b> sono i fiori del 2 novembre (il giorno dei morti) e si portano al cimitero: non si regalano mai a una persona. Quando sei invitato a casa di qualcuno è normale portare dei dolci della pasticceria, una bottiglia di vino o dei fiori (non crisantemi e, secondo la tradizione, in numero dispari). In montagna, anche d'estate, servono scarpe chiuse: sull'Appennino i sentieri sono spesso di sassi.",
    tr=("Se l'avessi saputo…", "Ripeti: il periodo ipotetico nel passato"),
    gist=("Domenica sera, al bar Giulia. Ascolta. Com'è andato il weekend di Camila?",
          ["bene alla fine, ma con due brutte figure", "malissimo: la mamma di Pietro si è offesa", "non è andata in montagna"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Camila ha portato dei crisantemi alla mamma di Pietro.", "V"), ("In Brasile i crisantemi si portano al cimitero.", "F"),
             ("La passeggiata è durata un'ora.", "F"), ("Camila adesso ha male ai piedi.", "V"),
             ("La mamma di Pietro le ha chiesto di darle del tu.", "V"), ("La scrivania di Júlia è già arrivata.", "F")]),
    talk2=["Secondo te, perché la mamma di Pietro ha sorriso ma era «un po' strana»?", "Che cosa avresti portato tu ai genitori di Pietro?",
           "Chi arriva domani allo studio e al bar?"],
    n2=["B: 2 in Brasile non c'è questa regola · 3 tre ore · 6 arriva mercoledì.", "Il cugino di Pietro e la nuova collega arrivano lunedì 14 giugno."],
    gref="periodo_ipotetico_3",
    t4="se l'avessi saputo…",
    pA=("Completa con il congiuntivo trapassato o il condizionale passato.",
        [("Se Camila ___ (sapere) dei crisantemi, avrebbe portato una torta.", "avesse saputo"), ("Se Pietro gliel'avesse detto, lei ___ (mettere) le scarpe giuste.", "avrebbe messo"),
         ("Se non ___ (andare, noi) in montagna, non avremmo conosciuto i suoi genitori.", "fossimo andati"), ("Se me l'avessi chiesto, te lo ___ (dire) io.", "avrei detto"),
         ("Se Júlia ___ (scrivere) subito, avrebbe già la scrivania.", "avesse scritto")]),
    pAw="30mm",
    pB=[("Se l'", ["avrei saputo", "avessi saputo"], "avessi saputo", ", sarei venuta prima."),
        ("Se fossi partita prima, ", ["sarei arrivata", "arriverei"], "sarei arrivata", " in tempo."),
        ("Se avessi dormito di più, oggi non ", ["sarei", "sarei stata"], "sarei", " così stanca.")],
    rule="<b>Se</b> + <b>congiuntivo trapassato</b> (<i>avessi / fossi</i> + participio) → <b>condizionale passato</b> (<i>avrei / sarei</i> + participio): un passato che non si può cambiare. <b>Misto</b>: conseguenza oggi → condizionale presente (<i>se avessi dormito, oggi non sarei stanca</i>). Mai il condizionale dopo <i>se</i>.",
    use=["Completa: <i>Se avessi saputo l'italiano prima, …</i>", "Una cosa che avresti fatto diversamente l'anno scorso?",
         "Se non avessi scelto il tuo lavoro, che cosa avresti fatto?", "Racconta una brutta figura: che cosa avresti dovuto fare?",
         "Completa: <i>Se fossi nato/a in Italia, oggi…</i>"],
    n4="B3: periodo misto, la conseguenza è oggi.",
    t5="rimpianti e brutte figure",
    fl=(["il rimpianto", "il consiglio (troppo tardi)", "l'altra possibilità", "consolare"],
        ["Se l'avessi saputo… · Avrei dovuto… · Peccato!", "Se me l'avessi chiesto… · Avresti potuto… · Bastava…",
         "Se non fossi andato/a… · Forse sarebbe stato meglio… · Chissà!", "Non è colpa tua. · Capita a tutti. · Dai, è andata bene lo stesso!"]),
    pron=("Le doppie cambiano il senso: <b>avremo</b> (futuro) / <b>avremmo</b> (condizionale), <b>avesse</b> (lui, lei) / <b>aveste</b> (voi), <b>fossi</b> / <b>fosti</b>. Nella doppia la consonante dura di più: <i>avre<b>mm</b>o</i>, <i>ave<b>ss</b>i</i>, <i>fo<b>ss</b>imo</i>.",
          "Ascolta e ripeti. Poi leggi: «Avremo tempo domani. Avremmo avuto tempo ieri.»"),
    task=("Le brutte figure. Leggi le tre situazioni (o raccontane una tua). Per ognuna di' che cosa è successo, che cosa avresti fatto se l'avessi saputo e che cosa sarebbe successo. Poi l'insegnante racconta una sua brutta figura: dagli un consiglio «troppo tardi» e consolalo.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>Hai chiesto un cappuccino dopo cena in un ristorante elegante.</li><li>Hai dato del tu al nuovo capo il primo giorno.</li><li>Sei arrivato a una cena alle otto in punto: nessuno era pronto.</li></ul>",
          "Modello: Se avessi saputo che…, avrei… / non sarei… · Insegnante (brutta figura): Ho sbagliato nome alla madre del mio amico per tutta la sera… Lo studente: Se me l'avessi chiesto… · Avresti potuto… · Dai, capita a tutti! Chiedere almeno un periodo misto (… adesso…)."),
    talk5=["C'è una scelta della tua vita che rifaresti uguale? Perché?", "È meglio avere rimpianti o rimorsi?"],
    n5=["far battere le mani sulla doppia: <i>avre-mmo</i> più lungo di <i>avre-mo</i>.", "Pretendere i tre passaggi per ogni situazione; correggere <i>se avrei</i> subito."],
    hA=("Il messaggio di Camila a sua mamma a Recife. Scegli la forma giusta.",
        "<i>Mamma, sono tornata dalla montagna! Ho portato dei crisantemi alla mamma di Pietro: se l'{0} saputo, avrei portato dei dolci. Poi siamo andati a camminare per tre ore, io in sandali: se Pietro me l'avesse detto, {1} le scarpe da montagna. Ma lei è simpaticissima! Se non ci {2} andata, non l'avrei conosciuta. Se tu {3} stata lì, avresti riso. Se avessi dormito di più, adesso non {4} così stanca. Un bacio!</i>",
        [(["avessi", "avrei"], "avessi"), (["avrei messo", "metterei"], "avrei messo"), (["fossi", "sarei"], "fossi"),
         (["fossi", "eri"], "fossi"), (["sarei", "fossi"], "sarei")]),
    hB=("Che cosa sarebbe successo? Scrivi una frase con il periodo ipotetico.",
        [("Non ho studiato, non ho passato l'esame.", "Se avessi studiato, avrei passato l'esame."), ("Siamo partiti tardi, abbiamo perso il treno.", "Se fossimo partiti prima, non avremmo perso il treno."),
         ("Non mi hai chiamato, non sono venuta.", "Se mi avessi chiamato, sarei venuta.")]),
    watch=[("Se l'avrei saputo…", "Se l'avessi saputo…", "mai il condizionale dopo <i>se</i>."),
           ("Se avessi saputo, porterei una torta.", "Se avessi saputo, avrei portato una torta.", "conseguenza nel passato: condizionale passato."),
           ("Regalo dei crisantemi alla mamma.", "Regalo dei dolci / dei fiori.", "i crisantemi sono per il cimitero.")],
    write=("Racconta una brutta figura o un piccolo rimpianto: che cosa è successo, che cosa avresti fatto se l'avessi saputo e che cosa hai imparato.",
           "Se l'avessi saputo…", ["tre periodi ipotetici nel passato", "un periodo misto (… oggi / adesso…)", "che cosa hai imparato"]),
    cando="So parlare di errori e rimpianti e immaginare un passato diverso con il periodo ipotetico dell'irrealtà.",
    nH="Prossima unità: <i>Dopo aver studiato</i> (gli esami di Bruno).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 23 - Se l'avessi saputo")
