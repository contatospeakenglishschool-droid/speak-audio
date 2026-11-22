# Speak! Progresso B1 - Unità 26 "Viaggio in Sicilia" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 26", audio_json=os.path.join(HERE, "audio_it-b1-unita-26.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-26", "26.1 Viaggio in Sicilia", "26.2 Ripeti")

C = dict(
    nn="26", title="Viaggio in Sicilia", subtitle="Storia e viaggi · <b>il passato remoto</b>",
    cover=[("SAI FARE", "capire una visita guidata, raccontare la storia di un luogo o di una persona, scrivere una breve biografia"),
           ("LINGUA", "fu costruito · creò · volle · nacque a… · visse a… · lo fece costruire"),
           ("PRONUNCIA", "parlo / parlò: l'accento che cambia il tempo")],
    t1="la storia",
    start=["Guarda la foto. Dove siamo? Che cosa sai della Sicilia?", "Ti piacciono le visite guidate o preferisci visitare da solo/a?",
           "Qual è il monumento più antico della tua città?"],
    kw=[("un giro in un museo o in una città con un esperto", "la visita guidata"), ("diventare re con una cerimonia", "essere incoronato"),
        ("una piccola chiesa dentro un palazzo", "la cappella"), ("un'immagine fatta con piccole pietre colorate", "il mosaico"),
        ("un luogo protetto per tutta l'umanità", "il patrimonio UNESCO"), ("riso fritto ripieno, tipico siciliano", "l'arancina / l'arancino")],
    use_words=["Hai mai visto un mosaico antico? Dove?", "Quali luoghi del tuo paese sono patrimonio UNESCO?"],
    n1=["A: a Palermo si dice <i>arancina</i>, a Catania <i>arancino</i>: un piccolo dibattito nazionale."],
    aims=["Viaggio in Sicilia: la visita guidata di Bruno e Chiara · Parliamone", "Il passato remoto: regolari, irregolari (1-3-3), quando si usa",
          "Racconta una storia (26.2) · parlo / parlò", "La cartolina di Chiara · una biografia · scrittura (100–150 parole)"],
    story="Mercoledì 14 luglio, Palermo. Bruno e Chiara (partiti il 12 luglio) fanno una visita guidata al Palazzo dei Normanni. La guida racconta al passato remoto: il palazzo fu costruito dagli arabi e trasformato dai normanni; nel 1130 Ruggero II fu incoronato re; volle la Cappella Palatina, con artisti greci, arabi e latini; nel 2015 la Palermo arabo-normanna diventò patrimonio UNESCO. Bruno (studente di storia) chiede di Federico II: nacque a Jesi ma visse a Palermo da bambino; la guida scherza: «La prossima visita la fa Lei!». Più tardi, in un bar vicino al mercato di Ballarò, Chiara nota che il barista usa il passato remoto anche per ieri; prova anche lei («stamattina mangiai un arancino») e Bruno la corregge: a Palermo si dice arancina. Domani: Monreale la mattina e il mare il pomeriggio.",
    prob="Il pretérito perfeito portoghese copre sia il passato prossimo sia il remoto, quindi lo studente non sente la differenza e a volte usa il remoto per ieri (corretto solo in Sicilia e nel Sud). Al B1 l'obiettivo è <b>riconoscere</b> il remoto (storia, letteratura, biografie) e usare la terza persona. Errori tipici: dimenticare l'accento (<i>parlo</i> per <i>parlò</i>), regolarizzare gli irregolari (<i>nascé</i> per <i>nacque</i>, <i>facé</i> per <i>fece</i>).",
    real="La <b>Palermo arabo-normanna</b> (con le cattedrali di Cefalù e Monreale) è patrimonio UNESCO dal 2015: chiese e palazzi uniscono arte araba, bizantina e normanna. A Palermo si dice <b>arancina</b>, a Catania e nella Sicilia orientale <b>arancino</b>. In Sicilia molte persone usano il passato remoto anche nel parlato di tutti i giorni (<i>ieri andai al mare</i>), mentre al Nord si usa quasi solo nello scritto.",
    tr=("Viaggio in Sicilia", "Ripeti: il passato remoto"),
    gist=("Palermo, una visita guidata. Ascolta. Di che cosa parla la guida?",
          ["della storia del palazzo e dei re normanni", "dei migliori ristoranti di Palermo", "della storia della mafia"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il palazzo fu costruito dai normanni e poi trasformato dagli arabi.", "F"), ("Ruggero II fu incoronato re nel 1130.", "V"),
             ("Nella Cappella Palatina lavorarono solo artisti greci.", "F"), ("Federico II nacque a Palermo.", "F"),
             ("Il barista usa il passato remoto anche per ieri.", "V"), ("A Palermo si dice arancina.", "V")]),
    talk2=["Perché secondo Bruno la guida usa il passato remoto?", "Ti piacerebbe fare questa visita? Perché?",
           "Arancina o arancino: conosci altre parole che cambiano da una regione all'altra?"],
    n2=["B: 1 dagli arabi, poi dai normanni · 3 greci, arabi e latini · 4 a Jesi (Marche).", "Bruno e Chiara sono partiti il 12 luglio (unità 24)."],
    gref="passato_remoto",
    t4="il passato remoto",
    pA=("Completa con il passato remoto (terza persona) del verbo tra parentesi.",
        [("Nel 1130 Ruggero II ___ (essere) incoronato re di Sicilia.", "fu"), ("Ruggero ___ (volere) una cappella tutta per sé.", "volle"),
         ("Gli artisti ___ (lavorare) insieme per anni.", "lavorarono"), ("Federico II ___ (nascere) a Jesi nel 1194.", "nacque"),
         ("Guglielmo II ___ (fare) costruire il duomo di Monreale.", "fece")]),
    pAw="24mm",
    pB=[("Stamattina ", ["ho mangiato", "mangiai"], "ho mangiato", " un'arancina (a Bologna)."),
        ("Dante ", ["nascé", "nacque"], "nacque", " a Firenze nel 1265."),
        ("Quella sera la ragazza ", ["parlò", "parlo"], "parlò", " a lungo con il barista.")],
    rule="<b>Passato remoto</b>: fatti storici o lontani, biografie, romanzi (<i>fu, creò, nacque</i>). <b>Passato prossimo</b>: fatti recenti o legati a oggi (<i>stamattina ho mangiato</i>). Regolari: <i>-ò, -é/-ette, -ì</i> (lui) · <i>-arono, -erono/-ettero, -irono</i> (loro). Irregolari: schema <b>1-3-3</b> (<i>feci, fece, fecero</i>).",
    use=["Racconta in tre frasi la storia della tua città (fu fondata…).", "Chi è un personaggio storico del tuo paese? Dove nacque? Che cosa fece?",
         "Conosci una favola? Comincia: <i>C'era una volta… Un giorno…</i>", "Che cosa hai fatto stamattina? (passato prossimo!)",
         "Di' tre forme del passato remoto che hai sentito nel dialogo."],
    n4="B1: fatto di oggi → passato prossimo; B3: racconto → <i>parlò</i> (accento).",
    t5="racconta una storia",
    fl=(["la nascita", "i fatti", "la fine", "il collegamento con oggi"],
        ["Nacque a… nel… · Crebbe a… · Era figlio/a di…", "Studiò… · Fece… · Fu il primo / la prima a…",
         "Morì a… · Visse fino a… anni.", "Oggi… · Ancora oggi si può vedere… · È famoso/a per…"]),
    pron=("Nel passato remoto la terza persona dei verbi regolari ha l'<b>accento sull'ultima sillaba</b>: <b>parlò</b>, <b>creò</b>, <b>arrivò</b>, <b>partì</b>. Senza accento è il presente di <i>io</i>: <b>parlo</b>, <b>creo</b>, <b>arrivo</b>, <b>parto</b>. Nello scritto l'accento è obbligatorio.",
          "Ascolta e ripeti. Poi leggi: «Io parlo con la guida. Ruggero parlò con gli artisti. Arrivo oggi. Arrivò nel 1130.»"),
    task=("Racconta una storia. Scegli un personaggio o un luogo (della lista o del tuo paese) e racconta la sua storia in cinque o sei frasi al passato remoto, come una guida. L'insegnante è un turista curioso e fa domande. Poi scambiate i ruoli: l'insegnante racconta, tu fai domande.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>un personaggio storico</li><li>un artista o uno scrittore</li><li>la tua città</li><li>un monumento famoso</li><li>un nonno o una nonna</li><li>un viaggio di molti anni fa</li></ul>",
          "Insegnante (turista): E dove nacque? · Che cosa fece di importante? · Quando morì? · E oggi che cosa resta? Quando racconta l'insegnante, usare almeno cinque irregolari (fu, ebbe, fece, disse, nacque, visse) e chiedere allo studente di riconoscerli."),
    talk5=["Nel tuo paese ci sono parole diverse da una regione all'altra? Fai un esempio.", "Per te, che cosa rende interessante una visita guidata?"],
    n5=["dettare quattro forme (parlo, parlò, arrivo, arrivò) e far scrivere l'accento.", "Accettare il passato prossimo nel parlato; pretendere il remoto solo nella biografia e nei racconti storici."],
    hA=("La cartolina di Chiara a Júlia. Scegli la forma giusta.",
        "<i>Cara Júlia, Palermo è meravigliosa! Ieri {0} una visita guidata al Palazzo dei Normanni: la guida ci ha raccontato che nel 1130 Ruggero II {1} incoronato re e che {2} costruire una cappella piena di mosaici d'oro. Bruno ha fatto mille domande: Federico II {3} a Jesi ma {4} a Palermo da bambino, lo sapevi? Domani Monreale e poi mare. Un bacio, Chiara</i>",
        [(["abbiamo fatto", "facemmo"], "abbiamo fatto"), (["fu", "fui"], "fu"), (["fece", "fa"], "fece"),
         (["nacque", "nascé"], "nacque"), (["visse", "vivé"], "visse")]),
    hB=("Riscrivi al passato prossimo, come si parla a Bologna.",
        [("Ieri andai al mare.", "Ieri sono andato/a al mare."), ("Stamattina arrivarono tanti turisti.", "Stamattina sono arrivati tanti turisti."),
         ("Ieri sera facemmo una passeggiata.", "Ieri sera abbiamo fatto una passeggiata.")]),
    watch=[("Federico nascé a Jesi.", "Federico nacque a Jesi.", "<i>nascere</i> è irregolare."),
           ("Lui parlo con la guida.", "Lui parlò con la guida.", "senza accento è il presente."),
           ("Stamattina mangiai un'arancina. (a Bologna)", "Stamattina ho mangiato un'arancina.", "fatto di oggi: passato prossimo.")],
    write=("Scrivi una breve biografia di un personaggio storico o di una persona della tua famiglia (un nonno, una nonna…) per una guida turistica o un album di famiglia.",
           "Nacque a… nel…", ["almeno sei verbi al passato remoto (tre irregolari)", "un'informazione con l'imperfetto (<i>era, aveva</i>)", "una frase finale su oggi (passato prossimo o presente)"]),
    cando="So capire una visita guidata e raccontare la storia di un luogo o di una persona con il passato remoto.",
    nH="Prossima unità: <i>Qualsiasi cosa</i> (qualsiasi, chiunque, dovunque + congiuntivo).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 26 - Viaggio in Sicilia")
