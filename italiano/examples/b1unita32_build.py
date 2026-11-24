# Speak! Progresso B1 - Unità 32 "Perché tutto funzioni" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 32", audio_json=os.path.join(HERE, "audio_it-b1-unita-32.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-32", "32.1 Perché tutto funzioni", "32.2 Ripeti")

C = dict(
    nn="32", title="Perché tutto funzioni", subtitle="Un progetto in centro · <b>affinché, prima che, senza che, purché, a meno che</b>",
    cover=[("SAI FARE", "organizzare un progetto, porre condizioni, parlare di scopi e scadenze"),
           ("LINGUA", "affinché · prima che · senza che · purché · a meno che (non) + congiuntivo"),
           ("PRONUNCIA", "l'accento finale: affinché, purché · ch = [k]")],
    t1="lavori in corso",
    start=["Guarda la foto. Hai mai fatto lavori in casa? Com'è andata?", "Quando organizzi qualcosa (un viaggio, una festa, un lavoro), fai un piano o improvvisi?",
           "Che cosa può andare storto in un progetto?"],
    kw=[("il luogo dove si fanno i lavori di costruzione", "il cantiere"), ("il documento con il prezzo dei lavori, prima di cominciare", "il preventivo"),
        ("la data entro cui bisogna finire o consegnare qualcosa", "la scadenza"), ("una visita sul posto per vedere com'è un edificio", "il sopralluogo"),
        ("rimettere a nuovo una casa o un edificio", "ristrutturare"), ("un edificio storico protetto dalla legge", "l'edificio vincolato")],
    use_words=["Prima di fare dei lavori, chiedi sempre un preventivo? Quanti?", "Hai una scadenza importante questo mese? Quale?"],
    n1=["A: <i>vincolato</i> = protetto dalla legge, non si può cambiare liberamente; <i>sopralluogo</i> = <i>sopra</i> + <i>luogo</i>: andare a vedere sul posto."],
    aims=["Perché tutto funzioni: il nuovo progetto dello studio · Parliamone", "affinché, prima che, senza che, purché, a meno che + congiuntivo",
          "Organizziamo un evento (32.2) · l'accento di purché e affinché", "La mail di Júlia al cliente · riscrivi · scrittura (100–150 parole)"],
    story="Lunedì 13 settembre, allo studio. Júlia e Marco organizzano il progetto del nuovo cliente (unità 31), il dottor Galli: un palazzo vincolato del Seicento in centro diventerà un piccolo albergo, da aprire a Pasqua. Servono la risposta del Comune (entro novembre) e la Soprintendenza; giovedì c'è il sopralluogo. Al piano terra un ristorante resta aperto: i lavori più rumorosi si faranno la mattina. Galli telefona: vuole anche una terrazza con bar sul tetto; preventivo entro venerdì. Giulia è partita sabato 11 per la Sardegna ed Elena è al bar: stasera aperitivo da lei, paga Júlia.",
    prob="Il portoghese ha le stesse congiunzioni con il congiuntivo (<i>para que, antes que, sem que, a menos que</i>): il modo non è il problema principale. Il falso amico è <i>purché</i>: sembra «porque», ma vuol dire «desde que / contanto que» (<s>Non vengo purché sono stanco</s> → <i>perché</i>). L'infinito personale (<i>para eles fazerem</i>) non esiste: <s>per loro fare</s> → <i>perché facciano</i>. Altri errori: <s>prima che partire</s> → <i>prima di partire</i>, e il <i>non</i> di <i>a meno che non</i> letto come negazione.",
    real="Gli edifici storici protetti dalla legge si dicono <b>vincolati</b>: per ogni lavoro serve l'autorizzazione della <b>Soprintendenza</b>, l'ufficio del Ministero della Cultura che tutela i beni culturali (Codice dei beni culturali e del paesaggio, 2004). Prima dei lavori si chiede un <b>preventivo</b> scritto. Nei centri storici molti palazzi hanno un negozio o un ristorante al piano terra e le case ai piani di sopra.",
    tr=("Perché tutto funzioni", "Ripeti: le congiunzioni"),
    gist=("Lunedì mattina, allo studio. Ascolta. Che cosa organizzano Júlia e Marco?",
          ["i lavori per trasformare un palazzo in albergo", "la festa per il ritorno di Giulia", "un viaggio di lavoro in Sardegna"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Il cliente vuole aprire l'albergo a Natale.", "F"), ("Per i lavori serve l'autorizzazione della Soprintendenza.", "V"),
             ("Il ristorante al piano terra chiuderà durante i lavori.", "F"), ("I lavori più rumorosi si faranno la mattina.", "V"),
             ("Il dottor Galli vuole anche una terrazza sul tetto.", "V"), ("Il preventivo arriverà tra un mese.", "F")]),
    talk2=["Secondo te, ce la faranno ad aprire a Pasqua? Perché?", "«Non cambiate niente senza che io lo sappia.» Galli è un buon cliente o un cliente difficile?",
           "Hai mai lavorato a un progetto con una scadenza impossibile?"],
    n2=["B: 1 a Pasqua · 3 resta aperto · 6 entro venerdì.", "Ripresa: il nuovo cliente dell'albergo (unità 31); Giulia è partita sabato 11 per la Sardegna ed Elena è tornata al bar."],
    gref="congiunzioni_congiuntivo_b1",
    t4="affinché, purché, a meno che",
    pA=("Completa con: affinché · prima che · senza che · purché · a meno che.",
        [("Ti presto la macchina, ___ tu me la riporti stasera.", "purché"), ("Il cliente non vuole che cambiamo niente ___ lui lo sappia.", "senza che"),
         ("Finiamo il tetto ___ arrivi l'inverno.", "prima che"), ("Mando i disegni oggi ___ il cliente possa guardarli con calma.", "affinché"),
         ("La terrazza si fa, ___ la Soprintendenza non dica di no.", "a meno che")]),
    pAw="30mm",
    pB=[("Prima ", ["di partire", "che partire"], "di partire", ", Giulia ha lasciato le chiavi a Elena."),
        ("Vi spiego tutto perché ", ["capite", "capiate"], "capiate", " come funziona."),
        ("Ho chiamato presto affinché ci ", ["danno", "dessero"], "dessero", " un appuntamento.")],
    rule="<b>affinché / perché</b> (scopo), <b>prima che</b>, <b>senza che</b>, <b>purché</b> (= solo se), <b>a meno che (non)</b> (= tranne se) + <b>congiuntivo</b>. Stesso soggetto → infinito: <i>prima di partire, senza salutare, per capire</i>. Dopo un tempo passato → congiuntivo imperfetto: <i>affinché ci dessero</i>.",
    use=["Che cosa fai prima che arrivino gli ospiti a casa tua? Usa <i>prima che</i>.", "Presteresti la tua macchina a un amico? A quali condizioni? Usa <i>purché</i>.",
         "Completa: <i>Domani vado al lavoro a piedi, a meno che…</i>", "Che cosa fai affinché i tuoi colleghi o la tua famiglia siano contenti?",
         "Una cosa che facevi da bambino senza che i tuoi genitori lo sapessero."],
    n4="B1: stesso soggetto (Giulia… Giulia) → <i>prima di</i> + infinito. B2: <i>perché</i> = scopo → congiuntivo.",
    t5="organizziamo un evento",
    fl=(["porre una condizione", "indicare lo scopo", "mettere in ordine i tempi", "prevedere un problema"],
        ["Va bene, purché… · A patto che… · Solo se…", "Lo facciamo affinché… · …in modo che…",
         "Prima di tutto… · Prima che…, bisogna… · Entro venerdì…", "A meno che non… · E se…? · Il rischio è che…"]),
    pron=("<i>Affinché, purché, perché</i>: l'accento è sull'ultima sillaba e la <i>e</i> è chiusa (é). <i>Ch</i> si legge [k]: <i>pur<b>ch</b>é</i>, mai «purxé». Attenzione alla doppia di <i>a<b>ff</b>inché</i>.",
          "Ascolta e ripeti. Poi leggi: «Ce la facciamo, purché il Comune ci risponda entro novembre.»"),
    task=("Progetto a due: organizzate un evento (una festa per il ritorno di un'amica, un trasloco, un viaggio di gruppo o un corso). Decidete le scadenze, chi fa che cosa e a quali condizioni. Usate almeno quattro congiunzioni.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>la data e il budget</li><li>chi aiuta e chi invitare</li><li>che cosa fare prima che…</li><li>le condizioni (purché…)</li><li>i rischi (a meno che…)</li><li>lo scopo (affinché…)</li></ul>",
          "Insegnante: Va bene, ma solo a patto che… · E se piove? · Perché lo facciamo? Lo studente: Purché… · Prima che…, dobbiamo… · A meno che non… · Affinché… Correggere l'indicativo dopo le congiunzioni e <i>prima che</i> + infinito."),
    talk5=["Sei una persona che organizza tutto prima o che improvvisa?", "Nel tuo lavoro, qual è la cosa più difficile da organizzare?"],
    n5=["far sentire l'accento finale e la [k] di <i>purché</i>.", "Pretendere almeno quattro congiunzioni diverse con il congiuntivo corretto."],
    hA=("La mail di Júlia al dottor Galli. Scegli la forma giusta.",
        "<i>Gentile dottor Galli, Le scrivo {0} abbia tutte le informazioni sul progetto. Giovedì faremo il sopralluogo e, {1} i disegni siano pronti, parleremo con la Soprintendenza. La terrazza si può fare, {2} la Soprintendenza non dica di no. Faremo i lavori più rumorosi la mattina, {3} i clienti del ristorante non sentano niente. Possiamo aprire a Pasqua, {4} il Comune ci risponda entro novembre. Venerdì riceverà il preventivo. Cordiali saluti, Júlia</i>",
        [(["affinché", "purché"], "affinché"), (["prima che", "senza che"], "prima che"), (["a meno che", "affinché"], "a meno che"),
         (["in modo che", "prima che"], "in modo che"), (["senza che", "purché"], "purché")]),
    hB=("Unisci le due frasi con la parola tra parentesi.",
        [("Giulia è partita. Non ha salutato Davide. (senza)", "Giulia è partita senza salutare Davide."),
         ("Ti aiuto. Così finisci in tempo. (affinché)", "Ti aiuto affinché tu finisca in tempo."),
         ("Stasera andiamo al bar. Ma se Marco lavora fino a tardi, no. (a meno che)", "Stasera andiamo al bar, a meno che Marco non lavori fino a tardi.")]),
    watch=[("Prima che cominciare, parliamo.", "Prima di cominciare, parliamo.", "stesso soggetto → <i>prima di</i> + infinito."),
           ("Ti chiamo affinché tu sai tutto.", "Ti chiamo affinché tu sappia tutto.", "dopo <i>affinché</i> serve il congiuntivo."),
           ("Non vengo purché sono stanco.", "Non vengo perché sono stanco.", "<i>purché</i> = solo se, non «porque».")],
    write=("Organizzi un evento per amici o colleghi (una festa, una cena, una gita). Scrivi un'e-mail a tutti con il programma, le scadenze e le condizioni.",
           "Cari tutti, vi scrivo affinché…", ["almeno quattro congiunzioni (<i>affinché, prima che, senza che, purché, a meno che</i>)", "almeno una frase con <i>prima di</i> o <i>senza</i> + infinito", "le scadenze: <i>entro…</i>"]),
    cando="So organizzare un progetto e parlare di scopi, condizioni e scadenze con affinché, prima che, senza che, purché e a meno che.",
    nH="Prossima unità: <i>Così stanco che…</i> (frasi consecutive; la maratona di Davide).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 32 - Perché tutto funzioni")
