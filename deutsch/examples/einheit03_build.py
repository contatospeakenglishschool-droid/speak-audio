# Speak! Essenziell A1 - Einheit 03 "Was sind Sie von Beruf?" (alles auf Deutsch, für absolute Anfänger; Menschen A1, L2) - shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 03", audio_json=os.path.join(HERE, "audio_de-a1-einheit-03.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

PHOTOS = [("A", "die Lehrerin", "die lehrerin"), ("B", "der Arzt", "der arzt"), ("C", "die Ingenieurin", "die ingenieurin"), ("D", "der Kellner", "der kellner"),
          ("E", "die Verkäuferin", "die verkäuferin"), ("F", "der Student", "der student"), ("G", "die Köchin", "die köchin"), ("H", "der Informatiker", "der informatiker")]

SCRIPT = [("Erzählerin", "Dialog eins."), ("Frau Krüger", "Herr Costa, eine Frage: Was sind Sie von Beruf?"), ("Rafael", "Ich bin Informatiker."),
          ("Frau Krüger", "Und sind Sie verheiratet?"), ("Rafael", "Nein, ich bin nicht verheiratet. Ich bin ledig."), ("Frau Krüger", "Danke schön!"),
          ("Erzählerin", "Dialog zwei."), ("Rafael", "Lena, was bist du von Beruf?"), ("Lena", "Ich bin Designerin. Ich arbeite hier bei Nordlicht."),
          ("Rafael", "Ich arbeite auch bei Nordlicht. Als Informatiker!"),
          ("Erzählerin", "Dialog drei."), ("Rafael", "Jonas, was machst du?"), ("Jonas", "Ich bin Student. Ich studiere Musik."),
          ("Rafael", "Und du, Aylin? Was bist du von Beruf?"), ("Aylin", "Ich bin Köchin. Ich arbeite hier im Café.")]
S032 = ["der Lehrer, die Lehrerin", "der Arzt, die Ärztin", "der Ingenieur, die Ingenieurin", "der Kellner, die Kellnerin",
        "der Verkäufer, die Verkäuferin", "der Student, die Studentin", "der Koch, die Köchin", "der Informatiker, die Informatikerin"]
