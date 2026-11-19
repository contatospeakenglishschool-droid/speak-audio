# Speak! Progresso B1 - Unità 07 "Cerco qualcuno che…" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 07", audio_json=os.path.join(HERE, "audio_it-b1-unita-07.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-07", "07.1 Cerco qualcuno che...", "07.2 Ripeti")

C = dict(
    nn="07", title="Cerco qualcuno che…", subtitle="Annunci · <b>il congiuntivo nelle relative</b>",
    cover=[("SAI FARE", "capire e scrivere un annuncio, descrivere la persona ideale, fare un colloquio"),
           ("LINGUA", "Cerco qualcuno che abbia esperienza. · Conosco una ragazza che cerca lavoro."),
           ("PRONUNCIA", "c dura e c dolce: «cerco», «cerchi», «conosci»")],
    t1="annunci",
    start=["Hai mai risposto a un annuncio di lavoro o di casa? Com'è andata?", "Hai mai avuto un coinquilino? Com'era?",
           "Che cosa non sopporti in una persona con cui vivi o lavori?"],
    kw=[("un testo per cercare o offrire qualcosa", "un annuncio"), ("una persona che vive nella stessa casa", "un coinquilino"),
        ("quello che sai fare perché l'hai già fatto", "l'esperienza"), ("che arriva sempre all'ora giusta", "puntuale"),
        ("le ore di lavoro di una persona: mattina, sera…", "un turno"), ("l'incontro per un posto di lavoro", "un colloquio")],
    use_words=["Sei una persona puntuale?", "Com'è andato il tuo ultimo colloquio di lavoro?"],
    n1=["A: <i>coinquilino</i> = <i>colega de apartamento</i>; <i>colloquio</i> = <i>entrevista de emprego</i> (l'<i>intervista</i> è dei giornalisti)."],
    aims=["Cerco qualcuno che… Due annunci al bar di Giulia · Parliamone", "Il congiuntivo nelle relative e la lingua degli annunci",
          "Annunci e colloqui (07.2) · gioco di ruolo: colloquio al bar di Giulia", "L'annuncio di Bruno · la mia persona ideale · scrittura (100–150 parole)"],
    story="Martedì 2 febbraio, mattina. Sulla porta del bar c'è il cartello «Cercasi barista»: da marzo Giulia apre anche la sera con l'aperitivo. Júlia e Bruno l'aiutano a scrivere l'annuncio: qualcuno che abbia esperienza, che sappia fare un cappuccino come si deve, che parli un po' d'inglese e soprattutto che sia puntuale. Davide conosce Elena, una compagna di ingegneria che d'estate ha fatto la barista a Rimini. Anche Bruno scrive un annuncio: a marzo Paolo parte per l'Erasmus e lui cerca un coinquilino che non fumi, non faccia feste e lavi i piatti. Giulia: «Tu cerchi un coinquilino che ti faccia il caffè, io un barista: siamo uguali!»",
    prob="Il portoghese ha la stessa regola (<i>procuro alguém que tenha</i>), ma nel parlato spesso si usa l'indicativo (<i>que tem</i>): lo studente dice <i>cerco qualcuno che ha</i>. Errore opposto per ipercorrezione: <i>conosco una ragazza che cerchi</i>. Falsi amici: <i>entrevista</i> → <i>colloquio</i>; <i>esperto</i> (sveglio) ≠ <i>esperto</i> (che sa molto di una cosa).",
    real="L'Università di Bologna è una delle università europee con più studenti Erasmus. Molti giovani lavorano con contratti a tempo determinato o part-time nei bar e nei ristoranti. Nei negozi italiani si vedono ancora spesso i cartelli <i>Cercasi personale</i>. L'aperitivo serale è un momento importante per i bar di Bologna.",
    tr=("Cerco qualcuno che…", "Ripeti: il congiuntivo nelle relative"),
    gist=("Martedì mattina, al bar di Giulia. Ascolta. Di che cosa parlano soprattutto?",
          ["di due annunci: un barista per il bar e un coinquilino per Bruno", "di un nuovo lavoro per Júlia", "di una festa a casa di Bruno"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Giulia cerca un barista perché da marzo apre anche la sera.", "V"), ("Per Giulia la cosa più importante è che il barista sia simpatico.", "F"),
             ("L'ultimo barista arrivava sempre in ritardo.", "V"), ("Elena ha già lavorato come barista.", "V"),
             ("Bruno cerca un coinquilino perché Paolo va a vivere con la ragazza.", "F"), ("Paolo lavava sempre i piatti.", "F")]),
    talk2=["Perché Júlia consiglia a Bruno di scrivere «una persona tranquilla e ordinata»?", "Giulia dice: «Siamo uguali!». Perché?",
           "È meglio vivere da soli o con dei coinquilini?"],
    n2=["B: 2 che sia puntuale · 5 Paolo parte per l'Erasmus · 6 non li ha mai lavati.", "<i>come si deve</i> = <i>direito</i>; <i>già che ci siamo</i> = <i>já que estamos aqui</i>."],
    gref="congiuntivo_relative",
    t4="il congiuntivo nelle relative",
    pA=("Completa con il verbo tra parentesi: indicativo o congiuntivo?",
        [("Cerco una persona che (sapere) ___ cucinare.", "sappia"), ("Conosco una ragazza che (parlare) ___ cinque lingue.", "parla"),
         ("Non c'è nessuno che (lavare) ___ i piatti volentieri.", "lavi"), ("Vorrei una casa che (avere) ___ un balcone.", "abbia"),
         ("Abbiamo una stagista che (essere) ___ bravissima.", "è")]),
    pB=[("Non ho trovato nessuna stanza che ", ["costi", "costa"], "costi", " meno di 400 euro."),
        ("Conosci qualcuno che ", ["sappia", "sa"], "sappia", " riparare una bici?"),
        ("<i>Cercasi barista</i> vuol dire ", ["si cerca un barista", "un barista cerca lavoro"], "si cerca un barista", ".")],
    rule="Dopo <i>che</i> relativo: <b>indicativo</b> per una persona o una cosa <b>reale</b> (<i>conosco una ragazza che <b>cerca</b> lavoro</i>); <b>congiuntivo</b> per una persona o una cosa <b>ideale</b> o che forse non esiste (<i>cerco qualcuno che <b>abbia</b> esperienza · non c'è nessuno che <b>lavi</b> i piatti</i>). Negli annunci: <i>cercasi, affittasi, vendesi</i>.",
    use=["Descrivi il tuo lavoro ideale: <i>Cerco un lavoro che…</i>", "Il capo ideale: <i>Vorrei un capo che…</i>", "Nella tua famiglia: <i>Non c'è nessuno che…</i>",
         "Una persona speciale che conosci: <i>Conosco una persona che…</i> (attenzione: indicativo!)", "La casa ideale: <i>Mi serve una casa che…</i>"],
    n4="Per ogni frase chiedere: <i>questa persona esiste? la conosci?</i> Se sì → indicativo.",
    t5="annunci e colloqui",
    fl=(["dire che cosa cerchi", "i requisiti", "chiedere informazioni", "presentarsi"],
        ["Cerco qualcuno che… · Ho bisogno di una persona che… · L'ideale sarebbe…", "È richiesta esperienza. · È importante che… · È gradito/a…",
         "Quali sono gli orari? · Com'è lo stipendio? · È a tempo determinato?", "Ho visto il Suo annuncio. · Ho esperienza come… · Sono disponibile da…"]),
    pron=("<b>c</b> + <i>a, o, u</i> e <b>ch</b> + <i>e, i</i> = [k]: <i>cerco, cerchi</i>. <b>c</b> + <i>e, i</i> = [tʃ]: <i>cercasi</i>. <b>sc</b> + <i>e, i</i> = [ʃ]: <i>conosci</i>, ma <i>conosco</i> = [sk].",
          "Ascolta e ripeti. Poi leggi ad alta voce: cerco · cerchi · cercasi · conosco · conosci · cuochi · amici."),
    task=("Gioco di ruolo. Hai letto l'annuncio di Giulia e fai il colloquio per il posto di barista; l'insegnante è Giulia. Poi scambiatevi i ruoli: tu sei Giulia e descrivi la persona che cerchi.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>esperienza e lingue</li><li>orari e disponibilità</li><li>domande sullo stipendio e sul contratto</li></ul>",
          "Insegnante (Giulia): Buongiorno, si accomodi. · Ha esperienza come barista? · Cerco qualcuno che possa lavorare il sabato sera: Lei può? · Parla inglese? · Come si prepara un buon cappuccino? · Ha domande per me? · Bene, Le faccio sapere entro venerdì."),
    talk5=["In un colloquio conta di più l'esperienza o la personalità?", "Esiste il lavoro perfetto, secondo te?"],
    n5=["errore tipico: <i>conosci</i> letto [konoski]; al plurale <i>cuoco → cuochi</i>, ma <i>amico → amici</i>.", "Registro formale (<i>Lei</i>)."],
    hA=("Leggi l'annuncio di Bruno e scegli la forma giusta.",
        "<b>AFFITTASI STANZA SINGOLA – via Zamboni.</b> Da marzo, in un appartamento per due persone. Cerco un coinquilino o una coinquilina che {0} all'Unibo, che non {1} e che {2} tranquillo/a e ordinato/a. Io mi chiamo Bruno, studio Storia e {3} a calcetto il martedì. Nel palazzo non c'è nessuno che {4} rumore la sera. 380 € al mese, spese incluse. Astenersi perditempo!",
        [(["studi", "studia"], "studi"), (["fumi", "fuma"], "fumi"), (["sia", "è"], "sia"), (["gioco", "giochi"], "gioco"), (["faccia", "fa"], "faccia")]),
    hB=("Riscrivi con le parole tra parentesi.",
        [("Mi serve un collega. Deve parlare inglese. (cerco qualcuno che)", "Cerco qualcuno che parli inglese."),
         ("Nessuno nel palazzo sa cucinare. (non c'è nessuno che)", "Non c'è nessuno nel palazzo che sappia cucinare."),
         ("Voglio una casa con un giardino. (vorrei una casa che)", "Vorrei una casa che abbia un giardino.")]),
    watch=[("Cerco qualcuno che ha esperienza.", "Cerco qualcuno che abbia esperienza.", "persona ideale → congiuntivo."),
           ("Domani ho un'intervista per il bar.", "Domani ho un colloquio per il bar.", "<i>intervista</i> = dei giornalisti."),
           ("Conosco una ragazza che cerchi lavoro.", "Conosco una ragazza che cerca lavoro.", "persona reale → indicativo.")],
    write=("Un annuncio: cerchi un collega, un coinquilino, un insegnante o un servizio.",
           "Cercasi… Cerchiamo una persona che…", ["quattro relative con il congiuntivo", "<i>cercasi, è gradito, si richiede</i>", "orari o prezzo", "come rispondere"]),
    cando="So capire e scrivere un annuncio e descrivere la persona che cerco.",
    nH="Prossima unità: <i>Mica male!</i> (la negazione rafforzata).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 07 - Cerco qualcuno che")
