# Rebuilt page 3 (explanation first) for A1 Essentials units 01-20, whose build files are lost.
# usage: p3old.py NN  -> writes oldbuild/NN - SB_draft.pdf / TB_draft.pdf (page 3 is the 3rd page)
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"))
import speak_engine as _se
from speak_engine import *

U = {}


def unit(n):
    def deco(f):
        U[n] = f
        return f
    return deco


def rules_ol(b, items):
    """items: (before, right, wrong, after, right_first)"""
    out = ""
    for s, right, wrong, after, rf in items:
        o = [right, wrong] if rf else [wrong, right]
        o = [b.R(f"<u>{x}</u>") if (b.T and x == right) else x for x in o]
        out += f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b>{after}</li>"
    return f"<ol>{out}</ol>"


def two_boxes(a, b_):
    return f'<div class="two"><div class="box" style="margin-top:1.5mm">{a}</div><div class="box" style="margin-top:1.5mm">{b_}</div></div>'


@unit(1)
def u01(b):
    A, sub = b.A, b.sub
    body = f"""{b.sec(3, "Language focus: the verb <i>to be</i>", "10 min")}
{sub("A", "Grammar table", "4 min", pt="Tabela de gramática: forma completa e forma curta")}
<table style="table-layout:fixed"><tr><th style="width:30mm"></th><th>Full form</th><th>Short form</th><th>Negative</th><th>Question</th></tr>
<tr><td><b>I</b></td><td>I am</td><td>I'm</td><td>I'm not</td><td>Am I…?</td></tr>
<tr><td><b>you</b></td><td>you are</td><td>you're</td><td>you aren't</td><td>Are you…?</td></tr>
<tr><td><b>he / she / it</b></td><td>she is</td><td>she's</td><td>she isn't</td><td>Is she…?</td></tr>
<tr><td><b>we / they</b></td><td>we are</td><td>we're</td><td>we aren't</td><td>Are we…?</td></tr></table>
{two_boxes("<h4>SHORT ANSWERS</h4>Are you a student?<br><b>Yes, I am.</b> / <b>No, I'm not.</b>", "<h4>IN CONVERSATION</h4>We usually say the <b>short form</b>:<br><i>I'm Ana.</i> (not <i>I am Ana</i>)")}
{sub("B", "Read the sentences from the audio. Choose the correct option.", "3 min", pt="Leia as frases do áudio. Escolha a opção correta.")}
<div class="bank" style="background:#fff">I'<b>m</b> Tom. · <b>Are</b> you a student? · No, I'<b>m not</b>. · She'<b>s</b> a student.</div>
{rules_ol(b, [("With <b>I</b>, we use", "am", "is", ".", True), ("With <b>he</b> and <b>she</b>, we use", "is", "are", ".", False),
              ("With <b>you</b>, <b>we</b> and <b>they</b>, we use", "are", "is", ".", True), ("The correct question is", "Are you a student?", "You are a student?", ".", False)])}
{sub("C", "Complete with am, is or are.", "3 min", pt="Complete com am, is ou are.")}
<ol><li>I {A("am", "min-width:12mm")} Brazilian.</li><li>Paulo {A("is", "min-width:12mm")} a photographer.</li><li>{A("Are", "min-width:12mm")} you a teacher? — Yes, I am.</li></ol>"""
    notes = """<ol><li>A: explain the table first. Use Portuguese to compare: <i>eu sou / estou</i> = <i>I am</i>. <i>To be</i> means both <i>ser</i> and <i>estar</i>: <i>I'm a doctor</i> (sou) and <i>I'm tired</i> (estou).</li>
<li>B: the student checks the rules with the sentences from the audio. Short answers: <i>Yes, I am.</i> never <i>Yes, I'm.</i></li>
<li>C: then ask the student real questions: <i>Are you tired? Is your mother a teacher?</i></li></ol>"""
    return body, 32, notes


