# Speak! Essenziell A1 - Einheit 06 "Was ist das?" (alles auf Deutsch, für absolute Anfänger; Menschen A1, L5) - shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 06", audio_json=os.path.join(HERE, "audio_de-a1-einheit-06.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

# Einstieg: bank in alphabetical order (without article), photos shuffled (rule 2026-11-23)
PHOTOS = [("A", "die Tasche", "die tasche"), ("B", "der Regenschirm", "der regenschirm"), ("C", "das Handy", "das handy"), ("D", "das Buch", "das buch"),
          ("E", "der Schlüssel", "der schlüssel"), ("F", "die Flasche", "die flasche"), ("G", "der Kuli", "der kuli"), ("H", "die Brille", "die brille")]
BANK = ["die Brille", "das Buch", "die Flasche", "das Handy", "der Kuli", "der Regenschirm", "der Schlüssel", "die Tasche"]

SCRIPT = [("Erzählerin", "Dialog eins. Im Büro."), ("Rafael", "Lena, was ist das?"), ("Lena", "Das ist ein Locher."),
          ("Rafael", "Und das? Wie heißt das auf Deutsch?"), ("Lena", "Das ist eine Schere."), ("Rafael", "Ist das ein Kuli?"),
          ("Lena", "Nein, das ist kein Kuli. Das ist ein Bleistift."),
          ("Erzählerin", "Dialog zwei. Im Café."), ("Aylin", "Rafael, hier ist eine Tasche. Ist das deine Tasche?"),
          ("Rafael", "Nein. Meine Tasche ist schwarz. Die Tasche ist blau."), ("Aylin", "Und ist das dein Regenschirm?"),
          ("Rafael", "Ja, der Regenschirm ist rot. Danke, Aylin!"),
          ("Erzählerin", "Dialog drei. Bei Rafael."), ("Jonas", "Was ist das, Rafael? Ein Buch?"), ("Rafael", "Ja, das ist ein Buch. Ein Deutschbuch!"),
          ("Jonas", "Und das? Ist das ein Heft?"), ("Rafael", "Nein, das ist kein Heft. Das ist ein Kalender.")]
