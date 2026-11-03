# Speak! Bridge A2 - Unit 18 "So am I" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 18", audio_json="audio_a2-unit-18.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-18"]
NAMES = {"Tom": "Tom", "Paulo": "Paulo"}
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["18.1 After the movie"].split("\n")]
S182 = [x.split(": ", 1)[1] for x in _r["18.2 Repeat replies"].split("\n")]
S183 = [x.split(": ", 1)[1] for x in _r["18.3 Repeat dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 18", "So am I", "Movies and food · <b>agreeing: so do I, neither did I, me too</b>",
                       [("YOU CAN", "find things in common with people and agree or disagree politely"),
                        ("LANGUAGE", "I'm hungry. – So am I! · I didn't like it. – Neither did I. · I don't. – Me neither."),
                        ("PRONUNCIATION", "NEIther = NEE-ther or NIGH-ther · so do I (stress on I)")])
    b.page(f"""{sec(1, "Warm-up: movies and food", "8 min")}
<div style="display:flex;gap:3mm">{img('A', 52, 32)}{img('B', 52, 32)}</div>
{sub("A", "Put the words into two groups. Why do they go together?", "4 min")}
<div class="bank">actor · comedy · fast · healthy · hero · junk · sea · thriller</div>
<table style="table-layout:fixed;margin-top:1mm;font-size:9pt"><tr><th>group 1: {R("movies")}</th><th>group 2: {R("___ food")}</th></tr>
<tr><td style="height:9mm">{R("actor · comedy · hero · thriller")}</td><td>{R("fast · healthy · junk · sea (food = seafood)")}</td></tr></table>
<p class="small">Add two more words to each group.</p>
{sub("B", "Talk about it.", "4 min")}
<ol><li>What was the last movie you saw? Did you like it?</li><li>What do you like to eat after a movie?</li></ol>""",
    22, """<ol><li>A: group 2 = words that go before <i>food</i>: fast food, healthy food, junk food (unhealthy), seafood (one word). More: <i>comfort food, street food · director, horror, theater</i>.</li>
<li>American English: <b>movie theater</b> (British: cinema).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Movie and food words</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom and Paulo after the movie</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>So / neither + auxiliary · me too / me neither · disagreeing</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>so am I, neither do I · tenses · disagreeing politely</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Short replies · stress on the subject</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Agree and disagree · Word builder: types of movies</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Find things in common</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo has arrived in Chicago on the train (Unit 17). He and Tom come out of a movie theater and look for food (Tom = Neural2-D, Paulo = Neural2-I). Fact: Chicago deep-dish pizza became famous at Pizzeria Uno, which opened in Chicago in 1943; historians don't agree on who invented it (National Geographic, "The story behind Chicago deep-dish pizza"; NBC Chicago). It's baked in a deep pan, with the cheese under the tomato sauce.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>Me too</i> after a negative sentence (<i>I don't like fast food. – Me too</i> ✗ → <b>Me neither</b>), use the wrong auxiliary (<i>I'm hungry. – So do I</i> ✗ → <b>So am I</b>) and the wrong word order (<i>So I do</i> ✗).</div>
<div class="box"><h4>AUDIO</h4>Track 18.1 Tom and Paulo after the movie (slow and natural) · Track 18.2 Short replies · Track 18.3 Mini-dialogues</div>""")

    # Page 2
    tf = [("Paulo liked the movie.", "F: neither of them liked it."), ("Both of them like the actor who played the hero.", "T"),
          ("Someone in the theater answered a phone during the movie.", "T"), ("Tom isn't hungry.", "F: So am I! He's hungry too."),
          ("Paulo has had deep-dish pizza before.", "F: he has always wanted to try it."), ("Tom says one slice of deep-dish is like a meal.", "T")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    cw = [("Tom", "Neither", ["did", "do"], "did", "I."), ("Tom", "Me", ["also", "too"], "too", "."), ("Tom", "So", ["did", "do"], "do", "I."),
          ("Paulo", "Neither", ["did", "was"], "did", "I."), ("Tom", "So", ["am", "do"], "am", "I!"), ("Tom", "", ["I", "Me"], "Me", "neither.")]
    cwl = [f'<li value="{i+1}"><b>{n}:</b> {a} {ch(o, k)} {z}</li>' for i, (n, a, o, k, z) in enumerate(cw)]
    b.page(f"""{sec(2, "Listening: after the movie", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Paulo is in Chicago for a photo job. He and Tom come out of a movie theater downtown. What do they think of the movie? Where do they go next?</p>{img('D', 36, 22)}</div>
{audiocard(["18.1 · SLOW", "18.1 · NATURAL"])}
{sub("A", "Listen. True (T) or false (F)? Correct the false sentences.", "4 min", "18.1 · SLOW")}
{twocol(tfl, 3)}
{sub("B", "Listen again. Choose the words you hear.", "4 min", "18.1 · NATURAL")}
{twocol(cwl, 3)}
{sub("C", "Would you like to try deep-dish pizza? What's a famous food from your city?", "2 min")}""",
    22, """<p>A4: <i>So am I!</i> = I'm hungry too. B: try from memory first. C: deep-dish is baked in a deep pan, with the cheese under the sauce. Fact: Pizzeria Uno, Chicago, 1943 (see the overview).</p>""")

    # Page 3
    ex = [("Paulo: I like the actor who played the hero.", "Tom: Me too."), ("Paulo: I like all his movies.", "Tom: So do I."),
          ("Paulo: I'm really hungry.", "Tom: So am I!"), ("Tom: I didn't like the movie.", "Paulo: Neither did I."),
          ("Paulo: I don't like fast food.", "Tom: Me neither."), ("Paulo: I can eat a whole pizza.", "Tom: I can't!")]
    exl = "".join(f"<li>{a} → <b>{c}</b></li>" for a, c in ex)
    b.page(f"""{sec(3, "Language focus: so do I, neither did I", "10 min")}
{sub("A", "Read the sentences from the conversation. Then choose the correct options.", "6 min")}
<ol style="columns:2;font-size:9pt">{exl}</ol>
<ol><li>The replies in 1–3 agree with a {ch(["positive", "negative"], "positive")} sentence. The replies in 4–5 agree with a {ch(["positive", "negative"], "negative")} sentence.</li>
<li><i>Me too</i> and <i>Me neither</i> {ch(["have", "don't have"], "don't have")} a verb.</li>
<li>We {ch(["repeat", "don't repeat"], "don't repeat")} the main verb (<i>like, eat</i>). We use the auxiliary: <i>do, did, am, can…</i></li>
<li>The auxiliary is in the {ch(["same", "a different"], "same")} tense as the first sentence: <i>didn't like</i> → <i>Neither <b>did</b> I</i>.</li>
<li>Sentence 6 shows {ch(["agreement", "disagreement"], "disagreement")}.</li></ol>
{sub("B", "Other people can have things in common too. Complete.", "4 min")}
<ol><li>Tom has been to Miami. So {A("has", "min-width:10mm")} Lucy.</li><li>Kate doesn't drink coffee. Neither {A("does", "min-width:10mm")} Rita.</li>
<li>Paulo can take great photos. So {A("can", "min-width:10mm")} Carol.</li><li>I'm not going out tonight. – Really? I {A("am", "min-width:10mm")}.</li></ol>
<div class="box sand"><h4>RULE</h4>Positive → <b>So + auxiliary + subject</b> (<i>So do I</i>) or <b>Me too</b>. Negative → <b>Neither + auxiliary + subject</b> (<i>Neither do I</i>) or <b>Me neither</b>. More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>A: point out that we use the same auxiliary as in a question: <i>Do you like it? → So do I</i>.</li>
<li>B: polite disagreement: <i>Really? Sorry, but I don't.</i> A direct <i>I don't</i> can sound strong.</li></ol>""")

    grammar_ref.so_neither(b)

    # Page 5
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I don't like fast food. – Me too.</td><td><b>Me neither. / Neither do I.</b></td><td>negative sentence.</td></tr>
<tr><td>I like comedies. – So I do.</td><td><b>So do I.</b></td><td>auxiliary before subject.</td></tr>
<tr><td>I'm hungry. – So do I.</td><td><b>So am I.</b></td><td>be → am.</td></tr>
<tr><td>I didn't like it. – Neither do I.</td><td><b>Neither did I.</b></td><td>same tense.</td></tr>
<tr><td>Tom likes pizza. – So do Paulo.</td><td><b>So does Paulo.</b></td><td>he / she → does.</td></tr>
<tr><td>I like this actor. – I also.</td><td><b>Me too. / So do I.</b></td><td>not a full answer.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["18.2", "18.3"])}
{sub("A", "Short replies. Listen and repeat. The stress is on the last word.", "2 min", "18.2")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S182)}</div>
{sub("B", "Mini-dialogues. Listen and repeat. Then say them with your teacher.", "2 min", "18.3")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S183)}</div>
<div class="box" style="margin-top:1mm"><h4>SOUND INTERESTED</h4>Say <i>So am I!</i> with energy and the voice going up and down: it shows you're happy to have something in common. <b>neither</b> = NEE-ther or NIGH-ther (both correct).</div>""",
    24, """<ol><li>4A: so do <b>I</b>, neither did <b>I</b>, me <b>too</b>: the last word is stressed.</li>
<li>4B: then say true sentences about yourself; the student replies.</li></ol>""")

    # Page 6
    tb = [("I like tennis.", "So do I.", "I don't."), ("I'm late for work.", "Me too. / So am I.", "I'm not."), ("I don't have a cat.", "Me neither. / Neither do I.", "I do."),
          ("Kate makes great cakes.", "So does Lucy.", "Lucy doesn't."), ("Tom isn't going to work today.", "Neither is Paulo.", "Paulo is."),
          ("I can drive.", "So can I.", "I can't."), ("I've been to Orlando.", "So have I.", "I haven't."), ("Carol watched the game.", "So did Ana.", "Ana didn't.")]
    tbr = "".join(f"<tr><td>{a}</td><td>{A(g, 'min-width:28mm')}</td><td>{A(d, 'min-width:20mm')}</td></tr>" for a, g, d in tb)
    gn = [("a funny movie", "comedy"), ("a scary movie with monsters or ghosts", "horror movie"), ("an exciting movie with crime and danger", "thriller"),
          ("a movie about a love story", "romance"), ("a movie with fights, chases and explosions", "action movie"), ("a movie about real life and facts", "documentary"),
          ("a movie with cartoons, for example from Pixar", "animated movie"), ("a movie about the future, space or robots", "sci-fi movie")]
    gnl = [f'<li value="{i+1}">{d} {A(w, "min-width:20mm")}</li>' for i, (d, w) in enumerate(gn)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Agree and disagree. Complete the table.", "5 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>sentence</th><th>agree</th><th>disagree</th></tr>{tbr}</table>
{sub("B", "Word builder: types of movies. Write the words.", "3 min")}
<div class="bank">action movie · animated movie · comedy · documentary · horror movie · romance · sci-fi movie · thriller</div>
{twocol(gnl, 4)}
<p class="small">Tell your teacher: <i>I love comedies.</i> Your teacher agrees or disagrees!</p>""",
    22, """<ol><li>A: some cells have two correct answers. Read the table aloud as mini-dialogues.</li>
<li>B: <i>sci-fi</i> = science fiction (SIGH-figh). Pixar is in California.</li></ol>""")

    # Page 7
    pr = ["Snacks and junk food: I like ______, but I don't like ______.", "Healthy food: my favorite healthy food is ______.",
          "Hot drinks: I always have ______, but I never have ______.", "Movies: I prefer ______, but I don't enjoy ______.",
          "Sports: I like to play ______, and I like to watch ______.", "Vacations: I've been to ______. I've never been to ______."]
    prl = "".join(f"<li>{p.replace('______', '<span style=\"display:inline-block;width:24mm;border-bottom:.6pt solid #999\"></span>')}</li>" for p in pr)
    b.page(f"""{sec(6, "Speaking: find things in common", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">
<div style="flex:1">{sub("A", "Complete the sentences about you.", "4 min")}
<ol style="font-size:9pt;line-height:1.9">{prl}</ol></div>{img('C', 34, 26)}</div>
{sub("B", "Read your sentences to your teacher. Your teacher agrees or disagrees. Continue the conversation.", "6 min")}
<div class="msg" style="max-width:none;font-size:9pt"><b>You:</b> I like chocolate. <b>Teacher:</b> So do I! But I don't like white chocolate. <b>You:</b> Me neither. It's too sweet.</div>
{sub("C", "How many things do you have in common? What was the most surprising?", "2 min")}""",
    26, """<ol><li>B: answer truthfully and give reasons; disagree on at least two things so the student hears <i>I don't / I do</i>. Then you read your sentences, and the student replies.</li>
<li>Note the student's errors and correct them at the end.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 14", "I can join ideas with and, but, so, because and although."), ("A2 Unit 15", "I can put ideas in order and talk about changing my mind."),
          ("A2 Unit 16", "I can define people, things and places with who, that and where."), ("A2 Unit 17", "I can make phone calls, take a message and leave a voicemail."),
          ("A2 Unit 18", "I can agree and disagree with so, neither, me too and me neither.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    mt = [("I didn't go shopping.", "d"), ("I'm not tired.", "b"), ("My sister hasn't finished her homework.", "c"), ("I'm going out tonight.", "f"),
          ("Lucy doesn't want cake.", "e"), ("Megan likes concerts.", "g"), ("Rita won't enjoy this movie.", "a"), ("I should watch more movies in English.", "h")]
    ends = ["a. Kate will.", "b. I am.", "c. I have.", "d. Neither did I.", "e. Neither does Tom.", "f. So am I.", "g. So does Carol.", "h. So should I."]
    mtl = "".join(f"<tr><td>{i+1}. {a} {R(k)}</td><td>{ends[i]}</td></tr>" for i, (a, k) in enumerate(mt))
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Match the sentences and the replies. Which three replies show disagreement?</b> {R("a, b, c")}</p>
<table style="table-layout:fixed;margin-top:0;font-size:9pt">{mtl}</table>
<p style="margin-top:2mm"><b>2. My friend and I (50–75 words).</b> Write about a friend or family member. What do you have in common? What's different? <i>I love horror movies, and so does my sister. She doesn't like coffee, but I do…</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>2: the sentence <i>and so does my sister</i> joins two people in one sentence; accept simple versions too. Next class: the student reads the text and you react with <i>So do I / I don't</i>.</p>""")

    b.extra("Audio scripts", f"""
{sub("18.1", "Tom and Paulo after the movie (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{NAMES[n]}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("18.2", "Short replies")}
<p>{" · ".join(S182)}</p>
{sub("18.3", "Mini-dialogues")}
<p>{" · ".join(S183)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 18 - So am I")
