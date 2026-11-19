# Speak! Progresso B1 - Unità 08 "Mica male!" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 08", audio_json=os.path.join(HERE, "audio_it-b1-unita-08.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-08", "08.1 Mica male!", "08.2 Ripeti")

C = dict(
    nn="08", title="Mica male!", subtitle="L'italiano parlato · <b>la negazione rafforzata</b>",
    cover=[("SAI FARE", "dire di no con forza, dare giudizi informali, reagire con le parole del parlato"),
           ("LINGUA", "Non è mica piccola. · Non è affatto il mio stile. · Non c'è neanche un piatto. · Neanch'io!"),
           ("PRONUNCIA", "l'accento sulla parola che nega")],
    t1="la lingua di tutti i giorni",
    start=["Guarda la foto. Che registro usano queste amiche: formale o informale?", "Quali parole usi solo con gli amici, in portoghese?",
           "Quando visiti una casa, che cosa controlli per prima cosa?"],
    kw=[("dove si lavano i piatti in cucina", "il lavandino"), ("il sistema che scalda la casa d'inverno", "il riscaldamento"),
        ("il pulsante che suona alla porta", "il campanello"), ("il ristorante economico dell'università", "la mensa"),
        ("il contrario di allegro e scherzoso", "serio"), ("fare un sorriso", "sorridere")],
    use_words=["Com'è il riscaldamento (o l'aria condizionata) a casa tua?", "Conosci una persona molto seria? Com'è?"],
    n1=["A: <i>il lavandino</i> = <i>a pia</i>; <i>il campanello</i> = <i>a campainha</i>; <i>la mensa</i> = <i>o bandejão</i>."],
    aims=["Mica male! Il primo candidato per la stanza di Bruno · Parliamone", "La negazione rafforzata: mica, affatto, per niente, neanche, nemmeno",
          "L'accento sulla negazione (08.2) · gioco di ruolo: un candidato pignolo", "Il messaggio di Tommaso · anch'io o neanch'io? · scrittura (100–150 parole)"],
    story="Sabato 6 febbraio, pomeriggio, in via Zamboni. Bruno ha pulito tutto («non c'è neanche un piatto nel lavandino») e Júlia è venuta ad aiutarlo. Arriva il primo candidato, Tommaso, studente di Medicina: la stanza «non è mica piccola», il tappeto blu di Paolo «non è affatto il suo stile», la vicina del piano di sopra ha novant'anni e non sente nemmeno il campanello. Tommaso non fuma, non fa feste e non sa neanche cucinare: mangia alla mensa. Per Bruno è perfetto; per Júlia è un po' troppo serio.",
    prob="Calco di <i>eu também não</i>: lo studente dice <i>anche io no</i> invece di <i>neanch'io</i>, e <i>anche a me no</i> invece di <i>neanche a me</i>. Falsi amici forti: <i>affatto</i> (= per niente) ≠ <i>de fato</i> (= <i>infatti</i>); <i>uffa</i> (noia) ≠ <i>ufa</i> (sollievo). La doppia negazione brasiliana (<i>não é pequeno não</i>) aiuta a capire <i>non è mica piccolo</i>.",
    real="<i>Mica</i> viene dal latino <i>mica</i> = briciola: «non è mica» = «non è neanche una briciola». È molto usato al Nord e al Centro. Le mense universitarie offrono un pasto completo a pochi euro. <i>Boh</i>, <i>mah</i> e <i>uffa</i> si usano in tutta Italia, ma solo nel registro informale.",
    tr=("Mica male!", "Ripeti: la negazione rafforzata"),
    gist=("Sabato pomeriggio, a casa di Bruno. Ascolta. Di che cosa parlano soprattutto?",
          ["della stanza di Paolo e del nuovo candidato", "di un esame di Tommaso", "di una festa di compleanno"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Quando arriva Tommaso, la cucina è sporca.", "F"), ("A Tommaso la stanza sembra piccola.", "F"),
             ("A Tommaso piace molto il tappeto blu.", "F"), ("La vicina del piano di sopra fa molto rumore.", "F"),
             ("Tommaso mangia quasi sempre alla mensa.", "V"), ("Secondo Júlia, Tommaso è un po' troppo serio.", "V")]),
    talk2=["Júlia dice «Mica tanto!». Che cosa pensa delle feste di Bruno?", "Tu prenderesti Tommaso come coinquilino? Perché?",
           "Che cosa non sopporteresti mai in un coinquilino?"],
    n2=["B: 1 non c'è neanche un piatto · 2 non è mica piccola · 3 non è affatto il suo stile · 4 non sente nemmeno il campanello.", "<i>Ah, però</i> = sorpresa positiva; <i>Che te ne pare?</i> = <i>o que você achou?</i>"],
    gref="negazione_rinforzata",
    t4="la negazione rafforzata",
    pA=("Reagisci con anch'io, neanch'io, anche a me o neanche a me.",
        [("Non fumo. — ___", "Neanch'io."), ("Mi piace cucinare. — ___", "Anche a me."),
         ("Non mi piacciono le feste. — ___", "Neanche a me."), ("Studio tutte le sere. — ___", "Anch'io."),
         ("Non sono mai stato a Torino. — ___", "Neanch'io.")]),
    pB=[("", ["Neanche", "Non neanche"], "Neanche", " Marco lo sapeva."),
        ("La stanza ", ["non è mica", "mica non è"], "non è mica", " piccola!"),
        ("Non ho ", ["nemmeno", "neanche non"], "nemmeno", " un euro in tasca.")],
    rule="<b>non + verbo + mica / affatto / per niente / neanche / nemmeno / neppure</b>: <i>non è mica piccola, non è affatto il mio stile</i>. Se <i>mica</i> o <i>neanche</i> vengono <b>prima</b> del verbo, niente <i>non</i>: <i>Mica è un problema! · Neanche tu sorridevi.</i> <b>Neanch'io / neanche a me</b> = <i>eu também não</i>.",
    use=["La tua città è cara? Rispondi con <i>mica</i> o <i>per niente</i>.", "Una cosa che non sai neanche fare.", "Un film che non ti è piaciuto per niente.",
         "Giudica la tua ultima cena fuori: <i>Mica male! / Mica tanto…</i>", "L'insegnante dice: «Non bevo caffè». Reagisci e continua."],
    n4="Con <i>piacere</i> si risponde <i>anche a me / neanche a me</i>, non <i>neanch'io</i>.",
    t5="il candidato pignolo",
    fl=(["dire di no con forza", "giudizi informali", "sorprendersi", "essere d'accordo nel no"],
        ["Per niente! · Niente affatto! · Neanche per sogno!", "Mica male! · Mica tanto. · Non è un granché.",
         "Ah, però! · Ma va'! · Non ci credo!", "Neanch'io. · Neanche a me. · Nemmeno io."]),
    pron=("Nella negazione rafforzata l'accento forte va sulla parola che nega: <i>non è <b>MI</b>ca piccola · non è af<b>FAT</b>to il mio stile · non c'è <b>NEAN</b>che un piatto</i>.",
          "Ascolta e ripeti con lo stesso accento. Poi l'insegnante dice una frase normale e tu la ripeti con la negazione rafforzata."),
    task=("Gioco di ruolo. L'insegnante visita la tua casa per affittare una stanza ed è molto pignolo/a. Rispondi in modo informale, con almeno cinque negazioni rafforzate. Poi scambiatevi i ruoli.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>la luce e lo spazio</li><li>il rumore e i vicini</li><li>il riscaldamento</li><li>i problemi (sii sincero/a!)</li></ul>",
          "Insegnante: La stanza è un po' piccola, no? · C'è rumore la sera? · Il riscaldamento funziona? · I vicini sono simpatici? · Posso portare il mio gatto? · Io non so neanche fare un uovo: è un problema? · Mah… mica male. Ci penso."),
    talk5=["Si possono usare <i>mica, boh, uffa</i> con persone che non conosci?", "Che cosa non è affatto importante, per te, in una casa?"],
    n5=["frasi per il gioco: <i>La stanza non è piccola → non è mica piccola · Non ho un euro → non ho neanche un euro.</i>", "Registro informale (tu). Reagire con <i>Ah, però! · Ma va'!</i>"],
    hA=("Domenica Tommaso scrive a sua sorella Marta. Scegli la forma giusta.",
        "<b>Tommaso:</b> Ciao Marta! Ieri ho visto la stanza in via Zamboni. {0}! Non è {1} piccola e il prezzo non è {2} alto. Il tappeto blu non è {3} bello, ma pazienza. E la cucina? Non c'era {4} un piatto sporco! Il coinquilino vuole insegnarmi a fare il feijão. Io non so cucinare, e neanche lui, secondo me!",
        [(["Mica male", "Mica bene"], "Mica male"), (["mica", "anche"], "mica"), (["per niente", "niente per"], "per niente"),
         (["affatto", "infatti"], "affatto"), (["neanche", "anche"], "neanche")]),
    hB=("Riscrivi con la parola tra parentesi.",
        [("La casa non è piccola. (mica)", "La casa non è mica piccola."), ("Non ho un euro. (neanche)", "Non ho neanche un euro."),
         ("Il film non mi è piaciuto. (per niente)", "Il film non mi è piaciuto per niente.")]),
    watch=[("Uffa! Finalmente a casa.", "Meno male! Finalmente a casa.", "<i>uffa</i> = noia, non sollievo."),
           ("Affatto, hai ragione.", "Infatti, hai ragione.", "<i>affatto</i> = per niente."),
           ("Non fumo. — Anche io no.", "Neanch'io.", "<i>eu também não</i> = <i>neanch'io</i>.")],
    write=("Un messaggio informale: racconta a un amico una visita (una casa, un ristorante, un posto nuovo).",
           "Ciao…, oggi ho visto…", ["cinque negazioni rafforzate", "<i>neanch'io</i> o <i>neanche a me</i>", "un'espressione del parlato (<i>Ah, però! · Ma va'!</i>)"]),
    cando="So usare mica, affatto, per niente e neanche e reagire con le parole del parlato.",
    nH="Prossima unità: <i>Modi di dire</i> (Carnevale; <i>da</i> + infinito).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 08 - Mica male")
