# Speak! Essenziell A1 - Einheit 02 "Woher kommst du?" (alles auf Deutsch, für absolute Anfänger; Menschen A1, L1) - shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 02", audio_json=os.path.join(HERE, "audio_de-a1-einheit-02.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

PHOTOS = [("A", "Brasilien", "brasilien"), ("B", "Deutschland", "deutschland"), ("C", "Österreich", "österreich"), ("D", "Italien", "italien"),
          ("E", "Spanien", "spanien"), ("F", "Portugal", "portugal"), ("G", "Frankreich", "frankreich"), ("H", "Japan", "japan")]

SCRIPT = [("Erzählerin", "Dialog eins."), ("Frau Krüger", "Guten Tag! Wie heißen Sie?"), ("Rafael", "Rafael Costa."),
          ("Frau Krüger", "Wie schreibt man das?"), ("Rafael", "C – O – S – T – A."), ("Frau Krüger", "Danke. Woher kommen Sie, Herr Costa?"),
          ("Rafael", "Ich komme aus Brasilien."),
          ("Erzählerin", "Dialog zwei."), ("Lena", "Hallo, Rafael! Wie geht’s?"), ("Rafael", "Gut, danke. Und dir?"),
          ("Lena", "Super! Sag mal, wo wohnst du?"), ("Rafael", "Ich wohne in Altona."), ("Lena", "Ich wohne auch in Altona!"),
          ("Erzählerin", "Dialog drei."), ("Aylin", "Hallo, Rafael! Das ist Jonas."), ("Jonas", "Hallo! Woher kommst du?"),
          ("Rafael", "Ich komme aus Brasilien. Und du?"), ("Jonas", "Ich komme aus Österreich, aus Wien.")]
S022 = ["Brasilien", "Deutschland", "Österreich", "Italien", "Spanien", "Portugal", "Frankreich", "Japan"]
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
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 02", "Woher kommst du?", "Herkunft und Wohnort · das Alphabet",
                       [("DU KANNST", "sagen, woher du kommst und wo du wohnst, und deinen Namen buchstabieren"),
                        ("SPRACHE", "Woher kommst du? – Ich komme aus … · Wo wohnst du? – Ich wohne in … · sein: ich bin, du bist, er / sie ist, Sie sind"),
                        ("AUSSPRACHE", "Länder · das Alphabet")])
    words = ["Brasilien", "Deutschland", "Frankreich", "Italien", "Japan", "Österreich", "Portugal", "Spanien"]
    b.page(f"""{sec(1, "Einstieg: Länder", "8 Min.")}
{sub("A", "Hör zu und sprich nach. Schreib.", "5 Min.", "02.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Und du? Ergänze.", "3 Min.")}
<div class="two"><div class="wline">Ich komme aus {R("Brasilien.")}</div><div class="wline">Ich wohne in {R("… (Stadt)")}</div></div>""",
    30, """<ol><li>A: Track 02.2. Die Lehrkraft zeigt auf jedes Foto: <i>Das ist Rio. Rio ist in … Brasilien!</i> Der Lernende spricht nach und schreibt das Land. Wiederholung aus Einheit 01 zuerst: <i>Hallo! Wie geht’s?</i></li>
<li>B: Vorlesen und zeigen: <i>Ich komme aus Brasilien. Ich wohne in Curitiba.</i> Der Lernende ergänzt mit seinem Land und seiner Stadt und sagt es laut.</li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>8 Länder mit Fotos</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Rafaels zweiter Tag: drei kurze Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>kommen aus</i> · <i>wohnen in</i> · <i>sein</i> (Singular) · wer, wie, woher, wo</td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>Das Alphabet · Namen buchstabieren</td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>Ergänzen, ordnen, verbinden</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Vier Personen: Woher? Wo? · Namen diktieren</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box"><h4>IMMER NOCH LANGSAM</h4>Neu sind: <i>Woher kommst du? – Ich komme aus …</i>, <i>Wo wohnst du? – Ich wohne in …</i>, die vier Formen von <i>sein</i> im Singular und das Alphabet. Alles aus Einheit 01 (Grüße, <i>Ich heiße …</i>, <i>Wie geht’s?</i>) kommt wieder. Langsam sprechen, viel zeigen und wiederholen.</div>
<div class="box sand"><h4>DIE GESCHICHTE</h4>Rafaels zweiter Tag in Hamburg. In der Firma fragt Frau Krüger vom Empfang nach seinem Namen: Er buchstabiert <i>Costa</i>. Lena fragt, wo er wohnt: in Altona, wie sie! Am Abend im Café lernt er Jonas kennen, seinen Nachbarn. Jonas kommt aus Österreich, aus Wien.</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4>„De onde?“ = <b>Woher?</b> (nicht <i>Wo?</i>). „Sou do Brasil“ = <b>Ich komme aus Brasilien</b> (nicht <i>von</i>). „Moro em“ = <b>Ich wohne in</b>. Beim Alphabet: <b>E</b> = [e], <b>I</b> = [i], <b>J</b> = jott, <b>V</b> = fau, <b>W</b> = we, <b>Z</b> = tsett.</div>
<div class="box"><h4>AUDIO</h4>Track 02.1 Drei Dialoge (langsam und natürlich) · Track 02.2 Länder · Track 02.3 Das Alphabet</div>""")

    # Seite 2
    gr = [("Rafael kommt aus …", ["Brasilien", "Portugal"], "Brasilien"), ("Rafael wohnt in …", ["Altona", "Berlin"], "Altona"),
          ("Jonas kommt aus …", ["Deutschland", "Österreich"], "Österreich")]
    wr = "".join(f'<td style="width:33%"><span class="small">{q}</span><br>{ch(o, a)}</td>' for q, o, a in gr)
    gp = [("Wie schreibt", "man", " das?"), ("Woher", "kommen", " Sie?"), ("Ich komme", "aus", " Brasilien."),
          ("Wo", "wohnst", " du?"), ("Ich wohne", "in", " Altona."), ("Woher", "kommst", " du?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Rafaels zweiter Tag", "10 Min.")}
