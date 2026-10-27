# Speak! Essenziell A1 - Einheit 01 "Hallo! Ich bin…" (alles auf Deutsch) - built with the shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 01", audio_json=os.path.join(HERE, "audio_de-a1-einheit-01.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

PHOTOS = [("A", "Hallo!", "hallo"), ("B", "Guten Morgen!", "guten morgen"), ("C", "Guten Tag!", "guten tag"), ("D", "Guten Abend!", "guten abend"),
          ("E", "Gute Nacht!", "gute nacht"), ("F", "Auf Wiedersehen!", "auf wiedersehen"), ("G", "Tschüss!", "tschüss"), ("H", "Freut mich!", "freut mich")]

SCRIPT = [("Erzählerin", "Dialog eins."), ("Herr Schneider", "Guten Morgen! Sind Sie Herr Costa?"), ("Rafael", "Ja, das bin ich. Guten Morgen!"),
          ("Herr Schneider", "Ich bin Klaus Schneider. Willkommen in Hamburg!"), ("Rafael", "Danke! Freut mich, Herr Schneider."),
          ("Herr Schneider", "Wie geht es Ihnen?"), ("Rafael", "Gut, danke. Und Ihnen?"), ("Herr Schneider", "Auch gut, danke."),
          ("Erzählerin", "Dialog zwei."), ("Lena", "Hallo! Bist du Rafael, der neue Kollege?"), ("Rafael", "Ja, das bin ich. Hallo! Und wie heißt du?"),
          ("Lena", "Ich heiße Lena. Freut mich!"), ("Rafael", "Freut mich auch, Lena."), ("Lena", "Und, wie geht’s? Heute ist dein erster Tag!"),
          ("Rafael", "Gut, danke. Ein bisschen müde. Und dir?"), ("Lena", "Super!"),
          ("Erzählerin", "Dialog drei."), ("Aylin", "Guten Abend!"), ("Rafael", "Guten Abend! Einen Tee, bitte."), ("Aylin", "Gern. Sind Sie neu hier?"),
          ("Rafael", "Ja, ich bin Rafael. Ich bin Brasilianer."), ("Aylin", "Rafael? Wie schreibt man das?"), ("Rafael", "R – A – F – A – E – L."),
          ("Aylin", "Danke! Ich heiße Aylin. Wir können du sagen, okay?"), ("Rafael", "Gern!"),
          ("Aylin", "Also … tschüss, Rafael! Bis morgen!"), ("Rafael", "Auf Wiedersehen … äh, nein: Tschüss, Aylin! Bis morgen!")]
