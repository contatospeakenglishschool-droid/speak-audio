# Speak! Essenziell A1 - Einheit 01 "Hallo!" (alles auf Deutsch, für absolute Anfänger) - built with the shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 01", audio_json=os.path.join(HERE, "audio_de-a1-einheit-01.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

PHOTOS = [("A", "Hallo!", "hallo"), ("B", "Guten Morgen!", "guten morgen"), ("C", "Guten Tag!", "guten tag"), ("D", "Guten Abend!", "guten abend"),
          ("E", "Gute Nacht!", "gute nacht"), ("F", "Auf Wiedersehen!", "auf wiedersehen"), ("G", "Tschüss!", "tschüss"), ("H", "Freut mich!", "freut mich")]

SCRIPT = [("Erzählerin", "Dialog eins."), ("Herr Schneider", "Guten Morgen! Ich bin Klaus Schneider. Wie heißen Sie?"),
          ("Rafael", "Guten Morgen! Ich heiße Rafael Costa."), ("Herr Schneider", "Freut mich, Herr Costa."), ("Rafael", "Freut mich auch!"),
          ("Erzählerin", "Dialog zwei."), ("Lena", "Hallo! Ich heiße Lena. Wie heißt du?"), ("Rafael", "Hallo, Lena! Ich bin Rafael."), ("Lena", "Freut mich, Rafael!"),
          ("Erzählerin", "Dialog drei."), ("Aylin", "Guten Abend!"), ("Rafael", "Guten Abend! Ich bin Rafael."),
          ("Aylin", "Hallo, Rafael! Ich bin Aylin. Freut mich!"), ("Rafael", "Freut mich auch! Tschüss, Aylin!"), ("Aylin", "Tschüss! Bis morgen!")]
