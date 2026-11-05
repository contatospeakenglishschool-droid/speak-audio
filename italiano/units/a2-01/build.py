# Speak! Ponte A2 - Unità 01 "Che cosa mi metto?" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
from vetrina import vetrina
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 01", audio_json=os.path.join(HERE, "audio_it-a2-unita-01.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la giacca", "giacca"), ("B", "il vestito", "vestito"), ("C", "la camicia", "camicia"), ("D", "la gonna", "gonna"),
          ("E", "i pantaloni", "pantaloni"), ("F", "le scarpe", "scarpe"), ("G", "la cravatta", "cravatta"), ("H", "il camerino", "camerino")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-01"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["01.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S012 = [x.split(": ", 1)[1] for x in _r["01.2 Ripeti domanda e affermazione"].split("\n")]
S013 = [x.split(": ", 1)[1] for x in _r["01.3 Domanda o affermazione"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 01", "Che cosa mi metto?", "Vestiti, negozi e regali · <b>mi, ti, gli, le · questo e quello · più / meno … di</b>",
                       [("SAI FARE", "comprare un vestito in un negozio, dire che cosa ti sta bene e fare paragoni"),
                        ("LINGUA", "Il blu ti sta benissimo! · Gli ho comprato una camicia. · Il blu è più caro del verde."),
                        ("PRONUNCIA", "domanda o affermazione? · Ti sta bene. / Ti sta bene?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: che cosa ti metti?", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Che cosa ti metti per andare al lavoro? E la domenica?</li><li>Che cosa ti metti per un matrimonio in Brasile?</li><li>Ti piace fare shopping? Dove compri i vestiti?</li></ol>""",
    22, """<ol><li>A: <i>i pantaloni</i> e <i>le scarpe</i> sono sempre plurali. <b>Il vestito</b> è l'abito da donna, ma anche l'abito da uomo (giacca + pantaloni); <i>i vestiti</i> = tutti gli abiti.</li>
<li>B: <i>mettersi</i> = mettere un vestito su di sé: <i>mi metto, ti metti, si mette</i>. Il titolo dell'unità: <i>Che cosa mi metto?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto di vestiti · che cosa ti metti?</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il matrimonio di Luca · al negozio · i regali</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>mi, ti, gli, le · questo / quello · più / meno … di</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>I pronomi indiretti: forma, posizione, atono o tonico, diretto o indiretto</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Domanda o affermazione?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Pronomi indiretti · la vetrina · parole del negozio</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Gioco di ruolo al negozio · i regali</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA: COMINCIA L'A2</h4>È settembre. Júlia è tornata dal Brasile e Bruno è arrivato a Bologna per studiare (unità 26). Sabato Luca, il fratello di Marco, si sposa a Firenze con Sara, e Júlia non sa che cosa mettersi. Giulia la accompagna in un negozio di via Indipendenza: Júlia prova un vestito blu e uno verde e prende il blu, più caro ma più elegante. La sera, sulle scale, racconta a Davide che ha comprato una camicia e una cravatta per Bruno (che odia le cravatte) e che agli sposi regalano un buono per il viaggio di nozze in Portogallo. Davide presta a Bruno la sua giacca grigia.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese parlato usa poco i pronomi indiretti (<i>dei um presente pra ele</i>), quindi lo studente dice <i>ho regalato a lui</i> o li evita. <b>Gli</b> e <b>le</b> si confondono (<i>gli</i> = a lui e a loro; <i>le</i> = a lei). <i>Ligar para</i> → <b>telefonare a</b>: <i>Gli telefono</i>, non <i>Lo telefono</i>. <i>Mais caro que</i> → <b>più caro di</b>. Per i vestiti si chiede la <b>taglia</b>, il <b>numero</b> è solo per le scarpe.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>A un matrimonio italiano non si mette il <b>bianco</b>: è il colore della sposa. Gli invitati spesso regalano un contributo per il <b>viaggio di nozze</b> o un oggetto della <b>lista di nozze</b>. I <b>saldi</b> cominciano all'inizio di gennaio e di luglio, e la data la decide ogni regione. Nei negozi si dà del <b>Lei</b>: <i>Desidera? Che taglia porta?</i> Le taglie italiane non sono come quelle brasiliane: meglio provare.</div>
<div class="box"><h4>AUDIO</h4>Traccia 01.1 Tre dialoghi (lento e naturale) · Traccia 01.2 Domanda e affermazione · Traccia 01.3 Domanda o affermazione?</div>""")

    # Page 2
    qs = [("Perché Júlia non sa che cosa mettersi?", "sabato Luca si sposa e lei ha solo un vestito nero vecchio"),
          ("Perché Júlia non può mettere il bianco?", "il bianco è solo per la sposa"),
          ("Che taglia porta Júlia?", "la quarantadue (42)"),
          ("Quanto costano i due vestiti?", "il blu 90 euro, il verde 65 euro"),
          ("Che cosa regalano agli sposi?", "un buono per il viaggio di nozze in Portogallo")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:52mm')}</li>" for q, a in qs)
    vf = [("Giulia accompagna Júlia in via Indipendenza.", "V"), ("Júlia prova solo il vestito blu.", "F"), ("Giulia dice che il verde è meno elegante del blu.", "V"),
          ("Júlia ha comprato una giacca per Bruno.", "F"), ("A Bruno le cravatte piacciono molto.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: un vestito per il matrimonio", "10 min")}
<p>Luca, il fratello di Marco, si sposa. Che cosa si mette Júlia? E che cosa regala?</p>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL"])}
{sub("A", "Ascolta e rispondi alle domande.", "5 min", "01.1 · SLOW")}
<ol style="line-height:1.55">{ql}</ol>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "3 min", "01.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Che cosa ha comprato Júlia per Bruno? Che cosa gli presta Davide?", "2 min")}
<div class="wline">{R("una camicia e una cravatta · Davide gli presta una giacca grigia")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. <i>Sei un tesoro</i> = sei gentilissima. <i>Gli sposi</i> = Luca e Sara.</li>
<li>B: versione <b>naturale</b>. 2: prova <b>tutti e due</b>. 4: <b>camicia e cravatta</b>; la giacca è di Davide. 5: <b>non</b> gli piacciono.</li></ol>""")

    # Page 3
    rules = [("Nella frase 2, <b>ti</b> =", ["a te", "te"], "a te"),
             ("Nella frase 3, <b>gli</b> = a Bruno, cioè", ["a lui", "a lei"], "a lui"),
             ("Nella frase 5, <b>gli</b> = a Luca e Sara, cioè", ["a lei", "a loro"], "a loro"),
             ("Nella frase 1, la commessa usa <b>Le</b> perché dà", ["del tu", "del Lei"], "del Lei"),
             ("Il pronome <i>mi, ti, gli, le</i> va", ["prima del verbo", "dopo il verbo"], "prima del verbo"),
             ("Per il contrasto (<i>a Bruno no, a me sì</i>) usiamo", ["mi", "a me"], "a me"),
             ("Per il paragone diciamo più / meno + aggettivo +", ["di", "che"], "di")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    qq = [("vicino a me", "<b>questo</b> vestito · <b>questa</b> giacca · <b>questi</b> pantaloni · <b>queste</b> scarpe"),
          ("lontano da me", "<b>quel</b> vestito · <b>quello</b> specchio · <b>quell'</b>abito · <b>quella</b> gonna<br><b>quei</b> pantaloni · <b>quegli</b> stivali · <b>quelle</b> scarpe"),
          ("da solo", "Quale preferisci? — <b>Quello</b> verde. · <b>Questa</b> è più cara di <b>quella</b>.")]
    qqr = "".join(f"<tr><td style='width:28mm'><b>{a}</b></td><td>{x}</td></tr>" for a, x in qq)
    b.page(f"""{sec(3, "Grammatica: mi, ti, gli, le · questo e quello · più / meno … di", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Le</b> piace questo vestito blu? &nbsp; 2. Il blu <b>ti</b> sta benissimo!<br>
3. <b>Gli</b> ho comprato una camicia e una cravatta. &nbsp; 4. A Bruno le cravatte non piacciono, ma <b>a me</b> sì!<br>
5. E agli sposi? <b>Gli</b> regaliamo un buono per il viaggio di nozze.<br>
6. Il verde è <b>meno</b> elegante <b>del</b> blu. &nbsp; 7. Il blu è <b>più</b> caro <b>del</b> verde. &nbsp; 8. <b>Questo</b> costa 90 euro, <b>quello</b> verde 65.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Questo o quello?", "3 min")}
<table style="margin:0">{qqr}</table>
<div class="box sand"><h4>REGOLA</h4><b>Pronomi indiretti</b> (a chi?): <b>mi, ti, gli, le, Le, ci, vi, gli</b> = a me, a te, a lui, a lei, a Lei, a noi, a voi, a loro. Vanno <b>prima del verbo</b>: <i>Gli telefono.</i> <b>Paragoni</b>: più / meno + aggettivo + <b>di</b> (<i>del, della…</i>): <i>più caro del verde</i>. <b>Quello</b> cambia come l'articolo: <i>il → quel, lo → quello, i → quei, gli → quegli</i>. Tutto sui pronomi: pagina 4.</div>""",
    20, """<ol><li>A: nella frase 5 <b>gli</b> = <b>agli sposi</b> = a loro. Nel parlato <i>gli</i> sostituisce anche <i>a loro</i>.</li>
<li>B: far trovare allo studente la persona dietro ogni pronome (<i>Le</i> = Júlia, per la commessa). C: <i>quello</i> segue l'articolo determinativo (unità 4 dell'A1).</li></ol>""")

    grammar_ref_it.pronomi_indiretti(b)

    # Page 5
    ans3 = ["?", ".", "?", "?", ".", "."]
    s3 = [s.rstrip("?.") for s in S013]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Lo telefono stasera.</td><td><b>Gli telefono stasera.</b></td><td><i>telefonare a</i> → indiretto.</td></tr>
<tr><td>A Giulia gli piace il blu.</td><td><b>A Giulia piace il blu. / Le piace il blu.</b></td><td>Un solo pronome; lei = <i>le</i>.</td></tr>
<tr><td>Ho regalato a lui una cravatta.</td><td><b>Gli ho regalato una cravatta.</b></td><td>Senza contrasto: l'atono.</td></tr>
<tr><td>Il blu è più caro que il verde.</td><td><b>Il blu è più caro del verde.</b></td><td><i>più … di</i> (di + il = del).</td></tr>
<tr><td>Quello vestito è bello.</td><td><b>Quel vestito è bello.</b></td><td>Come l'articolo: <i>il → quel</i>.</td></tr>
<tr><td>Che numero porta? (per un vestito)</td><td><b>Che taglia porta?</b></td><td>Il numero è per le scarpe.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["01.2", "01.3"])}
{sub("A", "Domanda o affermazione? Ascolta e ripeti. Le parole sono uguali: cambia solo la melodia. Nella domanda la voce sale alla fine.", "2 min", "01.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S012)}</div>
{sub("B", "Ascolta. È una domanda (?) o un'affermazione (.)? Scegli mentre ascolti.", "2 min", "01.3")}
{twocol([f'<li value="{i+1}">{s} {ch([".", "?"], a)}</li>' for i, (s, a) in enumerate(zip(s3, ans3))], 3)}""",
    26, """<ol><li>Errori: <i>a lui</i> non è sbagliato, ma serve solo per il contrasto (<i>a lui sì, a lei no</i>). Di solito si usa <b>gli</b>.</li>
<li>4A/4B: in italiano, come in portoghese, la domanda sì/no non cambia l'ordine delle parole. Dopo l'ascolto, lo studente legge una frase come domanda o come affermazione e l'insegnante indovina.</li></ol>""")

    # Page 6
    gp = [("Bruno compie venticinque anni: ", "gli", " regalo un libro."), ("Signora Rossi, ", "Le", " piace questo vestito?"), ("Giulia, questa giacca ", "ti", " sta benissimo!"),
          ("Sara è la sposa: ", "le", " scrivo un messaggio di auguri."), ("Ragazzi, ", "vi", " telefono domani, va bene?"), ("Luca e Sara ", "ci", " hanno mandato l'invito: a me e a Bruno.")]
    gpl = [f'<li value="{i+1}">{a}{A(x, "min-width:11mm")}{z}</li>' for i, (a, x, z) in enumerate(gp)]
    cm = [("la giacca nera / la giacca grigia (cara)", "La giacca nera è più cara della giacca grigia."),
          ("il vestito verde / il vestito blu (caro)", "Il vestito verde è meno caro del vestito blu."),
          ("le scarpe marroni / le scarpe nere (economiche)", "Le scarpe marroni sono più economiche delle scarpe nere."),
          ("quella giacca grigia / questa giacca nera (elegante)", "Secondo me quella giacca grigia è meno / più elegante di questa giacca nera.")]
    cml = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in cm)
    wb = [("la taglia", "la misura di un vestito: 40, 42, 44 o S, M, L"), ("il camerino", "il piccolo spazio dove provi i vestiti"),
          ("la vetrina", "dove il negozio mostra i vestiti a chi passa per strada"), ("i saldi", "il periodo con i prezzi più bassi"),
          ("lo sconto", "il prezzo meno alto: «il 20% di …»"), ("lo scontrino", "il foglio che ricevi quando paghi"),
          ("la cassa", "il posto dove paghi"), ("provare", "mettere un vestito per vedere come ti sta")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:19mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Completa con mi, ti, gli, le, Le, ci o vi.", "3 min")}
{twocol(gpl, 3)}
{sub("B", "La vetrina. Guarda i prezzi e scrivi un paragone con più … di o meno … di.", "3 min")}
{vetrina()}
<ol style="line-height:1.4">{cml}</ol>
{sub("C", "Parole del negozio. Scrivi la parola giusta.", "3 min")}
<div class="bank">la cassa · il camerino · provare · i saldi · lo sconto · lo scontrino · la taglia · la vetrina</div>
{twocol(wbl, 4)}""",
    20, """<ol><li>A: chiedere sempre <i>a chi?</i> 6: <i>ci</i> = a me e a Bruno. B: <i>di + la = della</i>, <i>di + le = delle</i>. La 4 è un'opinione.</li>
<li>C: mini-scena: <i>Posso provare la 42? C'è uno sconto?</i></li></ol>""")

    # Page 7
    ul = ("Desidera? · Che taglia porta? · Posso provare…? · Dov'è il camerino? · Come mi sta? · Ti / Le sta benissimo! · "
          "Ce l'ha in blu? · Ce l'ha in una taglia più grande? · Quanto costa? · È un po' caro. · C'è uno sconto? · Lo / La prendo. · Si può cambiare?")
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Gioco di ruolo: al negozio di vestiti. Leggi la tua situazione. Poi scambiate i ruoli.", "7 min")}
<div class="two"><div class="box" style="margin-top:1mm"><h4>CLIENTE (tu)</h4>Il mese prossimo hai un evento importante (un matrimonio, un colloquio di lavoro o una cena elegante). Saluta, di' che cosa cerchi, la taglia e il colore. Prova due cose e chiedi un'opinione. Chiedi il prezzo, fai un paragone e decidi: lo prendi o no?</div>
<div class="box" style="margin-top:1mm"><h4>COMMESSO / COMMESSA (l'insegnante)</h4>Dai del <b>Lei</b> al cliente. Chiedi che cosa cerca e che taglia porta. Proponi due vestiti (<i>questo… o quello…?</i>). Indica il camerino. Di' il prezzo: uno è più caro, ma è più elegante. Oggi c'è uno sconto del 20% su un articolo.</div></div>
<div class="box sand" style="font-size:9pt"><h4>FRASI UTILI</h4>{ul}</div>
{sub("B", "I regali. Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Che cosa regali a tua madre per il compleanno? E a un amico che si sposa?</li><li>Che cosa ti hanno regalato per il tuo ultimo compleanno? Ti è piaciuto?</li>
<li>Che colori ti stanno bene? Che cosa non ti metti mai?</li><li>Preferisci comprare i vestiti in un negozio o online? Perché?</li></ol>""",
    24, """<ol><li>A: prima l'insegnante fa il commesso, poi lo studente. Ascoltare il <i>Lei</i> del commesso (<i>Le piace? Le sta bene</i>) e il <i>tu</i> tra amici (<i>ti sta bene</i>). <i>Ce l'ha in blu?</i> = lo avete in blu? (solo da usare come frase fatta).</li>
<li>B: correggere alla fine <i>a lui</i> → <i>gli</i> e <i>più … que</i> → <i>più … di</i>.</li></ol>""")

    # Page 8
    pc = [("A1 · 20", "So descrivere l'aspetto di una persona."), ("A1 · 26", "So raccontare che cosa ho fatto quest'anno."),
          ("A2 · 01", "So comprare un vestito e chiedere taglia, colore e prezzo."), ("A2 · 01", "So usare mi, ti, gli, le, Le, ci, vi."),
          ("A2 · 01", "So fare paragoni con più / meno … di e usare questo / quello.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Lo telefono domani.", "Gli telefono domani."), ("Questa gonna è più cara di quella.", "✓"), ("A Sara gli piace il Portogallo.", "A Sara piace il Portogallo. / Le piace…"),
          ("Quello pantaloni sono belli.", "Quei pantaloni sono belli."), ("Gli ho comprato una cravatta.", "✓"), ("Il verde è meno elegante che il blu.", "…meno elegante del blu.")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:44mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio a un'amica (50–75 parole).</b> Sabato vai a una festa importante. Racconta che cosa hai comprato, che cosa ti metti e perché (usa <i>più / meno … di</i>), e che cosa regali al festeggiato (usa <i>gli</i> o <i>le</i>).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il messaggio. Fare domande: <i>Che cosa gli regali? Ti sta bene il rosso?</i> Unità 02: <i>Da bambina…</i> (l'imperfetto).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("01.1", "Un vestito per il matrimonio (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "Domanda e affermazione")}
<p>{" · ".join(S012)}</p>
{sub("01.3", "Domanda o affermazione?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S013))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 01 - Che cosa mi metto")