<p>Rafael ist in der Firma und im Café. Er spricht mit Frau Krüger, Lena und Jonas.</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Hör zu. Wähle.", "3 Min.", "02.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu. Ergänze.", "5 Min.", "02.1 · NATURAL")}
<div class="bank">aus · in · kommen · kommst · man · wohnst</div>
{twocol(gl, 4)}
{sub("C", "Lies die Dialoge mit der Lehrkraft.", "2 Min.")}""",
    30, """<ol><li>A: <b>langsame</b> Version, zweimal hören. Vorher fragen: <i>Wer ist das?</i> (Lena, Aylin aus Einheit 01). Neu: Frau Krüger (Empfang, Sie) und Jonas (Nachbar, du). <b>Altona</b> ist ein Stadtteil von Hamburg.</li>
<li>B: <b>natürliche</b> Version, nach jedem Dialog stoppen. Rafael buchstabiert <i>Costa</i>: kurz zeigen, das Alphabet kommt auf Seite 4.</li>
<li>C: Die Dialoge stehen auf der letzten Seite. Der Lernende ist Rafael, dann tauschen.</li></ol>""")

    # Seite 3
    rows = [("<b>Woher</b> kommst du?", "<b>Woher</b> kommen Sie?", "Ich komme <b>aus</b> Brasilien."),
            ("<b>Wo</b> wohnst du?", "<b>Wo</b> wohnen Sie?", "Ich wohne <b>in</b> Hamburg.")]
    tr_ = "".join(f"<tr><td>{a}</td><td>{c}</td><td>{d}</td></tr>" for a, c, d in rows)
    sein = [("ich", "bin"), ("du", "bist"), ("er / sie", "ist"), ("Sie", "sind")]
    ts = "".join(f"<td style='text-align:center'>{p}<br><b>{v}</b></td>" for p, v in sein)
    ai = [("Ich komme", "aus", "Brasilien."), ("Ich wohne", "in", "Hamburg."), ("Jonas kommt", "aus", "Wien."), ("Lena wohnt", "in", "Altona.")]
    al = "".join(f'<li>{a} {ch(["aus", "in"], x)} {c}</li>' for a, x, c in ai)
    b.page(f"""{sec(3, "Grammatik: Woher? Wo?", "10 Min.")}
{sub("A", "Lies.", "3 Min.")}
<table style="margin:0"><tr><th>du</th><th>Sie</th><th>ich</th></tr>{tr_}</table>
<div class="two" style="margin-top:2mm"><div><table style="margin:0"><tr><th colspan="4">sein</th></tr><tr>{ts}</tr></table>
<p class="small" style="margin-top:1mm">Ich <b>bin</b> Rafael. · <b>Bist</b> du Jonas? · Das <b>ist</b> Lena. · <b>Sind</b> Sie Frau Krüger?</p></div>
<div class="box" style="margin:0"><h4>W-FRAGEN</h4><b>Wer</b> ist das? &nbsp;·&nbsp; <b>Wie</b> heißt du? &nbsp;·&nbsp; <b>Woher</b> kommst du? &nbsp;·&nbsp; <b>Wo</b> wohnst du?</div></div>
{sub("B", "aus oder in? Wähle.", "4 Min.")}
<ol>{al}</ol>
{sub("C", "Und du? Schreib.", "3 Min.")}
<div class="two"><div class="wline">Ich komme aus {R("…")}</div><div class="wline">Ich wohne in {R("…")}</div></div>""",
    32, """<ol><li>A: <b>aus</b> = Herkunft (<i>de</i>), <b>in</b> = Wohnort (<i>em</i>). <i>kommen</i> und <i>wohnen</i> nur mit <i>ich / du / Sie</i>; die anderen Formen kommen später. <i>sein</i>: nur Singular.</li>