S012 = ["Hallo", "Guten Morgen", "Guten Tag", "Guten Abend", "Gute Nacht", "Tschüss", "Auf Wiedersehen", "Freut mich"]
S013 = ["Ich heiße Rafael.", "Ich bin Lena.", "Wie heißt du?", "Wie heißen Sie?", "Freut mich!", "Freut mich auch!"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Seite 1
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 01", "Hallo!", "Begrüßen und den Namen sagen",
                       [("DU KANNST", "Hallo sagen, deinen Namen sagen und nach dem Namen fragen"),
                        ("SPRACHE", "Ich heiße … · Ich bin … · Wie heißt du? · Wie heißen Sie?"),
                        ("AUSSPRACHE", "Grüße · ei / ie · ü")])
    words = ["Auf Wiedersehen!", "Freut mich!", "Gute Nacht!", "Guten Abend!", "Guten Morgen!", "Guten Tag!", "Hallo!", "Tschüss!"]
    qs = [("08:00", "Guten Morgen!"), ("13:00", "Guten Tag!"), ("19:00", "Guten Abend!"), ("23:00", "Gute Nacht!")]
    cl = "".join(f'<td style="width:25%;text-align:center"><b style="font-size:13pt">{t}</b><br>{A(a, "min-width:30mm")}</td>' for t, a in qs)
    b.page(f"""{sec(1, "Einstieg: Hallo!", "8 Min.")}
{sub("A", "Hör zu und sprich nach. Schreib.", "5 Min.", "01.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Wie spät ist es? Schreib.", "3 Min.")}
<table class="ck"><tr>{cl}</tr></table>""",
    30, """<ol><li>A: Track 01.2. Die Lehrkraft zeigt auf jedes Foto, spielt das Wort vor, der Lernende spricht nach und schreibt. Langsam, mit Gesten (Hand heben, Hand geben). Viel wiederholen.</li>
<li>B: Mit der Uhr zeigen: <b>Guten Morgen</b> bis ca. 10–11 Uhr, dann <b>Guten Tag</b>, ab ca. 18 Uhr <b>Guten Abend</b>, <b>Gute Nacht</b> nur vor dem Schlafen. <b>Tschüss</b> = informell, <b>Auf Wiedersehen</b> = formell. Info: In Hamburg sagt man auch <b>Moin!</b></li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>8 Grüße mit Fotos und Uhrzeiten</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Rafael in Hamburg: drei kurze Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>Ich heiße … / Ich bin …</i> · <i>Wie heißt du? / Wie heißen Sie?</i></td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>Sätze nachsprechen · ei / ie · ü</td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>Ergänzen, ordnen, verbinden</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Vier Personen begrüßen · Fragen der Lehrkraft</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box"><h4>ERSTE STUNDE: LANGSAM!</h4>Der Lernende hat noch nie Deutsch gehört. Langsam sprechen, viel zeigen (Fotos, Gesten, Uhr), jede Struktur oft wiederholen. Die Arbeitsanweisungen sind kurz und kommen immer wieder: <i>Hör zu. Sprich nach. Schreib. Ergänze. Verbinde.</i> Die Lehrkraft liest sie vor und zeigt, was zu tun ist. Ziel der Stunde: Grüße, den eigenen Namen sagen und nach dem Namen fragen. Nicht mehr.</div>
<div class="box sand"><h4>DIE GESCHICHTE BEGINNT</h4>Rafael Costa kommt aus Curitiba und wohnt jetzt in Hamburg. Am Morgen lernt er seinen Vermieter kennen, Herrn Schneider (Sie). In der Firma lernt er Lena kennen, eine Kollegin (du). Am Abend, im Café, lernt er Aylin kennen.</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4><i>Bin Rafael</i> ✗ → <b>Ich bin Rafael</b>: Im Deutschen steht <i>ich</i> immer da. <i>Ich heißen</i> ✗ → <b>Ich heiße</b>. Und zu <i>Herr / Frau …</i> sagt man <b>Sie</b>: <i>Wie heißen Sie?</i></div>
<div class="box"><h4>AUDIO</h4>Track 01.1 Drei Dialoge (langsam und natürlich) · Track 01.2 Grüße · Track 01.3 Sätze</div>""")

    # Seite 2
    gr = [("1", "Rafael und Herr Schneider", ["Hallo!", "Guten Morgen!"], "Guten Morgen!"), ("2", "Rafael und Lena", ["Hallo!", "Guten Abend!"], "Hallo!"),
          ("3", "Rafael und Aylin", ["Guten Morgen!", "Guten Abend!"], "Guten Abend!")]
    wr = "".join(f'<td style="width:33%"><b>Dialog {n}</b><br><span class="small">{p}</span><br>{ch(o, a)}</td>' for n, p, o, a in gr)
    gp = [("Ich", "bin", " Klaus Schneider."), ("Wie", "heißen", " Sie?"), ("Ich", "heiße", " Rafael Costa."),
          ("Wie", "heißt", " du?"), ("", "Freut", " mich!"), ("", "Tschüss", ", Aylin!")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Rafael in Hamburg", "10 Min.")}
<p>Das ist Rafael. Er kommt aus Brasilien. Er wohnt in Hamburg.</p>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL"])}
{sub("A", "Hör zu. Wähle.", "3 Min.", "01.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu. Ergänze.", "5 Min.", "01.1 · NATURAL")}
<div class="bank">bin · Freut · heiße · heißen · heißt · Tschüss</div>
{twocol(gl, 3)}
{sub("C", "Lies die Dialoge mit der Lehrkraft.", "2 Min.")}""",
    30, """<ol><li>A: <b>langsame</b> Version, zweimal hören. Vor dem Hören die drei Fotos von Seite 1 (B, A, D) zeigen: Morgen, Büro, Abend.</li>
<li>B: <b>natürliche</b> Version. Wörter aus dem Kasten. Nach jedem Dialog stoppen.</li>
<li>C: Die Dialoge stehen auf der letzten Seite des Handbuchs. Die Lehrkraft liest sie vor, der Lernende ist Rafael. Dann tauschen.</li></ol>""")

    # Seite 3
    who = [("Lena", "Kollegin", "Wie heißt du?"), ("Herr Schneider", "Vermieter", "Wie heißen Sie?"), ("Jonas", "Nachbar, 22 Jahre", "Wie heißt du?"), ("Frau Weber", "Ärztin", "Wie heißen Sie?")]
    wt = "".join(f'<td style="width:25%"><b>{n}</b><br><span class="small">{d}</span><br>{ch(["Wie heißt du?", "Wie heißen Sie?"], a)}</td>' for n, d, a in who)
    b.page(f"""{sec(3, "Grammatik: Ich heiße … / Wie heißt du?", "10 Min.")}
{sub("A", "Lies.", "3 Min.")}
<div class="two"><div><table style="margin:0"><tr><th colspan="2">Mein Name</th></tr>
<tr><td>Ich <b>heiße</b> Rafael.</td><td>Ich <b>bin</b> Rafael.</td></tr>
<tr><td>Ich <b>heiße</b> Lena.</td><td>Ich <b>bin</b> Lena.</td></tr></table></div>
<div><table style="margin:0"><tr><th colspan="2">Die Frage</th></tr>
<tr><td><b>du</b></td><td>Wie <b>heißt du</b>?</td></tr>
<tr><td><b>Sie</b></td><td>Wie <b>heißen Sie</b>?</td></tr></table></div></div>
<div class="box"><h4>DU ODER SIE?</h4><b>du</b> = Freunde, Kollegen, junge Leute. &nbsp; <b>Sie</b> = Herr …, Frau … &nbsp; <b>Sie</b> immer mit großem S.</div>
{sub("B", "du oder Sie? Wähle die Frage.", "4 Min.")}
<table class="ck"><tr>{wt}</tr></table>
{sub("C", "Schreib deinen Namen.", "3 Min.")}
<div class="two"><div class="wline">Ich heiße {R("…")}</div><div class="wline">Ich bin {R("…")}</div></div>""",
    32, """<ol><li>A: <i>Ich heiße …</i> und <i>Ich bin …</i> bedeuten hier dasselbe. Nur diese zwei Formen und die zwei Fragen üben, keine ganze Konjugation (die kommt später). Der Lernende liest laut.</li>
<li>B: Mit Gesten zeigen: Freund = du, Herr / Frau = Sie. Bei Jonas: jung, Nachbar → du.</li>
<li>C: Den Lernenden seinen Namen laut sagen lassen: <i>Ich heiße …</i></li></ol>""")

    # Seite 4
    b.page(f"""{sub("D", "Typische Fehler", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th></tr>
<tr><td>Bin Rafael.</td><td><b>Ich bin Rafael.</b></td></tr>
<tr><td>Ich heißen Rafael.</td><td><b>Ich heiße Rafael.</b></td></tr>
<tr><td>Wie heißt du, Herr Schneider?</td><td><b>Wie heißen Sie, Herr Schneider?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor", "5 Min.")}
{audiocard(["01.2", "01.3"])}
{sub("A", "Hör zu und sprich nach.", "2 Min.", "01.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S012)}</div>
{sub("B", "Hör zu und sprich nach.", "3 Min.", "01.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S013)}</div>
<div class="box"><h4>LAUTE</h4><b>ei</b> = [ai]: <i>h<b>ei</b>ße</i> &nbsp;·&nbsp; <b>ie</b> = [i:]: <i>S<b>ie</b>, w<b>ie</b></i> &nbsp;·&nbsp; <b>ü</b>: <i>Tsch<b>ü</b>ss</i> &nbsp;·&nbsp; <b>ß</b> = ss: <i>hei<b>ß</b>e</i></div>""",
    36, """<ol><li>Fehler: <i>Bin Rafael</i> ist der häufigste Fehler (im Portugiesischen fehlt das Subjekt oft: „Sou Rafael“). Freundlich korrigieren, die Hand auf die Brust legen: <i>ICH bin …</i></li>
<li>4A/4B: Jedes Wort zweimal nachsprechen. <b>ei</b> klingt wie „ai“, <b>ie</b> wie ein langes „i“. <b>ü</b>: Lippen rund wie bei „u“, Zunge wie bei „i“. Das <b>ß</b> nur zeigen, nicht erklären.</li></ol>""")

    # Seite 5
    gw = ["heiße", "bin", "heißt", "heißen", "heiße", "bin"]
    gs = [("Ich", "Lena."), ("Ich", "Rafael."), ("Wie", "du?"), ("Wie", "Sie?"), ("Ich", "Klaus Schneider."), ("Hallo! Ich", "Aylin.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")} {c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("heiße / ich / Jonas", "Ich heiße Jonas."), ("du / heißt / wie / ?", "Wie heißt du?"), ("Sie / wie / heißen / ?", "Wie heißen Sie?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Guten Morgen!", "c", "Ich heiße Jonas."), ("Wie heißt du?", "a", "Freut mich auch!"), ("Freut mich!", "b", "Guten Morgen!"), ("Tschüss!", "d", "Tschüss!")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "Ergänze.", "3 Min.")}
<div class="bank">bin · bin · heiße · heiße · heißen · heißt</div>
{twocol(gl5, 3)}
{sub("B", "Ordne.", "2 Min.")}
<ol>{ol5}</ol>
{sub("C", "Verbinde.", "3 Min.")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: In 1, 2, 5 und 6 sind <i>heiße</i> und <i>bin</i> beide richtig: beide akzeptieren.</li>
<li>B: Zeigen: Bei der Frage steht <i>wie</i> vorne. C: Die Paare danach laut lesen, die Lehrkraft spielt die erste Person.</li></ol>""")

    # Seite 6
    ppl = [("Lena", "Kollegin · 9:00 Uhr", "du · Hallo! / Guten Morgen!"), ("Herr Schneider", "Vermieter · 8:00 Uhr", "Sie · Guten Morgen!"),
           ("Jonas", "Nachbar · 19:00 Uhr", "du · Hallo! / Guten Abend!"), ("Frau Weber", "Ärztin · 14:00 Uhr", "Sie · Guten Tag!")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + a)}</div>' for n, d, a in ppl)
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Spiel mit der Lehrkraft. Begrüße die Person. Sag deinen Namen. Frag nach dem Namen.", "7 Min.")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="bank" style="background:#fff">Hallo! / Guten Morgen! / Guten Tag! / Guten Abend! · Ich heiße … · Wie heißt du? / Wie heißen Sie? · Freut mich! · Tschüss! / Auf Wiedersehen!</div>
<div class="msg"><b>A:</b> Guten Morgen! Ich heiße … Wie heißen Sie?<br><b>B:</b> Guten Morgen! Ich bin … <br><b>A:</b> Freut mich!<br><b>B:</b> Freut mich auch! … Auf Wiedersehen!</div>
{sub("B", "Antworte der Lehrkraft.", "5 Min.")}
<ol style="line-height:1.8"><li>Hallo! Wie heißt du?</li><li>Guten Tag! Wie heißen Sie?</li><li>Freut mich!</li><li>Tschüss!</li></ol>""",
    28, """<ol><li>A: Die Lehrkraft spielt die vier Personen (mit Namenskarte oder Foto). Der Lernende folgt dem Modell im Kasten. Dann tauschen: Der Lernende ist Herr Schneider, die Lehrkraft Rafael.</li>
<li>B: Die Lehrkraft fragt, der Lernende antwortet frei. Erwartete Antworten: <i>Ich heiße … · Freut mich auch! · Tschüss!</i> Fehler wie <i>Bin …</i> sofort korrigieren.</li></ol>""")

    # Seite 7
    pc = [("Einheit 01", "Ich kann Hallo sagen (morgens, mittags, abends)."), ("Einheit 01", "Ich kann meinen Namen sagen."),
          ("Einheit 01", "Ich kann nach dem Namen fragen (du und Sie).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("07:00", "Guten Morgen!"), ("15:00", "Guten Tag!"), ("20:00", "Guten Abend!"), ("23:30", "Gute Nacht!")]
    hl = [f'<li value="{i+1}"><b>{t}</b> {A(a, "min-width:32mm")}</li>' for i, (t, a) in enumerate(hw)]
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. Schreib den Gruß.</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Ergänze den Dialog.</b></p>
<div class="msg"><b>A:</b> Hallo! Ich heiße Lena. Wie heißt du?<br><b>B:</b> {A("Hallo! Ich heiße …", "min-width:60mm")}<br><b>A:</b> Freut mich!<br><b>B:</b> {A("Freut mich auch!", "min-width:60mm")}<br><b>A:</b> Tschüss!<br><b>B:</b> {A("Tschüss!", "min-width:60mm")}</div>
<p style="margin-top:2mm"><b>3. Schreib.</b> Ich heiße … <div class="wline"></div></p>""",
    22, """<p>Nächste Stunde: Die Hausaufgaben laut lesen. Mit Grüßen beginnen (<i>Guten Morgen! / Guten Abend!</i>) und den Lernenden fragen: <i>Wie heißt du?</i> In Einheit 02 kommen <i>Wie geht’s?</i>, das Alphabet und die Länder.</p>""")

    b.extra("Hörtexte", f"""
{sub("01.1", "Rafael in Hamburg (langsam und natürlich)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "Die Grüße")}
<p>{" · ".join(S012)}</p>
{sub("01.3", "Die Sätze")}
<p>{" · ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 01 - Hallo")
