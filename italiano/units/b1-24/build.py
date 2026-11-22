# Speak! Progresso B1 - Unità 24 "Dopo aver studiato" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 24", audio_json=os.path.join(HERE, "audio_it-b1-unita-24.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-24", "24.1 Dopo aver studiato", "24.2 Ripeti")

C = dict(
    nn="24", title="Dopo aver studiato", subtitle="Esami e scelte · <b>infinito passato: dopo aver…, prima di…, senza…</b>",
    cover=[("SAI FARE", "raccontare le tappe di un percorso, parlare di studio ed esami, prendere una decisione"),
           ("LINGUA", "Dopo aver studiato… · Dopo essere arrivato… · Prima di decidere… · Credo di aver capito…"),
           ("PRONUNCIA", "aver studiato, voler dire: la -e che cade")],
    t1="lo studio",
    start=["Guarda la foto. Come studia questa persona? E tu come studiavi?", "Ti ricordi un esame difficile? Com'è andato?",
           "Studi meglio da solo/a o con altre persone?"],
    kw=[("una prova all'università, spesso orale in Italia", "l'esame"), ("il numero che ricevi dopo un esame", "il voto"),
        ("la data in cui si può fare un esame", "l'appello"), ("studiare di nuovo una cosa già studiata", "ripassare"),
        ("dire di no, non accettare", "rifiutare"), ("il risultato medio di tutti i voti", "la media")],
    use_words=["Prima di un esame, ripassi tutto o solo le cose difficili?", "Hai mai rifiutato qualcosa (un voto, un lavoro, un invito)? Perché?"],
    n1=["A: in Italia i voti universitari vanno da 18 a 30 (e lode); <i>appello</i> = data d'esame, non <i>apelo</i>."],
    aims=["Dopo aver studiato: l'esame di Bruno · Parliamone", "L'infinito passato: dopo aver / essere…, prima di…, senza…",
          "Le tappe della mia vita (24.2) · la -e che cade", "Il messaggio di Bruno · unire le frasi · scrittura (100–150 parole)"],
    story="Giovedì 17 giugno, mezzogiorno, in via Zamboni davanti al dipartimento di Storia. Júlia e Chiara aspettano Bruno, che ha appena fatto l'ultimo esame della sessione: 24, dopo tre settimane di studio, perché il professore gli ha chiesto l'unico capitolo che non aveva ripassato. Il professore gli propone di rifiutare il voto e tornare al prossimo appello, il 12 luglio: ma è proprio il giorno in cui Bruno e Chiara partono per la Sicilia. Júlia si stupisce (in Brasile nessuno rifiuta un voto); Chiara l'ha fatto due volte. Bruno decide: non può finire l'anno senza aver visto la Sicilia, e accetta il 24. Dopo averlo accettato si sente leggerissimo; il pranzo lo paga «la sorella architetta».",
    prob="Il portoghese dice <i>depois de estudar</i> con l'infinito semplice: lo studente dice <i>dopo studiare</i> invece di <i>dopo aver studiato</i> (è l'errore principale dell'unità). Altri errori: l'ausiliare sbagliato (<i>dopo aver arrivato</i>), l'accordo con <i>essere</i> (Chiara: <i>dopo essere uscita</i>), <i>prima di che</i> (calco di <i>antes que</i>). Falsi amici: <i>appello</i> (data d'esame) e <i>la media</i> (dei voti).",
    real="All'università italiana i voti vanno da <b>18</b> (minimo) a <b>30</b>; il massimo è <b>30 e lode</b>. Molti esami sono <b>orali</b>, e lo studente può <b>rifiutare il voto</b> e ripresentarsi a un altro <b>appello</b> (ce ne sono diversi in ogni sessione: estiva, autunnale, invernale). Via Zamboni è la strada dell'Università di Bologna, la più antica d'Europa (1088).",
    tr=("Dopo aver studiato", "Ripeti: l'infinito passato"),
    gist=("Giovedì, davanti all'università. Ascolta. Che cosa deve decidere Bruno?",
          ["se accettare o rifiutare il voto", "se cambiare facoltà", "se andare in Sicilia con Júlia"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Bruno ha preso 24.", "V"), ("Il professore gli ha chiesto un capitolo che non aveva ripassato.", "V"),
             ("Il prossimo appello è il 21 luglio.", "F"), ("Chiara non ha mai rifiutato un voto.", "F"),
             ("Alla fine Bruno rifiuta il voto.", "F"), ("Il pranzo lo paga Júlia.", "V")]),
    talk2=["Tu avresti accettato il 24? Perché?", "Secondo te è giusto poter rifiutare un voto?",
           "Che cosa pensi degli esami orali?"],
    n2=["B: 3 il 12 luglio · 4 l'ha fatto due volte · 5 lo accetta.", "Bruno e Chiara partono per la Sicilia il 12 luglio (unità 26)."],
    gref="infinito_passato",
    t4="l'infinito passato",
    pA=("Completa con l'infinito passato o presente del verbo tra parentesi.",
        [("Dopo ___ (studiare) tre settimane, Bruno ha preso 24.", "aver studiato"), ("Prima di ___ (decidere), ci pensi bene.", "decidere"),
         ("Dopo ___ (arrivare) fin qui, non voglio studiare a luglio.", "essere arrivato"), ("Credo di ___ (capire) una cosa.", "aver capito"),
         ("Chiara, dopo ___ (uscire) dall'esame, ha chiamato sua madre.", "essere uscita")]),
    pAw="30mm",
    pB=[("", ["Dopo studiare", "Dopo aver studiato"], "Dopo aver studiato", ", Bruno è andato a pranzo."),
        ("È partito senza ", ["salutare", "di salutare"], "salutare", "."),
        ("", ["Dopo che", "Dopo"], "Dopo che", " il professore ha parlato, Bruno ha deciso.")],
    rule="<b>Dopo</b> + infinito <b>passato</b> (<i>aver</i> / <i>essere</i> + participio): <i>dopo aver studiato, dopo essere arrivata</i>. <b>Prima di</b> + infinito <b>presente</b>: <i>prima di decidere</i>. <b>Senza</b> + infinito. <b>Credo di</b> + infinito passato. Soggetti diversi: <b>dopo che</b> + indicativo.",
    use=["Che cosa fai di solito dopo esserti svegliato/a?", "Che cosa hai fatto ieri dopo aver finito di lavorare?",
         "Che cosa bisogna fare prima di partire per un lungo viaggio?", "Racconta una cosa che hai fatto senza pensarci.",
         "Completa: <i>Credo di aver fatto bene a…</i>"],
    n4="B3: soggetti diversi (il professore / Bruno) → <i>dopo che</i>.",
    t5="le tappe della mia vita",
    fl=(["l'ordine", "prima di…", "senza…", "il bilancio"],
        ["Dopo aver finito la scuola… · Dopo essermi trasferito/a… · Dopo che…", "Prima di cominciare a lavorare… · Prima di sposarmi…",
         "Senza pensarci troppo… · Senza aver mai visto…", "Credo di aver fatto bene a… · Mi sembra di aver imparato…"]),
    pron=("Nel parlato molte parole perdono la <b>-e</b> finale davanti a un'altra parola: <b>aver studiato</b>, <b>esser partiti</b>, <b>voler dire</b>, <b>poter fare</b>, <b>dottor Neri</b>. Si dice tutto insieme, in un solo respiro: <i>dopo-aver-studiato</i>.",
          "Ascolta e ripeti. Poi leggi: «Dopo aver mangiato, prima di partire, voglio poter dormire.»"),
    task=("Le tappe della mia vita. Racconta cinque tappe importanti della tua vita (studio, lavoro, casa, viaggi, famiglia) in ordine, usando dopo aver / dopo essere, prima di e senza. L'insegnante è un giornalista che ti intervista: alla fine fa' un bilancio (Credo di aver fatto bene a…).",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>finire la scuola</li><li>il primo lavoro</li><li>andare a vivere da solo/a</li><li>un viaggio importante</li><li>cominciare l'italiano</li><li>una decisione difficile</li></ul>",
          "Insegnante (giornalista): E dopo aver finito la scuola, che cosa ha fatto? · Prima di cominciare l'italiano, aveva studiato altre lingue? · L'ha fatto senza pensarci? · Rifarebbe tutto? Correggere subito <i>dopo finire</i> → <i>dopo aver finito</i>."),
    talk5=["Qual è stata la decisione più importante della tua vita?", "Hai mai fatto qualcosa senza pensarci e poi ti sei pentito/a?"],
    n5=["leggere le frasi due volte: prima lenta, poi veloce, senza la -e.", "Contare gli infiniti passati; ogni <i>dopo + infinito semplice</i> = correzione immediata."],
    hA=("Il messaggio di Bruno ai genitori. Scegli la forma giusta.",
        "<i>Ciao mamma, ciao papà! Ho finito gli esami! Dopo {0} studiato tre settimane, ho preso 24. Il professore mi ha detto di pensarci prima di {1}, perché potevo rifiutarlo. Ma dopo {2} arrivato fin qui, non volevo passare luglio sui libri: credo di {3} fatto la scelta giusta. E poi non potevo finire l'anno senza {4} la Sicilia! Un abbraccio!</i>",
        [(["aver", "avendo"], "aver"), (["decidere", "aver deciso"], "decidere"), (["essere", "avere"], "essere"),
         (["aver", "avere"], "aver"), (["vedere", "di vedere"], "vedere")]),
    hB=("Unisci le due frasi con dopo + infinito passato.",
        [("Bruno ha finito l'esame. Bruno è andato a pranzo.", "Dopo aver finito l'esame, Bruno è andato a pranzo."), ("Chiara è uscita dall'università. Chiara ha chiamato Bruno.", "Dopo essere uscita dall'università, Chiara ha chiamato Bruno."),
         ("Ho letto il libro. Ho capito tutto.", "Dopo aver letto il libro, ho capito tutto.")]),
    watch=[("Dopo studiare, sono uscito.", "Dopo aver studiato, sono uscito.", "<i>dopo</i> + infinito passato."),
           ("Dopo aver arrivato…", "Dopo essere arrivato…", "<i>arrivare</i> vuole <i>essere</i>."),
           ("Prima di che parti, chiamami.", "Prima di partire, chiamami.", "<i>prima di</i> + infinito.")],
    write=("Racconta un percorso: un esame, un trasloco, un viaggio o un cambiamento importante, dalla preparazione al risultato.",
           "Dopo aver deciso di…", ["tre infiniti passati (uno con <i>essere</i>)", "<i>prima di</i> e <i>senza</i>", "un bilancio finale (<i>credo di aver…</i>)"]),
    cando="So raccontare le tappe di un percorso e mettere in ordine le azioni con dopo aver…, prima di… e senza….",
    nH="Prossima unità: <i>Avrà già finito?</i> (il futuro anteriore).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 24 - Dopo aver studiato")
