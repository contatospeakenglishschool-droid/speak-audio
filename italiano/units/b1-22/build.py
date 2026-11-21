# Speak! Progresso B1 - Unità 22 "Spettabile…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 22", audio_json=os.path.join(HERE, "audio_it-b1-unita-22.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-22", "22.1 Spettabile", "22.2 Ripeti")

C = dict(
    nn="22", title="Spettabile…", subtitle="Reclami e lettere formali · <b>Lei e Voi, condizionale di cortesia</b>",
    cover=[("SAI FARE", "scrivere una lettera formale e un reclamo, chiedere con cortesia, difendere i tuoi diritti"),
           ("LINGUA", "Spettabile… · Vi scrivo in merito a… · Vi sarei grata se… · In attesa di un cortese riscontro"),
           ("PRONUNCIA", "le abbreviazioni: Spett.le, Sig.ra, Dott.")],
    t1="il reclamo",
    start=["Guarda la foto. Che cosa scrive questa persona? A chi?", "Scrivi spesso mail formali? A chi?",
           "Qual è l'ultimo acquisto online che ti ha deluso?"],
    kw=[("una protesta per un prodotto o un servizio che non va", "il reclamo"), ("l'ufficio che risponde ai clienti", "il servizio clienti"),
        ("che ha un danno, rotto", "danneggiato"), ("cambiare una cosa con un'altra uguale", "sostituire"),
        ("la risposta, in una lettera formale", "il riscontro"), ("la protezione per i prodotti difettosi", "la garanzia")],
    use_words=["Hai mai fatto un reclamo? Per che cosa?", "Che cosa fai se un pacco arriva danneggiato?"],
    n1=["A: <i>riscontro</i> = <i>retorno</i> (resposta) nelle lettere formali; <i>reclamo</i> e <i>sostituire</i> sono quasi uguali al portoghese."],
    aims=["Spettabile…: il reclamo di Júlia · Parliamone", "La lettera formale: formule, Lei e Voi, condizionale di cortesia",
          "Il reclamo al telefono (22.2) · le abbreviazioni", "La lettera di Júlia · da informale a formale · scrittura (100–150 parole)"],
    story="Giovedì 10 giugno, sera. Per lo smart working Júlia ha ordinato online una scrivania e una sedia: sono arrivate martedì, ma la scrivania ha una gamba rotta e la sedia è grigia invece che bianca. Il negozio non risponde al telefono e nella chat c'è solo un robot. Júlia va dalla signora Rossi con il computer: aveva scritto «Ciao! La scrivania è rotta…». La signora Rossi (che le dà del tu, mentre Júlia le dà del Lei) le insegna la lettera formale: Spettabile servizio clienti, in merito all'ordine del 2 giugno, Vi sarei grata se poteste…, i diritti del consumatore (14 giorni per restituire, garanzia di due anni) e «In attesa di un Vostro cortese riscontro, porgo distinti saluti». Júlia ride: sembra una lettera dell'Ottocento. Ma funziona.",
    prob="Il brasiliano trasporta le formule del portoghese: <i>Prezado</i> → <i>Gentile</i>, <i>Assunto</i> → <i>Oggetto</i> (<i>assunto</i> in italiano = preso a lavorare), <i>Atenciosamente</i> → <i>Cordiali / Distinti saluti</i>, <i>aguardo retorno</i> → <i>attendo un cortese riscontro</i>. Mescola <i>tu</i> e <i>Lei</i> nella stessa mail e dimentica il condizionale (<i>Voglio una scrivania nuova</i> suona aggressivo). <i>Spettabile</i> si usa solo per aziende e uffici.",
    real="In Italia per i reclami importanti si usa la <b>PEC</b> (posta elettronica certificata), che ha lo stesso valore legale di una raccomandata. Per gli acquisti online il consumatore ha 14 giorni per restituire la merce senza spiegazioni (diritto di recesso) e, per i prodotti difettosi, la garanzia legale è di due anni. Sulle buste e nelle mail si trova spesso <i>Spett.le</i> (Spettabile) e <i>c.a.</i> (alla cortese attenzione di).",
    tr=("Spettabile…", "Ripeti: le formule della lettera formale"),
    gist=("Giovedì sera, a casa della signora Rossi. Ascolta. Perché Júlia chiede aiuto?",
          ["deve scrivere un reclamo a un negozio online", "deve scrivere una lettera al capo", "vuole comprare una scrivania nuova"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("La scrivania e la sedia sono arrivate martedì.", "V"), ("Al telefono Júlia ha parlato con un impiegato gentile.", "F"),
             ("La sedia è bianca, ma Júlia l'aveva scelta grigia.", "F"), ("Per un'azienda si scrive «Spettabile».", "V"),
             ("Per gli acquisti online ci sono quattordici giorni per restituire la merce.", "V"), ("La signora Rossi pensa che la lettera non serva a niente.", "F")]),
    talk2=["Perché la signora Rossi dice «Oh, cara…» quando legge la mail di Júlia?", "Che cosa pensi delle chat con i robot nei servizi clienti?",
           "Quando un prodotto non va, tu fai un reclamo o lasci perdere?"],
    n2=["B: 2 non risponde nessuno, solo un robot · 3 è grigia, Júlia l'aveva scelta bianca · 6 dice che funziona.", "Nota: la signora Rossi dà del tu a Júlia, Júlia le dà del Lei."],
    gref="lettera_formale",
    t4="la lettera formale",
    pA=("Completa con la formula giusta: Spettabile, Gentile, in merito, grata, riscontro.",
        [("___ servizio clienti,", "Spettabile"), ("___ signora Bianchi,", "Gentile"),
         ("Vi scrivo ___ all'ordine n. 4521.", "in merito"), ("Vi sarei ___ se poteste sostituire la scrivania.", "grata"),
         ("In attesa di un Vostro cortese ___, porgo distinti saluti.", "riscontro")]),
    pAw="22mm",
    pB=[("", ["La ringrazio", "Ti ringrazio"], "La ringrazio", " per la Sua risposta, dottor Neri."),
        ("", ["Potreste", "Potete"], "Potreste", " inviarmi una scrivania nuova?"),
        ("Cordiali ", ["saluti", "abbracci"], "saluti", ", Júlia Souza")],
    rule="Lo schema: <b>Spettabile</b> (azienda) / <b>Gentile</b> (persona) → <b>Vi / Le scrivo in merito a…</b> → il problema (date, numeri) → la richiesta al <b>condizionale</b> (<i>Vi sarei grato/a se…, Potrebbe…?</i>) → <b>In attesa di un cortese riscontro, cordiali / distinti saluti</b>. <b>Voi</b> a un'azienda, <b>Lei</b> a una persona.",
    use=["Come cominci una mail al tuo medico? E a una banca?", "Trasforma in formale: <i>Ciao, mi mandi il preventivo?</i>",
         "Racconta un reclamo che hai fatto (o che vorresti fare).", "Telefono, mail o lettera: che cosa funziona meglio per un reclamo?",
         "Come si chiude una mail formale in portoghese? E in italiano?"],
    n4="B2: <i>Potete</i> non è sbagliato, ma <i>Potreste</i> è più cortese.",
    t5="il reclamo al telefono",
    fl=(["spiegare il problema", "chiedere con cortesia", "insistere", "chiudere bene"],
        ["Chiamo in merito a… · Il prodotto è arrivato… · Il numero dell'ordine è…", "Potrebbe…? · Le sarei grato/a se… · Vorrei sapere se…",
         "Mi dispiace, ma… · Ho diritto a… · La garanzia è di due anni.", "La ringrazio. · Mi conferma per mail? · Buona giornata."]),
    pron=("Nelle lettere le abbreviazioni si scrivono corte ma si leggono intere: <b>Spett.le</b> = <i>Spettabile</i>, <b>Sig.ra</b> = <i>Signora</i>, <b>Dott.</b> = <i>Dottore</i>, <b>c.a.</b> = <i>alla cortese attenzione</i>. Il tono formale è calmo: frasi complete, niente fretta.",
          "Ascolta e ripeti le formule con un tono calmo e cortese. Poi leggi: «Spett.le servizio clienti, c.a. Sig.ra Bianchi.»"),
    task=("Il reclamo al telefono. Scegli un problema. L'insegnante lavora al servizio clienti: spiega il problema in modo formale (Lei!), chiedi una soluzione con il condizionale e non accettare la prima risposta. Alla fine detta all'insegnante l'oggetto, l'apertura e la chiusura della mail di conferma.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>un pacco mai arrivato</li><li>un volo cancellato</li><li>una camera d'albergo sporca</li><li>una bolletta sbagliata</li><li>un telefono che non funziona</li><li>un rimborso che non arriva</li></ul>",
          "Insegnante (servizio clienti): Mi dà il numero dell'ordine? · Purtroppo non possiamo… · Le offriamo un buono sconto. · Deve scrivere all'ufficio reclami. Lo studente insiste: Mi dispiace, ma ho diritto a… · Potrebbe parlare con un responsabile? Correggere subito ogni passaggio dal Lei al tu."),
    talk5=["Nel tuo paese le aziende rispondono bene ai reclami?", "È più facile protestare per scritto o a voce? Perché?"],
    n5=["far leggere ad alta voce le abbreviazioni sulla lavagna: Spett.le, Sig.ra, Dott., c.a.", "Pretendere il Lei dall'inizio alla fine; segnare ogni condizionale usato."],
    hA=("La lettera di Júlia. Scegli la forma giusta.",
        "<i>{0} servizio clienti, Vi scrivo {1} all'ordine n. 4521 del 2 giugno. La scrivania è arrivata danneggiata (una gamba è rotta) e la sedia non è del colore che avevo scelto. Vi sarei {2} se poteste sostituire la scrivania e ritirare la sedia. Ricordo che per i prodotti difettosi la garanzia legale è di due anni. In attesa di un Vostro cortese {3}, porgo {4} saluti. Júlia Souza</i>",
        [(["Spettabile", "Caro"], "Spettabile"), (["in merito", "in proposito"], "in merito"), (["grata", "grato"], "grata"),
         (["riscontro", "ritorno"], "riscontro"), (["distinti", "distinte"], "distinti")]),
    hB=("Trasforma le frasi informali in frasi formali.",
        [("Ciao, mi mandi il preventivo?", "Gentile signora…, potrebbe inviarmi il preventivo?"), ("Grazie mille!", "La ringrazio in anticipo."),
         ("Rispondimi presto!", "Resto in attesa di un Suo cortese riscontro.")]),
    watch=[("Assunto: reclamo", "Oggetto: reclamo", "<i>assunto</i> = preso a lavorare."),
           ("Spettabile signora Bianchi,", "Gentile signora Bianchi,", "<i>Spettabile</i> solo per aziende e uffici."),
           ("Aspetto il Vostro ritorno.", "Attendo un Vostro riscontro.", "<i>ritorno</i> = tornare, non risposta.")],
    write=("Scrivi una mail di reclamo per un problema vero o inventato: un acquisto, un albergo, un volo o un servizio.",
           "Spettabile…", ["apertura e chiusura formali", "il problema con data e numero", "una richiesta al condizionale"]),
    cando="So scrivere una lettera formale e un reclamo, con le formule giuste, il Lei e il condizionale di cortesia.",
    nH="Prossima unità: <i>Se l'avessi saputo…</i> (il periodo ipotetico dell'irrealtà).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 22 - Spettabile")
