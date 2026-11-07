# Speak! Bridge A2 - Unit 31 "Say what you see" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 31", audio_json="audio_a2-unit-31.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-31"]
S311 = [x.split(": ", 1) for x in _r["31.1 The photo task"].split("\n")]
S312 = [x.split(": ", 1)[1] for x in _r["31.2 Repeat: describing a photo"].split("\n")]
S313 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["31.3 There, their or they're"].split("\n")]]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 31", "Say what you see", "Describing photos · <b>there is / are, look, maybe</b>",
                       [("YOU CAN", "describe a photo for about a minute, in an exam or in everyday life"),
                        ("LANGUAGE", "There are two people in this photo. · They look happy. · It looks like… · Maybe they're friends."),
                        ("PRONUNCIATION", "there / their / they're /ðer/")])
    wq = [(["by", "from", "of"], "of", "What's this picture", "?", "a market / a spice store"),
          (["at", "in", "on"], "in", "Who is", "the middle of the photo?", "nobody; there are baskets of spices"),
          (["at", "in", "on"], "on", "Who is", "the right?", "a man in a long gray shirt"),
          (["at", "in", "on"], "at", "What can you see", "the bottom of the photo?", "spices in big baskets"),
          (["at", "in", "on"], "in", "What can you see", "the background?", "more people and the store")]
    wql = "".join(f"<li>{a} {ch(o, r)} {e} {A(ans, 'min-width:34mm')}</li>" for o, r, a, e, ans in wq)
    b.page(f"""{sec(1, "Warm-up: talking about a photo", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 62, 42)}<div style="flex:1">{sub("A", "Choose the correct preposition. Then answer the questions about the photo.", "5 min")}
<ol style="line-height:1.55;font-size:9pt;margin:0">{wql}</ol></div></div>
{sub("B", "Talk about it.", "3 min")}
<ol style="line-height:1.55"><li>When do people describe photos? Think of three situations.</li><li>Do you take a lot of photos? Who do you show them to?</li></ol>
<p class="small" style="margin:0">{A("ideas: in a speaking test (TOEIC, for example), showing vacation photos to friends, on social media, at work (presentations, real estate, news)", "min-width:110mm")}</p>""",
    25, """<ol><li>A: accept any reasonable answer; the photo is from a spice market. Note the prepositions: a picture <b>of</b>, <b>in</b> the middle / background, <b>on</b> the left / right, <b>at</b> the top / bottom.</li>
<li>B: in Brazil, many professionals take the TOEIC test for work. Its Speaking test includes describing a picture (ETS, "TOEIC Speaking and Writing Tests", ets.org).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Prepositions for positions in a photo</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Ana practices the TOEIC photo task with Tom</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>there is / are · present continuous · look · maybe / perhaps</td><td>3</td></tr>
<tr><td>+ Language reference</td><td>–</td><td>Five tools for describing any photo</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Photo sentences · there / their / they're</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Complete a photo description · Word builder: photo words</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Describe a photo for one minute</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Back in São Paulo, Ana (Neural2-F) has her online class with Tom (Neural2-D). Her hospital wants doctors to have a TOEIC certificate, so they practice the photo task. Ana's description is slow, with pauses: this is normal in a speaking test. Fact: the TOEIC Speaking test, made by ETS (an American organization), includes questions where you describe a picture (ETS, "TOEIC Speaking and Writing Tests", ets.org). The exact timing changed in 2021, so we only say "about thirty seconds". The hospital requirement is part of our story.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students say <i>There is two people</i>, <i>They look like happy</i>, <i>Can be she's his mother</i>, start every sentence with <i>I can see</i>, use the present continuous with state verbs (<i>They are living together</i>), and confuse <i>their / there / they're</i> in writing.</div>
<div class="box"><h4>AUDIO</h4>Track 31.1 The photo task (slow and natural) · Track 31.2 Repeat: describing a photo · Track 31.3 There, their or they're</div>""")

    # Page 2
    opts = [(["There is", "There are"], "There are", "", "two people in this photo."), (["There's", "There are"], "There's", "", "a woman on the left and a man on the right."),
            (["cuts", "is cutting"], "is cutting", "The man", "some vegetables."), (["live", "are living"], "live", "I think they", "together."),
            (["can be", "maybe"], "maybe", "…or", "they're friends."), (["look", "look like"], "look", "They", "very happy."),
            (["there's", "their"], "there's", "…and", "a window in the background."), (["Perhaps", "Seems"], "Perhaps", "", "it's the weekend.")]
    ol = [f'<li value="{i+1}">{(a + " ") if a else ""}{ch(o, r)} {e}</li>' for i, (o, r, a, e) in enumerate(opts)]
    b.page(f"""{sec(2, "Listening: the photo task", "10 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1"><p style="margin:0">Ana's hospital in São Paulo wants doctors to have a TOEIC certificate. In her online class, Tom gives her a photo task from the TOEIC Speaking test.</p>
{audiocard(["31.1 · SLOW", "31.1 · NATURAL"])}</div>{img('B', 58, 40)}</div>
{sub("A", "Before you listen, look at the photo for 30 seconds. What would you say? Then listen to Ana.", "4 min", "31.1 · SLOW")}
<ol style="line-height:1.5"><li>Did Ana say the same things as you? What was different?</li>
<li>How long did Ana speak? {A("about thirty seconds", "min-width:36mm")}</li></ol>
{sub("B", "Listen again and choose the correct option.", "5 min", "31.1 · NATURAL")}
{twocol(ol, 5)}
{sub("C", "Their, there and they're: what's the difference? Do they sound different?", "1 min")}
<p class="small" style="margin:0">{A("their = possessive (their kitchen) · there = place / there is (over there) · they're = they are. They sound the same: /ðer/.", "min-width:110mm")}</p>""",
    22, """<ol><li>A: Ana speaks slowly and stops to think. That's normal in a test; what matters is that she doesn't stop completely.</li>
<li>B: 4 and 6 use state verbs (<i>live</i>, <i>look</i>), so no -ing. Read the description aloud together if there is time.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: describing a photo", "10 min")}
{sub("A", "What and where. Read and answer.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5"><b>There are</b> two people in this photo. · <b>There's</b> a woman on the left.</div>
<p style="margin:.5mm 0">What mistake do students often make with <i>there is / there are</i>? {A("They use there is with plurals: the verb must agree (there are + plural).", "min-width:70mm")}</p>
{sub("B", "Actions. Read and answer.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">They<b>'re cooking</b> in a kitchen. · The man <b>is cutting</b> some vegetables. · I think they <b>live</b> together. · They <b>look</b> very happy.</div>
<ol style="line-height:1.7"><li>How do we form the present continuous? {A("am / is / are + verb-ing", "min-width:40mm")}</li>
<li><i>Live</i> and <i>look</i> don't use -ing here because they are {ch(["state verbs", "irregular verbs"], "state verbs")}.</li></ol>
{sub("C", "The verb look. Match the sentences with the rules.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">1 They <b>look</b> very happy. · 2 He <b>looks like</b> a chef. · 3 <b>It looks like</b> they have a lot of time.</div>
<p style="margin:.5mm 0;line-height:1.7">+ a noun: {A("2", "min-width:8mm")} &nbsp; + a clause (subject + verb): {A("3", "min-width:8mm")} &nbsp; + an adjective: {A("1", "min-width:8mm")}</p>
{sub("D", "Guessing. Where do maybe and perhaps go?", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.5">…or <b>maybe</b> they're friends. · <b>Perhaps</b> it's the weekend.</div>
<p style="margin:.5mm 0">{ch(["at the beginning of the sentence or clause", "after the verb"], "at the beginning of the sentence or clause")}</p>
<div class="box sand"><h4>TEST TIPS</h4>Say where things are, but you don't need to describe everything. Speak for the right time (about 30 seconds in the TOEIC task; about one minute in many other tests). Avoid repeating <i>I can see…</i>: use <i>there is / there are</i>. More on the next page: <b>Language reference</b>.</div>""",
    27, """<ol><li>B: other state verbs from Unit 03 (Bridge): <i>know, like, want, have</i> (= own). C: <i>look like</i> + noun is also used for appearance: <i>She looks like her mother.</i></li>
<li>D: Brazilians often say <i>Can be…</i> for guesses; drill <i>Maybe…</i> and <i>Perhaps…</i>.</li></ol>""")

    grammar_ref.describing_photos(b)

    # Page 5
    tt = ["they're", "their", "there", "there", "they're", "their"]
    ttl = "".join(f"<li>{A(t, 'min-width:18mm')}</li>" for t in tt)
    b.page(f"""{sub("E", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>There is two people in the photo.</td><td><b>There are two people in the photo.</b></td><td>there are + plural.</td></tr>
<tr><td>They look like happy.</td><td><b>They look happy.</b></td><td>look + adjective.</td></tr>
<tr><td>Can be she's his mother.</td><td><b>Maybe she's his mother.</b></td><td>maybe / perhaps for guesses.</td></tr>
<tr><td>They are living together, I think.</td><td><b>I think they live together.</b></td><td>live is a state here.</td></tr>
<tr><td>On the background, there's a window.</td><td><b>In the background, there's a window.</b></td><td>in the background.</td></tr>
<tr><td>This photo is from two friends.</td><td><b>This photo is of two friends.</b></td><td>a photo of…</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["31.2", "31.3"])}
{sub("A", "Listen and repeat.", "2 min", "31.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S312)], 5)}
{sub("B", "Listen to six sentences. Do you hear there, their or they're? Write the word.", "2 min", "31.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{ttl}</ol>""",
    22, """<ol><li>A: <i>there's</i> /ðerz/; <i>they're</i> /ðer/; in fast speech the three words sound the same.</li>
<li>B: the student decides from the meaning. Script: 1 They're cooking dinner. 2 Their kitchen is really big. 3 There's a window in the background. 4 Put the bag over there. 5 They're my new neighbors. 6 Their dog is so cute.</li></ol>""")

    # Page 6
    txt = [("There", "are", "lots of people in this photo. They're"), ("", "sitting", "outside at a restaurant."), ("", "In", "the foreground, someone is"),
           ("", "taking", "a photo"), ("", "of", "a young woman with a phone. She's smiling, so she"), ("", "looks", "happy."),
           ("", "Maybe", "it's her birthday, or"), ("", "perhaps", "she's on vacation. It"), ("", "looks like", "a warm evening because people are wearing T-shirts.")]
    tx = " ".join(f"{a} {A(w, 'min-width:14mm')} {e}".strip() for a, w, e in txt)
    wb = [("background", "the part of a photo that's far away", "c"), ("close-up", "a photo taken very near something", "e"), ("selfie", "a photo you take of yourself", "a"),
          ("caption", "the words under a photo", "f"), ("blurry", "not clear or sharp", "b"), ("landscape", "a photo of the countryside, mountains or the sea", "d")]
    left = "".join(f"<li>{w} {A(l, 'min-width:7mm;text-align:center')}</li>" for w, _, l in wb)
    right = "".join(f"<li>{d}</li>" for l, d in sorted([(l, d) for _, d, l in wb]))
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Complete the description of this photo. Write one word or two in each gap.", "5 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('C', 56, 38)}<p style="flex:1;margin:0;line-height:1.85;font-size:9.2pt">{tx}</p></div>
<p class="small" style="margin:.8mm 0">Then read the description aloud. Can you add one more sentence?</p>
{sub("B", "Word builder: photo words. Match 1–6 with a–f.", "4 min")}
<div style="display:flex;gap:4mm;font-size:9pt"><ol style="flex:1;line-height:1.6;margin:0">{left}</ol><ol type="a" style="flex:1;line-height:1.6;margin:0">{right}</ol></div>
<p class="small" style="margin:.8mm 0 0">Talk about it: Do you take selfies? Do you write captions on social media? Do you prefer landscapes or photos of people?</p>""",
    22, """<ol><li>A: accept other correct answers (e.g. <i>Perhaps / Maybe</i>; <i>On the left</i> is also possible for the woman taking the photo).</li>
