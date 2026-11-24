# Speak! Progresso B1 - Unità 36 "Finita la festa…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 36", audio_json=os.path.join(HERE, "audio_it-b1-unita-36.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-36", "36.1 Finita la festa", "36.2 Ripeti")

C = dict(
    nn="36", title="Finita la festa…", subtitle="La laurea di Davide · <b>il participio passato assoluto</b>",
    cover=[("SAI FARE", "raccontare un evento e quello che succede dopo, in ordine"),
           ("LINGUA", "finita la festa · partiti gli ospiti · lavati i bicchieri · fatto questo"),
           ("PRONUNCIA", "la vocale finale: finita, finiti · la pausa")],
    t1="la laurea",
    start=["Guarda la foto: è una corona d'alloro. Hai mai partecipato a una festa di laurea? Com'era?", "Qual è il giorno più importante nella vita di uno studente?",
           "Dopo una grande festa, chi pulisce a casa tua?"],
    kw=[("finire l'università con l'esame finale", "laurearsi"), ("il lavoro scritto che si presenta alla fine dell'università", "la tesi"),
        ("il gruppo di professori che dà il voto finale", "la commissione"), ("le foglie che si portano in testa il giorno della laurea", "la corona d'alloro"),
        ("piccoli pezzi di carta colorata da lanciare alle feste", "i coriandoli"), ("chi ha appena finito l'università", "il neolaureato")],
    use_words=["Ti sei laureato/a? In che cosa? Com'è stata la discussione della tesi?", "In quali feste del tuo paese si usano i coriandoli?"],
    n1=["A: <i>laurearsi</i> = finire l'università; <i>discutere la tesi</i> = presentarla davanti alla commissione."],
    aims=["Finita la festa…: la laurea di Davide · Parliamone", "il participio passato assoluto: forma, accordo, usi",
          "Il racconto di un evento (36.2) · la vocale finale del participio", "Il messaggio di Camila · riscrivi · scrittura (100–150 parole)"],
    story="Sabato 27 novembre, mattina, al Bar Giulia dopo la festa. Venerdì 26 Davide si è laureato in ingegneria con 110: discussa la tesi, è uscito con la corona d'alloro, tutto rosso; la madre piangeva, il padre fotografava tutti. Al bar è stato letto il papiro con la caricatura di Davide sulla moto rossa (autrice segreta: Camila, che ha avuto anche l'idea dei coriandoli). Partiti gli ultimi ospiti alle due, Giulia ha chiuso; ora Júlia, Camila e Davide puliscono. Colazione offerta dal dottore; a pranzo un'altra festa con i parenti di Davide.",
    prob="Il portoghese ha la stessa struttura (<i>terminada a festa, feito isso</i>), quindi è facile da capire. Errori tipici: il participio senza accordo (<s>finito la festa</s>) e il calco <i>depois de terminada a festa</i> → <s>dopo finita la festa</s>. Lessico dell'università: la <i>laurea</i> è la «formatura» (non «láurea»), si discute la <i>tesi</i> (≈ TCC: «defender»), la <i>commissione</i> è la «banca» e ogni laureato si chiama <i>dottore</i>. Far sentire la vocale finale del participio (<i>finit<b>a</b>, finit<b>i</b></i>).",
    real="In Italia il voto di laurea va da 66 a <b>110</b>; il massimo è <b>110 e lode</b>. Il giorno della laurea si porta in testa la <b>corona d'alloro</b> e si regalano <b>confetti rossi</b>. In molte città del Nord, soprattutto a Padova, gli amici preparano il <b>papiro</b>: un grande foglio con una caricatura e una poesia scherzosa sul neolaureato, da leggere ad alta voce. Chi ha una laurea si chiama <b>dottore</b> o <b>dottoressa</b>.",
    tr=("Finita la festa", "Ripeti: il participio assoluto"),
    gist=("Sabato mattina, al Bar Giulia. Ascolta. Che cosa è successo ieri?",
          ["Davide si è laureato e c'è stata una festa", "Giulia ha compiuto gli anni", "Camila ha cominciato un nuovo lavoro"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("La festa di laurea è stata al Bar Giulia.", "V"), ("L'idea dei coriandoli è stata di Giulia.", "F"),
             ("La commissione ha dato a Davide centodieci.", "V"), ("Durante la cerimonia il padre di Davide piangeva.", "F"),
             ("Gli ultimi ospiti sono andati via a mezzanotte.", "F"), ("Dopo le pulizie la colazione la offre Davide.", "V")]),
    talk2=["Com'è una festa di laurea nel tuo paese? Che differenze ci sono con l'Italia?", "Ti piacerebbe ricevere un papiro con una caricatura? Perché?",
           "Secondo te, chi deve pulire dopo una festa: chi la organizza o gli invitati?"],
    n2=["B: 2 di Camila · 4 la madre · 5 alle due.", "Ripresa: Davide ha dato l'ultimo esame il 30 luglio e ha comprato la moto rossa (unità 29); le gambe che tremavano come alla maratona (unità 33)."],
    gref="participio_assoluto",
    t4="finita la festa",
    pA=("Completa con il participio passato del verbo tra parentesi. Attenzione all'accordo!",
        [("___ (finire) la festa, abbiamo pulito il bar.", "Finita"), ("___ (lavare) i bicchieri, puliamo i tavoli.", "Lavati"),
         ("___ (partire) gli ultimi ospiti, Giulia ha chiuso.", "Partiti"), ("___ (leggere) il papiro, tutti hanno applaudito.", "Letto"),
         ("___ (discutere) la tesi, Davide è uscito con la corona.", "Discussa")]),
    pAw="24mm",
    pB=[("", ["Finito", "Finita"], "Finita", " la cena, siamo andati a ballare."),
        ("", ["Arrivate", "Arrivati"], "Arrivati", " a casa, Júlia e Davide hanno dormito."),
        ("", ["Fatte", "Fatto"], "Fatto", " questo, possiamo fare colazione.")],
    rule="<b>Participio passato</b> + nome = <i>dopo che…</i>: <i>Finita la festa</i> = dopo che la festa è finita. Il participio si accorda con l'<b>oggetto</b> (verbi con avere: <i>lavati i bicchieri</i>) o con il <b>soggetto</b> (verbi con essere: <i>partiti gli ospiti, arrivata a casa</i>). Non serve <i>dopo</i>; si può dire <i>una volta finita la festa</i>.",
    use=["Che cosa fai di solito, finita la giornata di lavoro?", "Che cosa hai fatto, finita la scuola (o l'università)?",
         "Arrivato/a a casa la sera, qual è la prima cosa che fai?", "Racconta una festa: che cosa è successo, finita la cena?",
         "Spiega una ricetta con i participi: <i>Lavate le verdure, … Tagliata la cipolla, …</i>"],
    n4="A: 2 e 3 plurale maschile (<i>i bicchieri, gli ospiti</i>); 5 <i>la tesi</i> → <i>discussa</i>. B3: <i>questo</i> → <i>fatto</i>.",
    t5="il racconto di un evento",
    fl=(["raccontare in ordine", "dire che cosa succede dopo", "organizzare il dopo-festa", "fare i complimenti"],
        ["Finita la cena… · Arrivati al bar… · Una volta…", "Fatto questo… · Detto ciò… · Subito dopo…",
         "Tocca a te! · Tu lavi, io asciugo. · Prima…, poi…", "Congratulazioni! · Complimenti, dottore! · Te lo meriti!"]),
    pron=("La vocale finale del participio dice chi o che cosa: <i>finit<b>a</b> la festa, finit<b>i</b> gli esami, finit<b>o</b> il lavoro, finit<b>e</b> le vacanze</i>. Va pronunciata chiara, senza ridurla. Dopo la frase con il participio si fa una piccola pausa: <i>Finita la festa, ↗ | abbiamo pulito.</i>",
          "Ascolta e ripeti. Poi leggi: «Finita la discussione, la commissione ti ha dato centodieci!»"),
    task=("Il racconto di un evento: scegli un evento importante (una laurea, un matrimonio, un trasloco, una partita, un concerto) e raccontalo in ordine all'insegnante, dalla preparazione al giorno dopo. Usa almeno cinque participi assoluti. L'insegnante chiede che cosa è successo dopo.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>la preparazione</li><li>l'arrivo</li><li>il momento più emozionante</li><li>la fine</li><li>le pulizie</li><li>il giorno dopo</li></ul>",
          "Insegnante: E finita la cerimonia? · Arrivati alla festa, che cosa avete fatto? Lo studente: Finita la cerimonia… · Arrivati al ristorante… · Partiti gli ospiti… · Fatto questo… Correggere l'accordo del participio e <i>dopo finita</i>."),
    talk5=["Qual è stata la festa più bella della tua vita? Perché?", "Preferisci organizzare una festa o essere invitato/a? E le pulizie del giorno dopo?"],
    n5=["far sentire la vocale finale del participio e la pausa.", "Pretendere almeno cinque participi assoluti con l'accordo corretto."],
    hA=("Il messaggio di Camila a Elena. Scegli la forma giusta.",
        "<i>Ciao Elena! Peccato che ieri sera tu non ci fossi! {0} la tesi, Davide è uscito con la corona d'alloro, tutto rosso. {1} al bar, abbiamo letto il papiro: tutti ridevano! {2} gli ultimi ospiti alle due, Giulia ha chiuso. Stamattina abbiamo pulito tutto: {3} i coriandoli e {4} i bicchieri, abbiamo fatto colazione. Ha offerto il dottore!</i>",
        [(["Discussa", "Discusso"], "Discussa"), (["Arrivati", "Arrivato"], "Arrivati"), (["Partiti", "Partito"], "Partiti"),
         (["spazzati", "spazzato"], "spazzati"), (["lavati", "lavate"], "lavati")]),
    hB=("Riscrivi le frasi con il participio passato assoluto.",
        [("Dopo che la festa è finita, abbiamo pulito.", "Finita la festa, abbiamo pulito."),
         ("Dopo aver letto il papiro, tutti hanno applaudito.", "Letto il papiro, tutti hanno applaudito."),
         ("Quando gli ospiti sono partiti, Giulia ha chiuso il bar.", "Partiti gli ospiti, Giulia ha chiuso il bar.")]),
    watch=[("Finito la festa, abbiamo pulito.", "Finita la festa, abbiamo pulito.", "il participio si accorda: <i>la festa</i> → <i>finita</i>."),
           ("Dopo finita la cena, siamo usciti.", "Finita la cena, siamo usciti.", "non serve <i>dopo</i>: il participio dice già «dopo che»."),
           ("Ho discusso la mia laurea.", "Ho discusso la tesi. / Mi sono laureato.", "si discute la <i>tesi</i>; la <i>laurea</i> è il titolo.")],
    write=("Racconta un evento importante della tua vita (una laurea, un matrimonio, un trasloco, una festa), dalla preparazione al giorno dopo.",
           "Era un giorno speciale…", ["almeno cinque participi assoluti con l'accordo giusto", "connettivi di tempo (<i>prima, poi, subito dopo, alla fine</i>)", "una frase finale: che cosa ricordi di più"]),
    cando="So raccontare un evento e quello che succede dopo, in ordine, con il participio passato assoluto.",
    nH="Prossima unità: <i>Mi ha chiesto di…</i> (dire di + infinito, chiedere se).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 36 - Finita la festa")
