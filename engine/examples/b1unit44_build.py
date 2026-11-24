# Speak! Progress B1 - Unit 44 "Helping people" (all English) - lean B1 format
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
setup(band="B1 · UNIT 44", audio_json="audio_b1-unit-44.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-44"]
S441 = [l.split(": ", 1)[1] for l in _r["44.1 Gap Year Diaries: thank you!"].split("\n")]
S442 = [x.split(": ", 1)[1] for x in _r["44.2 Repeat: offering help"].split("\n")]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 44", "Helping people", "Offering, accepting and thanking · <b>I managed to… · I wasn't able to…</b>",
                       [("YOU CAN", "offer help, accept or refuse it, and say what you could or managed to do"),
                        ("LANGUAGE", "give somebody a hand · put somebody up · lend somebody cash · could · be able to · managed to"),
                        ("PRONUNCIATION", "linking in offers: Would you like me to…? Do you need a hand?")])
    kw = [("give somebody money that they will pay back later", "lend somebody cash"),
          ("help somebody with something that needs effort, e.g. carrying bags", "give somebody a hand"),
          ("let somebody stay at your home for a short time", "put somebody up"),
          ("tell somebody what you think they should do", "give somebody advice"),
          ("stop somebody from dying", "save somebody's life"),
          ("take somebody somewhere in your car", "give somebody a ride")]
    kwl = "".join(f'<li>{A(w, "min-width:40mm")} <span style="color:#6b7377">= {d}</span></li>' for d, w in kw)
    b.page(f"""{sec(1, "Warm-up: ways of helping", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Who do you usually ask for help: family, friends or nobody?", "Is it easy for you to accept help? Why or why not?", "When did a stranger last help you?"], "START TALKING")}</div></div>
{sub("A", "Key phrases. Write the phrases from the box next to the definitions.", "3 min")}
<div class="bank" style="font-size:8.6pt">{" · ".join(sorted(w for d, w in kw))}</div>
<ol style="font-size:8.7pt;line-height:1.75;margin:0">{kwl}</ol>
{talk(["Have you ever put somebody up for more than a week? Who?", "Do you lend cash to friends? What's your rule?", "Who gives you the best advice? Give an example."], "USE THE PHRASES")}""",
    28, """<ol><li>Top box: 3 minutes.</li>
<li>A: 4 minutes with the questions. The Linguahouse lesson uses <i>give somebody a lift</i>, which is British English; in American English we say <b>give somebody a ride</b>. Check <i>lend</i> (give) vs <i>borrow</i> (take): <i>Can you lend me…? / Can I borrow…?</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Gap Year Diaries: Danny thanks five people who helped him this year · who, how and why? · questions · Talk about it",
                      "ability: can / could / be able to in all tenses; could vs was able to / managed to for one specific success", "Choose the correct form · write offers of help · Use it (oral)",
                      "offering help (44.2) · offer help for the teacher's problems, accept, refuse, thank · long turn: a time someone helped you", "Danny's message to Mrs. Lima · rewrite · watch out · writing a thank-you message"),
        """The Linguahouse lesson has phrases for helping people (give somebody advice, lend somebody cash, put somebody up, give somebody a lift, give somebody a hand, save somebody's life), offers of help (Do you want me to…? Would you like me to…?), accepting and refusing, and replies to thanks. It has no listening text and offers were already studied, so we added an episode of Danny's podcast and a new B1 grammar point: ability with could, be able to and managed to. Story (Gap Year Diaries, a thank-you episode): Mrs. Lima lent Danny cash when the ATM kept his card (Unit 23) and he paid her back when the new card arrived; Tomás put him up for two nights in Patagonia (Unit 29); Ana gave him advice and planned his week before the interview (Unit 41) and he managed to get the job (Unit 42); Bruno gave him a ride to his first day at work; last Sunday a stranger helped him carry a new bookcase to the hostel and up three floors, and Danny didn't ask his name. No real-world facts are given.""",
        """<i>Yesterday I could finish it</i> for one specific success (<i>managed to / was able to</i>); <i>will can</i>, <i>have could</i>, <i>didn't can</i>; <i>borrow</i> for <i>lend</i> (<i>Can you borrow me…?</i>); British <i>give me a lift</i> (American: <i>a ride</i>). Pronunciation: linking in <i>Would you</i> /wʊdʒu/, <i>need a hand</i> /niːdə/.""",
        "Track 44.1 Gap Year Diaries: thank you! (natural and slow; Danny) · Track 44.2 Repeat: offering help"))

    # Page 2 - Listening
    rows = [("Mrs. Lima", "lent him cash", "an ATM kept his card; he wasn't able to get money"),
            ("Tomás", "put him up for two nights", "he was exhausted and couldn't find anywhere to stay"),
            ("Ana", "gave him advice", "he was so nervous that he couldn't sleep"),
            ("Bruno", "gave him a ride", "his first day at work"),
            ("a stranger", "gave him a hand", "the bookcase was too heavy to carry by himself")]
    rt = "".join(f'<tr><td><b>{p}</b></td><td>{A(h, "min-width:28mm")}</td><td>{A(w, "min-width:44mm")}</td></tr>' for p, h, w in rows)
    qs = [("When did Danny pay Mrs. Lima back?", "When his new card arrived."),
          ("What did Danny manage to do after Ana's advice?", "He managed to get the job."),
          ("What did Danny and the stranger manage to do?", "They carried the bookcase to the hostel and up three floors."),
          ("What did Danny learn this year?", "To say yes when people offer help.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:50mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Listening: a thank-you episode", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Listen to Danny's podcast. How did each person help him? What was the problem?", "5 min")}
<table style="font-size:8.5pt;margin:.5mm 0"><tr><th>who?</th><th>how did they help?</th><th>what was the problem?</th></tr>{rt}</table></div>{img('B', 32, 30)}</div>
{audiocard(["44.1 · NATURAL", "44.1 · SLOW"])}
{sub("B", "Listen again and answer.", "3 min")}
<ol style="line-height:1.5;font-size:8.6pt;margin:0">{ql}</ol>
<p style="margin:.6mm 0;font-size:8.6pt"><b>Think about it:</b> Danny didn't ask the stranger's name. Why do you think he thanks him on the podcast? {A("open answer: he can't find him; he hopes the man is listening; to inspire others", "min-width:20mm")}</p>
{talk(["Who helped you this year? Were you able to say thank you?", "Have you ever helped a stranger? What happened?", "Do you find it easy to say yes when people offer help?"])}""",
    30, """<ol><li>A: play the natural version; play the slow one if needed. Accept the phrases from page 1 in any form.</li>
<li>B: accept short answers. Ask the student to find Danny's ability phrases: <i>wasn't able to get, couldn't find, couldn't sleep, managed to get, managed to carry, could do, I'll be able to help</i>. They come back on page 3.</li>
<li>Talk about it: 4 minutes. Each person appeared in an earlier unit (Units 23, 29, 41 and 42).</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.ability)

    # Page 4 - Practice
    pc = [("When I was a kid, I", ["could", "managed to"], "could", "swim really well."),
          ("The bookcase was heavy, but we", ["could", "managed to"], "managed to", "carry it upstairs."),
          ("I", ["couldn't", "didn't can"], "couldn't", "find my keys this morning."),
          ("Next year I hope to", ["can", "be able to"], "be able to", "speak English fluently."),
          ("Since I started this job, I've", ["could", "been able to"], "been able to", "save some money."),
          ("After three hours, the firefighters", ["could", "were able to"], "were able to", "put out the fire."),
          ("Sorry, I won't", ["can", "be able to"], "be able to", "come to your party.")]
    cl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    of = [("A woman is trying to lift a heavy bag onto a bus.", "Can I give you a hand? / Would you like me to carry your bag?"),
          ("Your friend wants a movie ticket but has no money on him.", "I can lend you some cash if you like."),
          ("You're a guest. The phone is ringing, and your host is busy in the kitchen.", "Do you want me to answer the phone?"),
          ("A friend is visiting your city, and all the hotels are full. You have a spare room.", "I can put you up if you like.")]
    ofl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in of)
    use = ["What could you do as a child that you can't do now?", "What have you managed to do this year that you're proud of?",
           "What do you want to be able to do in English by December?", "Tell me about a time you couldn't find something important.",
           "Who gave you a hand recently? With what?"]
    b.page(f"""{sec(4, "Practice: could or managed to?", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.75;font-size:8.8pt;margin:0">{cl}</ol>
{sub("B", "Write an offer of help for each situation. Use the phrases from page 1 or Would you like me to…? / Do you want me to…? / I can… if you like.", "4 min")}
<ol style="line-height:1.45;font-size:8.6pt;margin:0">{ofl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Items 2 and 6 are one specific success: <i>could</i> is wrong there. Item 1 is a general ability.</li>
<li>B: this is the Linguahouse practice task. Accept any natural offer. <i>on him</i> = with him at that moment.</li>
<li>Use it: 3 minutes, all oral. Correct <i>Yesterday I could…</i> every time.</li></ol>""")

    # Page 5 - Speaking
    card = f"""<div class="box" style="margin-top:1mm;font-size:8.2pt">{R("<b>Teacher's card (B):</b> tell the student your problems one by one: I've got a flat tire. · My flight lands at 2 a.m. and there are no buses. · I'm moving apartments on Saturday. · My laptop is really slow. · I need to write an email in Spanish. Accept two offers, refuse two (No thanks, I can manage. / Thanks, but I can do it myself.) and thank the student for one: they reply (Any time! / My pleasure.). Then swap.")}</div>""" if T else ""
    b.page(f"""{sec(5, "Speaking: can I give you a hand?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>offering</th><th>accepting</th><th>refusing</th><th>answering thanks</th></tr>
<tr><td><i>Do you need any help with…? · Can I give you a hand? · Would you like me to…? · I can… if you like.</i></td><td><i>Thanks, that's very kind of you. · Yes, please, if it's not too much trouble. · I'd appreciate that.</i></td><td><i>No thanks, it's all right. · Thanks, but I can manage. · I can do it myself, thanks.</i></td><td><i>Any time! · My pleasure. · Don't mention it. · That's OK.</i></td></tr></table></div>
{audiocard(["44.2"])}
{sub("A", "Listen and repeat. Link the words: Would you /wʊdʒu/ · need a /niːdə/.", "3 min", "44.2")}
<p style="margin:.3mm 0;font-size:8.7pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S442))}</p>
{sub("B", "Your teacher has some problems. Offer help. Your teacher accepts or refuses. Then swap.", "7 min")}{card}
{sub("C", "Long turn. Tell your teacher about a time someone helped you, or you helped someone. What was the problem? What couldn't you do? What did you manage to do in the end?", "6 min")}
<p style="margin:.3mm 0;font-size:8.5pt">Plan (1 min): {lines(1)}</p>
{talk(["In your culture, is it easy to ask for help? Is it different in other countries you know?"], "TALK ABOUT IT")}""",
    30, """<ol><li>A: <i>Would you</i> sounds like /wʊdʒu/; <i>Do you need a hand?</i> rises at the end.</li>
<li>B combines the Linguahouse role-plays (offers, accepting and refusing, thanking) for 1:1. C: 1 minute to plan, 2 minutes to talk; listen for <i>managed to / wasn't able to</i>. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now offer help and talk about what you managed to do?</i>).</li></ol>""")

    # Homework
    pc2 = [(["couldn't", "didn't could"], "couldn't"), (["lent", "borrowed"], "lent"), (["was able to", "could to"], "was able to"),
           (["been able to", "could"], "been able to"), (["be able to", "can"], "be able to"), (["give you a hand", "give you a help"], "give you a hand")]
    p = [ch(o, a) for o, a in pc2]
    rw2 = [("I tried hard and finally finished the report. (managed)", "I managed to finish the report."),
           ("It wasn't possible for me to come yesterday. (able)", "I wasn't able to come yesterday."),
           ("Maybe I can help you next week. (might be able to)", "I might be able to help you next week.")]
    rwl2 = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw2)
    b.page(f"""{sec("H", "Homework", "at home")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Danny writes a note to Mrs. Lima. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0"><b>Dear Mrs. Lima,</b> I just want to say thank you again. When the ATM kept my card, I {p[0]} get any money, and you {p[1]} me some cash without asking any questions. Thanks to you, I {p[2]} pay for my food and my bus tickets. Now I have a job, and I've {p[3]} save a little money every month. I hope I'll {p[4]} do something for you one day. If you ever need someone to {p[5]} in the kitchen, just ask! Danny</div>
{sub("B", "Rewrite the sentences with the words in brackets.", "")}
<ol style="line-height:1.5;font-size:8.7pt;margin:0">{rwl2}</ol>
{lean.watch_out([("Yesterday I could finish the report.", "Yesterday I managed to finish the report.", "one specific success: <i>managed to / was able to</i>."), ("Can you borrow me twenty dollars?", "Can you lend me twenty dollars?", "<i>lend</i> = give · <i>borrow</i> = take."), ("Can you give me a lift?", "Can you give me a ride?", "<i>a lift</i> is British English.")])}
{lean.writing_task(sub, "Write a thank-you message to someone who helped you this year.", "Dear …, I just want to say thank you for…", ["what the problem was", "what you couldn't do / weren't able to do", "how the person helped and what you managed to do", "one phrase from page 1", "100–150 words"], "I can offer help, accept or refuse it, and say what I could or managed to do.")}""",
    20, """<p>Check A and B in 3 minutes at the start of the next class. In A, <i>was able to pay</i> is one specific success. Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.6mm 0'>{t}</p>" for t in S441)
    b.extra("Audio script", f"""
{sub("44.1", "Gap Year Diaries: thank you! (natural and slow; Danny)")}
<div style="line-height:1.35;font-size:8.6pt">{script}</div>
{sub("44.2", "Repeat: offering help")}
<p>{" · ".join(S442)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 44 - Helping people")
