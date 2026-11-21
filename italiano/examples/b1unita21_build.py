# Speak! Progresso B1 - Unità 21 "Il lavoro che cambia" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 21", audio_json=os.path.join(HERE, "audio_it-b1-unita-21.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-21", "21.1 Il lavoro che cambia", "21.2 Ripeti")

C = dict(
    nn="21", title="Il lavoro che cambia", subtitle="Smart working e ufficio · <b>il quale, il cui, chi, quello che</b>",
    cover=[("SAI FARE", "parlare di come cambia il lavoro, confrontare casa e ufficio, descrivere il lavoro ideale"),
           ("LINGUA", "Chi vuole… · i clienti, i cui progetti… · una collega, la quale… · quello che non capisco…"),
           ("PRONUNCIA", "cui, qui, chi: tre suoni diversi")],
    t1="il lavoro",
    start=["Guarda la foto. Dove lavora questa persona? Ti piacerebbe lavorare così?", "Lavori da casa, in ufficio o tutti e due?",
           "Che cosa è cambiato nel tuo lavoro negli ultimi anni?"],
    kw=[("lavorare da casa, con il computer", "lo smart working"), ("il tavolo dove lavori", "la scrivania"),
        ("una persona che lavora con te", "un collega / una collega"), ("un incontro di lavoro con altre persone", "una riunione"),
        ("nello stesso posto, non online", "in presenza"), ("il capo di uno studio o di un'azienda", "il titolare")],
    use_words=["Preferisci le riunioni online o in presenza? Perché?", "Com'è la tua scrivania? Che cosa c'è sopra?"],
    n1=["A: in Italia si dice <i>smart working</i> (la legge dice <i>lavoro agile</i>); <i>home office</i> non si usa. <i>Titolare</i> = <i>dono</i> (di un'attività)."],
    aims=["Il lavoro che cambia: la mail del capo · Parliamone", "I pronomi relativi: il quale, il cui, chi, quello che",
          "Casa o ufficio? (21.2) · il lavoro ideale e un capo scettico", "La mail del capo · i relativi · scrittura (100–150 parole)"],
    story="Mercoledì 9 giugno, mattina, allo studio. Marco e Júlia leggono una mail del capo: da luglio chi vuole può lavorare da casa il lunedì e il venerdì (Júlia lo chiedeva da un anno). I tre nuovi clienti arrivati dopo l'articolo sulla biblioteca, i cui progetti cominciano a luglio, saranno seguiti da un gruppo di tre architetti: Júlia, Marco e una nuova collega che arriva da Torino lunedì 14 giugno (il capo non aveva detto niente). Marco non ama lo smart working: la casa è il posto in cui dorme. Júlia è contenta: la sua scrivania è davanti alla finestra da cui si vedono i colli (e la signora Rossi passa con i biscotti). Le riunioni del mercoledì restano in presenza; chi arriva in ritardo porta le paste.",
    prob="Il portoghese ha gli stessi relativi (<i>o qual, cujo, quem, o que</i>), ma il brasiliano parlato usa quasi solo <i>que</i>: lo studente dice <i>la collega che ho parlato</i> (<i>a colega que eu falei</i>) ed evita <i>il cui</i>. Altri errori: <i>il cui</i> senza articolo (calco di <i>cujo</i>) o con l'articolo sbagliato, e <i>chi</i> con il verbo al plurale. Lessico: <i>home office</i> → <i>smart working, lavoro da casa</i>.",
    real="In Italia il lavoro da casa si chiama <i>lavoro agile</i> nella legge (n. 81 del 2017), ma tutti dicono <i>smart working</i>, un'espressione che in inglese non si usa in questo senso. Molte aziende oggi alternano giorni in ufficio e giorni a casa. Nelle riunioni italiane, chi arriva in ritardo spesso porta le paste o i cornetti per tutti.",
    tr=("Il lavoro che cambia", "Ripeti: i pronomi relativi"),
    gist=("Mercoledì mattina, allo studio. Ascolta. Di che cosa parla la mail del capo?",
          ["di smart working, nuovi progetti e una nuova collega", "di un trasloco dello studio a Torino", "delle ferie d'estate"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Da luglio tutti devono lavorare da casa.", "F"), ("I progetti dei nuovi clienti cominciano a luglio.", "V"),
             ("La nuova collega arriva da Milano.", "F"), ("Il capo aveva già parlato della nuova collega.", "F"),
             ("Dalla scrivania di Júlia si vedono i colli.", "V"), ("Le riunioni del mercoledì restano in presenza.", "V")]),
    talk2=["Perché Marco non vuole lavorare da casa?", "«Chi arriva in ritardo porta le paste.» Ti sembra una buona regola?",
           "Secondo te, come sarà la nuova collega?"],
    n2=["B: 1 solo chi vuole, il lunedì e il venerdì · 3 da Torino · 4 non aveva detto niente.", "I tre nuovi clienti sono arrivati dopo l'articolo sulla biblioteca (unità 16)."],
    gref="relativi_b1",
    t4="i pronomi relativi",
    pA=("Completa con il relativo giusto: chi, il cui / la cui / i cui, il quale / la quale, quello che, in cui.",
        [("___ arriva tardi porta le paste.", "Chi"), ("È una collega ___ ufficio è a Torino.", "il cui"),
         ("Ho parlato con il cliente, ___ era molto contento.", "il quale"), ("Non è ___ volevo dire.", "quello che"),
         ("Questo è lo studio ___ lavoro da tre anni.", "in cui")]),
    pAw="22mm",
    pB=[("La collega ", ["con cui", "che"], "con cui", " ho parlato è simpatica."),
        ("Chi ", ["lavora", "lavorano"], "lavora", " da casa risparmia tempo."),
        ("Il cliente, ", ["la cui", "il cui"], "la cui", " casa è a Modena, è arrivato.")],
    rule="<b>Chi</b> = la persona che (verbo al singolare). <b>Il quale / la quale</b> = che o cui, più formale (<i>con il quale = con cui</i>). <b>Il cui / la cui / i cui / le cui</b> = possesso: l'articolo concorda con la cosa posseduta (<i>il cliente, la cui casa</i>). <b>Quello che</b> = la cosa che.",
    use=["Descrivi il tuo lavoro ideale: <i>un lavoro in cui…</i>", "Un collega con il quale lavori bene: com'è?",
         "Completa: <i>Quello che mi piace del mio lavoro è…</i>", "Un proverbio: <i>Chi dorme non piglia pesci.</i> Che cosa vuol dire?",
         "Un'azienda o un negozio il cui nome ti piace: perché?"],
    n4="B3: l'articolo concorda con <i>casa</i>, non con <i>cliente</i>.",
    t5="casa o ufficio?",
    fl=(["vantaggi", "svantaggi", "il lavoro ideale", "trovare un compromesso"],
        ["Quello che mi piace è… · Si risparmia tempo. · Chi lavora da casa…", "Il problema è che… · Ci si sente soli. · Non si stacca mai.",
         "Un lavoro in cui… · Un capo il cui… · Colleghi con i quali…", "Due giorni a casa e tre in ufficio. · Dipende dal lavoro. · L'importante è…"]),
    pron=("Tre parole simili, tre suoni diversi: <b>cui</b> = <i>KU-i</i> (si sentono la <i>u</i> e la <i>i</i>), <b>qui</b> = <i>KWI</i> (una sillaba), <b>chi</b> = <i>KI</i> (senza <i>u</i>). <i>Il posto in <b>cui</b> lavoro è <b>qui</b>. <b>Chi</b> viene?</i>",
          "Ascolta e ripeti. Poi leggi: «Chi è qui? È la collega di cui parlavi.»"),
    task=("Casa o ufficio? Descrivi il tuo lavoro ideale con almeno cinque relativi (un posto in cui…, colleghi con i quali…, un capo il cui…). Poi l'insegnante è un capo scettico che non vuole lo smart working: convincilo con almeno tre argomenti e trovate un compromesso.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>il tempo per arrivare</li><li>la concentrazione</li><li>i colleghi</li><li>le riunioni</li><li>i costi</li><li>la vita privata</li></ul>",
          "Insegnante (capo): Chi lavora da casa lavora meno! · E le riunioni? · Come controllo quello che fate? · I clienti vogliono vedervi. Lo studente risponde: Quello che conta sono i risultati… · Chi perde due ore in macchina… · Le riunioni in cui… Alla fine: proposta di compromesso (due giorni a casa)."),
    talk5=["Lo smart working è possibile nel tuo lavoro? Perché?", "Chi lavora da casa lavora di più o di meno?"],
    n5=["far sentire la differenza con le mani: <i>cui</i> due battiti, <i>qui</i> e <i>chi</i> uno.", "Pretendere almeno cinque relativi diversi; correggere subito <i>la collega che ho parlato</i>."],
    hA=("La mail completa del capo. Scegli la forma giusta.",
        "<i>Cari tutti, da luglio cambiamo organizzazione. {0} vuole potrà lavorare da casa il lunedì e il venerdì. I tre nuovi clienti, {1} progetti cominciano a luglio, saranno seguiti da Júlia, Marco e da una nuova collega, {2} arriva da Torino lunedì 14. La scrivania {3} lavorerà è quella vicino alla finestra. {4} vi chiedo è solo di non mancare alle riunioni del mercoledì. Buona giornata!</i>",
        [(["Chi", "Che"], "Chi"), (["i cui", "che i"], "i cui"), (["la quale", "il quale"], "la quale"),
         (["a cui", "in cui"], "a cui"), (["Quello che", "Che"], "Quello che")]),
    hB=("Unisci le due frasi con un relativo.",
        [("Ho una collega. Il suo ufficio è a Torino.", "Ho una collega il cui ufficio è a Torino."), ("Questo è lo studio. Lavoro nello studio da tre anni.", "Questo è lo studio in cui lavoro da tre anni."),
         ("Ho parlato con il capo. Il capo era di buon umore.", "Ho parlato con il capo, il quale era di buon umore.")]),
    watch=[("La collega che ho parlato.", "La collega con cui ho parlato.", "con la preposizione: <i>cui</i> / <i>il quale</i>."),
           ("Chi vogliono, possono restare.", "Chi vuole, può restare.", "<i>chi</i> + verbo al singolare."),
           ("Lavoro in home office.", "Lavoro da casa / in smart working.", "<i>home office</i> non si usa.")],
    write=("Il lavoro che cambia: com'è cambiato il tuo lavoro (o il lavoro di una persona che conosci) negli ultimi anni? Che cosa è meglio e che cosa è peggio?",
           "Il lavoro in cui…", ["cinque pronomi relativi diversi (<i>chi, il quale, il cui, quello che, in cui</i>)", "un vantaggio e uno svantaggio", "una proposta per il futuro"]),
    cando="So parlare di come cambia il lavoro e descrivere persone, posti e cose con i pronomi relativi.",
    nH="Prossima unità: <i>Spettabile…</i> (lettere formali e reclami).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 21 - Il lavoro che cambia")