S033 = ["Was bist du von Beruf?", "Was sind Sie von Beruf?", "Was machst du?", "Ich bin Lehrerin.", "Ich arbeite als Kellner.", "Ich arbeite bei Nordlicht.", "Ich bin nicht verheiratet."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Seite 1
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 03", "Was sind Sie von Beruf?", "Berufe · arbeiten als, arbeiten bei",
                       [("DU KANNST", "nach dem Beruf fragen, deinen Beruf sagen und sagen, wo du arbeitest"),
                        ("SPRACHE", "Was bist du / sind Sie von Beruf? · Ich bin … · Ich arbeite als … / bei … · Lehrer → Lehrerin · nicht"),
                        ("AUSSPRACHE", "-er am Wortende · ä / ö")])
    words = ["der Arzt", "der Informatiker", "der Kellner", "der Student", "die Ingenieurin", "die Köchin", "die Lehrerin", "die Verkäuferin"]
    b.page(f"""{sec(1, "Einstieg: Berufe", "8 Min.")}
{sub("A", "Hör zu und sprich nach. Schreib.", "5 Min.", "03.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Mann oder Frau? Wähle.", "3 Min.")}
<table class="ck"><tr>{"".join(f'<td style="width:25%;text-align:center">{ch(o, a)}</td>' for o, a in [(["Lehrer", "Lehrerin"], "Lehrerin"), (["Arzt", "Ärztin"], "Arzt"), (["Koch", "Köchin"], "Köchin"), (["Student", "Studentin"], "Student")])}</tr>
<tr>{"".join(f'<td style="text-align:center"><span class="small">Foto {l}</span></td>' for l in "ABGF")}</tr></table>""",
    30, """<ol><li>A: Track 03.2 (Seite 4) sagt immer beide Formen: <i>der Lehrer, die Lehrerin</i>. Die Lehrkraft zeigt auf das Foto, der Lernende spricht beide Formen nach und schreibt die Form vom Foto. Wiederholung zuerst: <i>Hallo! Wie geht’s? Woher kommst du?</i></li>
<li>B: Mann = <i>der …</i>, Frau = <i>die …-in</i>. Nur zeigen, die Regel kommt auf Seite 3.</li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>8 Berufe mit Fotos</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Rafaels dritter Tag: drei kurze Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>Was sind Sie von Beruf?</i> · <i>arbeiten als / bei</i> · <i>-in</i> · <i>nicht</i></td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>Berufe und Sätze · <i>-er</i> · ä / ö</td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>Ergänzen, ordnen, verbinden</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Vier Personen: Beruf und Arbeitsplatz · Fragen der Lehrkraft</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box"><h4>IMMER NOCH LANGSAM</h4>Neu sind: <i>Was bist du / sind Sie von Beruf?</i> – <i>Ich bin …</i> (ohne Artikel), <i>Ich arbeite als … / bei …</i>, die Endung <i>-in</i> für Frauen und <i>nicht</i> (<i>Ich bin nicht verheiratet.</i>). Alter und <i>haben</i> kommen in Einheit 04 mit den Zahlen. Alles aus Einheit 01–02 kommt wieder.</div>
<div class="box sand"><h4>DIE GESCHICHTE</h4>Rafaels dritter Tag. Frau Krüger vom Empfang braucht noch zwei Informationen: Beruf und Familienstand. Rafael ist Informatiker und ledig. Lena ist Designerin – beide arbeiten bei <i>Nordlicht</i>. Am Abend im Café: Jonas studiert Musik und Aylin ist Köchin.</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4>„Trabalho como professor“ = <b>Ich arbeite als Lehrer</b> (nicht <i>wie</i>). Für Frauen fast immer <b>-in</b>: <i>Sie ist Lehrer</i> ✗ → <b>Sie ist Lehrerin</b>. „Não sou casado“ = <b>Ich bin nicht verheiratet</b>: <i>nicht</i> kommt nach dem Verb, nicht davor.</div>
<div class="box"><h4>AUDIO</h4>Track 03.1 Drei Dialoge (langsam und natürlich) · Track 03.2 Berufe · Track 03.3 Sätze</div>""")

    # Seite 2
    gr = [("Rafael ist …", ["Informatiker", "Ingenieur"], "Informatiker"), ("Lena ist …", ["Lehrerin", "Designerin"], "Designerin"),
          ("Aylin ist …", ["Köchin", "Kellnerin"], "Köchin")]
    wr = "".join(f'<td style="width:33%"><span class="small">{q}</span><br>{ch(o, a)}</td>' for q, o, a in gr)
    gp = [("Was", "sind", " Sie von Beruf?"), ("Nein, ich bin", "nicht", " verheiratet."), ("Ich arbeite hier", "bei", " Nordlicht."),
          ("Ich arbeite auch bei Nordlicht.", "Als", " Informatiker!"), ("Jonas, was", "machst", " du?"), ("Ich bin", "Köchin", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Rafaels dritter Tag", "10 Min.")}
<p>Rafael ist in der Firma und am Abend im Café. Er spricht mit Frau Krüger, Lena, Jonas und Aylin.</p>
{audiocard(["03.1 · SLOW", "03.1 · NATURAL"])}
{sub("A", "Hör zu. Wähle.", "3 Min.", "03.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu. Ergänze.", "5 Min.", "03.1 · NATURAL")}
<div class="bank">Als · bei · Köchin · machst · nicht · sind</div>
{twocol(gl, 4)}
{sub("C", "Lies die Dialoge mit der Lehrkraft.", "2 Min.")}""",
    30, """<ol><li>A: <b>langsame</b> Version, zweimal hören. Vorher fragen: <i>Wer ist das?</i> (Frau Krüger, Lena, Jonas, Aylin). <i>Nordlicht</i> ist der Name von Rafaels Firma.</li>
<li>B: <b>natürliche</b> Version, nach jedem Dialog stoppen. Neue Wörter mit Gesten erklären: <i>verheiratet</i> (Ring zeigen), <i>ledig</i> (kein Ring).</li>
<li>C: Die Dialoge stehen auf der letzten Seite. Der Lernende ist Rafael, dann tauschen.</li></ol>""")

    # Seite 3 (explanation first: 3A Erklärung, 3B Regel prüfen, 3C Üben)
    rows = [("Was <b>bist du</b> von Beruf?<br>Was <b>machst du</b>?", "Was <b>sind Sie</b> von Beruf?", "Ich bin Informatiker.<br>Ich bin Studentin."),
            ("Wo <b>arbeitest du</b>?", "Wo <b>arbeiten Sie</b>?", "Ich arbeite <b>als</b> Kellner.<br>Ich arbeite <b>bei</b> Nordlicht.")]
    tr_ = "".join(f"<tr><td>{a}</td><td>{c}</td><td>{d}</td></tr>" for a, c, d in rows)
    fem = [("der Lehrer", "die Lehrer<b>in</b>"), ("der Student", "die Student<b>in</b>"), ("der Arzt", "die <b>Ä</b>rzt<b>in</b>"), ("der Koch", "die K<b>ö</b>ch<b>in</b>")]
    tf = "".join(f"<tr><td>{m}</td><td>{f}</td></tr>" for m, f in fem)
    chk = [("Aylin ist", ["Koch", "Köchin"], "Köchin"), ("Rafael arbeitet", ["als", "wie"], "als"), ("Lena arbeitet", ["bei", "als"], "bei"), ("Ich", ["bin nicht", "nicht bin"], "bin nicht")]
    cl = "".join(f'<li>{s} {ch(o, a)} {"Nordlicht." if s.startswith("Lena") else "Informatiker." if s.startswith("Rafael") else "verheiratet." if s == "Ich" else ""}</li>' for s, o, a in chk)
    b.page(f"""{sec(3, "Grammatik: Was sind Sie von Beruf?", "10 Min.")}
{sub("A", "Lies die Erklärung.", "4 Min.")}
<table style="margin:0"><tr><th>du</th><th>Sie</th><th>ich</th></tr>{tr_}</table>
<div class="two" style="margin-top:2mm"><div><table style="margin:0"><tr><th>Mann</th><th>Frau: -in</th></tr>{tf}</table></div>
<div class="box" style="margin:0"><h4>REGELN</h4><b>Ich bin Lehrer.</b> Beruf ohne Artikel. &nbsp;·&nbsp; <b>als</b> + Beruf, <b>bei</b> + Firma. &nbsp;·&nbsp; Frau: meistens <b>-in</b>. &nbsp;·&nbsp; <b>nicht</b> nach dem Verb: Ich bin <b>nicht</b> verheiratet.</div></div>
{sub("B", "Wähle.", "3 Min.")}
<ol>{cl}</ol>
{sub("C", "Und du? Schreib.", "3 Min.")}
<div class="two"><div class="wline">Ich bin {R("… (Beruf)")}</div><div class="wline">Ich arbeite bei / in {R("…")}</div></div>""",
    32, """<ol><li>A: Zuerst die Tabelle mit den Sätzen aus den Dialogen lesen, dann den Regel-Kasten. <i>Was machst du?</i> fragt oft auch nach dem Beruf. Nur <i>ich / du / Sie</i>; andere Formen kommen später. Bei <i>Arzt / Koch</i>: <i>-in</i> + Umlaut (ä, ö).</li>
<li>B: Der Lernende wählt und sagt den ganzen Satz. Bei Satz 4: Im Portugiesischen steht „não“ vor dem Verb, in Deutsch steht <i>nicht</i> danach.</li>
<li>C: Ohne Beruf: <i>Ich bin Student / Studentin.</i> oder <i>Ich arbeite nicht.</i> Den Lernenden laut sprechen lassen.</li></ol>""")

    # Seite 4
    b.page(f"""{sub("D", "Typische Fehler", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th></tr>
<tr><td>Ich arbeite wie Lehrer.</td><td><b>Ich arbeite als Lehrer.</b></td></tr>
<tr><td>Lena ist Designer.</td><td><b>Lena ist Designerin.</b></td></tr>
<tr><td>Ich nicht bin verheiratet.</td><td><b>Ich bin nicht verheiratet.</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor", "5 Min.")}
{audiocard(["03.2", "03.3"])}
{sub("A", "Hör zu und sprich nach.", "2 Min.", "03.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S032)}</div>
{sub("B", "Hör zu und sprich nach.", "3 Min.", "03.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S033)}</div>
<div class="box"><h4>LAUTE</h4><b>-er</b> am Ende klingt wie ein kurzes „a“: <i>Lehr<b>er</b>, Kelln<b>er</b></i> &nbsp;·&nbsp; aber <b>-erin</b> mit „e“: <i>Lehr<b>erin</b></i> &nbsp;·&nbsp; <b>ä</b> wie „é“: <i><b>Ä</b>rztin</i> &nbsp;·&nbsp; <b>ö</b>: Lippen rund, Zunge wie bei „e“: <i>K<b>ö</b>chin</i></div>""",
    36, """<ol><li>Fehler: <i>wie</i> = „como“ bei Vergleichen; für den Beruf immer <i>als</i>. Bei Frauen auf <i>-in</i> achten. <i>nicht</i> nach dem Verb.</li>
<li>4A/4B: Jedes Wort zweimal nachsprechen. <i>Lehrer</i> ≈ „Lehra“: das <i>-er</i> nicht wie „êr“ sprechen. <b>ö</b> zuerst als „e“ sprechen, dann die Lippen rund machen.</li></ol>""")

    # Seite 5
    gw = ["bist", "sind", "als", "bei", "nicht", "Lehrerin"]
    gs = [("Was", " du von Beruf?"), ("Was", " Sie von Beruf, Frau Krüger?"), ("Ich arbeite", " Kellner."), ("Lena arbeitet", " Nordlicht."), ("Ich bin", " verheiratet."), ("Frau Weber ist", ".")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("Beruf / sind / was / von / Sie / ?", "Was sind Sie von Beruf?"), ("als / arbeite / Koch / ich", "Ich arbeite als Koch."), ("verheiratet / bin / ich / nicht", "Ich bin nicht verheiratet.")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("der Lehrer", "c", "die Köchin"), ("der Arzt", "d", "die Studentin"), ("der Koch", "a", "die Lehrerin"), ("der Student", "b", "die Ärztin")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "Ergänze.", "3 Min.")}
<div class="bank">als · bei · bist · Lehrerin · nicht · sind</div>
{twocol(gl5, 4)}
{sub("B", "Ordne.", "2 Min.")}
<ol>{ol5}</ol>
{sub("C", "Verbinde.", "3 Min.")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Satz 6: Frau Weber ist eine Frau → <i>Lehrerin</i>.</li>
<li>B: Bei der Frage steht <i>was</i> vorne, <i>von Beruf</i> am Ende. C: Danach laut lesen, mit Artikel.</li></ol>""")

    # Seite 6
    ppl = [("Lena", "Designerin · Nordlicht · ledig", "du"), ("Jonas", "Student · Universität Hamburg · ledig", "du"),
           ("Frau Krüger", "Assistentin · Nordlicht · verheiratet", "Sie"), ("Herr Schneider", "Lehrer · Schule in Altona · verheiratet", "Sie")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{d}<br>{R("→ " + ("Was bist du von Beruf? Wo arbeitest du?" if s == "du" else "Was sind Sie von Beruf? Wo arbeiten Sie?"))}</div>' for n, d, s in ppl)
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Spiel mit der Lehrkraft. Frag: Was bist du von Beruf? Wo arbeitest du? Bist du verheiratet?", "7 Min.")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> Guten Tag, Herr Schneider! Was sind Sie von Beruf?<br><b>B:</b> Ich bin Lehrer.<br><b>A:</b> Und wo arbeiten Sie?<br><b>B:</b> Ich arbeite in einer Schule in Altona.<br><b>A:</b> Sind Sie verheiratet?<br><b>B:</b> Ja, ich bin verheiratet.</div>
{sub("B", "Antworte der Lehrkraft.", "5 Min.")}
<ol style="line-height:1.8"><li>Was bist du von Beruf?</li><li>Wo arbeitest du?</li><li>Bist du verheiratet?</li><li>Woher kommst du? Wo wohnst du?</li></ol>""",
    30, """<ol><li>A: Die Lehrkraft spielt die vier Personen und antwortet wie auf der Karte. Der Lernende wählt du oder Sie. <i>Wo arbeitest du / arbeiten Sie?</i> steht auf Seite 3. Dann tauschen.</li>
<li>B: Frage 4 ist Wiederholung aus Einheit 02. Auf <i>-in</i>, <i>als</i> und <i>nicht</i> nach dem Verb achten.</li></ol>""")

    # Seite 7
    pc = [("Einheit 02", "Ich kann sagen, woher ich komme und wo ich wohne."), ("Einheit 03", "Ich kann nach dem Beruf fragen."),
          ("Einheit 03", "Ich kann meinen Beruf sagen und wo ich arbeite."), ("Einheit 03", "Ich kann sagen: Ich bin (nicht) verheiratet.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("der Lehrer", "die Lehrerin"), ("der Kellner", "die Kellnerin"), ("der Informatiker", "die Informatikerin"), ("der Verkäufer", "die Verkäuferin")]
    hl = [f'<li value="{i+1}">{m} → {A(f, "min-width:34mm")}</li>' for i, (m, f) in enumerate(hw)]
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. Schreib die Form für Frauen.</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Schreib über dich.</b> (4–5 Sätze)</p>
<div class="msg">Ich heiße … · Ich komme aus … · Ich wohne in … · Ich bin … (Beruf) · Ich arbeite bei / in …</div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Nächste Stunde: Der Lernende liest seinen Text vor (Aufgabe 2). Die Lehrkraft stellt Fragen: <i>Woher kommst du? Was bist du von Beruf?</i> In Einheit 04 kommen die Familie, <i>mein / dein</i>, die Zahlen, das Alter und <i>haben</i>.</p>""")

    b.extra("Hörtexte", f"""
{sub("03.1", "Rafaels dritter Tag (langsam und natürlich)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("03.2", "Berufe")}
<p>{" · ".join(S032)}</p>
{sub("03.3", "Die Sätze")}
<p>{" · ".join(S033)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 03 - Was sind Sie von Beruf")