@unit(2)
def u02(b):
    A, sub = b.A, b.sub
    body = f"""{b.sec(3, "Language focus: the verb <i>have</i>", "10 min")}
{sub("A", "Grammar table", "4 min", pt="Tabela de gramática")}
<table style="table-layout:fixed"><tr><th style="width:30mm"></th><th>Affirmative</th><th>Negative</th><th>Question</th><th>Short answers</th></tr>
<tr><td><b>I / you / we / they</b></td><td>I <b>have</b> a pen.</td><td>I <b>don't have</b> a pen.</td><td><b>Do</b> you <b>have</b> a pen?</td><td>Yes, I do. / No, I don't.</td></tr>
<tr><td><b>he / she / it</b></td><td>She <b>has</b> a pen.</td><td>She <b>doesn't have</b> a pen.</td><td><b>Does</b> she <b>have</b> a pen?</td><td>Yes, she does. / No, she doesn't.</td></tr></table>
{two_boxes("<h4>REMEMBER</h4>After <b>does</b> and <b>doesn't</b>, use <b>have</b>:<br><i>Does she have…? She doesn't have…</i>", "<h4>SHORT ANSWERS</h4>Do you have a pen?<br><b>Yes, I do.</b> (not <i>Yes, I have</i>)")}
{sub("B", "Read the sentences from the audio. Choose the correct option.", "3 min", pt="Leia as frases do áudio. Escolha a opção correta.")}
<div class="bank" style="background:#fff">I <b>have</b> a new notebook. · She <b>has</b> a new laptop. · <b>Do</b> you <b>have</b> a pen? · No, I <b>don't</b>.</div>
{rules_ol(b, [("With <b>I</b>, <b>you</b>, <b>we</b> and <b>they</b>, we use", "have", "has", ".", True), ("With <b>he</b>, <b>she</b> and <b>it</b>, we use", "has", "have", ".", False),
              ("The correct question is", "Do you have a pen?", "Have you a pen?", ".", True), ("The correct question is", "Does she have a bag?", "Does she has a bag?", ".", False),
              ("The correct negative is", "I don't have a laptop.", "I no have a laptop.", "", True)])}
{sub("C", "Complete with have, has, do or does.", "3 min", pt="Complete com have, has, do ou does.")}
<ol><li>Tom {A("has", "min-width:12mm")} a cat.</li><li>{A("Do", "min-width:12mm")} you have a car?</li><li>{A("Does", "min-width:12mm")} Kate {A("have", "min-width:12mm")} a bike?</li></ol>"""
    notes = """<ol><li>A: compare with Portuguese: <i>eu tenho</i> = <i>I have</i>, <i>ela tem</i> = <i>she has</i>. Show the pattern with your hands: <b>do / does</b> does the work in questions and negatives, so <i>have</i> doesn't change.</li>
<li>B: the student checks the rules. Short answers use <i>do / does</i>, not <i>have</i>: <i>Yes, I do.</i></li>
<li>C: then drill 3 or 4 quick questions about real objects near you.</li></ol>"""
    return body, 30, notes


