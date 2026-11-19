# Speak! Progresso B1 - Unità 12 "Credevo che…" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 12", audio_json=os.path.join(HERE, "audio_it-b1-unita-12.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-12", "12.1 Credevo che...", "12.2 Ripeti")

C = dict(
    nn="12", title="Credevo che…", subtitle="Prime impressioni e stereotipi · <b>la concordanza dei tempi</b>",
    cover=[("SAI FARE", "raccontare le prime impressioni, parlare di stereotipi, dire che hai cambiato idea"),
           ("LINGUA", "Pensavo che fosse timida. · Credevo che parlaste con le mani. · Credevo di essere…"),
           ("PRONUNCIA", "l'intonazione del contrasto: «credevo che… e invece…»")],
    t1="prima e dopo",
    start=["Guarda la foto. Dove sono queste persone? Che cosa bevono?", "Che cosa pensavi dell'Italia prima di studiare italiano?",
           "Che cosa pensano gli stranieri dei brasiliani?"],
    kw=[("l'idea che hai di una persona appena la conosci", "una prima impressione"), ("un'idea fissa su un gruppo di persone", "uno stereotipo"),
        ("che fa fatica a parlare con persone nuove", "timido"), ("il contrario di simpatico", "antipatico"),
        ("alzare i bicchieri per festeggiare", "brindare"), ("eccetto, a parte", "tranne")],
    use_words=["La tua prima impressione su una persona di solito è giusta?", "Sei timido/a con le persone nuove?"],
    n1=["A: <i>tranne</i> = <i>exceto, menos</i>; <i>brindare</i> = <i>brindar</i> (con <i>a</i>: <i>brindiamo agli amici</i>)."],
    aims=["Credevo che… Il primo aperitivo al bar di Giulia · Parliamone", "La concordanza dei tempi: penso che sia / pensavo che fosse",
          "Stereotipi e prime impressioni (12.2) · gioco di ruolo: un italiano pieno di stereotipi", "Le prime impressioni di Camila · dal presente al passato · scrittura (100–150 parole)"],
    story="Sabato 13 marzo, sera: il primo aperitivo serale del bar di Giulia; Elena, la nuova barista, porta gli spritz. Al tavolo Júlia, Marco, Camila e Davide parlano di stereotipi. Camila credeva che l'aperitivo fosse solo un bicchiere di vino e che gli italiani parlassero con le mani (vero!). Giulia pensava che in Brasile facesse caldo tutto l'anno; Júlia pensava che gli italiani mangiassero la pasta due volte al giorno (Marco quasi sì) e che fossero sempre in ritardo (Davide sì). Le prime impressioni: Marco pensava che Júlia fosse timida (non capiva niente!), lei pensava che lui fosse antipatico (era concentrato).",
    prob="La concordanza è uguale al portoghese (<i>achava que fosse</i>), ma il brasiliano parlato preferisce l'indicativo (<i>achava que era</i>): lo studente dice <i>pensavo che era</i>. Accettarlo nella conversazione veloce, correggerlo nello scritto. Altri errori: <i>pensavo che sia</i> e <i>credevo che io fossi</i> invece di <i>credevo di essere</i>. Lessico: <i>chato</i> → <i>noioso, pesante</i>.",
    real="L'aperitivo è nato a Torino e a Milano; lo spritz viene dal Veneto. A Bologna con l'aperitivo arrivano taglieri di salumi e formaggi, e per molti studenti diventa una cena: l'<i>apericena</i>. Gli italiani mangiano circa 23 kg di pasta a testa all'anno. All'università c'è il «quarto d'ora accademico».",
    tr=("Credevo che…", "Ripeti: pensavo che + congiuntivo imperfetto"),
    gist=("Sabato sera, il primo aperitivo al bar di Giulia. Ascolta. Di che cosa parlano soprattutto?",
          ["di stereotipi e di prime impressioni", "di un viaggio a Roma", "del lavoro di Elena"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("È il primo aperitivo serale del bar.", "V"), ("Camila pensava che l'aperitivo fosse una cena completa.", "F"),
             ("Secondo Júlia, a Belo Horizonte fa sempre caldo.", "F"), ("Marco mangia la pasta quasi tutti i giorni.", "V"),
             ("Davide è sempre puntuale.", "F"), ("Il primo giorno Marco pensava che Júlia fosse timida.", "V")]),
    talk2=["Perché Júlia parlava pochissimo il primo giorno?", "Giulia dice: «Le prime impressioni non valgono niente». Sei d'accordo?",
           "Gli stereotipi hanno sempre un po' di verità?"],
    n2=["B: 2 pensava che fosse solo un bicchiere di vino · 3 d'inverno, di notte, ci sono anche dieci gradi · 5 è sempre in ritardo.", "<i>e invece</i> = <i>mas na verdade</i>."],
    gref="concordanza_tempi",
    t4="la concordanza dei tempi",
    pA=("Porta le frasi al passato.",
        [("Penso che l'italiano sia facile. → Pensavo che l'italiano ___ facile.", "fosse"), ("Credo che i bolognesi mangino tanto. → Credevo che ___ tanto.", "mangiassero"),
         ("Mi sembra che Davide abbia ragione. → Mi sembrava che ___ ragione.", "avesse"), ("Ho paura che piova. → Avevo paura che ___.", "piovesse"),
         ("Spero che tu venga. → Speravo che tu ___.", "venissi")]),
    pB=[("Pensavo che Marco ", ["fosse", "sia"], "fosse", " antipatico."),
        ("Credevo ", ["di essere", "che io fossi"], "di essere", " in ritardo."),
        ("Oggi penso che Bologna ", ["sia", "fosse"], "sia", " la mia seconda casa.")],
    rule="Verbo principale al <b>presente</b> → congiuntivo <b>presente</b>: <i>penso che sia</i>. Verbo principale al <b>passato</b> → congiuntivo <b>imperfetto</b>: <i>pensavo che fosse, non immaginavo che si mangiasse</i>. Stesso soggetto → <b>di + infinito</b>: <i>credevo di essere in ritardo</i>.",
    use=["Che cosa pensavi dell'Italia prima di studiare italiano? <i>Pensavo che…</i>", "La prima impressione su un collega: <i>Mi sembrava che…</i>",
         "Una cosa che non immaginavi del tuo lavoro.", "Da bambino/a, che cosa credevi dei grandi?", "Che cosa pensi oggi della stessa cosa? <i>Oggi penso che…</i>"],
    n4="Far dire anche la seconda parte: <i>Pensavo che facesse freddo… e invece fa caldo!</i>",
    t5="stereotipi e prime impressioni",
    fl=(["prime impressioni", "cambiare idea", "parlare di stereotipi", "non generalizzare"],
        ["All'inizio pensavo che… · Mi sembrava che… · Mi ha fatto una buona impressione.", "E invece… · Poi ho capito che… · Mi sbagliavo.",
         "Si dice che… · Molti pensano che… · È un luogo comune.", "In generale… · Dipende dalla persona. · Non si può generalizzare."]),
    pron=("Quando raccontiamo un'idea sbagliata, la prima parte resta <b>sospesa</b> (<i>Pensavo che facesse caldo…</i>) e la seconda <b>scende</b> con forza su <i>e invece</i>: <i>…e in<b>VE</b>ce fa freddo!</i>",
          "Ascolta e ripeti. Poi completa ogni frase a voce con «e invece…»."),
    task=("Gioco di ruolo. Un amico italiano è appena arrivato in Brasile ed è pieno di stereotipi. Correggilo con gentilezza. Poi racconta un'idea che avevi su un paese, una città o una persona e com'è cambiata.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>che cosa pensavi prima</li><li>che cosa è successo, e invece…</li><li>che cosa pensi oggi</li></ul>",
          "Insegnante: Pensavo che in Brasile si ballasse la samba tutti i giorni! · Credevo che tutti giocassero a calcio sulla spiaggia. · Pensavo che la capitale fosse Rio! · Non immaginavo che a São Paulo facesse freddo. · E il caffè? Credevo che andasse tutto all'estero…"),
    talk5=["Qual è lo stereotipo sui brasiliani più sbagliato?", "Al lavoro, la prima impressione conta molto?"],
    n5=["esempi per la seconda parte: <i>…e invece è solo concentrato · …e invece a Belo Horizonte fa freddo.</i>", "Lo studente corregge con <i>In realtà… · Non è vero per tutti · E invece…</i>"],
    hA=("Camila scrive sul suo blog: «Cinque mesi a Bologna». Scegli la forma giusta.",
        "<i>Quando sono arrivata a Bologna, a ottobre, pensavo che la città {0} piccola e tranquilla. Credevo che gli italiani {1} presto, e invece qui si cena alle nove! Avevo paura che le persone {2} fredde con gli stranieri, ma Giulia mi ha accolta come una figlia. Oggi penso che Bologna {3} la mia seconda casa e spero che i miei genitori {4} presto a trovarmi.</i>",
        [(["fosse", "sia"], "fosse"), (["cenassero", "cenano"], "cenassero"), (["fossero", "sono"], "fossero"), (["sia", "fosse"], "sia"), (["vengano", "venissero"], "vengano")]),
    hB=("Porta le frasi al passato.",
        [("Penso che Marco sia simpatico.", "Pensavo che Marco fosse simpatico."), ("Credo che gli italiani parlino con le mani.", "Credevo che gli italiani parlassero con le mani."),
         ("Credo di sapere la risposta.", "Credevo di sapere la risposta.")]),
    watch=[("Pensavo che sia timida.", "Pensavo che fosse timida.", "passato → congiuntivo imperfetto."),
           ("Credevo che io fossi in ritardo.", "Credevo di essere in ritardo.", "stesso soggetto → <i>di</i> + infinito."),
           ("Il film era molto chato.", "Il film era molto noioso.", "<i>chato</i> → <i>noioso, pesante</i>.")],
    write=("Prima e dopo: racconta un'idea che avevi su un paese, una città o una persona e com'è cambiata.",
           "Prima di…, pensavo che…", ["quattro <i>pensavo / credevo che</i> + congiuntivo imperfetto", "un <i>e invece</i>", "un presente finale (<i>oggi penso che</i>)"]),
    cando="So raccontare le prime impressioni e parlare di stereotipi senza generalizzare.",
    nH="Prossima unità: <i>Magari!</i> (vorrei che + congiuntivo imperfetto).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 12 - Credevo che")
