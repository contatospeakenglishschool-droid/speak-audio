# Speak! Progresso B1 - Unità 11 "Comunicare a distanza" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 11", audio_json=os.path.join(HERE, "audio_it-b1-unita-11.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-11", "11.1 Comunicare a distanza", "11.2 Ripeti")

C = dict(
    nn="11", title="Comunicare a distanza", subtitle="Videochiamate e vocali · <b>il congiuntivo imperfetto</b>",
    cover=[("SAI FARE", "gestire una videochiamata, dare notizie a distanza, fare paragoni irreali"),
           ("LINGUA", "Parlava come se fossimo sulla luna. · Mi sento come se avessi quindici anni."),
           ("PRONUNCIA", "la doppia s: «fossi», «avessi», «sentissimo»")],
    t1="vicini e lontani",
    start=["Con chi fai videochiamate? Quanto spesso?", "Preferisci i messaggi scritti o i vocali? Perché?",
           "Che cosa ti dà fastidio nelle chiamate con la famiglia?"],
    kw=[("una telefonata in cui ci si vede", "una videochiamata"), ("il collegamento a internet", "la connessione"),
        ("un messaggio registrato con la voce", "un vocale"), ("l'occhio del computer o del telefono", "la telecamera"),
        ("dal vivo, non attraverso uno schermo", "di persona"), ("parlare a voce molto alta", "urlare")],
    use_words=["Hai mai avuto una videochiamata disastrosa? Che cosa è successo?", "Chi vorresti vedere di persona presto?"],
    n1=["A: <i>un vocale</i> = <i>um áudio</i>; <i>la telecamera</i> = <i>a câmera</i> (la <i>camera</i> in italiano è la stanza!)."],
    aims=["Comunicare a distanza: la videochiamata con Belo Horizonte · Parliamone", "Il congiuntivo imperfetto · come se",
          "Chiamate a distanza (11.2) · gioco di ruolo: una videochiamata disastrosa", "Il messaggio di Bruno a Chiara · come se · scrittura (100–150 parole)"],
    story="Inizia il secondo blocco (marzo–maggio). Domenica 7 marzo, sera, a casa di Júlia. Júlia e Bruno hanno appena finito la videochiamata con i genitori a Belo Horizonte: la connessione andava e veniva, la mamma parlava «come se fossimo sulla luna» e urlava; il papà ha cercato la telecamera per dieci minuti e ha chiesto se a Bologna nevicasse ancora. Camila racconta i cinquanta vocali al giorno di sua madre. La grande notizia: ad aprile i genitori vengono a Bologna per due settimane; la mamma vuole vedere tutta l'Italia e dormire da Júlia. Novità di marzo: Tommaso vive con Bruno, Elena lavora al bar, Camila ha cominciato il tirocinio.",
    prob="La regola è uguale al portoghese (<i>como se fosse, como se tivesse</i>), quindi lo studente capisce subito; il problema è la forma: <i>avesse</i> (non <i>tivesse</i>), la doppia <i>s</i>, <i>stessi / dessi</i> (non <i>stassi</i>). Falsi amici del telefono: <i>atender</i> → <i>rispondere</i> (<i>attendere</i> = aspettare); <i>ligar</i> → <i>chiamare</i>; <i>câmera</i> → <i>telecamera</i>.",
    real="In Italia WhatsApp è l'app più usata e i vocali sono amatissimi… e odiatissimi. Tra Italia e Brasile ci sono 4 ore di differenza in inverno e 5 ore dall'ultima domenica di marzo, quando in Italia comincia l'ora legale (il Brasile non la usa più). Per chiamare l'Italia dal Brasile: +39.",
    tr=("Comunicare a distanza", "Ripeti: come se + congiuntivo imperfetto"),
    gist=("Domenica sera, a casa di Júlia, dopo una videochiamata. Ascolta. Di che cosa parlano soprattutto?",
          ["della chiamata con i genitori e della loro visita", "di un nuovo lavoro", "di una festa"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Durante la chiamata la connessione era perfetta.", "F"), ("La madre di Camila manda molti messaggi vocali.", "V"),
             ("Il padre non trovava la telecamera.", "V"), ("A Bologna nevica ancora.", "F"),
             ("I genitori arrivano ad aprile per due settimane.", "V"), ("La madre vuole dormire in albergo.", "F")]),
    talk2=["Perché Júlia si sente «come se avesse ancora quindici anni»?", "Camila dice: «Darei qualunque cosa perché mia madre venisse qui». Che cosa capiamo di lei?",
           "Le videochiamate avvicinano o allontanano le persone?"],
    n2=["B: 1 andava e veniva · 4 il padre lo chiedeva, ma non nevica più · 6 vuole dormire da Júlia.", "<i>andava e veniva</i> = <i>caía toda hora</i>; <i>È che…</i> = <i>É que…</i>."],
    gref="congiuntivo_imperfetto",
    t4="come se",
    pA=("Completa con come se + congiuntivo imperfetto.",
        [("Mio fratello mangia come se non (mangiare) ___ da giorni.", "mangiasse"), ("Mi parli come se io (essere) ___ un bambino.", "fossi"),
         ("Spende soldi come se (essere) ___ ricco.", "fosse"), ("Corrono come se (avere) ___ paura.", "avessero"),
         ("Parla di Roma come se ci (abitare) ___.", "abitasse")]),
    pB=[("Camila parla italiano come se ", ["fosse", "è"], "fosse", " italiana."),
        ("Mi guardi come se ", ["avessi", "ho"], "avessi", " detto una cosa strana."),
        ("<i>Stare</i> con <i>io</i> fa ", ["stessi", "stassi"], "stessi", ".")],
    rule="<b>Congiuntivo imperfetto</b>: <i>-are</i> → <b>-assi</b>, <i>-ere</i> → <b>-essi</b>, <i>-ire</i> → <b>-issi</b> (<i>parlassi, avessi, sentissi</i>). <i>Essere</i> → <b>fossi</b>; <i>fare, dire, bere</i> → <i>facessi, dicessi, bevessi</i>; <i>dare, stare</i> → <i>dessi, stessi</i>. <b>Come se</b> + congiuntivo imperfetto = un paragone con una situazione irreale.",
    use=["Come ti tratta tua madre (o tuo padre)? <i>Mi tratta come se…</i>", "Una persona che parla troppo forte: <i>Parla come se…</i>",
         "Il tuo capo o un collega: <i>Si comporta come se…</i>", "Come ti senti il lunedì mattina? <i>Mi sento come se…</i>",
         "Un amico spende troppo: <i>Spende come se…</i>"],
    n4="La radice è quella dell'imperfetto indicativo: <i>sentivo → sentissi, facevo → facessi</i>.",
    t5="chiamate a distanza",
    fl=(["cominciare", "problemi tecnici", "dare una notizia", "chiudere"],
        ["Mi senti? · Mi vedi? · Ci sei? · Pronto, chi parla?", "Ti sento a tratti. · Si è bloccato lo schermo. · Sei muto/a! · Ti richiamo.",
         "Indovina chi viene? · Ho una notizia… · Ti devo dire una cosa.", "Ci sentiamo domani. · Salutami tutti. · Ti mando un vocale."]),
    pron=("Il congiuntivo imperfetto ha sempre la <b>doppia s</b>: <i>fo<b>ss</b>i, ave<b>ss</b>i</i>, sorda e lunga. La <i>s</i> semplice tra due vocali, nel Nord Italia, è sonora: <i>ca<b>s</b>a</i> [z]. Non dire <i>fo[z]e</i>!",
          "Ascolta e ripeti. Poi leggi ad alta voce: casa · cassa · rosa · rossa · fosse · avesse."),
    task=("Gioco di ruolo. Un amico italiano ti chiama da lontano, ma la connessione è pessima. Devi dargli una notizia importante. Poi racconta come comunichi con le persone lontane (con chi, come, che cosa ti dà fastidio: usa <i>come se</i>).",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>chiedi se ti sente e ti vede</li><li>risolvi i problemi tecnici</li><li>dai la notizia e saluta</li></ul>",
          "Insegnante: Pronto? Mi senti? · Ti vedo tutto bloccato! · Non ti sento, sei muto/a! · Hai una notizia? Dimmi! · Come? Ripeti, per favore! · Ma parli come se fossi in una galleria… · Ti richiamo tra cinque minuti, va bene?"),
    talk5=["I messaggi vocali sono comodi o un po' maleducati?", "Una notizia importante: meglio una telefonata o un messaggio?"],
    n5=["coppie minime <i>casa / cassa, rosa / rossa</i>: la doppia è più lunga e sempre sorda.", "Interrompere spesso lo studente come se la connessione saltasse: deve ripetere e riformulare."],
    hA=("Domenica notte Bruno scrive a Chiara. Scegli la forma giusta.",
        "<b>Bruno:</b> Ciao amore! Videochiamata con i miei appena finita. La mamma mi guardava come se {0} dimagrito dieci chili. Papà parlava a voce altissima, come se {1} su un altro pianeta. La mamma vuole vedere tutto, come se {2} un mese di vacanza. Ti tratteranno come se {3} già della famiglia. Ti chiamo domani, se la connessione {4}!",
        [(["fossi", "sono"], "fossi"), (["abitassimo", "abitiamo"], "abitassimo"), (["avessimo", "abbiamo"], "avessimo"), (["fossi", "sei"], "fossi"), (["regge", "reggesse"], "regge")]),
    hB=("Riscrivi con come se.",
        [("Ci saluta, ma sembra che non ci conosca.", "Ci saluta come se non ci conoscesse."), ("Parla come una persona stanca, ma non lo è.", "Parla come se fosse stanca."),
         ("Mi sento giovane, come a quindici anni.", "Mi sento come se avessi quindici anni.")]),
    watch=[("Non ho atteso il telefono.", "Non ho risposto al telefono.", "<i>attendere</i> = aspettare."),
           ("Mia madre mi ha ligato.", "Mia madre mi ha chiamato.", "<i>ligar</i> → <i>chiamare</i>."),
           ("Parla come se è stanca.", "Parla come se fosse stanca.", "<i>come se</i> + congiuntivo.")],
    write=("Una mail a chi è lontano: dagli una notizia, racconta una chiamata e fagli una domanda.",
           "Ciao…, come stai? Ti scrivo per darti una notizia: …", ["tre <i>come se</i> + congiuntivo imperfetto", "una notizia", "una domanda o una richiesta"]),
    cando="So gestire una chiamata a distanza e fare paragoni con come se.",
    nH="Prossima unità: <i>Credevo che…</i> (pensavo che + congiuntivo imperfetto).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 11 - Comunicare a distanza")