@unit(3)
def u03(b):
    A, sub = b.A, b.sub
    rows = [("I", "my", "my mother"), ("you", "your", "your father"), ("he", "his", "his wife"), ("she", "her", "her husband"), ("we", "our", "our son"), ("they", "their", "their daughter")]
    tr = "".join(f"<tr><td>{p}</td><td><b>{o}</b></td><td>{e}</td></tr>" for p, o, e in rows)
    l1 = [f'<li value="{i+1}">{x}</li>' for i, x in enumerate([f"This is {A('my', 'min-width:14mm')} husband, Marcos.", f"That's {A('our', 'min-width:14mm')} son, Leo.", f"This is Paulo and {A('his', 'min-width:14mm')} wife, Julia.",
                                                           f"She's Leo{A(chr(39) + 's', 'min-width:10mm')} cousin.", "I have one sister.", f"{A('Her', 'min-width:14mm')} name's Kate."])]
    body = f"""{b.sec(3, "Language focus: <i>my, his, her</i> and <i>'s</i>", "10 min")}
{sub("A", "Grammar table", "4 min", pt="Tabela de gramática")}
<div class="two"><div><table style="margin:0"><tr><th>Person</th><th>Possessive</th><th>Example</th></tr>{tr}</table></div>
<div><div class="box" style="margin-top:0"><h4>NAME + 'S</h4><b>Ana's</b> son = o filho da Ana<br><b>Tom's</b> sister = a irmã do Tom<br><b>Leo's</b> cousin = o primo do Leo</div>
<div class="box"><h4>WHO?</h4><b>Who's</b> this? → This is my brother.<br><b>Who are</b> they? → They're my parents.</div></div></div>
{sub("B", "Look at the sentences. Choose the correct option.", "3 min", pt="Olhe as frases. Escolha a opção correta.")}
{rules_ol(b, [("<b>Paulo and his wife.</b> <i>His</i> is for", "a man", "a woman", ".", True), ("<b>Kate is Tom's sister. Her name is Kate.</b> <i>Her</i> is for", "a woman", "a man", ".", False),
              ("The correct sentence is", "Leo is Ana's son.", "Leo is the son of Ana.", "", True), ("<b>Our son</b> means the son of", "Ana and Marcos", "Ana only", ".", False)])}
{sub("C", "Complete with my, our, his, her or 's. Then listen and check.", "3 min", "3.1 · NATURAL", pt="Complete com my, our, his, her ou 's. Depois, ouça e confira.")}
{twocol(l1, 4)}"""
    notes = """<ol><li>A: key idea in Portuguese: <b>his = dele</b>, <b>her = dela</b>. It depends on the owner, not on the thing: <i>Paulo and <b>his</b> wife</i>, never <i>her wife</i>. Show 's with real names: the student's name + a family word (<i>Carla's mother</i>).</li>
<li>B: <i>Our son</i>: the son of Ana and Marcos (we). C uses the audio.</li></ol>"""
    return body, 30, notes


CLOCK = """<svg width="9mm" height="9mm" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#fff" stroke="#1F3A44" stroke-width="2"/>
<line x1="20" y1="20" x2="{hx}" y2="{hy}" stroke="#1F3A44" stroke-width="3" stroke-linecap="round"/>
<line x1="20" y1="20" x2="{mx}" y2="{my}" stroke="#1F3A44" stroke-width="2" stroke-linecap="round"/></svg>"""


def clock(h, m):
    import math
    ma = math.radians(m * 6 - 90); ha = math.radians((h % 12 + m / 60) * 30 - 90)
    return CLOCK.format(hx=20 + 9 * math.cos(ha), hy=20 + 9 * math.sin(ha), mx=20 + 14 * math.cos(ma), my=20 + 14 * math.sin(ma))


@unit(4)
def u04(b):
    A, sub = b.A, b.sub
    times = [(7, 0, "It's <b>seven o'clock</b>.", "seven"), (7, 5, "It's <b>seven oh five</b>.", "five after / past seven"), (7, 15, "It's <b>seven fifteen</b>.", "a quarter after / past seven"),
             (7, 30, "It's <b>seven thirty</b>.", "half past seven"), (7, 45, "It's <b>seven forty-five</b>.", "a quarter to eight")]
    tr = "".join(f'<tr><td style="width:12mm;padding:.6mm 1mm">{clock(h, m)}</td><td style="width:14mm"><b>{h}:{m:02d}</b></td><td>{s}</td><td class="small">{o}</td></tr>' for h, m, s, o in times)
    body = f"""{b.sec(3, "Language focus: the time", "10 min")}
{sub("A", "How to say the time", "4 min", pt="Como dizer as horas. Use a coluna do meio; a última é só para reconhecer.")}
<table style="table-layout:fixed;font-size:9pt"><tr><th style="width:12mm"></th><th style="width:14mm">Time</th><th>Say this (most common in the US)</th><th>You can also hear</th></tr>{tr}</table>
{two_boxes("<h4>THE TIME NOW</h4>What time <b>is it</b>? → <b>It's</b> ten thirty.<br>Excuse me, do you have the time?", "<h4>THE TIME OF AN EVENT</h4>What time is lunch? → <b>It's at</b> twelve.<br>My class is <b>at</b> 6 p.m.")}
{sub("B", "Read the sentences from the audio. Choose the correct option.", "3 min", pt="Leia as frases do áudio. Escolha a opção correta.")}
<div class="bank" style="background:#fff">What time <b>is it</b>? It's nine fifteen. · What time is the meeting? <b>It's at</b> ten o'clock. · My class is at six <b>p.m.</b></div>
{rules_ol(b, [("To ask the time now, we say", "What time is it?", "What hours is it?", ".", True), ("For the time of an event, we use", "at", "in", ".", False),
              ("In English, 7 p.m. is", "seven p.m.", "nineteen o'clock", ".", True), ("<b>a.m.</b> means", "in the morning", "in the afternoon or evening", ".", False)])}
{sub("C", "Write the time in words.", "3 min", pt="Escreva as horas por extenso.")}
<p>8:10 → It's {A("eight ten", "min-width:26mm")}. &nbsp; 6:30 → It's {A("six thirty", "min-width:26mm")}. &nbsp; 11:45 → It's {A("eleven forty-five", "min-width:30mm")}.</p>"""
    notes = """<ol><li>A: teach the middle column for production; the right column is for listening only. 7:05 = <i>seven oh five</i>: the 0 is "oh". Compare with Portuguese: <i>Que horas são? São três horas</i> → <i>What time is it? It's three o'clock</i> (always <i>it's</i>, singular).</li>
<li>B: a.m. = midnight to noon; p.m. = noon to midnight. 12 p.m. = noon (meio-dia). C: then say times; the student says them in words.</li></ol>"""
    return body, 31, notes


