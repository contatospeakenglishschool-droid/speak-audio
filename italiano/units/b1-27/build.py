# Speak! Progresso B1 - Unità 27 "Qualsiasi cosa" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 27", audio_json=os.path.join(HERE, "audio_it-b1-unita-27.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-27", "27.1 Qualsiasi cosa", "27.2 Ripeti")

C = dict(
    nn="27", title="Qualsiasi cosa", subtitle="Incoraggiare e promettere · <b>qualsiasi, chiunque, dovunque, comunque + congiuntivo</b>",
    cover=[("SAI FARE", "incoraggiare un amico prima di una prova, fare promesse, parlare di lavoro e di futuro"),
           ("LINGUA", "Qualsiasi cosa succeda… · Chiunque ti conosca… · Dovunque tu vada… · Comunque vada…"),
           ("PRONUNCIA", "qualùnque, chiùnque, dovùnque: il suono «kw» e l'accento")],
    t1="il futuro",
    start=["Guarda la foto. Come si sente questa persona? Che cosa succederà?", "Prima di un colloquio importante sei calmo/a o nervoso/a?",
           "Che cosa ti dicono gli amici per incoraggiarti?"],
    kw=[("un periodo di lavoro per imparare, dopo gli studi", "il tirocinio"), ("una persona che fa un tirocinio", "il tirocinante / la tirocinante"),
        ("un incontro per un lavoro", "il colloquio"), ("un accordo scritto di lavoro", "il contratto"),
        ("un'offerta di lavoro pubblicata", "l'annuncio"), ("molto, moltissimo innamorato", "innamorato perso")],
    use_words=["Ti ricordi il tuo primo colloquio di lavoro? Com'è andato?", "Hai mai fatto un tirocinio? Dove?"],
    n1=["A: <i>tirocinio</i> = <i>estágio</i>; <i>colloquio</i> = <i>entrevista</i> (di lavoro), non <i>colóquio</i>."],
    aims=["Qualsiasi cosa: il colloquio di Camila · Parliamone", "Qualsiasi, chiunque, dovunque, comunque + congiuntivo",
          "Incoraggiare e promettere (27.2) · il suono «kw»", "Il messaggio di Camila · frasi con gli indefiniti · scrittura (100–150 parole)"],
    story="Giovedì 22 luglio, sera, bar Giulia. Domani è l'ultimo giorno di tirocinio di Camila: alle dieci colloquio con la direttrice. L'azienda prende una sola persona e i tirocinanti sono tre. Júlia la incoraggia («Chiunque abbia lavorato con te sa che sei bravissima»); Davide promette di offrire da bere qualunque cosa succeda (anche se mette da parte i soldi per la moto: «Per un'amica, questo e altro»). Camila ha guardato annunci a Milano, Torino, Roma: «Dovunque mi offrano un lavoro, ci vado»; Pietro dice che, ovunque lei vada, verrà con lei (ma deve finire l'università). Júlia: «Qualunque cosa, ma non i sandali della montagna!». Venerdì 23 luglio, ore 11: Camila chiama Júlia. L'hanno presa: contratto di un anno a Bologna, da settembre. Stasera si festeggia e paga Davide.",
    prob="Il portoghese ha le stesse strutture con il subjuntivo (<i>qualquer coisa que aconteça, quem quer que seja, onde quer que vá</i>), quindi l'idea è facile. Errori tipici: il plurale (<i>quaisquer</i> → <i>qualsiasi cose</i>), l'indicativo dopo <i>qualunque cosa</i>, il verbo al plurale dopo <i>chiunque</i>, e <i>comunque</i> usato per <i>como</i>. Falsi amici: <i>colloquio</i> (= entrevista) e <i>annuncio</i>.",
    real="In Italia molti giovani entrano nel mondo del lavoro con un <b>tirocinio</b> di alcuni mesi e poi, se va bene, con un <b>contratto a tempo determinato</b> (per esempio di un anno). Il sogno di tanti è il <b>posto fisso</b>, cioè il contratto a tempo indeterminato. Prima di un colloquio si dice <i>In bocca al lupo!</i> e si risponde <i>Crepi!</i>.",
    tr=("Qualsiasi cosa", "Ripeti: gli indefiniti con il congiuntivo"),
    gist=("Giovedì sera, al bar Giulia. Ascolta. Perché Camila è nervosa?",
          ["domani ha il colloquio finale del tirocinio", "domani parte per Milano", "ha litigato con Pietro"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il colloquio di Camila è alle dieci.", "V"), ("L'azienda prende due tirocinanti.", "F"),
             ("Davide promette di offrire da bere.", "V"), ("Camila ha guardato annunci solo a Bologna.", "F"),
             ("Pietro ha già finito l'università.", "F"), ("Camila ha un contratto di un anno da settembre.", "V")]),
    talk2=["Che cosa pensi della promessa di Pietro?", "Tu lasceresti la tua città per un lavoro? Dove andresti?",
           "Come festeggi una buona notizia?"],
    n2=["B: 2 una sola persona, i tirocinanti sono tre · 4 Milano, Torino, Roma · 5 deve ancora finire.", "Il tirocinio di Camila è cominciato a marzo; il contratto comincia a settembre."],
    gref="indefiniti_congiuntivo",
    t4="qualsiasi, chiunque, dovunque",
    pA=("Completa con qualsiasi / qualunque, chiunque, dovunque, comunque.",
        [("___ abbia lavorato con te sa che sei brava.", "Chiunque"), ("___ cosa succeda, stasera festeggiamo.", "Qualsiasi / Qualunque"),
         ("___ mi offrano un lavoro, ci vado.", "Dovunque"), ("___ vada, hai imparato tantissimo.", "Comunque"),
         ("___ lavoro tu trovi, sarai bravissima.", "Qualsiasi / Qualunque")]),
    pAw="34mm",
    pB=[("Qualunque cosa ", ["succede", "succeda"], "succeda", ", ti chiamo."),
        ("Chiunque ", ["venga", "vengano"], "venga", " è il benvenuto."),
        ("Puoi scegliere ", ["qualsiasi libro", "qualsiasi libri"], "qualsiasi libro", " dello scaffale.")],
    rule="<b>Qualsiasi / qualunque</b> (+ nome singolare), <b>qualsiasi cosa</b>, <b>chiunque</b> (persona), <b>dovunque / ovunque</b> (luogo), <b>comunque</b> (modo) + <b>congiuntivo</b> = non importa quale / chi / dove / come. Senza verbo dopo: <i>chiunque</i> = tutti, <i>comunque</i> = in ogni caso.",
    use=["Completa: <i>Qualunque cosa succeda, io…</i>", "Dovunque tu vada in vacanza, che cosa porti sempre?",
         "Chiunque venga a casa tua, che cosa gli offri?", "C'è un lavoro che non faresti mai, qualunque stipendio ti offrano?",
         "Che cosa diresti a un amico prima di un esame? (<i>Comunque vada…</i>)"],
    n4="B2: <i>chiunque</i> + verbo singolare.",
    t5="incoraggiare e promettere",
    fl=(["incoraggiare", "promettere", "non importa…", "reagire a una buona notizia"],
        ["Ce la farai! · Comunque vada… · Chiunque ti conosca sa che…", "Qualunque cosa succeda, io… · Dovunque tu vada, …",
         "Qualsiasi cosa ti dicano… · Chiunque sia…", "Lo sapevo! · Bravissimo/a! · Bisogna festeggiare!"]),
    pron=("Nelle parole con <b>qu</b> si sente «kw»: <b>qualsiasi</b>, <b>qualunque</b>, <b>dovunque</b>, <b>comunque</b>, <b>chiunque</b>. Attenzione all'accento: <i>qual<b>sì</b>asi</i>, <i>qua<b>lùn</b>que</i>, <i>chi<b>ùn</b>que</i>, <i>do<b>vùn</b>que</i>, <i>co<b>mùn</b>que</i>. In <i>chiunque</i> la <i>ch</i> è «k»: <i>ki-ÙN-kwe</i>.",
          "Ascolta e ripeti. Poi leggi: «Chiunque chiami, comunque vada, dovunque io sia, rispondo.»"),
    task=("Incoraggiare e promettere. L'insegnante è un amico nervoso prima di un momento importante (scegliete una situazione). Incoraggialo con almeno quattro indefiniti diversi e fagli tre promesse. Poi scambiate i ruoli: tu sei nervoso/a e l'insegnante ti incoraggia.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>un colloquio di lavoro</li><li>un esame difficile</li><li>un trasloco all'estero</li><li>il primo giorno di un lavoro</li><li>una cena con i suoceri</li><li>una gara sportiva</li></ul>",
          "Insegnante (amico nervoso): E se mi fanno una domanda difficile? · E se non mi prendono? · Non conosco nessuno! Lo studente: Qualsiasi domanda ti facciano… · Chiunque ti conosca… · Dovunque tu vada, ti vengo a trovare. · Comunque vada, stasera… Correggere <i>qualunque cosa succede</i> → <i>succeda</i>."),
    talk5=["Hai mai fatto una promessa difficile da mantenere?", "Secondo te, è meglio il posto fisso o cambiare spesso lavoro?"],
    n5=["far battere sulla sillaba accentata: <i>qua-LÙN-que</i>, <i>chi-ÙN-que</i>.", "Pretendere il congiuntivo dopo ogni indefinito; accettare anche <i>in ogni caso</i> per <i>comunque</i>."],
    hA=("Il messaggio di Camila a Elena. Scegli la forma giusta.",
        "<i>Elena, notizia bomba: mi hanno presa! Contratto di un anno da settembre. Ieri sera ero nervosissima, ma Júlia mi ha detto: «{0} abbia lavorato con te sa che sei brava». Davide ha promesso: «Qualunque cosa {1}, festeggiamo». E Pietro, romantico: «Dovunque tu {2}, vengo con te». Stasera offre Davide, a {3} venga al bar! Vieni anche tu? {4} vada il tuo tirocinio, a settembre facciamo una festa insieme. Baci!</i>",
        [(["Chiunque", "Qualsiasi"], "Chiunque"), (["succeda", "succede"], "succeda"), (["vada", "vai"], "vada"),
         (["chiunque", "qualunque"], "chiunque"), (["Comunque", "Dovunque"], "Comunque")]),
    hB=("Riscrivi la frase con l'indefinito tra parentesi.",
        [("Non importa che cosa dici: io ti credo. (qualunque cosa)", "Qualunque cosa tu dica, io ti credo."), ("Non importa dove vai: ti scrivo ogni giorno. (dovunque)", "Dovunque tu vada, ti scrivo ogni giorno."),
         ("Non importa chi chiama: non ci sono. (chiunque)", "Chiunque chiami, non ci sono.")]),
    watch=[("Qualunque cosa succede, ti chiamo.", "Qualunque cosa succeda, ti chiamo.", "dopo gli indefiniti: congiuntivo."),
           ("Qualsiasi cose ti servono…", "Qualsiasi cosa ti serva…", "<i>qualsiasi</i> + singolare."),
           ("Ho un colloquio con il mio amico.", "Ho una chiacchierata con il mio amico.", "<i>colloquio</i> = di lavoro, formale.")],
    write=("Scrivi un messaggio a un amico o un'amica che sta per affrontare un momento importante (un esame, un colloquio, un trasloco): incoraggialo/a e fai delle promesse.",
           "Qualunque cosa succeda…", ["quattro indefiniti diversi con il congiuntivo", "due promesse", "un augurio finale (<i>In bocca al lupo!</i>)"]),
    cando="So incoraggiare una persona e fare promesse con qualsiasi, chiunque, dovunque e comunque + congiuntivo.",
    nH="Prossima unità: <i>Bisognerebbe che…</i> (proposte e consigli con il congiuntivo imperfetto).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 27 - Qualsiasi cosa")