S062 = BANK
S063 = ["Was ist das?", "Das ist ein Schlüssel.", "Das ist eine Brille.", "Das ist kein Kuli.", "Das ist keine Tasche.", "Wie heißt das auf Deutsch?", "rot, blau, grün, gelb, schwarz, weiß"]
COLORS = [("grün", "#2e7d32", "#fff"), ("schwarz", "#222", "#fff"), ("blau", "#1e5bb8", "#fff"), ("weiß", "#fff", "#222"), ("rot", "#d32f2f", "#fff"), ("gelb", "#f6c915", "#222")]  # shuffled vs the alphabetical bank


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Seite 1
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 06", "Was ist das?", "Dinge · Farben · ein / kein",
                       [("DU KANNST", "fragen, was etwas ist, Dinge benennen und sagen: Das ist kein …"),
                        ("SPRACHE", "Was ist das? – Das ist ein / eine … · kein / keine · Wie heißt das auf Deutsch? · Farben"),
                        ("AUSSPRACHE", "ei wie in ein, kein · -e am Wortende")])
    sw = "".join(f'<td style="width:16.6%;text-align:center"><div style="height:9mm;background:{c};border:0.3mm solid #999;border-radius:1.5mm"></div>{A(n, "min-width:18mm")}</td>' for n, c, t in COLORS)
    b.page(f"""{sec(1, "Einstieg: Dinge", "8 Min.")}
{sub("A", "Hör zu und sprich nach. Schreib.", "5 Min.", "06.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(BANK)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Die Farben. Hör zu und schreib.", "3 Min.", "06.3")}
<div class="bank" style="background:#fff">blau · gelb · grün · rot · schwarz · weiß</div>
<table class="ck"><tr>{sw}</tr></table>""",
    30, """<ol><li>A: Track 06.2 (Seite 4). Die Lehrkraft zeigt echte Dinge, wenn möglich (Handy, Schlüssel, Brille, Kuli). Nomen immer mit Artikel. Wiederholung zuerst: <i>Was kostet …? Wie findest du …?</i></li>
<li>B: Die Farben sind am Ende von Track 06.3. Danach fragen: <i>Welche Farbe hat dein Handy?</i> – nur Antwort mit einem Wort (<i>Schwarz.</i>).</li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>8 Dinge mit Fotos · 6 Farben</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Was ist das? Drei kurze Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>ein / eine</i> · <i>kein / keine</i> · <i>Wie heißt das auf Deutsch?</i></td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>Dinge und Sätze · <i>ei</i> · <i>-e</i></td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>ein / eine, kein / keine, verbinden</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Was ist in deiner Tasche? · Ratespiel</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box"><h4>IMMER NOCH LANGSAM</h4>Neu sind: <i>ein / eine</i>, <i>kein / keine</i>, <i>Was ist das? – Das ist ein …</i>, <i>Wie heißt das auf Deutsch?</i> und 6 Farben. <i>der / die / das</i> aus Einheit 05 hilft: der / das → <i>ein</i>, die → <i>eine</i>. <i>sprechen</i> und <i>doch</i> kommen in Einheit 08 (mit den Verben mit Vokalwechsel).</div>
<div class="box sand"><h4>DIE GESCHICHTE</h4>Im Büro fragt Rafael Lena nach Wörtern: <i>der Locher, die Schere, der Bleistift</i>. Im Café findet Aylin eine blaue Tasche – nicht Rafaels Tasche – und Rafaels roten Regenschirm. Bei Rafael sieht Jonas ein Deutschbuch und einen Kalender.</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4>„Não é uma caneta“ = <b>Das ist kein Kuli</b>, nicht <i>Das ist nicht ein Kuli</i>. „Em alemão“ = <b>auf Deutsch</b> (nicht <i>in Deutsch</i>). Der Artikel ist oft anders: <i>a chave</i> → <b>der</b> Schlüssel → <b>ein</b> Schlüssel.</div>
<div class="box"><h4>AUDIO</h4>Track 06.1 Drei Dialoge (langsam und natürlich) · Track 06.2 Dinge · Track 06.3 Sätze und Farben</div>""")

    # Seite 2
    gr = [("Lena: Das ist ein …", ["Locher", "Kuli"], "Locher"), ("Die Tasche im Café ist …", ["schwarz", "blau"], "blau"), ("Rafaels Regenschirm ist …", ["rot", "grün"], "rot")]
    wr = "".join(f'<td style="width:33%"><span class="small">{q}</span><br>{ch(o, a)}</td>' for q, o, a in gr)
    gp = [("Lena,", "was", " ist das?"), ("Das ist", "eine", " Schere."), ("Nein, das ist", "kein", " Kuli."),
          ("Wie heißt das", "auf", " Deutsch?"), ("Meine Tasche ist", "schwarz", "."), ("Ja, das ist", "ein", " Buch.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Was ist das?", "10 Min.")}
<p>Rafael lernt neue Wörter: im Büro mit Lena, im Café mit Aylin und zu Hause mit Jonas.</p>
{audiocard(["06.1 · SLOW", "06.1 · NATURAL"])}
{sub("A", "Hör zu. Wähle.", "3 Min.", "06.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu. Ergänze.", "5 Min.", "06.1 · NATURAL")}
<div class="bank">auf · ein · eine · kein · schwarz · was</div>
{twocol(gl, 4)}
{sub("C", "Lies die Dialoge mit der Lehrkraft.", "2 Min.")}""",
    30, """<ol><li>A: <b>langsame</b> Version, zweimal hören. Neue Wörter im Dialog nur verstehen: <i>der Locher, die Schere, der Bleistift, das Heft, der Kalender</i> – mit Fotos oder echten Dingen zeigen.</li>
