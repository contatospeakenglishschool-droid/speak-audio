# Speak! Essenziell A1 - Einheit 05 "Was kostet das?" (alles auf Deutsch, für absolute Anfänger; Menschen A1, L4) - shared engine + German layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_de import *
setup(band="A1 · EINHEIT 05", audio_json=os.path.join(HERE, "audio_de-a1-einheit-05.json"), img_dir=os.path.join(HERE, "img"), lang="de-DE")

PHOTOS = [("A", "der Tisch", "der tisch"), ("B", "der Stuhl", "der stuhl"), ("C", "das Sofa", "das sofa"), ("D", "das Bett", "das bett"),
          ("E", "die Lampe", "die lampe"), ("F", "der Schrank", "der schrank"), ("G", "das Regal", "das regal"), ("H", "die Uhr", "die uhr")]

SCRIPT = [("Erzählerin", "Dialog eins. Auf dem Flohmarkt."), ("Rafael", "Entschuldigung, was kostet der Tisch?"), ("Verkäufer", "Der Tisch? Er kostet vierzig Euro."),
          ("Rafael", "Und die Lampe?"), ("Verkäufer", "Sie kostet fünfzehn Euro."), ("Rafael", "Gut, ich nehme die Lampe."),
          ("Erzählerin", "Dialog zwei."), ("Jonas", "Wie findest du das Sofa?"), ("Rafael", "Es ist schön, aber teuer. Neunzig Euro!"),
          ("Jonas", "Und der Stuhl?"), ("Rafael", "Der Stuhl ist praktisch. Und billig!"),
          ("Erzählerin", "Dialog drei. Bei Rafael."), ("Lena", "Oh, die Lampe ist schön! Ist sie neu?"), ("Rafael", "Ja, vom Flohmarkt."),
          ("Lena", "Was kostet sie?"), ("Rafael", "Nur fünfzehn Euro."), ("Lena", "Super!")]
