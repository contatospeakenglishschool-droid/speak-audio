# Speak! Progresso B1 - Unità 34 "Va fatto così" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 34", audio_json=os.path.join(HERE, "audio_it-b1-unita-34.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-34", "34.1 Va fatto così", "34.2 Ripeti")

C = dict(
    nn="34", title="Va fatto così", subtitle="Il sopralluogo con la Soprintendenza · <b>va fatto, si può fare, si devono fare</b>",
    cover=[("SAI FARE", "spiegare regole e istruzioni, dire che cosa si può e non si può fare"),
           ("LINGUA", "va fatto · vanno fatte · si può / si deve + infinito · si possono fare"),
           ("PRONUNCIA", "le doppie dei participi: fatto, messo · vanno ≠ vano")],
    t1="palazzi antichi",
    start=["Guarda la foto. Ti piacciono i palazzi antichi? Ci vivresti?", "Nella tua città ci sono regole per i palazzi del centro storico?",
           "Preferisci una casa antica restaurata o una casa nuova? Perché?"],
    kw=[("la grande porta d'ingresso di un palazzo", "il portone"), ("una pittura fatta direttamente sul muro o sul soffitto", "l'affresco"),
        ("riportare un oggetto antico com'era all'origine", "restaurare"), ("un materiale leggero per costruire pareti interne", "il cartongesso"),
        ("l'opinione ufficiale di un ufficio pubblico", "il parere"), ("il cartello con il nome di un negozio o di un albergo", "l'insegna")],
    use_words=["Hai mai visto un affresco famoso? Dove?", "Quale insegna ti ricordi della tua città? Perché?"],
    n1=["A: <i>il parere</i> = opinione ufficiale, qui obbligatoria; <i>il cartongesso</i> = pannelli leggeri di gesso per le pareti interne."],
    aims=["Va fatto così: il sopralluogo nel palazzo · Parliamone", "andare + participio · si può / si deve + infinito",
          "Il nuovo collega (34.2) · le doppie dei participi", "Il cartello del cantiere · riscrivi · scrittura (100–150 parole)"],
    story="Mercoledì 3 novembre, nel palazzo del dottor Galli: Júlia e Marco fanno il sopralluogo con la dottoressa Benassi della Soprintendenza. Il portone del Seicento va restaurato; le finestre vanno fatte in legno (niente alluminio); il colore della facciata va scelto dall'elenco del Comune; il soffitto affrescato del primo piano va protetto e fotografato; i bagni si possono fare in cartongesso, senza toccare i muri originali. La terrazza sì, ma non si deve vedere dalla strada: niente ombrelloni, niente insegne luminose. Il parere ufficiale arriva entro due settimane. Toccherà a Júlia dirlo a Galli.",
    prob="In portoghese non esiste <i>andare</i> + participio, e <i>va fatto</i> sembra «vai ser feito» (futuro): vuol dire invece «deve ser feito». Errori tipici: <s>va essere restaurato</s>, il participio senza accordo (<s>le finestre va fatto</s> → <i>vanno fatte</i>) e il modale al singolare con una cosa plurale (<s>si può usare i mattoni</s> → <i>si possono</i>; nel parlato brasiliano «pode usar os tijolos»). Doppie dei participi: <i>fa<b>tt</b>o, me<b>ss</b>o</i>.",
    real="Nei palazzi <b>vincolati</b> portoni, finestre e affreschi originali vanno conservati, e per ogni intervento la Soprintendenza dà un <b>parere</b> obbligatorio. Molti centri storici italiani hanno regole comunali sui <b>colori delle facciate</b> e sulle <b>insegne</b>. Nei restauri si usa spesso il <b>cartongesso</b>: con pareti leggere si creano stanze nuove senza toccare i muri antichi.",
    tr=("Va fatto così", "Ripeti: le regole"),
    gist=("Mercoledì mattina, in un palazzo antico. Ascolta. Che cosa fanno Júlia e Marco?",
          ["un sopralluogo con la Soprintendenza", "una riunione con il dottor Galli allo studio", "una visita guidata per turisti"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il portone va sostituito con uno nuovo.", "F"), ("Le finestre in alluminio non sono permesse.", "V"),
             ("Il colore della facciata si può scegliere liberamente.", "F"), ("Prima dei lavori gli affreschi vanno fotografati.", "V"),
             ("La terrazza non si deve vedere dalla strada.", "V"), ("I lavori possono cominciare anche senza il parere.", "F")]),
    talk2=["Secondo te, le regole della Soprintendenza sono giuste o troppo severe?", "Come reagirà il dottor Galli? Che cosa gli dirà Júlia?",
           "Nella tua città ci sono edifici storici protetti? Come sono tenuti?"],
    n2=["B: 1 va restaurato · 3 va scelto dall'elenco del Comune · 6 senza il parere non si possono cominciare.", "Ripresa: il progetto dell'albergo, la Soprintendenza e la terrazza di Galli (unità 32)."],
    gref="passivo_andare_modali",
    t4="va fatto, si può fare",
    pA=("Completa con va o vanno e il participio del verbo tra parentesi.",
        [("Il portone ___ (restaurare).", "va restaurato"), ("Le finestre ___ (fare) in legno.", "vanno fatte"),
         ("Gli affreschi ___ (proteggere) durante i lavori.", "vanno protetti"), ("La terrazza ___ (tenere) bassa.", "va tenuta"),
         ("Il modulo ___ (firmare) entro venerdì.", "va firmato")]),
    pAw="32mm",
    pB=[("In un palazzo vincolato l'alluminio non ", ["si può", "si possono"], "si può", " usare."),
        ("Senza il parere, i lavori non ", ["si può", "si possono"], "si possono", " cominciare."),
        ("Le insegne luminose non ", ["si deve", "si devono"], "si devono", " mettere sulla facciata.")],
    rule="<b>andare</b> + participio passato = <b>deve essere</b> + participio: <i>Il portone va restaurato. Le finestre vanno fatte in legno.</i> Il participio concorda con il soggetto; solo tempi semplici. <b>Si</b> + <b>potere / dovere</b> + infinito: il modale concorda con la cosa: <i>si può usare il legno · si possono fare i bagni</i>.",
    use=["Come va fatto il caffè con la moka? Spiega con <i>va / vanno</i>.", "Che cosa non si deve fare in una chiesa o in un museo?",
         "Che cosa si può e che cosa non si può fare a casa tua (ospiti, animali, musica)?", "Come vanno trattati i clienti nel tuo lavoro?",
         "Prima di un viaggio all'estero: che cosa va preparato?"],
    n4="A: 2 e 3 accordo al plurale (<i>fatte, protetti</i>). B1: <i>l'alluminio</i> è singolare → <i>si può</i>.",
    t5="il nuovo collega",
    fl=(["dare una regola", "vietare", "permettere", "chiedere istruzioni"],
        ["Va fatto così. · …vanno messi qui. · Si deve…", "Non si può… · Non va… · È vietato…",
         "Si può… · Puoi tranquillamente… · Nessun problema se…", "Come va fatto? · Si può…? · Dove vanno messi…?"]),
    pron=("Nei participi la doppia è lunga: <i>fa<b>tt</b>o, me<b>ss</b>o, scri<b>tt</b>o, de<b>tt</b>o</i>. Attenzione: <i>va<b>nn</b>o</i> (da <i>andare</i>) ≠ <i>vano</i> (inutile). <i>Va fatto</i> si dice come una sola parola: va-FAT-to.",
          "Ascolta e ripeti. Poi leggi: «Le finestre vanno fatte in legno, come quelle originali.»"),
    task=("Il nuovo collega: l'insegnante è un nuovo collega (o un ospite che resta un mese a casa tua). Spiegagli le regole: come vanno fatte le cose, che cosa si può e che cosa non si deve fare. L'insegnante fa domande e prova a «sbagliare».",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>gli orari e le pause</li><li>il caffè e la cucina</li><li>la posta e le e-mail</li><li>le riunioni</li><li>il rumore e il telefono</li><li>come ci si veste</li></ul>",
          "Insegnante: Posso mangiare alla scrivania? · Come va fatto il rapporto? · E se arrivo tardi? Lo studente: Qui non si può… · Il rapporto va mandato entro… · Le riunioni vanno preparate… Correggere il participio senza accordo e <i>si può</i> con una cosa plurale."),
    talk5=["Ci sono regole che ti sembrano inutili? Quali?", "Regole in Italia e in Brasile: che differenze conosci (a tavola, in strada, in ufficio)?"],
    n5=["far sentire le doppie dei participi e distinguere <i>vanno</i> / <i>vano</i>.", "Pretendere almeno tre frasi con <i>va / vanno</i> e due con <i>si può / si deve</i>."],
    hA=("Il cartello del cantiere scritto da Júlia. Scegli la forma giusta.",
        "<i>CANTIERE: REGOLE PER TUTTI. Il casco {0} portato sempre. Gli affreschi del primo piano {1} toccati: sono protetti dalla Soprintendenza. I materiali {2} lasciati nel cortile, non sulla strada. I lavori rumorosi {3} fare solo dalle 8 alle 12, prima che apra il ristorante. Per ogni dubbio {4} chiamare l'architetto. Grazie! Júlia</i>",
        [(["va", "vanno"], "va"), (["non vanno", "non va"], "non vanno"), (["vanno", "va"], "vanno"),
         (["si possono", "si può"], "si possono"), (["si deve", "si devono"], "si deve")]),
    hB=("Riscrivi la regola con andare + participio.",
        [("Bisogna restaurare il portone.", "Il portone va restaurato."),
         ("Bisogna fotografare tutti gli affreschi.", "Tutti gli affreschi vanno fotografati."),
         ("Non si deve toccare il soffitto.", "Il soffitto non va toccato.")]),
    watch=[("Le finestre va fatto in legno.", "Le finestre vanno fatte in legno.", "<i>andare</i> e il participio concordano con il soggetto."),
           ("Si può usare i mattoni.", "Si possono usare i mattoni.", "con il si il modale concorda con la cosa."),
           ("Il portone va essere restaurato.", "Il portone va restaurato.", "<i>va fatto</i> non è «vai ser feito»: vuol dire «deve ser feito».")],
    write=("Scrivi le regole di un posto che conosci bene (la tua casa per un ospite, il tuo ufficio per un nuovo collega, la tua città per un turista): che cosa va fatto, che cosa si può e che cosa non si deve fare.",
           "Benvenuto! Qui le cose vanno fatte così…", ["almeno quattro frasi con <i>va / vanno</i> + participio", "almeno due frasi con <i>si può / si deve</i> + infinito", "un consiglio finale (<i>Ti conviene…</i>)"]),
    cando="So spiegare regole e istruzioni con andare + participio e con si può / si deve + infinito.",
    nH="Prossima unità: <i>C'era una volta</i> (passato remoto nella narrazione; trapassato remoto).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 34 - Va fatto così")
