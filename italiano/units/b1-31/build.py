# Speak! Progresso B1 - Unità 31 "Secondo me, invece…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 31", audio_json=os.path.join(HERE, "audio_it-b1-unita-31.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-31", "31.1 Secondo me, invece", "31.2 Ripeti")

C = dict(
    nn="31", title="Secondo me, invece…", subtitle="Il turismo e la città · <b>tuttavia, eppure, dunque, piuttosto</b>",
    cover=[("SAI FARE", "dare la tua opinione, dire se sei d'accordo, collegare gli argomenti in un dibattito"),
           ("LINGUA", "Secondo me, invece… · tuttavia · eppure · dunque · piuttosto che + infinito"),
           ("PRONUNCIA", "le doppie: eppure, piuttosto, tuttavia · l'intonazione del contrasto")],
    t1="troppi turisti?",
    start=["Guarda la foto. Ti piace visitare città piene di turisti? Perché?", "Nella tua città arrivano molti turisti? In quale periodo dell'anno?",
           "Quando viaggi, preferisci l'albergo o un appartamento?"],
    kw=[("la persona che visita una città in vacanza", "il turista"), ("la valigia con le ruote", "il trolley"),
        ("una casa affittata ai turisti per pochi giorni", "l'affitto breve"), ("la tassa che si paga per ogni notte in albergo", "la tassa di soggiorno"),
        ("la parte più antica della città", "il centro storico"), ("chi va ogni giorno a lavorare o a studiare in un'altra città", "il pendolare")],
    use_words=["Hai mai pagato la tassa di soggiorno? Dove?", "Conosci qualcuno che fa il pendolare? Quanto tempo ci mette?"],
    n1=["A: <i>affitto breve</i> = casa prenotata con le app per pochi giorni; <i>il pendolare</i> viene da <i>pendolo</i>: va e torna ogni giorno."],
    aims=["Secondo me, invece…: un dibattito al bar · Parliamone", "tuttavia, eppure, dunque, piuttosto che",
          "Più turisti o meno turisti? (31.2) · le doppie e l'intonazione", "Il messaggio di Davide · riscrivi · scrittura (100–150 parole)"],
    story="Sabato 4 settembre, aperitivo al Bar Giulia (Júlia, Marco, Giulia, Davide). Il giornale: record di turisti anche ad agosto. Marco si lamenta (la ferramenta di suo zio è diventata un negozio di mortadella); Giulia no: il bar non è mai stato così pieno. Il compagno di Davide non trova una stanza e fa il pendolare da Modena. Júlia: il turismo porta lavoro; piuttosto che vietare gli affitti brevi, bisognerebbe costruire case per studenti. Camila ha cominciato il lavoro mercoledì 1° settembre. Elena torna lunedì 6; Giulia parte sabato 11 per un mese in Sardegna («non sono una turista, vado in vacanza!»).",
    prob="Il brasiliano usa <i>entretanto</i> nel senso di «però» e lo traduce con <i>intanto</i>, che in italiano vuol dire «nel frattempo»: <s>È caro, intanto lo compro</s> → <i>tuttavia lo compro</i>. <i>Eppure</i> suona come «e anche» e viene usato per aggiungere (<s>Mi piace Bologna, eppure mi piace Firenze</s>): esprime invece un contrasto inaspettato. Altri errori: <i>piuttosto</i> senza <i>che/di</i> nel confronto (<s>il mare piuttosto la montagna</s>) e le doppie (<i>e<b>pp</b>ure, piu<b>tt</b>osto, tu<b>tt</b>avia</i>).",
    real="Molte città italiane, tra cui Bologna, fanno pagare ai turisti l'<b>imposta di soggiorno</b>, un tanto per notte. Dal 2024 Venezia chiede in alcuni giorni un <b>contributo di accesso</b> a chi visita la città in giornata. Dal 2025 ogni casa per <b>affitti brevi</b> deve avere un codice nazionale (CIN). Dal 2021 i <b>portici di Bologna</b> sono patrimonio UNESCO.",
    tr=("Secondo me, invece", "Ripeti: i connettivi"),
    gist=("Sabato sera, aperitivo al bar. Ascolta. Di che cosa discutono?",
          ["del turismo a Bologna", "del nuovo lavoro di Camila", "di un nuovo bar in centro"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Quest'estate il bar di Giulia ha lavorato poco.", "F"), ("La ferramenta dello zio di Marco adesso vende mortadella.", "V"),
             ("Il compagno di Davide ha trovato una stanza in centro.", "F"), ("Júlia pensa che il turismo porti anche lavoro.", "V"),
             ("Elena torna al bar lunedì.", "V"), ("Giulia va in Sardegna per una settimana.", "F")]),
    talk2=["Con chi sei d'accordo: con Marco o con Júlia? Perché?", "Giulia ha ragione? C'è differenza tra turista e persona in vacanza?",
           "Che cosa succede alla tua città quando arrivano molti turisti?"],
    n2=["B: 1 il bar non è mai stato così pieno · 3 non la trova, fa il pendolare da Modena · 6 un mese intero.", "Ripresa: Elena torna e Giulia va in Sardegna (unità 25); Camila comincia il contratto a settembre (unità 27)."],
    gref="connettivi_b1",
    t4="tuttavia, eppure, dunque",
    pA=("Completa con: tuttavia · eppure · dunque · piuttosto che · invece.",
        [("Il bar è sempre pieno; ___, Giulia non si lamenta.", "tuttavia"), ("Abita a Bologna da tre anni, ___ si perde ancora.", "eppure"),
         ("Non trova una stanza, ___ fa il pendolare.", "dunque"), ("___ vietare gli affitti brevi, costruirei case per studenti.", "Piuttosto che"),
         ("Marco vuole meno turisti; Júlia, ___, vede anche i vantaggi.", "invece")]),
    pAw="30mm",
    pB=[("Fa freddo, ", ["eppure", "dunque"], "eppure", " Davide esce senza giacca."),
        ("Ho perso il treno, ", ["dunque", "piuttosto"], "dunque", " arrivo tardi."),
        ("Di sera la piazza è ", ["piuttosto", "tuttavia"], "piuttosto", " tranquilla.")],
    rule="<b>tuttavia</b> = però (più formale) · <b>eppure</b> = contrasto inaspettato · <b>dunque</b> = quindi (conseguenza) · <b>piuttosto che / di</b> + infinito = invece di: <i>Piuttosto che vietare, costruiamo.</i> · <b>piuttosto</b> + aggettivo = abbastanza: <i>piuttosto caro</i>.",
    use=["Il turismo nella tua città: un vantaggio e un problema. Usa <i>tuttavia</i>.", "Una cosa che fai anche se sai che non dovresti. Usa <i>eppure</i>.",
         "Vacanze al mare o in città? Usa <i>piuttosto che</i>.", "I prezzi delle case salgono: una conseguenza. Usa <i>dunque</i>.",
         "Completa: <i>Molti dicono che… Secondo me, invece,…</i>"],
    n4="B1: c'è un contrasto ma in tono formale → <i>tuttavia</i>. B3: <i>piuttosto</i> + aggettivo = abbastanza.",
    t5="più turisti o meno turisti?",
    fl=(["dare un'opinione", "essere d'accordo", "non essere d'accordo", "proporre e concludere"],
        ["Secondo me… · Per quanto mi riguarda… · Ho l'impressione che…", "Hai ragione. · Sono d'accordo con te. · Su questo non c'è dubbio.",
         "Non sono affatto d'accordo. · Sì, però… · Eppure…", "Piuttosto che…, bisognerebbe… · Dunque… · Insomma…"]),
    pron=("Nei connettivi la doppia è lunga: <i>e<b>pp</b>ure, piu<b>tt</b>osto, tu<b>tt</b>avia</i>. Dopo il connettivo si fa una piccola pausa e la voce sale: <i>Tuttavia… ↗ guarda che cosa succede.</i>",
          "Ascolta e ripeti. Poi leggi: «Secondo me, invece, piuttosto che vietare, bisognerebbe costruire.»"),
    task=("Dibattito: «La mia città: più turisti o meno turisti?». Scegli una posizione; l'insegnante prende quella contraria. Discutete almeno tre temi della lista, usate i connettivi e alla fine fate una proposta comune.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>gli affitti brevi</li><li>la tassa di soggiorno</li><li>i negozi del centro</li><li>il lavoro nei bar e negli alberghi</li><li>il rumore e la sporcizia</li><li>i trasporti pubblici</li></ul>",
          "Insegnante: Secondo me il turismo è una risorsa… · Sì, però… · Dunque che cosa proponi? Lo studente: Non sono affatto d'accordo… · Tuttavia… · Eppure… · Piuttosto che…, bisognerebbe… Correggere <i>eppure</i> usato per aggiungere e <i>intanto</i> per «però»."),
    talk5=["Nel tuo paese ci sono città che soffrono per il turismo? Quali?", "Tu come turista che cosa fai per rispettare la città che visiti?"],
    n5=["far sentire le doppie e la pausa dopo il connettivo.", "Pretendere almeno quattro connettivi diversi e una proposta con <i>piuttosto che</i>."],
    hA=("Il messaggio di Davide a Elena. Scegli la forma giusta.",
        "<i>Ciao Elena! Lunedì torni al bar, {0} preparati: sabato Giulia parte per la Sardegna! Ieri sera abbiamo discusso di turismo per due ore. Marco dice che ci sono troppi turisti; Júlia, {1}, pensa che il turismo porti lavoro. Io sono d'accordo con Marco, {2} il mio compagno di corso non ha ancora trovato una stanza. {3} lamentarsi, però, bisognerebbe proporre qualcosa. E Giulia? Dice di non essere una turista, {4} va in vacanza un mese!</i>",
        [(["dunque", "eppure"], "dunque"), (["invece", "dunque"], "invece"), (["perché", "tuttavia"], "perché"),
         (["Piuttosto che", "Tuttavia"], "Piuttosto che"), (["eppure", "dunque"], "eppure")]),
    hB=("Unisci le due frasi con il connettivo tra parentesi.",
        [("Il centro è pieno di turisti. Marco ci va ogni giorno. (eppure)", "Il centro è pieno di turisti, eppure Marco ci va ogni giorno."),
         ("Le stanze costano troppo. Molti studenti fanno i pendolari. (dunque)", "Le stanze costano troppo, dunque molti studenti fanno i pendolari."),
         ("Non vietiamo gli affitti brevi: costruiamo case per studenti. (piuttosto che)", "Piuttosto che vietare gli affitti brevi, costruiamo case per studenti.")]),
    watch=[("Mi piace Bologna, eppure mi piace Firenze.", "Mi piace Bologna e anche Firenze.", "<i>eppure</i> esprime un contrasto, non un'aggiunta."),
           ("È caro. Intanto lo compro.", "È caro. Tuttavia lo compro.", "<i>intanto</i> vuol dire «nel frattempo»."),
           ("Preferisco il mare piuttosto la montagna.", "Preferisco il mare piuttosto che la montagna.", "nel confronto serve <i>piuttosto che / di</i>.")],
    write=("Scrivi un commento per il forum della tua città: «Turismo: risorsa o problema?». Dai la tua opinione con almeno due argomenti e fai una proposta.",
           "Secondo me il turismo…", ["almeno quattro connettivi diversi (<i>tuttavia, eppure, dunque, piuttosto che…</i>)", "un argomento a favore e uno contro", "una proposta finale con <i>piuttosto che</i> o <i>bisognerebbe</i>"]),
    cando="So dare e difendere un'opinione e collegare gli argomenti con tuttavia, eppure, dunque e piuttosto.",
    nH="Prossima unità: <i>Perché tutto funzioni</i> (affinché, prima che, senza che, purché, a meno che).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 31 - Secondo me, invece")
