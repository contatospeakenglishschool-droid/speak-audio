# Speak! Essenziell A1 - Einheit 02 "Wie geht's?" (alles auf Deutsch, für absolute Anfänger) - built with the shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 02", audio_json=os.path.join(HERE, "audio_de-a1-einheit-02.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

PHOTOS = [("A", "Super!", "super"), ("B", "Sehr gut!", "sehr gut"), ("C", "Gut.", "gut"), ("D", "Es geht.", "es geht"),
          ("E", "Nicht so gut.", "nicht so gut"), ("F", "Schlecht.", "schlecht"), ("G", "müde", "müde"), ("H", "krank", "krank")]

SCRIPT = [("Erzählerin", "Dialog eins."), ("Rafael", "Guten Morgen, Herr Schneider!"), ("Herr Schneider", "Guten Morgen, Herr Costa! Wie geht es Ihnen?"),
          ("Rafael", "Gut, danke. Und Ihnen?"), ("Herr Schneider", "Sehr gut, danke."),
          ("Erzählerin", "Dialog zwei."), ("Frau Krüger", "Guten Tag! Sind Sie Herr Costa?"), ("Rafael", "Ja, ich bin Rafael Costa."),
          ("Frau Krüger", "Wie schreibt man Costa?"), ("Rafael", "C – O – S – T – A."), ("Frau Krüger", "Danke!"),
          ("Erzählerin", "Dialog drei."), ("Aylin", "Hallo, Rafael! Wie geht’s?"), ("Rafael", "Es geht. Ich bin müde. Und dir?"),
          ("Aylin", "Super, danke! Rafael, das ist Jonas. Er ist Student."), ("Jonas", "Hallo, Rafael!"), ("Rafael", "Hallo, Jonas! Freut mich!")]
S022 = ["Super!", "Sehr gut!", "Gut.", "Es geht.", "Nicht so gut.", "Schlecht.", "müde", "krank"]
ABC = [("A", "a"), ("B", "be"), ("C", "tse"), ("D", "de"), ("E", "e"), ("F", "ef"), ("G", "ge"), ("H", "ha"), ("I", "i"), ("J", "jott"),
       ("K", "ka"), ("L", "el"), ("M", "em"), ("N", "en"), ("O", "o"), ("P", "pe"), ("Q", "ku"), ("R", "er"), ("S", "es"), ("T", "te"),
       ("U", "u"), ("V", "fau"), ("W", "we"), ("X", "ix"), ("Y", "ypsilon"), ("Z", "tsett"), ("Ä", "ä"), ("Ö", "ö"), ("Ü", "ü"), ("ß", "eszett")]