@unit(5)
def u05(b):
    A, sub = b.A, b.sub
    l1 = [f'<li value="{i+1}">{x}</li>' for i, x in enumerate([f"{A('Can', 'min-width:14mm')} you make coffee?", f"Yes, I {A('can', 'min-width:14mm')}.", f"No, I {A(chr(99) + 'an' + chr(39) + 't', 'min-width:14mm')}. But I can learn.",
                                                           f"I {A('can', 'min-width:14mm')} speak English and Spanish.", f"I {A('can' + chr(39) + 't', 'min-width:14mm')} work on Monday mornings."])]
    body = f"""{b.sec(3, "Language focus: <i>can</i> and <i>can't</i>", "10 min")}
{sub("A", "Grammar table", "4 min", pt="Tabela de gramática: can é igual para todas as pessoas")}
<table style="table-layout:fixed"><tr><th style="width:40mm"></th><th>Affirmative</th><th>Negative</th><th>Question</th><th>Short answers</th></tr>
<tr><td><b>I / you / he / she / it / we / they</b></td><td>She <b>can</b> swim.</td><td>She <b>can't</b> swim.</td><td><b>Can</b> she swim?</td><td>Yes, she can. / No, she can't.</td></tr></table>
{two_boxes("<h4>CAN = SABER / CONSEGUIR / PODER</h4>I can swim. = Eu sei nadar.<br>I can't see. = Eu não consigo ver.<br>Can I sit here? = Posso sentar aqui?", "<h4>FULL FORM</h4><b>can't</b> = <b>cannot</b> (one word!)<br>We use <i>cannot</i> in formal writing.")}
{sub("B", "Look at the sentences. Choose the correct option.", "3 min", pt="Olhe as frases. Escolha a opção correta.")}
{rules_ol(b, [("With <b>he</b> and <b>she</b>, we say", "she can", "she cans", ".", True), ("After <b>can</b>, the verb is", "without to", "with to", ".", False),
              ("The correct question is", "Can you swim?", "Do you can swim?", ".", True), ("The correct negative is", "I can't drive.", "I no can drive.", "", False)])}
{sub("C", "Complete with can or can't. Then listen and check.", "3 min", "5.1 · NATURAL", pt="Complete com can ou can't. Depois, ouça e confira.")}
{twocol(l1, 4)}"""
    notes = """<ol><li>A: key idea: <i>can</i> never changes: no -s, no <i>to</i>, no <i>do</i>. It's easier than <i>have</i> (Unit 2)! Portuguese uses three verbs (<i>saber, conseguir, poder</i>); English uses one. Give one example of each and ask the student for another.</li>
<li>B: the student checks the rules. C uses the audio.</li></ol>"""
    return body, 30, notes