<li>W-Fragen: Mit den Händen zeigen: <i>Woher?</i> (von dort hierher), <i>Wo?</i> (hier). Typischer Fehler: <i>Wo kommst du?</i></li>
<li>B/C: Laut lesen lassen. C: Der Lernende sagt die Sätze auch mündlich.</li></ol>""")

    # Seite 4
    abc = "".join(f'<td style="width:10%;text-align:center;padding:1.2mm 0.5mm{";background:#f3ead8" if l in HOT else ""}"><b style="font-size:12pt">{l}</b><br><span class="small">{n}</span></td>' + ("</tr><tr>" if (i + 1) % 10 == 0 and i < len(ABC) - 1 else "") for i, (l, n) in enumerate(ABC))
    names = ["Lena", "Jonas", "Wien", "Altona", "Hamburg", "dein Name"]
    b.page(f"""{sub("D", "Typische Fehler", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th></tr>
<tr><td>Wo kommst du?</td><td><b>Woher kommst du?</b></td></tr>
<tr><td>Ich komme von Brasilien.</td><td><b>Ich komme aus Brasilien.</b></td></tr>
<tr><td>Ich wohne aus Hamburg.</td><td><b>Ich wohne in Hamburg.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor: das Alphabet", "5 Min.")}
{audiocard(["02.2", "02.3"])}
{sub("A", "Hör zu und sprich nach.", "3 Min.", "02.3")}
<table class="ck" style="table-layout:fixed"><tr>{abc}</tr></table>
<div class="box"><h4>ANDERS ALS IM PORTUGIESISCHEN</h4>Die farbigen Buchstaben: <b>E</b> [e] &nbsp;·&nbsp; <b>H</b> [ha] &nbsp;·&nbsp; <b>I</b> [i] &nbsp;·&nbsp; <b>J</b> [jott] &nbsp;·&nbsp; <b>V</b> [fau] &nbsp;·&nbsp; <b>W</b> [we] &nbsp;·&nbsp; <b>Y</b> [ypsilon] &nbsp;·&nbsp; <b>Z</b> [tsett]</div>
{sub("B", "Buchstabiere.", "2 Min.")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(names)}</div>""",
    32, """<ol><li>Fehler: <i>Wo kommst du?</i> kommt aus dem Portugiesischen („De onde…?“ → nur <i>Wo</i> gehört). Mit Gesten korrigieren.</li>
<li>4A: Track 02.3 zweimal. Die farbigen Buchstaben sind für Brasilianer schwer: <b>E</b> wie „ê“, <b>I</b> wie „i“ (nicht „ai“), <b>J</b> = jott, <b>V</b> = fau, <b>W</b> = we, <b>Z</b> = tsett. <b>ß</b> = eszett. Track 02.2 (Länder) gehört zu Seite 1.</li>
<li>4B: Der Lernende buchstabiert, die Lehrkraft schreibt mit. Dann umgekehrt. Bei Fehlern: <i>Wie bitte?</i></li></ol>""")

    # Seite 5
    gw = ["kommst", "komme", "wohnen", "wohne", "bist", "ist"]
    gs = [("Woher", " du, Jonas?"), ("Ich", " aus Österreich."), ("Wo", " Sie, Frau Krüger?"), ("Ich", " in Hamburg."), ("", " du Lena?"), ("Wer", " das? – Das ist Aylin.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("kommen / woher / Sie / ?", "Woher kommen Sie?"), ("wohne / Hamburg / ich / in", "Ich wohne in Hamburg."), ("ist / wer / das / ?", "Wer ist das?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Wer ist das?", "c", "Aus Brasilien."), ("Woher kommst du?", "a", "In Hamburg."), ("Wo wohnen Sie?", "b", "Das ist Jonas."), ("Wie schreibt man das?", "d", "J – O – N – A – S.")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "Ergänze.", "3 Min.")}
<div class="bank">bist · ist · komme · kommst · wohne · wohnen</div>
{twocol(gl5, 4)}
{sub("B", "Ordne.", "2 Min.")}
<ol>{ol5}</ol>
{sub("C", "Verbinde.", "3 Min.")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Endungen nur zeigen: <i>ich komm<b>e</b>, du komm<b>st</b>, Sie komm<b>en</b></i>. Satz 5: Ja/Nein-Frage, das Verb steht vorne (<i>Bist du …?</i>).</li>
<li>C: Die Paare danach laut lesen. Die Lehrkraft fragt, der Lernende antwortet.</li></ol>""")

    # Seite 6
    ppl = [("Lena", "Deutschland · wohnt in Hamburg", "du"), ("Jonas", "Österreich (Wien) · wohnt in Hamburg", "du"),
           ("Herr Schneider", "Deutschland (München) · wohnt in Hamburg", "Sie"), ("Frau Tanaka", "Japan (Tokio) · wohnt in Berlin", "Sie")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + s + ": " + ("Woher kommst du? Wo wohnst du?" if s == "du" else "Woher kommen Sie? Wo wohnen Sie?"))}</div>' for n, d, s in ppl)
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Spiel mit der Lehrkraft. Frag: Wie heißt du? Woher kommst du? Wo wohnst du?", "7 Min.")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> Guten Tag! Wie heißen Sie?<br><b>B:</b> Ich heiße Yuki Tanaka.<br><b>A:</b> Woher kommen Sie?<br><b>B:</b> Ich komme aus Japan, aus Tokio.<br><b>A:</b> Und wo wohnen Sie?<br><b>B:</b> Ich wohne in Berlin.</div>
{sub("B", "Hör zu und schreib die Namen.", "5 Min.")}
<ol style="line-height:2"><li>{A("MÜLLER", "min-width:55mm")}</li><li>{A("BECKER", "min-width:55mm")}</li><li>{A("WAGNER", "min-width:55mm")}</li><li>{A("ZIEGLER", "min-width:55mm")}</li></ol>""",
    30, """<ol><li>A: Die Lehrkraft spielt die vier Personen und antwortet wie auf der Karte. Der Lernende wählt du oder Sie. Dann tauschen: Der Lernende antwortet mit seinen eigenen Daten.</li>
