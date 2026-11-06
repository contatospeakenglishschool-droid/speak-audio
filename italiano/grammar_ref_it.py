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
