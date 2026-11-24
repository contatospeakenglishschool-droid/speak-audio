# Speak! Progresso B1 - Unità 33 "Così stanco che…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 33", audio_json=os.path.join(HERE, "audio_it-b1-unita-33.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-33", "33.1 Così stanco che", "33.2 Ripeti")

C = dict(
    nn="33", title="Così stanco che…", subtitle="La seconda maratona di Davide · <b>così… che, tanto… che, tale… che</b>",
    cover=[("SAI FARE", "raccontare un'esperienza intensa, esagerare, dire le conseguenze"),
           ("LINGUA", "così / talmente… che · tanto… che · un… tale che · al punto da + infinito"),
           ("PRONUNCIA", "l'enfasi: cosììì stanco… che · co-SÌ")],
    t1="la maratona",
    start=["Guarda la foto. Hai mai corso una gara o guardato una maratona?", "Fai sport? Quante volte a settimana?",
           "Qual è la cosa più faticosa che hai fatto nella tua vita?"],
    kw=[("la gara di corsa di 42 chilometri", "la maratona"), ("la linea dove finisce la gara", "il traguardo"),
        ("prepararsi con esercizio fisico regolare", "allenarsi"), ("una persona che corre la maratona", "il maratoneta"),
        ("il tempo migliore di una persona", "il record personale"), ("con la pelle più scura dopo tanto sole", "abbronzato")],
    use_words=["Hai un record personale in qualcosa (sport, lavoro, giochi)?", "Ti alleneresti per mesi per arrivare a un traguardo? Quale?"],
    n1=["A: <i>il traguardo</i> = la fine della gara, ma anche un obiettivo nella vita; <i>record personale</i> = il miglior tempo di una persona."],
    aims=["Così stanco che…: la maratona di Davide · Parliamone", "così… che, tanto… che, tale… che, al punto da",
          "Gara di esagerazioni (33.2) · l'enfasi e la pausa", "Il post di Davide · riscrivi · scrittura (100–150 parole)"],
    story="Lunedì 25 ottobre, Bar Giulia (Giulia, Davide, Júlia, Camila). Giulia è tornata dalla Sardegna da due settimane, abbronzatissima. Domenica Davide ha corso la sua seconda maratona: 3 ore e 31, a un minuto dall'obiettivo, ma 27 minuti meglio dell'anno scorso (3:58, A2 32). Si è allenato tutta l'estate salendo a San Luca; al km 35 è arrivato il vento. Gli amici gridavano al km 30; Camila ha sbagliato strada ed è arrivata al traguardo dopo di lui. Giulia offre la colazione. Prossimo obiettivo: 3:25.",
    prob="Il calco più tipico è <i>de tão cansado que estava</i> → <s>di tanto stanco che ero</s>: in italiano si dice <i>ero così stanco che…</i>. <i>Tanto</i> davanti a un nome si accorda (<s>tanto gente</s> → <i>tanta gente</i>), <i>così</i> e <i>talmente</i> no. Dopo <i>che</i> serve l'indicativo, non il congiuntivo (<s>che non riuscissi</s>). Attenzione anche a <i>fare il bagno</i> al mare («tomar banho de mar», non <s>prendere il bagno</s>) e a <i>commuoversi</i> («se emocionar» fino alle lacrime).",
    real="La maratona misura <b>42,195 km</b>: la distanza viene dalle Olimpiadi di Londra del 1908 ed è diventata ufficiale nel 1921. Il <b>portico di San Luca</b> a Bologna sale dalla città al santuario con 666 archi, per quasi 4 km: molti bolognesi ci vanno a camminare e a correre. In Italia le maratone si corrono soprattutto in primavera e in autunno, quando non fa troppo caldo.",
    tr=("Così stanco che", "Ripeti: le consecutive"),
    gist=("Lunedì mattina, al bar. Ascolta. Di che cosa parlano gli amici?",
          ["della maratona di Davide", "delle vacanze di Camila", "di una gara di ciclismo"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Davide ha corso la maratona in meno di tre ore e mezza.", "F"), ("Rispetto all'anno scorso ha migliorato di quasi mezz'ora.", "V"),
             ("Si è allenato correndo al mare.", "F"), ("Negli ultimi chilometri c'era molto vento.", "V"),
             ("Camila è arrivata al traguardo prima di Davide.", "F"), ("In Sardegna Giulia faceva il bagno anche a ottobre.", "V")]),
    talk2=["Davide è deluso o contento? E tu, al suo posto?", "Un minuto: è tanto o è poco? In quali situazioni un minuto cambia tutto?",
           "Che cosa pensi di chi si allena per mesi per una gara?"],
    n2=["B: 1 tre ore e trentuno · 3 salendo a San Luca · 5 dieci minuti dopo di lui.", "Ripresa: la prima maratona di Davide, 3 ore e 58 (A2, unità 32); Giulia in Sardegna per un mese (unità 31)."],
    gref="frasi_consecutive_b1",
    t4="così… che, tanto… che",
    pA=("Completa con: così · tanta · tale · tanto · al.",
        [("Era ___ stanca che si è addormentata sul divano.", "così"), ("C'era ___ gente che non si vedeva il traguardo.", "tanta"),
         ("Tirava un vento ___ che sembrava di correre in salita.", "tale"), ("Abbiamo riso ___ che mi fa male la pancia.", "tanto"),
         ("Ero stanco ___ punto da non ricordare il mio nome.", "al")]),
    pAw="20mm",
    pB=[("Faceva così caldo che ", ["facevo", "facessi"], "facevo", " il bagno anche a ottobre."),
        ("Ho ", ["tanto", "tanta"], "tanta", " sete che berrei un litro d'acqua."),
        ("Era così emozionata ", ["da", "per"], "da", " sbagliare strada.")],
    rule="<b>così / talmente</b> + aggettivo o avverbio + <b>che</b> · <b>tanto/a/i/e</b> + nome + <b>che</b> · verbo + <b>tanto che</b> · <b>un</b> + nome + <b>tale che</b> → <b>indicativo</b> (o condizionale). Stesso soggetto: <b>così… da / al punto da</b> + infinito.",
    use=["Racconta un giorno in cui eri stanchissimo/a. Usa <i>così… che</i>.", "Il posto più caldo o più freddo dove sei stato/a: <i>Faceva così… che…</i>",
         "Una volta in cui hai riso tantissimo. Usa <i>tanto che</i>.", "Un film o un libro talmente bello che…",
         "Completa: <i>C'era una fila tale che…</i>"],
    n4="A1: accettare anche <i>talmente</i>. B2: <i>sete</i> è femminile → <i>tanta</i>.",
    t5="gara di esagerazioni",
    fl=(["esagerare", "raccontare la conseguenza", "reagire a un racconto", "incoraggiare"],
        ["Ero così… che… · Era talmente… · C'era una tale…", "…al punto da… · …tanto che…",
         "Ma dai! · Non ci credo! · Che fatica! · Che peccato!", "Ce la farai! · Bravissimo/a! · Per un minuto!"]),
    pron=("Nelle consecutive la parola dell'intensità è lunga e forte, poi c'è una piccola pausa prima di <i>che</i>: <i>Ero <b>cosììì</b> stanco… che non parlavo.</i> <i>Così</i> ha l'accento sull'ultima sillaba: co<b>sì</b>.",
          "Ascolta e ripeti. Poi leggi: «Ho le gambe così stanche che non riesco a scendere le scale.»"),
    task=("Gara di esagerazioni: l'insegnante propone una situazione, lo studente racconta la conseguenza più esagerata possibile; poi si scambiano i ruoli. Vince chi usa più strutture diverse. Alla fine racconta una tua sfida personale (sport, lavoro, studio).",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>un volo di 14 ore</li><li>un esame difficilissimo</li><li>una festa di matrimonio</li><li>il primo giorno di lavoro</li><li>un'estate senza aria condizionata</li><li>una lunga camminata in montagna</li></ul>",
          "Insegnante: Era un volo così lungo che… · E poi? · Ma dai! Lo studente: Ero talmente stanco che… · C'era una tale confusione che… · Ho mangiato tanto che… Correggere <i>tanto</i> senza accordo e il congiuntivo dopo <i>che</i>."),
    talk5=["Hai mai fatto una sfida sportiva (una gara, una lunga camminata)? Com'è andata?", "Per quale obiettivo ti alleneresti per mesi?"],
    n5=["allungare la parola dell'intensità e fare la pausa prima di <i>che</i>.", "Pretendere almeno cinque strutture diverse; incoraggiare l'esagerazione e reagire con <i>Ma dai!</i>"],
    hA=("Il post di Davide sui social. Scegli la forma giusta.",
        "<i>Seconda maratona: 3 ore e 31 minuti! Per un minuto non ho fatto 3:30, ma sono {0} contento che non riesco a smettere di sorridere. Fino al chilometro 35 andavo {1} bene che sognavo già il record. Poi è arrivato un vento {2} che sembrava una salita. Al trentesimo chilometro i miei amici gridavano {3} che li sentivo da lontano. Oggi ho le gambe distrutte, al punto {4} non riuscire a scendere le scale. L'anno prossimo: 3:25!</i>",
        [(["così", "tanta"], "così"), (["talmente", "tale"], "talmente"), (["tale", "tanto"], "tale"),
         (["tanto", "tale"], "tanto"), (["da", "che"], "da")]),
    hB=("Unisci le due frasi con le parole tra parentesi.",
        [("Faceva molto caldo. Siamo rimasti in casa. (così… che)", "Faceva così caldo che siamo rimasti in casa."),
         ("C'era molta gente. Non abbiamo trovato posto. (tanta… che)", "C'era tanta gente che non abbiamo trovato posto."),
         ("Era molto stanco. Non riusciva a parlare. (al punto da)", "Era stanco al punto da non riuscire a parlare.")]),
    watch=[("Di tanto stanco che ero, non parlavo.", "Ero così stanco che non parlavo.", "<i>de tão cansado</i> non si traduce parola per parola."),
           ("C'era tanto gente.", "C'era tanta gente.", "<i>tanto</i> + nome si accorda: <i>la gente</i> → <i>tanta</i>."),
           ("…che non riuscissi a parlare.", "…che non riuscivo a parlare.", "nella consecutiva: indicativo.")],
    write=("Racconta una sfida che hai affrontato (una gara, un esame, un trasloco, un viaggio difficile): com'è andata e che cosa hai provato.",
           "Non dimenticherò mai…", ["almeno quattro strutture consecutive (<i>così… che, tanto… che, tale… che, al punto da</i>)", "passato prossimo e imperfetto", "una frase finale sul prossimo obiettivo"]),
    cando="So raccontare un'esperienza intensa e le sue conseguenze con così… che, tanto… che, tale… che e al punto da.",
    nH="Prossima unità: <i>Va fatto così</i> (passivo con andare; si passivante con i verbi modali).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 33 - Così stanco che")
