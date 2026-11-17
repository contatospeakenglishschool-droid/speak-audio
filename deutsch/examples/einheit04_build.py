# Speak! Essenziell A1 - Einheit 04 "Das ist meine Familie" (alles auf Deutsch, für absolute Anfänger; Menschen A1, L2-L3) - shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 04", audio_json=os.path.join(HERE, "audio_de-a1-einheit-04.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

PHOTOS = [("A", "der Opa", "der opa"), ("B", "die Oma", "die oma"), ("C", "der Vater", "der vater"), ("D", "die Mutter", "die mutter"),
          ("E", "der Bruder", "der bruder"), ("F", "die Schwester", "die schwester"), ("G", "der Sohn", "der sohn"), ("H", "die Tochter", "die tochter")]

SCRIPT = [("Erzählerin", "Dialog eins."), ("Lena", "Ist das deine Familie?"), ("Rafael", "Ja. Das ist mein Vater, Paulo. Und das ist meine Mutter, Ana."),
          ("Lena", "Und wer ist das?"), ("Rafael", "Das ist meine Schwester, Bia. Sie ist vierundzwanzig."), ("Lena", "Hast du Geschwister?"),
          ("Rafael", "Ja, ich habe eine Schwester."),
          ("Erzählerin", "Dialog zwei."), ("Aylin", "Schau mal, das ist meine Tochter, Elif."), ("Rafael", "Oh, wie alt ist sie?"),
          ("Aylin", "Sie ist sechs. Hast du Kinder, Rafael?"), ("Rafael", "Nein. Ich bin neunundzwanzig und ledig!"),
          ("Erzählerin", "Dialog drei."), ("Herr Schneider", "Guten Tag, Herr Costa! Das ist mein Sohn, Max."), ("Max", "Hallo! Freut mich."),
          ("Rafael", "Freut mich auch! Wie geht es Ihnen, Herr Schneider?"), ("Herr Schneider", "Gut, danke!")]
S042 = ["der Opa", "die Oma", "der Vater", "die Mutter", "der Bruder", "die Schwester", "der Sohn", "die Tochter"]
NUM = [(0, "null"), (1, "eins"), (2, "zwei"), (3, "drei"), (4, "vier"), (5, "fünf"), (6, "sechs"), (7, "sieben"), (8, "acht"), (9, "neun"), (10, "zehn"),
       (11, "elf"), (12, "zwölf"), (13, "dreizehn"), (14, "vierzehn"), (15, "fünfzehn"), (16, "sechzehn"), (17, "siebzehn"), (18, "achtzehn"), (19, "neunzehn"), (20, "zwanzig"),
       (30, "dreißig"), (40, "vierzig"), (50, "fünfzig"), (60, "sechzig"), (70, "siebzig"), (80, "achtzig"), (90, "neunzig"), (100, "hundert")]
TREE = """<svg viewBox="0 0 400 130" width="100%" style="max-height:40mm" font-family="Inter, sans-serif" font-size="11">
<g stroke="#77acb5" stroke-width="1.5" fill="none"><path d="M175 30 H225"/><path d="M200 30 V75"/><path d="M130 75 H270"/><path d="M130 75 V88"/><path d="M270 75 V88"/></g>
<g fill="#fff" stroke="#176074" stroke-width="1.2"><rect x="95" y="10" width="80" height="40" rx="5"/><rect x="225" y="10" width="80" height="40" rx="5"/>
<rect x="90" y="88" width="80" height="40" rx="5"/><rect x="230" y="88" width="80" height="40" rx="5"/></g>
<g text-anchor="middle" fill="#176074"><text x="135" y="27" font-weight="700">Paulo</text><text x="135" y="42">P1</text>
<text x="265" y="27" font-weight="700">Ana</text><text x="265" y="42">P2</text>
<text x="130" y="105" font-weight="700">Rafael</text><text x="130" y="120">29</text>
<text x="270" y="105" font-weight="700">Bia</text><text x="270" y="120">P3</text></g></svg>"""

