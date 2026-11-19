# Speak! Progresso B1 - Unità 05 "Il Made in Italy" - FORMATO RIDOTTO (rifatta 2026-11-19 con italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 05", audio_json=os.path.join(HERE, "audio_it-b1-unita-05.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-05", "05.1 Il Made in Italy", "05.2 Ripeti")

C = dict(
    nn="05", title="Il Made in Italy", subtitle="Prodotti tipici e marchi · <b>il congiuntivo presente</b>",
    cover=[("SAI FARE", "presentare e consigliare un prodotto, esprimere opinioni, desideri, paure e necessità"),
           ("LINGUA", "Spero che ti piaccia. · È importante che lo sappiate. · Ho paura che si rompa."),
           ("PRONUNCIA", "le doppie del congiuntivo: «faccia», «sappia», «abbia»")],
    t1="il Made in Italy",
    start=["Quali prodotti italiani conosci? Ne compri qualcuno in Brasile?", "Che cosa ti fa pensare la parola «Made in Italy»: moda, cibo, macchine…?",
           "Quando compri un prodotto, leggi l'etichetta?"],
    kw=[("un grande contenitore di legno", "una botte"), ("diventare vecchio", "invecchiare"),
        ("il foglietto con le informazioni sul prodotto", "un'etichetta"), ("il controllo delle merci alla frontiera", "la dogana"),
        ("mandare per posta", "spedire"), ("provare un cibo per sentire il sapore", "assaggiare")],
    use_words=["Hai mai spedito un pacco all'estero? Che cosa c'era dentro?", "Qual è il cibo più strano che hai assaggiato?"],
    n1=["A: l'<i>acetaia</i> (nell'ascolto) è il luogo dove si produce l'aceto balsamico: suffisso dei luoghi di produzione <i>-aia</i>."],
    aims=["Il Made in Italy: visita a un'acetaia di Modena · Parliamone", "Il congiuntivo presente: tutte le persone, irregolari, quando si usa",
          "Consigliare un prodotto (05.2) · gioco di ruolo: spedire un regalo", "Il biglietto di Marco a suo padre · completare · scrittura (100–150 parole)"],
    story="Sabato 23 gennaio Júlia, Marco e Camila vanno a Modena. Prima delle tigelle visitano un'acetaia: la guida spiega che il balsamico tradizionale invecchia almeno dodici anni e che all'estero molti prodotti hanno un nome italiano ma non vengono dall'Italia (bisogna cercare la sigla DOP, come per il <i>parmesão</i> brasiliano). Júlia vorrebbe mandare una bottiglia ai genitori ma ha paura che si rompa: l'acetaia spedisce in tutto il mondo. Marco ne compra una per il padre; Camila ne ha già tre nella borsa per gli amici di Recife.",
    prob="Il portoghese ha il <i>subjuntivo</i> (<i>espero que você goste</i>), quindi l'idea è facile; ma il brasiliano parlato usa spesso l'indicativo (<i>acho que é</i>) e lo studente dice <i>penso che è</i>. Problema di forma: <i>sapete / sappiate</i>. Falsi amici: <i>presente</i> ≠ <i>regalo</i>; <i>squisito</i> = buonissimo (≠ <i>esquisito</i>); <i>legittimo</i> = legale (≠ <i>legítimo</i> = autentico).",
    real="DOP e IGP sono marchi europei che proteggono i prodotti legati a un territorio. L'Aceto Balsamico Tradizionale di Modena DOP invecchia almeno 12 anni (<i>extravecchio</i>: 25). All'estero l'<i>Italian sounding</i> (nomi e bandiere italiane su prodotti non italiani) vale più delle esportazioni vere. Le tigelle sono piccoli pani rotondi dell'Appennino modenese.",
    tr=("Il Made in Italy", "Ripeti: il congiuntivo presente"),
    gist=("Sabato a Modena, in un'acetaia. Ascolta. Di che cosa parlano soprattutto?",
          ["dell'aceto balsamico, dei prodotti falsi e dei regali", "del prezzo della benzina", "di una partita di calcio"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("L'aceto balsamico tradizionale invecchia almeno dodici anni.", "V"), ("In Brasile il balsamico del supermercato è molto caro.", "F"),
             ("La guida consiglia di cercare la sigla DOP.", "V"), ("Júlia ha paura che il pacco arrivi in ritardo.", "F"),
             ("L'acetaia spedisce anche all'estero.", "V"), ("Camila non ha comprato niente.", "F")]),
    talk2=["Perché, secondo te, all'estero tanti prodotti hanno un nome italiano?", "Marco dice: «Spero che gli piaccia». È sicuro del suo regalo?",
           "Quale prodotto brasiliano porteresti a un amico italiano?"],
    n2=["B: 2 costa pochissimo · 4 ha paura che la bottiglia si rompa · 6 ne ha già tre nella borsa.", "<i>Basta che</i> e <i>peccato che</i> vogliono il congiuntivo."],
    gref="congiuntivo_sistema",
    t4="il congiuntivo presente",
    pA=("Completa con il congiuntivo del verbo tra parentesi.",
        [("Spero che voi (venire) ___ a Modena con noi.", "veniate"), ("È strano che loro non (sapere) ___ che cos'è la DOP.", "sappiano"),
         ("Voglio che tu (dire) ___ la verità: ti piace?", "dica"), ("Peccato che le tigelle (finire) ___ così presto!", "finiscano"),
         ("Ho paura che il pacco (essere) ___ troppo pesante.", "sia")]),
    pB=[("So che il parmigiano ", ["viene", "venga"], "viene", " da Parma e Reggio Emilia."),
        ("Spero che il pacco ", ["arrivi", "arriva"], "arrivi", " prima di Carnevale."),
        ("Secondo me il balsamico ", ["è", "sia"], "è", " troppo caro.")],
    rule="Il <b>congiuntivo presente</b> si usa dopo <b>opinione</b> (<i>penso che</i>), <b>volontà</b> (<i>voglio che</i>), <b>emozione</b> (<i>spero, ho paura, peccato che</i>), <b>necessità</b> (<i>è importante, bisogna, basta che</i>) e <b>giudizio</b> (<i>è giusto che</i>). Per i fatti sicuri: indicativo (<i>so che, secondo me</i>). Desinenze: <i>-are</i> → <b>-i</b>, <i>-ere / -ire</i> → <b>-a</b>; noi <b>-iamo</b>, voi <b>-iate</b>, loro <b>-ino / -ano</b>.",
    use=["Un amico viene in Brasile: che cosa è importante che faccia? <i>È importante che…</i>", "Che cosa speri per questo fine settimana? <i>Spero che…</i>",
         "Di che cosa hai paura quando spedisci un pacco?", "Che cosa pensi del Made in Italy? <i>Penso che sia…</i>", "Che cosa vuoi che faccia il tuo insegnante?"],
    n4="Pratica B3: <i>secondo me</i> vuole l'indicativo; con <i>penso che</i> sarebbe <i>sia</i>.",
    t5="consigliare un prodotto",
    fl=(["consigliare", "dare un'opinione", "desideri e speranze", "paure e dubbi"],
        ["È importante che tu provi… · Bisogna che… · Basta che…", "Penso che sia… · Mi sembra che… · Non credo che…",
         "Spero che… · Voglio che… · Sono contento/a che…", "Ho paura che… · Peccato che… · È strano che…"]),
    pron=("Molti congiuntivi irregolari hanno la doppia: <i>fa<b>cc</b>ia, sa<b>pp</b>ia, a<b>bb</b>ia, pia<b>cc</b>ia, po<b>ss</b>a</i>. La doppia distingue anche <i>sa<b>pp</b>iate</i> (congiuntivo) da <i>sapete</i> (indicativo).",
          "Ascolta e ripeti. Poi l'insegnante dice «sapete» o «sappiate»: indicativo o congiuntivo?"),
    task=("Gioco di ruolo. Sei in un negozio di prodotti tipici a Bologna e vuoi spedire un regalo in Brasile; l'insegnante è il commesso. Poi presenta tu un prodotto tipico brasiliano all'insegnante: perché è importante che lo provi?",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>che cos'è e dove si produce</li><li>come si usa o si mangia</li><li>come riconoscere il prodotto vero</li></ul>",
          "Insegnante: Buongiorno, posso aiutarLa? · Per chi è il regalo? · Le consiglio il Parmigiano di 24 mesi: è importante che sia sottovuoto. · Per la spedizione bisogna che compili questo modulo. · Ha paura che si rompa qualcosa? Lo imballiamo noi. · Sono 48 euro, più la spedizione."),
    talk5=["È giusto che i prodotti tipici siano protetti dalla legge?", "Vale la pena pagare di più per un prodotto originale?"],
    n5=["frasi per il gioco: <i>So che lo sapete · Voglio che lo sappiate · Penso che abbiate ragione · Avete ragione.</i>", "Registro formale (<i>Lei</i>). Idee per lo studente: caffè, cachaça, formaggio della Serra da Canastra."],
    hA=("Marco mette un biglietto nel pacco per suo padre. Scegli la forma giusta.",
        "<i>Caro papà, ti mando questa bottiglia da Modena. So che tu {0} il balsamico della bisnonna, ma spero che anche questo {1}. La guida dice che è importante che tu lo {2} lontano dal sole. Peccato che io non {3} venire a Firenze questo fine settimana. E per Pasqua bisogna che voi {4} la data del pranzo presto! Un abbraccio, Marco</i>",
        [(["preferisci", "preferisca"], "preferisci"), (["ti piaccia", "ti piace"], "ti piaccia"), (["tenga", "tieni"], "tenga"),
         (["possa", "posso"], "possa"), (["decidiate", "decidete"], "decidiate")]),
    hB=("Riscrivi con l'espressione tra parentesi e il congiuntivo.",
        [("Il regalo ti piace. (spero che)", "Spero che il regalo ti piaccia."), ("Voi leggete l'etichetta. (è importante che)", "È importante che leggiate l'etichetta."),
         ("La bottiglia si rompe. (ho paura che)", "Ho paura che la bottiglia si rompa.")]),
    watch=[("Ho comprato un presente per mia madre.", "Ho comprato un regalo per mia madre.", "<i>presente</i> = il tempo di oggi."),
           ("Questo vino è esquisito (= strano).", "Questo vino è strano.", "<i>squisito</i> = buonissimo!"),
           ("Spero che ti piace.", "Spero che ti piaccia.", "<i>sperare che</i> + congiuntivo.")],
    write=("Una recensione online di un negozio, di un mercato o di un prodotto che conosci bene.",
           "Un'esperienza da non perdere! …", ["cinque congiuntivi con persone diverse", "un'opinione (<i>penso che…</i>)", "una necessità (<i>è importante che</i>)", "un consiglio finale"]),
    cando="So presentare e consigliare un prodotto con il congiuntivo presente.",
    nH="Prossima unità: <i>Può darsi che…</i> (il congiuntivo passato).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 05 - Il Made in Italy")
