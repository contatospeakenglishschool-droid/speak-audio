# Speak! Ponte (Italian A2+): Riferimento grammaticale pages, one function per topic, page(b) style
# (modelled on engine/grammar_ref.py of the English line). Each function adds one SB/TB page to a Book.


def _h(t):
    return f'<h4 style="color:#0f4a5a;margin:1.4mm 0 .5mm">{t}</h4>'


def _tbl(head, rows, size="8.8pt", widths=None):
    w = widths or [None] * len(head)
    th = "".join(f'<th{f" style=\'width:{x}\'" if x else ""}>{h}</th>' for h, x in zip(head, w))
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table style="table-layout:fixed;margin-top:0;font-size:{size}"><tr>{th}</tr>{tr}</table>'


def _dont(items):
    return '<div class="box sand" style="margin-top:1.5mm"><h4>NON DIRE</h4>' + " · ".join(f"<s>{a}</s> → {b}" for a, b in items) + "</div>"


def pronomi_indiretti(b):
    """A2 Ponte 01: i pronomi indiretti atoni e tonici, posizione, diretto o indiretto."""
    forms = [("io", "<b>mi</b>", "<b>a me</b>", "Come <b>mi</b> sta? · <b>A me</b> piace il blu."),
             ("tu", "<b>ti</b>", "<b>a te</b>", "Il blu <b>ti</b> sta benissimo!"),
             ("lui", "<b>gli</b>", "<b>a lui</b>", "<b>Gli</b> ho comprato una camicia. (a Bruno)"),
             ("lei", "<b>le</b>", "<b>a lei</b>", "<b>Le</b> scrivo un messaggio. (a Sara)"),
             ("Lei (formale)", "<b>Le</b>", "<b>a Lei</b>", "Signora, <b>Le</b> piace questo vestito?"),
             ("noi", "<b>ci</b>", "<b>a noi</b>", "<b>Ci</b> hanno mandato l'invito."),
             ("voi", "<b>vi</b>", "<b>a voi</b>", "<b>Vi</b> telefono domani."),
             ("loro", "<b>gli</b>", "<b>a loro</b>", "<b>Gli</b> regaliamo un buono. (a Luca e Sara)")]
    dir_ind = [("Chiamo <b>Bruno</b>. → <b>Lo</b> chiamo.", "Telefono <b>a Bruno</b>. → <b>Gli</b> telefono."),
               ("Vedo <b>Giulia</b>. → <b>La</b> vedo.", "Scrivo <b>a Giulia</b>. → <b>Le</b> scrivo."),
               ("Prendo <b>il vestito</b>. → <b>Lo</b> prendo.", "Regalo il vestito <b>a Júlia</b>. → <b>Le</b> regalo il vestito.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: i pronomi indiretti", "")}
