# Speak! Progresso B1 - Unità 29 "Me lo faccio fare" - FORMATO RIDOTTO (italiano/lean_b1.py)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
import lean_b1
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 29", audio_json=os.path.join(HERE, "audio_it-b1-unita-29.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")
SCRIPT, S2 = lean_b1.load_script(HERE, "it-b1-unita-29", "29.1 Me lo faccio fare", "29.2 Ripeti")

C = dict(
    nn="29", title="Me lo faccio fare", subtitle="Servizi e artigiani · <b>fare + infinito, farsi fare</b>",
    cover=[("SAI FARE", "chiedere un servizio, dire che cosa fai fare agli altri, dare consigli pratici"),
           ("LINGUA", "Faccio riparare… · La faccio controllare · Mi sono fatta tagliare… · Fattela controllare!"),
           ("PRONUNCIA", "faccio, fatta: le doppie · gli in tagliare")],
    t1="fai da te?",
    start=["Guarda la foto. Ti piacerebbe andare in moto? Perché?", "Quando qualcosa si rompe, lo ripari tu o chiami qualcuno?",
           "Che cosa devi sistemare prima di partire per le vacanze?"],
    kw=[("la persona che ripara auto e moto", "il meccanico"), ("la persona che taglia i capelli", "il parrucchiere"),
        ("si mette in testa per andare in moto", "il casco"), ("il carburante di auto e moto", "la benzina"),
        ("il posto dove si fa benzina", "il distributore"), ("il controllo obbligatorio di auto e moto", "la revisione")],
    use_words=["Hai la patente? Per la macchina o anche per la moto?", "Hai un parrucchiere o un meccanico di fiducia?"],
    n1=["A: <i>di fiducia</i> = di cui ti fidi; <i>fare benzina</i> = mettere benzina nel serbatoio."],
    aims=["Me lo faccio fare: la moto di Davide · Parliamone", "fare + infinito, farsi fare, pronomi e accordo",
          "Lo fai o lo fai fare? (29.2) · le doppie e gli", "Il messaggio di Davide · riscrivi · scrittura (100–150 parole)"],
    story="Lunedì 2 agosto, mattina, davanti al Bar Giulia (Júlia, Giulia, Davide). Davide ha finito l'ultimo esame venerdì e sabato si è comprato la moto (usata, rossa), senza farla controllare («sono quasi ingegnere»). Giulia fa riparare la macchina dallo stesso meccanico da vent'anni. Júlia alle 11 si fa tagliare i capelli e nel pomeriggio fa portare terra e piante per il giardino del cortile; Ferri ha fatto mettere la rastrelliera venerdì (la signora Rossi gli ha telefonato tre volte). Davide vuole portare Júlia dal parrucchiere, ma la moto non parte. Giulia fa venire il suo meccanico (voce generica): la moto è perfetta, è senza benzina. Il meccanico non gli fa pagare niente ma gli consiglia un controllo completo; Giulia lo farà sapere a tutto il bar e accompagna Júlia in macchina.",
    prob="In portoghese si dice <i>cortei o cabelo, lavei o carro</i> anche quando l'ha fatto un altro: lo studente traduce <i>ho tagliato i capelli</i>, che in italiano vuol dire «da solo». Serve <i>mi sono fatto/a tagliare</i> (con <b>essere</b>). Altri errori: il pronome dopo l'infinito (<i>faccio ripararla</i> → <i>la faccio riparare</i>), l'oggetto tra <i>fare</i> e l'infinito (<i>ho fatto la moto controllare</i>) e il calco <i>mando riparare</i>.",
    real="In Italia con la <b>patente A2</b> si può guidare una moto media già a 18 anni; il <b>casco</b> è obbligatorio per tutti. Moto e auto fanno la <b>revisione</b> la prima volta dopo quattro anni, poi ogni due anni. Al distributore si sceglie tra <i>fai da te</i> (self-service) e <i>servito</i>, che costa un po' di più. Molti italiani hanno il loro meccanico e il loro parrucchiere <i>di fiducia</i> per tutta la vita.",
    tr=("Me lo faccio fare", "Ripeti: fare + infinito"),
    gist=("Lunedì mattina, davanti al bar. Ascolta. Qual è il problema della moto?",
          ["è senza benzina", "ha i freni rotti", "qualcuno l'ha rubata"]),
    detail=("vf", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.",
            [("Davide ha fatto controllare la moto prima di comprarla.", "F"), ("Giulia va dallo stesso meccanico da vent'anni.", "V"),
             ("Oggi Júlia si fa tagliare i capelli.", "V"), ("La rastrelliera arriverà a settembre.", "F"),
             ("Il meccanico si fa pagare il controllo.", "F"), ("Júlia va dal parrucchiere con Giulia.", "V")]),
    talk2=["Davide ha sbagliato? Che cosa avrebbe dovuto fare?", "Perché Giulia si fida del suo meccanico?",
           "Ti è mai successo qualcosa di simile (una cosa ovvia che non avevi visto)?"],
    n2=["B: 1 la controlla lui · 4 l'amministratore l'ha fatta mettere venerdì · 5 non gli fa pagare niente.", "Ripresa: giardino e rastrelliera approvati all'assemblea (unità 28)."],
    gref="fare_causativo",
    t4="lo faccio fare",
    pA=("Completa con <i>fare</i> + infinito al tempo giusto.",
        [("Giulia ___ (riparare) la macchina dallo stesso meccanico.", "fa riparare"), ("Domani mi ___ (tagliare) i capelli.", "faccio tagliare"),
         ("L'amministratore ha ___ (mettere) la rastrelliera.", "fatto mettere"), ("Davide non l'ha ___ (controllare) prima di comprarla.", "fatta controllare"),
         ("Il meccanico non gli ha ___ (pagare) niente.", "fatto pagare")]),
    pAw="30mm",
    pB=[("Ho ", ["fatto riparare la bici", "riparato la bici"], "fatto riparare la bici", " dal meccanico."),
        ("La moto? ", ["La faccio controllare", "Faccio controllarla"], "La faccio controllare", " domani."),
        ("Júlia ", ["si è fatta", "ha fatto"], "si è fatta", " tagliare i capelli.")],
    rule="<b>fare + infinito</b>: l'azione la fa un'altra persona: <i>Faccio riparare la moto (al / dal meccanico).</i> I pronomi vanno prima di <i>fare</i>: <i>La faccio riparare.</i> Per te stesso: <b>farsi</b> + infinito, con <b>essere</b> al passato: <i>Mi sono fatta tagliare i capelli.</i>",
    use=["Che cosa fai da solo/a e che cosa fai fare (capelli, macchina, vestiti, pulizie)?", "Ti sei mai fatto/a fare un vestito su misura o un tatuaggio?",
         "Che cosa ti fa ridere? E che cosa ti fa arrabbiare?", "Da bambino/a, che cosa ti facevano fare i tuoi genitori?",
         "Completa: <i>Prima delle vacanze mi faccio…</i>"],
    n4="B1: chi ripara è il meccanico → <i>ho fatto riparare</i>. B3: per sé stessa → <i>farsi</i>, ausiliare essere.",
    t5="lo fai o lo fai fare?",
    fl=(["chiedere un servizio", "tempi e prezzi", "dare un consiglio", "lamentarsi"],
        ["Vorrei far controllare… · Dovrei farmi tagliare…", "Per quando sarebbe pronta? · Quanto mi costa?",
         "Fattela controllare! · Perché non te lo fai fare da…?", "Mi avete fatto aspettare un'ora! · Me l'avete fatta pagare troppo."]),
    pron=("Nelle forme di <b>fare</b> la doppia è lunga: <i>fa<b>cc</b>io, fa<b>tt</b>o, fa<b>tt</b>a</i> (≠ <i>fata</i>). In <b>tagliare</b> e <b>meglio</b> si sente <b>gli</b>, come <i>lh</i> in portoghese: <i>ta-<b>GLIA</b>-re</i>.",
          "Ascolta e ripeti. Poi leggi: «Mi sono fatta tagliare i capelli e ho fatto controllare la moto.»"),
    task=("Lo fai o lo fai fare? Prima delle vacanze devi sistemare molte cose. Scegli tre servizi dalla lista. L'insegnante fa l'artigiano o il negoziante: spiega che cosa vuoi far fare, chiedi tempi e prezzi e lamentati se qualcosa non va.",
          "<ul style='line-height:1.45;font-size:8.9pt;margin:0;columns:2'><li>il meccanico (auto o moto)</li><li>il parrucchiere</li><li>la sarta (un vestito da accorciare)</li><li>il tecnico del telefono</li><li>l'idraulico (un rubinetto)</li><li>la tintoria (una macchia)</li></ul>",
          "Insegnante: È pronta venerdì. · Glielo faccio fare dal mio collega. · Le costa 80 euro. · Prima devo farlo vedere al tecnico… Lo studente: Vorrei far riparare… · Me lo può far avere entro…? · Mi avete fatto aspettare… Correggere <i>ho tagliato i capelli</i> → <i>mi sono fatto/a tagliare</i>."),
    talk5=["Sei una persona che ripara le cose da sola o che le fa riparare?", "Nel tuo paese è facile trovare un artigiano bravo e onesto?"],
    n5=["far sentire la differenza <i>fatta / fata</i>, <i>faccio</i> con la doppia.", "Pretendere almeno tre frasi con <i>fare</i> + infinito e una con <i>farsi fare</i>."],
    hA=("Il messaggio di Davide a Elena. Scegli la forma giusta.",
        "<i>Ciao Elena! Finalmente ho la moto: sabato me la sono {0} da un signore di Imola. Stamattina però non partiva. Giulia ha {1} venire il suo meccanico al bar: era senza benzina… Il meccanico non mi ha fatto {2} niente, ma Giulia {3} sapere la storia a tutto il quartiere! Domani la {4} bene: freni e gomme. A settembre ti porto a fare un giro!</i>",
        [(["comprata", "fatta comprare"], "comprata"), (["fatto", "fatta"], "fatto"), (["pagare", "pagato"], "pagare"),
         (["ha fatto", "si è fatta"], "ha fatto"), (["faccio controllare", "controllo io"], "faccio controllare")]),
    hB=("Riscrivi con <i>fare</i> + infinito: l'azione la fa un'altra persona.",
        [("Il meccanico controlla la mia moto.", "Faccio controllare la moto dal meccanico."), ("La parrucchiera mi ha tagliato i capelli.", "Mi sono fatto/a tagliare i capelli dalla parrucchiera."),
         ("Un operaio ha messo la rastrelliera. (l'amministratore)", "L'amministratore ha fatto mettere la rastrelliera.")]),
    watch=[("Ho tagliato i capelli (dal parrucchiere).", "Mi sono fatto/a tagliare i capelli.", "l'ha fatto un altro: <i>farsi</i> + infinito."),
           ("Faccio ripararla domani.", "La faccio riparare domani.", "il pronome va prima di <i>fare</i>."),
           ("Ho fatto la moto controllare.", "Ho fatto controllare la moto.", "l'infinito va subito dopo <i>fare</i>.")],
    write=("Scrivi un post per un forum: «Fai da te o fai fare?». Racconta che cosa fai da solo/a e che cosa fai fare (casa, macchina, capelli, vestiti) e un'esperienza buona o cattiva con un artigiano.",
           "Io sono una persona che…", ["almeno tre frasi con <i>fare</i> + infinito", "una frase con <i>farsi fare</i> al passato prossimo", "un consiglio finale (<i>fatti fare…</i>)"]),
    cando="So parlare dei servizi e di quello che faccio fare agli altri con fare + infinito e farsi fare.",
    nH="Prossima unità: <i>Ripasso 3</i> (unità 21–29).",
)

if __name__ == "__main__":
    render(lean_b1.make_build(C, SCRIPT, S2), sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 29 - Me lo faccio fare")