<li>B: <b>natürliche</b> Version, nach jedem Dialog stoppen.</li>
<li>C: Der Lernende ist Rafael, dann tauschen.</li></ol>""")

    # Seite 3 (explanation first)
    rows = [("der Schlüssel", "<b>ein</b> Schlüssel", "<b>kein</b> Schlüssel"), ("das Handy", "<b>ein</b> Handy", "<b>kein</b> Handy"), ("die Brille", "<b>eine</b> Brille", "<b>keine</b> Brille")]
    tr_ = "".join(f"<tr><td>{a}</td><td>{e}</td><td>{k}</td></tr>" for a, e, k in rows)
    chk = [("Das ist", ["ein", "eine"], "eine", "Tasche."), ("Das ist", ["ein", "eine"], "ein", "Buch."), ("Nein, das ist", ["kein", "keine"], "keine", "Flasche."),
           ("Nein, das ist", ["nicht ein", "kein"], "kein", "Kuli."), ("Wie heißt das", ["auf", "in"], "auf", "Deutsch?")]
    cl = "".join(f'<li>{s} {ch(o, a)} {c}</li>' for s, o, a, c in chk)
    b.page(f"""{sec(3, "Grammatik: ein, eine · kein, keine", "10 Min.")}
{sub("A", "Lies die Erklärung.", "4 Min.")}
<table style="margin:0"><tr><th>Artikel</th><th>Das ist …</th><th>Nein, das ist …</th></tr>{tr_}</table>
<div class="two" style="margin-top:2mm"><div><table style="margin:0"><tr><th>Frage</th><th>Antwort</th></tr>
<tr><td>Was ist das?</td><td>Das ist ein Kuli.</td></tr><tr><td>Ist das ein Kuli?</td><td>Nein, das ist <b>kein</b> Kuli.<br>Das ist ein Bleistift.</td></tr>
<tr><td>Wie heißt das <b>auf</b> Deutsch?</td><td>Das ist eine Schere.</td></tr></table></div>
<div class="box" style="margin:0"><h4>REGELN</h4><b>der</b> und <b>das</b> → ein / kein &nbsp;·&nbsp; <b>die</b> → ein<b>e</b> / kein<b>e</b>. &nbsp;·&nbsp; <i>kein</i> = nicht + ein: <b>Das ist kein Kuli.</b> &nbsp;·&nbsp; Farbe nach dem Verb: <i>Die Tasche ist <b>blau</b>.</i></div></div>
{sub("B", "Wähle.", "3 Min.")}
<ol>{cl}</ol>
{sub("C", "Und du? Schreib.", "3 Min.")}
<div class="two"><div class="wline">Mein Handy ist {R("… (Farbe)")}</div><div class="wline">Meine Tasche ist {R("… (Farbe)")}</div></div>""",
    32, """<ol><li>A: Zuerst die Tabelle, dann die Regeln. <i>der / das → ein</i> ist leicht zu merken: nur bei <i>die</i> kommt <i>-e</i>. <i>kein</i> funktioniert genau wie <i>ein</i>.</li>
