# Speak! Progresso B1 - Unità 03 "Avrei dovuto…" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 03", audio_json=os.path.join(HERE, "audio_it-b1-unita-03.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-03", "03.1 Avrei dovuto...", "03.2 Ripeti")

C = dict(
    nn="03", title="Avrei dovuto…", subtitle="Piccoli rimpianti · <b>il condizionale passato</b>",
    cover=[("SAI FARE", "parlare di rimpianti, criticare con gentilezza, scusarsi e consolare"),
           ("LINGUA", "Avrei dovuto prenotare. · Avresti potuto dirmelo! · Ha detto che sarebbe venuto."),
           ("PRONUNCIA", "avremmo / avremo: la doppia che cambia il tempo")],
    t1="piccoli rimpianti",
    start=["Guarda la foto. A che cosa pensa quest'uomo, secondo te?", "La settimana scorsa: c'è una cosa che non hai fatto e che ti dispiace?",
           "Sei una persona che prenota in anticipo o all'ultimo momento?"],
    kw=[("una cosa che ci dispiace non aver fatto", "un rimpianto"), ("riservare un posto o un biglietto", "prenotare"),
        ("provare imbarazzo", "vergognarsi"), ("il negozio dove lavano i vestiti", "la tintoria"),
        ("dove teniamo i soldi e le carte", "il portafoglio"), ("l'orologio che ci sveglia", "la sveglia")],
    use_words=["Hai mai dimenticato il portafoglio in un momento importante?", "Di che cosa ti vergognavi da bambino/a?"],
    n1=["A: <i>vergognarsi</i> = <i>ter vergonha</i> (riflessivo); <i>la tintoria</i> = <i>lavanderia a seco</i>."],
    aims=["Avrei dovuto… Il fine settimana di Júlia, Camila e Bruno · Parliamone", "Il condizionale passato", "Rimpianti e scuse (03.2) · gioco di ruolo: chiedere scusa",
          "Il messaggio di Pietro · che cosa avrebbero dovuto fare? · scrittura (100–150 parole)"],
    story="Lunedì 18 gennaio, mattina, al bar di Giulia. Júlia è tornata da Milano: il cliente ha approvato il progetto, ma non ha visto il Cenacolo perché non aveva prenotato. Camila confessa che sabato, a cena con Pietro, ha rovesciato il vino rosso sul vestito nero di Júlia; non l'ha chiamata perché si vergognava; il vestito è in tintoria fino a mercoledì. Pietro aveva detto che avrebbe pagato lui, ma aveva dimenticato il portafoglio: ha pagato Camila. Bruno riporta la bici lunedì invece di domenica, bagnato: si era addormentato e aveva prestato l'ombrello a Davide. Giulia «aveva detto che sarebbe piovuto».",
    prob="Il portoghese usa il condizionale semplice per il futuro nel passato (<i>ele disse que viria</i>): lo studente dice <i>ha detto che verrebbe</i>; in italiano serve il condizionale <b>passato</b> (<i>sarebbe venuto</i>). <i>Eu devia ter feito</i> → lo studente traduce <i>dovevo aver fatto</i>; la forma naturale è <i>avrei dovuto fare</i>. Attenzione all'ausiliare <i>essere</i> e a <i>avremmo / avremo</i>.",
    real="Il Cenacolo di Leonardo è nel refettorio di Santa Maria delle Grazie, a Milano: entrano pochi visitatori per volta e per circa un quarto d'ora, quindi i biglietti finiscono settimane prima. Al primo appuntamento spesso paga chi ha invitato, ma tra i giovani si divide spesso il conto (<i>fare alla romana</i>).",
    tr=("Avrei dovuto…", "Ripeti: il condizionale passato"),
    gist=("Lunedì mattina, al bar di Giulia. Ascolta. Di che cosa parlano soprattutto?",
          ["delle cose andate storte nel fine settimana", "di un nuovo lavoro di Camila", "di un esame di Davide"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("A Milano Júlia ha visto il Cenacolo.", "F"), ("Camila ha macchiato il vestito con il vino rosso.", "V"),
             ("Il vestito sarà pronto lunedì.", "F"), ("Alla fine della cena ha pagato Pietro.", "F"),
             ("Bruno ha riportato la bici con un giorno di ritardo.", "V"), ("Bruno aveva prestato l'ombrello a Davide.", "V")]),
    talk2=["Perché Camila non ha chiamato Júlia sabato sera?", "Giulia dice: «Io avevo detto che sarebbe piovuto». Con che tono lo dice?",
           "Chi dovrebbe pagare al primo appuntamento, secondo te?"],
    n2=["B: 1 non c'erano più biglietti · 3 mercoledì · 4 ha pagato Camila.", "Parliamone 2: tono scherzoso, da «te l'avevo detto»."],
    gref="condizionale_passato",
    t4="il condizionale passato",
    pA=("Che cosa avrebbero dovuto fare? Completa con il condizionale passato.",
        [("Júlia non ha visto il Cenacolo: (dovere) ___ prenotare prima.", "avrebbe dovuto"), ("Bruno si è bagnato: (dovere) ___ prendere l'ombrello.", "avrebbe dovuto"),
         ("Camila, (potere) ___ dirmelo subito!", "avresti potuto"), ("Al posto tuo io (arrabbiarsi) ___.", "mi sarei arrabbiata"),
         ("Pietro aveva detto che (pagare) ___ lui.", "avrebbe pagato")]),
    pAw="28mm",
    pB=[("Ieri Davide ha detto che ", ["sarebbe passato", "passerebbe"], "sarebbe passato", " da me."),
        ("", ["Avresti dovuto", "Dovresti"], "Avresti dovuto", " studiare di più: ormai l'esame è finito."),
        ("Sabato, al posto tuo, ", ["sarei rimasto", "avrei rimasto"], "sarei rimasto", " a casa.")],
    rule="<b>condizionale di avere / essere + participio</b>: <i>avrei dovuto, avresti potuto, sarei arrivato</i>. Per le cose che <b>non sono successe</b> (rimpianti, desideri, critiche, <i>al posto tuo</i>) e per il <b>futuro nel passato</b>: <i>ha detto che <b>sarebbe venuto</b></i> (mai <i>verrebbe</i>).",
    use=["Un piccolo errore recente: che cosa avresti dovuto fare?", "Un desiderio non realizzato: <i>Avrei voluto…</i>",
         "Un amico è arrivato tardi a un colloquio: criticalo con gentilezza. <i>Avresti potuto…</i>", "Che cosa avresti fatto al posto di Camila?",
         "Una promessa non mantenuta: <i>Aveva detto che…</i>"],
    n4="Pratica B2: <i>dovresti</i> = consiglio per il futuro; qui l'esame è finito, quindi <i>avresti dovuto</i>.",
    t5="rimpianti e scuse",
    fl=(["rimpiangere", "criticare con gentilezza", "scusarsi", "consolare"],
        ["Avrei dovuto… · Avrei voluto… · Che stupido/a!", "Avresti potuto… · Al posto tuo… · Forse sarebbe stato meglio…",
         "Mi dispiace tantissimo. · Scusami, è colpa mia. · Come posso rimediare?", "Non è la fine del mondo. · Può capitare. · Succede a tutti."]),
    pron=("La doppia cambia il tempo: <i>avre<b>mm</b>o</i> (condizionale) ≠ <i>avremo</i> (futuro); lo stesso con <i>sare<b>mm</b>o / saremo</i>. Anche <i>avre<b>bb</b>e, sare<b>bb</b>e</i> hanno la doppia.",
          "Ascolta e ripeti. Poi l'insegnante dice «avremo» o «avremmo»: tu dici quale hai sentito."),
    task=("Gioco di ruolo. L'insegnante ti ha prestato una cosa e tu l'hai rovinata. Chiedi scusa, spiega che cosa è successo e proponi una soluzione. Poi parla per un minuto di un tuo rimpianto, piccolo o grande.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>che cosa è successo</li><li>che cosa avresti dovuto fare</li><li>come puoi rimediare</li></ul>",
          "Insegnante: Allora, la mia macchina fotografica? · Che cosa è successo? · Perché non me l'hai detto subito? · Avresti potuto stare più attento/a! · E adesso come facciamo? · Va bene, ma la prossima volta…"),
    talk5=["Meglio avere rimpianti (cose non fatte) o rimorsi (cose fatte male)?", "È facile per te chiedere scusa?"],
    n5=["frasi per il gioco: <i>Domani avremo tempo · Ieri avremmo avuto tempo · Saremo a Roma · Saremmo andati a Roma.</i>", "Usare almeno un <i>avresti potuto</i> per far reagire lo studente con le scuse."],
    hA=("Domenica mattina Pietro scrive a Camila. Scegli la forma giusta.",
        "<b>Pietro:</b> Buongiorno Camila… Ieri sera che figuraccia! {0} controllare il portafoglio prima di uscire. Ti avevo detto che {1} io, e invece… Al posto tuo {2}, e tu invece ridevi! {3} invitarti di nuovo sabato prossimo, in un posto dove il vino è bianco. E questa volta {4} io, giuro!",
        [(["Avrei dovuto", "Dovrei"], "Avrei dovuto"), (["avrei pagato", "pagherei"], "avrei pagato"), (["mi sarei arrabbiato", "mi avrei arrabbiato"], "mi sarei arrabbiato"),
         (["Vorrei", "Avrei voluto"], "Vorrei"), (["pagherò", "avrei pagato"], "pagherò")]),
    hB=("Riscrivi con il condizionale passato.",
        [("Non ho studiato e ora mi dispiace. (dovere)", "Avrei dovuto studiare."), ("Ha detto: «Verrò alle otto».", "Ha detto che sarebbe venuto alle otto."),
         ("Volevo vedere il Cenacolo, ma non l'ho visto.", "Avrei voluto vedere il Cenacolo.")]),
    watch=[("Ha detto che verrebbe.", "Ha detto che sarebbe venuto.", "futuro nel passato = condizionale passato."),
           ("Dovevo aver prenotato.", "Avrei dovuto prenotare.", "<i>devia ter feito</i> → <i>avrei dovuto fare</i>."),
           ("Ho derrubato il bicchiere.", "Ho fatto cadere il bicchiere.", "<i>derrubar</i> → <i>far cadere</i>.")],
    write=("Lettera a te stesso/a di dieci anni fa: che cosa avresti dovuto fare, che cosa avresti voluto, che cosa non cambieresti.",
           "Caro/a me di dieci anni fa, ti scrivo da…", ["quattro condizionali passati", "<i>avrei dovuto / voluto / potuto</i>", "un futuro nel passato", "<i>al posto tuo…</i>"]),
    cando="So parlare di rimpianti, criticare con gentilezza e chiedere scusa.",
    nH="Prossima unità: <i>Me ne vado!</i> (i verbi pronominali).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 03 - Avrei dovuto")