RED = '<tspan fill="#c0392b" font-weight="700">{}</tspan>'


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Seite 1
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 04", "Das ist meine Familie", "Familie · Zahlen · Wie alt bist du?",
                       [("DU KANNST", "deine Familie zeigen, nach dem Alter fragen und sagen, wie alt du bist"),
                        ("SPRACHE", "mein / meine · dein / deine · haben: ich habe, du hast · Wie alt bist du? – Ich bin 29."),
                        ("AUSSPRACHE", "Zahlen 0–100 · ei / ie in drei, vier")])
    words = ["der Bruder", "der Opa", "der Sohn", "der Vater", "die Mutter", "die Oma", "die Schwester", "die Tochter"]
    b.page(f"""{sec(1, "Einstieg: die Familie", "8 Min.")}
{sub("A", "Hör zu und sprich nach. Schreib.", "5 Min.", "04.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Mann oder Frau? Ordne.", "3 Min.")}
<div class="two"><div class="wline"><b>der</b> (Mann): {R("Opa, Vater, Bruder, Sohn")}</div><div class="wline"><b>die</b> (Frau): {R("Oma, Mutter, Schwester, Tochter")}</div></div>""",
    30, """<ol><li>A: Track 04.2 (Seite 4). Die Lehrkraft zeigt auf das Foto, der Lernende spricht nach und schreibt das Wort mit Artikel. Wiederholung zuerst: <i>Wie geht’s? Was bist du von Beruf?</i></li>
<li>B: <i>der</i> = Mann, <i>die</i> = Frau. Extra: <i>die Eltern</i> = Vater + Mutter, <i>die Geschwister</i> = Bruder + Schwester.</li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>8 Familienwörter mit Fotos</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Familienfotos: drei kurze Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>mein / meine, dein / deine</i> · <i>haben</i> · <i>Wie alt bist du?</i></td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>Familie · Zahlen 0–100</td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>Ergänzen, Zahlen schreiben, verbinden</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Rafaels Familie · Zahlen diktieren · meine Familie</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box"><h4>IMMER NOCH LANGSAM</h4>Neu sind: die Familienwörter, <i>mein / meine</i> und <i>dein / deine</i>, <i>haben</i> (ich habe, du hast, Sie haben), die Zahlen 0–100 und <i>Wie alt bist du? – Ich bin 29.</i> Die Zahlen nicht alle auf einmal: zuerst 0–20, dann die Zehner, dann 21–99 nach dem Muster. <i>sprechen</i> und <i>doch</i> kommen später (Einheit 06).</div>
<div class="box sand"><h4>DIE GESCHICHTE</h4>Rafael zeigt Lena ein Foto von seiner Familie in Curitiba: Vater Paulo, Mutter Ana und Schwester Bia (24). Im Café zeigt Aylin ein Foto von ihrer Tochter Elif (6). Rafael ist 29 und ledig. Am Nachmittag stellt Herr Schneider seinen Sohn Max vor.</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4>„Tenho 29 anos“ = <b>Ich bin 29 (Jahre alt)</b>, nicht <i>Ich habe 29 Jahre</i>. Bei Frauen <b>meine</b>: <i>mein Mutter</i> ✗ → <b>meine Mutter</b>. Zahlen 21–99 „von hinten“: 24 = <b>vier</b>und<b>zwanzig</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 04.1 Drei Dialoge (langsam und natürlich) · Track 04.2 Familie · Track 04.3 Zahlen</div>""")

    # Seite 2
    gr = [("Rafaels Schwester heißt …", ["Ana", "Bia"], "Bia"), ("Elif ist …", ["sechs", "sieben"], "sechs"), ("Max ist Herr Schneiders …", ["Bruder", "Sohn"], "Sohn")]
    wr = "".join(f'<td style="width:33%"><span class="small">{q}</span><br>{ch(o, a)}</td>' for q, o, a in gr)
    gp = [("Ist das", "deine", " Familie?"), ("Das ist", "mein", " Vater, Paulo."), ("Und das ist", "meine", " Mutter, Ana."),
          ("Ja, ich", "habe", " eine Schwester."), ("Oh, wie", "alt", " ist sie?"), ("Ich bin", "neunundzwanzig", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Familienfotos", "10 Min.")}
<p>Rafael zeigt Lena ein Foto. Aylin zeigt Rafael ein Foto. Herr Schneider stellt seinen Sohn vor.</p>
{audiocard(["04.1 · SLOW", "04.1 · NATURAL"])}
{sub("A", "Hör zu. Wähle.", "3 Min.", "04.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu. Ergänze.", "5 Min.", "04.1 · NATURAL")}
<div class="bank">alt · deine · habe · mein · meine · neunundzwanzig</div>
{twocol(gl, 4)}
{sub("C", "Hör noch einmal zu. Ergänze den Stammbaum.", "2 Min.")}
<div style="margin-top:1mm">{TREE.replace("P1", RED.format("Vater") if T else "?").replace("P2", RED.format("Mutter") if T else "?").replace("P3", RED.format("24") if T else "?")}</div>""",
    30, """<ol><li>A: <b>langsame</b> Version, zweimal hören. Neu: Max, der Sohn von Herrn Schneider. <i>Schau mal!</i> = Olha!</li>
<li>B: <b>natürliche</b> Version, nach jedem Dialog stoppen. <i>Geschwister</i> = Brüder und Schwestern.</li>
<li>C: Im Stammbaum fehlen: Paulo = Vater, Ana = Mutter, Bia = 24. Der Lernende sagt ganze Sätze: <i>Paulo ist der Vater. Bia ist vierundzwanzig.</i></li></ol>""")

    # Seite 3 (explanation first)
    pos = [("der Vater / der Sohn", "<b>mein</b> Vater", "<b>dein</b> Vater"), ("die Mutter / die Tochter", "<b>meine</b> Mutter", "<b>deine</b> Mutter"), ("die Eltern (Plural)", "<b>meine</b> Eltern", "<b>deine</b> Eltern")]
    tp = "".join(f"<tr><td>{a}</td><td>{m}</td><td>{d}</td></tr>" for a, m, d in pos)
    hb = [("ich", "habe"), ("du", "hast"), ("Sie", "haben")]
    th = "".join(f"<td style='text-align:center'>{p}<br><b>{v}</b></td>" for p, v in hb)
    chk = [("Das ist", ["mein", "meine"], "meine", "Schwester."), ("Ist das", ["dein", "deine"], "dein", "Bruder?"), ("Ich", ["habe", "bin"], "bin", "29."),
           ("", ["Hast", "Bist"], "Hast", "du Kinder?")]
    cl = "".join(f'<li>{s} {ch(o, a)} {c}</li>' for s, o, a, c in chk)
    b.page(f"""{sec(3, "Grammatik: mein, dein · haben · das Alter", "10 Min.")}
{sub("A", "Lies die Erklärung.", "4 Min.")}
<table style="margin:0"><tr><th></th><th>ich → mein</th><th>du → dein</th></tr>{tp}</table>
<div class="two" style="margin-top:2mm"><div><table style="margin:0"><tr><th colspan="3">haben</th></tr><tr>{th}</tr></table>
<p class="small" style="margin-top:1mm">Ich <b>habe</b> eine Schwester. · <b>Hast</b> du Kinder? · <b>Haben</b> Sie Kinder?</p></div>
<div class="box" style="margin:0"><h4>REGELN</h4><b>der</b> → mein / dein · <b>die</b> und Plural → mein<b>e</b> / dein<b>e</b>. &nbsp;·&nbsp; Das Alter mit <b>sein</b>: <i>Wie alt <b>bist</b> du? – Ich <b>bin</b> 29 (Jahre alt).</i></div></div>
{sub("B", "Wähle.", "3 Min.")}
<ol>{cl}</ol>
{sub("C", "Und du? Schreib.", "3 Min.")}
<div class="two"><div class="wline">Ich bin {R("… (Jahre alt).")}</div><div class="wline">Ich habe {R("eine Schwester / zwei Brüder / …")}</div></div>""",
    32, """<ol><li>A: Zuerst die Tabelle, dann den Regel-Kasten. Nur <i>ich / du / Sie</i> bei <i>haben</i>; andere Formen kommen später. <i>Sie</i> (formell) + <i>Ihr</i>: <i>Ihre Familie</i> nur zeigen.</li>
<li>B: Satz 3: der typische Fehler <i>Ich habe 29 Jahre</i> („tenho“). Im Deutschen mit <i>sein</i>.</li>
<li>C: Ohne Geschwister: <i>Ich habe keine Geschwister</i> als feste Wendung akzeptieren (<i>kein</i> kommt in Einheit 06).</li></ol>""")

    # Seite 4
    nt = "".join(f'<td style="width:14.28%;text-align:center;padding:1mm 0.5mm"><b style="font-size:11pt">{n}</b><br><span class="small">{w}</span></td>' + ("</tr><tr>" if (i + 1) % 7 == 0 and i < len(NUM) - 1 else "") for i, (n, w) in enumerate(NUM))
    b.page(f"""{sub("D", "Typische Fehler", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th></tr>
<tr><td>Ich habe 29 Jahre.</td><td><b>Ich bin 29 (Jahre alt).</b></td></tr>
<tr><td>Das ist mein Mutter.</td><td><b>Das ist meine Mutter.</b></td></tr>
<tr><td>Bia ist zwanzigvier.</td><td><b>Bia ist vierundzwanzig.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor: die Zahlen", "5 Min.")}
{audiocard(["04.2", "04.3"])}
{sub("A", "Hör zu und sprich nach.", "3 Min.", "04.3")}
<table class="ck" style="table-layout:fixed"><tr>{nt}</tr></table>
<div class="box"><h4>21–99: VON HINTEN</h4>21 = <b>ein</b>und<b>zwanzig</b> &nbsp;·&nbsp; 24 = <b>vier</b>und<b>zwanzig</b> &nbsp;·&nbsp; 29 = <b>neun</b>und<b>zwanzig</b> &nbsp;·&nbsp; 35 = <b>fünf</b>und<b>dreißig</b> &nbsp;·&nbsp; Achtung: <b>ei</b> = „ai“ (dr<b>ei</b>), <b>ie</b> = „i“ (v<b>ie</b>r)</div>
{sub("B", "Sprich: Wie alt sind sie?", "2 Min.")}
<div class="bank" style="font-weight:600;background:#fff">Rafael 29 &nbsp;·&nbsp; Bia 24 &nbsp;·&nbsp; Elif 6 &nbsp;·&nbsp; Max 41 &nbsp;·&nbsp; Paulo 58 &nbsp;·&nbsp; Ana 55</div>""",
    36, """<ol><li>Fehler: <i>Ich habe 29 Jahre</i> sofort korrigieren. Bei <i>meine</i> auf <i>die</i>-Wörter achten.</li>
<li>4A: Track 04.3: 0–20, die Zehner, dann 21, 24, 29. Track 04.2 (Familie) gehört zu Seite 1. <i>sechzehn, siebzehn</i>: ohne <i>-s</i> / <i>-en</i>. <i>dreißig</i> mit <i>ß</i>.</li>
<li>4B: Der Lernende sagt ganze Sätze: <i>Rafael ist neunundzwanzig.</i> Max = 41: <i>einundvierzig</i>.</li></ol>""")

    # Seite 5
    gw = ["mein", "meine", "deine", "dein", "habe", "hast"]
    gs = [("Das ist", " Opa."), ("Das ist", " Tochter, Elif."), ("Ist das", " Mutter, Lena?"), ("Wie heißt", " Bruder?"), ("Ich", " eine Schwester."), ("", " du Kinder?")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    nums = [(12, "zwölf"), (17, "siebzehn"), (30, "dreißig"), (45, "fünfundvierzig"), (63, "dreiundsechzig"), (99, "neunundneunzig")]
    nl = [f'<li value="{i+1}"><b>{n}</b> {A(w, "min-width:40mm")}</li>' for i, (n, w) in enumerate(nums)]
    mt = [("Wie alt bist du?", "c", "Nein, ich habe keine Kinder."), ("Hast du Geschwister?", "d", "Das ist meine Mutter."), ("Wer ist das?", "b", "Ich bin 35."), ("Haben Sie Kinder?", "a", "Ja, zwei Brüder.")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "Ergänze.", "3 Min.")}
<div class="bank">dein · deine · habe · hast · mein · meine</div>
{twocol(gl5, 4)}
{sub("B", "Schreib die Zahlen.", "2 Min.")}
{twocol(nl, 4)}
{sub("C", "Verbinde.", "3 Min.")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Satz 1 <i>der Opa</i> → <i>mein</i>; Satz 2 <i>die Tochter</i> → <i>meine</i>.</li>
<li>B: Zuerst sagen, dann schreiben. C: <i>keine Kinder</i> nur verstehen.</li></ol>""")

    # Seite 6
    ppl = [("Paulo", "Rafaels Vater · 58"), ("Ana", "Rafaels Mutter · 55"), ("Bia", "Rafaels Schwester · 24"), ("Elif", "Aylins Tochter · 6")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}</div>' for n, d in ppl)
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Frag und antworte: Wer ist das? Wie alt ist er / sie?", "4 Min.")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> Wer ist das?<br><b>B:</b> Das ist Paulo. Er ist Rafaels Vater.<br><b>A:</b> Wie alt ist er?<br><b>B:</b> Er ist achtundfünfzig.</div>
{sub("B", "Hör zu und schreib die Zahlen.", "3 Min.")}
<ol style="line-height:2"><li>{A("16", "min-width:20mm")}</li><li>{A("38", "min-width:20mm")}</li><li>{A("52", "min-width:20mm")}</li><li>{A("87", "min-width:20mm")}</li></ol>
{sub("C", "Und deine Familie? Zeig ein Foto und sprich.", "5 Min.")}
<div class="bank" style="background:#fff">Das ist mein … / meine … · Er / Sie heißt … · Er / Sie ist … (Jahre alt). · Ich habe … · Hast du Geschwister?</div>""",
    30, """<ol><li>A: <i>Rafaels Vater</i> nur verstehen und wiederholen. Die Lehrkraft fragt zuerst, dann der Lernende.</li>
<li>B: Die Lehrkraft sagt jede Zahl zweimal: sechzehn, achtunddreißig, zweiundfünfzig, siebenundachtzig.</li>
<li>C: Der Lernende zeigt ein Foto (Handy) und stellt 2–3 Personen vor. Die Lehrkraft fragt: <i>Wie alt ist er? Was ist er von Beruf?</i></li></ol>""")

    # Seite 7
    pc = [("Einheit 03", "Ich kann meinen Beruf sagen."), ("Einheit 04", "Ich kann meine Familie vorstellen (mein / meine)."),
          ("Einheit 04", "Ich kann die Zahlen 0–100 sagen."), ("Einheit 04", "Ich kann nach dem Alter fragen und sagen, wie alt ich bin.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(14, "vierzehn"), (26, "sechsundzwanzig"), (50, "fünfzig"), (73, "dreiundsiebzig")]
    hl = [f'<li value="{i+1}"><b>{n}</b> {A(w, "min-width:40mm")}</li>' for i, (n, w) in enumerate(hw)]
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. Schreib die Zahlen.</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Meine Familie.</b> Schreib 4–5 Sätze.</p>
<div class="msg">Das ist mein Vater. Er heißt … Er ist … (Jahre alt). · Das ist meine … · Ich habe …</div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Nächste Stunde: Der Lernende liest seinen Text vor und zeigt ein Familienfoto. Kurz die Zahlen wiederholen (die Lehrkraft sagt, der Lernende schreibt). In Einheit 05 kommen Dinge, Möbel, Preise und <i>der / die / das</i>.</p>""")

    b.extra("Hörtexte", f"""
{sub("04.1", "Familienfotos (langsam und natürlich)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("04.2", "Familie")}
<p>{" · ".join(S042)}</p>
{sub("04.3", "Zahlen")}
<p>{" · ".join(f"{n} {w}" for n, w in NUM)} · 21 einundzwanzig · 24 vierundzwanzig · 29 neunundzwanzig</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 04 - Das ist meine Familie")