<li>B: <i>landscape</i> and <i>portrait</i> are also the two ways to hold a phone or a page (horizontal / vertical).</li></ol>""")

    # Page 7
    model = ("There are four friends in this photo. They're having a picnic in a park. On the left, a man is playing the guitar, and the others are listening and laughing. "
             "There's some food and drinks in the middle. Maybe it's someone's birthday, or perhaps they're just enjoying a sunny day. They look really relaxed.")
    ckl = ["I used there is / there are correctly", "I said where things are (on the left, in the background…)", "I used the present continuous for actions",
           "I used look, look like or it looks like", "I guessed with maybe or perhaps", "I spoke for about one minute"]
    ck = "".join(f"<tr><td>{c}</td><td>☐</td><td>☐</td></tr>" for c in ckl)
    b.page(f"""{sec(6, "Speaking: describe a photo", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1;text-align:center">{img('D', 72, 46)}<p class="small" style="margin:.5mm 0 0">Photo 1: your teacher describes it</p></div><div style="flex:1;text-align:center">{img('E', 72, 46)}<p class="small" style="margin:.5mm 0 0">Photo 2: you describe it</p></div></div>
{sub("A", "Listen to your teacher's description of Photo 1. Which tools from page 4 does your teacher use?", "3 min")}
<p class="small" style="margin:0">{R(model) if T else ''}</p>
{sub("B", "Look at Photo 2 for one minute. Write key words only. Then describe it for about one minute.", "5 min")}
<div class="wline"></div>
{sub("C", "Check your description with your teacher.", "2 min")}
<table class="ck"><tr><th>My description</th><th style="width:18mm">Yes</th><th style="width:18mm">Not yet</th></tr>{ck}</table>
{sub("D", "Describe Photo 2 again, but say something different: new guesses about the people and the place.", "2 min")}""",
    27, """<ol><li>A: read the red model at natural speed. Tools: there are / there's, on the left, present continuous, maybe / perhaps, look + adjective.</li>
<li>B–D: time the student. Photo 2 ideas: a couple and their dog, mountains in the background, maybe on vacation, perhaps it's cold because they're wearing jackets.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 27", "I can compare people and things with comparatives and superlatives."), ("A2 Unit 28", "I can use adverbs in the correct position."),
          ("A2 Unit 29", "I can check in, go through security and understand announcements on a plane."), ("A2 Unit 31", "I can describe a photo for about a minute.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    wrong = ("This photo is <u>by</u> a big park. <u>There is</u> a lot of people on the grass, and some of them <u>sits</u> in groups. In the background, there are some trees and a tall building, "
             "so it <u>look</u> like they're in a city. <u>Can be</u> it's a Saturday, and people <u>is</u> enjoying the sunny weather. <u>On</u> the foreground, there are two bikes, so perhaps some people <u>are come</u> by bike.")
    wrong_sb = wrong.replace("<u>", "").replace("</u>", "")
    corr = "of · There are · are sitting · looks · Maybe / Perhaps · are · In · came"
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Read the description of this photo and correct eight mistakes.</b></p>
<div style="display:flex;gap:3mm;align-items:flex-start">{img('F', 46, 32)}<div class="msg" style="flex:1;max-width:none;padding:2mm 3mm;font-size:9pt;line-height:1.5">{wrong if T else wrong_sb}</div></div>
<p class="small" style="margin:.5mm 0">{R(corr) if T else ''}</p>
<p style="margin-top:1.5mm"><b>2. A special photo (50–75 words).</b> Think of a photo from a special day (from your phone or your memory). Describe it: who and what is in it, where things are, what people are doing, and your guesses or feelings.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the description aloud without showing the photo; the teacher tries to imagine it and asks two questions. Then describe a photo together under time pressure (30 seconds).</p>""")

    b.extra("Audio script", f"""
{sub("31.1", "The photo task (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S311)}</p>
{sub("31.2", "Repeat: describing a photo")}
<p>{" · ".join(S312)}</p>
{sub("31.3", "There, their or they're (3-second pause)")}
<p>{" · ".join(S313)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 31 - Say what you see")
