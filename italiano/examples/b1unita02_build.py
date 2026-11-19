# Speak! Progresso B1 - Unità 02 "Me lo dai?" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 02", audio_json=os.path.join(HERE, "audio_it-b1-unita-02.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-02", "02.1 Me lo dai?", "02.2 Ripeti")

C = dict(
    nn="02", title="Me lo dai?", subtitle="Favori tra amici · <b>i pronomi combinati</b>",
    cover=[("SAI FARE", "chiedere, accettare e rifiutare un favore senza ripetere i nomi"),
           ("LINGUA", "Me la presti? · Te lo tengo io. · Portaglielo tu. · Ce ne dai un po'?"),
           ("PRONUNCIA", "l'accento non si sposta: TRATtamela")],
    t1="un favore",
    start=["Quando parti, a chi lasci le chiavi di casa? Perché?", "Qual è l'ultimo favore che hai chiesto? E l'ultimo che hai fatto?",
           "Che cosa presti facilmente? Che cosa non presti mai?"],
    kw=[("dare una cosa che poi torna indietro", "prestare"), ("dare l'acqua alle piante", "annaffiare"),
        ("dare indietro una cosa a chi la possiede", "restituire"), ("andare a prendere un pacco o la posta", "ritirare"),
        ("la ruota della bici senza aria", "una gomma a terra"), ("andare con qualcuno in un posto", "accompagnare")],
    use_words=["Ti hanno mai restituito una cosa rotta? Che cosa hai detto?", "Chi ti accompagna all'aeroporto quando parti?"],
    n1=["A: <i>prestare</i> = <i>emprestar</i> (dare); <i>chiedere in prestito</i> = <i>pedir emprestado</i>; <i>restituire</i> = <i>devolver</i>."],
    aims=["Me lo dai? Júlia parte per Milano e tutti chiedono qualcosa · Parliamone", "I pronomi combinati", "Chiedere e rifiutare un favore (02.2) · gioco di ruolo: il vicino che parte",
          "I messaggi di Júlia e Davide · rispondere con i pronomi · scrittura (100–150 parole)"],
    story="Giovedì 14 gennaio, sera. Júlia parte la mattina dopo per Milano con Marco: tre giorni di lavoro da un cliente. A casa sua ci sono Davide, Bruno e Camila, e ognuno ha un favore da chiedere o da fare. Davide le annaffia le piante, tiene le chiavi e ritirerà un pacco di libri; porterà alla signora Rossi il libro di ricette brasiliane promesso a Natale. Bruno si fa prestare la bici (l'ultima volta l'aveva riportata con una gomma a terra). Camila chiede il vestito nero lungo per la cena di sabato con Pietro. Júlia regala ai ragazzi il caffè portato da Camila da Recife. Bruno promette di accompagnarla alla stazione… finché scopre che il treno è alle 6:40.",
    prob="In portoghese parlato l'oggetto si omette (<i>Me empresta? — Empresto.</i>) o si usa il pronome tonico (<i>dou pra ele</i>): lo studente dice <i>mi presti?</i>, <i>do a lui</i> ed evita i pronomi combinati. Inoltre scrive <i>gli lo</i> separato, dimentica il raddoppio in <i>dammelo</i> e accorda il participio con l'indiretto.",
    real="In molti condomini italiani è normale lasciare una copia delle chiavi a un vicino di fiducia. Chi riceve un favore di solito ricambia con un piccolo regalo e dice <i>Ti devo un favore!</i>. Da Bologna a Milano in Frecciarossa ci vuole circa un'ora: molti professionisti fanno avanti e indietro in giornata.",
    tr=("Me lo dai?", "Ripeti: l'accento con i pronomi"),
    gist=("Giovedì sera, a casa di Júlia. Ascolta. Di che cosa parlano soprattutto?",
          ["dei favori da fare mentre Júlia è a Milano", "di un viaggio a Recife", "di un esame di Davide"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Davide deve annaffiare le piante ogni giorno.", "F"), ("Júlia aspetta un pacco con dei libri.", "V"),
             ("Bruno vuole la bici perché l'autobus è sempre pieno.", "V"), ("Camila prende le chiavi da Júlia sabato.", "F"),
             ("Júlia aveva promesso il libro alla signora Rossi.", "V"), ("Bruno accompagna volentieri Júlia alla stazione.", "F")]),
    talk2=["Júlia dice a Bruno: «Trattamela bene!». Perché?", "Alla fine Bruno dice: «Forse è meglio se te la porta Davide». Che cosa vuol dire davvero?",
           "Tu a chi lasceresti le chiavi di casa: a Davide, a Bruno o a Camila?"],
    n2=["B: 1 basta una volta, sabato · 4 le prende da Davide · 6 scopre che il treno è alle 6:40.", "Parliamone 1: l'ultima volta Bruno gliel'aveva riportata con una gomma a terra."],
    gref="pronomi_combinati_b1",
    t4="i pronomi combinati",
    pA=("Rispondi con i pronomi combinati.",
        [("Mi presti la penna? — Sì, ___ presto.", "te la"), ("Hai dato le chiavi a Davide? — Sì, ___ ho date.", "gliele"),
         ("Ci porti il dolce stasera? — Sì, ___ porto.", "ve lo"), ("Mi dai due biglietti? — Sì, ___ do due.", "te ne"),
         ("Hai restituito la bici a Júlia? — No, non ___ ho ancora restituita.", "gliel'")]),
    pB=[("Il libro? Davide ", ["gliel'ha portato", "gli l'ha portato"], "gliel'ha portato", " stamattina."),
        ("Ti piace il mio vestito? ", ["Te lo presto!", "Ti lo presto!"], "Te lo presto!", ""),
        ("Le foto della festa? ", ["Mandamele", "Mandami le"], "Mandamele", " stasera!")],
    rule="<b>indiretto + diretto</b> (o <b>ne</b>): <i>mi, ti, ci, vi</i> → <b>me, te, ce, ve</b> + <i>lo, la, li, le, ne</i>; <i>gli, le, Le</i> → <b>glielo, gliela, glieli, gliele, gliene</b>. Prima del verbo; <b>dopo e attaccati</b> all'infinito e all'imperativo (<i>portaglielo, dammelo</i>). Al passato: <i>gliel<b>e</b> ho dat<b>e</b></i>.",
    use=["Chi ti presta la macchina? <i>Me la presta…</i>", "A chi racconti i tuoi segreti? <i>Li racconto a… / Glieli racconto…</i>",
         "Il tuo amico vuole il tuo libro preferito. Rispondi. <i>Te lo…</i>", "Chi ti ha regalato l'ultimo regalo? <i>Me l'ha regalato…</i>",
         "Dai un ordine con l'imperativo: le chiavi, a me. <i>Dammele!</i>"],
    n4="B3: imperativo con <i>tu</i> → pronomi attaccati.",
    t5="favori e risposte",
    fl=(["chiedere", "accettare", "rifiutare con gentilezza", "ringraziare"],
        ["Ti posso chiedere un favore? · Mi faresti un favore? · Me lo presti?", "Certo! · Figurati! · Ci penso io. · Te lo do volentieri.",
         "Mi dispiace, ma… · Questa volta non posso. · Non è che non voglio, è che…", "Grazie, sei un tesoro! · Ti devo un favore."]),
    pron=("Quando attacchiamo i pronomi, l'accento <b>non si sposta</b>: <i><b>TRAT</b>ta → <b>TRAT</b>tamela · <b>POR</b>ta → <b>POR</b>taglielo</i>. Il suono <b>gl</b> è come <i>lh</i> in <i>filho</i>: <i>glielo, gliele</i>.",
          "Ascolta e ripeti. Poi chiedi tre oggetti all'insegnante, che ti risponde con i pronomi."),
    task=("Gioco di ruolo. L'insegnante è un vicino che parte per un mese e ti chiede molti favori. Accettane alcuni e rifiutane uno con gentilezza. Usa i pronomi! Poi scambiatevi i ruoli.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>le piante</li><li>il gatto</li><li>la posta</li><li>la valigia</li><li>la macchina</li><li>il numero di telefono</li></ul>",
          "Insegnante: Mi annaffi le piante? · Mi tieni il gatto? · Mi ritiri la posta? · Me la porti al quarto piano? (la valigia) · Mi presti la tua macchina? · Mi dai il tuo numero? Lo studente risponde: Te le annaffio io · Mi dispiace, ma non te la posso prestare…"),
    talk5=["Presti soldi agli amici? Perché sì o perché no?", "È facile per te dire di no a un favore?"],
    n5=["battere il ritmo sul tavolo: la sillaba forte è la stessa del verbo da solo.", "Insistere perché lo studente non ripeta i nomi degli oggetti; il rifiuto deve avere un motivo."],
    hA=("Sabato Júlia scrive a Davide da Milano. Scegli la forma giusta.",
        "<b>Júlia:</b> Ciao Davide! Il pacco è arrivato? Se sì, {0} fino a domenica? E il libro di ricette: {1} alla signora Rossi? Camila passa da te oggi: se ti chiede il caricabatterie, è sul comodino, {2} pure. Il caffè di Camila: {3} un altro pacchetto voi, se volete! E le piante? Mi raccomando, {4} sabato!",
        [(["me lo tieni", "me la tieni"], "me lo tieni"), (["gliel'hai portato", "gli l'hai portato"], "gliel'hai portato"), (["daglielo", "dalle lo"], "daglielo"),
         (["prendetene", "prendetelo"], "prendetene"), (["annaffiale", "annaffiale le"], "annaffiale")]),
    hB=("Rispondi con i pronomi combinati.",
        [("Puoi spiegare la regola a Camila?", "Sì, posso spiegargliela. / Gliela posso spiegare."), ("Mi hai comprato il pane?", "Sì, te l'ho comprato."),
         ("Ci mandi le foto?", "Sì, ve le mando.")]),
    watch=[("Ho prestato la bici da Júlia.", "Júlia mi ha prestato la bici.", "<i>prestare</i> = solo dare."),
           ("Quando mi ritorni la bici?", "Quando me la restituisci?", "<i>ritornare</i> = <i>voltar</i>."),
           ("Mi presti? — Sì, presto.", "Me la presti? — Sì, te la presto.", "il pronome diretto non si omette.")],
    write=("Istruzioni per un amico: parti per una settimana e un amico ti tiene la casa. Che cosa deve fare, dove trova le cose, come lo ringrazi.",
           "Caro/a…, grazie ancora! Ti lascio qualche istruzione.", ["cinque pronomi combinati", "due imperativi con i pronomi attaccati", "un'espressione per ringraziare"]),
    cando="So chiedere, accettare e rifiutare un favore con i pronomi combinati.",
    nH="Prossima unità: <i>Avrei dovuto…</i> (il condizionale passato).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 02 - Me lo dai?")