HOT = {"E", "H", "I", "J", "V", "W", "Y", "Z"}


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Seite 1
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 02", "Wie geht’s?", "Fragen und sagen, wie es geht · das Alphabet",
                       [("DU KANNST", "fragen, wie es geht, antworten und deinen Namen buchstabieren"),
                        ("SPRACHE", "Wie geht’s? / Wie geht es Ihnen? · ich bin, du bist, er / sie ist, Sie sind"),
                        ("AUSSPRACHE", "das Alphabet · E, I, J, V, W, Z")])
    words = ["krank", "müde", "Es geht.", "Gut.", "Nicht so gut.", "Schlecht.", "Sehr gut!", "Super!"]
    me = "".join(f'<td style="text-align:center">☐<br><span class="small">{w}</span></td>' for w in ["Super!", "Sehr gut!", "Gut.", "Es geht.", "Nicht so gut.", "Schlecht."])
    b.page(f"""{sec(1, "Einstieg: Wie geht’s?", "8 Min.")}
{sub("A", "Hör zu und sprich nach. Schreib.", "5 Min.", "02.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Und du? Wie geht’s dir heute? Kreuz an.", "3 Min.")}
<table class="ck"><tr>{me}</tr></table>""",
    30, """<ol><li>A: Track 02.2. Mit Gesichtern und Gesten zeigen: Daumen hoch = <b>Super! / Sehr gut!</b>, Schultern hoch = <b>Es geht.</b>, Daumen runter = <b>Schlecht.</b> Wiederholung aus Einheit 01: zuerst mit <i>Hallo! / Guten Morgen!</i> beginnen.</li>
<li>B: Die Lehrkraft fragt: <i>Wie geht’s?</i> Der Lernende zeigt auf das Wort und sagt es. Dann fragt der Lernende die Lehrkraft.</li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>Wie geht’s? 8 Antworten mit Fotos</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Rafaels zweiter Tag: drei kurze Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>sein</i> (Singular) · <i>Wie geht’s? / Wie geht es Ihnen?</i></td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>Das Alphabet · Namen buchstabieren</td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>Ergänzen, ordnen, verbinden</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Vier Personen: Wie geht’s? · Namen diktieren</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box"><h4>IMMER NOCH LANGSAM</h4>Neu sind nur drei Dinge: <i>Wie geht’s? / Wie geht es Ihnen?</i> mit Antworten, die vier Formen von <i>sein</i> im Singular und das Alphabet. Alles aus Einheit 01 (Grüße, <i>Ich heiße …</i>, <i>Wie heißt du?</i>) kommt wieder. Langsam sprechen, viel zeigen und wiederholen.</div>
<div class="box sand"><h4>DIE GESCHICHTE</h4>Rafaels zweiter Tag in Hamburg. Am Morgen trifft er wieder Herrn Schneider (Sie). In der Firma fragt Frau Krüger vom Empfang nach seinem Namen: Er buchstabiert <i>Costa</i>. Am Abend, im Café, ist er müde. Aylin stellt ihm Jonas vor, seinen Nachbarn. Jonas ist Student.</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4><i>Ich bin gut</i> ✗ (wie „Estou bem“) → <b>Gut, danke.</b> / <b>Mir geht’s gut.</b> Mit <i>Herr / Frau …</i>: <b>Wie geht es Ihnen?</b>, nicht <i>Wie geht’s?</i> Beim Alphabet: <b>E</b> = [e], <b>I</b> = [i], <b>J</b> = jott, <b>V</b> = fau, <b>W</b> = we, <b>Z</b> = tsett.</div>
<div class="box"><h4>AUDIO</h4>Track 02.1 Drei Dialoge (langsam und natürlich) · Track 02.2 Wie geht’s? · Track 02.3 Das Alphabet</div>""")

    # Seite 2
    gr = [("1", "Herr Schneider", ["Sehr gut.", "Schlecht."], "Sehr gut."), ("3", "Rafael", ["Super!", "Es geht."], "Es geht."), ("3", "Aylin", ["Super!", "Nicht so gut."], "Super!")]
    wr = "".join(f'<td style="width:33%"><b>Dialog {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Wie geht es", "Ihnen", "?"), ("Ja, ich", "bin", " Rafael Costa."), ("Wie", "schreibt", " man Costa?"),
          ("Es geht. Ich bin", "müde", "."), ("Das ist Jonas. Er", "ist", " Student."), ("Hallo, Rafael! Wie", "geht’s", "?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Rafaels zweiter Tag", "10 Min.")}
<p>Das ist Rafaels zweiter Tag in Hamburg. Er trifft Herrn Schneider, Frau Krüger, Aylin und Jonas.</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Hör zu. Wie geht’s? Wähle.", "3 Min.", "02.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu. Ergänze.", "5 Min.", "02.1 · NATURAL")}
<div class="bank">bin · geht’s · Ihnen · ist · müde · schreibt</div>
{twocol(gl, 4)}
{sub("C", "Lies die Dialoge mit der Lehrkraft.", "2 Min.")}""",
    30, """<ol><li>A: <b>langsame</b> Version, zweimal hören. Vorher fragen: <i>Wer ist das?</i> (Herr Schneider, Aylin aus Einheit 01). Neu: Frau Krüger (Empfang) und Jonas (Nachbar).</li>
<li>B: <b>natürliche</b> Version, nach jedem Dialog stoppen. Rafael buchstabiert <i>Costa</i>: kurz zeigen, das Alphabet kommt auf Seite 4.</li>
<li>C: Die Dialoge stehen auf der letzten Seite. Der Lernende ist Rafael, dann tauschen.</li></ol>""")

    # Seite 3
    sein = [("ich", "bin", "Ich bin Rafael."), ("du", "bist", "Bist du Jonas?"), ("er / sie", "ist", "Er ist Student."), ("Sie", "sind", "Sind Sie Herr Costa?")]
    ts = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in sein)
    who = [("Lena", "Kollegin", "Und dir?"), ("Herr Schneider", "Vermieter", "Und Ihnen?"), ("Jonas", "Nachbar", "Und dir?"), ("Frau Krüger", "Empfang", "Und Ihnen?")]
    wt = "".join(f'<td style="width:25%"><b>{n}</b><br><span class="small">{d}</span><br>{ch(["Und dir?", "Und Ihnen?"], a)}</td>' for n, d, a in who)
    b.page(f"""{sec(3, "Grammatik: sein · Wie geht’s?", "10 Min.")}
{sub("A", "Lies.", "3 Min.")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">sein</th></tr>{ts}</table></div>
<div><table style="margin:0"><tr><th>du</th><th>Sie</th></tr>
<tr><td>Wie <b>geht’s</b>?</td><td>Wie <b>geht es Ihnen</b>?</td></tr>
<tr><td>Gut, danke. Und <b>dir</b>?</td><td>Gut, danke. Und <b>Ihnen</b>?</td></tr></table></div></div>
<div class="box"><h4>ACHTUNG</h4>Wie geht’s? → <b>Gut, danke.</b> &nbsp;Nicht: <i>Ich bin gut.</i> &nbsp;·&nbsp; Aber: Ich <b>bin</b> müde. Ich <b>bin</b> krank.</div>
{sub("B", "dir oder Ihnen? Wähle.", "4 Min.")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "Und du? Schreib.", "3 Min.")}
<div class="two"><div class="wline">Wie geht’s? – {R("Gut, danke. / Es geht. / …")}</div><div class="wline">Ich bin {R("… (Name)")}</div></div>""",
    32, """<ol><li>A: Nur der Singular von <i>sein</i>; den Plural (wir, ihr, sie) gibt es später. Wiederholung: <i>du</i> = Freunde, <i>Sie</i> = Herr / Frau. <i>geht’s</i> = <i>geht es</i>.</li>