<li>B: Satz 4: typischer Fehler <i>nicht ein</i>. Satz 5: <i>auf Deutsch</i> ist eine feste Wendung.</li>
<li>C: Mit Gegenständen des Lernenden üben: <i>Was ist das? Welche Farbe?</i></li></ol>""")

    # Seite 4
    b.page(f"""{sub("D", "Typische Fehler", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th></tr>
<tr><td>Das ist nicht ein Kuli.</td><td><b>Das ist kein Kuli.</b></td></tr>
<tr><td>Das ist eine Handy.</td><td><b>Das ist ein Handy.</b></td></tr>
<tr><td>Wie heißt das in Deutsch?</td><td><b>Wie heißt das auf Deutsch?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor", "5 Min.")}
{audiocard(["06.2", "06.3"])}
{sub("A", "Hör zu und sprich nach.", "2 Min.", "06.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S062)}</div>
{sub("B", "Hör zu und sprich nach.", "3 Min.", "06.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S063)}</div>
<div class="box"><h4>LAUTE</h4><b>ei</b> = „ai“: <i><b>ei</b>n, k<b>ei</b>n, h<b>ei</b>ßt, w<b>ei</b>ß</i> &nbsp;·&nbsp; <b>-e</b> am Wortende kurz und schwach: <i>Tasch<b>e</b>, Brill<b>e</b>, Flasch<b>e</b></i> (nicht „Tasché“) &nbsp;·&nbsp; <b>ü</b> in <i>gr<b>ü</b>n, Schl<b>ü</b>ssel</i></div>""",
    36, """<ol><li>Fehler: <i>nicht ein</i> → <i>kein</i> mit Geste (Kopf schütteln) üben. <i>Handy</i> ist <i>das</i> → <i>ein</i>.</li>
<li>4A/4B: Das <i>-e</i> am Ende ist sehr kurz und schwach. <i>weiß</i> klingt wie <i>heißt</i> („ai“). Jedes Wort zweimal nachsprechen.</li></ol>""")

    # Seite 5
    gw = ["ein", "eine", "ein", "kein", "keine", "kein"]
    gs = [("Das ist", " Schlüssel."), ("Das ist", " Flasche."), ("Das ist", " Buch."), ("Nein, das ist", " Handy."), ("Nein, das ist", " Brille."), ("Nein, das ist", " Regenschirm.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:16mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("das / ist / was / ?", "Was ist das?"), ("Kuli / ist / kein / das", "Das ist kein Kuli."), ("Deutsch / heißt / das / wie / auf / ?", "Wie heißt das auf Deutsch?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    mt = [("Was ist das?", "c", "Nein, das ist kein Heft."), ("Ist das ein Heft?", "a", "Sie ist blau."), ("Welche Farbe hat die Tasche?", "b", "Das ist eine Brille."), ("Wie heißt das auf Deutsch?", "d", "Das ist ein Locher.")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "Ergänze: ein, eine, kein oder keine.", "3 Min.")}
<div class="bank">ein · ein · eine · kein · kein · keine</div>
{twocol(gl5, 4)}
{sub("B", "Ordne.", "2 Min.")}
<ol>{ol5}</ol>
{sub("C", "Verbinde.", "3 Min.")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Erst den Artikel suchen (Seite 1): <i>der Schlüssel → ein</i>, <i>die Flasche → eine</i>.</li>
<li>C: <i>Welche Farbe hat …?</i> nur verstehen. Danach die Paare laut lesen.</li></ol>""")

    # Seite 6
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Was ist in deiner Tasche? Zeig und sprich.", "5 Min.")}
<div class="msg"><b>A:</b> Was ist das?<br><b>B:</b> Das ist ein Schlüssel.<br><b>A:</b> Und das? Ist das ein Kuli?<br><b>B:</b> Nein, das ist kein Kuli. Das ist ein Bleistift.<br><b>A:</b> Welche Farbe hat der Bleistift?<br><b>B:</b> Er ist gelb.</div>
{sub("B", "Ratespiel. Die Lehrkraft zeigt ein Foto von Seite 1 nur ein bisschen. Rate!", "4 Min.")}
<div class="bank" style="background:#fff">Ist das ein / eine …? – Ja! / Nein, das ist kein / keine …</div>
{sub("C", "Wie heißt das auf Deutsch? Frag die Lehrkraft.", "3 Min.")}
<div class="bank" style="background:#fff">Wie heißt das auf Deutsch? – Das ist …</div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    30, """<ol><li>A: Der Lernende nimmt 3–4 Dinge aus der Tasche (oder vom Tisch). Die Lehrkraft fragt, dann tauschen. <i>Er / sie / es</i> für Dinge aus Einheit 05 wiederholen.</li>
<li>B: Die Lehrkraft deckt ein Foto von Seite 1 fast ganz ab (Papier / Bildschirm). Der Lernende fragt <i>Ist das ein …?</i></li>
<li>C: Der Lernende zeigt Dinge im Raum und fragt. Die neuen Wörter auf die Linien schreiben (mit Artikel!).</li></ol>""")

    # Seite 7
    pc = [("Einheit 05", "Ich kann nach dem Preis fragen."), ("Einheit 06", "Ich kann fragen: Was ist das? Wie heißt das auf Deutsch?"),
          ("Einheit 06", "Ich kann ein / eine und kein / keine benutzen."), ("Einheit 06", "Ich kann 6 Farben sagen.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Kuli", "ein"), ("Brille", "eine"), ("Handy", "ein"), ("Tasche", "eine")]
    hl = [f'<li value="{i+1}">Das ist {A(a, "min-width:14mm")} {n}.</li>' for i, (n, a) in enumerate(hw)]
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. ein oder eine?</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Meine Dinge.</b> Schreib über 4 Dinge: Was ist das? Welche Farbe?</p>
<div class="msg">Das ist mein Handy. Es ist schwarz. · Das ist meine Tasche. Sie ist …</div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Nächste Stunde: Der Lernende zeigt die 4 Dinge und liest seinen Text vor. In Einheit 07 kommen das Büro, der Akkusativ (<i>Ich brauche einen Kuli</i>) und der Plural.</p>""")

    b.extra("Hörtexte", f"""
{sub("06.1", "Was ist das? (langsam und natürlich)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("06.2", "Dinge")}
<p>{" · ".join(S062)}</p>
{sub("06.3", "Sätze und Farben")}
<p>{" · ".join(S063)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 06 - Was ist das")
