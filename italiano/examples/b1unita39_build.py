# Speak! Progresso B1 - Unità 39 "Tre anni a Bologna" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 39", audio_json=os.path.join(HERE, "audio_it-b1-unita-39.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-39", "39.1 Tre anni a Bologna", "39.2 Ripeti")

C = dict(
    nn="39", title="Tre anni a Bologna", subtitle="L'aperitivo di saluto prima di Natale · <b>tutti i tempi del racconto</b>",
    cover=[("SAI FARE", "raccontare un periodo della tua vita: ricordi, bilancio e progetti"),
           ("LINGUA", "passato prossimo · imperfetto · trapassato · condizionale passato · periodo ipotetico · futuro"),
           ("PRONUNCIA", "raccontare con ritmo: le pause prima di <i>e allora, però, alla fine</i>")],
    t1="bilanci e ricordi",
    start=["Guarda la foto. Che cosa stanno festeggiando, secondo te?", "Dove abitavi tre anni fa? Che cosa facevi?",
           "Che cosa è cambiato di più nella tua vita negli ultimi tre anni?"],
    kw=[("un incontro tra amici per salutare chi parte", "l'aperitivo di saluto"), ("alzare il bicchiere e fare gli auguri", "il brindisi"),
        ("guardare indietro e valutare un periodo", "fare un bilancio"), ("un lavoro senza data di fine", "il contratto a tempo indeterminato"),
        ("la cadenza tipica di chi parla una lingua straniera", "l'accento"), ("sentirsi bene in un posto, come a casa", "ambientarsi")],
    use_words=["Quanto tempo ci hai messo ad ambientarti nel tuo lavoro o nella tua città?", "Quando hai fatto l'ultimo brindisi? Per che cosa?"],
    n1=["A: <i>il contratto a tempo indeterminato</i> = contrato efetivo, sem prazo (≠ <i>a tempo determinato</i>).", "Ultima lezione con una storia nuova del B1: dopo c'è il Ripasso 4."],
    aims=["Tre anni a Bologna: l'aperitivo al Bar Giulia · Parliamone", "tutti i tempi del racconto · se fossi… avrei…",
          "Il mio bilancio (39.2) · raccontare con ritmo", "Il blog di Júlia · riscrivi · scrittura (100–150 parole)"],
    story="Martedì 21 dicembre, sera, al Bar Giulia: aperitivo di saluto prima della partenza per il Brasile (Júlia e Bruno partono domani alle 6). Giulia, Davide e la signora Rossi ricordano i primi giorni di Júlia: pioveva, non conosceva nessuno e aveva ordinato un cappuccino alle sette di sera; Davide l'aveva vista sulle scale con tre valigie e lei gli aveva risposto in inglese. Novità: ieri Júlia ha consegnato il disegno della pergola e stamattina Galli ha telefonato: gli piace moltissimo, ma la vorrebbe un po' più alta (Marco la voleva più bassa!). Il capo le ha detto che da gennaio avrà il contratto a tempo indeterminato. «Tre anni fa avrei detto di no: adesso Bologna è casa mia.» Progetti: i genitori in primavera, la terrazza di Galli finita per l'estate, un italiano «senza accento».",
    prob="Nel racconto il brasiliano usa un solo passato. In italiano: <i>passato prossimo</i> per i fatti (<i>sono arrivata</i>), <i>imperfetto</i> per la scena (<i>pioveva, non conoscevo nessuno</i>), <i>trapassato</i> per il fatto prima del fatto (<i>avevo ordinato</i>), dove il portoghese usa spesso il perfeito. Nel periodo ipotetico: <s>se avrei saputo</s> → <i>se avessi saputo</i> (como «se eu tivesse sabido»). E la durata: <i>abito qui <b>da</b> tre anni</i> (presente!), mai <s>ho abitato qui da tre anni</s>; <i>tre anni <b>fa</b></i> = há três anos.",
    real="In Italia molti lavoratori dipendenti ricevono a dicembre la <b>tredicesima</b>, una mensilità in più (come il <i>13º salário</i> in Brasile). Il <b>contratto a tempo indeterminato</b> è il contratto senza data di fine; il <b>contratto a tempo determinato</b> ha una scadenza. Prima delle feste colleghi e amici si salutano spesso con un <b>aperitivo</b> e gli auguri: <i>Buon Natale e buone feste!</i>",
    tr=("Tre anni a Bologna", "Ripeti: il racconto"),
    gist=("Martedì sera, al Bar Giulia. Ascolta. Perché gli amici di Júlia si incontrano?",
          ["per salutarla prima del viaggio in Brasile", "per festeggiare il compleanno di Júlia", "per festeggiare la fine del progetto di Galli"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il primo giorno Júlia aveva ordinato un cappuccino la sera.", "V"), ("Davide l'aveva conosciuta all'aeroporto.", "F"),
             ("A Galli la pergola piace, ma la vorrebbe più bassa.", "F"), ("Da gennaio Júlia avrà un contratto a tempo indeterminato.", "V"),
             ("Tre anni fa Júlia pensava di restare a Bologna per sempre.", "F"), ("Júlia e Bruno partono domani mattina presto.", "V")]),
    talk2=["Qual è il ricordo più divertente di Júlia, secondo te? Perché?", "Galli vuole la pergola più alta, Marco più bassa: chi ha ragione?",
           "Secondo te, è importante parlare una lingua straniera «senza accento»?"],
    n2=["B: 2 sulle scale, con tre valigie · 3 più alta (Marco la voleva più bassa) · 5 avrebbe detto di no.", "Ripresa: il primo giorno (A1 01, A2 35); la pergola (unità 37 e 38); il viaggio (unità 38)."],
    gref="tempi_racconto_b1",
    t4="tutti i tempi del racconto",
    pA=("Il racconto di Júlia. Completa con il tempo giusto del verbo tra parentesi.",
        [("Tre anni fa ___ (arrivare) a Bologna con tre valigie.", "sono arrivata"), ("Quel giorno ___ (piovere) e io non conoscevo nessuno.", "pioveva"),
         ("Quando Giulia mi ha sorriso, ___ già un cappuccino (ordinare).", "avevo ordinato"), ("Se non fossi venuta, non ___ (conoscere) i miei amici.", "avrei conosciuto"),
         ("L'anno prossimo ___ (finire) la terrazza di Galli.", "finiremo")]),
    pAw="26mm",
    pB=[("Abito a Bologna ", ["da tre anni", "tre anni fa"], "da tre anni", "."),
        ("Se ", ["avessi saputo", "avrei saputo"], "avessi saputo", " che pioveva, avrei preso l'ombrello."),
        ("Spero che i miei genitori ", ["tornino", "tornano"], "tornino", " in primavera.")],
    rule="<b>Passato prossimo</b> = i fatti (<i>sono arrivata</i>) · <b>imperfetto</b> = la scena, le abitudini (<i>pioveva</i>) · <b>trapassato prossimo</b> = prima di un altro fatto passato (<i>avevo ordinato</i>) · <b>condizionale passato</b> = quello che non è successo (<i>avrei detto di no</i>) · <b>se + congiuntivo trapassato</b> → condizionale passato (<i>se non fossi venuta, non avrei…</i>) · <b>futuro</b> = i progetti (<i>avrò il contratto</i>).",
    use=["Dove eri e che cosa facevi tre anni fa a dicembre?", "Che cosa avevi già fatto prima dei 20 anni?",
         "Una decisione che, potendo tornare indietro, prenderesti in modo diverso: <i>Se avessi…, avrei…</i>", "Che cosa avresti voluto fare quest'anno e non hai fatto?",
         "Che cosa farai l'anno prossimo? Che cosa speri che succeda?"],
    n4="A: 3 <i>avevo già ordinato</i>: prima del sorriso di Giulia · 4 periodo ipotetico dell'irrealtà. B2 <i>se</i> + congiuntivo trapassato, mai condizionale.",
    t5="il mio bilancio",
    fl=(["ricordare", "fare un bilancio", "immaginare un passato diverso", "fare progetti e auguri"],
        ["Mi ricordo che… · Quando sono arrivato/a… · Non avevo ancora…", "In questi anni ho imparato… · La cosa più difficile è stata… · Ne è valsa la pena.",
         "Se non avessi…, non avrei… · Avrei voluto… · Tre anni fa avrei detto…", "L'anno prossimo… · Spero che… · Buone feste! · Alla prossima!"]),
    pron=("Chi racconta bene fa una piccola <b>pausa</b> prima delle parole che fanno avanzare la storia: <i>e allora… · però… · alla fine…</i> e alza un po' la voce sulla parola importante: <i>Pioveva, non conoscevo NESSUNO…</i>",
          "Ascolta e ripeti. Poi leggi: «Pioveva, non conoscevo nessuno… e allora sono entrata in un bar.»"),
    task=("Il mio bilancio: racconta all'insegnante un periodo della tua vita (un lavoro, una città, un corso, gli ultimi tre anni). Come è cominciato, che cosa era difficile, che cosa hai imparato, che cosa avresti fatto in modo diverso e che cosa farai adesso. L'insegnante fa domande. Poi scambiatevi i ruoli.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>il primo giorno</li><li>le difficoltà</li><li>una persona importante</li><li>un errore divertente</li><li>se potessi tornare indietro…</li><li>l'anno prossimo</li></ul>",
          "Insegnante: E il primo giorno com'era? Che cosa avevi già fatto prima? Lo farei di nuovo? Lo studente: Quando ho cominciato… · Non avevo mai… · Se avessi saputo…, avrei… · L'anno prossimo… Controllare la scelta passato prossimo / imperfetto e il periodo ipotetico."),
    talk5=["Qual è stato il momento più bello del tuo anno? E il più difficile?", "Che cosa ti auguri per l'anno prossimo, anche per il tuo italiano?"],
    n5=["Far raccontare almeno due minuti senza interruzioni; poi domande.", "Annotare gli errori di tempo verbale (passato prossimo / imperfetto) per la conclusione."],
    hA=("Il blog di Júlia: «Tre anni a Bologna». Scegli la forma giusta.",
        "<i>Tre anni fa {0} a Bologna con tre valigie. Pioveva e non {1} nessuno. La sera {2} un cappuccino e Giulia mi ha sorriso. Ma ne è valsa la pena: se non {3} qui, non avrei mai conosciuto i miei amici. Da gennaio avrò il contratto a tempo indeterminato e l'anno prossimo {4} la terrazza più bella di Bologna. Buone feste! Júlia</i>",
        [(["sono arrivata", "arrivavo"], "sono arrivata"), (["conoscevo", "ho conosciuto"], "conoscevo"), (["avevo ordinato", "ordinerei"], "avevo ordinato"),
         (["fossi venuta", "sarei venuta"], "fossi venuta"), (["finiremo", "finissimo"], "finiremo")]),
    hB=("Riscrivi le frasi con il periodo ipotetico (se + congiuntivo trapassato, condizionale passato).",
        [("Júlia non è rimasta in Brasile, così ha conosciuto Giulia.", "Se Júlia fosse rimasta in Brasile, non avrebbe conosciuto Giulia."),
         ("Davide ha parlato velocissimo e Júlia non ha capito.", "Se Davide non avesse parlato velocissimo, Júlia avrebbe capito."),
         ("Júlia ha disegnato la pergola bassa perché Marco l'ha chiesto.", "Se Marco non l'avesse chiesto, Júlia non avrebbe disegnato la pergola bassa.")]),
    watch=[("Ho abitato qui da tre anni.", "Abito qui da tre anni.", "durata fino a oggi → presente + <i>da</i>."),
           ("Se avrei saputo, sarei venuta.", "Se avessi saputo, sarei venuta.", "dopo <i>se</i> → congiuntivo, non condizionale."),
           ("Quel giorno ha piovuto e non ho conosciuto nessuno.", "Quel giorno pioveva e non conoscevo nessuno.", "la scena → imperfetto.")],
    write=("Scrivi un post per il blog «Tre anni a…» (o «Un anno a…»): racconta un periodo della tua vita, dal primo giorno a oggi, e i progetti per il futuro.",
           "Tre anni fa…", ["passato prossimo e imperfetto (fatti e scena)", "almeno un trapassato e un periodo ipotetico (<i>se avessi…, avrei…</i>)", "almeno due progetti al futuro o con <i>spero che</i>"]),
    cando="So raccontare un periodo della mia vita, fare un bilancio e parlare dei progetti, usando tutti i tempi del racconto.",
    nH="Prossima lezione: <i>Ripasso 4</i> (unità 31–39).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 39 - Tre anni a Bologna")
