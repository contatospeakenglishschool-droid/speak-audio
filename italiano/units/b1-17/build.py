# Speak! Progresso B1 - Unità 17 "La famiglia oggi" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 17", audio_json=os.path.join(HERE, "audio_it-b1-unita-17.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-17", "17.1 La famiglia oggi", "17.2 Ripeti")

C = dict(
    nn="17", title="La famiglia oggi", subtitle="Modelli di famiglia · <b>benché, sebbene, nonostante, anche se</b>",
    cover=[("SAI FARE", "parlare di modelli di famiglia, confrontare Italia e Brasile, difendere una scelta"),
           ("LINGUA", "Benché sia piccola… · Sebbene viva da sola… · Anche se non sei sposata…"),
           ("PRONUNCIA", "l'accento delle congiunzioni: benCHÉ, sebBEne, nonoSTANte")],
    t1="la famiglia",
    start=["Guarda la foto. Chi sono queste persone? Che cosa si festeggia?", "Com'è il pranzo della domenica nella tua famiglia?",
           "Quante persone vivono a casa tua?"],
    kw=[("il figlio di tuo figlio o di tua figlia", "un nipote"), ("lasciare la casa dei genitori", "uscire di casa"),
        ("due persone che stanno insieme", "una coppia"), ("la persona con cui stai insieme, prima del matrimonio", "il fidanzato / la fidanzata"),
        ("far conoscere una persona a qualcuno", "presentare"), ("essere importante", "contare")],
    use_words=["A che età sei uscito/a di casa? O vivi ancora con la tua famiglia?", "Nella vita, che cosa conta di più per te?"],
    n1=["A: <i>nipote</i> = <i>neto</i> e anche <i>sobrinho</i>; <i>fidanzato</i> = <i>namorado</i> (non solo <i>noivo</i>)."],
    aims=["La famiglia oggi: il pranzo dalla signora Rossi · Parliamone", "Benché, sebbene, nonostante + congiuntivo · anche se + indicativo",
          "Difendere una scelta (17.2) · discussione: le famiglie di oggi", "La lettera della signora Rossi a Franco · concessive · scrittura (100–150 parole)"],
    story="Domenica 18 aprile, dopo l'inaugurazione della biblioteca: la signora Rossi invita a pranzo Júlia, Bruno, Lúcia e Roberto (tagliatelle). Vive da sola da tanti anni ma non si sente sola (il fratello Franco, i vicini, Júlia). In Brasile la domenica sono in venti (e parla sempre la mamma). Lúcia: Júlia ha 32 anni e non è sposata; la signora Rossi spiega che in Italia è normale. Bruno non ha ancora presentato Chiara ai genitori (fidanzati da più di un anno): lo farà martedì. Júlia: «Giulia, Davide, Camila, Marco sono la mia famiglia italiana». Lúcia accetta («È questo che conta»), ma vuole Júlia a casa per Natale: «Ci penso».",
    prob="La struttura è uguale al portoghese (<i>embora seja</i>), ma lo studente mette l'indicativo dopo <i>benché</i> (<i>benché è</i>), il congiuntivo dopo <i>anche se</i> (calco di <i>mesmo que seja</i>) e traduce <i>apesar de</i> + infinito con <i>nonostante di</i>. Lessico: <i>nipote</i> = <i>neto</i> e <i>sobrinho</i>; <i>fidanzato</i> = <i>namorado</i>; <i>parenti</i> = tutti i familiari (≠ <i>pais</i>).",
    real="Secondo l'ISTAT in Italia nascono circa 1,2 figli per donna, uno dei valori più bassi d'Europa. I giovani italiani escono dalla casa dei genitori in media verso i 30 anni (dati Eurostat). Il <i>pranzo della domenica</i> con la famiglia è ancora una tradizione molto forte, soprattutto con i nonni.",
    tr=("La famiglia oggi", "Ripeti: frasi concessive"),
    gist=("Domenica, a casa della signora Rossi. Ascolta. Di che cosa parlano soprattutto?",
          ["di come sono le famiglie oggi, in Italia e in Brasile", "della ricetta delle tagliatelle", "dell'inaugurazione della biblioteca"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("La signora Rossi vive con suo fratello Franco.", "F"), ("In Brasile, la domenica, la famiglia pranza in venti.", "V"),
             ("Júlia ha trentadue anni.", "V"), ("I genitori conoscono già la fidanzata di Bruno.", "F"),
             ("Per Júlia, gli amici di Bologna sono come una famiglia.", "V"), ("Júlia promette di tornare in Brasile per Natale.", "F")]),
    talk2=["Perché la signora Rossi dice che non si sente mai sola?", "Lúcia dice: «Anche se non sei sposata, sei felice. È questo che conta». Che cosa è cambiato?",
           "Gli amici possono essere una famiglia? Perché?"],
    n2=["B: 1 vive da sola · 4 Bruno la presenta martedì · 6 dice solo «Ci penso».", "La fidanzata di Bruno è Chiara: stanno insieme da più di un anno."],
    gref="concessive_b1",
    t4="le frasi concessive",
    pA=("Completa con il verbo al congiuntivo o all'indicativo.",
        [("Benché la cucina ___ (essere) piccola, c'è posto per tutti.", "sia"), ("Anche se ___ (lavorare) tanto, Júlia è felice.", "lavora"),
         ("Sebbene ___ (vivere) da sola, la signora Rossi non è mai sola.", "viva"), ("Nonostante Bruno ___ (avere) una fidanzata, non l'ha presentata.", "abbia"),
         ("Benché ___ (piovere), ieri sono venuti tutti.", "piovesse")]),
    pB=[("", ["Anche se", "Benché"], "Anche se", " siamo in venti, parla sempre la mamma."),
        ("Benché ", ["abbia", "ha"], "abbia", " trentadue anni, Júlia non è sposata."),
        ("", ["Nonostante", "Anche se"], "Nonostante", " il traffico, siamo arrivati in tempo.")],
    rule="<b>Benché, sebbene, nonostante (che)</b> + <b>congiuntivo</b>: <i>benché sia piccola</i>; al passato → congiuntivo imperfetto: <i>benché piovesse</i>. <b>Anche se</b> + <b>indicativo</b>: <i>anche se non sei sposata</i>. <b>Nonostante</b> + nome: <i>nonostante la pioggia</i>.",
    use=["Una cosa che fai anche se non ti piace. <i>Anche se…</i>", "Un posto che ami benché abbia dei difetti.",
         "Una persona che stimi nonostante… <i>Nonostante sia…</i>", "Una cosa che hai fatto benché fossi stanco/a.",
         "La tua famiglia: com'è? <i>Sebbene…, …</i>"],
    n4="A5: verbo principale al passato → congiuntivo imperfetto (<i>piovesse</i>).",
    t5="la famiglia di oggi",
    fl=(["dare un'opinione", "ammettere, ma…", "difendere una scelta", "concludere"],
        ["Secondo me… · Per quanto mi riguarda… · Credo che…", "È vero che…, però… · Benché…, … · Anche se…, …",
         "È una mia scelta. · Ognuno è libero di… · Non c'è niente di male.", "Alla fine… · L'importante è che… · È questo che conta."]),
    pron=("Le congiunzioni concessive hanno l'accento in posti diversi: <i>ben<b>CHÉ</b></i> (ultima sillaba, con l'accento grafico), <i>seb<b>BE</b>ne</i>, <i>nono<b>STAN</b>te</i>, <i><b>AN</b>che se</i>. La frase concessiva resta <b>sospesa</b>, la principale scende: <i>Benché sia piccola… c'è posto per tutti.</i>",
          "Ascolta e ripeti. Poi inventa una frase con ognuna delle quattro congiunzioni."),
    task=("Discussione: la famiglia di oggi. L'insegnante legge un'affermazione forte. Sei d'accordo o no? Rispondi ammettendo una parte (benché, anche se…) e difendendo la tua opinione. Poi confronta la famiglia brasiliana e quella italiana.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0'><li>«A trent'anni bisogna essere sposati.»</li><li>«Una coppia senza figli non è una vera famiglia.»</li><li>«I figli devono uscire di casa a diciott'anni.»</li><li>«Gli amici non possono essere una famiglia.»</li></ul>",
          "Insegnante: legge un'affermazione e insiste (Ma davvero? E i nonni?). Esempio di risposta: Benché molti lo pensino, non sono d'accordo: anche se… · È vero che…, però… Poi: In Brasile la famiglia è più grande? Si esce di casa prima o dopo?"),
    talk5=["Nella tua famiglia chi è «la signora Rossi», la persona che riunisce tutti?", "Secondo te, la famiglia brasiliana sta cambiando come quella italiana?"],
    n5=["far sentire la sospensione della concessiva con la mano che sale e poi scende.", "Pretendere almeno tre concessive diverse nella discussione; non giudicare le opinioni, solo la lingua."],
    hA=("La signora Rossi scrive una lettera a suo fratello Franco. Scegli la forma giusta.",
        "<i>Caro Franco, domenica ho invitato a pranzo Júlia con i suoi genitori. Benché la mia cucina {0} piccola, siamo stati benissimo. La mamma, Lúcia, parla poco l'italiano: {1} non capisse tutto, rideva sempre. Il papà, nonostante {2} stanco per il viaggio, ha mangiato tre piatti di tagliatelle! {3} viva da sola da tanti anni, quando la casa è piena sono felice. Anche se {4} vecchia, ho ancora voglia di cucinare per tutti. Un abbraccio, tua sorella</i>",
        [(["sia", "è"], "sia"), (["anche se", "benché"], "benché"), (["fosse", "era"], "fosse"),
         (["Sebbene", "Anche se"], "Sebbene"), (["sono", "sia"], "sono")]),
    hB=("Unisci le due frasi con la congiunzione tra parentesi.",
        [("Piove. Usciamo lo stesso. (benché)", "Benché piova, usciamo lo stesso."), ("Sono stanca. Vengo alla festa. (anche se)", "Anche se sono stanca, vengo alla festa."),
         ("Aveva poco tempo. Mi ha aiutato. (nonostante)", "Nonostante avesse poco tempo, mi ha aiutato.")]),
    watch=[("Benché è tardi, restiamo.", "Benché sia tardi, restiamo.", "<i>benché</i> + congiuntivo."),
           ("Anche se sia stanca, esco.", "Anche se sono stanca, esco.", "<i>anche se</i> + indicativo."),
           ("I miei parenti sono Lúcia e Roberto.", "I miei genitori sono Lúcia e Roberto.", "<i>parenti</i> = tutti i familiari.")],
    write=("La famiglia oggi: com'è la tua famiglia e come è cambiata rispetto a quella dei tuoi nonni? Che cosa pensi delle famiglie di oggi?",
           "Benché la mia famiglia sia…", ["quattro concessive (<i>benché, sebbene, nonostante, anche se</i>)", "un confronto tra ieri e oggi", "una conclusione (<i>L'importante è che…</i>)"]),
    cando="So parlare dei modelli di famiglia, ammettere un'idea diversa e difendere la mia opinione con le concessive.",
    nH="Prossima unità: <i>Mi chiedo se…</i> (le interrogative indirette).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 17 - La famiglia oggi")
