# Speak! Progresso B1 - Unità 19 "Ha detto che sarebbe…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 19", audio_json=os.path.join(HERE, "audio_it-b1-unita-19.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-19", "19.1 Ha detto che sarebbe...", "19.2 Ripeti")

C = dict(
    nn="19", title="Ha detto che sarebbe…", subtitle="Notizie e promesse · <b>il discorso indiretto al passato</b>",
    cover=[("SAI FARE", "riferire quello che altri hanno detto, raccontare promesse, passare una notizia"),
           ("LINGUA", "Ha detto che sarebbe tornato. · Mi ha chiesto di… · Ha spiegato che aveva…"),
           ("PRONUNCIA", "riferire con la voce neutra, senza imitare")],
    t1="le notizie degli altri",
    start=["Guarda la foto. Con chi parla? Che cosa le raccontano?", "Chi ti racconta sempre le ultime notizie?",
           "Ti è mai capitato di dire un segreto per sbaglio?"],
    kw=[("dire che farai sicuramente una cosa", "promettere"), ("riferire una notizia a un'altra persona", "passare una notizia"),
        ("andare via da un lavoro o da un posto", "lasciare"), ("un periodo di lavoro per imparare, dopo o durante gli studi", "un tirocinio"),
        ("pensare che qualcuno abbia cattive intenzioni", "pensare male"), ("la temperatura alta quando sei malato", "la febbre")],
    use_words=["Che cosa hai promesso a qualcuno e non hai ancora fatto?", "Pensi male facilmente delle persone?"],
    n1=["A: <i>lasciare</i> = <i>deixar</i> (un lavoro, una persona, un oggetto); <i>pensare male</i> = <i>pensar besteira</i>, <i>desconfiar</i>."],
    aims=["Ha detto che sarebbe… Le notizie del sabato · Parliamone", "Il discorso indiretto al passato: i tempi, tempo e luogo, di + infinito",
          "Riferire una notizia (19.2) · gioco: i messaggi vocali", "Il messaggio di Giulia a Marco · dal diretto all'indiretto · scrittura (100–150 parole)"],
    story="Sabato 8 maggio, aperitivo al bar di Giulia. Lúcia e Roberto sono tornati in Brasile: la mamma ha detto che il viaggio era stato lunghissimo ma si erano divertiti; Roberto aveva promesso a Davide che l'anno prossimo avrebbe parlato italiano meglio di lui e che sarebbe tornato per una partita allo stadio; Lúcia vuole Júlia a casa per Natale. Pietro aveva detto a Camila che l'avrebbe presentata ai genitori in montagna oggi, ma sua madre ha la febbre: rimandato a giugno (Camila dubita; Júlia ricorda San Valentino). Davide si lascia scappare un segreto: Elena gli ha detto che a giugno lascerà il bar per un tirocinio estivo in uno studio di ingegneria, e che l'avrebbe detto a Giulia lunedì.",
    prob="In portoghese il futuro nel passato è il condizionale semplice (<i>disse que viria</i>): lo studente dice <i>ha detto che verrebbe</i> invece di <i>sarebbe venuto</i>. Altri errori: <i>mi ha chiesto che torno</i> (invece di <i>di tornare</i>), il passato prossimo che non diventa trapassato (<i>ha detto che ha trovato</i>) e <i>domani, ieri, qui</i> che non cambiano.",
    real="A Bologna si gioca a calcio allo stadio Renato Dall'Ara, inaugurato nel 1927. In Italia i messaggi vocali sono molto usati, soprattutto su WhatsApp: tanti italiani preferiscono «mandare un vocale» invece di scrivere. Il tirocinio estivo è comune tra gli studenti universitari.",
    tr=("Ha detto che sarebbe…", "Ripeti: il discorso indiretto al passato"),
    gist=("Sabato, aperitivo al bar di Giulia. Ascolta. Di che cosa parlano?",
          ["delle notizie dei genitori di Júlia, di Pietro e di Elena", "di una partita allo stadio", "di un viaggio in montagna di tutto il gruppo"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Secondo Lúcia, il viaggio di ritorno è stato breve.", "F"), ("Roberto ha detto che sarebbe tornato per vedere una partita.", "V"),
             ("Oggi Camila conosce i genitori di Pietro.", "F"), ("La madre di Pietro ha la febbre.", "V"),
             ("Giulia sapeva già che Elena lascia il bar.", "F"), ("Elena ha trovato un tirocinio per l'estate.", "V")]),
    talk2=["Perché Davide dice «Ops. Forse non dovevo dirlo»?", "Camila si chiede se Pietro dica la verità. Tu che cosa pensi?",
           "Giulia vuole sapere le notizie «per prima». È giusto?"],
    n2=["B: 1 è stato lunghissimo · 3 la visita è rimandata a giugno · 5 Elena voleva dirglielo lunedì.", "Elena lascia il bar a giugno: Giulia avrà bisogno di un nuovo barista (spunto per le prossime unità)."],
    gref="discorso_indiretto_passato",
    t4="il discorso indiretto",
    pA=("Riferisci al passato. Comincia con «Ha detto che…» o «Mi ha chiesto di…».",
        [("Lúcia: «Sono stanca.» → Ha detto che ___ stanca.", "era"), ("Roberto: «Tornerò per una partita.» → Ha detto che ___ per una partita.", "sarebbe tornato"),
         ("Elena: «Ho trovato un tirocinio.» → Ha detto che ___ un tirocinio.", "aveva trovato"), ("Lúcia: «Torna a Natale!» → Mi ha chiesto ___ a Natale.", "di tornare"),
         ("Pietro: «Andremo in montagna domani.» → Ha detto che saremmo andati in montagna ___.", "il giorno dopo")]),
    pAw="30mm",
    pB=[("Pietro ha detto che ", ["sarebbe venuto", "verrebbe"], "sarebbe venuto", " a giugno."),
        ("Mi ha chiesto ", ["di chiamarlo", "che lo chiamo"], "di chiamarlo", " stasera."),
        ("Elena ha spiegato che ", ["aveva trovato", "ha trovato"], "aveva trovato", " un tirocinio.")],
    rule="Verbo introduttivo al <b>passato</b> → i tempi vanno indietro: presente → <b>imperfetto</b>; passato prossimo → <b>trapassato</b>; futuro → <b>condizionale passato</b> (<i>sarebbe tornato</i>); imperativo → <b>di + infinito</b>. Cambiano anche <i>oggi → quel giorno, domani → il giorno dopo, qui → lì</i>.",
    use=["Che cosa ti ha detto l'ultima persona con cui hai parlato? <i>Mi ha detto che…</i>", "Una promessa che qualcuno ti ha fatto: <i>Mi ha promesso che…</i>",
         "Che cosa ti dicevano sempre i tuoi genitori da piccolo/a? <i>Mi dicevano di…</i>", "Una notizia che hai letto: <i>Il giornale diceva che…</i>",
         "Che cosa ti ha chiesto il tuo capo o il tuo insegnante? <i>Mi ha chiesto di…</i>"],
    n4="A5 e B: anche <i>domani → il giorno dopo</i>. Nell'orale accettare <i>ha detto che viene</i>, mai <i>verrebbe</i>.",
    t5="riferire una notizia",
    fl=(["riferire", "riferire un ordine", "promesse", "commentare"],
        ["Mi ha detto che… · Mi ha raccontato che… · Ha spiegato che…", "Mi ha chiesto di… · Mi ha detto di… · Mi ha pregato di…",
         "Mi aveva promesso che… · Aveva detto che avrebbe… · E l'ha fatto / non l'ha fatto.", "Non ci credo! · Me l'ha detto in segreto. · Acqua in bocca!"]),
    pron=("Quando riferiamo le parole di un altro, la voce è <b>neutra</b> e più <b>bassa</b>: non imitiamo il tono della persona. Si alza solo sulla parola importante: <i>Ha detto che sarebbe tornato <b>a GIUgno</b>.</i>",
          "Ascolta e ripeti. Poi riferisci tre frasi dette dall'insegnante."),
    task=("I messaggi vocali. L'insegnante legge un «vocale» alla volta, come se fosse un tuo amico. Poi ti chiede: «Che cosa ha detto?». Riferisci il messaggio al passato. Alla fine racconta una promessa che qualcuno ti ha fatto: l'ha mantenuta?",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>Marta: «Arrivo domani alle otto. Vieni a prendermi?»</li><li>Il capo: «Manda il progetto entro venerdì!»</li><li>Luca: «Ho perso il treno. Ci vediamo stasera.»</li><li>La mamma: «Ti ho spedito un pacco. Chiamami quando arriva!»</li></ul>",
          "Risposte modello: Marta ha detto che sarebbe arrivata il giorno dopo alle otto e mi ha chiesto se andavo a prenderla. · Il capo mi ha detto di mandare il progetto entro venerdì. · Luca ha detto che aveva perso il treno e che ci saremmo visti quella sera. · La mamma ha detto che mi aveva spedito un pacco e mi ha chiesto di chiamarla."),
    talk5=["Sai mantenere un segreto?", "Una promessa importante che hai fatto: l'hai mantenuta?"],
    n5=["voce neutra: far riferire una frase prima «imitando», poi in modo neutro, e confrontare.", "<i>Acqua in bocca!</i> = non dirlo a nessuno."],
    hA=("Sabato sera Giulia scrive a Marco. Scegli la forma giusta.",
        "<b>Giulia:</b> Marco, indovina! Davide mi ha detto che Elena {0} il bar a giugno. Lei non mi ha detto niente! Davide ha spiegato che Elena {1} un tirocinio e che me lo {2} lunedì. Allora l'ho chiamata e le ho chiesto {3} subito. Mi ha risposto che le {4} moltissimo e che sarebbe tornata al bar a settembre!",
        [(["avrebbe lasciato", "lascerebbe"], "avrebbe lasciato"), (["aveva trovato", "ha trovato"], "aveva trovato"), (["avrebbe detto", "dice"], "avrebbe detto"),
         (["di passare", "che passa"], "di passare"), (["dispiaceva", "dispiace"], "dispiaceva")]),
    hB=("Riferisci al passato.",
        [("Camila: «Pietro è simpatico.»", "Camila ha detto che Pietro era simpatico."), ("Davide: «Domani porterò le sfrappole.»", "Davide ha detto che il giorno dopo avrebbe portato le sfrappole."),
         ("Giulia a Elena: «Chiamami!»", "Giulia ha chiesto a Elena di chiamarla.")]),
    watch=[("Ha detto che verrebbe a giugno.", "Ha detto che sarebbe venuto a giugno.", "futuro nel passato = condizionale passato."),
           ("Mi ha chiesto che torno.", "Mi ha chiesto di tornare.", "ordini e richieste: <i>di</i> + infinito."),
           ("Ha detto che ci andremo domani.", "Ha detto che ci saremmo andati il giorno dopo.", "cambiano il tempo e <i>domani</i>.")],
    write=("Racconta una conversazione importante che hai avuto (con un amico, un familiare, un collega): che cosa ti ha detto, che cosa ti ha chiesto, che cosa ti ha promesso e com'è finita.",
           "La settimana scorsa … mi ha detto che…", ["cinque frasi al discorso indiretto con tempi diversi", "un ordine riferito (<i>mi ha chiesto di…</i>)", "una parola di tempo cambiata (<i>il giorno dopo, quel giorno</i>)"]),
    cando="So riferire quello che altri hanno detto, chiesto e promesso usando il discorso indiretto al passato.",
    nH="Prossima unità: <i>Ripasso 2</i> (unità 11–19).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 19 - Ha detto che sarebbe")