<li>Box: Der typische Fehler <i>Ich bin gut</i> kommt aus dem Portugiesischen („Estou bem“). Mit <i>sein</i>: Name, <i>müde</i>, <i>krank</i>.</li>
<li>B: Wie in Einheit 01: Kollege / Nachbar → du; Herr / Frau → Sie.</li></ol>""")

    # Seite 4
    abc = "".join(f'<td style="width:10%;text-align:center;padding:1.2mm 0.5mm{";background:#f3ead8" if l in HOT else ""}"><b style="font-size:12pt">{l}</b><br><span class="small">{n}</span></td>' + ("</tr><tr>" if (i + 1) % 10 == 0 and i < len(ABC) - 1 else "") for i, (l, n) in enumerate(ABC))
    names = ["Lena", "Aylin", "Jonas", "Krüger", "Hamburg", "dein Name"]
    b.page(f"""{sub("D", "Typische Fehler", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th></tr>
<tr><td>Wie geht’s? – Ich bin gut.</td><td><b>Gut, danke.</b></td></tr>
<tr><td>Er bist Jonas.</td><td><b>Er ist Jonas.</b></td></tr>
<tr><td>Wie geht’s, Herr Schneider?</td><td><b>Wie geht es Ihnen, Herr Schneider?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor: das Alphabet", "5 Min.")}
{audiocard(["02.3"])}
{sub("A", "Hör zu und sprich nach.", "3 Min.", "02.3")}
<table class="ck" style="table-layout:fixed"><tr>{abc}</tr></table>
<div class="box"><h4>ANDERS ALS IM PORTUGIESISCHEN</h4>Die farbigen Buchstaben: <b>E</b> [e] &nbsp;·&nbsp; <b>H</b> [ha] &nbsp;·&nbsp; <b>I</b> [i] &nbsp;·&nbsp; <b>J</b> [jott] &nbsp;·&nbsp; <b>V</b> [fau] &nbsp;·&nbsp; <b>W</b> [we] &nbsp;·&nbsp; <b>Y</b> [ypsilon] &nbsp;·&nbsp; <b>Z</b> [tsett]</div>
{sub("B", "Buchstabiere.", "2 Min.")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(names)}</div>""",
    32, """<ol><li>Fehler: <i>Ich bin gut</i> sofort korrigieren: <i>Gut, danke.</i></li>
<li>4A: Track 02.3 zweimal. Die farbigen Buchstaben sind für Brasilianer schwer: <b>E</b> wie „ê“, <b>I</b> wie „i“ (nicht „ai“), <b>J</b> = jott, <b>V</b> = fau, <b>W</b> = we, <b>Z</b> = tsett. <b>ß</b> = eszett.</li>
<li>4B: Der Lernende buchstabiert, die Lehrkraft schreibt mit. Dann umgekehrt. Bei Fehlern: <i>Wie bitte?</i></li></ol>""")

    # Seite 5
    gw = ["bin", "bist", "ist", "sind", "ist", "bin"]
    gs = [("Ich", " Rafael."), ("", " du Jonas?"), ("Das ist Aylin. Sie", " in Hamburg."), ("", " Sie Frau Krüger?"), ("Das ist Lena. Sie", " Kollegin."), ("Ich", " müde.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("es / Ihnen / geht / wie / ?", "Wie geht es Ihnen?"), ("danke / gut / ,", "Gut, danke."), ("man / wie / das / schreibt / ?", "Wie schreibt man das?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Wie geht’s?", "c", "Ja, ich bin Jonas."), ("Wie geht es Ihnen?", "d", "L – E – N – A."), ("Wie schreibt man das?", "b", "Gut, danke. Und dir?"), ("Bist du Jonas?", "a", "Sehr gut, danke. Und Ihnen?")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "Ergänze.", "3 Min.")}
<div class="bank">bin · bin · bist · ist · ist · sind</div>
{twocol(gl5, 4)}
{sub("B", "Ordne.", "2 Min.")}
<ol>{ol5}</ol>
{sub("C", "Verbinde.", "3 Min.")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Satz 3 und 5: <i>Sie</i> mit großem S am Satzanfang = <i>sie</i> (Aylin, Lena), nicht das formelle Sie: das Verb zeigt es (<i>ist</i>).</li>
<li>C: Die Paare danach laut lesen. Die Lehrkraft fragt, der Lernende antwortet.</li></ol>""")

    # Seite 6
    ppl = [("Lena", "Kollegin · Super!"), ("Herr Schneider", "Vermieter · Gut."), ("Jonas", "Nachbar · müde"), ("Frau Krüger", "Empfang · Es geht.")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + ("Wie geht es Ihnen?" if "Herr" in n or "Frau" in n else "Wie geht’s?"))}</div>' for n, d in ppl)
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Spiel mit der Lehrkraft. Begrüße die Person. Frag: Wie geht’s?", "7 Min.")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> Guten Morgen, Herr Schneider! Wie geht es Ihnen?<br><b>B:</b> Gut, danke. Und Ihnen?<br><b>A:</b> Es geht. Ich bin müde.</div>
{sub("B", "Hör zu und schreib die Namen.", "5 Min.")}
<ol style="line-height:2"><li>{A("MÜLLER", "min-width:55mm")}</li><li>{A("BECKER", "min-width:55mm")}</li><li>{A("WAGNER", "min-width:55mm")}</li><li>{A("ZIEGLER", "min-width:55mm")}</li></ol>""",
    30, """<ol><li>A: Die Lehrkraft spielt die vier Personen und antwortet wie auf der Karte. Der Lernende wählt <i>Wie geht’s?</i> oder <i>Wie geht es Ihnen?</i> Dann tauschen.</li>
