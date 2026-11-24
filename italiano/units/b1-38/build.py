# Speak! Progresso B1 - Unità 38 "Ne vale la pena" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 38", audio_json=os.path.join(HERE, "audio_it-b1-unita-38.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-38", "38.1 Ne vale la pena", "38.2 Pro e contro")

C = dict(
    nn="38", title="Ne vale la pena", subtitle="Natale in Brasile? Júlia e Bruno decidono · <b>valerne la pena, tenerci, entrarci</b>",
    cover=[("SAI FARE", "valutare una decisione, dire che cosa è importante per te, reagire"),
           ("LINGUA", "valerne la pena · tenerci · entrarci · sentirsela · smetterla"),
           ("PRONUNCIA", "i blocchi fissi: <i>ne vale la pena · ci tengo · che c'entra?</i>")],
    t1="decisioni e priorità",
    start=["Guarda la foto. Una partita a scacchi è piena di decisioni: tu decidi in fretta o ci pensi a lungo?", "Qual è stata l'ultima decisione difficile che hai preso?",
           "Per che cosa spenderesti molti soldi senza pensarci due volte?"],
    kw=[("il viaggio di andata e quello di ritorno", "andata e ritorno"), ("una fermata intermedia di un volo, per cambiare aereo", "lo scalo"),
        ("una cosa a cui teniamo molto e che mettiamo al primo posto", "la priorità"), ("consegnare un lavoro entro una certa data", "la scadenza"),
        ("pensare a vantaggi e svantaggi prima di decidere", "valutare"), ("cambiare idea molte volte, non sapere che cosa fare", "essere indeciso")],
    use_words=["Preferisci un volo diretto più caro o uno con scalo più economico? Perché?", "Quali sono le tue priorità in questo periodo della tua vita?"],
    n1=["A: <i>la scadenza</i> = o prazo (non «a validade»: <i>la data di scadenza</i> del latte).", "Riprendere la domanda della mamma (unità 17 e 19): Júlia andrà a casa per Natale?"],
    aims=["Ne vale la pena: Júlia, Bruno e Chiara guardano i voli · Parliamone", "valerne la pena · tenerci · entrarci · sentirsela · smetterla",
          "Pro e contro (38.2) · i blocchi fissi", "Il messaggio di Chiara · riscrivi · scrittura (100–150 parole)"],
    story="Sabato 4 dicembre, sera, a casa di Júlia. Júlia, suo fratello Bruno e Chiara guardano i voli per Belo Horizonte: 1.400 euro andata e ritorno, 22 ore con lo scalo a Lisbona. Bruno ha dubbi (soldi, tre esami a gennaio); Júlia dice che ne vale la pena: la mamma ci tiene tantissimo (glielo chiede da maggio) e sono due anni che non passano il Natale a casa. Il progetto di Galli non c'entra: Júlia consegnerà il disegno della pergola il 20. Bruno non se la sente di lasciare Chiara sola, ma Chiara va dai suoi come ogni anno. Decidono: partono il 22, tornano il 2 gennaio. Chiara vuole una foto della mamma all'aeroporto.",
    prob="In portoghese si dice <i>vale a pena</i>, <i>faço questão</i>, <i>o que isso tem a ver?</i>, <i>não tenho coragem de</i>. Il brasiliano dice <i>vale la pena</i> (corretto prima di un infinito: <i>vale la pena partire</i>), ma quando la cosa è già stata detta l'italiano aggiunge <b>ne</b>: <i>Ne vale la pena</i>. Al passato l'ausiliare è <b>essere</b> e il participio va al femminile: <i>ne è valsa la pena</i>. <i>Faço questão</i> = <i>ci tengo</i> (mai <s>faccio questione</s>); <i>o que tem a ver?</i> = <i>che c'entra?</i>; <i>não tenho coragem</i> = <i>non me la sento</i>.",
    real="Un proverbio che tutti gli italiani conoscono: <b>«Natale con i tuoi, Pasqua con chi vuoi»</b>. In Italia sono giorni festivi il <b>25</b> e il <b>26 dicembre</b> (Santo Stefano) e il <b>6 gennaio</b> (Epifania): per questo molte persone stanno a casa fino al 6. Da Bologna non ci sono voli diretti per il Brasile: bisogna fare almeno uno scalo, per esempio a Lisbona, a Madrid o a Roma.",
    tr=("Ne vale la pena", "Pro e contro"),
    gist=("Sabato sera, a casa di Júlia. Ascolta. Che cosa decidono Júlia e Bruno?",
          ["di passare il Natale in Brasile con i genitori", "di restare a Bologna per Natale", "di invitare i genitori a Bologna"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il volo costa 1.400 euro andata e ritorno.", "V"), ("Bruno ha due esami a gennaio.", "F"),
             ("Júlia e Bruno non passano il Natale a casa da due anni.", "V"), ("Júlia consegnerà il disegno della pergola dopo Natale.", "F"),
             ("Chiara passerà il Natale con la sua famiglia.", "V"), ("Júlia e Bruno torneranno a Bologna il 2 gennaio.", "V")]),
    talk2=["Secondo te, 22 ore di viaggio per dieci giorni: ne vale la pena?", "Bruno ha ragione a pensare ai soldi e agli esami? Perché?",
           "Nella tua famiglia il Natale è importante? Dove lo passi di solito?"],
    n2=["B: 2 ne ha tre · 4 la consegnerà il 20 dicembre.", "Ripresa: la domanda della mamma (unità 17 e 19); il progetto di Galli e la pergola (unità 37)."],
    gref="verbi_ci_ne_b1",
    t4="ne vale la pena, ci tengo",
    pA=("Completa con ne vale, ci tengo, c'entra, me la sento o smettila.",
        [("Il volo è caro, ma vedo la mamma: ___ la pena.", "ne vale"), ("Galli non ___ con il nostro Natale!", "c'entra"),
         ("___ a finire bene la pergola prima di partire.", "Ci tengo"), ("Non ___ di lasciare Chiara sola a Natale.", "me la sento"),
         ("___ di cercare problemi, Bruno!", "Smettila")]),
    pAw="20mm",
    pB=[("Il viaggio era lungo, ma ", ["ne è valsa", "ne ha valso"], "ne è valsa", " la pena."),
        ("La mamma ", ["ci tiene", "ne tiene"], "ci tiene", " tantissimo a vederci."),
        ("Scusate, io non ", ["c'entro", "ne entro"], "c'entro", " niente.")],
    rule="<b>valerne la pena</b> = valer a pena: <i>Ne vale la pena</i> (pass. <i>ne è valsa la pena</i>) · <b>tenerci</b> (a qualcosa / a + infinito) = fazer questão, ser importante: <i>Ci tengo</i> (pass. <i>ci ho tenuto</i>) · <b>entrarci</b> = ter a ver: <i>Che c'entra? Io non c'entro.</i> · <b>sentirsela di</b> = ter coragem, estar disposto: <i>Non me la sento.</i> · <b>smetterla</b> = parar: <i>Smettila!</i>",
    use=["Un viaggio lungo e caro di cui <i>ne è valsa la pena</i>: dove, quando?", "A che cosa ci tieni tantissimo nella tua vita?",
         "Una cosa che non te la senti di fare (anche se tutti la fanno)?", "Una discussione in cui qualcuno ha detto: «Che c'entra?»",
         "Che cosa vorresti che qualcuno smettesse di fare?"],
    n4="A: 1 <i>ne</i> = il viaggio · 4 <i>sentirsela di</i> + infinito. B1 <i>valere</i> → ausiliare <i>essere</i>, participio femminile (<i>la pena</i>).",
    t5="pro e contro",
    fl=(["valutare", "dire che è importante", "dire che non c'entra", "esitare o reagire"],
        ["Ne vale la pena? · Secondo me non ne vale la pena. · Ne è valsa la pena!", "Ci tengo (tantissimo) a… · Ci tiene molto. · Non ci tengo.",
         "Che c'entra? · Questo non c'entra niente! · C'entra eccome!", "Non me la sento. · Smettila! · Dai, smettetela di litigare!"]),
    pron=("Questi verbi si dicono come un <b>blocco unico</b>, senza pause: <i>ne-vale-la-pena</i>, <i>ci-tengo</i>, <i>che-c'entra</i>. In <i>c'entra</i> la <i>c</i> si pronuncia [tʃ], come in <i>cena</i>.",
          "Ascolta e ripeti. Poi leggi: «Il volo è caro, ma ne vale la pena: la mamma ci tiene.»"),
    task=("Pro e contro: l'insegnante ti propone una decisione. Insieme valutate vantaggi e svantaggi e decidete: «Ne vale la pena?». Usa almeno <b>valerne la pena, tenerci</b> ed <b>entrarci</b>. Poi scambiatevi i ruoli.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>un master all'estero di due anni</li><li>un cane in un appartamento piccolo</li><li>una macchina nuova o usata</li><li>cambiare lavoro per guadagnare di più</li><li>una festa di matrimonio grande</li><li>imparare una terza lingua</li></ul>",
          "Insegnante: Costa tanto, e poi c'è il lavoro… Lo studente: Ne vale la pena, perché ci tengo a… · Il lavoro non c'entra! · Non me la sento di… Correggere <i>vale la pena</i> senza <i>ne</i> quando la cosa è già detta e <i>ne ha valso</i>."),
    talk5=["Hai mai fatto un viaggio molto lungo per vedere la famiglia? Ne è valsa la pena?", "Che cosa pensi del proverbio «Natale con i tuoi, Pasqua con chi vuoi»?"],
    n5=["Far dire i blocchi senza pause: <i>ne vale la pena</i>, <i>ci tengo</i>, <i>che c'entra</i>.", "Pretendere almeno una decisione motivata con <i>ne vale / non ne vale la pena perché…</i>"],
    hA=("Il messaggio di Chiara a un'amica. Scegli la forma giusta.",
        "<i>Ciao Giorgia! Bruno e Júlia vanno in Brasile per Natale. Il volo costa tantissimo, ma secondo me {0} la pena: la loro mamma {1} tiene da mesi. Bruno all'inizio diceva che non {2} sentiva di lasciarmi sola. Gli ho detto: «Io che {3}? Vado dai miei come ogni anno!» E alla fine gli ho detto di {4} di trovare scuse. Partono il 22. Un bacio, Chiara</i>",
        [(["ne vale", "vale"], "ne vale"), (["ci", "ne"], "ci"), (["se la", "si"], "se la"),
         (["c'entro", "ci entro"], "c'entro"), (["smetterla", "smettere"], "smetterla")]),
    hB=("Riscrivi le frasi con valerne la pena, tenerci, entrarci o sentirsela.",
        [("Per me è molto importante vedere la mamma.", "Ci tengo (molto) a vedere la mamma."),
         ("Non ho il coraggio di dirlo alla mamma.", "Non me la sento di dirlo alla mamma."),
         ("Il viaggio è stato lungo, ma è stato giusto farlo.", "Il viaggio è stato lungo, ma ne è valsa la pena.")]),
    watch=[("Il volo è caro, ma vale la pena.", "Il volo è caro, ma <b>ne</b> vale la pena.", "la cosa è già detta → <i>ne</i>."),
           ("Ne ha valso la pena.", "Ne <b>è valsa</b> la pena.", "<i>valere</i> → <i>essere</i>, accordo con <i>la pena</i>."),
           ("Faccio questione di venire.", "Ci tengo a venire.", "<i>fazer questão</i> → <i>tenerci</i>.")],
    write=("Racconta una decisione importante (un viaggio, un trasloco, un lavoro, un acquisto): che cosa hai valutato, a che cosa ci tenevi e se alla fine ne è valsa la pena.",
           "Qualche anno fa…", ["almeno una frase con <i>ne vale / ne è valsa la pena</i>", "almeno una frase con <i>ci tengo / ci tenevo a</i>", "<i>entrarci</i> o <i>sentirsela</i> almeno una volta"]),
    cando="So valutare una decisione e dire che cosa è importante per me con valerne la pena, tenerci ed entrarci.",
    nH="Prossima unità: <i>Tre anni a Bologna</i> (tutti i tempi del racconto).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 38 - Ne vale la pena")
