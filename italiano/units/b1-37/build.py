# Speak! Progresso B1 - Unità 37 "Mi ha chiesto di…" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 37", audio_json=os.path.join(HERE, "audio_it-b1-unita-37.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-37", "37.1 Mi ha chiesto di", "37.2 Ripeti")

C = dict(
    nn="37", title="Mi ha chiesto di…", subtitle="Júlia racconta l'incontro con il cliente · <b>dire di, chiedere di, chiedere se</b>",
    cover=[("SAI FARE", "riferire richieste, consigli e domande"),
           ("LINGUA", "dire di · chiedere di · chiedere se · consigliare di · pregare di + infinito"),
           ("PRONUNCIA", "l'intonazione: domanda diretta ↗ e domanda riferita ↘")],
    t1="favori e richieste",
    start=["Guarda la foto. Ti capita spesso di riferire ad altri quello che ha detto qualcuno? Quando?", "Chi ti chiede più favori: i colleghi, la famiglia o gli amici?",
           "Com'è il cliente (o il capo) ideale?"],
    kw=[("una struttura di legno, con piante o tessuto, che fa ombra", "la pergola"), ("la zona dove non arriva il sole", "l'ombra"),
        ("dire a qualcuno che cosa è meglio fare", "consigliare"), ("chiedere qualcosa con molta gentilezza o insistenza", "pregare"),
        ("chi pretende molto e non perdona facilmente", "severo"), ("dire a qualcuno, con insistenza, di fare attenzione", "raccomandare")],
    use_words=["Ti piacerebbe una pergola in giardino o in terrazza? Che cosa ci faresti?", "Chi è stata la persona più severa della tua vita (un insegnante, un capo)?"],
    n1=["A: <i>pregare</i> = chiedere con insistenza (non solo in chiesa!); <i>raccomandare</i> = dire con insistenza di fare attenzione: <i>Mi raccomando!</i>"],
    aims=["Mi ha chiesto di…: Júlia racconta l'incontro con Galli · Parliamone", "dire / chiedere / consigliare di + infinito · chiedere se",
          "Il telefono senza fili (37.2) · l'intonazione della domanda riferita", "Il riassunto dell'incontro · riscrivi · scrittura (100–150 parole)"],
    story="Giovedì 2 dicembre, allo studio. Il parere della Soprintendenza è arrivato e stamattina Júlia ha spiegato tutto al dottor Galli. All'inizio si è arrabbiato (niente alluminio); poi ha chiesto se almeno la terrazza si poteva fare: sì, ma senza ombrelloni. Júlia gli ha proposto una pergola bassa di legno, che dalla strada non si vede; Galli le ha chiesto di disegnarla entro Natale, di mandargli tre preventivi e di dire a Marco che è troppo severo. La dottoressa Benassi ha chiesto le foto degli affreschi entro lunedì (Júlia le ha fatte venerdì). Marco vuole la pergola «un po' più bassa».",
    prob="In portoghese si dice <i>pedir para / dizer para</i> + infinito: il brasiliano traduce <s>mi ha chiesto per mandare</s>, <s>gli ho detto per leggere</s> → <i>di</i>. <i>Chiedere</i> vale sia «pedir» sia «perguntar» (<i>domandare</i> = perguntar): <i>chiedere di</i> + infinito (richiesta) ≠ <i>chiedere se</i> (domanda). Pronomi: <i>chiedere / dire / consigliare <b>a</b> qualcuno</i> → <i>gli, le</i>; <i>pregare qualcuno</i> → <i>lo, la</i>. E l'intonazione: la domanda riferita non sale alla fine.",
    real="In Italia il <b>cliente</b> si tratta quasi sempre con il <b>Lei</b> e con il titolo: <i>dottore, ingegnere, architetto, avvocato</i>. Anche nelle e-mail di lavoro si usa spesso il titolo (<i>Gentile architetto…</i>). Prima di Natale molti studi e uffici corrono per chiudere i lavori: l'<b>8 dicembre</b> (Immacolata, giorno festivo) apre il periodo delle feste.",
    tr=("Mi ha chiesto di", "Ripeti: richieste e domande"),
    gist=("Giovedì, allo studio. Ascolta. Di che cosa parlano Júlia e Marco?",
          ["dell'incontro di Júlia con il dottor Galli", "di un nuovo cliente a Milano", "delle vacanze di Natale"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("All'inizio il dottor Galli si è arrabbiato.", "V"), ("Júlia gli ha detto di leggere il parere con calma.", "V"),
             ("Galli ha chiesto se poteva mettere un ombrellone grande.", "F"), ("L'idea della pergola è stata di Marco.", "F"),
             ("Galli vuole il disegno della pergola entro Natale.", "V"), ("La dottoressa Benassi ha chiesto le foto degli affreschi.", "V")]),
    talk2=["Galli è un cliente difficile o normale? Perché?", "Hai mai dovuto dare una cattiva notizia a qualcuno? Come l'hai fatto?",
           "Marco è troppo severo, secondo te? Con i clienti bisogna essere severi o flessibili?"],
    n2=["B: 3 ha chiesto se almeno la terrazza si poteva fare · 4 l'ha proposta Júlia.", "Ripresa: il dottor Galli e la terrazza (unità 32); le regole della Soprintendenza (unità 34)."],
    gref="richieste_indirette",
    t4="mi ha chiesto di…",
    pA=("Riferisci le frasi: completa con di, di non o se.",
        [("«Leggi il parere!» → Gli ho detto ___ leggere il parere.", "di"), ("«Non mettete ombrelloni!» → Ci ha detto ___ mettere ombrelloni.", "di non"),
         ("«Si può fare la terrazza?» → Mi ha chiesto ___ si poteva fare la terrazza.", "se"), ("«Mandatemi le foto!» → Ci ha chiesto ___ mandarle le foto.", "di"),
         ("«Ti piace la pergola?» → Júlia mi ha chiesto ___ mi piaceva la pergola.", "se")]),
    pAw="16mm",
    pB=[("Galli mi ha chiesto ", ["di disegnare", "per disegnare"], "di disegnare", " una pergola."),
        ("Ho chiesto a Marco ", ["se gli piaceva", "che gli piace"], "se gli piaceva", " il disegno."),
        ("Júlia ", ["gli", "lo"], "gli", " ha consigliato di avere pazienza.")],
    rule="Ordine, richiesta, consiglio (imperativo) → verbo + <b>di</b> + infinito: <i>«Leggi!»</i> → <i>Gli ho detto di leggere</i>; <i>«Non mettete!»</i> → <i>Ci ha detto di non mettere</i>. Domanda sì / no → <b>chiedere se</b>: <i>Mi ha chiesto se si poteva fare.</i> Domanda aperta → <b>chiedere perché / dove / quando…</b> Dopo <i>chiedere</i> e <i>dire</i> mai <i>per</i> + infinito.",
    use=["Che cosa ti dicevano sempre di fare i tuoi genitori?", "Qual è l'ultimo favore che qualcuno ti ha chiesto?",
         "Che cosa ti ha consigliato di fare un medico o un amico?", "L'ultima domanda strana che ti hanno fatto: <i>Mi ha chiesto se… / perché…</i>",
         "Che cosa chiedi sempre ai tuoi colleghi o alla tua famiglia?"],
    n4="A: 2 un ordine negativo → <i>di non</i>; 3 e 5 domande sì / no → <i>se</i> + imperfetto. B3: <i>consigliare <b>a</b> qualcuno</i> → <i>gli</i>.",
    t5="il telefono senza fili",
    fl=(["riferire una richiesta", "riferire una domanda", "chiedere un favore", "reagire"],
        ["Mi ha detto di… · Mi ha chiesto di… · Mi ha pregato di…", "Mi ha chiesto se… · Voleva sapere perché… · Mi ha domandato dove…",
         "Ti chiedo un favore: … · Mi faresti un piacere? · Potresti…?", "Classico! · E tu che cosa gli hai detto? · Davvero ti ha chiesto questo?"]),
    pron=("La domanda diretta sale alla fine: <i>Si può fare? ↗</i> La domanda riferita è una frase normale e la voce scende: <i>Mi ha chiesto se si poteva fare. ↘</i> In <i>chiesto</i> e <i>chiedere</i>, <i>ch</i> si legge [k].",
          "Ascolta e ripeti. Poi leggi: «Mi ha chiesto se almeno la terrazza si poteva fare.»"),
    task=("Il telefono senza fili: l'insegnante ti fa domande e richieste come un cliente difficile, un capo o un parente. Poi le riferisci a un'altra persona (l'insegnante cambia ruolo): <i>Mi ha chiesto di… / se… / perché…</i> Alla fine vi scambiate i ruoli.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>un cliente che vuole tutto subito</li><li>un capo prima delle ferie</li><li>una suocera a Natale</li><li>un vicino rumoroso</li><li>un amico che trasloca</li><li>un medico</li></ul>",
          "Insegnante (cliente): Mi mandi il progetto entro domani! Si può fare più economico? Perché costa così tanto? Lo studente: Mi ha chiesto di mandargli… · Mi ha chiesto se… · Voleva sapere perché… Correggere <i>per</i> + infinito e la domanda riferita detta come una domanda."),
    talk5=["Hai mai avuto un cliente, un capo o un parente «difficile»? Che cosa ti chiedeva?", "È facile per te dire di no quando qualcuno ti chiede un favore?"],
    n5=["far sentire l'intonazione: la domanda diretta sale, quella riferita scende.", "Pretendere almeno tre richieste con <i>di</i> + infinito e due domande con <i>se / perché</i>."],
    hA=("Il riassunto di Júlia per lo studio. Scegli la forma giusta.",
        "<i>Incontro con il dottor Galli, 2 dicembre. Il cliente mi ha chiesto {0} sostituire le finestre con finestre in alluminio: gli ho spiegato che non è possibile. Poi mi ha chiesto {1} almeno la terrazza si poteva fare. Gli ho detto {2} mettere ombrelloni e gli ho proposto una pergola bassa. Mi ha pregato {3} disegnarla entro Natale. La dottoressa Benassi ci ha chiesto {4} mandarle le foto degli affreschi entro lunedì. Júlia</i>",
        [(["se poteva", "di potere"], "se poteva"), (["se", "di"], "se"), (["di non", "di"], "di non"),
         (["di", "per"], "di"), (["di", "se"], "di")]),
    hB=("Riferisci le frasi con dire di, chiedere di o chiedere se.",
        [("Galli a Júlia: «Trovi una soluzione!»", "Galli ha chiesto a Júlia di trovare una soluzione."),
         ("Marco a Júlia: «Ti piace il disegno?»", "Marco ha chiesto a Júlia se le piaceva il disegno."),
         ("Benassi a Marco: «Non toccate niente senza il mio permesso!»", "La dottoressa Benassi ha detto a Marco di non toccare niente senza il suo permesso.")]),
    watch=[("Mi ha chiesto per mandare le foto.", "Mi ha chiesto di mandare le foto.", "<i>pedir para</i> → <i>chiedere di</i>."),
           ("Gli ho detto che legge il parere.", "Gli ho detto di leggere il parere.", "per un ordine o un consiglio: <i>dire di</i> + infinito."),
           ("Gli ho pregato di venire.", "L'ho pregato di venire.", "<i>pregare qualcuno</i> → <i>lo / la</i>.")],
    write=("Racconta una conversazione difficile che hai avuto (con un cliente, un capo, un parente, un vicino): che cosa ti ha chiesto, che cosa gli hai detto, com'è finita.",
           "La settimana scorsa…", ["almeno tre frasi con <i>dire / chiedere / consigliare di</i> + infinito", "almeno due domande riferite con <i>se, perché, dove…</i>", "com'è finita la conversazione"]),
    cando="So riferire richieste, consigli e domande con dire di, chiedere di e chiedere se.",
    nH="Prossima unità: <i>Ne vale la pena</i> (valerne la pena, tenerci, entrarci).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 37 - Mi ha chiesto di")