S012 = ["ich", "dich", "Nacht", "auch", "heiße", "Sie", "wie", "Willkommen", "Tschüss"]
S013 = ["Wie heißt du? ↘", "Wie heißen Sie? ↘", "Wie geht’s? ↘", "Wie geht es Ihnen? ↘", "Bist du Lena? ↗", "Sind Sie Herr Schneider? ↗", "Und du? ↗", "Und Sie? ↗"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Seite 1
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 01", "Hallo! Ich bin …", "Begrüßen und sich vorstellen · <b>du oder Sie?</b>",
                       [("DU KANNST", "begrüßen, dich vorstellen, deinen Namen buchstabieren und fragen, wie es geht"),
                        ("SPRACHE", "sein · heißen · ich / du / Sie · Wie geht’s? / Wie geht es Ihnen?"),
                        ("AUSSPRACHE", "ich / ach · ei / ie · w · ü · Satzmelodie in Fragen")])
    words = ["Auf Wiedersehen!", "Freut mich!", "Gute Nacht!", "Guten Abend!", "Guten Morgen!", "Guten Tag!", "Hallo!", "Tschüss!"]
    qs = [("Es ist 8 Uhr morgens. Du gehst in eine Bäckerei.", "Guten Morgen!"), ("Es ist 20 Uhr. Du gehst in ein Restaurant.", "Guten Abend!"),
          ("Du gehst schlafen.", "Gute Nacht!"), ("Du gehst aus einem Geschäft.", "Auf Wiedersehen!"), ("Du lernst eine neue Person kennen.", "Freut mich!")]
    ql = [f'<li value="{i+1}">{q} {R("→ " + a) if T else ""}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Einstieg: Begrüßungen", "8 Min.")}
{sub("A", "Sieh die Fotos an, hör zu und sprich nach. Schreib dann den Gruß unter das Foto.", "4 Min.")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Was sagst du?", "4 Min.")}
{twocol(ql, 4)}""",
    28, """<ol><li>A: Die Lehrkraft liest jedes Wort, der Lernende spricht nach und schreibt. <b>Guten Morgen</b> bis ca. 10–11 Uhr, dann <b>Guten Tag</b>; <b>Guten Abend</b> ab ca. 18 Uhr; <b>Gute Nacht</b> nur vor dem Schlafen. In Norddeutschland hört man auch <b>Moin!</b> (den ganzen Tag) – und Rafael wohnt in Hamburg!</li>
<li>B: In informellen Situationen auch <i>Hallo!</i> akzeptieren. Fragen: <i>Und in Brasilien?</i></li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>8 Grüße und Ausdrücke mit Fotos</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Rafaels erster Tag in Hamburg: drei Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>sein</i> · <i>heißen</i> · du oder Sie?</td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>ich / ach · ei / ie · w · Satzmelodie in Fragen</td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>Ergänzen, ordnen, umformen (du → Sie)</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Vier Situationen: du oder Sie? · persönliche Fragen</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box sand"><h4>DIE GESCHICHTE BEGINNT</h4>Rafael Costa ist Softwareentwickler aus Curitiba. Er zieht nach Hamburg und arbeitet in einer IT-Firma. Am Morgen lernt er seinen Vermieter kennen, Herrn Schneider (Sie). In der Firma lernt er Lena kennen, eine Kollegin (du). Am Abend, im Café unten im Haus, lernt er Aylin kennen … und muss seinen Namen buchstabieren!</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4><i>Bin Rafael</i> ✗ → <b>Ich bin Rafael</b>: Im Deutschen steht das Subjekt immer da. <i>Ich heißen</i> ✗ → <b>Ich heiße</b>. Das formelle <b>Sie</b> hat das Verb wie im Plural (<i>Sie sind, Sie heißen</i>) und immer ein großes S. Und <i>Wie geht’s?</i> nur mit du.</div>
<div class="box"><h4>AUDIO</h4>Track 01.1 Drei Dialoge (langsam und natürlich) · Track 01.2 Laute · Track 01.3 Fragen</div>""")

    # Seite 2
    who = [("1", "Rafael und Herr Schneider", "Sie"), ("2", "Rafael und Lena", "du"), ("3", "Rafael und Aylin", "Sie → du")]
    wr = "".join(f'<td style="width:33%"><b>Dialog {n}</b><br><span class="small">{p}</span><br>{ch(["du", "Sie"], a) if a != "Sie → du" else (R("<u>Sie → du</u>") if T else "<b>du / Sie</b>")}</td>' for n, p, a in who)
    gp = [("Ich bin Klaus Schneider.", "Willkommen", " in Hamburg!"), ("Wie geht es", "Ihnen", "?"), ("Und wie", "heißt", " du?"),
          ("", "Freut mich", " auch, Lena."), ("Rafael? Wie", "schreibt", " man das?"), ("Wir können", "du", " sagen, okay?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:22mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Rafaels erster Tag", "10 Min.")}
<p>Rafael ist Brasilianer. Heute ist sein erster Tag in Hamburg. Er lernt drei Personen kennen: den Vermieter, eine Kollegin und die Chefin vom Café unten im Haus.</p>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL"])}
{sub("A", "Hör zu. Sagen die Personen in jedem Dialog du oder Sie?", "3 Min.", "01.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu und ergänze.", "5 Min.", "01.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Am Ende sagt Rafael: „Auf Wiedersehen … äh, nein: Tschüss!“ Warum?", "2 Min.")}
<div class="wline">{R("Weil Aylin sagt: „Wir können du sagen.“ Jetzt sprechen sie informell, und mit du sagt man „Tschüss!“.")}</div>""",
    34, """<ol><li>A: <b>langsame</b> Version. In Dialog 3 beginnt Aylin mit <b>Sie</b> (<i>Sind Sie neu hier?</i>) und bietet dann das Du an.</li>
<li>B: <b>natürliche</b> Version. Rafael buchstabiert seinen Namen: R – A – F – A – E – L. Kurz das Alphabet zeigen; das ganze Alphabet kommt in den Hausaufgaben.</li>
<li>C: <i>Wir können du sagen</i> = wir duzen uns. Unter jungen Leuten und Kollegen ist das oft schnell normal; mit Vermietern, Ärzten und Behörden bleibt man beim Sie.</li></ol>""")

    # Seite 3
    sein = [("ich", "bin", "Ich bin Rafael."), ("du", "bist", "Bist du Lena?"), ("er / sie", "ist", "Er ist Brasilianer."), ("Sie (formell)", "sind", "Sind Sie Herr Schneider?")]
    heis = [("ich", "heiße"), ("du", "heißt"), ("er / sie", "heißt"), ("Sie (formell)", "heißen")]
    reg = [("Hallo!", "Guten Tag! / Guten Abend!"), ("Wie geht’s?", "Wie geht es Ihnen?"), ("Wie heißt du?", "Wie heißen Sie?"), ("Und dir?", "Und Ihnen?"), ("Tschüss! Bis morgen!", "Auf Wiedersehen!")]
    rules = [("Zu einem Freund:", "Wie geht’s?", "Wie geht es Ihnen?"), ("Zu einer Dame, die du nicht kennst:", "Sind Sie Deutsche?", "Bist du Deutsche?"),
             ("Deinen Namen sagen:", "Ich heiße Rafael.", "Heiße Rafael."), ("Das formelle Sie schreibt man mit", "großem S", "kleinem s")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    ts = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in sein)
    th = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in heis)
    tr_ = "".join(f"<tr><td>{a}</td><td>{f}</td></tr>" for a, f in reg)
    b.page(f"""{sec(3, "Grammatik: sein, heißen, du oder Sie?", "10 Min.")}
{sub("A", "Die Verben sein und heißen. Lies die Sätze aus den Dialogen.", "3 Min.")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">sein</th></tr>{ts}</table></div>
<div><table style="margin:0"><tr><th colspan="2">heißen</th></tr>{th}</table></div></div>
{sub("B", "Informell oder formell?", "3 Min.")}
<table style="margin:0"><tr><th>du (informell)</th><th>Sie (formell)</th></tr>{tr_}</table>
{sub("C", "Wähle die richtige Option.", "4 Min.")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>DU ODER SIE?</h4><b>du</b> = Freunde, Familie, Kinder, oft auch Kollegen. <b>Sie</b> = Erwachsene, die du nicht kennst, Geschäfte, Ämter, Ärzte, Vermieter. Mit <b>Sie</b> ist das Verb wie im Plural: Sie <b>sind</b>, Sie <b>heißen</b>. Das Subjekt steht immer da: <i>Ich bin Rafael</i>, nie nur <i>Bin Rafael</i>. Bei Ja/Nein-Fragen steht das Verb vorne: <i><b>Bist</b> du Lena?</i></div>""",
    24, """<ol><li>A: Zeigen, dass <i>sie ist</i> (= ela) und <i>Sie sind</i> (formell) verschieden sind: Verb und großes S helfen. <i>du heißt</i> und <i>er heißt</i> sind gleich.</li>
<li>B/C: Den Lernenden nach Beispielen aus seinem Leben fragen: <i>Sagst du zu deinem Arzt du oder Sie?</i></li></ol>""")

    # Seite 4
    b.page(f"""{sub("D", "Typische Fehler von Brasilianern", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th><th>Warum?</th></tr>
<tr><td>Bin Rafael.</td><td><b>Ich bin Rafael.</b></td><td>Das Subjekt steht immer da.</td></tr>
<tr><td>Ich heißen Rafael.</td><td><b>Ich heiße Rafael.</b></td><td><i>ich</i> → Verb mit <i>-e</i>.</td></tr>
<tr><td>Sie bist Herr Schneider?</td><td><b>Sind Sie Herr Schneider?</b></td><td>Mit <i>Sie</i>: <i>sind</i>. Bei Ja/Nein-Fragen: Verb vorne.</td></tr>
<tr><td>Wie heißen sie? (formell)</td><td><b>Wie heißen Sie?</b></td><td>Das formelle <i>Sie</i> immer groß.</td></tr>
<tr><td>Wie geht’s, Herr Schneider?</td><td><b>Wie geht es Ihnen, Herr Schneider?</b></td><td><i>Herr / Frau</i> + Nachname = Sie.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor", "5 Min.")}
{audiocard(["01.2", "01.3"])}
{sub("A", "Die Laute. Hör zu und sprich nach: ch in ich und in Nacht, ei und ie, w wie in wie.", "2 Min.", "01.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S012)}</div>
{sub("B", "Die Fragen. Hör zu und sprich nach. W-Fragen gehen nach unten ↘, Ja/Nein-Fragen nach oben ↗.", "3 Min.", "01.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S013)}</div>""",
    40, """<ol><li>Fehler: <i>Bin Rafael</i> und <i>Ich heißen</i> sind die häufigsten Fehler (im Portugiesischen fehlt das Subjekt oft). Sofort und freundlich korrigieren.</li>
<li>4A: <b>ch</b> nach i/e (<i>ich, dich</i>) = weich, wie ein langes „ch“ mit Lächeln; nach a/o/u (<i>Nacht, auch</i>) = hinten im Hals, wie das brasilianische „rr“ in <i>carro</i>. <b>ei</b> = „ai“ (<i>heiße</i>), <b>ie</b> = langes „i“ (<i>Sie, wie</i>). <b>w</b> = „v“. <b>ü</b> in <i>Tschüss</i>: Lippen wie bei „u“, Zunge wie bei „i“.</li>
<li>4B: Anders als im Portugiesischen geht die Stimme bei W-Fragen am Ende nach unten. Nur Ja/Nein-Fragen und <i>Und du?</i> gehen nach oben.</li></ol>""")

    # Seite 5
    gw = ["bin", "Bist", "Sind", "heißt", "heiße", "heißen", "ist", "heißt"]
    gs = [("Ich", "Rafael."), ("", "du Lena?"), ("", "Sie Herr Schneider?"), ("Wie", "du?"), ("Ich", "Aylin."),
          ("Wie", "Sie?"), ("Das", "Jonas, der Nachbar von Rafael."), ("Die Kollegin", "Lena.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")} {c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("heißt / wie / du / ?", "Wie heißt du?"), ("es / Ihnen / wie / geht / ?", "Wie geht es Ihnen?"),
          ("Lena / ich / bin / Hallo,", "Hallo, ich bin Lena."), ("neu / Sie / hier / sind / ?", "Sind Sie neu hier?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "Ergänze mit sein oder heißen.", "3 Min.")}
<div class="bank">bin · bist · heiße · heißen · heißt · heißt · ist · sind</div>
{twocol(gl5, 5)}
{sub("B", "Bring die Wörter in die richtige Reihenfolge.", "2 Min.")}
<ol>{ol5}</ol>
{sub("C", "Schreib den Dialog um: von du zu Sie.", "3 Min.")}
<div class="two"><div class="msg"><b>A:</b> Hallo! Wie heißt du?<br><b>B:</b> Ich heiße Jonas. Und du?<br><b>A:</b> Ich bin Rafael. Wie geht’s?<br><b>B:</b> Gut, danke!</div>
<div><div class="wline">{R("A: Guten Tag! Wie heißen Sie?")}</div><div class="wline">{R("B: Ich heiße Jonas Becker. Und Sie?")}</div><div class="wline">{R("A: Ich bin Rafael Costa. Wie geht es Ihnen?")}</div><div class="wline">{R("B: Gut, danke!")}</div></div></div>""",
    25, """<ol><li>A: Sätze 2 und 3 sind Ja/Nein-Fragen: Das Verb steht vorne und beginnt mit großem Buchstaben (<i>Bist, Sind</i>).</li>
<li>B: Auf die Verbposition achten. C: Mit Sie benutzt man meistens den Nachnamen. <i>Guten Morgen / Guten Abend</i> auch akzeptieren.</li></ol>""")

    # Seite 6
    sit = [("1", "In der Bäckerei, 7:30 Uhr", "Du kaufst Brötchen. Die Verkäuferin ist eine ältere Dame.", "Sie · Guten Morgen!"),
           ("2", "Im Büro, erster Tag", "Du lernst einen jungen Kollegen kennen.", "du · Hallo!"),
           ("3", "Im Hotel, 21 Uhr", "Du kommst an die Rezeption.", "Sie · Guten Abend!"),
           ("4", "Auf einer Party", "Du lernst einen Freund von einem Freund kennen.", "du · Hallo!")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n} · {t}</b>{d}<br>{R("→ " + a)}</div>' for n, t, d, a in sit)
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Rollenspiel. Lies die Situation: du oder Sie? Begrüße die Person, stell dich vor und frag, wie es geht. Dann tauscht die Rollen.", "7 Min.")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="bank" style="background:#fff">Hallo! / Guten Tag! · Ich heiße … · Freut mich! · Wie geht’s? / Wie geht es Ihnen? · Gut, danke. Und dir? / Und Ihnen? · Tschüss! / Auf Wiedersehen!</div>
{sub("B", "Und du? Antworte der Lehrkraft.", "5 Min.")}
<ol style="line-height:1.65"><li>Wie heißt du? Wie schreibt man das?</li><li>Wie geht’s dir heute?</li><li>Sagst du bei der Arbeit du oder Sie? Zu wem?</li><li>Kennst du einen Deutschen oder eine Deutsche? Wie heißt er oder sie?</li></ol>""",
    30, """<ol><li>A: Die Lehrkraft spielt die andere Person. In Situation 1 mit Sie antworten, in Situation 4 mit du. Dann spielt der Lernende die Verkäuferin, den Rezeptionisten usw.</li>
<li>B: Frage 1: den Namen buchstabieren lassen (Alphabet auf Seite 7). Fragen 3 und 4 wiederholen <i>du / Sie</i> und <i>heißt</i>. <i>Bin …</i> und <i>Sie bist</i> korrigieren.</li></ol>""")

    # Seite 7
    pc = [("Einheit 01", "Ich kann formell und informell begrüßen."), ("Einheit 01", "Ich kann meinen Namen sagen und buchstabieren."),
          ("Einheit 01", "Ich kann fragen und sagen, wie es mir geht."), ("Einheit 01", "Ich kann zwischen du und Sie wählen.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ich heißen Paul.", "Ich heiße Paul."), ("Gute Morgen, Frau Weber!", "Guten Morgen, Frau Weber!"), ("Sie bist Herr Fischer?", "Sind Sie Herr Fischer?"),
          ("Wie geht’s dir, Frau Braun?", "Wie geht es Ihnen, Frau Braun?"), ("Wie heiße du?", "Wie heißt du?"), ("Bin Rafael Costa.", "Ich bin Rafael Costa.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. Korrigiere die Fehler.</b> In jedem Satz ist ein Fehler.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Das Alphabet.</b> Schreib deinen Vornamen, deinen Nachnamen und den Namen deiner Stadt. Buchstabiere sie in der nächsten Stunde.</p>
<div class="wline"></div>
<p style="margin-top:2mm"><b>3. Eine Nachricht.</b> Schreib Aylin eine kurze Nachricht: Begrüße sie, stell dich vor und frag, wie es ihr geht (3–4 Sätze, mit du).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Nächste Stunde: die Korrekturen kontrollieren. Der Lernende buchstabiert die Namen aus Aufgabe 2. Dann liest er die Nachricht vor und die Lehrkraft antwortet als Aylin (<i>Hallo, Rafael! Mir geht’s gut, danke …</i>).</p>""")

    b.extra("Hörtexte", f"""
{sub("01.1", "Rafaels erster Tag (langsam und natürlich)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "Die Laute")}
<p>{" · ".join(S012)}</p>
{sub("01.3", "Die Fragen")}
<p>{" ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 01 - Hallo")
