# Speak! Progresso B1 - Unità 25 "Avrà già finito?" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 25", audio_json=os.path.join(HERE, "audio_it-b1-unita-25.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-25", "25.1 Avrà già finito", "25.2 Ripeti")

C = dict(
    nn="25", title="Avrà già finito?", subtitle="Ipotesi e progetti · <b>il futuro anteriore</b>",
    cover=[("SAI FARE", "fare ipotesi su che cosa è successo, parlare di progetti con una scadenza, mettere in ordine azioni future"),
           ("LINGUA", "Si sarà scaricato. · Avrai perso l'autobus. · Quando avrò finito… · Entro luglio avrò…"),
           ("PRONUNCIA", "avrò, sarà, finirò: l'accento sull'ultima sillaba")],
    t1="aspettare",
    start=["Guarda la foto. Chi aspetta questa persona? Da quanto tempo?", "Sei una persona puntuale? E i tuoi amici?",
           "Quanto tempo aspetti prima di chiamare qualcuno in ritardo?"],
    kw=[("non ha più batteria", "scarico"), ("l'ultima fermata di un autobus", "il capolinea"), ("lezioni private a pagamento", "le ripetizioni"),
        ("risparmiare soldi per il futuro", "mettere da parte"), ("i giorni di vacanza dal lavoro", "le ferie"), ("prima di una data, non dopo", "entro")],
    use_words=["Quando prendi le ferie quest'anno? Dove vai?", "Stai mettendo da parte soldi per qualcosa? Per che cosa?"],
    n1=["A: <i>le ferie</i> = vacanze dal lavoro (sempre plurale); <i>entro</i> = <i>até</i> (scadenza): <i>entro venerdì</i>."],
    aims=["Avrà già finito?: Davide è in ritardo · Parliamone", "Il futuro anteriore: progetti e ipotesi sul passato",
          "Ipotesi e progetti (25.2) · l'accento del futuro", "Il messaggio di Giulia · che cosa sarà successo? · scrittura (100–150 parole)"],
    story="Sabato 19 giugno, ore 19, bar Giulia. Júlia e Giulia aspettano Davide, che oggi ha l'ultimo esame di giugno: aveva detto alle sei e mezza e il telefono è spento. Ipotesi: l'esame sarà durato di più, il telefono si sarà scaricato, non avrà dormito, avrà dimenticato (impossibile: Giulia gli ha promesso lo spritz gratis). Intanto il cugino di Pietro, al bar da una settimana, fa già i cappuccini meglio di Giulia: quando avrà imparato anche i conti, lei potrà andare in ferie (un mese in Sardegna, il suo sogno) — ma solo quando Elena sarà tornata, cioè a settembre. Alle 19.30 arriva Davide: si è addormentato sull'autobus ed è finito al capolinea; ha preso 28. Entro fine luglio avrà finito gli esami e poi comprerà la moto (il suo sogno), con i soldi delle ripetizioni.",
    prob="Il futuro anteriore corrisponde al portoghese <i>quando eu tiver terminado</i> (futuro do subjuntivo composto), che l'italiano non ha: lo studente dice <i>quando ho finito…, comprerò</i> o <i>quando avessi finito</i>. Per le ipotesi il brasiliano usa <i>deve ter perdido</i> o <i>será que ele…?</i>: l'italiano preferisce <i>avrà perso</i>, <i>dove sarà andato?</i>. Attenzione all'accordo con <i>essere</i> e all'accento finale (<i>avrò</i>, non <i>avro</i>).",
    real="In Italia molti negozi e bar chiudono per qualche settimana d'estate: sulla porta c'è il cartello <i>Chiuso per ferie</i>, soprattutto intorno a Ferragosto (15 agosto). Per legge ogni lavoratore dipendente ha almeno quattro settimane di ferie pagate all'anno. Gli italiani usano il futuro per le ipotesi tutti i giorni: <i>Che ore sono? — Saranno le sette.</i>",
    tr=("Avrà già finito?", "Ripeti: il futuro anteriore"),
    gist=("Sabato sera, al bar Giulia. Ascolta. Perché Davide arriva in ritardo?",
          ["si è addormentato sull'autobus", "l'esame è durato tre ore", "ha dimenticato l'appuntamento"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Davide aveva detto che arrivava alle sei e mezza.", "V"), ("Il cugino di Pietro fa i cappuccini meglio di Giulia.", "V"),
             ("Giulia andrà in Sardegna a luglio.", "F"), ("Davide ha preso trenta.", "F"),
             ("Davide vuole comprare una macchina.", "F"), ("Davide ha dato ripetizioni tutto l'anno.", "V")]),
    talk2=["Quali ipotesi fanno Júlia e Giulia? Quale ti sembrava la più probabile?", "Ti sei mai addormentato/a sull'autobus o sul treno?",
           "Secondo te, Davide riuscirà a comprare la moto?"],
    n2=["B: 3 a settembre, quando Elena sarà tornata · 4 ventotto · 5 la moto.", "La moto e la Sardegna sono i sogni di Davide e Giulia (unità 14)."],
    gref="futuro_anteriore",
    t4="il futuro anteriore",
    pA=("Completa con il futuro anteriore del verbo tra parentesi.",
        [("Davide non risponde: il telefono si ___ (scaricare).", "sarà scaricato"), ("Quando il cugino ___ (imparare) i conti, Giulia andrà in ferie.", "avrà imparato"),
         ("Entro fine luglio Davide ___ (finire) tutti gli esami.", "avrà finito"), ("Giulia partirà quando Elena ___ (tornare).", "sarà tornata"),
         ("Sono già le otto: ___ (perdere, loro) il treno.", "avranno perso")]),
    pAw="30mm",
    pB=[("Quando ", ["avrò finito", "ho finito"], "avrò finito", " il corso, farò un viaggio in Italia."),
        ("Marco non è venuto: ", ["sarà stato", "sarà"], "sarà stato", " male ieri sera."),
        ("Che ore sono? Non so, ", ["saranno", "saranno state"], "saranno", " le otto.")],
    rule="<b>Futuro anteriore</b> = <i>avrò / sarò</i> + participio. 1) azione futura finita <b>prima</b> di un'altra: <i>quando / appena / dopo che avrò finito, partirò</i>. 2) scadenza: <i>entro luglio avrò finito</i>. 3) <b>ipotesi sul passato</b>: <i>avrà perso l'autobus</i> (ipotesi sul presente: futuro semplice, <i>sarà stanco</i>).",
    use=["Che cosa avrai fatto entro la fine dell'anno?", "Completa: <i>Quando avrò imparato bene l'italiano, …</i>",
         "Un amico non risponde da due giorni: che cosa sarà successo?", "Il tuo collega oggi è arrivato in ritardo e di cattivo umore: perché?",
         "Dove sarà andato in vacanza il tuo capo / il tuo insegnante?"],
    n4="B3: ipotesi sul presente → futuro semplice.",
    t5="ipotesi e progetti",
    fl=(["fare ipotesi", "reagire", "progetti con scadenza", "prima… poi…"],
        ["Avrà perso… · Si sarà dimenticato/a… · Sarà stato/a…", "Può darsi. · Non credo. · Sarà, ma… · Magari!",
         "Entro dicembre avrò… · Per l'estate avrò…", "Quando avrò finito…, … · Appena sarò tornato/a…, …"]),
    pron=("Il futuro ha l'<b>accento sull'ultima sillaba</b> alla prima e alla terza persona: <b>avrò</b>, <b>sarò</b>, <b>avrà</b>, <b>sarà</b>, <b>finirò</b>. Senza accento la parola cambia: <i>sarà</i> (futuro) ≠ <i>Sara</i> (nome). Nello scritto l'accento si mette sempre.",
          "Ascolta e ripeti. Poi leggi: «Sara sarà già partita? Avrà preso il treno delle otto.»"),
    task=("Ipotesi e progetti. 1) Misteri: l'insegnante legge una situazione; fai almeno tre ipotesi con il futuro anteriore e l'insegnante dice quale è vera. 2) Il tuo piano: racconta che cosa avrai fatto entro la fine dell'anno e che cosa farai quando avrai finito.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>Il tuo vicino è uscito con una valigia enorme alle cinque di mattina.</li><li>La tua amica è arrivata al lavoro con un mazzo di fiori e un sorriso.</li><li>Il bar sotto casa è chiuso da tre giorni.</li></ul>",
          "Soluzioni possibili (l'insegnante sceglie): sarà partito per le vacanze / avrà avuto un volo presto · avrà ricevuto una proposta / sarà stato il suo compleanno · saranno andati in ferie / avranno rinnovato il locale. Nel piano chiedere almeno due frasi con <i>quando / appena + futuro anteriore</i>."),
    talk5=["Fai spesso ipotesi quando qualcuno è in ritardo, o ti preoccupi subito?", "Che cosa vorresti aver fatto entro i prossimi cinque anni?"],
    n5=["far notare l'accento scritto: scrivere alla lavagna <i>sara / sarà</i> e far leggere.", "Se lo studente usa <i>deve aver perso</i>, accettarlo e proporre anche <i>avrà perso</i>."],
    hA=("Il messaggio di Giulia a Elena. Scegli la forma giusta.",
        "<i>Ciao Elena! Come va il tirocinio? Qui tutto bene: il cugino di Pietro è bravissimo. Quando {0} imparato anche i conti, sarà perfetto! Sabato Davide è arrivato con un'ora di ritardo: pensavamo che {1} dimenticato l'appuntamento, invece si era addormentato sull'autobus. Io conto i giorni: appena tu {2} tornata, partirò per la Sardegna. Entro settembre {3} anche risparmiato abbastanza per un mese intero. Tu {4} già stanca degli ingegneri, no? Un abbraccio!</i>",
        [(["avrà", "ha"], "avrà"), (["avesse", "avrà"], "avesse"), (["sarai", "sei"], "sarai"),
         (["avrò", "ho"], "avrò"), (["sarai", "saresti"], "sarai")]),
    hB=("Fai un'ipotesi con il futuro anteriore.",
        [("Marco ha gli occhi rossi e sbadiglia.", "Avrà dormito poco. / Sarà stato sveglio tutta la notte."), ("Camila è tornata dalla montagna con le scarpe nuove.", "Le avrà comprate in montagna. / Avrà imparato la lezione."),
         ("La signora Rossi non è uscita oggi.", "Sarà stata stanca. / Avrà avuto ospiti.")]),
    watch=[("Quando ho finito, ti chiamerò.", "Quando avrò finito, ti chiamerò.", "due azioni future: futuro anteriore + futuro."),
           ("Deve aver perso l'autobus, sarà?", "Avrà perso l'autobus.", "basta il futuro anteriore."),
           ("Giulia sarà arrivato.", "Giulia sarà arrivata.", "con <i>essere</i> il participio concorda.")],
    write=("I tuoi progetti per i prossimi sei mesi: che cosa avrai fatto entro dicembre e che cosa farai quando avrai finito? Aggiungi un piccolo mistero della tua settimana e le tue ipotesi.",
           "Entro dicembre avrò…", ["tre futuri anteriori di progetto (<i>quando, appena, entro</i>)", "due ipotesi sul passato", "l'accento scritto su <i>avrò, sarà</i>"]),
    cando="So fare ipotesi su che cosa è successo e parlare di progetti futuri con il futuro anteriore.",
    nH="Prossima unità: <i>Viaggio in Sicilia</i> (il passato remoto).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 25 - Avrà già finito")
