# Speak! Indipendenza B2 - Unità 04 "Secondo indiscrezioni" - formato ridotto (italiano/lean_b1.py, level="B2"), pagina 2 = LETTURA
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Indipendenza"
setup(band="B2 · UNITÀ 04", audio_json=os.path.join(HERE, "audio_it-b2-unita-04.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b2-unita-04", "04.1 L'albergo sul giornale", "04.2 Ripeti")

ARTICLE = """<p style="margin:0 0 1mm">Un albergo di lusso con piscina sul tetto: è quello che <b>starebbe nascendo</b> in un palazzo del Seicento in pieno centro storico. Secondo indiscrezioni, i lavori, cominciati a febbraio, <b>sarebbero</b> già in ritardo di due mesi, e il proprietario, il dottor Galli, <b>avrebbe speso</b> più di dieci milioni di euro.</p>
<p style="margin:0 0 1mm">Pare che le camere <b>siano</b> una ventina, tutte con vista sulle torri, e si dice che una notte <b>possa</b> costare fino a mille euro. Alcuni vicini sostengono che sul tetto <b>sia prevista</b> una piscina; altri parlano di un ristorante panoramico. Secondo una fonte vicina al cantiere, all'inaugurazione <b>parteciperebbe</b> anche un famoso attore americano.</p>
<p style="margin:0 0 1mm">Non tutti, però, sono contenti. «Ho paura che ci siano feste fino alle due di notte», racconta una residente. «Per noi sarebbe un disastro.» Altri invece sono favorevoli: «Il palazzo era chiuso da anni. Meglio un albergo che un edificio abbandonato.»</p>
<p style="margin:0">Contattato dal nostro giornale, il dottor Galli non ha voluto commentare: «Leggerete tutto a settembre.» Anche lo studio di architettura che segue il progetto non ha rilasciato dichiarazioni. Una cosa è certa: il progetto ha il parere favorevole della Soprintendenza. Per tutto il resto, il condizionale è d'obbligo.</p>"""

C = dict(
    level="B2", words="150–200",
    reading=dict(kicker="CRONACA DI BOLOGNA · MERCOLEDÌ 15 MARZO", head="Centro storico: un albergo di lusso nel palazzo del Seicento?", body=ARTICLE),
    nn="04", title="Secondo indiscrezioni", subtitle="L'albergo di Galli sul giornale · <b>condizionale giornalistico e pare che + congiuntivo</b>",
    cover=[("SAI FARE", "capire una notizia di cronaca, riferire voci non confermate"),
           ("LINGUA", "avrebbe speso · sarebbero · pare che sia · si dice che"),
           ("PRONUNCIA", "la doppia <i>b</i> del condizionale: <i>sarebbe, avrebbe</i>")],
    t1="le notizie",
    start=["Guarda la foto. Dove leggi le notizie: giornale, siti, social?", "Leggi le notizie della tua città? Di che cosa parlano di solito?",
           "Hai mai creduto a una notizia che poi era falsa?"],
    kw=[("una notizia non ufficiale, uscita in segreto", "l'indiscrezione"), ("la persona o il documento da cui arriva una notizia", "la fonte"),
        ("le notizie sui fatti della città: cantieri, quartieri, incidenti", "la cronaca"), ("dire in pubblico, per esempio a un giornalista", "dichiarare"),
        ("una cosa che dicono in tanti, ma che nessuno ha confermato", "la voce"), ("dire in modo ufficiale che una notizia è vera", "confermare")],
    use_words=["Che cosa fai quando senti una voce su una persona che conosci?", "Quale fonte di notizie ti sembra più affidabile? Perché?"],
    n1=["A: <i>la voce</i> = boato, rumor (e anche la voz!) · <i>la cronaca</i> = noticiário local, policial.", "Ripresa: il cantiere dell'albergo di Galli (B2 01) e la terrazza con bar sul tetto (B1 32)."],
    aims=["L'albergo sul giornale: lettura e audio · Parliamone", "condizionale giornalistico (presente e passato) · pare che / si dice che + congiuntivo",
          "Il giornalista curioso · ripeti (04.2) · la doppia b del condizionale", "La lettera del dottor Galli al giornale · trasforma · scrittura (150–200 parole)"],
    story="Mercoledì 15 marzo 2028. La cronaca locale pubblica un articolo sull'albergo del dottor Galli pieno di voci: lusso, piscina sul tetto, due mesi di ritardo, dieci milioni spesi, camere da mille euro, un attore americano all'inaugurazione. Galli non commenta («Leggerete tutto a settembre»), lo studio di Júlia e Marco non rilascia dichiarazioni. Che cosa sappiamo davvero: il cantiere è cominciato il 7 febbraio (B2 01), l'apertura è prevista a settembre, sul tetto ci sarà la terrazza con bar e la pergola di legno chiaro di Júlia (non una piscina), la Soprintendenza ha dato parere favorevole. Nei compiti: la lettera del dottor Galli al direttore del giornale.",
    prob="Qui il portoghese aiuta: anche i giornali brasiliani usano il futuro do pretérito per le notizie non confermate (<i>o empresário <b>teria gastado</b></i>). Gli errori sono altri: 1) l'ausiliare del passato: <i><b>sarebbe</b> stato, <b>sarebbero</b> cominciati</i> (non <s>avrebbe stato</s>); 2) <i>parece que</i> + indicativo, ma <b>pare che, sembra che, si dice che</b> + <b>congiuntivo</b>: <i>pare che <b>sia</b></i> (non <s>pare che è</s>); 3) <b>a quanto pare</b> (= pelo jeito) vuole l'indicativo e niente <i>che</i>; 4) la doppia <i>b</i>: <i>sarebbe</i>, non <s>sarebe</s>.",
    real="Nei giornali italiani il <b>condizionale</b> segnala una notizia <b>non confermata</b>: il giornalista riferisce senza garantire («il condizionale è d'obbligo»). Le pagine di <b>cronaca locale</b> raccontano cantieri, negozi e quartieri. Chi ritiene falsa una notizia che lo riguarda può chiedere al giornale una <b>rettifica</b>: la prevede la legge sulla stampa del 1948.",
    tr=("L'albergo sul giornale", "Ripeti: le voci"),
    gist=("Leggi velocemente. Le notizie dell'articolo sono…",
          ["soprattutto voci non confermate", "fatti sicuri, confermati dal proprietario", "una pubblicità dell'albergo"]),
    detail=("vf", "Leggi di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("I lavori sono cominciati a febbraio.", "V"), ("Il giornale è sicuro che i lavori sono in ritardo.", "F"),
             ("Secondo alcuni, una notte potrebbe costare mille euro.", "V"), ("Tutti i vicini sono contrari all'albergo.", "F"),
             ("Il dottor Galli ha raccontato molti dettagli al giornale.", "F"), ("Il parere della Soprintendenza è una notizia sicura.", "V")]),
    talk2=["Quali notizie dell'articolo sono vere? Che cosa sai dalla storia?", "Come reagirà il dottor Galli? E Júlia?"],
    n2=["B: 2 «sarebbero già in ritardo» è una voce · 4 alcuni sono favorevoli · 5 «non ha voluto commentare».",
        "Talk2, che cosa sappiamo davvero: cantiere cominciato il 7 febbraio (B2 01), apertura a settembre, sul tetto la terrazza con bar e la pergola di Júlia, non una piscina."],
    gref="condizionale_giornalistico_b2",
    t4="la notizia non confermata",
    pA=("Trasforma in voce: metti il verbo al condizionale (presente o passato).",
        [("Secondo indiscrezioni, l'albergo ___ (avere) venti camere.", "avrebbe"), ("I lavori ___ (cominciare) con due settimane di ritardo.", "sarebbero cominciati"),
         ("Il proprietario ___ (spendere) dieci milioni.", "avrebbe speso"), ("Un attore americano ___ (venire) all'inaugurazione.", "verrebbe"),
         ("I vicini ___ (essere) preoccupati per la musica.", "sarebbero")]),
    pAw="30mm",
    pB=[("Pare che il palazzo ", ["sia", "è"], "sia", " del Seicento."),
        ("A quanto pare, il dottor Galli ", ["non vuole", "non voglia"], "non vuole", " parlare."),
        ("Si dice che la Soprintendenza ", ["abbia detto", "ha detto"], "abbia detto", " di sì.")],
    rule="Il <b>condizionale giornalistico</b> riferisce una notizia non confermata: <b>presente</b> per oggi e per il futuro (<i>l'albergo aprirebbe a settembre</i>), <b>passato</b> per un fatto già successo (<i>avrebbe speso, sarebbero cominciati</i>). <b>Pare che, sembra che, si dice che</b> + congiuntivo (<i>pare che sia, si dice che abbia speso</i>); <b>a quanto pare</b> + indicativo; <b>secondo</b> + fonte + condizionale.",
    use=["Che cosa si dice nella tua città in questo periodo? (Si dice che…)", "Racconta una voce che hai sentito sul lavoro, con il condizionale.",
         "Secondo i giornali, che cosa succederebbe nel tuo paese l'anno prossimo?", "Pare che gli italiani… : completa con un luogo comune e discutilo.",
         "Che cosa hai letto ultimamente che, a quanto pare, non era vero?"],
    n4="A: 2 <i>cominciare</i> qui vuole <i>essere</i> (<i>i lavori sono cominciati</i>, B2 01) → <i>sarebbero cominciati</i> · 3 <i>avrebbe speso</i>. B: <i>a quanto pare</i> + indicativo; <i>pare che, si dice che</i> + congiuntivo.",
    t5="riferire le voci",
    fl=(["dare una voce", "citare la fonte", "prendere le distanze", "confermare o smentire"],
        ["Pare che… · Si dice che… · Gira voce che… (+ congiuntivo)", "Secondo… · Stando a… · A quanto pare… (+ indicativo)",
         "Sarebbe… · Avrebbe detto… · Il condizionale è d'obbligo.", "È confermato. · Non è vero che… (+ congiuntivo) · Smentisco."]),
    pron=("Nel condizionale la <i>b</i> è doppia e lunga: <i>sarebbe, avrebbe, parteciperebbe</i>; al plurale <i>sarebbero, avrebbero</i>. L'accento cade su <i>-rèb-</i>: <i>sa-RÈB-be</i>.",
          "Ascolta e ripeti. Poi leggi: «Secondo indiscrezioni, i lavori sarebbero già in ritardo.»"),
    task=("Il giornalista curioso: l'insegnante è un/una giornalista e ti chiede di una voce della tua città o del tuo lavoro. Rispondi con prudenza e separa i fatti dalle voci. Poi scambiatevi i ruoli.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>È vero che…?</li><li>Che cosa si dice in giro?</li><li>Chi gliel'ha detto?</li><li>Quanto sarebbe costato?</li><li>Quando aprirebbe?</li><li>Lei ci crede?</li></ul>",
          "Insegnante: Si dice che… È vero? Lo studente: Pare che… · Secondo… · Non è confermato. Nel riassunto: «Secondo il nostro intervistato, il cantiere sarebbe…». Correggere <i>pare che</i> + indicativo e <i>avrebbe stato</i>."),
    talk5=["Le voci di quartiere sono pericolose o servono a qualcosa?", "Un giornale deve pubblicare una notizia non confermata? Quando sì?"],
    n5=["Insistere sulla doppia <i>b</i>: <i>sarebbe</i>, non <i>sarebe</i>.", "Pretendere almeno tre condizionali giornalistici e due <i>pare che / si dice che</i> + congiuntivo nel riassunto."],
    hA=("La lettera del dottor Galli al direttore del giornale. Scegli la forma giusta.",
        "<i>Egregio direttore, nell'articolo di ieri si legge che i lavori nel mio palazzo {0} già in ritardo. Non è vero. Si dice anche che sul tetto {1} una piscina: in realtà ci sarà una terrazza con una pergola. Pare che io {2} dieci milioni di euro: magari! L'albergo {3} a settembre, come previsto. E secondo il Suo giornale, all'inaugurazione {4} un attore americano: lo inviterò volentieri, se mi manda il suo numero. Distinti saluti, dott. Galli</i>",
        [(["sarebbero", "siano"], "sarebbero"), (["ci sia", "c'è"], "ci sia"), (["abbia speso", "ho speso"], "abbia speso"), (["aprirà", "aprirebbe"], "aprirà"), (["parteciperebbe", "partecipi"], "parteciperebbe")]),
    hB=("Trasforma il fatto in voce: usa il condizionale o pare che + congiuntivo.",
        [("Il sindaco ha visitato il cantiere.", "Il sindaco avrebbe visitato il cantiere."),
         ("L'albergo ha venti camere.", "L'albergo avrebbe venti camere. / Pare che l'albergo abbia venti camere."),
         ("I lavori finiscono a luglio.", "I lavori finirebbero a luglio. / Si dice che i lavori finiscano a luglio.")]),
    watch=[("Pare che i lavori sono in ritardo.", "Pare che i lavori <b>siano</b> in ritardo.", "<i>pare che, si dice che</i> + congiuntivo."),
           ("Il proprietario avrebbe stato a Roma.", "Il proprietario <b>sarebbe</b> stato a Roma.", "<i>essere</i> → <i>sarebbe stato</i>."),
           ("A quanto pare che è vero.", "<b>A quanto pare</b> è vero.", "<i>a quanto pare</i> + indicativo, senza <i>che</i>.")],
    write=("Scrivi un articolo di cronaca su una notizia della tua città (un nuovo negozio, un cantiere, un evento). Separa i fatti sicuri dalle voci.",
           "Secondo indiscrezioni…", ["almeno quattro verbi al condizionale giornalistico (presente e passato)", "almeno due frasi con <i>pare che / si dice che</i> + congiuntivo",
                                     "un titolo e una citazione tra virgolette («…», ha dichiarato…)"]),
    cando="So capire e scrivere una notizia non confermata con il condizionale giornalistico e pare che / si dice che + congiuntivo.",
    nH="Prossima unità: <i>Più di quanto pensassi</i> (comparativi con frase; il costo della vita a Bologna e a Belo Horizonte).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B2 Indipendenza 04 - Secondo indiscrezioni")