S052 = ["der Tisch", "der Stuhl", "das Sofa", "das Bett", "die Lampe", "der Schrank", "das Regal", "die Uhr"]
S053 = ["Was kostet der Tisch?", "Er kostet vierzig Euro.", "Was kostet die Lampe?", "Sie kostet fünfzehn Euro.", "Wie findest du das Sofa?", "Es ist schön, aber teuer.", "Der Stuhl ist billig."]
ADJ = "schön · hässlich · teuer · billig · praktisch · modern · alt · neu"


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Seite 1
    cover = cover_html(T, "NIVEAU A1 · EINHEIT 05", "Was kostet das?", "Möbel · Preise · Wie findest du …?",
                       [("DU KANNST", "nach dem Preis fragen und sagen, wie du etwas findest"),
                        ("SPRACHE", "der / die / das · er / sie / es · Was kostet …? – Er kostet 40 Euro. · Wie findest du …?"),
                        ("AUSSPRACHE", "eu wie in Euro · st / sp am Wortanfang")])
    words = ["das Bett", "das Regal", "das Sofa", "der Schrank", "der Stuhl", "der Tisch", "die Lampe", "die Uhr"]
    pr = [("die Lampe", "250 €", "teuer"), ("der Stuhl", "8 €", "billig"), ("das Sofa", "1.900 €", "teuer"), ("die Uhr", "5 €", "billig")]
    pt = "".join(f'<td style="width:25%;text-align:center"><b>{n}</b><br>{p}<br>{ch(["teuer", "billig"], a)}</td>' for n, p, a in pr)
    b.page(f"""{sec(1, "Einstieg: Möbel", "8 Min.")}
{sub("A", "Hör zu und sprich nach. Schreib.", "5 Min.", "05.2")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Teuer oder billig? Wähle.", "3 Min.")}
<table class="ck"><tr>{pt}</tr></table>""",
    30, """<ol><li>A: Track 05.2 (Seite 4). Wörter immer mit Artikel lernen: <i>der Tisch, die Lampe, das Sofa</i>. Wiederholung zuerst: <i>Wie geht’s? Wie alt bist du?</i></li>
<li>B: Mit Gesten: <i>teuer</i> (Hand hoch), <i>billig</i> (Hand runter). Die Preise laut lesen: <i>zweihundertfünfzig Euro</i> – große Zahlen nur verstehen.</li></ol>""", cover=cover)

    b.extra("Stundenüberblick · 55 Min.", """
<table><tr><th>Phase</th><th>Zeit</th><th>Ziel</th><th>Seite</th></tr>
<tr><td>1 Einstieg</td><td>8 Min.</td><td>8 Möbel mit Fotos · teuer / billig</td><td>1</td></tr>
<tr><td>2 Hören</td><td>10 Min.</td><td>Auf dem Flohmarkt: drei kurze Dialoge</td><td>2</td></tr>
<tr><td>3 Grammatik</td><td>10 Min.</td><td><i>der / die / das</i> · <i>er / sie / es</i> · <i>Was kostet …?</i> · <i>Wie findest du …?</i></td><td>3–4</td></tr>
<tr><td>4 Aussprache-Labor</td><td>5 Min.</td><td>Möbel und Sätze · <i>eu</i> · <i>st / sp</i></td><td>4</td></tr>
<tr><td>5 Üben</td><td>8 Min.</td><td>Artikel, er / sie / es, verbinden</td><td>5</td></tr>
<tr><td>6 Sprechen</td><td>12 Min.</td><td>Flohmarkt-Rollenspiel · Wie findest du …?</td><td>6</td></tr>
<tr><td>7 Abschluss</td><td>2 Min.</td><td>Selbstevaluation und Hausaufgaben</td><td>7</td></tr></table>
<div class="box"><h4>SO FUNKTIONIERT DIESES HANDBUCH</h4>Jede Seite entspricht der Seite im Kursbuch mit derselben Nummer. Deine Notizen stehen im <b>gelben Kasten</b>.
<span class="red">Die Lösungen in Rot</span> stehen nicht im Kursbuch. Die Etiketten <span class="time">5 Min.</span> zeigen die Zeit für jede Aktivität. Die Hörtexte stehen auf der letzten Seite.</div>
<div class="box"><h4>IMMER NOCH LANGSAM</h4>Neu sind: <i>der / die / das</i> (jedes Nomen mit Artikel lernen), <i>er / sie / es</i> für Dinge, <i>Was kostet …? – Er / Sie / Es kostet … Euro.</i> und <i>Wie findest du …?</i> mit 8 Adjektiven. Die Zahlen aus Einheit 04 kommen als Preise wieder.</div>
<div class="box sand"><h4>DIE GESCHICHTE</h4>Rafaels Wohnung in Altona ist noch leer. Am Samstag geht er mit Jonas auf den Flohmarkt. Der Tisch kostet 40 Euro, die Lampe 15 Euro – Rafael nimmt die Lampe. Das Sofa ist schön, aber teuer. Später kommt Lena zu Besuch und findet die Lampe schön.</div>
<div class="box"><h4>DAS PROBLEM FÜR BRASILIANER</h4>Der Artikel ist oft anders als im Portugiesischen: <i>a mesa</i> → <b>der</b> Tisch, <i>o sofá</i> → <b>das</b> Sofa. Darum: Nomen immer mit Artikel lernen. Für Dinge sagt man auch <b>er / sie / es</b>: <i>Der Tisch? <b>Er</b> kostet 40 Euro.</i> (nicht <i>Es kostet</i> für alles). <b>eu</b> = „oi“: <i>Euro, teuer</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 05.1 Drei Dialoge (langsam und natürlich) · Track 05.2 Möbel · Track 05.3 Sätze</div>""")

    # Seite 2
    gr = [("Der Tisch kostet …", ["40 Euro", "14 Euro"], "40 Euro"), ("Rafael nimmt …", ["den Tisch", "die Lampe"], "die Lampe"), ("Das Sofa ist …", ["billig", "teuer"], "teuer")]
    wr = "".join(f'<td style="width:33%"><span class="small">{q}</span><br>{ch(o, a)}</td>' for q, o, a in gr)
    gp = [("Was", "kostet", " der Tisch?"), ("", "Er", " kostet vierzig Euro."), ("Und die Lampe? –", "Sie", " kostet fünfzehn Euro."),
          ("Wie", "findest", " du das Sofa?"), ("Es ist schön, aber", "teuer", "."), ("Der Stuhl ist", "praktisch", ".")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Hören: Auf dem Flohmarkt", "10 Min.")}
<p>Rafaels Wohnung ist noch leer. Am Samstag geht er mit Jonas auf den Flohmarkt. Später kommt Lena.</p>
{audiocard(["05.1 · SLOW", "05.1 · NATURAL"])}
{sub("A", "Hör zu. Wähle.", "3 Min.", "05.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Hör noch einmal zu. Ergänze.", "5 Min.", "05.1 · NATURAL")}
<div class="bank">Er · findest · kostet · praktisch · Sie · teuer</div>
{twocol(gl, 4)}
{sub("C", "Lies die Dialoge mit der Lehrkraft.", "2 Min.")}""",
    30, """<ol><li>A: <b>langsame</b> Version, zweimal hören. <i>der Flohmarkt</i>: ein Markt mit alten Dingen (Foto zeigen). In A „den Tisch“ nur lesen, nicht erklären (Akkusativ kommt in Einheit 07).</li>
<li>B: <b>natürliche</b> Version, nach jedem Dialog stoppen. <i>Entschuldigung</i> = höflich eine Frage beginnen.</li>
<li>C: Der Lernende ist Rafael, dann tauschen.</li></ol>""")

    # Seite 3 (explanation first)
    art = [("<b>der</b> Tisch", "<b>er</b>", "Der Tisch? <b>Er</b> kostet 40 Euro."), ("<b>die</b> Lampe", "<b>sie</b>", "Die Lampe? <b>Sie</b> kostet 15 Euro."), ("<b>das</b> Sofa", "<b>es</b>", "Das Sofa? <b>Es</b> kostet 90 Euro.")]
    ta = "".join(f"<tr><td>{a}</td><td style='text-align:center'>{p}</td><td>{e}</td></tr>" for a, p, e in art)
    chk = [("Der Schrank?", ["Er", "Es"], "Er", "kostet 120 Euro."), ("Das Bett?", ["Sie", "Es"], "Es", "ist neu."), ("Die Uhr?", ["Sie", "Er"], "Sie", "ist schön."),
           ("", ["Wie", "Was"], "Was", "kostet das Regal?")]
    cl = "".join(f'<li>{s} {ch(o, a)} {c}</li>' for s, o, a, c in chk)
    b.page(f"""{sec(3, "Grammatik: der, die, das · er, sie, es", "10 Min.")}
{sub("A", "Lies die Erklärung.", "4 Min.")}
<table style="margin:0"><tr><th>Artikel</th><th>Pronomen</th><th>Beispiel</th></tr>{ta}</table>
<div class="two" style="margin-top:2mm"><div><table style="margin:0"><tr><th>Frage</th><th>Antwort</th></tr>
<tr><td>Was <b>kostet</b> der Tisch?</td><td>Er <b>kostet</b> 40 Euro.</td></tr>
<tr><td>Wie <b>findest</b> du das Sofa?</td><td>Es ist schön.<br>Ich finde es schön.</td></tr></table></div>
<div class="box" style="margin:0"><h4>REGELN</h4>Jedes Nomen hat einen Artikel: <b>der, die</b> oder <b>das</b>. Immer mit Artikel lernen! &nbsp;·&nbsp; Für Dinge: der → <b>er</b>, die → <b>sie</b>, das → <b>es</b>. &nbsp;·&nbsp; Adjektive: {ADJ}</div></div>
{sub("B", "Wähle.", "3 Min.")}
<ol>{cl}</ol>
{sub("C", "Und du? Schreib über ein Möbelstück bei dir.", "3 Min.")}
<div class="two"><div class="wline">Mein Sofa / Mein Bett / … {R("ist … (schön, alt …)")}</div><div class="wline">Es kostet / Er kostet {R("… Euro.")}</div></div>""",
    32, """<ol><li>A: Zuerst die Tabelle, dann die Regeln. <i>er / sie / es</i> kennt der Lernende schon für Personen (Einheit 02); jetzt auch für Dinge. Die Adjektive mit Bildern / Gesten zeigen.</li>
<li>B: Den ganzen Satz laut lesen lassen.</li>
<li>C: Freie Antworten akzeptieren. <i>Mein Sofa ist alt. Es kostet …</i> – Preise schätzen ist okay.</li></ol>""")

    # Seite 4
    b.page(f"""{sub("D", "Typische Fehler", "2 Min.")}
<div class="box sand"><h4>ACHTUNG: TYPISCHE FEHLER</h4>
<table style="margin:0"><tr><th>Nicht sagen</th><th>Sag</th></tr>
<tr><td>Die Tisch ist schön.</td><td><b>Der Tisch ist schön.</b></td></tr>
<tr><td>Die Lampe? Es kostet 15 Euro.</td><td><b>Die Lampe? Sie kostet 15 Euro.</b></td></tr>
<tr><td>Was kostet? (ohne Nomen)</td><td><b>Was kostet das? / Was kostet der Stuhl?</b></td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Aussprache-Labor", "5 Min.")}
{audiocard(["05.2", "05.3"])}
{sub("A", "Hör zu und sprich nach.", "2 Min.", "05.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S052)}</div>
{sub("B", "Hör zu und sprich nach.", "3 Min.", "05.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S053)}</div>
<div class="box"><h4>LAUTE</h4><b>eu</b> = „oi“: <i><b>Eu</b>ro, t<b>eu</b>er</i> &nbsp;·&nbsp; <b>st</b> am Wortanfang = „scht“: <i><b>St</b>uhl</i> &nbsp;·&nbsp; <b>sch</b>: <i><b>Sch</b>rank, <b>sch</b>ön</i> &nbsp;·&nbsp; <b>ö</b> in <i>schön</i></div>""",
    36, """<ol><li>Fehler: Der Artikel ist das Hauptproblem. Tipp: Farben benutzen (der = blau, die = rot, das = grün) und Nomen immer mit Artikel aufschreiben.</li>
<li>4A/4B: <i>Euro</i> klingt „Oiro“, nicht „Êuro“. <i>Stuhl</i> = „Schtuhl“. Jedes Wort zweimal nachsprechen.</li></ol>""")

    # Seite 5
    gw = ["der", "die", "das", "der", "das", "die"]
    gs = [("", " Tisch"), ("", " Lampe"), ("", " Sofa"), ("", " Schrank"), ("", " Bett"), ("", " Uhr")]
    gl5 = [f'<li value="{i+1}">{A(gw[i], "min-width:14mm")}{c}</li>' for i, (a, c) in enumerate(gs)]
    ps = [("Der Stuhl ist schön.", "Er", " ist auch billig."), ("Die Uhr ist alt.", "Sie", " kostet 5 Euro."), ("Das Regal ist modern.", "Es", " ist praktisch.")]
    pl = "".join(f'<li>{a} {A(x, "min-width:14mm")}{c}</li>' for a, x, c in ps)
    mt = [("Was kostet die Lampe?", "c", "Er ist schön, aber teuer."), ("Wie findest du den Schrank?", "a", "Ja, vom Flohmarkt."), ("Was kostet das Bett?", "d", "Sie kostet 15 Euro."), ("Ist der Stuhl neu?", "b", "Es kostet 200 Euro.")]
    mr = "".join(f'<tr><td>{i+1}. {l} &nbsp;{A(k, "min-width:9mm")}</td><td>{chr(97+i)}) {r}</td></tr>' for i, (l, k, r) in enumerate(mt))
    b.page(f"""{sec(5, "Üben", "8 Min.")}
{sub("A", "der, die oder das? Ergänze.", "2 Min.")}
{twocol(gl5, 4)}
{sub("B", "er, sie oder es? Ergänze.", "3 Min.")}
<ol>{pl}</ol>
{sub("C", "Verbinde.", "3 Min.")}
<table style="margin:0">{mr}</table>""",
    24, """<ol><li>A: Der Lernende darf auf Seite 1 schauen. Danach die Wörter mit Artikel laut lesen.</li>
<li>C: Frage 2: <i>den Schrank</i> nur lesen (Akkusativ kommt später). Danach die Paare laut lesen.</li></ol>""")

    # Seite 6
    items = [("der Tisch", "35 €"), ("die Lampe", "12 €"), ("das Regal", "20 €"), ("der Spiegel", "18 €")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{p}</div>' for n, p in items)
    b.page(f"""{sec(6, "Sprechen", "12 Min.")}
{sub("A", "Auf dem Flohmarkt. Spiel mit der Lehrkraft: Frag nach dem Preis.", "7 Min.")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="msg"><b>A:</b> Entschuldigung, was kostet der Tisch?<br><b>B:</b> Er kostet fünfunddreißig Euro.<br><b>A:</b> Hm, teuer! Und die Lampe?<br><b>B:</b> Sie kostet zwölf Euro.<br><b>A:</b> Gut, ich nehme die Lampe.</div>
{sub("B", "Wie findest du …? Antworte der Lehrkraft.", "5 Min.")}
<ol style="line-height:1.8"><li>Wie findest du das Sofa auf Seite 1 (Foto C)?</li><li>Wie findest du die Uhr (Foto H)?</li><li>Wie findest du dein Bett?</li><li>Was ist teuer in Brasilien? Was ist billig?</li></ol>
<div class="bank" style="background:#fff">{ADJ}</div>""",
    30, """<ol><li>A: Die Lehrkraft ist Verkäufer(in), der Lernende Kunde. Dann tauschen und die Preise ändern. <i>der Spiegel</i> ist neu: mit Geste oder Foto erklären.</li>
<li>B: Antworten: <i>Es ist schön. / Ich finde es modern.</i> Frage 4: kurze Antworten genügen (<i>Das Auto ist teuer.</i>).</li></ol>""")

    # Seite 7
    pc = [("Einheit 04", "Ich kann die Zahlen 0–100 sagen."), ("Einheit 05", "Ich kann Möbel mit Artikel nennen (der / die / das)."),
          ("Einheit 05", "Ich kann nach dem Preis fragen und antworten."), ("Einheit 05", "Ich kann sagen, wie ich etwas finde.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Stuhl", "der"), ("Bett", "das"), ("Lampe", "die"), ("Regal", "das")]
    hl = [f'<li value="{i+1}">{A(a, "min-width:14mm")} {n}</li>' for i, (n, a) in enumerate(hw)]
    b.page(f"""{sec(7, "Abschluss und Hausaufgaben", "2 Min.")}
{sub("A", "Selbstevaluation", "1 Min.")}
<table class="ck"><tr><th style="width:19mm"></th><th>Auf Deutsch …</th><th style="width:18mm">Leicht!</th><th style="width:18mm">Manchmal</th><th style="width:18mm">Noch nicht</th></tr>{pcr}</table>
{sub("B", "Hausaufgaben", "1 Min.")}
<p><b>1. der, die oder das?</b></p>
{twocol(hl, 3)}
<p style="margin-top:2mm"><b>2. Bei mir zu Hause.</b> Schreib über 3 Möbel. Was kostet es (ungefähr)? Wie findest du es?</p>
<div class="msg">Mein Sofa ist alt. Es ist schön. Es kostet … Euro. · Die Lampe ist …</div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Nächste Stunde: Der Lernende liest seinen Text vor. Die Lehrkraft fragt: <i>Wie findest du …? Was kostet …?</i> In Einheit 06 kommen <i>ein / eine</i>, <i>kein / keine</i>, Farben, <i>sprechen</i> und <i>doch</i>.</p>""")

    b.extra("Hörtexte", f"""
{sub("05.1", "Auf dem Flohmarkt (langsam und natürlich)")}
<p style="line-height:1.6">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("05.2", "Möbel")}
<p>{" · ".join(S052)}</p>
{sub("05.3", "Die Sätze")}
<p>{" · ".join(S053)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziell 05 - Was kostet das")