<div class="box" style="margin-top:0"><h4>CHE COSA SONO?</h4>Il pronome indiretto risponde alla domanda <b>a chi?</b> e sostituisce <b>a + persona</b>: <i>Regalo una cravatta <b>a Bruno</b>.</i> → <i><b>Gli</b> regalo una cravatta.</i> Così non ripetiamo il nome della persona.</div>
{_h("1. LA FORMA: ATONO E TONICO")}
{_tbl(["persona", "atono", "tonico", "esempio"], forms, "8.6pt", ["24mm", "17mm", "19mm", None])}
<p class="small" style="margin:.6mm 0">Per <i>loro</i> nella lingua di tutti i giorni si usa <b>gli</b>; nello scritto formale anche <i>loro</i> dopo il verbo (<i>Regaliamo <b>loro</b> un buono</i>).</p>
{_h("2. I VERBI CON A + PERSONA")}
<p style="margin:0 0 .5mm;font-size:8.8pt"><b>piacere · stare bene / male · regalare · dare · dire · telefonare · scrivere · chiedere · rispondere · prestare · mandare · portare</b> (qualcosa <b>a</b> qualcuno)</p>
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. DOVE VA L'ATONO?</b><br><b>prima del verbo</b>: <i>Gli telefono.</i> · con <i>non</i>: <i>Non gli telefono.</i><br>passato prossimo: <b>prima dell'ausiliare</b>, il participio non cambia: <i>Le ho regalato un libro.</i><br>con <i>potere, dovere, volere</i>: <i>Gli puoi prestare…?</i> = <i>Puoi prestar<b>gli</b>…?</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. ATONO O TONICO?</b><br>di solito l'<b>atono</b>: <i>Mi piace.</i><br>il <b>tonico</b> per il contrasto, con <i>anche / neanche</i> e da solo:<br><i>A Bruno le cravatte non piacciono, <b>a me</b> sì!</i><br><i>Anche <b>a te</b>? — A chi piace il verde? — <b>A me!</b></i></div></div>
{_h("5. DIRETTO O INDIRETTO?")}
{_tbl(["diretto: lo, la, li, le (chi? che cosa?)", "indiretto: gli, le (a chi?)"], dir_ind, "8.6pt")}
<p class="small" style="margin:.6mm 0">Attenzione: <b>telefonare a</b> vuole l'indiretto; <b>chiamare</b> vuole il diretto: <i>Gli telefono = Lo chiamo.</i></p>
{_dont([("Lo telefono stasera.", "<b>Gli</b> telefono stasera."), ("A Giulia gli piace il blu.", "A Giulia piace il blu. / <b>Le</b> piace il blu."),
        ("Gli piace (a Sara).", "<b>Le</b> piace."), ("Ti sta bene a te.", "<b>Ti</b> sta bene. / <b>A te</b> sta bene."), ("Ho gli comprato…", "<b>Gli</b> ho comprato…")])}""",
    16, """<p>Domanda chiave: <b>a chi?</b> Persona con <i>a</i> → indiretto. <i>A me mi piace</i> si sente nel parlato, ma è da evitare. <i>Glielo, me lo</i> arrivano più avanti.</p>""")


_LINEA_IMPF = """<svg viewBox="0 0 520 64" width="100%" height="15mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="34" x2="500" y2="34" stroke="#77acb5" stroke-width="2"/><polygon points="500,34 490,29 490,39" fill="#77acb5"/>
<text x="20" y="58" font-size="11" fill="#7d858a">PASSATO</text><text x="448" y="58" font-size="11" fill="#7d858a">OGGI</text>
<line x1="456" y1="18" x2="456" y2="50" stroke="#176074" stroke-width="2"/>
<rect x="70" y="27" width="240" height="14" rx="3" fill="#cbbca0" opacity=".75"/>
<text x="74" y="16" font-size="11" fill="#9a7b4f" font-weight="700">imperfetto: com'era? che cosa si faceva di solito?</text>
<circle cx="380" cy="34" r="7" fill="#176074"/><text x="336" y="58" font-size="11" fill="#176074" font-weight="700">passato prossimo: un fatto</text></svg>"""


def imperfetto(b):
    """A2 Ponte 02: l'imperfetto (forme, irregolari, abitudini e descrizioni, primo contrasto con il passato prossimo)."""
    forms = [("io", "parl<b>avo</b>", "prend<b>evo</b>", "dorm<b>ivo</b>", "<b>ero</b>"),
             ("tu", "parl<b>avi</b>", "prend<b>evi</b>", "dorm<b>ivi</b>", "<b>eri</b>"),
             ("lui / lei / Lei", "parl<b>ava</b>", "prend<b>eva</b>", "dorm<b>iva</b>", "<b>era</b>"),
             ("noi", "parl<b>avamo</b>", "prend<b>evamo</b>", "dorm<b>ivamo</b>", "<b>eravamo</b>"),
             ("voi", "parl<b>avate</b>", "prend<b>evate</b>", "dorm<b>ivate</b>", "<b>eravate</b>"),
             ("loro", "parl<b>avano</b>", "prend<b>evano</b>", "dorm<b>ivano</b>", "<b>erano</b>")]
    usi = [("<b>abitudini</b>: che cosa si faceva di solito", "sempre · di solito · ogni domenica · d'estate · spesso · da bambino/a",
            "<i>Ogni domenica <b>andavamo</b> dal nonno.</i>"),
           ("<b>descrizioni</b>: persone, luoghi, età, tempo", "era · aveva · c'era / c'erano",
            "<i><b>Avevo</b> sei anni. <b>Ero</b> bionda. <b>C'erano</b> poche macchine.</i>"),
           ("<b>stati d'animo e desideri</b>", "volevo · mi piaceva · sapevo · ero felice",
            "<i>Da grande <b>volevo</b> fare la cantante.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: l'imperfetto", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>L'imperfetto è il tempo dei <b>ricordi</b>: racconta <b>com'era</b> una persona o un posto e <b>che cosa si faceva di solito</b> nel passato. Non dice quando l'azione è cominciata o finita: è come una foto o un film, non un fatto preciso.
{_LINEA_IMPF}</div>
{_h("1. LA FORMA: -AVO, -EVO, -IVO")}
{_tbl(["", "-are: parlare", "-ere: prendere", "-ire: dormire", "essere"], forms, "8.6pt", ["26mm", None, None, None, None])}
<p class="small" style="margin:.6mm 0"><b>avere</b> è regolare: <i>avevo, avevi, aveva…</i> · Irregolari (dal latino): <b>fare → facevo</b> · <b>bere → bevevo</b> · <b>dire → dicevo</b> · <b>tradurre → traducevo</b>. L'accento: par<u>la</u>vo, parla<u>va</u>mo, ma <u>par</u>lavano.</p>
{_h("2. QUANDO SI USA?")}
{_tbl(["uso", "parole che aiutano", "esempio"], usi, "8.6pt", ["52mm", "56mm", None])}
{_h("3. IMPERFETTO O PASSATO PROSSIMO? (PRIMO CONTATTO)")}
{_tbl(["imperfetto: abitudine, descrizione", "passato prossimo: un fatto, una volta"],
      [("D'estate <b>andavamo</b> a Rimini. (ogni anno)", "Nel 1975 <b>siamo andati</b> a Rimini. (una volta)"),
       ("Il nonno <b>faceva</b> la polenta. (sempre)", "Domenica il nonno <b>ha fatto</b> la polenta. (quella domenica)"),
       ("<b>Era</b> una bambina vivace.", "Mia madre mi <b>ha mandato</b> le foto.")], "8.6pt")}
<p class="small" style="margin:.6mm 0">Nell'unità 03 usiamo i due tempi insieme per raccontare una storia: <i>Mentre <b>giocavo</b>, <b>è arrivato</b> il nonno.</i></p>
{_dont([("Quando ero piccola, ho abitato a Belo Horizonte.", "…<b>abitavo</b> a Belo Horizonte."), ("Io facevevo…", "<b>facevo</b>"),
        ("Era sei anni.", "<b>Avevo</b> sei anni."), ("C'era tanti turisti.", "<b>C'erano</b> tanti turisti."), ("Parlávamo.", "parla<b>va</b>mo")])}""",
    16, """<p>Il portoghese ha lo stesso tempo (<i>pretérito imperfeito</i>), quindi l'uso è facile: la difficoltà è la forma. Far coniugare <i>essere</i> e <i>fare</i> a voce. L'età si dice con <b>avere</b>.</p>""")


_LINEA_STORIA = """<svg viewBox="0 0 520 64" width="100%" height="15mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="34" x2="500" y2="34" stroke="#77acb5" stroke-width="2"/><polygon points="500,34 490,29 490,43" fill="#77acb5"/>
<rect x="60" y="27" width="330" height="14" rx="3" fill="#cbbca0" opacity=".75"/>
<text x="64" y="16" font-size="11" fill="#9a7b4f" font-weight="700">mentre attraversavo la piazza (imperfetto: lo sfondo)</text>
<line x1="250" y1="14" x2="250" y2="54" stroke="#176074" stroke-width="2.5"/><circle cx="250" cy="34" r="7" fill="#176074"/>
<text x="160" y="60" font-size="11" fill="#176074" font-weight="700">all'improvviso un cane è uscito (passato prossimo)</text></svg>"""


def imperfetto_passato_prossimo(b):
    """A2 Ponte 03: imperfetto e passato prossimo insieme per raccontare; mentre, all'improvviso, quando; ricapitolazione dei tempi del passato."""
    pat = [("<b>A. sfondo + fatto</b><br>un'azione in corso viene interrotta", "imperfetto + passato prossimo",
            "<i>Mentre <b>attraversavo</b> la piazza, un cane <b>è uscito</b>.</i>"),
           ("<b>B. due azioni in corso</b><br>nello stesso momento", "imperfetto + imperfetto",
            "<i>Io <b>guardavo</b> un film, mentre Bruno <b>studiava</b>.</i>"),
           ("<b>C. una serie di fatti</b><br>uno dopo l'altro", "passato prossimo + passato prossimo",
            "<i>Si <b>è svegliato</b>, <b>ha telefonato</b> e alla fine <b>è uscito</b>.</i>")]
    mark = [("<b>mentre</b> (+ imperfetto)", "<b>all'improvviso · a un certo punto</b> (+ passato prossimo)"),
            ("<b>sempre · di solito · ogni giorno</b>", "<b>una volta · ieri · sabato sera · alle dieci</b>"),
            ("<b>quando</b> + imperfetto = in quel periodo: <i>Quando ero piccola…</i>", "<b>quando</b> + passato prossimo = in quel momento: <i>Quando si è svegliato…</i>"),
            ("<b>sapevo</b> = conoscevo l'informazione", "<b>ho saputo</b> = ho scoperto, mi hanno detto")]
    rec = [("presente", "<i>Studio italiano da un anno.</i>", "A1"), ("passato prossimo", "<i>Ieri sono andata a Firenze.</i> · un fatto finito", "A1 · 11, 21"),
           ("imperfetto", "<i>Da bambina abitavo a Belo Horizonte.</i> · abitudini, descrizioni", "A2 · 02"),
           ("imperfetto + passato prossimo", "<i>Pioveva quando sono uscita.</i> · raccontare una storia", "A2 · 03")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: imperfetto e passato prossimo", "")}
<div class="box" style="margin-top:0"><h4>COME UN FILM</h4>Quando raccontiamo una storia, l'<b>imperfetto</b> descrive lo <b>sfondo</b> (com'era, che cosa succedeva, che tempo faceva) e il <b>passato prossimo</b> racconta i <b>fatti</b>, le azioni che fanno andare avanti la storia.
{_LINEA_STORIA}</div>
{_h("1. TRE COMBINAZIONI")}
{_tbl(["che cosa succede", "tempi", "esempio"], pat, "8.6pt", ["52mm", "44mm", None])}
{_h("2. LE PAROLE CHE AIUTANO")}
{_tbl(["di solito → imperfetto", "di solito → passato prossimo"], mark, "8.6pt")}
<p class="small" style="margin:.6mm 0">Lo sfondo di una storia usa quasi sempre l'imperfetto: <b>era</b> (lunedì, tardi, buio), <b>c'era / c'erano</b>, <b>faceva</b> freddo, <b>pioveva</b>, <b>avevo</b> fame, <b>ero</b> stanca.</p>
{_h("3. I TEMPI DEL PASSATO FINO A QUI")}
{_tbl(["tempo", "esempio e uso", "unità"], rec, "8.6pt", ["46mm", None, "24mm"])}
{_dont([("Mentre ho attraversato la piazza, un cane è uscito.", "Mentre <b>attraversavo</b>…"), ("Quando sono arrivata, la porta è stata chiusa.", "…la porta <b>era</b> chiusa."),
        ("All'improvviso il telefono suonava.", "All'improvviso il telefono <b>ha suonato</b>."), ("Quando ero arrivata, la porta era chiusa.", "Quando <b>sono arrivata</b>…")])}""",
    16, """<p>Domanda chiave: <i>Sfondo o fatto?</i> La barra = imperfetto, il punto = passato prossimo. In portoghese è uguale: il problema è la forma.</p>""")


def imperativo_informale(b):
    """A2 Ponte 04: l'imperativo informale (tu, noi, voi), affermativo e negativo, irregolari, pronomi attaccati."""
    forms = [("tu", "parl<b>a</b>!", "prend<b>i</b>!", "dorm<b>i</b>!", "fin<b>isci</b>!", "non <b>parlare</b>!"),
             ("noi", "parl<b>iamo</b>!", "prend<b>iamo</b>!", "dorm<b>iamo</b>!", "fin<b>iamo</b>!", "non <b>parliamo</b>!"),
             ("voi", "parl<b>ate</b>!", "prend<b>ete</b>!", "dorm<b>ite</b>!", "fin<b>ite</b>!", "non <b>parlate</b>!")]
    irr = [("andare", "<b>va'</b> / vai", "andate"), ("fare", "<b>fa'</b> / fai", "fate"), ("dare", "<b>da'</b> / dai", "date"),
           ("stare", "<b>sta'</b> / stai", "state"), ("dire", "<b>di'</b>", "dite"), ("essere", "<b>sii</b>", "<b>siate</b>"), ("avere", "<b>abbi</b>", "<b>abbiate</b>")]
    irl = "".join(f"<tr><td>{a}</td><td>{t}</td><td>{v}</td></tr>" for a, t, v in irr)
    b.page(f"""{b.sec("+", "Riferimento grammaticale: l'imperativo informale", "")}
<div class="box" style="margin-top:0"><h4>A CHE COSA SERVE?</h4>L'imperativo serve per dare <b>consigli</b>, <b>istruzioni</b> e <b>ordini</b>: <i>Bevi tanta acqua! Non uscire!</i> L'imperativo <b>informale</b> si usa con gli amici e la famiglia: <b>tu</b> (una persona), <b>voi</b> (più persone) e <b>noi</b> (una proposta: <i>Andiamo!</i>). L'imperativo formale (<i>Lei</i>) arriva nell'unità 08.</div>
{_h("1. LA FORMA")}
{_tbl(["", "-are: parlare", "-ere: prendere", "-ire: dormire", "-ire (-isc-): finire", "negativo"], forms, "8.6pt", ["12mm", None, None, None, "30mm", "28mm"])}
<p class="small" style="margin:.6mm 0"><b>noi</b> e <b>voi</b> sono uguali al presente. Solo <b>tu</b> dei verbi in <b>-are</b> cambia: <i>tu parli</i> (presente) → <i>parla!</i> (imperativo). Il negativo di <b>tu</b> è <b>non + infinito</b>: <i>Non prendere! Non venire!</i></p>
<div class="two"><div>{_h("2. GLI IRREGOLARI")}
<table style="margin-top:0;font-size:8.6pt"><tr><th>verbo</th><th>tu</th><th>voi</th></tr>{irl}</table>
<p class="small" style="margin:.6mm 0"><i>venire → vieni!</i> · <i>uscire → esci!</i> · <i>bere → bevi!</i> (come il presente)</p></div>
<div>{_h("3. CON I PRONOMI")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>affermativo</b>: il pronome va <b>dopo</b> e si attacca al verbo:<br><i>Chiama il medico → Chiama<b>lo</b>! · Scrivi<b>mi</b>! · Prende<b>teli</b>!</i><br>riflessivi: <i>riposar<b>si</b> → Riposa<b>ti</b>! · Riposate<b>vi</b>! · Metti<b>ti</b> la sciarpa!</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt;margin-top:1mm"><b>con va', fa', da', di', sta'</b> la consonante si <b>raddoppia</b>:<br><i>da' + mi → da<b>mm</b>i · di' + lo → di<b>ll</b>o · fa' + mi → fa<b>mm</b>i vedere</i><br>eccezione: <b>gli</b> → <i>dagli, digli</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt;margin-top:1mm"><b>negativo</b>: due posizioni, stesso significato:<br><i>Non prender<b>li</b>! = Non <b>li</b> prendere!</i> · <i>Non avvicinar<b>ti</b>! = Non <b>ti</b> avvicinare!</i><br>voi: <i>Non portate<b>lo</b>! = Non <b>lo</b> portate!</i></div></div></div>
<p class="small" style="margin:.8mm 0">L'accento non si sposta quando aggiungiamo il pronome: <u>ri</u>posa → <u>ri</u>posati · <u>chia</u>ma → <u>chia</u>malo · <u>scri</u>vi → <u>scri</u>vimi.</p>
{_dont([("Non prendi l'antibiotico!", "Non <b>prendere</b> l'antibiotico!"), ("Ti riposa!", "<b>Riposati</b>!"), ("Dami un abbraccio!", "<b>Dammi</b> un abbraccio!"),
        ("Lo chiama!", "<b>Chiamalo</b>!"), ("Ragazzi, non giocare!", "Ragazzi, non <b>giocate</b>!")])}""",
    16, """<p>In Brasile l'imperativo di tutti i giorni è spesso uguale al presente (<i>pega, toma</i>): per questo lo studente dice <i>non prendi!</i>. Regola d'oro: <b>tu negativo = non + infinito</b>. I pronomi doppi (<i>dammelo</i>) arrivano più avanti.</p>""")


def condizionale_presente(b):
    """A2 Ponte 05: il condizionale presente (forme regolari e irregolari; richieste gentili, desideri, consigli, proposte)."""
    forms = [("io", "parl<b>erei</b>", "prend<b>erei</b>", "dorm<b>irei</b>", "<b>sarei</b>"),
             ("tu", "parl<b>eresti</b>", "prend<b>eresti</b>", "dorm<b>iresti</b>", "<b>saresti</b>"),
             ("lui / lei / Lei", "parl<b>erebbe</b>", "prend<b>erebbe</b>", "dorm<b>irebbe</b>", "<b>sarebbe</b>"),
             ("noi", "parl<b>eremmo</b>", "prend<b>eremmo</b>", "dorm<b>iremmo</b>", "<b>saremmo</b>"),
             ("voi", "parl<b>ereste</b>", "prend<b>ereste</b>", "dorm<b>ireste</b>", "<b>sareste</b>"),
             ("loro", "parl<b>erebbero</b>", "prend<b>erebbero</b>", "dorm<b>irebbero</b>", "<b>sarebbero</b>")]
    irr = [("perdono una vocale", "andare → <b>andrei</b> · avere → <b>avrei</b> · dovere → <b>dovrei</b> · potere → <b>potrei</b> · sapere → <b>saprei</b> · vedere → <b>vedrei</b> · vivere → <b>vivrei</b>"),
           ("doppia <b>rr</b>", "volere → <b>vorrei</b> · venire → <b>verrei</b> · rimanere → <b>rimarrei</b> · bere → <b>berrei</b>"),
           ("tengono la <b>a</b>", "fare → <b>farei</b> · dare → <b>darei</b> · stare → <b>starei</b>"),
           ("-care, -gare · -ciare, -giare", "cercare → <b>cercherei</b> · pagare → <b>pagherei</b> · cominciare → <b>comincerei</b> · mangiare → <b>mangerei</b>")]
    usi = [("<b>chiedere in modo gentile</b>", "<i>Vorrei un cappuccino. · Potresti aiutarmi? · Ti dispiacerebbe…?</i>"),
           ("<b>un desiderio</b>", "<i>Mi piacerebbe sciare. · Vorrei tanto tornare in Brasile.</i>"),
           ("<b>un consiglio</b>", "<i>Dovresti riposarti. · Al tuo posto, io cercherei un volo per febbraio.</i>"),
           ("<b>una proposta</b>", "<i>Potremmo fare una cena insieme!</i>"),
           ("<b>che cosa farei</b> (un'ipotesi)", "<i>Io non lo comprerei mai! · Bruno resterebbe qui.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: il condizionale presente", "")}
<div class="box" style="margin-top:0"><h4>A CHE COSA SERVE?</h4>Il condizionale è il tempo della <b>gentilezza</b> e dei <b>desideri</b>: rende le richieste più morbide (<i>voglio → <b>vorrei</b></i>), esprime un desiderio, dà un consiglio e dice che cosa faremmo in una situazione.</div>
{_h("1. LA FORMA REGOLARE")}
{_tbl(["", "-are: parlare", "-ere: prendere", "-ire: dormire", "essere"], forms, "8.6pt", ["26mm", None, None, None, None])}
<p class="small" style="margin:.6mm 0">Nei verbi in <b>-are</b> la <b>a</b> diventa <b>e</b>: <i>parlare → parl<b>e</b>rei</i>, <i>telefonare → telefon<b>e</b>rei</i>. <b>noi</b> ha sempre la doppia <b>m</b>: <i>potre<b>mm</b>o, andre<b>mm</b>o</i>.</p>
{_h("2. GLI IRREGOLARI")}
{_tbl(["gruppo", "verbi"], irr, "8.6pt", ["40mm", None])}
<p class="small" style="margin:.6mm 0"><b>piacere</b>: <i>mi piacerebbe</i> + infinito o singolare · <i>mi piacerebbero</i> + plurale. Lo stesso per <b>servire</b>: <i>mi servirebbe il computer</i>.</p>
{_h("3. QUANDO SI USA?")}
{_tbl(["uso", "esempi"], usi, "8.6pt", ["46mm", None])}
{_dont([("Voglio un caffè. (al bar)", "<b>Vorrei</b> un caffè."), ("parlarei · comprarei", "parl<b>e</b>rei · compr<b>e</b>rei"), ("poterei · volerei", "<b>potrei · vorrei</b>"),
        ("mi piacerei andare", "mi <b>piacerebbe</b> andare"), ("potremo", "potre<b>mm</b>o")])}""",
    16, """<p>In portoghese il <i>futuro do pretérito</i> funziona allo stesso modo (<i>eu gostaria, você poderia</i>), quindi l'uso è facile. Gli errori sono di forma: la <b>a</b> dei verbi in <i>-are</i>, gli irregolari e la doppia <b>m</b> di <i>noi</i>.</p>""")


def sapere_conoscere(b):
    """A2 Ponte 06: sapere e conoscere; ci vuole / ci vogliono; i verbi modali al passato prossimo."""
    sc = [("<b>sapere</b> + infinito: una capacità", "<i>So fare il cappuccino. · Sai usare questa macchina?</i>"),
          ("<b>sapere</b> + che, se, dove, quando, perché…", "<i>Non so perché è tornato. · Sai se ha esperienza?</i>"),
          ("<b>sapere</b> + un'informazione", "<i>Sai il suo numero? · Lo so!</i>"),
          ("<b>conoscere</b> + persone", "<i>Conosco un ragazzo, Matteo.</i>"),
          ("<b>conoscere</b> + luoghi, cose, lingue (bene, per esperienza)", "<i>Conosco la zona universitaria. · Questa macchina non la conosco.</i>")]
    pp = [("<b>ho conosciuto</b> = ho incontrato la prima volta", "<i>Ho conosciuto Matteo sabato.</i>"),
          ("<b>ho saputo</b> = ho scoperto, mi hanno detto", "<i>Oggi ho saputo che vuole imparare il portoghese.</i>")]
    mod = [("lavorare → <b>avere</b>", "<i>Matteo <b>ha dovuto</b> lavorare da solo.</i>"),
           ("andare, tornare → <b>essere</b>", "<i>Giulia <b>è dovuta</b> andare in banca. · Matteo <b>è dovuto</b> tornare.</i>"),
           ("solo il modale", "<i>Volevo restare, ma non <b>ho potuto</b>.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: sapere, conoscere, ci vuole", "")}
<div class="box" style="margin-top:0"><h4>DUE VERBI DIVERSI</h4><b>Sapere</b> = un'informazione o una capacità. <b>Conoscere</b> = una persona, un luogo, una cosa che hai incontrato o provato.</div>
{_h("1. SAPERE O CONOSCERE?")}
{_tbl(["uso", "esempio"], sc, "8.6pt", ["70mm", None])}
<p class="small" style="margin:.6mm 0"><b>sapere</b>: so, sai, sa, sappiamo, sapete, sanno · <b>conoscere</b>: cono<b>sc</b>o [sk], cono<b>sc</b>i [sci], conosce, conosciamo, conoscete, cono<b>sc</b>ono [sk]. Al passato prossimo il significato cambia un po':</p>
{_tbl(["passato prossimo", "esempio"], pp, "8.6pt", ["70mm", None])}
<div class="two"><div>{_h("2. CI VUOLE / CI VOGLIONO")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt">= è necessario (tempo, cose, qualità)<br><b>ci vuole</b> + singolare: <i>Ci vuole <b>una persona</b> in più. · Ci vuole <b>pazienza</b>.</i><br><b>ci vogliono</b> + plurale: <i>Ci vogliono <b>cinque minuti</b>. · Ci vogliono <b>settimane</b>.</i><br>con <b>per</b> + infinito: <i>Per fare un cappuccino ci vuole il latte.</i><br>passato: <i>c'è voluta un'ora · ci sono voluti due giorni</i></div></div>
<div>{_h("3. I MODALI AL PASSATO PROSSIMO")}
<p style="margin:0 0 .5mm;font-size:8.6pt"><b>dovere, potere, volere</b> prendono l'ausiliare del verbo all'infinito:</p>
{_tbl(["infinito", "esempio"], mod, "8.4pt", ["26mm", None])}
<p class="small" style="margin:.6mm 0">Nel parlato si sente anche <i>ho dovuto andare</i>. <b>volevo</b> (imperfetto) = l'intenzione; <b>ho voluto</b> = l'ho fatto.</p></div></div>
{_dont([("So Matteo.", "<b>Conosco</b> Matteo."), ("Conosco nuotare.", "<b>So</b> nuotare."), ("Conosco dove abita.", "<b>So</b> dove abita."),
        ("Ci vuole cinque minuti.", "Ci <b>vogliono</b> cinque minuti."), ("Giulia ha dovuto andata in banca.", "Giulia <b>è dovuta andare</b> in banca.")])}""",
    16, """<p>Il portoghese ha la stessa coppia <i>saber / conhecer</i>: basta la domanda chiave: <i>è una persona o un posto?</i> → <b>conoscere</b>. <i>Ci vuole</i> corrisponde a <i>leva / é preciso</i>; l'errore tipico è <i>ci vuole</i> con il plurale.</p>""")


def futuro_semplice(b):
    """A2 Ponte 07: il futuro semplice (forme, irregolari), se + presente/futuro, bisogna + infinito."""
    forms = [("io", "torn<b>erò</b>", "prend<b>erò</b>", "part<b>irò</b>", "<b>sarò</b>"),
             ("tu", "torn<b>erai</b>", "prend<b>erai</b>", "part<b>irai</b>", "<b>sarai</b>"),
             ("lui / lei / Lei", "torn<b>erà</b>", "prend<b>erà</b>", "part<b>irà</b>", "<b>sarà</b>"),
             ("noi", "torn<b>eremo</b>", "prend<b>eremo</b>", "part<b>iremo</b>", "<b>saremo</b>"),
             ("voi", "torn<b>erete</b>", "prend<b>erete</b>", "part<b>irete</b>", "<b>sarete</b>"),
             ("loro", "torn<b>eranno</b>", "prend<b>eranno</b>", "part<b>iranno</b>", "<b>saranno</b>")]
    irr = [("perdono una vocale", "andare → <b>andrò</b> · avere → <b>avrò</b> · dovere → <b>dovrò</b> · potere → <b>potrò</b> · sapere → <b>saprò</b> · vedere → <b>vedrò</b> · vivere → <b>vivrò</b>"),
           ("doppia <b>rr</b>", "volere → <b>vorrò</b> · venire → <b>verrò</b> · rimanere → <b>rimarrò</b> · bere → <b>berrò</b>"),
           ("tengono la <b>a</b>", "fare → <b>farò</b> · dare → <b>darò</b> · stare → <b>starò</b>"),
           ("-care, -gare · -ciare, -giare", "cercare → <b>cercherò</b> · pagare → <b>pagherò</b> · cominciare → <b>comincerò</b> · mangiare → <b>mangerò</b>")]
    usi = [("<b>progetti e previsioni</b>", "<i>A ottobre correrò la maratona. · Sarà un anno pieno di novità.</i>"),
           ("<b>promesse</b>", "<i>Le porterò un regalo dal Brasile.</i>"),
           ("<b>una supposizione</b> (forse è così)", "<i>Davide non risponde: dormirà ancora.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: il futuro semplice", "")}
<div class="box" style="margin-top:0"><h4>A CHE COSA SERVE?</h4>Il futuro parla di <b>progetti</b>, <b>previsioni</b> e <b>promesse</b>. Nel parlato, per un futuro vicino e sicuro si usa spesso il <b>presente</b>: <i>Domani parto.</i> = <i>Domani partirò.</i> Il futuro ha la stessa radice del condizionale (unità 05): <i>vorrei → vorrò, andrei → andrò</i>.</div>
{_h("1. LA FORMA")}
{_tbl(["", "-are: tornare", "-ere: prendere", "-ire: partire", "essere"], forms, "8.6pt", ["26mm", None, None, None, None])}
<p class="small" style="margin:.6mm 0">Nei verbi in <b>-are</b> la <b>a</b> diventa <b>e</b>: <i>tornare → torn<b>e</b>rò</i>. L'accento è sull'ultima sillaba di <i>io</i> e <i>lui/lei</i>: <i>tornerò, tornerà</i> (con l'accento scritto!).</p>
{_h("2. GLI IRREGOLARI (COME IL CONDIZIONALE)")}
{_tbl(["gruppo", "verbi"], irr, "8.6pt", ["40mm", None])}
<p class="small" style="margin:.6mm 0">Il futuro di <b>ci vuole</b>: <i>ci vorrà un mese · ci vorranno otto mesi</i>.</p>
<div class="two"><div>{_h("3. QUANDO SI USA?")}
{_tbl(["uso", "esempio"], usi, "8.4pt", ["30mm", None])}</div>
<div>{_h("4. SE… E BISOGNA")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>se + presente</b>, poi presente, futuro o imperativo:<br><i>Se finisco tutto, <b>parto</b> / <b>partirò</b> tranquilla.</i><br><i>Se il cliente telefona, <b>chiamalo</b>!</i><br>anche <b>se + futuro, futuro</b>: <i>Se avrò tempo, verrò.</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt;margin-top:1mm"><b>bisogna + infinito</b> = è necessario (per tutti; non cambia):<br><i>Bisogna finire il progetto. · Bisogna comprare i regali.</i></div></div></div>
{_dont([("tornarò · comprarò", "torn<b>e</b>rò · compr<b>e</b>rò"), ("poterò · volerò", "<b>potrò · vorrò</b>"), ("Bisognamo partire.", "<b>Bisogna</b> partire."),
        ("Se avrò tempo, ti chiamarò.", "…ti chiam<b>e</b>rò.")])}""",
    16, """<p>In Brasile il futuro sintetico (<i>voltarei</i>) si usa poco: lo studente preferisce <i>vou voltar</i>. In italiano <i>vado a tornare</i> non esiste: si usa il futuro o il presente. Stessa radice del condizionale: ripassare le due tabelle insieme.</p>""")


def imperativo_formale(b):
    """A2 Ponte 08: l'imperativo formale (Lei), irregolari, negativo, pronomi prima del verbo; confronto con tu."""
    forms = [("-are", "girare · firmare · pagare", "gir<b>i</b>! · firm<b>i</b>! · pagh<b>i</b>!", "gira! · firma! · paga!"),
             ("-ere", "prendere · chiudere", "prend<b>a</b>! · chiud<b>a</b>!", "prendi! · chiudi!"),
             ("-ire", "sentire · finire", "sent<b>a</b>! · fin<b>isca</b>!", "senti! · finisci!")]
    irr = [("andare", "<b>vada</b>"), ("fare", "<b>faccia</b>"), ("dare", "<b>dia</b>"), ("stare", "<b>stia</b>"), ("dire", "<b>dica</b>"),
           ("venire", "<b>venga</b>"), ("uscire", "<b>esca</b>"), ("essere", "<b>sia</b>"), ("avere", "<b>abbia</b>"), ("sedersi", "<b>si sieda</b>")]
    irl = "".join(f"<tr><td>{a}</td><td>{f}</td></tr>" for a, f in irr)
    pr = [("Mi dia il passaporto.", "Dammi il passaporto."), ("Si sieda!", "Siediti!"), ("Mi racconti tutto.", "Raccontami tutto."),
          ("La controlli.", "Controllala."), ("Non si preoccupi!", "Non preoccuparti!")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: l'imperativo formale (Lei)", "")}
<div class="box" style="margin-top:0"><h4>A CHE COSA SERVE?</h4>Con le persone che non conosciamo, negli uffici, nei negozi e per strada usiamo il <b>Lei</b>. L'imperativo formale serve per dare istruzioni e consigli in modo cortese: <i>Firmi qui. · Vada dritto. · Si sieda, prego.</i> Per l'imperativo informale (<i>tu</i>) vedi l'unità 04.</div>
{_h("1. LA FORMA: LE VOCALI SI SCAMBIANO")}
{_tbl(["verbi", "infinito", "Lei", "tu (unità 04)"], forms, "8.6pt", ["14mm", "40mm", None, None])}
<p class="small" style="margin:.6mm 0">Trucco: i verbi in <b>-are</b> prendono la <b>-i</b>, i verbi in <b>-ere/-ire</b> prendono la <b>-a</b>: il contrario del <i>tu</i>. <i>pagare → paghi</i>, <i>cercare → cerchi</i> (con la <b>h</b>). Negativo: <b>non</b> + la stessa forma: <i>Non chiuda la busta!</i></p>
<div class="two"><div>{_h("2. GLI IRREGOLARI")}
<table style="margin-top:0;font-size:8.6pt"><tr><th>verbo</th><th>Lei</th></tr>{irl}</table>
<p class="small" style="margin:.6mm 0">Molti vengono dalla forma <i>io</i> del presente: <i>(io) faccio → faccia · vengo → venga · esco → esca · dico → dica</i>.</p></div>
<div>{_h("3. I PRONOMI VANNO PRIMA")}
<p style="margin:0 0 .5mm;font-size:8.6pt">Con il <b>Lei</b> i pronomi vanno <b>prima</b> del verbo e non si attaccano (con il <i>tu</i> vanno dopo):</p>
{_tbl(["Lei", "tu"], pr, "8.6pt")}
<p class="small" style="margin:.6mm 0">Espressioni fisse: <b>Mi scusi! · Senta! · Prego, si accomodi. · Si figuri! · Mi dica.</b></p></div></div>
{_dont([("Signora, firma qui.", "Signora, <b>firmi</b> qui."), ("Prendi il numero, signore.", "<b>Prenda</b> il numero."), ("Dia mi il passaporto.", "<b>Mi dia</b> il passaporto."),
        ("Non si preoccupa!", "Non si <b>preoccupi</b>!"), ("Vadi dritto.", "<b>Vada</b> dritto.")])}""",
    16, """<p>Il portoghese ha la stessa logica (<i>o senhor vire à direita, assine aqui</i>): -are → -i, -ere/-ire → -a. Errori tipici: <i>vadi</i> e <i>facci</i> per analogia, e il pronome attaccato (<i>diami</i>). Fare tante istruzioni brevi a voce.</p>""")


def congiuntivo_presente(b):
    """A2 Ponte 09: primo contatto con il congiuntivo presente dopo penso, credo, spero, mi sembra che; secondo me + indicativo; di + infinito."""
    forms = [("io / tu / lui / lei / Lei", "parl<b>i</b>", "prend<b>a</b>", "dorm<b>a</b>", "<b>sia</b>", "<b>abbia</b>"),
             ("noi", "parl<b>iamo</b>", "prend<b>iamo</b>", "dorm<b>iamo</b>", "<b>siamo</b>", "<b>abbiamo</b>"),
             ("voi", "parl<b>iate</b>", "prend<b>iate</b>", "dorm<b>iate</b>", "<b>siate</b>", "<b>abbiate</b>"),
             ("loro", "parl<b>ino</b>", "prend<b>ano</b>", "dorm<b>ano</b>", "<b>siano</b>", "<b>abbiano</b>")]
    trig = [("<b>penso che · credo che · mi sembra che</b>", "un'opinione", "<i>Penso che il nostro progetto <b>sia</b> il migliore.</i>"),
            ("<b>spero che</b>", "una speranza", "<i>Spero che il Comune <b>scelga</b> noi.</i>"),
            ("<b>non sono sicuro/a che · non so se</b>", "un dubbio", "<i>Non sono sicura che <b>venga</b>.</i>")]
    ind = [("<b>secondo me · per me</b>", "<i>Secondo me Bologna <b>è</b> troppo cara.</i>"),
           ("<b>so che · sono sicuro/a che · è vero che</b>", "<i>So che <b>viene</b>. · Sono sicura che <b>ha</b> ragione.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: primo incontro con il congiuntivo", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Il <b>congiuntivo</b> è il modo delle <b>opinioni</b>, delle <b>speranze</b> e dei <b>dubbi</b>: non presenta un fatto sicuro, ma quello che pensiamo o speriamo. Buona notizia: le forme di <i>io, tu, lui, lei</i> le conosci già, sono come l'imperativo formale dell'unità 08 (<i>Vada! → Spero che vada</i>).</div>
{_h("1. LA FORMA")}
{_tbl(["", "-are: parlare", "-ere: prendere", "-ire: dormire", "essere", "avere"], forms, "8.6pt", ["34mm", None, None, None, None, None])}
<p class="small" style="margin:.6mm 0">Le tre persone singolari sono <b>uguali</b>: per questo spesso aggiungiamo il soggetto (<i>Penso che <b>tu</b> abbia ragione</i>). Irregolari come l'imperativo formale: <b>vada, faccia, dia, stia, dica, venga, esca, scelga, possa, voglia, debba, sappia</b>.</p>
{_h("2. DOPO QUALI ESPRESSIONI?")}
{_tbl(["espressione + che", "per…", "esempio"], trig, "8.6pt", ["56mm", "24mm", None])}
<div class="two"><div>{_h("3. ATTENZIONE: CON L'INDICATIVO")}
{_tbl(["espressione", "esempio"], ind, "8.4pt", ["34mm", None])}</div>
<div>{_h("4. STESSO SOGGETTO: DI + INFINITO")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt">Se il soggetto è lo stesso, niente <i>che</i>:<br><i>(Io) spero che <b>(io)</b> vinca</i> ✗ → <i>Spero <b>di vincere</b>.</i><br><i>Penso <b>di partire</b> a maggio.</i><br><i>Credo <b>di avere</b> ragione.</i><br>Soggetto diverso: <i>Spero che <b>tu</b> vinca.</i></div></div></div>
{_dont([("Penso che è caro.", "Penso che <b>sia</b> caro."), ("Secondo me sia caro.", "Secondo me <b>è</b> caro."), ("Spero che vadi bene.", "Spero che <b>vada</b> bene."),
        ("Spero che io vinca.", "Spero <b>di vincere</b>."), ("Penso che sì.", "Penso <b>di sì</b>.")])}""",
    16, """<p>In portoghese c'è il <i>subjuntivo</i>, ma dopo <i>acho que</i> si usa l'indicativo (<i>acho que é caro</i>): da qui l'errore <i>penso che è</i>. Basta un primo contatto con <i>sia, abbia, vada, faccia</i>; il resto al B1.</p>""")


def pronomi_diretti_passato(b):
    """A2 Ponte 11: pronomi diretti con il passato prossimo (accordo del participio); già, non… ancora, appena; il pronome che riprende il nome."""
    forms = [("il film", "<b>lo</b> vedo", "<b>l'</b>ho vist<b>o</b>", "<i>Il film? L'ho già visto.</i>"),
             ("la mostra", "<b>la</b> vedo", "<b>l'</b>ho vist<b>a</b>", "<i>La mostra? Non l'ho ancora vista.</i>"),
             ("i biglietti", "<b>li</b> compro", "<b>li</b> ho comprat<b>i</b>", "<i>I biglietti? Li ho presi ieri.</i>"),
             ("le foto", "<b>le</b> guardo", "<b>le</b> ho guardat<b>e</b>", "<i>Le foto? Alcune le ho viste.</i>")]
    adv = [("<b>già</b>", "una cosa fatta (prima del previsto)", "Ho <b>già</b> visto il film. · L'ho <b>già</b> visto."),
           ("<b>non… ancora</b>", "una cosa non fatta (ma la farò)", "<b>Non</b> ho <b>ancora</b> visto la mostra. · <b>Non</b> l'ho <b>ancora</b> vista."),
           ("<b>appena</b>", "una cosa fatta un momento fa", "Ho <b>appena</b> sentito Davide. · Siamo <b>appena</b> arrivate.")]
    cmp = [("pronome <b>diretto</b> (lo, la, li, le)", "il participio <b>cambia</b>", "<i>La mostra? L'ho vist<b>a</b>.</i>"),
           ("pronome <b>indiretto</b> (gli, le)", "il participio <b>non cambia</b>", "<i>A Giulia? Le ho telefonat<b>o</b>.</i>"),
           ("nessun pronome", "il participio <b>non cambia</b>", "<i>Ho vist<b>o</b> la mostra.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: l'ho visto, l'ho vista", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Con il passato prossimo il pronome diretto va <b>prima di avere</b>: <i>lo, la</i> diventano <b>l'</b> e il participio prende il genere e il numero della cosa (<b>-o, -a, -i, -e</b>). Così, anche quando diciamo solo <i>l'ho vista</i>, chi ascolta capisce che parliamo di una cosa femminile.</div>
{_h("1. LA FORMA")}
{_tbl(["la cosa", "presente", "passato prossimo", "esempio"], forms, "8.6pt", ["24mm", "24mm", "34mm", None])}
<p class="small" style="margin:.6mm 0">Davanti a <i>ho, hai, ha, hanno</i> scriviamo <b>l'</b>: <i>l'ho, l'hai, l'ha, l'hanno</i>. <i>Li</i> e <i>le</i> non cambiano mai: <i>li ho, le ho</i>.</p>
{_h("2. GIÀ, NON… ANCORA, APPENA")}
{_tbl(["parola", "per dire…", "esempio (va tra avere e il participio)"], adv, "8.6pt", ["24mm", "46mm", None])}
<div class="two"><div>{_h("3. QUANDO CAMBIA IL PARTICIPIO?")}
{_tbl(["con…", "", "esempio"], cmp, "8.2pt", ["30mm", "24mm", None])}</div>
<div>{_h("4. PRIMA LA COSA, POI IL PRONOME")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt">Nel parlato mettiamo la cosa all'inizio e poi la riprendiamo con il pronome:<br><i><b>I biglietti li</b> compro io.</i><br><i><b>Il libro l'</b>ho letto tutto.</i><br><i><b>Le birre le</b> pago io!</i><br>Il pronome è obbligatorio: <s>I biglietti compro io.</s></div></div></div>
{_dont([("Ho visto lo.", "<b>L'ho visto</b>."), ("La mostra? L'ho visto.", "L'ho vist<b>a</b>."), ("I biglietti? Li ho comprato.", "Li ho comprat<b>i</b>."),
        ("Ancora non ho visto.", "<b>Non</b> l'ho <b>ancora</b> visto."), ("Ho già lo visto.", "<b>L'ho già</b> visto.")])}""",
    16, """<p>In portoghese il pronome si mette spesso dopo il verbo o si omette (<i>vi ontem</i>), e il participio non cambia. Per lo studente l'accordo <i>l'ho vista</i> non è naturale: farlo ascoltare molte volte (pagina 5B) prima di chiederlo nello scritto.</p>""")


def modali_passato_ne(b):
    """A2 Ponte 12: volevo / ho voluto, dovevo / ho dovuto, potevo / ho potuto; ne con le quantità e l'accordo del participio."""
    forms = [("volere", "volevo, volevi, voleva, volevamo, volevate, volevano", "ho voluto"),
             ("dovere", "dovevo, dovevi, doveva, dovevamo, dovevate, dovevano", "ho dovuto"),
             ("potere", "potevo, potevi, poteva, potevamo, potevate, potevano", "ho potuto")]
    uses = [("<b>imperfetto</b>: volevo, dovevo, potevo", "un'intenzione, un programma, una possibilità: <b>non sappiamo</b> se è successo (spesso + <i>ma</i>)", "<i>Volevo vedere il Palazzo Ducale, ma c'era la fila.</i><br><i>Dovevamo arrivare alle nove.</i>"),
            ("<b>passato prossimo</b>: ho voluto, ho dovuto, ho potuto", "una cosa che <b>è successa</b> davvero (o che non è successa: <i>non ho potuto</i>)", "<i>Abbiamo dovuto prendere il pullman.</i><br><i>Non ho potuto vederlo.</i> · <i>Ho voluto vedere tutto.</i>")]
    ne = [("Quanti ombrelli hai?", "<b>Ne</b> ho uno.", "ne = di ombrelli"), ("Quanti cicchetti volete?", "<b>Ne</b> prendiamo sei.", "ne = di cicchetti"),
          ("Quante foto hai fatto?", "<b>Ne</b> ho fatt<b>e</b> trecento.", "il participio si accorda: foto → -e"),
          ("Hai comprato cartoline?", "Sì, <b>ne</b> ho comprat<b>e</b> cinque. / No, non <b>ne</b> ho comprat<b>a</b> nessuna.", "")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: volevo o ho voluto? · ne", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Al passato <i>volere, dovere, potere</i> hanno due forme con un significato diverso. Con l'<b>imperfetto</b> raccontiamo i programmi e le intenzioni (spesso andati male: <i>volevo…, ma…</i>); con il <b>passato prossimo</b> diciamo che cosa è successo davvero. <b>Ne</b> sostituisce un nome quando parliamo di una <b>quantità</b>.</div>
{_h("1. LA FORMA")}
{_tbl(["", "imperfetto (regolare)", "passato prossimo"], forms, "8.6pt", ["18mm", None, "30mm"])}
<p class="small" style="margin:.6mm 0">Con un verbo che vuole <i>essere</i> si può usare <i>essere</i>: <i>Non sono potuta entrare</i> (come <i>Giulia è dovuta andare</i>, unità 06). L'accento dell'imperfetto: vol<b>é</b>vo, volev<b>à</b>mo, vol<b>é</b>vano.</p>
{_h("2. IMPERFETTO O PASSATO PROSSIMO?")}
{_tbl(["forma", "per dire…", "esempio"], uses, "8.5pt", ["40mm", "58mm", None])}
{_h("3. NE CON LE QUANTITÀ")}
{_tbl(["domanda", "risposta", ""], ne, "8.5pt", ["40mm", "64mm", None])}
<p class="small" style="margin:.6mm 0"><i>Ne</i> va prima del verbo (<i>ne prendiamo</i>) o si attacca all'infinito (<i>volevo portar<b>ne</b> uno</i>). Al passato il participio si accorda con la cosa: <i>ne ho fatt<b>e</b> trecento</i> (le foto), <i>ne ho comprat<b>i</b> due</i> (i biglietti).</p>
{_dont([("Volevo vedere il museo e l'ho visto.", "<b>Ho voluto</b> vedere il museo (e l'ho visto)."), ("Ho dovuto partire alle sette, ma il treno era cancellato.", "<b>Dovevo</b> partire…"),
        ("Quante foto? Ho fatto trecento.", "<b>Ne</b> ho fatt<b>e</b> trecento."), ("Ne ho fatto trecento (foto).", "Ne ho fatt<b>e</b>."), ("Ho uno.", "<b>Ne</b> ho uno.")])}""",
    21, """<p>In portoghese <i>eu queria / eu quis</i> funziona in modo simile: <i>queria ver, mas…</i> = <i>volevo vedere, ma…</i>. Il problema più grande è <i>ne</i>, che il portoghese non ha: lo studente dice <i>ho uno</i> o <i>ho fatto trecento</i>. Farlo ripetere in domanda e risposta veloce.</p>""")


def comparativi_superlativi(b):
    """A2 Ponte 13: comparativo di uguaglianza (così… come, tanto… quanto), superlativo relativo e assoluto (-issimo), meglio / migliore, peggio / peggiore."""
    cmp = [("<b>più</b> … <b>di</b> / <b>che</b>", "superiorità", "<i>Tommaso ha <b>più</b> esperienza <b>di</b> Elena.</i> · <i>È più facile parlare <b>che</b> scrivere.</i>"),
           ("<b>meno</b> … <b>di</b>", "inferiorità", "<i>Chiara è <b>meno</b> socievole <b>di</b> Bruno.</i>"),
           ("<b>(così)</b> … <b>come</b> · <b>(tanto)</b> … <b>quanto</b>", "uguaglianza", "<i>Elena è brava <b>quanto</b> Tommaso.</i> · <i>Non sei <b>così</b> paziente <b>come</b> pensi.</i>")]
    sup = [("relativo: <b>il / la più</b> … <b>di</b>", "il primo di un gruppo", "<i>La tua stanza è <b>la più</b> disordinata <b>del</b> palazzo.</i>"),
           ("assoluto: <b>-issimo</b>", "= molto, moltissimo", "<i>bello → bell<b>issimo</b> · gentile → gentil<b>issima</b> · simpatico → simpatic<b>issimi</b></i>")]
    irr = [("buono", "<b>migliore</b> (= più buono)", "<b>il migliore</b>", "<b>ottimo</b>", "<i>I disegni di Elena sono <b>migliori</b>.</i>"),
           ("cattivo", "<b>peggiore</b>", "<b>il peggiore</b>", "<b>pessimo</b>", "<i>La stanza di Bruno è <b>peggiore</b> della mia.</i>"),
           ("bene (avverbio)", "<b>meglio</b>", "—", "<b>benissimo</b>", "<i>Elena parla inglese <b>meglio</b> di lui.</i>"),
           ("male (avverbio)", "<b>peggio</b>", "—", "<b>malissimo</b>", "<i>Oggi sto <b>peggio</b> di ieri.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: paragoni e superlativi", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Per descrivere le persone spesso le <b>paragoniamo</b>: <i>più, meno, quanto</i>. Il <b>superlativo</b> dice chi è il primo di un gruppo (<i>la più disordinata del palazzo</i>) o che una qualità è molto forte (<i>bravissima</i>). <i>Buono, cattivo, bene, male</i> hanno anche forme speciali.</div>
{_h("1. I COMPARATIVI")}
{_tbl(["forma", "per…", "esempio"], cmp, "8.6pt", ["44mm", "22mm", None])}
{_h("2. I SUPERLATIVI")}
{_tbl(["forma", "per…", "esempio"], sup, "8.6pt", ["44mm", "30mm", None])}
<p class="small" style="margin:.6mm 0"><i>-issimo</i> si accorda: <i>-issimo, -issima, -issimi, -issime</i>. Con <i>-co, -go</i> attenzione all'<i>h</i>: <i>ricco → ricc<b>h</b>issimo, lungo → lung<b>h</b>issimo</i> (ma <i>simpatico → simpaticissimo</i>).</p>
{_h("3. FORME SPECIALI")}
{_tbl(["", "comparativo", "superlativo relativo", "assoluto", "esempio"], irr, "8.4pt", ["24mm", "30mm", "26mm", "20mm", None])}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt;margin-top:1mm"><b>meglio o migliore?</b> Se puoi dire <i>più buono / più buona</i> → <b>migliore</b> (con un nome: <i>il regalo migliore</i>). Se puoi dire <i>più bene</i> → <b>meglio</b> (con un verbo: <i>parla meglio</i>; con <i>è</i> = è una scelta migliore: <i>un libro è meglio</i>).</div>
{_dont([("È più alto que me.", "È più alto <b>di</b> me."), ("È tanto bravo come Tommaso.", "È bravo <b>quanto</b> / <b>così</b> bravo <b>come</b> Tommaso."),
        ("Parla inglese migliore.", "Parla inglese <b>meglio</b>."), ("È il più migliore.", "È <b>il migliore</b>."), ("Molto bellissimo.", "<b>Bellissimo</b>.")])}""",
    20, """<p>In portoghese <i>melhor</i> vale sia per <i>migliore</i> che per <i>meglio</i>: da qui l'errore <i>parla migliore</i>. Usare la prova "più buono / più bene". <i>Tanto… quanto</i> e <i>così… come</i>: spesso basta solo <i>quanto</i> o <i>come</i> (<i>bravo quanto lui</i>).</p>""")


def ne_ci(b):
    """A2 Ponte 14: ne partitivo (quantità, non… più, ce n'è / ce ne sono) e ci locativo (ci vado) + ci pensare / credere."""
    ne = [("un numero", "Quante uova compri? — <b>Ne</b> compro dieci dozzine."), ("un peso / una misura", "Quanto formaggio? — <b>Ne</b> prendo due etti. · <b>Ne</b> usiamo trenta litri."),
          ("una quantità vaga", "<b>Ne</b> ho ancora un po'. · <b>Ne</b> vuole un po'?"), ("zero", "Non <b>ne</b> ho più. · Non <b>ne</b> buttiamo più.")]
    ci = [("<b>ci</b> = in / a quel posto", "Vai al mercato? — Sì, <b>ci</b> vado ogni sabato. · <b>Ci</b> arrivo alle otto."),
          ("<b>ci</b> + pensare / credere", "Pensi all'ambiente? — Sì, <b>ci</b> penso. · <b>Ci</b> ho pensato a lungo."),
          ("<b>c'è / ci sono</b> + ne", "Ci sono fragole? — No, non <b>ce ne</b> sono. · C'è formaggio? — Sì, <b>ce n'è</b> ancora.")]
    cmp = [("<b>lo, la, li, le</b>", "tutta la cosa", "<i>Le uova? <b>Le</b> ho finite.</i> (tutte)"),
           ("<b>ne</b>", "una parte, una quantità", "<i>Le uova? <b>Ne</b> ho prese sei.</i> (sei di tutte)"),
           ("<b>ci</b>", "un luogo (o un'idea con <i>pensare a</i>)", "<i>Al mercato? <b>Ci</b> vado domani.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: ne e ci", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4><b>Ne</b> e <b>ci</b> sono due piccole parole che evitano di ripetere. <b>Ne</b> sostituisce un nome quando parliamo di una <b>quantità</b> (anche zero). <b>Ci</b> sostituisce un <b>luogo</b> (<i>al mercato, a Bologna, in via San Vitale</i>) e la cosa a cui pensiamo (<i>pensare a…</i>). Tutti e due vanno <b>prima del verbo</b>.</div>
{_h("1. NE: QUANTO?")}
{_tbl(["con…", "esempio"], ne, "8.6pt", ["38mm", None])}
{_h("2. CI: DOVE? A CHE COSA?")}
{_tbl(["uso", "esempio"], ci, "8.6pt", ["38mm", None])}
<p class="small" style="margin:.6mm 0">Davanti a <i>ne</i>, <i>ci</i> diventa <b>ce</b>: <i>ce n'è, ce ne sono</i>. Al passato: <i>Ci sono andata ieri. · Ne ho comprat<b>e</b> sei</i> (le uova: accordo, come nell'unità 12).</p>
{_h("3. LO, NE O CI?")}
{_tbl(["pronome", "per…", "esempio"], cmp, "8.6pt", ["24mm", "46mm", None])}
{_dont([("Quanto formaggio? Prendo due etti.", "<b>Ne</b> prendo due etti."), ("Non ho più uova. — Neanche io ho.", "Neanch'io <b>ne</b> ho."),
        ("Vai al mercato? Sì, vado lì ogni sabato.", "Sì, <b>ci</b> vado."), ("Ci ne sono?", "<b>Ce ne</b> sono?"), ("Penso a questo. → Lo penso.", "<b>Ci</b> penso.")])}""",
    20, """<p>Il portoghese non ha <i>ne</i> e usa poco <i>ci</i> (<i>vou lá</i>): lo studente tende a ometterli o a dire <i>lì</i>. Non serve vietare <i>lì</i>, ma <i>ci vado</i> è la forma naturale. Lavorare con domande veloci: <i>Quanto? → ne. Dove? → ci.</i></p>""")


def stare_gerundio(b):
    """A2 Ponte 15: stare + gerundio (azione in corso), stare per + infinito (azione imminente), gerundi irregolari, pronomi."""
    forms = [("io", "<b>sto</b>", "pul<b>endo</b>", "<b>Sto</b> pulendo la casa."), ("tu", "<b>stai</b>", "fac<b>endo</b>", "Che cosa <b>stai</b> facendo?"),
             ("lui / lei / Lei", "<b>sta</b>", "abbai<b>ando</b>", "Briciola <b>sta</b> abbaiando."), ("noi", "<b>stiamo</b>", "arriv<b>ando</b>", "<b>Stiamo</b> arrivando!"),
             ("voi", "<b>state</b>", "mangi<b>ando</b>", "Che cosa <b>state</b> mangiando?"), ("loro", "<b>stanno</b>", "suon<b>ando</b>", "<b>Stanno</b> suonando alla porta.")]
    ger = [("-are → <b>-ando</b>", "parlare → parl<b>ando</b> · passare → pass<b>ando</b> · cercare → cerc<b>ando</b>"),
           ("-ere → <b>-endo</b>", "bere → <b>bevendo</b> · leggere → legg<b>endo</b> · scrivere → scriv<b>endo</b>"),
           ("-ire → <b>-endo</b>", "dormire → dorm<b>endo</b> · aprire → apr<b>endo</b> · pulire → pul<b>endo</b>"),
           ("irregolari", "fare → <b>facendo</b> · bere → <b>bevendo</b> · dire → <b>dicendo</b>")]
    cmp = [("<b>stare + gerundio</b>", "adesso, in questo momento", "<i>Sto bevendo un caffè.</i>"),
           ("<b>stare per + infinito</b>", "tra pochissimo (non ancora)", "<i>Sto per uscire.</i> · <i>La maglietta sta per cadere!</i>"),
           ("<b>presente</b>", "anche adesso: va benissimo!", "<i>Che fai? — Bevo un caffè.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: stare + gerundio, stare per", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4><b>Stare + gerundio</b> dice che un'azione è <b>in corso</b>, proprio adesso: <i>Sto passando l'aspirapolvere.</i> <b>Stare per + infinito</b> dice che un'azione <b>comincia tra pochissimo</b>: <i>Sto per buttare la pasta.</i> Il verbo <i>stare</i> cambia con la persona; il gerundio non cambia mai.</div>
{_h("1. LA FORMA")}
{_tbl(["persona", "stare", "gerundio", "esempio"], forms, "8.6pt", ["26mm", "17mm", "22mm", None])}
{_h("2. IL GERUNDIO")}
{_tbl(["verbo", "esempi"], ger, "8.6pt", ["30mm", None])}
<p class="small" style="margin:.6mm 0">I pronomi vanno <b>prima di stare</b> o <b>attaccati al gerundio</b>: <i><b>Lo</b> sto facendo</i> = <i>Sto facendo<b>lo</b></i>. · <i><b>Mi</b> sto preparando</i> = <i>Sto preparando<b>mi</b></i>. Con <i>stare per</i>: <i><b>Ti</b> sto per chiamare</i> = <i>Sto per chiamar<b>ti</b></i>.</p>
{_h("3. ADESSO O TRA POCO?")}
{_tbl(["forma", "quando?", "esempio"], cmp, "8.6pt", ["38mm", "44mm", None])}
{_dont([("Sto abitando a Bologna.", "<b>Abito</b> a Bologna."), ("Sto avendo un problema.", "<b>Ho</b> un problema."),
        ("Sto faccendo / sto fando.", "Sto <b>facendo</b>."), ("Sto per uscendo.", "Sto per <b>uscire</b>."), ("Stanno suonandi.", "Stanno <b>suonando</b>.")])}""",
    20, """<p>In italiano <i>stare + gerundio</i> si usa meno che in portoghese: solo per un'azione proprio in corso. Per situazioni lunghe o abituali si usa il presente (<i>abito, lavoro in uno studio</i>), e con <i>avere, essere, sapere, volere</i> il gerundio progressivo non si usa. Il gerundio è invariabile (mai <i>-andi, -enda</i>).</p>""")


def che_cui(b):
    """A2 Ponte 16: pronomi relativi che (soggetto/oggetto) e cui (dopo preposizione); in cui = dove; il quale (riconoscere)."""
    che = [("soggetto", "un ufficio postale <b>che</b> apre il pomeriggio", "(l'ufficio postale apre)"),
           ("oggetto", "la città <b>che</b> vorrei · l'idea <b>che</b> mi piace", "(vorrei la città)")]
    cui = [("<b>in cui</b>", "la via <b>in cui</b> abito · una piazza <b>in cui</b> i ragazzi suonano", "abito <b>in</b> una via"),
           ("<b>con cui</b>", "la signora <b>con cui</b> parli sulle scale", "parli <b>con</b> la signora"),
           ("<b>di cui</b>", "un'idea <b>di cui</b> parla da anni", "parla <b>di</b> un'idea"),
           ("<b>su cui</b>", "panchine <b>su cui</b> riposare", "riposare <b>su</b> panchine"),
           ("<b>a cui</b>", "l'amica <b>a cui</b> scrivo", "scrivo <b>a</b> un'amica"),
           ("<b>per cui</b>", "il motivo <b>per cui</b> vado in bici", "vado in bici <b>per</b> un motivo")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: che e cui", "")}
<div class="box" style="margin-top:0"><h4>CHE COSA SONO?</h4>I pronomi relativi uniscono due frasi e evitano di ripetere un nome: <i>Vorrei una biblioteca. La biblioteca resta aperta fino alle dieci.</i> → <i>Vorrei una biblioteca <b>che</b> resta aperta fino alle dieci.</i> <b>Che</b> e <b>cui</b> non cambiano mai: maschile, femminile, singolare, plurale.</div>
{_h("1. CHE: SENZA PREPOSIZIONE")}
{_tbl(["funzione", "esempio", "perché"], che, "8.6pt", ["24mm", None, "46mm"])}
{_h("2. CUI: DOPO UNA PREPOSIZIONE")}
{_tbl(["preposizione + cui", "esempio", "il verbo vuole…"], cui, "8.6pt", ["32mm", None, "46mm"])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. IN CUI O DOVE?</b><br>Per un luogo si può dire anche <b>dove</b>: <i>la via <b>in cui</b> abito = la via <b>dove</b> abito</i>. Per il tempo: <i>il giorno <b>in cui</b> sono arrivata</i>.</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. IL QUALE (DA RICONOSCERE)</b><br>Nello scritto formale: <i>il quale, la quale, i quali, le quali</i> (<i>la signora <b>con la quale</b> parli</i> = <i>con cui</i>). Nel parlato si usa poco.</div></div>
{_dont([("La via che abito.", "La via <b>in cui</b> abito."), ("La signora che parlo sempre.", "La signora <b>con cui</b> parlo."),
        ("Un'idea che parla da anni.", "Un'idea <b>di cui</b> parla."), ("La ragazza cui esco.", "<b>con</b> cui esco"), ("Il libro cui leggo.", "Il libro <b>che</b> leggo.")])}""",
    20, """<p>In portoghese <i>que</i> va bene quasi sempre nel parlato (<i>a rua que eu moro</i>): lo studente dice <i>la via che abito</i>. Metodo: guardare il verbo della seconda frase: <i>abitare <b>in</b>, parlare <b>con / di</b></i> → la preposizione va davanti a <i>cui</i>. Senza preposizione → <i>che</i>. <i>Cui</i> si pronuncia [kùi], due vocali.</p>""")


def si_impersonale(b):
    """A2 Ponte 17: si impersonale (si + 3a sing.), si + verbo plurale con nome plurale, è vietato / è obbligatorio / bisogna + infinito."""
    si = [("<b>si</b> + verbo (3ª persona singolare)", "Qui <b>si paga</b> prima. · In Italia <b>si mangia</b> tardi. · <b>Non si fuma</b>."),
          ("<b>si</b> + verbo singolare + nome singolare", "Il cappuccino <b>si beve</b> la mattina. · Il portone <b>si chiude</b>."),
          ("<b>si</b> + verbo plurale + nome plurale", "Le bici <b>si mettono</b> in cortile. · <b>Si vendono</b> biglietti."),
          ("<b>si può / si deve</b> + infinito", "Qui <b>si può</b> pagare dopo. · <b>Si deve</b> chiudere il portone.")]
    reg = [("<b>è vietato</b> + infinito", "non si può (regola)", "<b>È vietato</b> fumare. · <b>È vietato</b> lasciare le bici nell'ingresso."),
           ("<b>è obbligatorio</b> + infinito", "si deve (regola)", "<b>È obbligatorio</b> fare la raccolta differenziata."),
           ("<b>è permesso</b> + infinito", "si può", "<b>È permesso</b> entrare con il cane."),
           ("<b>bisogna</b> + infinito", "è necessario", "<b>Bisogna</b> arrivare presto. (unità 14)")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: il si impersonale, è vietato", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Con il <b>si impersonale</b> parliamo di regole e abitudini <b>di tutti</b>, senza dire chi fa l'azione: <i>Qui <b>si paga</b> prima</i> (= tutti pagano prima). È come il portoghese <i>a gente</i> / <i>se</i>: <i>aqui se paga antes</i>. Per le regole scritte si usa anche <b>è vietato / è obbligatorio + infinito</b>.</div>
{_h("1. IL SI IMPERSONALE")}
{_tbl(["forma", "esempio"], si, "8.6pt", ["60mm", None])}
<p class="small" style="margin:.6mm 0">Con un nome <b>plurale</b> il verbo va al <b>plurale</b>: <i>si mettono le bici, si vendono biglietti</i>. Negazione: <b>non si</b> + verbo (<i>non si stende sul balcone</i>). Con i verbi riflessivi: <b>ci si</b> (<i>ci si siede, ci si alza presto</i>), da riconoscere.</p>
{_h("2. LE REGOLE")}
{_tbl(["espressione", "significa", "esempio"], reg, "8.6pt", ["40mm", "32mm", None])}
<p class="small" style="margin:.6mm 0">Sui cartelli spesso solo: <b>vietato fumare</b>, <b>vietato l'ingresso</b>, <b>obbligatorio il casco</b>. Il contrario di <i>vietato</i> è <i>permesso / consentito</i>.</p>
{_dont([("Qui paga prima.", "Qui <b>si</b> paga prima."), ("Si mette le bici in cortile.", "Si <b>mettono</b> le bici."), ("È vietato di fumare.", "È vietato fumare."),
        ("Si non fuma.", "<b>Non si</b> fuma."), ("È obbligatorio che chiudere.", "È obbligatorio chiudere.")])}""",
    20, """<p>Nel parlato brasiliano si dice spesso <i>aqui paga antes</i>, senza <i>se</i>: lo studente omette <i>si</i>. E dice <i>si vende case</i> (come <i>vende-se casas</i> nel parlato): in italiano <i>si vendono case</i>. Dopo <i>è vietato / obbligatorio</i> nessuna preposizione (non <i>di</i>, non <i>a</i>).</p>""")


def connettivi_email(b):
    """A2 Ponte 18: connettivi (infatti, invece, quindi, però, comunque) + la mail formale e informale."""
    con = [("<b>però</b>", "contrasto (= ma)", "Sara vuole venire, <b>però</b> sabato io lavoro. · È un divano, <b>però</b> è comodo."),
           ("<b>invece</b>", "il contrario, un confronto", "In Italia si scrive <i>cordiali saluti</i>; in Brasile, <b>invece</b>, <i>um abraço</i>. · <b>invece di</b> + infinito"),
           ("<b>infatti</b>", "conferma, spiega", "Fa caldo: <b>infatti</b> ieri c'erano 32 gradi."),
           ("<b>quindi</b>", "conseguenza (= allora)", "Le bici sono per terra, <b>quindi</b> i bambini non giocano."),
           ("<b>comunque</b>", "in ogni caso, anyway", "Sabato lavoro. <b>Comunque</b> possiamo venire domenica.")]
    mail = [("saluto", "<b>Gentile</b> signora Bianchi, · <b>Gentile</b> ragionier Ferri, · Buongiorno,", "<b>Ciao</b> Sara! · <b>Cara</b> Sara, · <b>Caro</b> Luca,"),
            ("inizio", "<b>Le scrivo per</b> chiedere / informare… · Mi chiamo…", "Come stai? · <b>Ti scrivo per</b>…"),
            ("richiesta", "<b>Potrebbe</b>…? · <b>Vorrei sapere</b> se…", "<b>Puoi</b>…? · <b>Fammi sapere!</b>"),
            ("chiusura", "<b>La ringrazio</b> e resto in attesa di una Sua risposta.", "Un bacio a tutti! · A presto!"),
            ("firma", "<b>Cordiali saluti</b>, + nome e cognome", "<b>Un abbraccio</b>, + nome")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: i connettivi e la mail", "")}
<div class="box" style="margin-top:0"><h4>CHE COSA SONO?</h4>I <b>connettivi</b> sono piccole parole che uniscono le frasi e mostrano il rapporto tra le idee: contrasto, conseguenza, conferma. Rendono un testo chiaro e naturale. In una <b>mail</b> cambiano anche il saluto, il pronome (<i>Lei</i> o <i>tu</i>) e la firma.</div>
{_h("1. I CONNETTIVI")}
{_tbl(["connettivo", "per…", "esempio"], con, "8.6pt", ["22mm", "36mm", None])}
<p class="small" style="margin:.6mm 0"><b>Però</b> e <b>invece</b> possono andare anche dopo il soggetto o alla fine: <i>Io, <b>invece</b>, lavoro. · Hai ragione, <b>però</b>.</i> <b>Infatti!</b> da solo = <i>Exatamente! / Pois é!</i></p>
{_h("2. LA MAIL: FORMALE O INFORMALE?")}
{_tbl(["parte", "formale (Lei)", "informale (tu)"], mail, "8.4pt", ["20mm", None, None])}
{_dont([("Comunque = como?", "<b>comunque</b> = de qualquer forma"), ("Prezado signor Ferri,", "<b>Gentile</b> signor Ferri,"),
        ("Att., Júlia", "<b>Cordiali saluti</b>, Júlia …"), ("Invece dormire in albergo", "<b>Invece di</b> dormire"), ("Gentile Ferri, come stai?", "come <b>sta</b>?")])}""",
    20, """<p>Falsi amici: <i>comunque</i> non è <i>como</i>; <i>infatti</i> conferma (<i>de fato, realmente</i>); <i>invece</i> = <i>em vez / por outro lado</i>. Nelle mail formali gli italiani non usano <i>abbraccio</i> né <i>bacio</i>: <i>Cordiali saluti</i> (o <i>Distinti saluti</i>, più freddo). Titoli: <i>dottore / dottoressa</i> (laureati), <i>ragioniere</i>, <i>avvocato</i>, <i>ingegnere</i>.</p>""")


def verbi_preposizione(b):
    """A2 Ponte 20: verbi + a / di + infinito; verbi senza preposizione."""
    va = [("cominciare <b>a</b>", "Ho cominciato <b>a</b> studiare a maggio."), ("continuare <b>a</b>", "Ho continuato <b>a</b> parlare."),
          ("provare <b>a</b>", "Prova <b>a</b> respirare."), ("aiutare qualcuno <b>a</b>", "Chiara mi ha aiutato <b>a</b> ripassare."),
          ("imparare <b>a</b> · riuscire <b>a</b>", "Ho imparato <b>a</b> guidare. · Non riesco <b>a</b> dormire.")]
    vd = [("finire <b>di</b>", "Non ho finito <b>di</b> ripassare."), ("smettere <b>di</b>", "Smetti <b>di</b> preoccuparti!"),
          ("decidere <b>di</b>", "Ho deciso <b>di</b> non bere il caffè."), ("dimenticare <b>di</b> · ricordarsi <b>di</b>", "Ho dimenticato <b>di</b> dire una data. · Ricordati <b>di</b> portare il documento."),
          ("promettere <b>di</b> · cercare <b>di</b>", "Ha promesso <b>di</b> smettere. · Cerco <b>di</b> dormire."), ("avere paura <b>di</b> · sperare <b>di</b>", "Ho paura <b>di</b> dimenticare. · Spero <b>di</b> passare.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: verbi + a / di + infinito", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Quando un verbo è seguito da un altro verbo all'infinito, spesso in mezzo c'è una <b>preposizione</b>: <b>a</b> o <b>di</b>. Non c'è una regola sicura: bisogna <b>impararli insieme</b>, come una parola sola (<i>cominciare a, finire di</i>). Un aiuto: molti verbi di <b>inizio e movimento</b> vogliono <i>a</i>; molti verbi di <b>fine, decisione e memoria</b> vogliono <i>di</i>.</div>
{_h("1. VERBI + A + INFINITO")}
{_tbl(["verbo", "esempio"], va, "8.6pt", ["46mm", None])}
{_h("2. VERBI + DI + INFINITO")}
{_tbl(["verbo", "esempio"], vd, "8.6pt", ["46mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. SENZA PREPOSIZIONE</b><br><i>dovere, potere, volere, sapere</i> · <i>preferire, desiderare</i> · <i>piacere</i>: <i>Voglio dormire. · Preferisco restare. · Mi piace studiare.</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. ANCHE VERBI DI MOVIMENTO + A</b><br><i>andare, venire, uscire, tornare</i> + <b>a</b> + infinito: <i>Vado <b>a</b> studiare in biblioteca. · Vieni <b>a</b> mangiare da me?</i></div></div>
{_dont([("Ho cominciato studiare.", "cominciato <b>a</b> studiare"), ("Ho deciso a partire.", "deciso <b>di</b> partire"), ("Smetti preoccuparti!", "Smetti <b>di</b>…"),
        ("Voglio di dormire.", "Voglio dormire."), ("Mi ha aiutato di ripassare.", "aiutato <b>a</b> ripassare")])}""",
    20, """<p>Il portoghese ha preposizioni simili ma non uguali: <i>começar a</i> = <i>cominciare a</i> (facile), ma <i>decidir</i> + infinito senza preposizione → <i>decidere <b>di</b></i>; <i>parar de</i> → <i>smettere <b>di</b></i>; <i>tentar</i> → <i>provare <b>a</b></i> / <i>cercare <b>di</b></i>; <i>esquecer de</i> → <i>dimenticare <b>di</b></i>. Far creare una lista personale "a / di" e aggiungere i verbi nuovi delle prossime unità.</p>""")


def prima_di_dopo(b):
    """A2 Ponte 21: prima di + infinito / nome; dopo + nome; dopo aver / essere + participio (ricettivo)."""
    pr = [("prima di + <b>infinito</b>", "<b>Prima di partire</b> chiudo il gas. · Metto la sveglia <b>prima di andare</b> a letto."),
          ("prima di + verbo riflessivo", "<b>Prima di vestirmi</b> faccio la doccia. · <b>Prima di alzarti</b>, guarda l'ora!"),
          ("prima di + <b>nome</b>", "<b>Prima della</b> partenza · <b>prima di</b> cena · <b>prima delle</b> sette"),
          ("prima (avverbio)", "<b>Prima</b> faccio la valigia, <b>poi</b> chiamo un taxi.")]
    do = [("dopo + <b>nome</b>", "<b>Dopo</b> cena · <b>dopo il</b> lavoro · <b>dopo le</b> sei"),
          ("dopo <b>aver</b> + participio", "<b>Dopo aver chiuso</b> la porta, ho controllato tutto."),
          ("dopo <b>essere</b> + participio (-o/-a/-i/-e)", "<b>Dopo essere arrivata</b> alla stazione, Giulia ha visto…"),
          ("dopo (avverbio)", "Prima mangiamo, <b>dopo</b> andiamo al mare.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: prima di / dopo", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Con <b>prima di</b> e <b>dopo</b> mettiamo due azioni in ordine. Quando la persona è la stessa nelle due azioni, il secondo verbo non si coniuga: <b>prima di</b> + <b>infinito</b> (<i>Prima di partire, chiudo il gas</i>). Per l'azione già finita si usa <b>dopo aver / essere</b> + <b>participio passato</b>: per ora basta riconoscerlo.</div>
{_h("1. PRIMA DI")}
{_tbl(["struttura", "esempio"], pr, "8.6pt", ["46mm", None])}
{_h("2. DOPO")}
{_tbl(["struttura", "esempio"], do, "8.6pt", ["46mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. L'ORDINE DELLA FRASE</b><br>Le due parti si possono invertire: <i>Prima di partire, chiudo il gas.</i> = <i>Chiudo il gas prima di partire.</i> L'azione con <i>prima di</i> succede <b>dopo</b>!</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. AVER O ESSERE?</b><br>Come nel passato prossimo: <i>ho chiuso</i> → <b>dopo aver chiuso</b>; <i>sono arrivato</i> → <b>dopo essere arrivato</b>. <i>Aver</i> = <i>avere</i> senza la <i>-e</i>.</div></div>
{_dont([("Prima partire, chiudo il gas.", "<b>Prima di</b> partire"), ("Prima di parto…", "Prima di <b>partire</b>"), ("Prima di mi vestire.", "Prima di <b>vestirmi</b>"),
        ("Dopo di mangiare…", "<b>Dopo aver mangiato</b>… / <b>Dopo</b> pranzo…"), ("Prima de cena.", "Prima <b>di</b> cena")])}""",
    26, """<p>Il portoghese usa <i>antes de / depois de</i> + infinito per tutte e due: lo studente dice <i>dopo di mangiare</i>. In italiano <i>dopo</i> + infinito semplice è raro: si usa <b>dopo aver mangiato</b> oppure un nome (<i>dopo pranzo</i>). A questo livello pretendere <b>prima di + infinito</b> in produzione; <b>dopo aver + participio</b> solo in comprensione (lo riprenderemo al B1). Attenzione anche a <i>de</i> → <b>di</b>.</p>""")


def futuro_supposizione(b):
    """A2 Ponte 22: futuro di supposizione; se + futuro, futuro."""
    ir = [("essere", "sarò · sarai · <b>sarà</b> · saremo · sarete · <b>saranno</b>"), ("avere", "avrò · avrai · <b>avrà</b> · avremo · avrete · <b>avranno</b>"),
          ("esserci", "<b>ci sarà</b> · <b>ci saranno</b>"), ("fare · stare", "<b>farà</b>, faranno · <b>starà</b>, staranno"),
          ("venire · andare", "<b>verrà</b>, verranno · <b>andrà</b>, andranno")]
    us = [("supposizione sul <b>presente</b>", "Dov'è Bruno? <b>Sarà</b> al cinema. (= forse è al cinema)"),
          ("ora ed età", "Che ore sono? <b>Saranno</b> le nove. · Quanti anni ha? <b>Avrà</b> settant'anni."),
          ("numeri e quantità", "<b>Ci saranno</b> trentotto gradi. · <b>Saranno</b> cento persone."),
          ("futuro vero", "Domani <b>farà</b> caldo. · Il tecnico <b>arriverà</b> oggi pomeriggio.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: il futuro di supposizione · se + futuro", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Il futuro semplice (unità 07) non parla solo del futuro. Quando <b>non siamo sicuri</b> di una cosa di <b>adesso</b>, usiamo il futuro: <i>Sarà in biblioteca</i> = <i>forse è in biblioteca</i>. Si usa soprattutto con <b>essere</b> e <b>avere</b>. Con <b>se</b> + futuro facciamo ipotesi sul futuro: <i>Se pioverà, dormiremo.</i></div>
{_h("1. I FUTURI PIÙ USATI")}
{_tbl(["verbo", "futuro"], ir, "8.6pt", ["32mm", None])}
{_h("2. FUTURO O SUPPOSIZIONE?")}
{_tbl(["uso", "esempio"], us, "8.6pt", ["46mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. SE + FUTURO, FUTURO</b><br><i>Se domani <b>farà</b> caldo, <b>lavorerò</b> da casa.</i> · <i>Se il tecnico non <b>verrà</b>, <b>lavoreremo</b> da casa.</i> Nel parlato si usa anche il presente: <i>Se piove, resto a casa.</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. CERTO O NON CERTO?</b><br><i>Bruno <b>è</b> al cinema.</i> → lo so. <br><i>Bruno <b>sarà</b> al cinema.</i> → penso, ma non lo so. <br>Parole utili: <i>mah…, forse, probabilmente</i>.</div></div>
{_dont([("Deve essere in biblioteca.", "<b>Sarà</b> in biblioteca."), ("Quanti gradi saranno qui?", "Quanti gradi <b>ci saranno</b> qui?"), ("Saranno le nove ore.", "<b>Saranno le nove.</b>"),
        ("Averà caldo.", "<b>Avrà</b> caldo."), ("Esserà al cinema.", "<b>Sarà</b> al cinema.")])}""",
    29, """<p>Il portoghese esprime la supposizione con <i>deve estar</i>, <i>será que…?</i> o <i>acho que</i>. Lo studente traduce <i>deve essere</i>: non è sbagliato, ma l'italiano parlato preferisce <b>sarà</b>. Far notare il contrasto <i>Bruno è / sarà al cinema</i> con la voce (certezza / dubbio). Nelle frasi con <i>se</i> accettare anche presente + presente (<i>Se piove, resto a casa</i>), molto comune nel parlato.</p>""")


def esclamazioni_bello_buono(b):
    """A2 Ponte 23: che…!, quanto…!, com'è…!; bello / buono / grande davanti al nome."""
    es = [("<b>Che</b> + nome / aggettivo", "<b>Che</b> caldo! · <b>Che</b> bella voce! · <b>Che</b> bello! · <b>Che</b> vergogna!"),
          ("<b>Quanto / quanta / quanti / quante</b> + nome", "<b>Quanta</b> gente! · <b>Quanti</b> ricordi! · <b>Quante</b> foto!"),
          ("<b>Quanto</b> + verbo + aggettivo", "<b>Quanto</b> siete abbronzati! · <b>Quanto</b> è caro!"),
          ("<b>Com'è / come sono</b> + aggettivo", "<b>Com'è</b> brava la cantante! · <b>Come sono</b> buone!")]
    be = [("bel", "bei", "<b>bel</b> mare · <b>bei</b> ricordi (come <i>il / i</i>)"),
          ("bello", "begli", "<b>bello</b> spettacolo · <b>begli</b> occhiali (come <i>lo / gli</i>)"),
          ("bell'", "begli", "<b>bell'</b>albergo · <b>begli</b> alberghi (come <i>l' / gli</i>)"),
          ("bella / bell'", "belle", "<b>bella</b> voce · <b>bell'</b>idea · <b>belle</b> canzoni (come <i>la / l' / le</i>)")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: le esclamazioni · bello, buono, grande", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Per esprimere entusiasmo o sorpresa usiamo <b>che…!</b>, <b>quanto…!</b> e <b>com'è…!</b>. Gli aggettivi <b>bello</b> e <b>buono</b>, quando vanno <b>prima</b> del nome, cambiano forma come gli articoli: <i>un <b>bel</b> mare, un <b>buon</b> vino</i>. Dopo il nome o dopo <i>essere</i> non cambiano: <i>Il mare è <b>bello</b>.</i></div>
{_h("1. LE ESCLAMAZIONI")}
{_tbl(["struttura", "esempio"], es, "8.6pt", ["56mm", None])}
{_h("2. BELLO PRIMA DEL NOME")}
{_tbl(["singolare", "plurale", "esempio"], be, "8.6pt", ["24mm", "18mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. BUONO PRIMA DEL NOME</b><br>Come <i>un / uno / una / un'</i>: <b>buon</b> vino, <b>buon</b> appetito · <b>buono</b> stipendio · <b>buona</b> pizza · <b>buon'</b>idea. Plurale regolare: <b>buoni</b>, <b>buone</b>.</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. GRANDE</b><br>Prima del nome può diventare <b>gran</b>: <i>un <b>gran</b> caldo, una <b>gran</b> festa</i>. Prima del nome spesso cambia significato: <i>un <b>grande</b> uomo</i> (importante) / <i>un uomo <b>grande</b></i> (alto, grosso).</div></div>
{_dont([("Che bello mare!", "Che <b>bel</b> mare!"), ("Che belli occhiali!", "Che <b>begli</b> occhiali!"), ("Quanto gente!", "<b>Quanta</b> gente!"),
        ("Un buono vino.", "Un <b>buon</b> vino."), ("Che una bella voce!", "Che bella voce!")])}""",
    26, """<p>In portoghese <i>Que lindo!</i>, <i>Quanta gente!</i>, <i>Como é bonita!</i> funzionano come in italiano: la struttura è facile. Il problema sono le <b>forme</b> di <i>bello</i> (lo studente dice <i>bello mare, belli occhiali</i>) e l'articolo dopo <i>che</i> (<i>che una bella voce</i> → <b>che bella voce</b>). Trucco: <i>bello</i> si comporta come l'articolo determinativo, <i>buono</i> come l'indeterminativo. Ripassare gli articoli dell'A1 prima della tabella.</p>""")


def indefiniti(b):
    """A2 Ponte 24: qualche, qualcuno, qualcosa, ogni, ognuno, nessuno, niente."""
    ag = [("<b>qualche</b> + nome <b>singolare</b>", "= alcuni / alcune", "Porto <b>qualche</b> birra. · <b>Qualche</b> vicino è rimasto."),
          ("<b>ogni</b> + nome <b>singolare</b>", "= tutti / tutte", "<b>Ogni</b> negozio è chiuso. · <b>ogni</b> anno, <b>ogni</b> giorno"),
          ("<b>nessun / nessuna</b> + nome", "= zero", "Non c'è <b>nessun</b> bar aperto. · <b>nessuna</b> farmacia")]
    pr = [("<b>qualcuno</b>", "una persona (non so chi)", "C'è <b>qualcuno</b> nel palazzo. · <b>Qualcuno</b> vuole ancora lasagne?"),
          ("<b>qualcosa</b>", "una cosa (non so quale)", "<b>Ognuno</b> porta <b>qualcosa</b>. · Vuoi <b>qualcosa</b> da bere?"),
          ("<b>ognuno / ognuna</b>", "ogni persona", "<b>Ognuno</b> porta un piatto."),
          ("<b>nessuno</b>", "zero persone", "<b>Non</b> c'è <b>nessuno</b>. · <b>Nessuno</b> le fa così."),
          ("<b>niente</b> (= nulla)", "zero cose", "<b>Non</b> ho <b>niente</b> da fare. · <b>Non</b> c'è <b>niente</b> nel frigo.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: gli indefiniti", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Gli <b>indefiniti</b> indicano persone o cose senza dire esattamente quali o quante: <i>qualcuno, qualcosa, nessuno, niente, ogni, ognuno, qualche</i>. Alcuni vanno <b>con un nome</b> (aggettivi: <i>ogni negozio</i>), altri <b>da soli</b> (pronomi: <i>c'è qualcuno</i>).</div>
{_h("1. CON UN NOME")}
{_tbl(["forma", "significato", "esempio"], ag, "8.6pt", ["42mm", "28mm", None])}
{_h("2. DA SOLI")}
{_tbl(["forma", "significato", "esempio"], pr, "8.6pt", ["30mm", "40mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. LA DOPPIA NEGAZIONE</b><br>Dopo il verbo: <b>non</b> + verbo + <b>nessuno / niente</b>: <i>Non c'è nessuno. Non ho niente.</i> Prima del verbo: niente <i>non</i>: <i><b>Nessuno</b> le fa così. <b>Niente</b> è impossibile.</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. SEMPRE SINGOLARE</b><br><i>qualche</i> e <i>ogni</i> vogliono il nome e il verbo al <b>singolare</b>, anche se il significato è plurale: <i><b>Ogni</b> negozio <b>è</b> chiuso. <b>Qualche</b> vicino <b>è</b> rimasto.</i></div></div>
{_dont([("Porto qualche birre.", "qualche <b>birra</b>"), ("Ogni negozi sono chiusi.", "Ogni <b>negozio è</b> chiuso."), ("C'è nessuno.", "<b>Non</b> c'è nessuno."),
        ("Nessuno non le fa così.", "<b>Nessuno</b> le fa così."), ("Ho niente da fare.", "<b>Non</b> ho niente da fare.")])}""",
    26, """<p>In portoghese <i>não tem ninguém</i>, <i>não tenho nada</i> funzionano come in italiano (doppia negazione): è facile. Gli errori sono due: il <b>plurale</b> dopo <i>qualche</i> e <i>ogni</i> (pensano ad <i>alguns</i>, <i>todos</i>) e <i>non</i> davanti a <i>nessuno</i> quando sta all'inizio della frase. <i>Qualche</i> = <i>alguns/algumas</i> ma con il singolare; <i>ogni</i> = <i>cada</i>; <i>ognuno</i> = <i>cada um</i>.</p>""")


def pronomi_combinati(b):
    """A2 Ponte 25: pronomi combinati (ricettivo): me lo, te lo, glielo, ce lo, ve lo."""
    tb = [("mi → <b>me</b>", "<b>me lo</b>", "<b>me la</b>", "<b>me li</b>", "<b>me le</b>"),
          ("ti → <b>te</b>", "<b>te lo</b>", "<b>te la</b>", "<b>te li</b>", "<b>te le</b>"),
          ("gli / le / Le → <b>glie-</b>", "<b>glielo</b>", "<b>gliela</b>", "<b>glieli</b>", "<b>gliele</b>"),
          ("ci → <b>ce</b>", "<b>ce lo</b>", "<b>ce la</b>", "<b>ce li</b>", "<b>ce le</b>"),
          ("vi → <b>ve</b>", "<b>ve lo</b>", "<b>ve la</b>", "<b>ve li</b>", "<b>ve le</b>")]
    ex = [("Mi presti <b>la bici</b>?", "<b>Te la</b> presto."), ("Mi lasci <b>le chiavi</b>?", "<b>Te le</b> lascio."),
          ("Riporti <b>l'ombrellone</b> alla signora?", "Sì, <b>glielo</b> riporto domenica."), ("Mandi <b>la cartolina</b> a Marco?", "Sì, <b>gliela</b> mando."),
          ("Chi vi presta <b>la macchina</b>?", "<b>Ce la</b> presta la mamma di Marco.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: i pronomi combinati", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Quando in una frase ci sono un pronome <b>indiretto</b> (a chi?) e un pronome <b>diretto</b> (che cosa?), si mettono insieme: prima l'indiretto, poi il diretto. L'indiretto cambia la <i>i</i> in <b>e</b>: <i>mi + lo</i> → <b>me lo</b>. Con <i>gli, le</i> e <i>Le</i> si scrive tutto attaccato: <b>glielo, gliela</b>. A questo livello basta <b>capirli</b> e usare <i>me lo / te lo</i>.</div>
{_h("1. LE FORME")}
{_tbl(["indiretto", "+ lo", "+ la", "+ li", "+ le"], tb, "8.6pt", ["44mm", None, None, None, None])}
{_h("2. DOMANDA E RISPOSTA")}
{_tbl(["domanda", "risposta"], ex, "8.6pt", ["70mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. DOVE SI METTONO?</b><br>Prima del verbo: <i><b>Te lo</b> presto.</i> Con l'infinito e l'imperativo (tu) si attaccano alla fine: <i>Puoi prestar<b>melo</b>? · Prestami la bici → Presta<b>mela</b>!</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. GLIELO = A LUI, A LEI, A LEI (formale)</b><br><i>Glielo</i> va bene per tutti e tre: <i>Lo do a Marco / a Giulia / a Lei, signora</i> → <b>Glielo</b> do. Il contesto dice chi è.</div></div>
{_dont([("Mi lo presti?", "<b>Me lo</b> presti?"), ("Ti la presto.", "<b>Te la</b> presto."), ("Lo te presto.", "<b>Te lo</b> presto."),
        ("Gli lo riporto.", "<b>Glielo</b> riporto."), ("Le la mando.", "<b>Gliela</b> mando.")])}""",
    28, """<p>In portoghese parlato i pronomi combinati quasi non si usano (<i>Empresta pra mim? — Empresto.</i>), quindi lo studente li evita. A livello A2 l'obiettivo è <b>riconoscerli</b> nell'ascolto e usare in produzione solo <i>me lo / te lo / me la / te la</i> nelle frasi di ogni giorno (<i>Me lo presti? Te lo do.</i>). <i>Glielo</i> e le forme attaccate all'infinito si riprendono al B1. Accettare risposte senza pronome combinato (<i>Sì, la presto a te</i>) se il significato è chiaro, ma riformularle.</p>""")


def nomi_alterati(b):
    """A2 Ponte 26: nomi alterati (-ino, -etto, -one, -accio) e plurali irregolari (le braccia, le dita, le uova)."""
    suf = [("<b>-ino / -ina</b>", "piccolo, carino", "il tavolo → il tavol<b>ino</b> · la cucina → il cucin<b>ino</b> · poverino!"),
           ("<b>-etto / -etta</b>", "piccolo, carino", "la casa → la cas<b>etta</b> · il giardino → il giardin<b>etto</b>"),
           ("<b>-one</b>", "grande", "il letto → il lett<b>one</b> · il bicchiere → il bicchier<b>one</b> · un abbracci<b>one</b>"),
           ("<b>-accio / -accia</b>", "brutto, cattivo", "il tempo → il temp<b>accio</b> · la parola → la parol<b>accia</b>")]
    irr = [("il braccio", "le <b>braccia</b>"), ("il dito", "le <b>dita</b>"), ("il ginocchio", "le <b>ginocchia</b>"), ("il labbro", "le <b>labbra</b>"),
           ("l'osso", "le <b>ossa</b>"), ("l'uovo", "le <b>uova</b>"), ("il paio", "le <b>paia</b>"), ("il lenzuolo", "le <b>lenzuola</b>")]
    irr2 = [("la mano", "le <b>mani</b>"), ("l'uomo", "gli <b>uomini</b>"), ("il bue", "i <b>buoi</b>"), ("la radio · la foto · il caffè", "le radio · le foto · i caffè")]
    rows = [(irr[i][0], irr[i][1], irr[i + 4][0], irr[i + 4][1]) for i in range(4)]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: i nomi alterati e i plurali irregolari", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Con un <b>suffisso</b> alla fine del nome si dice com'è la cosa: piccola, grande, brutta. <i>Una casa piccola e carina</i> → <b>una casetta</b>. Alcuni nomi del corpo e poche altre parole hanno un plurale in <b>-a</b>: <i>il braccio → le braccia</i>. Questi plurali sono <b>femminili</b>.</div>
{_h("1. I SUFFISSI")}
{_tbl(["suffisso", "significa", "esempi"], suf, "8.6pt", ["30mm", "30mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>ATTENZIONE: I FALSI ALTERATI</b><br>Alcune parole sembrano alterate, ma sono parole nuove: <i>il panino</i> (non è un pane piccolo), <i>il bottone</i>, <i>il limone</i>, <i>il cerotto</i>, <i>il mattone</i>. Si usano come parole normali.</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>-ONE DIVENTA MASCHILE</b><br>Spesso un nome femminile con <i>-one</i> diventa maschile: <i>la porta → il portone</i>, <i>la finestra → il finestrone</i>. Con <i>-ino</i> a volte succede lo stesso: <i>la cucina → il cucinino</i>.</div></div>
{_h("2. PLURALI IN -A (FEMMINILI)")}
{_tbl(["singolare", "plurale", "singolare", "plurale"], rows, "8.6pt", ["38mm", None, "38mm", None])}
<p style="font-size:8.6pt;margin:1mm 0">L'aggettivo è femminile plurale: <i>le braccia <b>rosse</b>, le uova <b>fresche</b>, le dita <b>gonfie</b></i>.</p>
{_h("3. ALTRI PLURALI DA RICORDARE")}
{_tbl(["singolare", "plurale"], irr2, "8.6pt", ["70mm", None])}
{_dont([("Ho i bracci rossi.", "Ho <b>le braccia rosse</b>."), ("Mi fanno male due diti.", "Mi fanno male due <b>dita</b>."),
        ("Ho comprato sei uovi.", "Ho comprato sei <b>uova</b>."), ("Le uova sono freschi.", "Le uova sono <b>fresche</b>."), ("Ho le mane fredde.", "Ho le <b>mani</b> fredde.")])}""",
    26, """<p>In portoghese <i>-inho</i> si usa moltissimo (<i>cafezinho, rapidinho</i>); in italiano gli alterati sono meno frequenti e non si possono inventare con ogni parola: insegnare quelli più comuni come vocabolario. <i>-one</i> corrisponde a <i>-ão</i> (<i>casarão</i> → <i>casone</i>). Per i plurali in <i>-a</i> il problema è l'accordo: in portoghese <i>os braços</i> è maschile, in italiano <i>le braccia</i> è femminile.</p>""")


def discorso_indiretto_tonici(b):
    """A2 Ponte 27: discorso indiretto (dice che / ha detto che) e pronomi tonici."""
    ind = [("«Vado a Milano.»", "Dice che <b>va</b> a Milano.", "Ha detto che <b>va</b> a Milano."),
           ("«Sono stanca.»", "Dice che <b>è</b> stanca.", "Ha detto che <b>è</b> stanca."),
           ("«Ho studiato.»", "Dice che <b>ha studiato</b>.", "Ha detto che <b>ha studiato</b>."),
           ("«Il mio esame è giovedì.»", "Dice che <b>il suo</b> esame è giovedì.", "Ha detto che <b>il suo</b> esame è giovedì.")]
    ton = [("io", "mi", "<b>me</b>", "per <b>me</b> · con <b>me</b>"), ("tu", "ti", "<b>te</b>", "per <b>te</b> · secondo <b>te</b>"),
           ("lui / lei / Lei", "lo, gli / la, le / La, Le", "<b>lui / lei / Lei</b>", "con <b>lui</b> · per <b>Lei</b>"),
           ("noi", "ci", "<b>noi</b>", "da <b>noi</b>"), ("voi", "vi", "<b>voi</b>", "senza <b>voi</b>"), ("loro", "li, le / gli", "<b>loro</b>", "a <b>loro</b>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: il discorso indiretto e i pronomi tonici", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Con il <b>discorso indiretto</b> riportiamo le parole di un'altra persona: <i>«Vado a Milano.»</i> → <i>Il signor Neri <b>dice che</b> va a Milano.</i> I <b>pronomi tonici</b> (<i>me, te, lui, lei…</i>) si usano dopo una preposizione (<i>per te, con me</i>) o quando vogliamo dare importanza alla persona.</div>
{_h("1. DICE CHE / HA DETTO CHE")}
{_tbl(["parole dirette", "dice che…", "ha detto che…"], ind, "8.6pt", ["40mm", None, None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>CHE COSA CAMBIA?</b><br>Cambia la <b>persona</b>: <i>vado → va, sono → è, ho → ha</i>. Cambiano i possessivi: <i>mio → suo</i>. Dopo <i>dice che</i> il tempo resta uguale. <i>Che</i> non si toglie mai.</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>PER INIZIARE UNA NOTIZIA</b><br><i><b>Lo sai che</b> il signor Neri va via?</i> · <i>Hai sentito che…?</i> · <i><b>Chi ti ha detto che</b>…?</i> · <i>Mi ha detto che…</i> · <i>Si dice che…</i></div></div>
{_h("2. I PRONOMI TONICI")}
{_tbl(["soggetto", "atono", "tonico", "esempi"], ton, "8.6pt", ["28mm", "40mm", "30mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. QUANDO SI USANO?</b><br>Dopo le preposizioni: <i>per me, con te, da lui, senza di loro</i>. Per dare enfasi: <i>Mi cerchi?</i> → <i>Cerchi <b>me</b>?</i> (proprio me). Per dire un'opinione: <b>secondo me</b>, <b>per me</b>.</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. ATTENZIONE</b><br>Dopo <i>anche</i> come soggetto: <i><b>Anch'io</b> vado</i> (soggetto) ma <i>Inviti <b>anche me</b>?</i> (oggetto). <i>Da me</i> = a casa mia: <i>Ceniamo <b>da me</b>?</i></div></div>
{_dont([("Vieni con io?", "Vieni con <b>me</b>?"), ("È per tu.", "È per <b>te</b>."), ("Secondo io, sì.", "Secondo <b>me</b>, sì."),
        ("Ha detto vado a Milano.", "Ha detto <b>che va</b> a Milano."), ("Lei dice che lei è stanca.", "Dice che è stanca.")])}""",
    26, """<p>In portoghese brasiliano si dice <i>com eu, pra eu, entre eu e você</i>: lo studente trasferisce l'errore (<i>con io, per tu</i>). Ricordare: dopo ogni preposizione → <b>me, te</b>. Nel discorso indiretto il brasiliano spesso omette <i>che</i> (<i>disse que</i> → ok, ma all'orale <i>ele falou: vou embora</i>): pretendere <i>ha detto che</i>. A livello A2 solo <i>dice che / ha detto che</i> con il tempo che non cambia; la concordanza dei tempi (<i>ha detto che andava</i>) è B1.</p>""")


def congiuntivo_volonta(b):
    """A2 Ponte 29: congiuntivo presente (2): volere che, è importante che, bisogna che, sono contento che, ho paura che; forme irregolari."""
    trig = [("<b>voglio che · preferisco che</b>", "volontà", "<i>Voglio che tutto <b>sia</b> perfetto.</i>"),
            ("<b>è importante che · bisogna che · è meglio che</b>", "necessità", "<i>Bisogna che il tecnico <b>venga</b> domattina.</i>"),
            ("<b>sono contento/a che · mi dispiace che</b>", "emozione", "<i>Sono contenta che <b>abbiate</b> messo tante panchine.</i>"),
            ("<b>ho paura che · spero che</b>", "paura, speranza", "<i>Ho paura che <b>piova</b>. · Spero che non <b>facciano</b> rumore.</i>")]
    irr = [("andare", "<b>vada</b>", "<b>vadano</b>"), ("fare", "<b>faccia</b>", "<b>facciano</b>"), ("venire", "<b>venga</b>", "<b>vengano</b>"),
           ("potere", "<b>possa</b>", "<b>possano</b>"), ("dovere", "<b>debba</b>", "<b>debbano</b>"), ("dire", "<b>dica</b>", "<b>dicano</b>"),
           ("stare · dare", "<b>stia · dia</b>", "<b>stiano · diano</b>"), ("sapere · uscire", "<b>sappia · esca</b>", "<b>sappiano · escano</b>")]
    rows = [(irr[i][0], irr[i][1], irr[i][2], irr[i + 4][0], irr[i + 4][1], irr[i + 4][2]) for i in range(4)]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: il congiuntivo presente (2)", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Nell'unità 09 hai usato il congiuntivo dopo <i>penso che, credo che, spero che</i>. Il congiuntivo si usa anche quando <b>vogliamo</b> qualcosa da un'altra persona, quando una cosa è <b>necessaria</b> e quando parliamo di <b>emozioni</b> e <b>paure</b>: <i>Voglio che tu <b>venga</b>. · È importante che <b>sia</b> pronto. · Ho paura che <b>piova</b>.</i></div>
{_h("1. DOPO QUALI ESPRESSIONI?")}
{_tbl(["espressione + che", "per…", "esempio"], trig, "8.6pt", ["58mm", "26mm", None])}
{_h("2. LE FORME IRREGOLARI (io, tu, lui, lei, Lei · loro)")}
{_tbl(["verbo", "io / tu / lui", "loro", "verbo", "io / tu / lui", "loro"], rows, "8.6pt", ["22mm", None, None, "22mm", None, None])}
<p class="small" style="margin:.6mm 0">Regolari: <i>-are → -i</i> (<i>che parli</i>), <i>-ere / -ire → -a</i> (<i>che prenda, che dorma</i>). <i>Essere → sia, siano</i> · <i>avere → abbia, abbiano</i> · <i>noi → -iamo, voi → -iate</i> (<i>che siate, che abbiate</i>).</p>
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>3. STESSO SOGGETTO: INFINITO</b><br><i>Voglio <b>andare</b>.</i> (io voglio, io vado) · <i>Voglio che <b>tu vada</b>.</i> (io voglio, tu vai) · <i>Sono contenta <b>di essere</b> qui.</i> · <i>Ho paura <b>di sbagliare</b>.</i> · <i>È importante <b>arrivare</b> presto.</i> (per tutti)</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. FATTO SICURO: INDICATIVO</b><br><i>So che <b>viene</b>. · Sono sicuro che <b>è</b> pronto. · È vero che <b>piove</b>. · Secondo me <b>è</b> bellissimo.</i> Il congiuntivo dice un desiderio, un'opinione o un'emozione; l'indicativo dice un fatto.</div></div>
{_dont([("Voglio che vieni.", "Voglio che <b>venga</b>."), ("È importante che sei puntuale.", "È importante che tu <b>sia</b> puntuale."),
        ("Voglio che io vado.", "Voglio <b>andare</b>."), ("Sono contenta che siete qui.", "Sono contenta che <b>siate</b> qui."), ("So che venga.", "So che <b>viene</b>.")])}""",
    27, """<p>In portoghese dopo <i>quero que, é importante que, tenho medo que</i> si usa il <i>subjuntivo</i> (<i>quero que você venha</i>): qui il portoghese aiuta! Far notare il parallelo <i>venha → venga, faça → faccia, seja → sia, tenha → abbia</i>. Il vero problema è la forma: lo studente dice <i>vieni, sei</i> perché le forme del presente sono più frequenti. A livello A2 basta il congiuntivo presente; il passato (<i>che abbia fatto</i>) al B1.</p>""")


def consigli_imperativo_pronomi(b):
    """A2 Ponte 30: dare consigli (ti consiglio di, dovresti, perché non…?, è meglio) e l'imperativo con i pronomi (ripasso in uso)."""
    cs = [("<b>Ti consiglio di</b> + infinito", "<i>Ti consiglio di andarci presto.</i>"), ("<b>Dovresti</b> + infinito (condizionale)", "<i>Dovresti fare l'abbonamento.</i>"),
          ("<b>Perché non</b> + presente?", "<i>Perché non vieni con noi sabato?</i>"), ("<b>È meglio</b> + infinito", "<i>È meglio comprare una bici usata.</i>"),
          ("<b>Imperativo</b> (più diretto)", "<i>Vai all'ufficio abbonamenti!</i>")]
    dv = [("io", "dovrei"), ("tu", "<b>dovresti</b>"), ("lui / lei / Lei", "<b>dovrebbe</b>"), ("noi", "dovremmo"), ("voi", "<b>dovreste</b>"), ("loro", "dovrebbero")]
    dvr = [(dv[i][0], dv[i][1], dv[i + 3][0], dv[i + 3][1]) for i in range(3)]
    ip = [("tu: <b>attaccato</b> alla fine", "Compra<b>la</b>! · Chiedi<b>lo</b>! · Porta<b>la</b> con te! · Iscriviti!"),
          ("tu, negativo: prima o attaccato", "Non <b>la</b> comprare! = Non comprar<b>la</b>! · Non preoccupar<b>ti</b>!"),
          ("noi / voi: attaccato", "Chiamiamo<b>lo</b>! · Ditemi tutto!"),
          ("Lei: <b>prima</b> del verbo", "<b>La</b> compri! · <b>Me lo</b> dica! · Non <b>si</b> preoccupi!")]
    mono = [("di' → <b>dimmi</b>", "da' → <b>dammi</b>", "fa' → <b>fammi</b>", "va' → <b>vacci</b>", "sta' → <b>stammi</b> bene")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: dare consigli e l'imperativo con i pronomi", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Per dare un consiglio in italiano ci sono molti modi, dal più gentile al più diretto: <i>ti consiglio di…, dovresti…, perché non…?, è meglio…</i> e l'imperativo. Con l'imperativo i pronomi (<i>lo, la, mi, ci, ti</i>) si <b>attaccano</b> al verbo: <i>Comprala! Dimmi!</i> (unità 04 e 08).</div>
{_h("1. I CONSIGLI")}
{_tbl(["struttura", "esempio"], cs, "8.6pt", ["62mm", None])}
<div class="two"><div>{_h("2. DOVERE AL CONDIZIONALE")}
{_tbl(["persona", "dovere", "persona", "dovere"], dvr, "8.6pt", ["24mm", None, "24mm", None])}</div>
<div>{_h("ATTENZIONE: NIENTE DI")}
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><i>Ti consiglio <b>di</b> andare.</i> (con <i>di</i>)<br><i>Dovresti andare.</i> (senza <i>di</i>)<br><i>È meglio andare.</i> (senza <i>di</i>)<br><i>Ti consiglio <b>il</b> mercatino.</i> (+ nome)</div></div></div>
{_h("3. L'IMPERATIVO CON I PRONOMI")}
{_tbl(["persona", "esempi"], ip, "8.6pt", ["52mm", None])}
{_h("4. DI', DA', FA', VA', STA' + PRONOME: LA CONSONANTE RADDOPPIA")}
{_tbl(["dire", "dare", "fare", "andare", "stare"], mono, "8.6pt")}
{_dont([("Ti consiglio andare presto.", "Ti consiglio <b>di</b> andare presto."), ("Dovresti di iscriverti.", "Dovresti iscriverti."),
        ("La compra! (a un amico)", "<b>Comprala!</b>"), ("Dami il tuo numero.", "<b>Dammi</b> il tuo numero."), ("Non ti preoccupi! (a un amico)", "Non preoccupar<b>ti</b>!")])}""",
    26, """<p>In portoghese brasiliano si dice <i>me dá, me fala, compra ela</i>: il pronome va prima o resta separato. In italiano con <i>tu</i> il pronome si <b>attacca</b> alla fine (<i>dammi, dimmi, comprala</i>) e con i monosillabi la consonante raddoppia. <i>Non ti preoccupi</i> è la forma di <i>Lei</i> sbagliata: con un amico <i>non preoccuparti</i>. <i>Dovresti</i> è il condizionale dell'unità 05: è il modo più naturale e gentile per un consiglio.</p>""")


def ordinali_secoli(b):
    """A2 Ponte 31: numeri ordinali (tutti), numeri romani, secoli (il Duecento = il XIII secolo), anni (nel 1088, negli anni Sessanta)."""
    o1 = [("1°", "primo"), ("2°", "secondo"), ("3°", "terzo"), ("4°", "quarto"), ("5°", "quinto"),
          ("6°", "sesto"), ("7°", "settimo"), ("8°", "ottavo"), ("9°", "nono"), ("10°", "decimo")]
    o1r = [(o1[i][0], o1[i][1], o1[i + 5][0], o1[i + 5][1]) for i in range(5)]
    o2 = [("11°", "undic<b>esimo</b>", "undici → undic-"), ("20°", "vent<b>esimo</b>", "venti → vent-"), ("23°", "ventitre<b>esimo</b>", "ventitré: la <i>e</i> resta"),
          ("100°", "cent<b>esimo</b>", "cento → cent-"), ("1000°", "mill<b>esimo</b>", "mille → mill-")]
    sc = [("XI secolo", "1001–1100", "il Mille / l'undicesimo secolo"), ("XII secolo", "1101–1200", "il Millecento"),
          ("XIII secolo", "1201–1300", "il <b>Duecento</b>"), ("XIV secolo", "1301–1400", "il <b>Trecento</b>"),
          ("XVI secolo", "1501–1600", "il <b>Cinquecento</b>"), ("XX secolo", "1901–2000", "il <b>Novecento</b>"), ("XXI secolo", "2001–2100", "il Duemila")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: i numeri ordinali e i secoli", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Gli <b>ordinali</b> dicono la posizione (<i>il terzo capitolo, la seconda volta</i>) e sono aggettivi: si accordano con il nome. Per i <b>secoli</b> l'italiano ha due modi: <i>il XIII secolo</i> (il tredicesimo secolo) e <i>il Duecento</i> (gli anni 1200).</div>
<div class="two"><div>{_h("1. DA 1 A 10")}
{_tbl(["", "ordinale", "", "ordinale"], o1r, "8.6pt", ["12mm", None, "12mm", None])}</div>
<div>{_h("2. DA 11: NUMERO + -ESIMO")}
{_tbl(["", "ordinale", "come?"], o2, "8.6pt", ["12mm", "30mm", None])}</div></div>
<p class="small" style="margin:.6mm 0">Si accordano: <i>il prim<b>o</b> giorno, la prim<b>a</b> volta, i prim<b>i</b> giorni, le prim<b>e</b> lezioni</i>. Si scrivono anche con i numeri romani: <i>Giovanni XXIII</i> (ventitreesimo), <i>Luigi XIV</i> (quattordicesimo), <i>il XX secolo</i>.</p>
{_h("3. I SECOLI")}
{_tbl(["numero romano", "anni", "nome"], sc, "8.6pt", ["32mm", "28mm", None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>ATTENZIONE</b><br>Il <i>Duecento</i> è il <b>XIII</b> secolo, non il XII: si conta come in portoghese (<i>século XIII</i> = anos 1200). <i>Il Trecento, il Quattrocento</i> si scrivono con la maiuscola.</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>4. GLI ANNI</b><br><b>nel</b> 1088 · <b>nel</b> 2021 · <b>dal</b> 1563 <b>al</b> 1803 · <b>negli anni</b> Sessanta · <b>alla fine del</b> Novecento · <b>all'inizio del</b> secolo. Si leggono come numeri: <i>millenovecentonovanta</i>.</div></div>
{_dont([("La terzo volta.", "La <b>terza</b> volta."), ("Il secolo tredici.", "Il <b>tredicesimo</b> secolo."), ("In 1088.", "<b>Nel</b> 1088."),
        ("Il XIII secolo = il Milletrecento.", "Il XIII secolo = il <b>Duecento</b>."), ("Il undicesimo capitolo.", "L'<b>undicesimo</b> capitolo.")])}""",
    26, """<p>Il portoghese ha <i>décimo primeiro, vigésimo</i>; l'italiano è più regolare: da 11 in poi basta <i>-esimo</i>. La difficoltà vera sono i nomi dei secoli (<i>il Duecento</i> = XIII): far fare sempre la conversione con gli anni. In portoghese si dice <i>em 1088</i>, in italiano <b>nel</b> 1088 (articolo + preposizione). Accento: undic<b>è</b>simo, vent<b>è</b>simo.</p>""")


def farcela_metterci(b):
    """A2 Ponte 32: farcela (ce la faccio, ce l'ho fatta), metterci / volerci (tempo), ce n'è / ce ne sono (ripasso)."""
    fc = [("io", "ce la <b>faccio</b>", "ce l'<b>ho</b> fatta"), ("tu", "ce la <b>fai</b>", "ce l'<b>hai</b> fatta"), ("lui / lei / Lei", "ce la <b>fa</b>", "ce l'<b>ha</b> fatta"),
          ("noi", "ce la <b>facciamo</b>", "ce l'<b>abbiamo</b> fatta"), ("voi", "ce la <b>fate</b>", "ce l'<b>avete</b> fatta"), ("loro", "ce la <b>fanno</b>", "ce l'<b>hanno</b> fatta")]
    tm = [("<b>metterci</b> (soggetto = la persona)", "<i>Quanto <b>ci metti</b> a fare dieci km? — <b>Ci metto</b> cinquanta minuti.</i>", "<i>Ci <b>ho messo</b> tre ore.</i>"),
          ("<b>volerci</b> (soggetto = il tempo)", "<i><b>Ci vuole</b> un'ora. · <b>Ci vogliono</b> quattro ore.</i>", "<i><b>Ci sono volute</b> quattro ore.</i>")]
    ce = [("C'è ancora pasta?", "Sì, <b>ce n'è</b> un piatto.", "No, <b>non ce n'è</b> più."), ("Ci sono ancora panini?", "Sì, <b>ce ne sono</b> tre.", "No, <b>non ce ne sono</b> più.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: farcela, metterci e ce n'è", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Alcuni verbi molto usati hanno dentro dei pronomi fissi. <b>Farcela</b> (= riuscire, avere la forza) e <b>metterci</b> (= usare un certo tempo) sono due di questi: <i>Ce la faccio! · Ci metto un'ora.</i> Il pronome non si riferisce a niente di preciso: è parte del verbo.</div>
{_h("1. FARCELA: PRESENTE E PASSATO PROSSIMO")}
{_tbl(["persona", "presente", "passato prossimo"], fc, "8.6pt", ["34mm", None, None])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>ATTENZIONE</b><br>Nel passato prossimo: <i>ce l'ho fatt<b>a</b></i> (con la <b>a</b>, perché <i>la</i>). <b>Non ce la faccio più</b> = sono stanchissimo. <b>Ce la puoi fare!</b> = incoraggiamento. Con l'infinito: <i>Ce la fai <b>a</b> finire?</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>RIUSCIRE O FARCELA?</b><br><i>Riesco a correre 42 km</i> = <i>ce la faccio a correre 42 km</i>. <i>Farcela</i> è più colloquiale e si usa molto da solo: <i>Ce la fai? — Sì, ce la faccio!</i></div></div>
{_h("2. IL TEMPO: METTERCI E VOLERCI")}
{_tbl(["verbo", "presente", "passato"], tm, "8.6pt", ["46mm", None, "36mm"])}
{_h("3. CE N'È, CE NE SONO (UNITÀ 14)")}
{_tbl(["domanda", "sì", "no"], ce, "8.6pt", ["40mm", None, None])}
{_dont([("Ce lo faccio.", "Ce <b>la</b> faccio."), ("Ce l'ho fatto!", "Ce l'ho fatt<b>a</b>!"), ("Ho messo tre ore.", "<b>Ci</b> ho messo tre ore."),
        ("Ci vuole tre ore.", "Ci <b>vogliono</b> tre ore."), ("Ci sono ne due.", "<b>Ce ne sono</b> due.")])}""",
    26, """<p>In portoghese si dice <i>consegui! / dá pra fazer?</i> e <i>demorei três horas / leva uma hora</i>: lo studente traduce con <i>ho demorato</i> (non esiste con questo senso) o <i>prende un'ora</i>. Insegnare le frasi come blocchi fissi: <i>ce la faccio, non ce la faccio più, ce l'ho fatta, quanto ci metti?, ci vuole un'ora</i>. La differenza <i>metterci / volerci</i> è utile ma non va forzata: basta che lo studente la capisca.</p>""")


def reciproci_mentre(b):
    """A2 Ponte 33: verbi reciproci (ci siamo conosciuti, si sono sposati); mentre + imperfetto, quando + passato prossimo."""
    vr = [("conoscersi", "Ci <b>siamo conosciuti</b> a una festa."), ("vedersi · rivedersi", "Ci <b>vediamo</b> ogni giorno. · Ci <b>siamo rivisti</b>."),
          ("scriversi · telefonarsi", "Ci <b>scrivevamo</b> e ci <b>telefonavamo</b>."), ("mettersi insieme · lasciarsi", "Si <b>sono messi</b> insieme. · Si <b>sono lasciati</b>."),
          ("sposarsi · innamorarsi", "Si <b>sono sposati</b> dopo sei mesi. · Si <b>sono innamorati</b>."), ("aiutarsi · salutarsi · parlarsi", "Ci <b>aiutiamo</b>. · Vi <b>siete parlati</b>?")]
    pr = [("noi", "<b>ci</b> vediamo", "<b>ci</b> siamo visti/e"), ("voi", "<b>vi</b> vedete", "<b>vi</b> siete visti/e"), ("loro", "<b>si</b> vedono", "<b>si</b> sono visti/e")]
    mq = [("<b>mentre</b> + imperfetto", "un'azione in corso, lo sfondo", "<i>Mentre tutti <b>ballavano</b>, io <b>parlavo</b>.</i> (due azioni lunghe)"),
          ("<b>quando</b> + passato prossimo", "un'azione breve, un fatto", "<i><b>Quando</b> la musica <b>è finita</b>, lui le <b>ha chiesto</b> il numero.</i>"),
          ("<b>mentre</b> + imperfetto, passato prossimo", "un'azione interrompe l'altra", "<i>Mentre <b>aspettavo</b> l'autobus, un ragazzo mi <b>ha sorriso</b>.</i>")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: i verbi reciproci e mentre / quando", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Un verbo <b>reciproco</b> dice un'azione che due o più persone fanno <b>l'una con l'altra</b>: <i>Bruno conosce Chiara + Chiara conosce Bruno</i> → <b>Si sono conosciuti</b>. Ha la stessa forma dei verbi riflessivi, ma solo al plurale (<i>ci, vi, si</i>). Per raccontare: <b>mentre</b> + imperfetto (lo sfondo) e <b>quando</b> + passato prossimo (il fatto).</div>
{_h("1. I VERBI RECIPROCI PIÙ USATI")}
{_tbl(["verbo", "esempio"], vr, "8.6pt", ["52mm", None])}
<div class="two"><div>{_h("2. LA FORMA")}
{_tbl(["persona", "presente", "passato prossimo"], pr, "8.6pt", ["18mm", None, None])}</div>
<div><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt;margin-top:4mm"><b>ATTENZIONE</b><br>Al passato prossimo: sempre <b>essere</b> e il participio si accorda: <i>ci siamo conosciut<b>i</b></i> (un ragazzo e una ragazza), <i>ci siamo conosciut<b>e</b></i> (due ragazze). <i>Sposare</i> qualcuno, ma <i>sposarsi con</i> qualcuno; <i>innamorarsi <b>di</b></i> qualcuno.</div></div></div>
{_h("3. MENTRE E QUANDO")}
{_tbl(["struttura", "per…", "esempio"], mq, "8.6pt", ["52mm", "40mm", None])}
{_dont([("Abbiamo conosciuto a una festa.", "<b>Ci siamo conosciuti</b> a una festa."), ("Si sono sposato.", "Si sono sposat<b>i</b>."),
        ("Mentre ho aspettato, un ragazzo sorrideva.", "Mentre <b>aspettavo</b>, un ragazzo <b>ha sorriso</b>."), ("Si è innamorata con lui.", "Si è innamorata <b>di</b> lui."),
        ("Ci vediamo? Sì, ci vediamo ieri.", "Sì, <b>ci siamo visti</b> ieri.")])}""",
    26, """<p>In portoghese <i>nos conhecemos, se casaram</i> funzionano come in italiano, ma lo studente usa <i>avere</i> al passato (<i>abbiamo conosciuto</i>) perché in portoghese l'ausiliare non cambia. <i>Enquanto</i> + <i>imperfeito</i> è uguale a <i>mentre</i> + imperfetto: far notare il parallelo. Errore frequente: <i>casar com</i> → <i>sposare con</i> (corretto: <i>sposare qualcuno</i> o <i>sposarsi con</i>) e <i>apaixonar-se por</i> → <i>innamorarsi di</i>.</p>""")


def opinioni_ne(b):
    """A2 Ponte 34: chiedere e dare opinioni; penso di + infinito / penso che + congiuntivo; accordo e disaccordo; ne = di questo, ci = a questo."""
    ch_ = [("<b>Che ne pensi?</b> · Che ne dici?", "(ne = di questo)"), ("<b>Secondo te?</b> · Per te?", "(informale)"), ("<b>Lei che ne pensa?</b>", "(formale)"), ("<b>Sei d'accordo?</b>", "(sì o no)")]
    op = [("<b>secondo me / per me</b> + indicativo", "<i>Secondo me <b>è</b> rischioso.</i>"),
          ("<b>penso che / credo che</b> + congiuntivo (unità 09)", "<i>Penso che <b>sia</b> un'idea fantastica.</i>"),
          ("<b>penso di</b> + infinito (stesso soggetto)", "<i>Penso <b>di avere</b> ragione.</i> (io penso, io ho ragione)"),
          ("<b>penso di</b> + infinito = intenzione", "<i>Penso <b>di fare</b> un venerdì brasiliano.</i> (= ho intenzione di)")]
    ad = [("<b>Sono d'accordo</b> (con te / con Lei) · Concordo.", "<b>Non sono d'accordo</b> (con te)."), ("<b>Hai ragione.</b> · Esatto! · Certo!", "<b>Non è vero.</b> · Io la penso diversamente."),
          ("<b>Anch'io.</b> · Neanch'io.", "<b>Mah, non sono sicuro/a.</b> · Dipende.")]
    nc = [("<b>ne</b> = di questo / di + cosa", "Che <b>ne</b> pensi? (pensare <b>di</b>) · <b>Ne</b> parliamo domani. (parlare <b>di</b>) · Non <b>ne</b> so niente. (sapere <b>di</b>)"),
          ("<b>ne</b> = una parte (unità 14)", "<b>Ne</b> prendo solo un po'."),
          ("<b>ci</b> = a questo", "<b>Ci</b> penso. (pensare <b>a</b> = riflettere) · Pensi all'esame? — Sì, <b>ci</b> penso sempre.")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: le opinioni e il pronome ne", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Per chiedere un'opinione l'italiano usa <b>Che ne pensi?</b>: <i>ne</i> sostituisce <i>di questo</i> (<i>pensare di</i> qualcosa). Per rispondere: <i>secondo me</i> + indicativo, <i>penso che</i> + congiuntivo, <i>penso di</i> + infinito. Poi si dice se si è d'accordo o no.</div>
<div class="two"><div>{_h("1. CHIEDERE UN'OPINIONE")}
{_tbl(["domanda", ""], ch_, "8.6pt", [None, "26mm"])}</div>
<div>{_h("3. ACCORDO E DISACCORDO")}
{_tbl(["sono d'accordo", "non sono d'accordo"], ad, "8.4pt")}</div></div>
{_h("2. DARE UN'OPINIONE")}
{_tbl(["struttura", "esempio"], op, "8.6pt", ["70mm", None])}
{_h("4. NE E CI")}
{_tbl(["pronome", "esempi"], nc, "8.6pt", ["46mm", None])}
{_dont([("Penso che è una buona idea.", "Penso che <b>sia</b> una buona idea."), ("Penso che faccio una festa.", "Penso <b>di fare</b> una festa."),
        ("Sono d'accordo a te.", "Sono d'accordo <b>con</b> te."), ("Che pensi di questo?", "Che <b>ne</b> pensi?"), ("Vieni? — Non so, ne penso.", "Non so, <b>ci</b> penso.")])}""",
    26, """<p>Il brasiliano dice <i>o que você acha disso?</i> e traduce <i>che pensi di questo?</i> (comprensibile, ma poco naturale): insegnare il blocco <i>Che ne pensi?</i>. <i>Acho que é</i> → <i>penso che è</i>: ricordare il congiuntivo (unità 09) o usare <i>secondo me</i> + indicativo. <i>Pensar em</i> = <i>pensare a</i> → <i>ci penso</i>; <i>pensar de</i> (opinione) → <i>ne</i>. <i>Concordo</i> esiste anche in italiano ed è corretto.</p>""")


def tempi_a2(b):
    """A2 Ponte 35: tutti i tempi dell'A2 insieme; da / fa / tra; da + presente."""
    tt = [("presente", "oggi, abitudini", "<i>Adesso <b>parlo</b> italiano tutti i giorni.</i>", "A1"),
          ("passato prossimo", "fatti finiti", "<i><b>Sono andata</b> a Venezia con Giulia.</i>", "A1 · A2 11"),
          ("imperfetto", "com'era, sfondo, abitudini passate", "<i>Non <b>conoscevo</b> nessuno.</i>", "A2 02–03"),
          ("futuro", "progetti, previsioni, supposizioni", "<i>La <b>proverò</b> a casa. · <b>Sarà</b> stanco.</i>", "A2 07 · 22"),
          ("condizionale", "desideri, consigli gentili", "<i><b>Vorrei</b> visitare la Sicilia. · <b>Dovremmo</b>…</i>", "A2 05 · 30"),
          ("congiuntivo", "opinioni, speranze, volontà", "<i>Spero che <b>vengano</b>. · Penso che <b>sia</b>…</i>", "A2 09 · 29"),
          ("imperativo", "istruzioni, consigli diretti", "<i><b>Parlagli</b> tu! · <b>Non preoccuparti!</b></i>", "A2 04 · 08 · 30")]
    tm = [("<b>fa</b> (passato)", "<i>Sono arrivata due anni <b>fa</b>.</i>", "(há dois anos, atrás)"),
          ("<b>da</b> + presente (ancora vero)", "<i>Abito a Bologna <b>da</b> due anni.</i>", "(moro aqui há dois anos)"),
          ("<b>tra / fra</b> (futuro)", "<i><b>Tra</b> un mese è Natale.</i>", "(daqui a um mês)"),
          ("<b>per</b> (durata finita)", "<i>Ho abitato a Recife <b>per</b> vent'anni.</i>", "(durante, e adesso no)")]
    b.page(f"""{b.sec("+", "Riferimento grammaticale: tutti i tempi dell'A2", "")}
<div class="box" style="margin-top:0"><h4>CHE COS'È?</h4>Alla fine dell'A2 sai raccontare il <b>passato</b> (che cosa è successo e com'era), parlare del <b>presente</b>, fare <b>progetti</b>, esprimere <b>desideri</b> e <b>speranze</b>. Questa pagina mette tutto insieme. Per ogni tempo trovi l'unità dove l'hai studiato.</div>
{_h("1. I TEMPI E I MODI DELL'A2")}
{_tbl(["tempo", "per…", "esempio", "unità"], tt, "8.4pt", ["28mm", "42mm", None, "24mm"])}
{_h("2. FA, DA, TRA, PER")}
{_tbl(["parola", "esempio", "in portoghese"], tm, "8.6pt", ["46mm", None, "40mm"])}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>ATTENZIONE: DA + PRESENTE</b><br>Se una cosa è cominciata nel passato ed è <b>ancora vera</b>, si usa il <b>presente</b>: <i>Studio italiano <b>da</b> un anno</i> (e studio ancora). <i>Ho studiato italiano <b>per</b> un anno</i> = adesso non studio più.</div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt"><b>RACCONTARE IN TRE TEMPI</b><br><b>Prima</b> (imperfetto): <i>non capivo niente.</i><br><b>Poi</b> (passato prossimo): <i>ho conosciuto Giulia, ho cominciato a…</i><br><b>Adesso</b> (presente) e <b>in futuro</b> (futuro, condizionale): <i>parlo… vorrei…</i></div></div>
{_dont([("Abito qui per due anni.", "Abito qui <b>da</b> due anni."), ("Ho abitato qui da due anni.", "<b>Abito</b> qui da due anni."), ("Sono arrivata da due anni.", "Sono arrivata due anni <b>fa</b>."),
        ("Quando sono arrivata, ha piovuto.", "Quando sono arrivata, <b>pioveva</b>."), ("Spero che vengono.", "Spero che <b>vengano</b>.")])}""",
    26, """<p>L'errore più importante di questa pagina: il portoghese <i>moro aqui há dois anos</i> diventa <i>ho abitato qui da due anni</i> o <i>abito qui per due anni</i>. In italiano: <b>da</b> + <b>presente</b>. <i>Há dois anos</i> (= tempo fa) è <i>due anni <b>fa</b></i>. Usare questa pagina come ripasso: per ogni riga della tabella 1 chiedere allo studente una frase sulla sua vita.</p>""")
