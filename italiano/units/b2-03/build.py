# Speak! Indipendenza B2 - Unità 03 "Cercasi ingegnere" - formato ridotto (italiano/lean_b1.py, level="B2")
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Indipendenza"
setup(band="B2 · UNITÀ 03", audio_json=os.path.join(HERE, "audio_it-b2-unita-03.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b2-unita-03", "03.1 Cercasi ingegnere", "03.2 Ripeti")

C = dict(
    level="B2", words="150–200",
    nn="03", title="Cercasi ingegnere", subtitle="Il colloquio di Davide · <b>verbi con preposizione e i pronomi ci e ne</b>",
    cover=[("SAI FARE", "presentarti a un colloquio, parlare di interessi e punti deboli"),
           ("LINGUA", "occuparsi di · contare su · dipendere da · ci penso, me ne occupo"),
           ("PRONUNCIA", "<i>ci</i> e <i>ne</i> attaccati al verbo: <i>ci-credo, me-ne-occupo</i>")],
    t1="il lavoro che cerchi",
    start=["Guarda la foto. Che cosa scrivi per primo in un curriculum?", "Ricordi il tuo primo colloquio di lavoro? Com'è andato?",
           "Che cosa ti rende nervoso/a in un colloquio?"],
    kw=[("mandare il proprio curriculum per un posto di lavoro", "candidarsi"), ("il periodo di lavoro per imparare, durante o dopo gli studi", "il tirocinio"),
        ("che chiede molto agli altri, difficile da accontentare", "esigente"), ("lavorare con poco tempo e molte richieste", "lavorare sotto pressione"),
        ("il lato in cui una persona non è forte", "il punto debole"), ("il documento con studi ed esperienze di lavoro", "il curriculum")],
    use_words=["Hai mai fatto un tirocinio? Che cosa hai imparato?", "Qual è il tuo punto debole sul lavoro (o nello studio)? Dillo con sincerità!"],
    n1=["A: <i>esigente</i> = exigente (attenzione: <i>severo</i> è più duro).", "Riprendere la laurea di Davide (B1 36) e i curriculum mandati a tre studi (Ripasso 4)."],
    aims=["Cercasi ingegnere: il colloquio di Davide · Parliamone", "verbi + preposizione (a, di, da, su, in) · ci e ne al posto del complemento",
          "Il colloquio · ripeti (03.2) · ci e ne attaccati al verbo", "La mail di ringraziamento · riscrivi · scrittura (150–200 parole)"],
    story="Giovedì 2 marzo 2028, ore 10, in una società di ingegneria a Casalecchio di Reno. Davide ha un colloquio con l'ingegnera Rinaldi (Lei, formale). Si è laureato a novembre con una tesi sul risparmio energetico negli edifici storici; la società si occupa di ristrutturazioni in centro storico (gliene ha parlato «un'amica architetta»: Júlia). Durante il tirocinio ha partecipato a un progetto su un palazzo del Settecento. Si è abituato ad alzarsi presto con la maratona; per finire la tesi ha rinunciato a tutto, perfino alla moto. Con un cliente che cambia idea ogni settimana: capire di che cosa si tratta, convincerlo a fidarsi. Punto debole: si dimentica di mangiare. Rinaldi decide entro venerdì prossimo; se lo scelgono, lavorerà con lei, «molto esigente». «Ci credo molto.»",
    prob="Molti verbi hanno una preposizione diversa in portoghese: <i>gostar de</i> ma <i>piacere</i> (senza <i>di</i>); <i>pensar em</i> → <i>pensare <b>a</b></i> (non <s>pensare in</s>); <i>depender de</i> → <i>dipendere <b>da</b></i>; <i>confiar em</i> → <i>fidarsi <b>di</b></i>; <i>contar com</i> → <i>contare <b>su</b></i>; <i>insistir em</i> → <i>insistere <b>su</b> / <b>per</b></i>. E <i>pensare di</i> + infinito = pretender / achar. Il complemento si riprende con <b>ci</b> (a, su, in: <i>ci penso, ci conto, ci credo</i>) o con <b>ne</b> (di, da: <i>me ne occupo, ne dipende, ne ho sentito parlare</i>).",
    real="Al colloquio di lavoro in Italia si usa il <b>Lei</b>, anche con persone giovani. Il curriculum più diffuso è il modello europeo (<b>Europass</b>). Dopo la laurea si è «dottore», ma per <b>firmare i progetti</b> un ingegnere deve superare l'<b>esame di Stato</b> e iscriversi all'<b>Albo</b> (l'Ordine degli ingegneri) della sua provincia.",
    tr=("Cercasi ingegnere", "Ripeti: il colloquio"),
    gist=("Giovedì mattina, a Casalecchio. Ascolta. Com'è andato il colloquio di Davide?",
          ["bene: l'ingegnera lo chiamerà entro venerdì prossimo", "male: Davide non ha l'esperienza giusta", "benissimo: Davide comincia lunedì"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("La tesi di Davide parla di risparmio energetico.", "V"), ("La società si occupa di nuovi grattacieli.", "F"),
             ("Durante il tirocinio Davide andava in cantiere ogni giorno.", "F"), ("Per la tesi Davide ha rinunciato anche alla moto.", "V"),
             ("Secondo Davide, un cliente difficile spesso ha un problema di soldi.", "V"), ("L'ingegnera Rinaldi dice di essere molto tranquilla.", "F")]),
    talk2=["Davide ha risposto bene? Che cosa avresti risposto tu sul punto debole?", "Chi è «il cliente così» di cui Davide ha sentito parlare?",
           "L'ingegnera Rinaldi ti sembra un buon capo? Perché?"],
    n2=["B: 2 di ristrutturazioni in centro storico · 3 due volte alla settimana · 6 «molto esigente».", "Talk2: il cliente è Galli (Júlia ne parla sempre!)."],
    gref="verbi_preposizione_b2",
    t4="occuparsi di, contare su",
    pA=("Completa con la preposizione giusta (a, di, da, su, in) e, se serve, l'articolo.",
        [("Mi interesso ___ edifici storici.", "di"), ("Il risultato dipende ___ cliente.", "dal"),
         ("Può contare ___ di me.", "su"), ("Ho rinunciato ___ moto per due mesi.", "alla"), ("Penso spesso ___ mio futuro.", "al")]),
    pAw="14mm",
    pB=[("Della moto? Non ", ["me ne", "mi ci"], "me ne", " occupo più."),
        ("Al colloquio? ", ["Ci", "Ne"], "Ci", " penso da una settimana."),
        ("In questo lavoro ", ["ci", "ne"], "ci", " credo molto.")],
    rule="Il verbo decide la preposizione: <b>a</b> (pensare, rinunciare, partecipare, abituarsi) · <b>di</b> (occuparsi, interessarsi, fidarsi, parlare) · <b>da</b> (dipendere) · <b>su</b> (contare, insistere) · <b>in</b> (credere in qualcosa). Il complemento si sostituisce con <b>ci</b> (a, su, in: <i>ci penso, ci conto, ci credo</i>) o con <b>ne</b> (di, da: <i>me ne occupo, ne parliamo</i>). <b>Pensare a</b> = pensar em; <b>pensare di</b> + infinito = pretender.",
    use=["Di che cosa ti occupi nel tuo lavoro (o nei tuoi studi)?", "A che cosa non rinunceresti mai, neanche per un lavoro fantastico?",
         "Su chi puoi contare sempre?", "Da che cosa dipende, per te, un buon lavoro: dallo stipendio, dalle persone o da altro?",
         "Che cosa pensi di fare il prossimo anno? Ci pensi spesso?"],
    n4="A: 2 <i>da + il</i> → <i>dal</i> · 3 <i>su di me</i> (con i pronomi tonici) · 4 <i>a + la</i>. B: <i>occuparsi di</i> → <i>ne</i>; <i>pensare a, credere in</i> → <i>ci</i>.",
    t5="il colloquio",
    fl=(["presentarsi", "parlare di esperienze", "rispondere a domande difficili", "chiudere il colloquio"],
        ["Mi occupo di… · Mi interesso di… da… · Mi sono laureato/a in…", "Ho partecipato a… · Mi sono abituato/a a… · Ho imparato a…",
         "Dipende da… · Su di me si può contare. · Ci ho pensato molto.", "Vorrei sapere di che cosa si tratta. · Con chi lavorerei? · Grazie per il Suo tempo."]),
    pron=("<i>Ci</i> e <i>ne</i> si pronunciano attaccati al verbo, senza pausa: <i>ci-credo</i>, <i>ci-penso</i>, <i>me-ne-occupo</i>, <i>ne-ho-sentito-parlare</i>. La voce sale sul verbo, non sul pronome.",
          "Ascolta e ripeti. Poi leggi: «Voi vi occupate proprio di ristrutturazioni: un'amica me ne ha parlato.»"),
    task=("Il colloquio: l'insegnante è il/la selezionatore/selezionatrice di un'azienda (o di una scuola, un ospedale, un hotel). Tu ti candidi. Rispondi alle domande con il Lei: interessi, esperienze, come lavori sotto pressione, punti deboli. Alla fine fai due domande. Poi scambiatevi i ruoli.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>Di che cosa si occupa adesso?</li><li>Perché si è candidato/a?</li><li>Ha partecipato a progetti importanti?</li><li>Su di Lei si può contare?</li><li>Da che cosa dipende la Sua motivazione?</li><li>A che cosa rinuncerebbe?</li></ul>",
          "Insegnante: Di che cosa si occupa? Ci ha pensato bene? Lo studente: Mi occupo di… · Ci ho pensato molto. · Dipende da… · Ne ho parlato con… Correggere le preposizioni calcate sul portoghese (<i>pensare in, dipendere di, contare con</i>)."),
    talk5=["Meglio un lavoro sicuro e noioso o uno interessante ma incerto?", "Che cosa conta di più in un colloquio: il curriculum o la personalità?"],
    n5=["Il colloquio si fa con il <i>Lei</i>: correggere il passaggio al <i>tu</i>.", "Pretendere almeno tre risposte con <i>ci</i> o <i>ne</i> al posto del complemento."],
    hA=("La mail di ringraziamento di Davide. Scegli la forma giusta.",
        "<i>Gentile ingegnera Rinaldi, La ringrazio per il colloquio di oggi. Come Le ho detto, mi interesso {0} risparmio energetico da molti anni e {1} credo molto. Il progetto di cui mi ha parlato mi interessa: {2} ho pensato tutto il pomeriggio. Può contare {3} di me anche per il cantiere. Resto in attesa di una Sua risposta e, se {4} ha bisogno, Le mando altri documenti. Cordiali saluti, Davide</i>",
        [(["di", "in"], "di"), (["ci", "ne"], "ci"), (["Ci", "Ne"], "Ci"), (["su", "con"], "su"), (["ne", "ci"], "ne")]),
    hB=("Riscrivi la parte sottolineata con ci o ne.",
        [("Penso <u>al colloquio</u> tutto il giorno.", "Ci penso tutto il giorno."),
         ("Mi occupo <u>dei calcoli</u>.", "Me ne occupo."),
         ("Puoi contare <u>su questo progetto</u>.", "Ci puoi contare. / Puoi contarci.")]),
    watch=[("Penso in te.", "Penso <b>a</b> te.", "<i>pensar em</i> → <i>pensare a</i>."),
           ("Dipende di te.", "Dipende <b>da</b> te.", "<i>depender de</i> → <i>dipendere da</i>."),
           ("Conto con te.", "Conto <b>su</b> di te.", "<i>contar com</i> → <i>contare su</i>.")],
    write=("Scrivi una lettera di presentazione (una candidatura) per il lavoro dei tuoi sogni: chi sei, di che cosa ti occupi, a che cosa hai partecipato, perché possono contare su di te.",
           "Gentile…", ["almeno cinque verbi con preposizione (<i>occuparsi di, partecipare a, contare su…</i>)", "almeno due frasi con <i>ci</i> o <i>ne</i>", "registro formale con il <i>Lei</i> e una chiusura (<i>Cordiali saluti</i>)"]),
    cando="So presentarmi a un colloquio usando i verbi con la preposizione giusta e i pronomi ci e ne.",
    nH="Prossima unità: <i>Secondo indiscrezioni</i> (condizionale giornalistico; l'albergo di Galli sul giornale).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B2 Indipendenza 03 - Cercasi ingegnere")
