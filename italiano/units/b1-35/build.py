# Speak! Progresso B1 - Unità 35 "C'era una volta" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 35", audio_json=os.path.join(HERE, "audio_it-b1-unita-35.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-35", "35.1 C'era una volta", "35.2 Ripeti")

C = dict(
    nn="35", title="C'era una volta", subtitle="Storie di famiglia · <b>passato remoto, imperfetto, trapassato remoto</b>",
    cover=[("SAI FARE", "raccontare storie di famiglia e fatti lontani"),
           ("LINGUA", "passato remoto + imperfetto nel racconto · trapassato remoto: appena fu arrivato"),
           ("PRONUNCIA", "l'accento: parlò ≠ parlo · arrivarono")],
    t1="storie di famiglia",
    start=["Guarda la foto. Hai album di fotografie di famiglia? Chi li conserva?", "Conosci la storia dei tuoi nonni? Da dove venivano?",
           "Ti piace ascoltare le storie delle persone anziane? Perché?"],
    kw=[("il padre del nonno", "il bisnonno"), ("lasciare il proprio paese per vivere in un altro", "emigrare"),
        ("il piccolo negozio-laboratorio di un artigiano", "la bottega"), ("chi lavora il legno e fa mobili e porte", "il falegname"),
        ("il libro con le fotografie di famiglia", "l'album"), ("risparmiare soldi per il futuro", "mettere da parte")],
    use_words=["Che mestieri facevano i tuoi nonni o bisnonni?", "Per che cosa stai mettendo da parte dei soldi?"],
    n1=["A: <i>bottega</i> = negozio e laboratorio insieme (falegname, sarto, calzolaio); <i>mettere da parte</i> = risparmiare."],
    aims=["C'era una volta: le storie della signora Rossi · Parliamone", "il passato remoto nel racconto · il trapassato remoto (riconoscere)",
          "La storia della mia famiglia (35.2) · l'accento del passato remoto", "Il racconto per il giornalino · riscrivi · scrittura (100–150 parole)"],
    story="Domenica 14 novembre, a casa della signora Rossi, con Júlia e Davide (che ha portato su dalla cantina una scatola di foto). Il padre della signora nacque nel 1924 nell'Appennino; dopo la guerra venne a Bologna a piedi con una valigia di cartone e lavorò da un falegname in via Santo Stefano. Conobbe la madre, che lavorava nel forno di fronte, quando riparò la porta del forno. Si sposarono nel 1950; lui aprì una bottega e lei nacque due anni dopo, sopra la bottega. Júlia: il bisnonno partì dal Veneto a fine Ottocento, un mese di nave, piantagioni di caffè. Ciambella per tutti.",
    prob="Il portoghese ha un solo tempo, il pretérito perfeito (<i>nasceu, foi, chegou</i>), dove l'italiano ne ha due: il prossimo per i fatti vicini o legati al presente, il remoto per i fatti lontani e il racconto. Il brasiliano o evita il remoto, o appena lo impara lo usa anche per ieri (<s>stamattina andai</s>). Irregolari difficili: <i>nacque, venne, ebbe, ruppe</i> (<s>nascé</s>). Il trapassato remoto (<i>appena fu arrivato</i>) somiglia al mais-que-perfeito dei libri (<i>chegara</i>): basta riconoscerlo. E l'accento: <i>parlò</i> ≠ <i>parlo</i>.",
    real="Tra il 1875 e il 1920 più di un milione di italiani emigrarono in <b>Brasile</b>, moltissimi dal <b>Veneto</b>: il viaggio in nave durava settimane e molti lavorarono nelle piantagioni di caffè. Il <b>passato remoto</b> si usa nei libri, nelle fiabe e nei racconti storici; nel parlato è frequente in Toscana e al Sud, mentre al Nord si preferisce il passato prossimo. A Bologna la <b>ciambella</b> è il dolce tradizionale di famiglia.",
    tr=("C'era una volta", "Ripeti: il passato remoto"),
    gist=("Domenica pomeriggio, a casa della signora Rossi. Ascolta. Di che cosa parlano?",
          ["di storie di famiglia del passato", "dei progetti per Natale", "di un viaggio in Veneto"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il padre della signora Rossi arrivò a Bologna in treno.", "F"), ("La madre lavorava in un forno.", "V"),
             ("I genitori si conobbero quando lui riparò la porta del forno.", "V"), ("Si sposarono nel 1960.", "F"),
             ("Il bisnonno di Júlia emigrò in Brasile alla fine dell'Ottocento.", "V"), ("Il viaggio in nave durò una settimana.", "F")]),
    talk2=["Quale storia ti è piaciuta di più: quella della signora Rossi o quella di Júlia? Perché?", "Che cosa vuol dire, secondo te, «la storia fa dei giri strani»?",
           "Nella tua famiglia ci sono storie d'amore o di viaggi come queste?"],
    n2=["B: 1 a piedi · 4 nel 1950 · 6 un mese.", "Ripresa: la signora Rossi è cresciuta in via Santo Stefano; il nonno Antonio di Júlia parlava veneto e faceva la polenta (A2)."],
    gref="narrazione_passato_remoto",
    t4="nacque, venne, si sposarono",
    pA=("Completa con il passato remoto del verbo tra parentesi.",
        [("Mio padre ___ (nascere) nel 1924.", "nacque"), ("Dopo la guerra ___ (venire) a Bologna a piedi.", "venne"),
         ("Un giorno la porta del forno si ___ (rompere).", "ruppe"), ("I miei genitori si ___ (sposare) nel 1950.", "sposarono"),
         ("Il viaggio in nave ___ (durare) un mese.", "durò")]),
    pAw="26mm",
    pB=[("Appena ", ["fu arrivato", "ebbe arrivato"], "fu arrivato", " in città, cercò lavoro."),
        ("Quando ", ["ebbe messo", "fu messo"], "ebbe messo", " da parte i soldi, aprì una bottega."),
        ("Mentre il bisnonno ", ["attraversava", "attraversò"], "attraversava", " l'oceano, scriveva un diario.")],
    rule="Nel racconto di fatti lontani: <b>passato remoto</b> per le azioni (<i>nacque, venne, si sposarono</i>), <b>imperfetto</b> per lo sfondo (<i>lavorava nel forno</i>). Fatto subito prima, dopo <i>appena, dopo che, quando</i> + passato remoto → <b>trapassato remoto</b>: <i>appena fu arrivato, quando ebbe messo da parte</i> (soprattutto scritto: basta riconoscerlo).",
    use=["Dove e quando nacquero i tuoi nonni? Rispondi con il passato remoto.", "Come si conobbero i tuoi genitori (o due persone che conosci)?",
         "C'è un emigrante nella tua famiglia? Da dove partì? Dove arrivò?", "Racconta l'inizio di una fiaba: <i>C'era una volta… Un giorno…</i>",
         "Che cosa si faceva la domenica a casa dei tuoi nonni? (imperfetto)"],
    n4="A: <i>nacque, venne, ruppe</i> sono irregolari. B1–2: con i verbi di movimento l'ausiliare è <i>essere</i> (<i>fu arrivato</i>); B3: <i>mentre</i> + imperfetto.",
    t5="la storia della mia famiglia",
    fl=(["cominciare un racconto", "mettere in ordine i fatti", "dare lo sfondo", "reagire"],
        ["C'era una volta… · Tanti anni fa… · Si racconta che…", "Un giorno… · Appena… · Dopo che… · Alla fine…",
         "Allora non c'era… · Era un periodo in cui… · Ogni mattina…", "Che bella storia! · Davvero? · E poi? · Che romantico!"]),
    pron=("Nel passato remoto l'accento cambia il significato: <i>parl<b>ò</b></i> (lui, tanto tempo fa) ≠ <i>p<b>a</b>rlo</i> (io, adesso); <i>arriv<b>ò</b>, lavor<b>ò</b>, dur<b>ò</b></i>. Alla terza plurale l'accento cade sulla terzultima sillaba: <i>arriv<b>a</b>rono, si spos<b>a</b>rono</i>.",
          "Ascolta e ripeti. Poi leggi: «Si sposarono nel 1950, nella chiesa di Santo Stefano.»"),
    task=("La storia della mia famiglia: racconta all'insegnante una storia della tua famiglia (come si conobbero due persone, un trasloco, un emigrante, un mestiere di una volta). Passato remoto per i fatti, imperfetto per lo sfondo. Poi l'insegnante racconta una storia e tu fai le domande.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>chi erano</li><li>dove vivevano</li><li>che lavoro facevano</li><li>che cosa successe</li><li>come si conobbero</li><li>come finì la storia</li></ul>",
          "Insegnante: E dove nacque? · Come si conobbero? · E poi che cosa successe? Lo studente: Mio nonno nacque… · Un giorno… · Appena arrivò… · Allora non c'era… Correggere l'accento (<i>parlò</i>) e gli irregolari (<i>nacque, venne, fece</i>)."),
    talk5=["Quali storie di famiglia si raccontano a casa tua, alle feste?", "Conosci la storia dei tuoi antenati? Ti piacerebbe saperne di più?"],
    n5=["far sentire l'accento finale (<i>parlò</i>) e quello della terza plurale.", "Pretendere almeno cinque verbi al passato remoto e due all'imperfetto; accettare il prossimo nel parlato, ma far notare la differenza."],
    hA=("Il racconto della signora Rossi per il giornalino del quartiere. Scegli la forma giusta.",
        "<i>Mio padre {0} nel 1924 in un paesino dell'Appennino. Dopo la guerra venne a Bologna: appena {1} arrivato, trovò lavoro da un falegname. Mia madre {2} nel forno di fronte. Un giorno la porta del forno si ruppe e lui la riparò: così si {3}. Si sposarono nel 1950 e due anni dopo {4} io, sopra la bottega di via Santo Stefano.</i>",
        [(["nacque", "nasceva"], "nacque"), (["fu", "ebbe"], "fu"), (["lavorava", "lavorò"], "lavorava"),
         (["conobbero", "conoscevano"], "conobbero"), (["nacqui", "nascevo"], "nacqui")]),
    hB=("Riscrivi le frasi al passato remoto.",
        [("Il bisnonno è partito dal Veneto alla fine dell'Ottocento.", "Il bisnonno partì dal Veneto alla fine dell'Ottocento."),
         ("Il viaggio è durato un mese.", "Il viaggio durò un mese."),
         ("Ha lavorato nelle piantagioni di caffè e non è più tornato in Italia.", "Lavorò nelle piantagioni di caffè e non tornò più in Italia.")]),
    watch=[("Mio padre nascé nel 1924.", "Mio padre nacque nel 1924.", "<i>nascere</i> è irregolare: <i>nacqui, nacque, nacquero</i>."),
           ("Appena ebbe arrivato, cercò lavoro.", "Appena fu arrivato, cercò lavoro.", "con i verbi di movimento: <i>essere</i>."),
           ("Stamattina andai al bar.", "Stamattina sono andata al bar.", "per un fatto di oggi: passato prossimo.")],
    write=("Racconta una storia della tua famiglia (i nonni, un emigrante, come si conobbero i tuoi genitori) per un giornalino o un blog.",
           "Tanti anni fa…", ["almeno sei verbi al passato remoto e tre all'imperfetto", "espressioni di tempo (<i>appena, dopo che, un giorno, alla fine</i>)", "una frase finale: che cosa significa per te questa storia"]),
    cando="So raccontare storie di famiglia e fatti lontani con il passato remoto e l'imperfetto, e riconosco il trapassato remoto.",
    nH="Prossima unità: <i>Finita la festa…</i> (participio passato assoluto).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 35 - C'era una volta")
