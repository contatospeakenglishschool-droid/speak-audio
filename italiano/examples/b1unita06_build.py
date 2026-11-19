# Speak! Progresso B1 - Unità 06 "Può darsi che…" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 06", audio_json=os.path.join(HERE, "audio_it-b1-unita-06.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-06", "06.1 Può darsi che...", "06.2 Ripeti")

C = dict(
    nn="06", title="Può darsi che…", subtitle="Ipotesi e pettegolezzi · <b>il congiuntivo passato</b>",
    cover=[("SAI FARE", "fare ipotesi su un fatto passato, esprimere preoccupazione e certezza, tranquillizzare"),
           ("LINGUA", "Può darsi che abbia perso il telefono. · Penso di averlo visto."),
           ("PRONUNCIA", "l'intonazione del dubbio e della certezza")],
    t1="chiacchiere al bar",
    start=["Guarda la foto. Di che cosa parlano, secondo te?", "Quando un amico non risponde ai messaggi per giorni, che cosa pensi?",
           "Ti preoccupi facilmente per le persone che ami?"],
    kw=[("chiacchiere sulla vita degli altri", "i pettegolezzi"), ("un'idea su una cosa che non sappiamo con sicurezza", "un'ipotesi"),
        ("essere in ansia per qualcuno", "preoccuparsi"), ("una cosa che nessuno riesce a spiegare", "un mistero"),
        ("il contrario di accendere", "spegnere"), ("discutere in modo arrabbiato", "litigare")],
    use_words=["Ti piacciono i pettegolezzi? Dove se ne sentono di più?", "Quando spegni il telefono?"],
    n1=["A: <i>pettegolezzi</i> = <i>fofocas</i>; <i>spegnere</i> = <i>desligar</i> (≠ <i>slegare</i>)."],
    aims=["Può darsi che… Il mistero di Bruno · Parliamone", "Il congiuntivo passato · che + congiuntivo o di + infinito",
          "Ipotesi e preoccupazioni (06.2) · gioco di ruolo: un'amica sparita", "Il messaggio di Chiara · fare ipotesi · scrittura (100–150 parole)"],
    story="Giovedì 28 gennaio, sera, al bar di Giulia. Bruno non risponde ai messaggi da tre giorni e Júlia è preoccupata. Le ipotesi: ha perso il telefono (impossibile, «ci dorme insieme»), si è innamorato (ma sta con Chiara da più di un anno), ha litigato con Chiara. Davide pensa di averlo visto martedì in via Zamboni con dei libri; Stefano dice che non è venuto al calcetto. Giulia capisce: gennaio = esami. Bruno arriva stanco ma felice: ha spento il telefono per tre giorni (anzi, l'ha spento Chiara) e ha preso 26 in Storia medievale.",
    prob="Il portoghese usa <i>que</i> anche con lo stesso soggetto (<i>acho que vi o Bruno</i>): lo studente dice <i>penso che ho visto</i> invece di <i>penso di aver visto</i>. Con <i>pode ser que tenha perdido</i> il parallelo aiuta. Dopo <i>forse</i> serve l'indicativo (<i>forse ha perso</i>), mentre il portoghese usa il subjuntivo (<i>talvez tenha perdido</i>). Falsi amici: <i>desligar</i> → <i>spegnere</i>; <i>desaparecer</i> → <i>sparire</i>.",
    real="Nelle università italiane ci sono tre sessioni d'esame: invernale (gennaio–febbraio), estiva (giugno–luglio) e autunnale (settembre). Lo studente può rifiutare un voto e ripetere l'esame. Il bar sotto casa è il centro delle notizie del quartiere. <i>Acqua in bocca!</i> = non dirlo a nessuno.",
    tr=("Può darsi che…", "Ripeti: il congiuntivo passato"),
    gist=("Giovedì sera, al bar di Giulia. Ascolta. Di che cosa parlano soprattutto?",
          ["del silenzio di Bruno e delle ipotesi degli amici", "del compleanno di Giulia", "di un viaggio a Roma"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Bruno non risponde ai messaggi da una settimana.", "F"), ("Davide pensa di aver visto Bruno martedì.", "V"),
             ("Bruno e Chiara si sono lasciati.", "F"), ("Martedì Bruno non è andato al calcetto.", "V"),
             ("Júlia aveva dimenticato gli esami di Bruno.", "V"), ("All'esame Bruno ha preso ventotto.", "F")]),
    talk2=["Quali ipotesi fanno gli amici su Bruno? Quale ti sembrava la più probabile?", "Perché, secondo te, Chiara ha spento il telefono di Bruno?",
           "È giusto spegnere il telefono per giorni senza avvisare?"],
    n2=["B: 1 da tre giorni · 3 stanno ancora insieme · 6 ventisei.", "<i>Non è che ha gli esami?</i> = domanda-ipotesi con l'indicativo."],
    gref="congiuntivo_passato",
    t4="il congiuntivo passato",
    pA=("Fai un'ipotesi con il congiuntivo passato.",
        [("Il tuo collega non è venuto al lavoro. Può darsi che (ammalarsi) ___.", "si sia ammalato"),
         ("Il bar di Giulia è chiuso. Può darsi che Giulia (andare) ___ dal medico.", "sia andata"),
         ("Marco è sorridente. È possibile che il cliente (approvare) ___ il progetto.", "abbia approvato"),
         ("Spero che non gli (succedere) ___ niente.", "sia successo"), ("Sono contenta che tu (passare) ___ l'esame.", "abbia passato")]),
    pAw="26mm",
    pB=[("Davide pensa ", ["di aver visto", "che ha visto"], "di aver visto", " Bruno in via Zamboni."),
        ("È possibile che Bruno ", ["sia andato", "è andato"], "sia andato", " in biblioteca."),
        ("Forse ", ["ha perso", "abbia perso"], "ha perso", " il telefono.")],
    rule="<b>congiuntivo presente di avere / essere + participio</b>: <i>abbia perso, sia successo, si sia innamorato</i>. Per un fatto <b>già successo</b> dopo <i>spero, penso, può darsi, è possibile, sono contento che…</i>. Con lo <b>stesso soggetto</b>: <b>di + infinito</b> (passato: <i>di aver visto</i>). Dopo <i>forse</i>: indicativo.",
    use=["Il tuo vicino ha una macchina nuova: fai due ipotesi. <i>Può darsi che…</i>", "Una cosa che pensi di aver fatto bene questa settimana. <i>Penso di aver…</i>",
         "Un amico non è venuto a una festa: perché? <i>È possibile che…</i>", "Di che cosa sei contento/a? <i>Sono contento/a che…</i>", "Una cosa che speri non sia successa."],
    n4="Pratica B3: <i>forse</i> + indicativo, anche se il portoghese usa il subjuntivo.",
    t5="ipotesi e preoccupazioni",
    fl=(["fare ipotesi", "essere sicuri", "preoccuparsi", "tranquillizzare"],
        ["Può darsi che… · È possibile che… · Forse… · Non è che…?", "Sono sicuro/a che… · Ci metterei la mano sul fuoco. · Di sicuro…",
         "Ho paura che… · Spero che non… · Non è da lui / da lei.", "Dai, non ti preoccupare. · Succede. · Ci sarà una spiegazione."]),
    pron=("Con un'<b>ipotesi</b> la voce resta sospesa e un po' più lenta (<i>Può darsi che… abbia perso il telefono</i>). Con una <b>certezza</b> la voce scende alla fine, decisa (<i>Ha perso il telefono.</i>).",
          "Ascolta e ripeti. Poi l'insegnante dice una frase con tono sicuro o con tono di dubbio: tu dici quale hai sentito."),
    task=("Gioco di ruolo. Un'amica che avete in comune non risponde da giorni. L'insegnante è preoccupato/a: fai ipotesi e tranquillizzalo/a. Poi guarda la foto e fai tre ipotesi su queste persone.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>chi sono, secondo te?</li><li>che cosa è successo prima?</li><li>dove vanno e perché?</li></ul>",
          "Insegnante: Marta non risponde da quattro giorni! · Non è da lei. · Penso di averla vista lunedì con una valigia… · Ho paura che le sia successo qualcosa. · Hai ragione, forse… · Alla fine: Ah, mi ha appena scritto! È in Sardegna con il suo nuovo ragazzo!"),
    talk5=["I pettegolezzi sono sempre negativi?", "Ti preoccupi di più tu o la tua famiglia quando non rispondi?"],
    n5=["le stesse frasi una volta con certezza (<i>Ha perso il telefono.</i>) e una volta con dubbio (<i>Forse… ha perso il telefono?</i>).", "Insistere sulla preoccupazione per far usare le espressioni per tranquillizzare."],
    hA=("Venerdì mattina Chiara scrive a Júlia. Scegli la forma giusta.",
        "<b>Chiara:</b> Ciao Júlia! Bruno mi dice che ieri eravate tutti preoccupati: scusami! Penso {0} con il telefono. Spero che tu non {1} con lui: è colpa mia. È vero che in questi giorni {2} tantissimo, e sono contenta che il professore gli {3} ventisei. Forse Bruno {4} ragione: la prossima volta lo lascio scrivere a sua sorella!",
        [(["di aver esagerato", "che ho esagerato"], "di aver esagerato"), (["ti sia arrabbiata", "ti sei arrabbiata"], "ti sia arrabbiata"),
         (["ha studiato", "abbia studiato"], "ha studiato"), (["abbia dato", "ha dato"], "abbia dato"), (["ha", "abbia"], "ha")]),
    hB=("Riscrivi con le parole tra parentesi.",
        [("Forse ha perso l'autobus. (può darsi che)", "Può darsi che abbia perso l'autobus."), ("Penso che io abbia sbagliato. (penso di)", "Penso di aver sbagliato."),
         ("Tu sei arrivato. Sono contento. (sono contento che)", "Sono contento che tu sia arrivato.")]),
    watch=[("Penso che ho visto Bruno.", "Penso di aver visto Bruno.", "stesso soggetto → <i>di</i> + infinito."),
           ("Forse abbia perso il telefono.", "Forse ha perso il telefono.", "<i>forse</i> + indicativo."),
           ("Bruno è disparito.", "Bruno è sparito / scomparso.", "<i>desaparecer</i> = <i>sparire</i>.")],
    write=("Un mistero risolto: una situazione in cui avete fatto tante ipotesi e poi avete scoperto la verità.",
           "La settimana scorsa è successa una cosa strana: …", ["quattro congiuntivi passati", "un'ipotesi con <i>può darsi che</i>", "<i>di</i> + infinito passato", "il finale: la verità"]),
    cando="So fare ipotesi su un fatto passato e tranquillizzare qualcuno.",
    nH="Prossima unità: <i>Cerco qualcuno che…</i> (il congiuntivo nelle relative).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 06 - Può darsi che")
