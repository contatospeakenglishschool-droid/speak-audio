# Speak! Progresso B1 - Unità 09 "Modi di dire" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 09", audio_json=os.path.join(HERE, "audio_it-b1-unita-09.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-09", "09.1 Modi di dire", "09.2 Ripeti")

C = dict(
    nn="09", title="Modi di dire", subtitle="Carnevale, gesti e modi di dire · <b>da + infinito</b>",
    cover=[("SAI FARE", "capire e spiegare modi di dire, fare gli auguri, capire i gesti"),
           ("LINGUA", "Vuoi qualcosa da bere? · Non c'è niente da fare. · In bocca al lupo!"),
           ("PRONUNCIA", "«da» e «dà»: preposizione e verbo")],
    t1="il Carnevale",
    start=["Ti piace il Carnevale? Come lo passi di solito?", "Conosci già qualche modo di dire italiano?",
           "Quale modo di dire brasiliano è impossibile da tradurre?"],
    kw=[("dolci fritti con lo zucchero, tipici del Carnevale bolognese", "le sfrappole"), ("un oggetto che copre il viso", "una maschera"),
        ("una frase che non vuol dire quello che dicono le parole", "un modo di dire"), ("un movimento delle mani che comunica", "un gesto"),
        ("un periodo di lavoro per imparare una professione", "un tirocinio"), ("smettere di provare, accettare di aver perso", "arrendersi")],
    use_words=["Che gesti usi quando parli? Mostrane uno.", "Hai mai fatto un tirocinio? Dove?"],
    n1=["A: <i>sfrappole</i>: il nome bolognese; altrove <i>chiacchiere, frappe, crostoli</i>. <i>Tirocinio</i> = <i>estágio</i>."],
    aims=["Modi di dire: martedì grasso al bar di Giulia · Parliamone", "Da + infinito · da o per? · da o di?",
          "Fare gli auguri e spiegare (09.2) · il gioco dei gesti", "Il messaggio di Camila da Venezia · da + infinito · scrittura (100–150 parole)"],
    story="Martedì 9 febbraio, martedì grasso. Giulia ha fatto un vassoio di sfrappole; Camila arriva con una maschera da gatto e «una fame da lupi». Domani ha il colloquio per il tirocinio: Giulia le dice «In bocca al lupo» e Davide le insegna a rispondere «Crepi!». Júlia ha preso un granchio: ha comprato due biglietti del treno per il carnevale di Venezia per sabato prossimo, ma il carnevale finisce oggi; i biglietti sono costati un occhio della testa e non si possono cambiare. Giulia e Davide mostrano due gesti. Júlia va a Venezia lo stesso con Camila: «due piccioni con una fava».",
    prob="Il portoghese dice <i>algo para beber, nada para fazer</i>: lo studente traduce <i>qualcosa per bere, niente a fare</i>; in italiano serve <i>da</i>. I modi di dire non si traducono parola per parola: <i>matar dois coelhos com uma cajadada</i> → <i>prendere due piccioni con una fava</i>; <i>custar os olhos da cara</i> → <i>costare un occhio della testa</i>. A <i>in bocca al lupo</i> non si risponde <i>grazie</i>.",
    real="Il Carnevale finisce il martedì grasso; il giorno dopo comincia la Quaresima. Eccezione: a Milano il Carnevale ambrosiano finisce il sabato successivo. Vicino a Bologna è famoso il Carnevale di Cento. A Venezia, nei <i>bacari</i>, si mangiano i <i>cicchetti</i> con un bicchiere di vino.",
    tr=("Modi di dire", "Ripeti: da + infinito"),
    gist=("Martedì grasso, al bar di Giulia. Ascolta. Di che cosa parlano soprattutto?",
          ["di dolci, modi di dire, gesti e di un viaggio a Venezia", "di una partita di calcio", "di un nuovo lavoro per Giulia"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Le sfrappole sono dolci bolognesi di Carnevale.", "V"), ("Domani Camila ha un esame all'università.", "F"),
             ("A «In bocca al lupo» si risponde «Grazie».", "F"), ("Júlia ha comprato i biglietti per il giorno sbagliato.", "V"),
             ("I biglietti del treno si possono cambiare.", "F"), ("Sabato Camila va a Venezia con Júlia.", "V")]),
    talk2=["Perché Camila chiede «Quanti lupi ci sono in Italia?»", "Perché, secondo te, i modi di dire sono così difficili per uno straniero?",
           "Il Carnevale è una festa da bambini o da adulti?"],
    n2=["B: 2 un colloquio per il tirocinio · 3 si risponde «Crepi!» · 5 non si possono cambiare.", "<i>anzi</i> = <i>aliás, ou melhor</i>; <i>lo stesso</i> = <i>mesmo assim</i>."],
    gref="da_infinito",
    t4="da + infinito",
    pA=("Completa con da + infinito. Verbi: bere, fare, lavare, leggere, non perdere.",
        [("Hai qualcosa ___? Ho sete.", "da bere"), ("Questo film è ___: è bellissimo.", "da non perdere"),
         ("In cucina ci sono ancora i piatti ___.", "da lavare"), ("Domenica non ho niente ___.", "da fare"),
         ("Mi presti un libro ___ in vacanza?", "da leggere")]),
    pB=[("Hai qualcosa ", ["da", "per"], "da", " leggere in treno?"),
        ("Sono passata ", ["per", "da"], "per", " salutarti."),
        ("Ho comprato degli occhiali ", ["da", "di"], "da", " sole.")],
    rule="<b>da + infinito</b> = una cosa che si deve o si può fare: <i>qualcosa da bere, niente da fare, una città da vedere, le sfrappole sono da provare</i>. <b>da + nome</b> = uso o tipo: <i>una maschera da gatto, occhiali da sole</i>. Per lo scopo di chi agisce: <b>per</b> + infinito.",
    use=["Una città brasiliana da vedere almeno una volta: perché?", "Un libro o una serie da non perdere.", "Che cosa hai da fare questo fine settimana?",
         "Un piatto da provare nella tua regione.", "Che cosa c'è da vedere nel tuo quartiere?"],
    n4="Pratica B2: lo scopo di chi agisce (io passo per salutarti) → <i>per</i>.",
    t5="modi di dire e gesti",
    fl=(["chiedere il significato", "spiegare", "fare gli auguri", "reagire"],
        ["Che cosa vuol dire…? · In che senso? · Si usa spesso?", "Vuol dire che… · Si dice quando… · Letteralmente…",
         "In bocca al lupo! — Crepi! · Incrociamo le dita! · Buon divertimento!", "Che sfortuna! · Che figuraccia! · Mi arrendo!"]),
    pron=("La preposizione <b>da</b> non ha accento e si lega alla parola successiva: <i>qualcosa da <b>be</b>re</i>. Il verbo <b>dà</b> (<i>lui dà</i>) ha l'accento e si sente: <i>Giulia <b>dà</b> una sfrappola a Camila</i>.",
          "Ascolta e ripeti. Poi l'insegnante dice una frase con «da» o con «dà»: tu dici quale hai sentito."),
    task=("Il gioco dei gesti e dei modi di dire. L'insegnante fa un gesto italiano: tu indovini il significato. Poi tu spieghi in italiano tre modi di dire brasiliani: che cosa vogliono dire letteralmente, che cosa significano davvero, quando si usano.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>in bocca al lupo · prendere un granchio</li><li>costare un occhio della testa</li><li>avere le mani bucate · non vedere l'ora</li></ul>",
          "Insegnante: 1 punte delle dita unite, mano su e giù = Ma che cosa dici? · 2 indice sulla guancia che gira = Buonissimo! · 3 pollice verso la bocca = Beviamo qualcosa? · 4 dorso della mano sotto il mento, verso fuori = Non me ne importa niente."),
    talk5=["I gesti sono utili o un po' maleducati?", "Quale modo di dire italiano ti piace di più? Perché?"],
    n5=["frasi per il gioco: <i>Giulia dà le sfrappole · le sfrappole da provare · Chi mi dà una mano? · niente da fare.</i>", "Fare il gesto senza parlare; dire la frase solo dopo il tentativo dello studente. Idee: <i>pagar mico, chutar o balde, cair a ficha</i>."],
    hA=("Sabato Camila scrive a Pietro da Venezia. Scegli la forma giusta.",
        "<b>Camila:</b> Ciao Pietro! Sono a Venezia con Júlia. È davvero una città {0} vedere almeno una volta nella vita. Júlia ha preso un granchio con le date, ma alla fine abbiamo preso due piccioni con una {1}. Il caffè in piazza San Marco però è costato un occhio della {2}! Ho comprato una maschera {3} gatto e adesso cerchiamo qualcosa {4} mangiare.",
        [(["da", "per"], "da"), (["fava", "pietra"], "fava"), (["testa", "faccia"], "testa"), (["da", "di"], "da"), (["da", "per"], "da")]),
    hB=("Riscrivi con da + infinito.",
        [("Roma è una città che si deve vedere.", "Roma è una città da vedere."), ("Non c'è niente che possiamo fare.", "Non c'è niente da fare."),
         ("Ho tanti libri che devo leggere.", "Ho tanti libri da leggere.")]),
    watch=[("In bocca al lupo! — Grazie!", "In bocca al lupo! — Crepi!", "«grazie» porta sfortuna!"),
           ("Costa gli occhi della faccia.", "Costa un occhio della testa.", "i modi di dire non si traducono."),
           ("Vuoi qualcosa per bere?", "Vuoi qualcosa da bere?", "<i>qualcosa</i> + <i>da</i> + infinito.")],
    write=("Un post per un blog di lingue: spiega tre modi di dire (italiani o brasiliani) a chi impara la lingua.",
           "Ogni giorno scopro un modo di dire da imparare. …", ["tre modi di dire spiegati", "tre <i>da</i> + infinito", "un esempio di situazione", "un consiglio finale"]),
    cando="So spiegare un modo di dire, fare gli auguri e usare da + infinito.",
    nH="La prossima lezione è il <b>Ripasso 1</b> (unità 01–09).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 09 - Modi di dire")
