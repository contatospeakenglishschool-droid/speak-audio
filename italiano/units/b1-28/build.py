# Speak! Progresso B1 - Unità 28 "Bisognerebbe che…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 28", audio_json=os.path.join(HERE, "audio_it-b1-unita-28.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-28", "28.1 Bisognerebbe che", "28.2 Ripeti")

C = dict(
    nn="28", title="Bisognerebbe che…", subtitle="Proposte e riunioni · <b>condizionale + che + congiuntivo imperfetto</b>",
    cover=[("SAI FARE", "fare proposte in una riunione, esprimere desideri e preferenze, protestare con gentilezza"),
           ("LINGUA", "Vorrei che… · Bisognerebbe che… · Sarebbe meglio che… · Sarebbe ora che…"),
           ("PRONUNCIA", "bisognerebbe, sarebbe: gn e la doppia b")],
    t1="vivere insieme",
    start=["Guarda la foto. Ti piacerebbe vivere in un palazzo così? Perché?", "Abiti in un condominio, in una casa o in un appartamento?",
           "Che cosa cambieresti nel posto dove abiti?"],
    kw=[("un palazzo con molti appartamenti e proprietari", "il condominio"), ("la riunione di tutti i proprietari", "l'assemblea"),
        ("la persona che gestisce il palazzo", "l'amministratore"), ("lo spazio all'aperto in mezzo al palazzo", "il cortile"),
        ("l'ingresso del palazzo, al piano terra", "l'androne"), ("dove si mettono le biciclette", "la rastrelliera")],
    use_words=["Nel tuo palazzo o nella tua strada c'è un cortile o un giardino?", "Hai mai partecipato a un'assemblea? Com'era?"],
    n1=["A: <i>condominio</i> = palazzo e anche le regole comuni; <i>ragioniere</i> = titolo di studio, si usa con gli amministratori."],
    aims=["Bisognerebbe che…: l'assemblea di condominio · Parliamone", "Vorrei che, bisognerebbe che, sarebbe meglio che + congiuntivo imperfetto",
          "L'assemblea (28.2) · gn e la doppia b", "Il verbale di Júlia · proposte per la tua città · scrittura (100–150 parole)"],
    story="Martedì 27 luglio, ore 21, assemblea di condominio in cortile, con l'amministratore ragionier Ferri (Lei con tutti). 1) Júlia vorrebbe che il cortile grigio diventasse un piccolo giardino (pianta, panchina, ombra) e fa il progetto gratis; la signora Rossi vorrebbe un posto per i bambini; Ferri: bisognerebbe che ogni famiglia pagasse 50 euro. 2) Camila chiede la rastrelliera per le bici, che Júlia aveva chiesto per iscritto più di un anno fa (A2); Ferri vuole rimandare a settembre, la signora Rossi: «Sarebbe ora che la mettesse!». 3) Rumori dopo le 22: Camila pensa di essere lei, ma è la radio del signore del quarto piano. 4) Varie: la signora Rossi vuole che il pranzo di Ferragosto in cortile diventi una tradizione ufficiale e che l'amministratore porti il vino. Tutto approvato all'unanimità («Bastava che qualcuno lo chiedesse… per la terza volta»).",
    prob="La struttura è uguale al portoghese (<i>eu queria que você viesse</i>), ma lo studente mette spesso l'indicativo (<i>vorrei che vieni</i>) o il congiuntivo presente dopo il condizionale (<i>vorrei che venga</i>, che si sente anche nel parlato italiano). Un altro errore è <i>che</i> + congiuntivo con lo stesso soggetto (<i>vorrei che io andassi</i> → <i>vorrei andare</i>). Lessico: <i>androne</i>, <i>assemblea</i>, <i>varie ed eventuali</i>.",
    real="In Italia molte persone vivono in <b>condominio</b>. Quando i proprietari sono più di otto, la legge chiede un <b>amministratore</b>, che organizza l'<b>assemblea</b> almeno una volta all'anno. L'ordine del giorno finisce quasi sempre con <i>varie ed eventuali</i> (le altre cose), il momento delle discussioni più lunghe. Il regolamento indica anche le ore di silenzio, di solito dopo cena e nel primo pomeriggio.",
    tr=("Bisognerebbe che…", "Ripeti: condizionale + congiuntivo imperfetto"),
    gist=("Martedì sera, in cortile. Ascolta. Che cosa succede?",
          ["un'assemblea di condominio con tre proposte", "una festa di Ferragosto", "un litigio tra Camila e la signora Rossi"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Júlia vuole essere pagata per il progetto del giardino.", "F"), ("Ogni famiglia dovrebbe pagare cinquanta euro.", "V"),
             ("Júlia aveva già chiesto la rastrelliera.", "V"), ("La musica dopo le ventidue è di Camila.", "F"),
             ("La signora Rossi vuole che l'amministratore porti il vino.", "V"), ("Le proposte non passano.", "F")]),
    talk2=["Quale proposta ti sembra la migliore? Perché?", "Com'è l'amministratore? Ti piacerebbe averlo nel tuo palazzo?",
           "Perché la signora Rossi dice «per la terza volta»?"],
    n2=["B: 1 lo fa gratis · 4 è la radio del signore del quarto piano · 6 passano all'unanimità.", "Júlia aveva scritto all'amministratore nell'A2 (unità 17)."],
    gref="condizionale_congiuntivo",
    t4="vorrei che…",
    pA=("Completa con il congiuntivo imperfetto del verbo tra parentesi.",
        [("Vorrei che il cortile ___ (diventare) un giardino.", "diventasse"), ("Bisognerebbe che ogni famiglia ___ (pagare) una quota.", "pagasse"),
         ("Sarebbe meglio che ne ___ (parlare, noi) a settembre.", "parlassimo"), ("Preferirei che me lo ___ (dire, voi) direttamente.", "diceste"),
         ("Sarebbe ora che l'amministratore ___ (mettere) la rastrelliera!", "mettesse")]),
    pAw="26mm",
    pB=[("Vorrei che tu ", ["vieni", "venissi"], "venissi", " all'assemblea."),
        ("Mi piacerebbe ", ["che io avessi", "avere"], "avere", " un giardino."),
        ("Bisognerebbe che i vicini ", ["facessero", "fanno"], "facessero", " meno rumore.")],
    rule="<b>Condizionale</b> (<i>vorrei, preferirei, bisognerebbe, sarebbe meglio / bello / ora, mi piacerebbe</i>) + <b>che</b> + <b>congiuntivo imperfetto</b>: <i>Vorrei che il cortile diventasse un giardino.</i> Stesso soggetto → <b>infinito</b>: <i>Vorrei fare il progetto.</i>",
    use=["Che cosa vorresti che cambiasse nella tua città?", "Che cosa bisognerebbe che facesse il governo per i giovani?",
         "Al lavoro, che cosa preferiresti che facessero i tuoi colleghi?", "Completa: <i>Sarebbe ora che…</i>",
         "Che cosa ti piacerebbe che ti regalassero per il compleanno?"],
    n4="B2: stesso soggetto (io) → infinito.",
    t5="l'assemblea",
    fl=(["proporre", "chiedere con gentilezza", "protestare", "decidere"],
        ["Io avrei una proposta. · Vorrei che… · Mi piacerebbe che…", "Sarebbe possibile che…? · Bisognerebbe che…",
         "Sarebbe ora che… · Non è giusto che… · Preferirei che…", "Votiamo? · Sono d'accordo. · Allora facciamo così."]),
    pron=("In <b>bisognerebbe</b> si sentono il suono <b>gn</b> (come <i>nh</i> in portoghese: <i>bi-so-<b>gne</b>-REB-be</i>) e la <b>doppia b</b>, più lunga. Lo stesso nel condizionale: <i>sa<b>reb</b>be</i>, <i>vor<b>reb</b>be</i>, <i>piace<b>reb</b>be</i>. L'accento è sempre su <i>-rèb-</i>.",
          "Ascolta e ripeti. Poi leggi: «Bisognerebbe che il signore del quarto piano abbassasse la radio.»"),
    task=("L'assemblea. Scegliete un luogo (della lista o vostro). Prepara tre proposte con vorrei che, bisognerebbe che, sarebbe meglio che. L'insegnante fa l'amministratore (o il capo) difficile: discutete, protestate con gentilezza (sarebbe ora che…) e alla fine votate.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>il tuo palazzo</li><li>il tuo ufficio</li><li>la tua città</li><li>la tua scuola di lingue</li><li>la tua famiglia (le vacanze)</li><li>il gruppo di amici (il weekend)</li></ul>",
          "Insegnante (amministratore difficile): Costa troppo. · Ne parliamo a settembre. · Nessuno l'ha mai chiesto. · Bisognerebbe che qualcuno se ne occupasse… Lo studente insiste: Sarebbe ora che… · Mi piacerebbe che… · Preferirei che decidessimo stasera. Correggere <i>vorrei che vieni</i> → <i>venissi</i>."),
    talk5=["Nel tuo paese le riunioni di condominio sono tranquille o animate?", "È più facile vivere in una casa o in un condominio?"],
    n5=["far dire <i>bisognerebbe</i> lentamente, sillaba per sillaba, poi veloce.", "Pretendere almeno tre forme diverse del condizionale + congiuntivo."],
    hA=("Il verbale dell'assemblea scritto da Júlia. Scegli la forma giusta.",
        "<i>Verbale dell'assemblea del 27 luglio. La sig.ra Souza propone che il cortile {0} un piccolo giardino; il progetto è gratuito. L'amministratore osserva che bisognerebbe che ogni famiglia {1} una quota di 50 euro. Camila (terzo piano) chiede che {2} una rastrelliera; la sig.ra Rossi aggiunge che sarebbe ora che l'amministratore la {3}. Per Ferragosto la sig.ra Rossi vorrebbe che l'amministratore {4} il vino. Tutte le proposte sono approvate all'unanimità.</i>",
        [(["diventi", "diventa"], "diventi"), (["pagasse", "paga"], "pagasse"), (["si metta", "si mette"], "si metta"),
         (["mettesse", "metterebbe"], "mettesse"), (["portasse", "porta"], "portasse")]),
    hB=("Fai una proposta gentile con l'espressione tra parentesi.",
        [("I vicini fanno rumore di notte. (preferirei che)", "Preferirei che i vicini non facessero rumore di notte."), ("Nessuno pulisce le scale. (bisognerebbe che)", "Bisognerebbe che qualcuno pulisse le scale."),
         ("Il comune non apre la biblioteca la domenica. (sarebbe bello che)", "Sarebbe bello che il comune aprisse la biblioteca la domenica.")]),
    watch=[("Vorrei che tu vieni.", "Vorrei che tu venissi.", "dopo il condizionale: congiuntivo imperfetto."),
           ("Vorrei che io andassi al mare.", "Vorrei andare al mare.", "stesso soggetto: infinito."),
           ("Il sindaco del palazzo è Ferri.", "L'amministratore del palazzo è Ferri.", "<i>sindaco</i> = capo del comune (≠ <i>síndico</i>).")],
    write=("Scrivi una lettera all'amministratore, al sindaco o al tuo capo con tre proposte per migliorare il tuo palazzo, la tua città o il tuo ufficio.",
           "Gentile…, vorrei che…", ["tre espressioni diverse (<i>vorrei che, bisognerebbe che, sarebbe meglio che</i>)", "un <i>sarebbe ora che…</i>", "apertura e chiusura formali (unità 22)"]),
    cando="So fare proposte, esprimere desideri e protestare con gentilezza con il condizionale + congiuntivo imperfetto.",
    nH="Prossima unità: <i>Me lo faccio fare</i> (fare + infinito, farsi fare).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 28 - Bisognerebbe che")
