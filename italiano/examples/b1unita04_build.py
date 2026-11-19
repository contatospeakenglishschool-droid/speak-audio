# Speak! Progresso B1 - Unità 04 "Me ne vado!" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 04", audio_json=os.path.join(HERE, "audio_it-b1-unita-04.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-04", "04.1 Me ne vado!", "04.2 Ripeti")

C = dict(
    nn="04", title="Me ne vado!", subtitle="Una giornataccia · <b>i verbi pronominali</b>",
    cover=[("SAI FARE", "sfogarti dopo una giornata storta, mostrare comprensione, consolare e dare consigli"),
           ("LINGUA", "Me ne vado. · Non te la prendere. · Ce l'ho con lui. · Ce l'ho fatta."),
           ("PRONUNCIA", "i pronomi senza accento: «me ne vado», «ce l'ho»")],
    t1="giornate storte",
    start=["Guarda la foto. Che cosa è successo a questa donna, secondo te?", "Qual è stata la tua ultima giornata storta?",
           "Che cosa fai la sera, dopo una giornata difficile al lavoro?"],
    kw=[("una giornata in cui va tutto male", "una giornataccia"), ("dare il lavoro finito al cliente", "consegnare"),
        ("un cambiamento in un progetto", "una modifica"), ("un segno di sporco su un vestito", "una macchia"),
        ("la persona che dirige un ufficio", "il capo"), ("una bevanda calda che calma", "la camomilla")],
    use_words=["Racconta la tua ultima giornataccia in tre frasi.", "Com'è il tuo capo (o il tuo insegnante ideale)?"],
    n1=["A: il suffisso <i>-accio</i> = negativo (<i>tempaccio, parolaccia</i>). <i>Sfogarsi</i> = <i>desabafar</i>."],
    aims=["Me ne vado! La giornataccia di Júlia · Parliamone", "I verbi pronominali: andarsene, prendersela, cavarsela, avercela, farcela",
          "Sfogarsi e consolare (04.2) · gioco di ruolo: un collega si sfoga", "Il messaggio di Júlia a Camila · trasformare le frasi · scrittura (100–150 parole)"],
    story="Mercoledì 20 gennaio, sera. Il cliente di Milano, che lunedì aveva approvato il progetto, vuole cambiare tutto; il capo chiede le modifiche entro venerdì. Júlia chiude il computer con un colpo, chiede scusa a Marco («non me la prendo con te, ce l'ho con lui») e Marco la manda a casa: «ce la caviamo». In tintoria la macchia di vino c'è ancora: Júlia se la prende con la ragazza e se ne va senza salutare. Al bar Davide racconta il suo esame orale di fisica: se l'è cavata con un sorriso e un disegno alla lavagna (24). Júlia non ce l'ha con Camila; Giulia le offre una camomilla.",
    prob="Il portoghese non ha verbi come <i>andarsene</i> o <i>prendersela</i>: lo studente li capisce poco e usa sempre <i>andare via, arrabbiarsi</i>. Errori tipici: <i>mi ne vado</i> (davanti a <i>ne / la</i>: <i>me, te, se, ce</i>), <i>me la ho presa</i> (ausiliare <b>essere</b>), <i>ce la ho</i> (si dice <i>ce l'ho</i>). Falso amico: <i>estou brava</i> = <i>sono arrabbiata / ce l'ho con…</i>; in italiano <i>brava</i> vuol dire competente.",
    real="All'università italiana molti esami sono <b>orali</b>: lo studente parla con il professore per 15–30 minuti. I voti vanno da 18 a 30 (il massimo è <i>30 e lode</i>): il 24 di Davide è un voto discreto. Al bar, quando il barista non fa pagare, si dice <i>offre la casa</i>.",
    tr=("Me ne vado!", "Ripeti: i verbi pronominali"),
    gist=("Mercoledì sera: prima allo studio, poi al bar di Giulia. Ascolta. Di che cosa parlano soprattutto?",
          ["di una giornata storta e di come se la cavano", "di una vacanza al mare", "di un trasloco"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il cliente di Milano vuole cambiare tutto il progetto.", "V"), ("Júlia deve consegnare le modifiche lunedì.", "F"),
             ("In tintoria hanno tolto la macchia.", "F"), ("Júlia è stata gentile con la ragazza della tintoria.", "F"),
             ("Davide ha preso ventiquattro all'esame.", "V"), ("Júlia ce l'ha con Camila per il vestito.", "F")]),
    talk2=["Perché Júlia chiede scusa a Marco?", "Giulia dice: «Se il cliente vuole un progetto diverso, glielo fai diverso». È un buon consiglio?",
           "Che cosa fai tu per calmarti dopo una giornataccia?"],
    n2=["B: 2 entro venerdì · 3 la macchia c'è ancora · 4 se l'è presa con lei · 6 non ce l'ha con Camila.", "Parliamone 1: era nervosa, ma ce l'ha con il cliente."],
    gref="verbi_pronominali",
    t4="i verbi pronominali",
    pA=("Di' la stessa cosa con un verbo pronominale.",
        [("Sono arrabbiato con il mio vicino. → ___ con il mio vicino.", "Ce l'ho"), ("Non riesco a finire tutto. → Non ___ a finire tutto.", "ce la faccio"),
         ("Davide è andato via presto. → Davide ___ presto.", "se n'è andato"), ("Non ti offendere! → Non ___ prendere!", "te la"),
         ("Bruno è riuscito a rispondere. → Bruno ___ con il professore.", "se l'è cavata")]),
    pAw="26mm",
    pB=[("Ieri Júlia ", ["se l'è presa", "l'ha presa"], "se l'è presa", " con la ragazza della tintoria."),
        ("Non ", ["te la", "ti la"], "te la", " prendere, è solo un esame!"),
        ("Alla fine Davide ", ["ce l'ha fatta", "ce l'è fatta"], "ce l'ha fatta", " a passare l'esame.")],
    rule="I <b>verbi pronominali</b> hanno pronomi fissi che cambiano il significato: <i>andar<b>sene</b></i> (andare via), <i>prender<b>sela</b></i> (offendersi), <i>cavar<b>sela</b></i> (riuscire in una situazione difficile), <i>aver<b>cela</b> con</i> (essere arrabbiato con), <i>far<b>cela</b></i> (riuscire). Davanti a <i>ne / la</i>: <b>me, te, se, ce, ve</b>. Passato con <b>essere</b> (<i>me la sono presa</i>), ma <i>ce l'<b>ho</b> fatta</i>.",
    use=["Con chi ce l'hai in questo periodo? Perché?", "Una situazione difficile: come te la sei cavata?", "Quando te la prendi facilmente?",
         "Una festa noiosa: dopo quanto tempo te ne vai?", "Una cosa difficile che alla fine ce l'hai fatta a fare."],
    n4="Pratica B1: <i>prendersela</i> → <i>essere</i> e participio sempre in <i>-a</i> (accordo con <i>la</i>).",
    t5="sfogarsi e consolare",
    fl=(["sfogarsi", "mostrare comprensione", "dare consigli", "calmare"],
        ["Che giornataccia! · Non ce la faccio più! · Ce l'ho con…", "Ti capisco. · Che nervi! · Ci credo che te la sei presa.",
         "Al posto tuo… · Perché non…? · Lascia perdere.", "Dai, non te la prendere. · Vedrai che ce la fai. · Te la caverai."]),
    pron=("I pronomi <i>me, te, ce, ne, la</i> non hanno accento: si legano al verbo come una sola parola. L'accento è solo sul verbo: <i>me ne <b>va</b>do · ce l'<b>ho</b> · non te la <b>pren</b>dere</i>. Attenzione: <i><b>vat</b>tene</i>.",
          "Ascolta e ripeti con un tono arrabbiato e poi con un tono calmo."),
    task=("Gioco di ruolo. L'insegnante è un tuo collega e ha avuto una giornataccia. Ascolta, mostra comprensione e dai consigli. Poi scambiatevi i ruoli e racconta tu la tua giornataccia peggiore.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>che cosa è successo</li><li>con chi te la sei presa</li><li>come te la sei cavata</li></ul>",
          "Insegnante: Non ce la faccio più! · Il capo ce l'ha con me, ne sono sicuro/a. · Mi ha dato tre progetti per lunedì. · Domani me ne vado da questa azienda! · Forse hai ragione… (finire con «Che cosa farei senza di te?»)"),
    talk5=["È meglio sfogarsi subito o aspettare di essere calmi?", "In Brasile, al lavoro, si mostra la rabbia o si nasconde?"],
    n5=["accenti: <i>va</i>do · <i>pren</i>dere · <i>ho</i> · <i>fac</i>cio · ca<i>va</i>ta · <i>vat</i>tene.", "Esagerare un po' la rabbia per far usare allo studente le espressioni per calmare."],
    hA=("Giovedì notte Júlia scrive a Camila. Scegli la forma giusta.",
        "<b>Júlia:</b> Ciao Cami! Giornata lunghissima, ma {0}: domani consegniamo le modifiche. Ieri invece {1} con tutti, anche con la povera ragazza della tintoria… Sì, la macchia c'è ancora, ma tranquilla: non {2} con te! Stasera {3} dallo studio alle undici. Sabato {4} tutti a Modena a mangiare le tigelle?",
        [(["ce l'abbiamo fatta", "ce l'abbiamo fatto"], "ce l'abbiamo fatta"), (["me la sono presa", "mi la sono presa"], "me la sono presa"),
         (["ce l'ho", "ce la ho"], "ce l'ho"), (["me ne sono andata", "mi ne sono andata"], "me ne sono andata"), (["ce ne andiamo", "ci ne andiamo"], "ce ne andiamo")]),
    hB=("Riscrivi con un verbo pronominale.",
        [("Siamo riusciti a prendere il treno!", "Ce l'abbiamo fatta a prendere il treno!"), ("Marco è andato via dalla festa alle dieci.", "Marco se n'è andato dalla festa alle dieci."),
         ("Non ti arrabbiare con me!", "Non te la prendere con me!")]),
    watch=[("Sono brava con il cliente.", "Ce l'ho con il cliente.", "<i>brava</i> = competente."),
           ("Mi ne vado.", "Me ne vado.", "davanti a <i>ne</i>: <i>mi → me</i>."),
           ("Me la ho presa con lui.", "Me la sono presa con lui.", "<i>prendersela</i> vuole <i>essere</i>.")],
    write=("Una settimana difficile: racconta a un amico con chi te la sei presa e come ce l'hai fatta alla fine.",
           "Ciao…, che settimana! Lunedì…", ["quattro verbi pronominali", "un passato con <i>essere</i> (<i>me la sono presa</i>)", "<i>ce l'ho fatta</i>"]),
    cando="So sfogarmi dopo una giornataccia e consolare qualcuno con i verbi pronominali.",
    nH="Prossima unità: <i>Il Made in Italy</i> (il congiuntivo presente).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 04 - Me ne vado")
