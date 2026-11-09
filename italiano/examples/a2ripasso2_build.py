# Speak! Ponte A2 - Ripasso 2 (Unità 11-18), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Ponte"
setup(band="A2 · RIPASSO 2", audio_json=os.path.join(HERE, "audio_it-a2-ripasso-2.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la mostra", "Unità 11"), ("B", "la gondola", "Unità 12"), ("C", "socievole", "Unità 13"), ("D", "le fragole", "Unità 14"),
          ("E", "l'aspirapolvere", "Unità 15"), ("F", "la panchina", "Unità 16"), ("G", "il cappuccino", "Unità 17"), ("H", "la e-mail", "Unità 18")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-ripasso-2"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S23 = lines("R2.1 Conversazione"), lines("R2.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R2.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: cover + photo memory
    cover = cover_html(T, "LIVELLO A2 · RIPASSO 2", "Ripasso 2", "Unità 11–18 · tempo libero · viaggi · carattere · spesa · casa · città · regole · mail",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 11–18 dell'A2"),
                        ("LINGUA", "l'ho vista · volevo / ho dovuto · più… di, -issimo · ne, ci · sto facendo, sto per · che, cui · si impersonale · però, quindi, comunque"),
                        ("PRONUNCIA", "dettato di frasi · al mercato e al telefono")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la parola.", "5 min")}
<div class="bank">l'aspirapolvere · il cappuccino · la e-mail · le fragole · la gondola · la mostra · la panchina · socievole</div>
{photo_grid(T, PHOTOS)}""",
    30, """<p>Le foto A–H vengono dalle unità 11–18, in ordine. Chiedere una frase con la grammatica dell'unità: <i>La mostra? L'ho vista ad aprile (11). Volevo fare un giro in gondola, ma costava troppo (12). Sono socievolissimo (13). Le fragole? Ne prendo mezzo chilo (14). Sto passando l'aspirapolvere (15). È una panchina su cui riposo (16). Il cappuccino si beve la mattina (17). Ho scritto una mail, però non mi hanno risposto (18).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>11–18</td><td>1</td></tr>
<tr><td>2 Ascolto: le novità della primavera</td><td>10 min</td><td>11–18</td><td>2</td></tr>
<tr><td>3 Grammatica: pronomi + passato, modali, paragoni, ne e ci</td><td>10 min</td><td>11–14</td><td>3</td></tr>
<tr><td>4 Grammatica: stare + gerundio, che / cui, si, connettivi</td><td>10 min</td><td>15–18</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>11–18</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>8 min</td><td>11–18</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>11–18</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 4 dell'unità.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Aprile: Giulia porta Júlia a una mostra di foto sulla Bologna degli anni Cinquanta (unità 11); il 25 aprile vanno a Venezia: sciopero dei treni, pullman, pioggia, niente Palazzo Ducale, trecento foto (12). Maggio: il quiz del carattere, la stagista Elena allo studio (13); il blog di Giulia sulla spesa a chilometro zero e il mercato contadino (14); il sabato delle pulizie, l'aspirapolvere e la signora Rossi (15); il Comune chiede ai cittadini la città che vorrebbero (16). Giugno: l'avviso del condominio e le regole del bar (17); le mail a Sara e all'amministratore (18). Domenica 21 giugno, Festa della Musica: Luca e Sara sono a Bologna, e al bar di Giulia Luca chiede a Júlia le novità.</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>L'ho visto</i> (la mostra) → <b>L'ho vista</b> 2. <i>Prendo due etti</i> (di formaggio) → <b>Ne prendo due etti</b> 3. <i>Sto per uscendo</i> → <b>Sto per uscire</b> 4. <i>La via che abito</i> → <b>La via in cui abito</b> 5. <i>Qui paga prima</i> → <b>Qui si paga prima</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia R2.1 Conversazione (lenta e naturale) · Traccia R2.2 Dettato di frasi · Traccia R2.3 Due dialoghi</div>""")

    # Page 2: listening
    topics = [("una mostra", True), ("un viaggio a Venezia", True), ("una stagista", True), ("la spesa a chilometro zero", True), ("le pulizie di casa", True),
              ("il giardino", True), ("come si paga al bar", True), ("l'esame di Bruno", False)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Júlia e Giulia hanno visto la mostra in un'ora.", "V"), ("A Venezia sono andate in treno.", "F: in pullman, per lo sciopero."),
          ("Al Palazzo Ducale non sono potute entrare.", "V"), ("Elena è più vecchia di Júlia e Marco.", "F: è più giovane."),
          ("Giulia va al mercato contadino ogni sabato.", "V"), ("Júlia passava l'aspirapolvere la domenica sera.", "F: il sabato alle otto (di mattina)."),
          ("Nel giardino ci sarà un piccolo palco.", "V"), ("Da Giulia si paga prima.", "F: si paga dopo.")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: le novità della primavera", "10 min")}
<p>Domenica 21 giugno, Festa della Musica. Al bar di Giulia, Luca chiede a Júlia le novità di questi mesi.</p>
{audiocard(["R2.1 · SLOW", "R2.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) sette argomenti. Un argomento è in più.", "3 min", "R2.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R2.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>pronome + passato prossimo</td><td>{R("L'abbiamo vista in un'ora.")}</td></tr>
<tr><td>modale al passato</td><td>{R("abbiamo dovuto prendere · non siamo potute entrare")}</td></tr><tr><td>ne / ci</td><td>{R("Ne compro dieci dozzine. · Ci vado ogni sabato.")}</td></tr>
<tr><td>preposizione + cui</td><td>{R("un angolo in cui · panchine su cui · il progetto di cui")}</td></tr><tr><td>stare per + infinito</td><td>{R("Stanno per cominciare a suonare.")}</td></tr></table>""",
    18, """<p>A: argomento in più = <span class="red">l'esame di Bruno</span> (arriva nell'unità 20). B: lo studente corregge a voce le frasi false. C: altri esempi: <i>più giovane di noi, bravissima, ordinata quanto Marco</i> (13), <i>si paga dopo</i> (17), <i>però, comunque, quindi</i> (18).</p>""")

    # Page 3: grammar 11-14
    pd = [("La mostra? ___ ho vista ieri.", ["L'"]), ("I biglietti? ___ ho già presi.", ["Li"]), ("Le cartoline? Le ho ___ ieri. (spedire)", ["spedite"]),
          ("Il film? Non l'ho ___ visto.", ["ancora"])]
    pdl = "".join(f"<li>{fill(s, a, '12mm')}</li>" for s, a in pd)
    md = [("Il treno non partiva, quindi ", ["abbiamo dovuto", "dovevamo"], "abbiamo dovuto", " prendere il pullman."),
          ("Non ", ["siamo potute", "abbiamo potuto"], "siamo potute", " entrare al Palazzo Ducale (Júlia e Giulia)."),
          ("", ["Volevo", "Ho voluto"], "Volevo", " fare un giro in gondola, ma costava 80 euro.")]
    mdl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in md)
    cp = [("Elena è giovane ___ Tommaso. (=)", ["quanto"]), ("Marco è più ordinato ___ Davide.", ["di"]), ("Questo caffè è ___! (molto buono)", ["buonissimo"]),
          ("Il tiramisù di Giulia è il ___ di Bologna. (+ buono)", ["migliore"])]
    cpl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in cp)
    nc = [("Quanti caffè bevi? — ___ bevo tre.", ["Ne"]), ("Vai spesso a Firenze? — Sì, ___ vado ogni mese.", ["ci"]),
          ("C'è ancora latte? — No, non ___ è più.", ["ce n'"]), ("Pensi alle vacanze? — Sì, ___ penso sempre.", ["ci"])]
    ncl = "".join(f"<li>{fill(s, a, '12mm')}</li>" for s, a in nc)
    b.page(f"""{sec(3, "Grammatica: unità 11–14", "10 min")}
<div class="two"><div>{sub("A", "Unità 11. Pronome + passato prossimo.", "2 min")}<ol>{pdl}</ol></div>
<div>{sub("B", "Unità 12. I modali al passato. Scegli.", "2 min")}<ol>{mdl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 13. Paragoni e superlativi.", "3 min")}<ol>{cpl}</ol></div>
<div>{sub("D", "Unità 14. Ne o ci?", "3 min")}<ol>{ncl}</ol></div></div>""",
    26, """<ol><li>A: con <i>lo, la, li, le</i> il participio si accorda: <i>l'ho vist<b>a</b>, li ho pres<b>i</b></i>. B: fatto finito → passato prossimo (<i>abbiamo dovuto</i>); intenzione non realizzata → imperfetto (<i>volevo, ma…</i>). Modale + <i>entrare</i> → <i>essere</i>.</li>
<li>C: <i>buono → migliore</i> (aggettivo), <i>bene → meglio</i> (avverbio). D: <i>ce n'è</i> = <i>ci + ne</i> davanti a <i>è</i>.</li></ol>""")

    # Page 4: grammar 15-18
    sg = [("Non posso rispondere: (guidare) ___.", ["sto guidando"]), ("Che cosa (fare, tu) ___? ", ["stai facendo"]),
          ("Corri! Il treno (partire) ___.", ["sta per partire"]), ("Shh! I bambini (dormire) ___.", ["stanno dormendo"])]
    sgl = "".join(f"<li>{fill(s, a, '26mm')}</li>" for s, a in sg)
    cc = [("la piazza", ["che", "in cui"], "in cui", "i ragazzi suonano"), ("il libro", ["che", "di cui"], "che", "sto leggendo"),
          ("la signora", ["con cui", "che"], "con cui", "parlo sulle scale"), ("un'idea", ["di cui", "che"], "di cui", "parla da anni")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    si = [("In Italia (cenare) ___ verso le otto.", ["si cena"]), ("Le bici (mettere) ___ in cortile.", ["si mettono"]),
          ("(fumare) È vietato ___ in ospedale.", ["fumare"]), ("Al bar del centro (pagare) ___ prima.", ["si paga"])]
    sil = "".join(f"<li>{fill(s, a, '20mm')}</li>" for s, a in si)
    cn = [("Piove, ___ resto a casa.", ["quindi"]), ("Volevo venire, ___ sono malata.", ["però"]), ("Fa caldo: ___ ci sono 35 gradi.", ["infatti"]),
          ("Io bevo il tè; Luca, ___, beve il caffè.", ["invece"])]
    cnl = "".join(f"<li>{fill(s, a, '16mm')}</li>" for s, a in cn)
    mk = [("La mostra? L'ho visto ieri.", "L'ho vista ieri."), ("Formaggio? Prendo due etti.", "Ne prendo due etti."), ("Sto per uscendo.", "Sto per uscire."),
          ("La via che abito è tranquilla.", "La via in cui abito è tranquilla."), ("Qui paga prima.", "Qui si paga prima.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 15–18", "10 min")}
<div class="two"><div>{sub("A", "Unità 15. Stare + gerundio o stare per.", "2 min")}<ol>{sgl}</ol></div>
<div>{sub("B", "Unità 16. Che o preposizione + cui? Scegli.", "2 min")}<ol>{ccl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 17. Il si impersonale e le regole.", "2 min")}<ol>{sil}</ol></div>
<div>{sub("D", "Unità 18. I connettivi.", "2 min")}<ol>{cnl}</ol></div></div>
{sub("E", "Unità 11–18. Correggi gli errori.", "2 min")}
<ol>{mkl}</ol>""",
    26, """<ol><li>A: <i>fare → facendo</i>; dopo <i>stare per</i> sempre l'infinito. B: il verbo vuole una preposizione? (<i>suonare <b>in</b> una piazza, parlare <b>con</b>, parlare <b>di</b></i>) → prep. + cui; <i>leggere un libro</i> → <i>che</i>.</li>
<li>C: nome plurale → verbo plurale (<i>si mettono</i>); <i>è vietato</i> + infinito senza <i>di</i>. D: <i>infatti</i> conferma, <i>invece</i> confronta.</li></ol>""")

    # Page 5: vocabulary
    cats = [("Il tempo libero", "la mostra · il concerto · la partita"), ("Il carattere", "socievole · pigro · curioso"),
            ("La casa", "stirare · il bucato · l'aspirapolvere"), ("La città", "la panchina · il marciapiede · la fermata")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("sprecare", "lo spreco"), ("vendere", "la vendita"), ("vietare", "il divieto"), ("rispondere", "la risposta"), ("abitare", "l'abitante"), ("firmare", "la firma")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    df = [("Si usa per lavare i piatti.", "la lavastoviglie"), ("100 grammi.", "un etto"), ("Lo dai al barista dopo la cassa.", "lo scontrino"),
          ("Chi va in bici.", "il / la ciclista")]
    dfl = "".join(f"<li>{a} {A(x, 'min-width:24mm')}</li>" for a, x in df)
    od = [("il pullman · la gondola · il treno · la panchina", "la panchina"), ("timido · curioso · socievole · stirare", "stirare (è un verbo)"),
          ("però · quindi · infatti · subito", "subito (non è un connettivo)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 11–16. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">l'aspirapolvere · il bucato · il concerto · curioso · la fermata · il marciapiede · la mostra · la panchina · la partita · pigro · socievole · stirare</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 4)}
<div class="two"><div>{sub("C", "Che cos'è?", "1 min")}<ol>{dfl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>B: parole dalle unità 14, 16, 17 e 18 (<i>lo spreco, l'abitante, il divieto, la risposta</i>). C: unità 14, 15, 16, 17. D: chiedere sempre perché.</p>""")

    # Page 6: dictation + social Italian
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Contadino", "Buongiorno, signorina! Quante fragole vuole?", ""), ("Júlia", "Prendo mezzo chilo. E le uova? Ce ne sono ancora?", "Ne prendo"),
          ("Contadino", "No, mi dispiace, non ho più. Sono le uova più fresche del mercato: finiscono sempre alle nove!", "non ne ho più"),
          ("Júlia", "Allora sabato prossimo vengo lì prima.", "ci vengo prima")]
    d2 = [("Marco", "Pronto, Júlia? Che cosa stai facendo?", ""), ("Júlia", "Sto scrivando una mail alla dottoressa Bianchi. È la signora che ti ho parlato.", "scrivendo · di cui"),
          ("Marco", "Ricordati: nelle mail formali scrive Cordiali saluti.", "si scrive"), ("Júlia", "Lo so! Comunque sto per uscire: ci vediamo al bar?", "")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "8 min")}
{audiocard(["R2.2", "R2.3"])}
{sub("A", "Unità 11–18. Dettato. Ascolta e scrivi le frasi.", "3 min", "R2.2")}
<ol style="line-height:1.3">{dal}</ol>
{sub("B", "Unità 14, 15, 16 e 17. Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R2.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: al mercato contadino</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: al telefono</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: altri prodotti, un'altra cosa che stai facendo.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Ogni frase ripassa un'unità, dalla 11 alla 18. Controllare l'accordo (<i>siamo potute</i>), le doppie (<i>bravissima</i>) e <i>ne</i> (<i>non ne ho più</i>).</li>
<li>B: dialogo 1: <i>Ne prendo</i>, <i>non ne ho più</i>, <i>ci vengo</i>. Dialogo 2: <i>scrivendo</i> (-ere → -endo), <i>di cui</i> (parlare di), <i>si scrive</i>. L'audio ha le versioni corrette.</li></ol>""")

    # Page 7: reflect
    cd = [("11", "So parlare del tempo libero (l'ho visto, non l'ho ancora vista)."), ("12", "So raccontare un viaggio andato storto (volevo, ho dovuto)."),
          ("13", "So descrivere il carattere e fare paragoni (-issimo, migliore)."), ("14", "So fare la spesa con ne e parlare di luoghi con ci."),
          ("15", "So dire che cosa sto facendo e che cosa sto per fare."), ("16", "So descrivere luoghi con che e cui."),
          ("17", "So spiegare le regole (si impersonale, è vietato)."), ("18", "So scrivere una mail formale e informale con i connettivi.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Che cosa vuoi ripassare ancora? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>La mia primavera.</b> Scrivi una mail a un amico italiano (50–75 parole) e raccontagli:</p>
<ol><li>un'uscita o un viaggio (passato prossimo, pronomi: <i>l'ho visto</i>);</li><li>una cosa che volevi fare ma non hai potuto (<i>volevo… ma…</i>);</li><li>che cosa stai facendo in questo periodo;</li><li>un posto della tua città in cui ti piace andare (<i>che / cui</i>). Usa almeno due connettivi.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare le righe «Non ancora» e preparare due brevi attività prima dell'unità 20. Il compito usa la grammatica delle unità 11–18. Prossima lezione: <b>Unità 20 · Il primo esame</b> (verbi + preposizione: cominciare a, finire di, provare a…).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R2.1", "Le novità della primavera (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R2.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R2.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S23)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 19 - Ripasso 2")