@unit(6)
def u06(b):
    A, sub = b.A, b.sub
    l1 = [f'<li value="{i+1}">{x}</li>' for i, x in enumerate([f"{A('Do', 'min-width:14mm')} you work at night?", f"Yes, I {A('do', 'min-width:14mm')}.", f"I {A('don' + chr(39) + 't', 'min-width:14mm')} have lunch.",
                                                           f"{A('Does', 'min-width:14mm')} Ana work at night?", f"No, she {A('doesn' + chr(39) + 't', 'min-width:16mm')}.", f"She {A('works', 'min-width:14mm')} in the day."])]
    body = f"""{b.sec(3, "Language focus: the present simple", "10 min")}
{sub("A", "Grammar table", "4 min", pt="Tabela de gramática: a regra muda só com he / she / it")}
<table style="table-layout:fixed"><tr><th style="width:30mm"></th><th>Affirmative</th><th>Negative</th><th>Question</th><th>Short answers</th></tr>
<tr><td><b>I / you / we / they</b></td><td>I <b>work</b>.</td><td>I <b>don't work</b>.</td><td><b>Do</b> you work?</td><td>Yes, I do. / No, I don't.</td></tr>
<tr><td><b>he / she / it</b></td><td>She <b>works</b>.</td><td>She <b>doesn't work</b>.</td><td><b>Does</b> she work?</td><td>Yes, she does. / No, she doesn't.</td></tr></table>
{two_boxes("<h4>SPELLING: HE / SHE / IT</h4>work → works · get → gets<br>go → goes · do → does<br>finish → finishes · watch → watches<br><b>have → has</b> (irregular!)", "<h4>WHEN DO WE USE IT?</h4>For routines and things that are always true.<br><i>I get up at seven.</i> (every day)<br><i>She works at a hospital.</i> (her job)<br><span class='small'>don't = do not · doesn't = does not</span>")}
{sub("B", "Look at the table. Choose the correct option.", "3 min", pt="Olhe a tabela. Escolha a opção correta.")}
{rules_ol(b, [("With <b>he / she / it</b>, the verb has", "-s", "no -s", ".", True), ("With <b>I / you / we / they</b>, the verb has", "no -s", "-s", ".", False),
              ("For questions with <b>he / she</b>, we use", "Does", "Do", ".", True), ("After <b>does / doesn't</b>, the verb has", "no -s", "-s", ".", False)])}
{sub("C", "Complete the sentences from the dialogue. Then listen and check.", "3 min", "6.1 · NATURAL", pt="Complete as frases do diálogo. Depois, ouça e confira.")}
{twocol(l1, 4)}
<div class="bank">do · does · don't · doesn't · works</div>"""
    notes = """<ol><li>A: key idea: the -s goes to only ONE place: <i>She works</i> but <i>She doesn't work / Does she work?</i> The -s moves to <i>does</i>.</li>
<li>B: the student checks the rules. Portuguese has no auxiliary in questions (<i>Você trabalha?</i>). Insist on <i>Do</i> at the start. C: the student completes, then plays the audio.</li></ol>"""
    return body, 28, notes


def run(n):
    _se.SERIES = "Essentials"
    nn = f"{n:02d}"
    aj = f"oldbuild/audio_{nn}.json"
    if not os.path.exists(aj):
        d, base = {}, f"https://contatospeakenglishschool-droid.github.io/speak-audio/a1-unit-{nn}/"
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", f"a1-unit-{nn}")
        for f in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
            if f.endswith("-natural.mp3"):
                d[f[:-12] + " · NATURAL"] = base + f
            elif f.endswith("-slow.mp3"):
                d[f[:-9] + " · SLOW"] = base + f
            elif f.endswith(".mp3"):
                d[f[:-4]] = base + f
        json.dump(d, open(aj, "w"))
    setup(band=f"A1 · UNIT {n}", audio_json=aj, img_dir="none")

    def build(teacher):
        b = Book(teacher)
        b.page("", 20, "")
        b.page("", 20, "")
        body, h, notes = U[n](b)
        b.page(body, h, notes)
        return b.html()
    render(build, f"oldbuild/{nn}")


import importlib
if __name__ == "__main__":
    for _m in ("units_b", "units_c"):
        try:
            importlib.import_module(_m)
        except ModuleNotFoundError:
            pass
    import p3old as _me
    U.update(_me.U)
    os.makedirs("oldbuild", exist_ok=True)
    for a in sys.argv[1:]:
        run(int(a))
