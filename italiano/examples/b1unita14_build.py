# Speak! Progresso B1 - Unità 14 "Se vincessi…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 14", audio_json=os.path.join(HERE, "audio_it-b1-unita-14.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-14", "14.1 Se vincessi...", "14.2 Ripeti")

C = dict(
    nn="14", title="Se vincessi…", subtitle="Sogni e ipotesi · <b>il periodo ipotetico della possibilità</b>",
    cover=[("SAI FARE", "fare ipotesi, parlare dei tuoi sogni, dare un consiglio"),
           ("LINGUA", "Se vincessi, comprerei… · Che cosa faresti se…? · Se fossi in te…"),
           ("PRONUNCIA", "la doppia s del congiuntivo: vinCESSi, aVESSi")],
    t1="i sogni",
    start=["Guarda la foto. Che cos'è? Hai mai giocato a un gioco così?", "Hai un sogno nel cassetto? Quale?",
           "Secondo te, i soldi fanno la felicità?"],
    kw=[("il foglio su cui scrivi i numeri del gioco", "una schedina"), ("il momento in cui escono i numeri vincenti", "l'estrazione"),
        ("il negozio dove compri francobolli, sigarette e giochi", "la tabaccheria"), ("il foglio che ricevi quando paghi", "la ricevuta"),
        ("dare un lavoro a qualcuno", "assumere"), ("una persona che sogna sempre", "un sognatore")],
    use_words=["Che cosa compri di solito in tabaccheria?", "Sei un sognatore o una persona con i piedi per terra?"],
    n1=["A: falso amico <i>assumere</i> = <i>contratar</i> (<i>assumir</i> un compito = <i>prendersi</i>, <i>assumersi</i>). <i>Un sogno nel cassetto</i> = <i>um sonho guardado</i>."],
    aims=["Se vincessi… Davide gioca al SuperEnalotto · Parliamone", "Il periodo ipotetico della possibilità: se + congiuntivo imperfetto + condizionale",
          "Fare ipotesi e dare consigli (14.2) · il gioco «E se…?»", "Il messaggio di Davide · dal tipo 1 al tipo 2 · scrittura (100–150 parole)"],
    story="Venerdì 26 marzo, sera, aperitivo al bar di Giulia. Davide arriva con una schedina del SuperEnalotto: stasera c'è l'estrazione, il jackpot è altissimo ed è la prima volta che gioca. Tutti dicono che cosa farebbero se vincessero: Davide una moto e il giro del Brasile (e poi finirebbe l'università… forse); Marco aprirebbe uno studio tutto suo e assumerebbe Júlia, ma pagandola di meno («Allora non verrei!»); Júlia comprerebbe un appartamento con terrazza sui tetti di Bologna e porterebbe qui i genitori ogni anno; Camila pagherebbe il biglietto a sua madre; Giulia non chiuderebbe mai il bar, ma prenderebbe un'altra barista e farebbe un mese in Sardegna. Marco: 1 possibilità su 622 milioni. Júlia: «Se fossi in te…». Finale: la tabaccheria era chiusa, Davide non ha mai giocato.",
    prob="La struttura è uguale al portoghese (<i>se eu ganhasse, compraria</i>), ma parlando in fretta il brasiliano mette il condizionale anche dopo <i>se</i> (<i>se vincerei, se avrei</i>) e traduce <i>se eu fosse você</i> con <i>se sarei te</i> invece di <i>se fossi in te</i>. Falsi amici: <i>assumere</i> = <i>contratar</i>; <i>sorte</i> = <i>destino</i> (la <i>sorte</i> brasiliana è la <i>fortuna</i>).",
    real="Il SuperEnalotto è il gioco a numeri più famoso d'Italia: si gioca in tabaccheria, in molti bar o online, e la probabilità di fare 6 è di circa 1 su 622 milioni. Il gioco equivalente in Brasile è la Mega-Sena. Quando il jackpot diventa altissimo, ne parlano i telegiornali e anche chi non gioca mai compra una schedina.",
    tr=("Se vincessi…", "Ripeti: se + congiuntivo imperfetto, condizionale"),
    gist=("Venerdì sera, aperitivo al bar di Giulia. Ascolta. Di che cosa parlano soprattutto?",
          ["di che cosa farebbero con tanti soldi", "di un problema al lavoro di Marco", "della vacanza di Giulia in Sardegna"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Davide gioca al SuperEnalotto ogni settimana.", "F"), ("Se vincesse, Davide farebbe il giro del Brasile in moto.", "V"),
             ("Marco assumerebbe Júlia, ma la pagherebbe di meno.", "V"), ("Se vincesse, Giulia chiuderebbe il bar.", "F"),
             ("Júlia vorrebbe un appartamento con una terrazza.", "V"), ("Davide ha pagato la schedina in tabaccheria.", "F")]),
    talk2=["Perché alla fine Davide dice che piangerebbe per un anno?", "Davide dice: «Se non giocassi, non potrei sognare». Sei d'accordo?",
           "Quale sogno ti sembra più bello: quello di Davide, di Júlia o di Giulia? Perché?"],
    n2=["B: 1 è la prima volta · 4 non lo chiuderebbe mai: prenderebbe un'altra barista · 6 la tabaccheria era chiusa.", "Parliamone 1: se uscissero i suoi numeri, non vincerebbe niente."],
    gref="periodo_ipotetico_2",
    t4="il periodo ipotetico",
    pA=("Completa con il congiuntivo imperfetto o il condizionale presente.",
        [("Se ___ (avere) più tempo, studierei il pianoforte.", "avessi"), ("Se Davide vincesse, ___ (comprare) una moto.", "comprerebbe"),
         ("Se ___ (essere) in te, non giocherei.", "fossi"), ("Che cosa faresti se ___ (potere) cambiare lavoro?", "potessi"),
         ("Se i miei genitori abitassero qui, li ___ (vedere) ogni domenica.", "vedrei")]),
    pB=[("Se vinco stasera, ", ["ti offro", "ti offrissi"], "ti offro", " la cena. (è probabile!)"),
        ("Se ", ["avessi", "avrei"], "avessi", " una terrazza, farei una festa ogni sabato."),
        ("Se fossi ricca, ", ["porterei", "portassi"], "porterei", " qui i miei genitori.")],
    rule="Condizione <b>poco probabile o impossibile</b> → <b>se + congiuntivo imperfetto</b>, conseguenza al <b>condizionale presente</b>: <i>se vincessi, comprerei</i>. Condizione <b>probabile</b> → <b>se + presente</b>: <i>se vinco, ti offro la cena</i>. Dopo <i>se</i> <b>mai il condizionale</b>. Per un consiglio: <i>Se fossi in te…</i>",
    use=["Se vincessi un milione, che cosa faresti per prima cosa? <i>Se vincessi…</i>", "Se potessi vivere in un'altra città, quale sceglieresti?",
         "Se fossi il sindaco della tua città, che cosa cambieresti?", "Un amico vuole lasciare il lavoro. Dagli un consiglio: <i>Se fossi in te…</i>",
         "Se domani avessi un giorno libero, come lo passeresti?"],
    n4="B1: <i>se vinco</i> = è probabile (tipo 1) → presente. Chiedere sempre la frase completa, con le due parti.",
    t5="ipotesi e sogni",
    fl=(["fare un'ipotesi", "sognare", "dare un consiglio", "essere realisti"],
        ["E se…? · Che cosa faresti se…? · Immagina di…", "Se potessi, … · Il mio sogno sarebbe… · Mi piacerebbe tanto…",
         "Se fossi in te, … · Al posto tuo, … · Io non lo farei.", "Magari! · È solo un sogno. · Con i piedi per terra…"]),
    pron=("Nel congiuntivo imperfetto la <b>s è doppia</b>: <i>vin<b>CES</b>si, a<b>VES</b>si, po<b>TES</b>si</i>. Nel condizionale l'accento cade su <b>-REI</b>: <i>compre<b>REI</b>, sa<b>REI</b></i>. La parte con <i>se</i> sale, la conseguenza scende.",
          "Ascolta e ripeti. Poi completa a voce: «Se vincessi…»."),
    task=("Il gioco «E se…?». L'insegnante legge una domanda alla volta: rispondi con almeno due frasi e spiega perché. Poi fai tu le domande all'insegnante, che ti racconta un suo sogno: dagli un consiglio con «Se fossi in te…».",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>…vincessi un milione?</li><li>…parlassi tutte le lingue?</li><li>…fossi invisibile per un giorno?</li><li>…non dovessi lavorare?</li><li>…potessi vivere in un'altra epoca?</li><li>…avessi una casa in Italia?</li></ul>",
          "Insegnante: Che cosa faresti se vincessi un milione? · E se parlassi tutte le lingue? … Poi l'insegnante racconta: «Vorrei lasciare il lavoro e aprire un bar a Bologna». Lo studente: Se fossi in te, prima farei un corso… · Al posto tuo, non lascerei subito il lavoro…"),
    talk5=["I soldi fanno la felicità?", "Giochi alla Mega-Sena o ad altre lotterie? Perché sì o perché no?"],
    n5=["far sentire la doppia s battendo due colpi sul tavolo: <i>vin-CES-si</i>.", "Chiedere un <i>perché</i> per ogni risposta; correggere subito <i>se vincerei</i>."],
    hA=("Sabato mattina Davide scrive a Camila. Scegli la forma giusta.",
        "<b>Davide:</b> Camila, ieri sera sono usciti tre dei miei numeri! Con tre numeri non sarei diventato ricco, ma che rabbia! E ho buttato la schedina: se l'{0} ancora, la metterei in cornice. Ho deciso: se lunedì la tabaccheria {1} aperta, gioco di nuovo. Júlia dice che se {2} in me, metterebbe i soldi in banca. Ma se tutti {3} come Júlia, il mondo {4} proprio noioso!",
        [(["avessi", "avrei"], "avessi"), (["è", "fosse"], "è"), (["fosse", "sarebbe"], "fosse"),
         (["fossero", "sarebbero"], "fossero"), (["sarebbe", "fosse"], "sarebbe")]),
    hB=("Trasforma: la condizione diventa poco probabile.",
        [("Se ho tempo, vengo alla festa.", "Se avessi tempo, verrei alla festa."), ("Se Davide vince, compra una moto.", "Se Davide vincesse, comprerebbe una moto."),
         ("Se siamo liberi, andiamo al mare.", "Se fossimo liberi, andremmo al mare.")]),
    watch=[("Se vincerei, comprerei una casa.", "Se vincessi, comprerei una casa.", "dopo <i>se</i> mai il condizionale."),
           ("Se sarei te, non giocherei.", "Se fossi in te, non giocherei.", "consiglio: <i>se fossi in te</i>."),
           ("Davide ha avuto molta sorte.", "Davide ha avuto molta fortuna.", "<i>sorte</i> = destino."),],
    write=("Se vincessi alla lotteria: che cosa faresti con i soldi? Che cosa cambieresti nella tua vita e che cosa non cambieresti mai?",
           "Se vincessi alla lotteria, la prima cosa che farei…", ["cinque periodi ipotetici (se + congiuntivo imperfetto + condizionale)", "una cosa che non cambieresti (<i>non… mai</i>)", "un'espressione realista (<i>Magari! · È solo un sogno</i>)"]),
    cando="So fare ipotesi poco probabili, parlare dei miei sogni e dare un consiglio con «se fossi in te».",
    nH="Prossima unità: <i>Arrivano i genitori</i> (il gerundio).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 14 - Se vincessi")
