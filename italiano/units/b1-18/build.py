# Speak! Progresso B1 - Unità 18 "Mi chiedo se…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 18", audio_json=os.path.join(HERE, "audio_it-b1-unita-18.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-18", "18.1 Mi chiedo se...", "18.2 Ripeti")

C = dict(
    nn="18", title="Mi chiedo se…", subtitle="Dubbi e domande · <b>le interrogative indirette</b>",
    cover=[("SAI FARE", "esprimere dubbi, riferire domande, chiedere informazioni con gentilezza"),
           ("LINGUA", "Mi chiedo se… · Non so che cosa dire. · Potrebbe dirmi dove…?"),
           ("PRONUNCIA", "domanda diretta (sale) e indiretta (scende)")],
    t1="i dubbi",
    start=["Guarda la foto. Che cosa pensa questa persona? Di che cosa ha dubbi?", "Quando sei nervoso/a, che cosa ti chiedi?",
           "Ti ricordi la prima volta che hai conosciuto i genitori di un fidanzato o di un amico?"],
    kw=[("farsi una domanda, avere un dubbio", "chiedersi"), ("non sapere niente di una cosa", "non avere idea"),
        ("il titolo di campione d'Italia nel calcio", "lo scudetto"), ("organizzarsi prima di una cosa per essere pronti", "prepararsi"),
        ("il gruppo di partite di una stagione", "il campionato"), ("dare un po' di spazio a qualcuno", "lasciare respirare")],
    use_words=["Che cosa ti chiedi spesso sul tuo futuro?", "C'è un argomento di cui non hai idea? Quale?"],
    n1=["A: <i>chiedersi</i> = <i>perguntar-se</i>; <i>chiedere</i> = <i>perguntar</i> e anche <i>pedir</i>. Lo <i>scudetto</i> è lo scudo tricolore sulla maglia dei campioni d'Italia."],
    aims=["Mi chiedo se… Chiara conosce i genitori di Bruno · Parliamone", "Le interrogative indirette: se, chi, che cosa, dove, quando…",
          "Domande gentili (18.2) · gioco di ruolo: chiedere informazioni", "Il messaggio di Chiara · dalla domanda diretta all'indiretta · scrittura (100–150 parole)"],
    story="Martedì 20 aprile, sera, davanti a una trattoria in via del Pratello: Chiara, la fidanzata di Bruno, sta per conoscere Lúcia e Roberto. È nervosissima: si chiede se piacerà, non sa che cosa dire, non sa se Lúcia capisce l'italiano (Júlia: capisce quasi tutto). Roberto, dopo le spiegazioni di Davide, vuole sapere chi vincerà lo scudetto; Chiara non sa niente di calcio. Ha portato un dolce (lo darà dopo cena). Lúcia arriva: «Mi chiedevo quando ti avremmo conosciuta» e la riempie di domande; Bruno: «Lasciala respirare!». Chiara dà del Lei a Lúcia e risponde a tutto… dopo essere entrata, perché ha fame.",
    prob="La struttura è uguale al portoghese (<i>me pergunto se, não sei o que</i>). Errori tipici: <i>non so cosa che dire</i> (calco di <i>o que</i>), <i>mi chiedo quando che arriva</i> (dal parlato <i>quando que</i>), il tempo che non cambia dopo un verbo al passato (<i>mi ha chiesto se parlo</i>) e l'intonazione da domanda in una frase che non lo è. <i>Chiedere</i> vale per <i>perguntar</i> e per <i>pedir</i>.",
    real="Via del Pratello, nel centro di Bologna, è una strada piena di osterie e trattorie frequentate da studenti. In Italia, quando si conoscono i genitori del fidanzato o della fidanzata, all'inizio di solito si dà del <i>Lei</i>, finché non sono loro a proporre il <i>tu</i>. Lo scudetto è il simbolo dei campioni d'Italia nel calcio.",
    tr=("Mi chiedo se…", "Ripeti: le interrogative indirette"),
    gist=("Martedì sera, davanti a una trattoria. Ascolta. Perché Chiara è nervosa?",
          ["sta per conoscere i genitori di Bruno", "ha un esame il giorno dopo", "non ha prenotato il ristorante"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Secondo Júlia, sua madre capisce quasi tutto in italiano.", "V"), ("Chiara sa molte cose sul calcio.", "F"),
             ("Roberto vuole sapere chi vincerà lo scudetto.", "V"), ("Chiara dà il dolce a Lúcia subito.", "F"),
             ("Lúcia fa molte domande a Chiara.", "V"), ("Chiara dà del tu a Lúcia.", "F")]),
    talk2=["Perché Bruno dice «Mamma, lasciala respirare!»?", "Chiara risponde «Non si preoccupi, signora». Perché usa il Lei?",
           "Secondo te, Chiara piacerà ai genitori di Bruno? Perché?"],
    n2=["B: 2 non sa niente di calcio · 4 dopo cena, consiglio di Júlia · 6 dà del Lei («Non si preoccupi, signora»).", "Far notare: <i>Mi chiedevo quando ti avremmo conosciuta</i> = futuro nel passato (B1 03)."],
    gref="interrogative_indirette",
    t4="le interrogative indirette",
    pA=("Trasforma la domanda in una domanda indiretta.",
        [("«Piacerò ai tuoi genitori?» → Mi chiedo ___ ai tuoi genitori.", "se piacerò"), ("«Che cosa porto?» → Non so ___.", "che cosa portare / che cosa porto"),
         ("«Dove abitano i tuoi?» → Lúcia vuole sapere ___ i miei.", "dove abitano"), ("«Quanti anni hai?» → Ti chiederà ___.", "quanti anni hai"),
         ("«Parli italiano?» → Mi ha chiesto ___ italiano.", "se parlavo")]),
    pAw="34mm",
    pB=[("Non so ", ["che cosa", "cosa che"], "che cosa", " dire ai tuoi genitori."),
        ("Mi chiedo ", ["quando", "quando che"], "quando", " arriva l'autobus."),
        ("Mi ha chiesto se ", ["avevo", "ho"], "avevo", " fame.")],
    rule="<b>Mi chiedo / non so / vorrei sapere</b> + <b>se</b> (sì/no) o <b>chi, che cosa, come, dove, quando, perché, quanto</b>. Modo: <b>indicativo</b> nel parlato, <b>congiuntivo</b> nel registro curato (<i>non so se capisca</i>). Verbo principale al passato → il tempo va indietro: <i>mi ha chiesto se parlavo</i>.",
    use=["Che cosa ti chiedi prima di un colloquio di lavoro? <i>Mi chiedo se…</i>", "Una cosa che non sai di te stesso/a: <i>Non so perché…</i>",
         "Che cosa vorresti sapere dell'Italia? <i>Vorrei sapere…</i>", "Che cosa ti ha chiesto l'ultima persona che hai conosciuto?",
         "Chiedi un'informazione con gentilezza: <i>Potrebbe dirmi…?</i>"],
    n4="A5 e B3: verbo principale al passato → <i>parlavo, avevo</i>. In A2 accettare entrambe le forme.",
    t5="domande gentili",
    fl=(["esprimere un dubbio", "chiedere con gentilezza", "rispondere senza sapere", "riferire una domanda"],
        ["Mi chiedo se… · Mi domando come… · Chissà se…", "Potrebbe dirmi…? · Sa per caso se…? · Vorrei sapere…",
         "Non ne ho idea. · Non saprei. · Non so se… · Mi informo e Le faccio sapere.", "Mi ha chiesto se… · Voleva sapere dove… · Mi domandava perché…"]),
    pron=("La domanda diretta <b>sale</b> alla fine: <i>Parli italiano? ↗</i>. Nella domanda indiretta la voce <b>scende</b>, perché la frase non è una domanda: <i>Mi chiedo se parli italiano. ↘</i> Solo con <i>Sa…? / Potrebbe…?</i> la voce torna a salire.",
          "Ascolta e ripeti. Poi trasforma tre domande dell'insegnante in domande indirette."),
    task=("Gioco di ruolo. Stai organizzando una vacanza di una settimana a Bologna. Telefoni alla reception di un albergo (l'insegnante) e chiedi informazioni con domande gentili e indirette. Poi l'insegnante ti chiede che cosa ti ha risposto l'albergo: riferisci le domande e le risposte.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>camere libere</li><li>prezzo e colazione</li><li>distanza dalla stazione</li><li>parcheggio</li><li>animali</li><li>orario del check-in</li></ul>",
          "Insegnante (receptionist): Buongiorno, Hotel Due Torri. Mi dica! · Risponde: sì, una doppia a 120 euro con colazione; 10 minuti a piedi dalla stazione; parcheggio no, garage vicino; animali piccoli sì; check-in dalle 14. Lo studente: Potrebbe dirmi se…? · Vorrei sapere quanto… · Sa per caso se…? Poi riferisce: Ho chiesto se… e mi hanno detto che…"),
    talk5=["Fai tante domande quando conosci una persona nuova, o preferisci ascoltare?", "Quali domande trovi indiscrete?"],
    n5=["marcare con la mano: domanda ↗, indiretta ↘.", "Il nome dell'albergo è inventato. Pretendere almeno quattro domande indirette diverse e due domande riferite al passato."],
    hA=("Mercoledì mattina Chiara scrive a Júlia. Scegli la forma giusta.",
        "<b>Chiara:</b> Ciao Júlia! Grazie per ieri sera. Ero così nervosa che non sapevo {0} dire! Tua madre mi ha chiesto {1} studiavo, dove abitavano i miei e perfino {2} pensavamo di sposarci. Tuo padre invece voleva sapere {3} squadra tifava mio padre. Adesso mi chiedo {4} gli sono piaciuta davvero… Tu che dici?",
        [(["che cosa", "cosa che"], "che cosa"), (["che cosa", "che"], "che cosa"), (["quando", "quando che"], "quando"),
         (["per quale", "quale che"], "per quale"), (["se", "si"], "se")]),
    hB=("Trasforma in domanda indiretta, cominciando come indicato.",
        [("«Dov'è la stazione?» (Potrebbe dirmi…)", "Potrebbe dirmi dov'è la stazione?"), ("«Vieni stasera?» (Marco mi ha chiesto…)", "Marco mi ha chiesto se venivo stasera."),
         ("«Perché sei in ritardo?» (Non so…)", "Non so perché sei in ritardo.")]),
    watch=[("Non so cosa che dire.", "Non so che cosa dire.", "niente <i>che</i> dopo <i>cosa</i>."),
           ("Mi chiedo quando che arrivano.", "Mi chiedo quando arrivano.", "niente <i>che</i> dopo <i>quando, dove</i>."),
           ("Mi chiedo se mi piacerò ai tuoi genitori.", "Mi chiedo se piacerò ai tuoi genitori.", "con <i>piacere</i> il soggetto sono io.")],
    write=("Scrivi a un amico i tuoi dubbi prima di un momento importante (un colloquio, un viaggio, conoscere una persona): che cosa ti chiedi, che cosa non sai, che cosa vorresti sapere.",
           "Caro/a…, domani… e mi chiedo se…", ["cinque interrogative indirette con parole diverse (<i>se, come, dove, quando, perché</i>)", "una domanda riferita al passato (<i>mi ha chiesto se…</i>)", "un <i>chissà se…</i>"]),
    cando="So esprimere dubbi, riferire domande e chiedere informazioni con domande indirette e gentili.",
    nH="Prossima unità: <i>Ha detto che sarebbe…</i> (il discorso indiretto al passato).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 18 - Mi chiedo se")
