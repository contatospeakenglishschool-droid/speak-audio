# Speak! Essenziale A1 - Unità 20 "Com'è?" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from volti import thepeople
setup(band="A1 · UNITÀ 20", audio_json=os.path.join(HERE, "audio_it-a1-unita-20.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "i capelli lunghi", "capelli lunghi"), ("B", "i capelli corti", "capelli corti"), ("C", "i capelli ricci", "capelli ricci"), ("D", "la barba", "barba"),
          ("E", "gli occhiali", "occhiali"), ("F", "gli occhi azzurri", "occhi azzurri"), ("G", "i capelli grigi", "capelli grigi"), ("H", "calvo", "calvo")]

SCRIPT = [("Narratore", "Dialogo uno. Allo studio."), ("Marco", "Júlia, oggi devo andare a prendere l'ingegnere Ferri alla stazione, ma non la conosco. Com'è?"),
          ("Júlia", "È alta, ha i capelli corti e biondi e porta gli occhiali. Ha circa cinquant'anni."), ("Marco", "E di carattere?"),
          ("Júlia", "È molto gentile, ma un po' seria. Ah, porta sempre una giacca rossa!"), ("Marco", "Perfetto, allora la trovo subito."),
          ("Narratore", "Dialogo due. Al bar."), ("Giulia", "Júlia, com'è tuo fratello? Non lo conosco ancora."),
          ("Júlia", "Bruno è alto e magro, ha i capelli ricci e neri e gli occhi castani. È molto simpatico, ma un po' pigro!"), ("Giulia", "Ha la barba?"),
          ("Júlia", "Sì, ha la barba."), ("Giulia", "Ah, allora l'ho visto ieri qui al bar! Ha preso tre cornetti!"),
          ("Narratore", "Dialogo tre. Sulle scale."), ("Davide", "Júlia, tuo fratello è proprio divertente! Alla festa ha conosciuto una ragazza, Chiara."),
          ("Júlia", "Davvero? Com'è?"), ("Davide", "È bassa e ha i capelli lunghi e rossi."), ("Júlia", "E di carattere?"),
          ("Davide", "È abbastanza timida, ma molto intelligente. Studia medicina."), ("Júlia", "Bene! Bruno parla sempre… lei ascolta!")]
S202 = ["simpatico, simpatici", "simpatica, simpatiche", "amico, amici", "amica, amiche", "antipatico, antipatici", "I miei amici sono simpatici e le mie amiche sono simpatiche."]
S203 = ["Com'è tuo fratello?", "È alto e magro.", "Ha i capelli ricci e neri.", "Ha gli occhi castani e porta gli occhiali.", "È molto simpatico, ma un po' pigro.",
        "Lei è abbastanza timida, ma molto intelligente."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 20", "Com'è?", "Descrivere le persone · <b>è alto, ha i capelli ricci, è simpatico</b>",
                       [("SAI FARE", "descrivere l'aspetto e il carattere di una persona e riconoscere una persona da una descrizione"),
                        ("LINGUA", "essere + aggettivo · avere i capelli / gli occhi · portare gli occhiali · molto, abbastanza, un po'"),
                        ("PRONUNCIA", "C e CH al plurale: simpatici, simpatiche · descrivere una persona")])
    words = [w for _, w, _ in PHOTOS]
    op = [("alto", "basso"), ("giovane", "anziano"), ("simpatico", "antipatico"), ("lunghi", "corti"), ("lisci", "ricci"), ("timido", "estroverso")]
    opl = [f'<li value="{i+1}">{a} ↔ {A(x, "min-width:24mm")}</li>' for i, (a, x) in enumerate(op)]
    b.page(f"""{sec(1, "Riscaldamento: l'aspetto", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le parole sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Scrivi il contrario.", "4 min")}
<div class="bank" style="background:#fff">anziano · antipatico · basso · corti · estroverso · ricci</div>
{twocol(opl, 4)}""",
    24, """<ol><li>A: <i>calvo</i> = senza capelli. Gli occhi possono essere <i>azzurri, verdi, castani, neri</i>; i capelli <i>biondi, castani, neri, rossi, grigi</i>.</li>
<li>B: <i>i capelli</i> è maschile plurale: <i>lunghi, corti, lisci, ricci</i>. Chiedere: <i>Com'è il tuo migliore amico?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: capelli, occhi, barba · i contrari</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Tre descrizioni: l'ingegnere Ferri, Bruno, Chiara</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>essere / avere / portare · accordo degli aggettivi · molto, abbastanza, un po'</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>C e CH al plurale · descrivere una persona</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Chi è? Sei ritratti · l'accordo</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Indovina chi? · una persona importante per te</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Marco deve andare a prendere alla stazione l'ingegnere Ferri, ma non la conosce: Júlia la descrive (alta, capelli corti e biondi, occhiali, giacca rossa). Giulia chiede com'è Bruno: alto, magro, capelli ricci, barba… l'ha visto al bar con tre cornetti! Davide racconta che alla festa Bruno ha conosciuto Chiara: bassa, capelli lunghi e rossi, timida ma molto intelligente.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Bruno tiene la barba</i> ✗ → <b>Bruno ha la barba</b>. <i>Capelli marroni</i> ✗ → <b>capelli castani</b>. <i>I capelli lunghe</i> ✗ → <b>lunghi</b> (maschile plurale). <i>Simpatichi</i> ✗ → <b>simpatici</b>. <i>È un po' intelligente</i> ✗ → <i>un po'</i> solo con le qualità negative: <b>è un po' pigro</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Parlare del peso di una persona è delicato: invece di <i>grasso</i> gli italiani dicono <b>robusto</b> o <b>un po' in carne</b>. Per i capelli scuri si dice spesso <b>moro / mora</b>; <i>marrone</i> si usa per le cose, non per i capelli e gli occhi (<b>castani</b>).</div>
<div class="box"><h4>AUDIO</h4>Traccia 20.1 Tre dialoghi (lento e naturale) · Traccia 20.2 C e CH al plurale · Traccia 20.3 Descrivere una persona</div>""")

    # Page 2
    pp = [("L'ingegnere Ferri", "alta, capelli corti e biondi, occhiali", "molto gentile, un po' seria"), ("Bruno", "alto e magro, capelli ricci e neri, barba", "molto simpatico, un po' pigro"),
          ("Chiara", "bassa, capelli lunghi e rossi", "abbastanza timida, molto intelligente")]
    ppr = "".join(f"<tr><td style='width:30mm'><b>{n}</b></td><td>{A(a, 'min-width:62mm')}</td><td>{A(c, 'min-width:46mm')}</td></tr>" for n, a, c in pp)
    vf = [("Marco conosce già l'ingegnere Ferri.", "F"), ("L'ingegnere Ferri porta sempre una giacca rossa.", "V"), ("Giulia ha visto Bruno al bar.", "V"), ("Chiara studia medicina.", "V"),
          ("Chiara è molto estroversa.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: com'è?", "10 min")}
<p>Allo studio, al bar e sulle scale: tre persone da descrivere.</p>
{audiocard(["20.1 · SLOW", "20.1 · NATURAL"])}
{sub("A", "Ascolta e completa: com'è? Aspetto e carattere.", "5 min", "20.1 · SLOW")}
<table style="margin:0"><tr><th></th><th>Aspetto</th><th>Carattere</th></tr>{ppr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "3 min", "20.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Come riconosce Marco l'ingegnere Ferri alla stazione?", "2 min")}
<div class="wline">{R("È alta, ha i capelli corti e biondi, porta gli occhiali e una giacca rossa.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi. <i>L'ingegnere</i> si usa anche per una donna.</li>
<li>B: versione <b>naturale</b>. 1: Marco <b>non la conosce</b>. 5: Chiara è <b>abbastanza timida</b>. <i>L'ho visto</i> = ho visto lui (pronome + passato prossimo, solo da capire).</li></ol>""")

    # Page 3
    asp = [("essere", "alto/a · basso/a · magro/a · giovane · anziano/a · calvo"), ("avere", "i capelli corti / lunghi · lisci / ricci · biondi / castani / neri / rossi / grigi"),
           ("avere", "gli occhi azzurri / verdi / castani · la barba · i baffi"), ("portare", "gli occhiali")]
    tasp = "".join(f"<tr><td style='width:20mm'><b>{a}</b></td><td>{x}</td></tr>" for a, x in asp)
    ag = [("alto", "alta", "alti", "alte"), ("simpatico", "simpatica", "simpatici", "simpatiche"), ("gentile", "gentile", "gentili", "gentili")]
    tag = "".join(f"<tr><td><b>{a}</b></td><td><b>{bb}</b></td><td><b>{c}</b></td><td><b>{d}</b></td></tr>" for a, bb, c, d in ag)
    rules = [("Bruno", "ha i capelli ricci", "è i capelli ricci"), ("Chiara ha gli occhi", "verde", "verdi"), ("Giulia è molto", "simpatica", "simpatico"),
             ("I miei amici sono", "simpatichi", "simpatici")]
    def rule(i, s, right, wrong):
        # in this list some correct answers come second on purpose
        o = [right, wrong]
        good = {"ha i capelli ricci", "verdi", "simpatica", "simpatici"}
        o = [R(f"<u>{x}</u>") if (T and x in good) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: descrivere l'aspetto e il carattere", "10 min")}
{sub("A", "L'aspetto: essere, avere, portare.", "3 min")}
<table style="margin:0">{tasp}</table>
<div class="two"><div>{sub("B", "L'accordo degli aggettivi.", "2 min")}
<table style="margin:0"><tr><th>m. sing.</th><th>f. sing.</th><th>m. pl.</th><th>f. pl.</th></tr>{tag}</table>
<p class="small" style="margin-top:1mm"><i>i capelli</i> = maschile plurale → <i>i capelli lung<b>hi</b>, ner<b>i</b></i></p></div>
<div>{sub("C", "Il carattere: quanto?", "2 min")}
<p><b>molto</b> simpatico · <b>abbastanza</b> timida<br><b>un po'</b> pigro / serio (solo qualità negative)<br><b>non</b> è <b>per niente</b> antipatico</p>
<p class="small">simpatico · gentile · divertente · intelligente · timido · serio · pigro · generoso</p></div></div>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>""",
    24, """<ol><li>A: in italiano i capelli e gli occhi si descrivono con <b>avere</b>, non con <i>essere</i>. Gli occhiali si <b>portano</b>.</li>
<li>B: <i>simpatico → simpatici</i> (suono «ci»), ma <i>simpatica → simpatiche</i> (suono «che»): pagina 4, pronuncia.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Bruno tiene la barba.</td><td><b>Bruno ha la barba.</b></td><td>Aspetto fisico: <i>avere</i>.</td></tr>
<tr><td>Ha i capelli marroni.</td><td><b>Ha i capelli castani.</b></td><td>Capelli e occhi: <i>castani</i>.</td></tr>
<tr><td>Chiara ha i capelli lunghe.</td><td><b>Chiara ha i capelli lunghi.</b></td><td><i>i capelli</i> = maschile.</td></tr>
<tr><td>I miei amici sono simpatichi.</td><td><b>I miei amici sono simpatici.</b></td><td>Plurale in <i>-ci</i>.</td></tr>
<tr><td>Marco è un po' intelligente.</td><td><b>Marco è molto intelligente.</b></td><td><i>un po'</i> solo per il negativo.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["20.2", "20.3"])}
{sub("A", "C e CH al plurale. Ascolta e ripeti: simpatiCI (suono dolce) e simpatiCHE (suono duro).", "2 min", "20.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S202)}</div>
{sub("B", "Descrivere una persona. Ascolta e ripeti.", "3 min", "20.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S203)}</div>""",
    38, """<ol><li>Errori: <i>tenere</i> in italiano vuol dire tenere in mano. Per l'aspetto si usa sempre <i>avere</i>.</li>
<li>4A: ripasso dell'unità 02 (<i>ci / chi, ce / che</i>) applicato al plurale. Attenzione: <i>amico → amici</i> ma <i>amica → amiche</i>.</li></ol>""")

    # Page 5
    who = [("Ha i capelli lunghi e rossi.", "Chiara"), ("È calvo e ha i baffi grigi.", "Sergio"), ("Ha i capelli corti e biondi e porta gli occhiali.", "Anna"),
           ("Ha i capelli ricci e neri e la barba.", "Paolo")]
    whl = [f'<li value="{i+1}">{s} {A(x, "min-width:22mm")}</li>' for i, (s, x) in enumerate(who)]
    ds = [("Lucia", "Lucia ha i capelli lunghi e castani e porta gli occhiali."), ("Tommaso", "Tommaso ha i capelli corti e neri. È giovane.")]
    dsl = "".join(f'<li>{n}<div class="wline">{R(x)}</div></li>' for n, x in ds)
    ac = [("Le mie sorelle sono", "alte", "alto"), ("Marco e Luca sono", "simpatici", "simpatico"), ("Giulia è", "gentile", "gentile"), ("Chiara ha i capelli", "lunghi", "lungo")]
    acl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")} <span class="small">({n})</span></li>' for i, (a, x, n) in enumerate(ac)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Chi è? Leggi e scrivi il nome.", "3 min")}
<div style="margin:1mm 0 2mm">{thepeople(170)}</div>
{twocol(whl, 3)}
{sub("B", "Descrivi Lucia e Tommaso.", "2 min")}
<ol>{dsl}</ol>
{sub("C", "Scrivi l'aggettivo nella forma corretta.", "3 min")}
{twocol(acl, 3)}""",
    22, """<ol><li>A: dopo l'esercizio, l'insegnante descrive una persona del disegno e lo studente indovina.</li>
<li>B: accettare altre descrizioni corrette (<i>Tommaso è giovane, non porta gli occhiali</i>).</li></ol>""")

    # Page 6
    qs = ["È un uomo o una donna?", "Ha i capelli lunghi?", "Ha la barba?", "Porta gli occhiali?", "È giovane?", "È italiano/a?"]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Indovina chi? L'insegnante pensa a una persona (del disegno a pagina 5 o famosa). Fai domande: l'insegnante risponde solo sì o no.", "5 min")}
<div class="bank" style="background:#fff">{" · ".join(qs)}</div>
<p class="small">Poi cambiate: tu pensi a una persona e l'insegnante fa le domande.</p>
{sub("B", "Una persona importante per te. Scrivi tre parole per l'aspetto e tre per il carattere. Poi descrivi la persona all'insegnante.", "4 min")}
<table style="margin:1mm 0 2mm"><tr><th style="width:30mm">Chi è?</th><td></td></tr><tr><th>Aspetto</th><td style="height:9mm"></td></tr><tr><th>Carattere</th><td style="height:9mm"></td></tr></table>
{sub("C", "Rispondi all'insegnante.", "3 min")}
<ol style="line-height:1.65"><li>Com'è il tuo collega o il tuo amico ideale?</li><li>Sei timido/a o estroverso/a? Sei pigro/a?</li><li>A chi assomigli nella tua famiglia?</li></ol>""",
    26, """<ol><li>A: per «Indovina chi?» l'insegnante risponde con frasi complete (<i>Sì, ha la barba</i>) per dare un modello. Vince chi indovina con meno domande.</li>
<li>B: correggere <i>avere</i> per i capelli e l'accordo degli aggettivi. C: <i>assomigliare a</i> = essere simile a (solo da capire).</li></ol>""")

    # Page 7
    pc = [("Unità 19", "So invitare e rispondere a un invito."), ("Unità 20", "So descrivere l'aspetto di una persona."), ("Unità 20", "So descrivere il carattere."),
          ("Unità 20", "So fare l'accordo degli aggettivi."), ("Unità 20", "So riconoscere una persona da una descrizione.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Bruno tiene la barba.", "Bruno ha la barba."), ("Chiara ha i capelli lunghe.", "Chiara ha i capelli lunghi."), ("Mia sorella è molto simpatico.", "Mia sorella è molto simpatica."),
          ("I miei amici sono simpatichi.", "I miei amici sono simpatici."), ("Marco ha i capelli marroni.", "Marco ha i capelli castani."), ("Giulia è un po' gentile.", "Giulia è molto gentile.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Una persona speciale.</b> Scrivi 6 frasi su una persona che conosci bene: com'è (aspetto) e com'è di carattere.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi lo studente descrive un compagno di lavoro o un attore famoso e l'insegnante indovina chi è.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("20.1", "Com'è? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("20.2", "C e CH al plurale")}
<p>{" · ".join(S202)}</p>
{sub("20.3", "Descrivere una persona")}
<p>{" ".join(S203)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 20 - Com'è")