<li>B: Die Lehrkraft buchstabiert langsam (zweimal): M-Ü-L-L-E-R, B-E-C-K-E-R, W-A-G-N-E-R, Z-I-E-G-L-E-R. Der Lernende schreibt und liest den Namen laut. Üben: <i>Wie bitte? Noch einmal, bitte.</i></li></ol>""")

    # Seite 7
    pc = [("Einheit 01", "Ich kann begrüßen und fragen: Wie geht’s?"), ("Einheit 02", "Ich kann sagen, woher ich komme."),
          ("Einheit 02", "Ich kann sagen, wo ich wohne."), ("Einheit 02", "Ich kann meinen Namen buchstabieren.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. Ergänze den Dialog.</b></p>
<div class="msg"><b>Jonas:</b> Hallo! Ich bin Jonas. Wie heißt du?<br><b>Du:</b> {A("Hallo! Ich heiße …", "min-width:60mm")}<br><b>Jonas:</b> Woher kommst du?<br><b>Du:</b> {A("Ich komme aus Brasilien.", "min-width:60mm")}<br><b>Jonas:</b> Und wo wohnst du?<br><b>Du:</b> {A("Ich wohne in …", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>2. Ergänze: aus oder in?</b> &nbsp; Rafael kommt {A("aus", "min-width:12mm")} Brasilien. · Er wohnt {A("in", "min-width:12mm")} Hamburg. · Jonas kommt {A("aus", "min-width:12mm")} Wien.</p>
<p style="margin-top:2mm"><b>3. Schreib deinen Namen und deine Stadt.</b> Buchstabiere sie in der nächsten Stunde.</p>
<div class="wline"></div><div class="wline"></div>""",
    22, """<p>Nächste Stunde: mit <i>Hallo! Wie geht’s? Woher kommst du?</i> beginnen. Der Lernende buchstabiert Namen und Stadt aus Aufgabe 3, die Lehrkraft schreibt mit. In Einheit 03 kommen Beruf, Alter und <i>haben</i>.</p>""")

    b.extra("Hörtexte", f"""
{sub("02.1", "Rafaels zweiter Tag (langsam und natürlich)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "Länder")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "Das Alphabet")}
<p>{" · ".join(f"{l} ({n})" for l, n in ABC)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 02 - Woher kommst du")
