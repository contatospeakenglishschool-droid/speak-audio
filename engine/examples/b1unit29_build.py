# Speak! Progress B1 - Unit 29 "In the wild" (all English) - lean B1 format
import sys, os, json
_h = os.path.dirname(os.path.abspath(__file__))
for _d in ("/home/claude/speak-audio/engine", os.path.join(_h, "..", "speak-audio", "engine"), os.path.join(_h, "..", "..", "speak-audio", "engine"),
           os.path.join(_h, "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Progress"
import lean
from lean import talk
setup(band="B1 · UNIT 29", audio_json="audio_b1-unit-29.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-29"]
_n = [("twenty-five years", "25 years"), ("twenty years", "20 years")]
def _num(s):
    for k, v in _n:
        s = s.replace(k, v)
    return s.replace('"', "&quot;")
S291 = [_num(l.split(": ", 1)[1]) for l in _r["29.1 The man at the end of the road"].split("\n")]
S292 = [x.split(": ", 1)[1] for x in _r["29.2 Repeat: contractions"].split("\n")]
def _q(s):
    out, op = "", True
    for c in s.split("&quot;"):
        out += c + ("&ldquo;" if op else "&rdquo;")
        op = not op
    return out[:-7] if out.endswith(("&ldquo;", "&rdquo;")) else out
S291 = [_q(p) for p in S291]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n

    # Page 1 - Warm-up
    cover = cover_html(T, "LEVEL B1 · UNIT 29", "In the wild", "Danny meets a hermit in Patagonia · <b>past simple, present perfect, past perfect</b>",
                       [("YOU CAN", "tell a life story and talk about changes, choosing the right past tense"),
                        ("LANGUAGE", "a hermit · the wilderness · damp · sick of · save up · He has lived there for 25 years."),
                        ("PRONUNCIATION", "contractions: I've, he'd, he's")])
    kw = [("a person who lives alone, far from other people", "a hermit"), ("a wild area where nobody lives", "the wilderness"),
          ("a person who owns a house and rents it to people", "a landlord"), ("different, unusual", "unconventional"),
          ("slightly wet", "damp"), ("simple and easy to understand", "straightforward")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:24mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Warm-up: city or country?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Are you originally from a city or the countryside?", "Which lifestyle do you prefer? Why?", "Could you live in a place like this? For how long?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to the definitions.", "3 min")}
<div class="bank">damp · a hermit · a landlord · straightforward · unconventional · the wilderness</div>
<div style="font-size:8.7pt">{twocol(kwl, 3)}</div>
{talk(["Do you know anyone with an unconventional lifestyle? Tell me about them.", "Have you ever had a problem with a landlord or a damp apartment?"], "USE THE WORDS")}""",
    26, """<ol><li>Start with the questions in the top box: this is speaking time, not a test. 4 minutes.</li>
<li>A: quick check (3 minutes), then the two questions. Listen for <i>I live here since…</i> and save it for page 3.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's blog: a hermit in Patagonia · predict and check · true or false · Talk about it",
                      "past simple, present perfect and past perfect", "Complete, choose · Use it (oral)",
                      "Contractions (29.2) · role-play: an interview with a hermit", "Ana's email about Grandma Lourdes · tenses · word choice · writing", "Reading"),
        """The Linguahouse lesson is an adapted interview with a hermit in Scotland (The Independent, 2012), with a grammar focus on past simple, present perfect and past perfect. Our reading is a post on Danny's travel blog: during his two weeks in Patagonia (B1 Units 21 and 28), he meets Tomás, a fictional hermit who has lived alone by a lake for 25 years after 20 years in an office in Buenos Aires. Tomás and his story are invented; no real person or place is named. The only general fact (pumas live in Patagonia) is common knowledge. In the homework, Ana writes to Danny about her grandmother Lourdes's childhood on a farm (invented family story).""",
        """Present simple with <i>for / since</i> (<i>I live here for five years</i>), present perfect with finished times (<i>I've seen him yesterday</i>), no past perfect for the earlier action, and <i>Did you ever been…?</i>. Pronunciation: the contractions <i>'ve, 'd, 's</i> almost disappear in speech.""",
        "Track 29.1 The man at the end of the road (natural and slow; read by Danny) · Track 29.2 Repeat: contractions"))

    # Page 2 - Reading
    pr = ["Why did he become a hermit?", "What does he eat?", "How often does he see other people?", "How does he feel about his life?"]
    prl = "".join(f"<li>{q}</li>" for q in pr)
    tf = [("Tomás has lived by the lake for 25 years.", "T"), ("Before he moved, he had worked on a farm.", "F"), ("He took out a mortgage to buy the land.", "F"),
          ("The house was in good condition when he moved in.", "F"), ("He goes to town once a month.", "T"), ("Danny had never met anyone so calm.", "T")]
    tfl = "".join(f"<li>{s} {A(w, 'min-width:6mm')}</li>" for s, w in tf)
    title = S291[0].rstrip(".")
    art = "".join(f"<p style='margin:0 0 1mm'>{p}</p>" for p in S291[1:])
    b.page(f"""{sec(2, "Reading: the man at the end of the road", "12 min")}
{sub("A", "Danny met a hermit in Patagonia. Before you read, guess the answers. Then read Danny's blog post and check.", "4 min")}
<ol style="line-height:1.4;font-size:8.5pt;margin:0;columns:2">{prl}</ol>
<div class="box" style="margin:.5mm 0 0;font-size:7.9pt;line-height:1.32;column-count:2;column-gap:4mm"><b style="font-size:9.5pt">{title}</b><br>{art}</div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Write T (true) or F (false). Correct the false sentences.", "3 min")}
<ol style="line-height:1.4;font-size:8.4pt;margin:0;columns:2">{tfl}</ol></div>{img('B', 34, 22)}</div>
{audiocard(["29.1 · NATURAL", "29.1 · SLOW"])}
{talk(["Would you like to live like Tomás? What would be the hardest part?", "Why do you think some people choose to live alone in the wild?", "&ldquo;In the city, I worked to pay the rent. Here, I work to live.&rdquo; What does he mean?"])}""",
    28, """<ol><li>A–B: 7 minutes. Corrections: 2 in an office in Buenos Aires · 3 he saved up (no mortgage) · 4 no windows, very damp. Answers to A: sick of the city and his landlord; potatoes, onions, fish; once a month; calm, happy.</li>
<li>Talk about it: 5 minutes. Tomás is fictional (see the story box). Note examples of the three tenses in the text for page 3.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.past_tenses_contrast)

    # Page 4 - Practice
    fs = [("Tomás ___ (live) alone in the wilderness for 25 years.", "has lived"), ("Before he moved there, he ___ (work) in an office for almost 20 years.", "had worked"),
          ("He ___ (save) up and bought the cheapest land he could find.", "saved"), ("Nobody ___ (live) in the house for years.", "had lived"),
          ("He ___ (never / have) a TV.", "has never had")]
    fsl = "".join(f"<li><i>{s.replace('___', A(a, 'min-width:22mm'))}</i></li>" for s, a in fs)
    use = ["How long have you lived in your home? Where did you live before?", "What's the most interesting place you've ever visited? When did you go?", "Think of your first day at work or school. What had you done the night before?",
           "Have you ever changed your life completely? What happened?", "Tell me something you had never done before you were 18."]
    b.page(f"""{sec(4, "Practice: which past tense?", "10 min")}
{sub("A", "Complete the sentences from Danny's blog with the correct form of the verb.", "3 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{fsl}</ol>
{sub("B", "Choose.", "2 min")}
<ol style="line-height:1.8;font-size:8.9pt;margin:0"><li>I {ch(["met", "have met"], "met")} Tomás two weeks ago.</li>
<li>I {ch(["live", "have lived"], "have lived")} in São Paulo since July.</li>
<li>When I got to the station, the bus {ch(["already left", "had already left"], "had already left")}.</li></ol>
<div class="box sand"><h4>RULE</h4><b>past simple</b> = finished time (<i>ago, yesterday, in 2001</i>) · <b>present perfect</b> = up to now (<i>for, since, ever, never</i>) · <b>past perfect</b> = before another past moment. See the <b>Grammar reference</b> on page 3.</div>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    24, """<ol><li>A–B: 4 minutes. For each answer, ask <i>When?</i>: a finished time, up to now, or before another past moment?</li>
<li>Use it: 6 minutes, all oral. Each question needs two tenses; push for the follow-up.</li></ol>""")

    # Page 5 - Speaking
    facts = ["worked as a lawyer / teacher / chef in a big city for 15 years", "moved to a beach / a mountain / an island 10 years ago", "had never lived alone before",
             "grows / catches / buys… for food", "has never… · has learned to…", "the best and worst moment so far"]
    fl = "".join(f"<li>{f}</li>" for f in facts)
    b.page(f"""{sec(5, "Speaking: an interview with a hermit", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.3pt"><tr><th>journalist</th><th>hermit: the past</th><th>hermit: up to now</th><th>reacting</th></tr>
<tr><td><i>How long have you lived here? · What did you do before? · Why did you decide to…? · Have you ever regretted it?</i></td><td><i>Before I moved here, I had… · I was sick of… · I saved up and…</i></td><td><i>I've lived here for / since… · I've never… · I've learned to…</i></td><td><i>Really? · That must be hard! · I can imagine. · What a change!</i></td></tr></table></div>
{audiocard(["29.2"])}
{sub("A", "Listen and repeat. The contractions are very short. Which sentences are in the past perfect?", "4 min", "29.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S292))}</p>
{sub("B", "Role-play. You are a hermit. Plan your life story in 2 minutes with the ideas below. Your teacher is a journalist and interviews you. Then swap: you interview your teacher.", "14 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0;columns:2">{fl}</ol>
{talk(["Many people dream of leaving the city. Why do you think so few do it?", "What's one thing you'd never give up: your phone, the internet, your friends…?"], "TALK ABOUT IT")}""",
    38, """<ol><li>A: past perfect = 3, 4 and 5. Model the weak forms: <i>I've</i> /aɪv/, <i>he'd</i> /hiːd/.</li>
<li>B: 12 minutes. As the journalist, ask questions that need each tense (<i>How long…? What did you do before? What had you done before you moved?</i>). When you are the hermit, you were an engineer in Chicago, moved to a cabin in Alaska 12 years ago, had never seen snow before, have learned to fish and chop wood, and the worst moment was a winter without electricity. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now tell a life story with the right past tenses?</i>).</li></ol>""")

    # Homework
    pc = [(["lived", "has lived"], "lived"), (["had never seen", "has never seen"], "had never seen"), (["moved", "has moved"], "moved"), (["has lived", "lived"], "has lived"), (["didn't", "hasn't"], "hasn't")]
    p = [ch(o, a) for o, a in pc]
    rw = [("I moved to São Paulo in July. I still live here. (since)", "I've lived in São Paulo since July."),
          ("Danny arrived at the hotel. The receptionist left before that. (had)", "When Danny arrived at the hotel, the receptionist had left."),
          ("Tomás has never used a smartphone. (question: ever)", "Has Tomás ever used a smartphone?")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Ana reads Danny's blog and writes to him about her grandmother. Choose the correct verbs.", "")}</div>{img('C', 28, 18)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Hi Danny,</b><br>I loved your post about Tomás! It reminded me of Grandma Lourdes. She {p[0]} on a farm until she was twenty. When she first went to São Paulo, she {p[1]} a tall building in her life! A year later, she got married and {p[2]} to the city for good. She {p[3]} in the same apartment for more than fifty years, and she still talks about the farm every Sunday. She {p[4]} lost her love of the countryside. Ana</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl}</ol>
{lean.watch_out([("I'm sick with my landlord.", "I'm sick of my landlord.", "<i>sick of</i> = tired and annoyed; <i>sick with</i> = ill with a disease."), ("He moved to the house the first day.", "He moved in on the first day.", "<i>move in</i> / <i>move out</i> = start / stop living somewhere."), ("I'm saving money to buy a car.", "I'm saving up for a car.", "<i>save up (for)</i> = keep money for something.")])}
{lean.writing_task(sub, "Write about a big change in someone's life (you, a relative or a friend): what they did before, what happened, and how long they have lived this new life.", "My uncle had worked in a bank for twenty years when…", ["past simple", "present perfect (for / since)", "past perfect", "two words from page 1", "100–150 words"], "I can tell a life story with the right past tenses.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. The story about Grandma Lourdes is invented for the unit. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{l}</p>" for l in S291)
    b.extra("Audio script", f"""
{sub("29.1", "The man at the end of the road (natural and slow; read by Danny)")}
<div style="line-height:1.3;font-size:8.6pt">{script}</div>
{sub("29.2", "Repeat: contractions")}
<p>{" · ".join(S292)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 29 - In the wild")