<li>B: Die Lehrkraft buchstabiert langsam (zweimal): M-Ü-L-L-E-R, B-E-C-K-E-R, W-A-G-N-E-R, Z-I-E-G-L-E-R. Der Lernende schreibt und liest den Namen laut. Fragen üben: <i>Wie bitte? Noch einmal, bitte.</i></li></ol>""")

    # Seite 7
    pc = [("Einheit 01", "Ich kann begrüßen und meinen Namen sagen."), ("Einheit 02", "Ich kann fragen: Wie geht’s? / Wie geht es Ihnen?"),
          ("Einheit 02", "Ich kann sagen, wie es mir geht."), ("Einheit 02", "Ich kann meinen Namen buchstabieren.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. Ergänze den Dialog.</b></p>
<div class="msg"><b>Jonas:</b> Hallo, Rafael! Wie geht’s?<br><b>Rafael:</b> {A("Gut, danke. Und dir?", "min-width:60mm")}<br><b>Jonas:</b> Super, danke!<br><br>
<b>Rafael:</b> Guten Tag, Frau Krüger! Wie geht es Ihnen?<br><b>Frau Krüger:</b> {A("Sehr gut, danke. Und Ihnen?", "min-width:60mm")}<br><b>Rafael:</b> {A("Es geht. Ich bin müde.", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>2. Ergänze: bin, bist, ist oder sind?</b> &nbsp; Ich {A("bin", "min-width:12mm")} Lena. · {A("Bist", "min-width:12mm")} du Jonas? · Er {A("ist", "min-width:12mm")} Student. · {A("Sind", "min-width:12mm")} Sie Herr Schneider?</p>
<p style="margin-top:2mm"><b>3. Schreib deinen Namen und deine Stadt.</b> Buchstabiere sie in der nächsten Stunde.</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Nächste Stunde: mit <i>Hallo! Wie geht’s?</i> beginnen. Der Lernende buchstabiert Namen und Stadt aus Aufgabe 3, die Lehrkraft schreibt mit. In Einheit 03 kommen die Länder: <i>Woher kommst du?</i></p>""")

    b.extra("Hörtexte", f"""
{sub("02.1", "Rafaels zweiter Tag (langsam und natürlich)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "Wie geht’s?")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "Das Alphabet")}
<p>{" · ".join(f"{l} ({n})" for l, n in ABC)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 02 - Wie geht's")
