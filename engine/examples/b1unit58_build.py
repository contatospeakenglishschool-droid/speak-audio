# Speak! Progress B1 - Unit 58 "Fake news" (all English) - lean B1 format
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
setup(band="B1 · UNIT 58", audio_json="audio_b1-unit-58.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["b1-unit-58"]
S581 = [l.split(": ", 1)[1] for l in _r["58.1 Danny's blog: the day the bakery closed"].split("\n")]
S582 = [x.split(": ", 1)[1] for x in _r["58.2 Repeat: reporting verbs"].split("\n")]


TITLE = "The day the bakery closed"
PARAS = [S581[0].replace(TITLE + ". ", "", 1)] + S581[1:]


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
    cover = cover_html(T, "LEVEL B1 · UNIT 58", "Fake news", "Rumors, sources and checking the facts · <b>he denied closing… · she warned us not to…</b>",
                       [("YOU CAN", "talk about fake news, report what people said and judge if a story is reliable"),
                        ("LANGUAGE", "rumor · source · misleading · spot · according to · reporting verbs: deny, admit, warn, accuse"),
                        ("PRONUNCIATION", "linking verb + -ing: denied_closing, admitted_sharing")])
    words = ["accept", "frustrated", "influence", "judge", "misleading", "rumor", "source", "worrying"]
    defs = {"accept": "to believe that something is true, especially when it's bad", "frustrated": "annoyed because things don't happen the way you want",
            "influence": "to affect how someone thinks or behaves", "judge": "to form an opinion after thinking carefully",
            "misleading": "making people believe something that isn't true", "rumor": "a story passed from person to person that may not be true",
            "source": "the place or person that information comes from", "worrying": "making you feel anxious"}
    order = [4, 7, 0, 6, 1, 3, 5, 2]
    kwl = "".join(f'<li>{A(words[i], "min-width:24mm")} <span style="color:#6b7377">= {defs[words[i]]}</span></li>' for i in order)
    b.page(f"""{sec(1, "Warm-up: did you see this?", "7 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 52, 34)}<div style="flex:1">
{talk(["Look at the photo. What news do you think she has just seen?", "What is fake news? Give an example of the kind of stories people share.", "Where do you usually get your news?"], "START TALKING")}</div></div>
{sub("A", "Key words. Write the words from the box next to their meanings.", "3 min")}
<div class="bank">{" · ".join(words)}</div>
<ol style="font-size:8.6pt;line-height:1.7;margin:0">{kwl}</ol>
{talk(["Have you ever heard a rumor about your neighborhood or your work?", "Who or what influences your opinions the most?", "Is it hard to judge if a story online is real? Why?"], "USE THE WORDS")}""",
    30, """<ol><li>Top box: 3 minutes. Fake news is false information created on purpose and presented as fact; it often spreads fast because it is surprising or emotional.</li>
<li>A: 4 minutes with the questions. Stress: <i>RU-mor, SOURCE, mis-LEAD-ing, IN-flu-ence</i> (both the verb and the noun).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55–60 min", lean.overview(
        lean.std_rows("Danny's blog: the day the bakery closed · true or false · find the words · Talk about it",
                      "reporting verbs and their patterns: deny / admit + -ing, warn / advise + person + to, offer / promise + to, accuse of / apologize for + -ing", "Choose the correct pattern · report what they said · Use it (oral)",
                      "linking (58.2) · talking about news and sources · spot the fake headlines · long turn: a rumor you believed", "internet language · Ana's message · watch out · writing: how to spot fake news",
                      listen_label="Reading"),
        """The Linguahouse lesson is a newspaper article about teachers in another country who say students use fake news as facts, with survey numbers, a real union and its leader, a politician, a new law with fines and an international expert. We did not use it, because we cannot check those facts and they date quickly. Instead, the student reads a post from Danny's blog (also recorded as audio): a message in the hostel group chat says the bakery on the corner (where Pipoca once ate three cheese breads) is closing forever. Mrs. Lima, devastated, insists on going to say goodbye; Bruno offers to go with her; there is a long line. The owner, Mr. Nunes (new, one-off), denies closing: the photo is from last year, when he closed for one day to paint. A customer accuses him of lying. Rafa admits sharing the message without reading it carefully (it came from his cousin) and apologizes. Ana gives a short lesson on how to spot fake news. We kept the Linguahouse key words, internet language, talking points and the real-or-fake headline task (now with invented headlines), and added a new B1 grammar point: reporting verbs.""",
        """<i>She suggested me to check</i> (→ <i>suggested checking</i>); <i>He denied to close</i> (→ <i>denied closing</i>); <i>accused him to lie</i> (→ <i>of lying</i>); <i>He explained me</i> (→ <i>explained to me</i>). Vocabulary: <i>a news</i> (→ <i>a piece of news / a news story</i>); <i>fake news are</i> (→ <i>is</i>).""",
        "Track 58.1 Danny's blog: the day the bakery closed (natural and slow; read by Danny) · Track 58.2 Repeat: reporting verbs"))

    # Page 2 - Reading
    text = "".join(f"<p style='margin:0 0 1mm'>{p}</p>" for p in PARAS)
    tf = [("The photo in the message was taken last Tuesday.", "F: it was from last year, when the bakery closed for one day."),
          ("Mrs. Lima wanted to say goodbye to the bakery.", "T"),
          ("Rafa wrote the fake message.", "F: he only shared it; nobody knows where it began."),
          ("Ana thinks fake news can influence people's decisions.", "T")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    fw = [("very sad and shocked (P2)", "devastated"), ("not able to understand what was happening (P3)", "confused"),
          ("see or recognize something (P5)", "spot"), ("not being serious (P6)", "joking")]
    fwl = "".join(f"<li>{d} {A(w, 'min-width:24mm')}</li>" for d, w in fw)
    b.page(f"""{sec(2, "Reading: the day the bakery closed", "12 min")}
{sub("A", "Read Danny's blog post. Was the bakery really closing? Who shared the message in the hostel group?", "5 min")}
<div class="box" style="margin:.5mm 0;font-size:8.2pt;line-height:1.36"><div style="float:right;margin:0 0 1mm 2.5mm">{img('B', 34, 23)}</div><b style="font-size:9.4pt;color:#176074">{TITLE}</b><br>{text}</div>
{audiocard(["58.1 · NATURAL", "58.1 · SLOW"])}
<div style="display:flex;gap:4mm"><div style="flex:1.2">
{sub("B", "True (T) or false (F)?", "3 min")}
<ol style="line-height:1.4;font-size:8.3pt;margin:0">{tfl}</ol></div><div style="flex:1">
{sub("C", "Find the words.", "3 min")}
<ol style="line-height:1.5;font-size:8.3pt;margin:0">{fwl}</ol></div></div>""",
    35, """<ol><li>A: no, the photo was old (the bakery closed for one day last year to paint the walls); Rafa shared it. Students can read and listen at the same time.</li>
<li>After C, ask the student to underline how Danny reports what people said or did: <i>insisted on going, offered to go, denied closing, refused to accept, accused him of lying, admitted sharing, apologized for causing, promised to check, advised us to check, suggested asking</i>. They come back on page 3.</li>
<li>Also from the Linguahouse lesson: <i>according to, take down, deal with, misuse, critical</i>.</li></ol>""")

    # Page 3
    lean.grammar_in_class(b, grammar_ref.reporting_verbs)

    # Page 4 - Practice
    pc = [("Mr. Nunes denied", ["closing", "to close"], "closing", "the bakery."), ("Rafa promised", ["to check", "checking"], "to check", "messages first."),
          ("Ana warned us", ["not to share", "not sharing"], "not to share", "stories without a source."), ("A man accused him", ["of lying", "to lie"], "of lying", "."),
          ("Rafa apologized", ["for causing", "to cause"], "for causing", "confusion."), ("Bruno offered", ["to go", "going"], "to go", "with Mrs. Lima."),
          ("Mrs. Lima insisted", ["on going", "to go"], "on going", "there at once."), ("Ana suggested", ["asking", "us to ask"], "asking", "a simple question.")]
    cl = "".join(f"<li>{a} {ch(o, r)}{'' if z == '.' else ' '}{z}</li>" for a, o, r, z in pc)
    rw = [("\"I didn't start the rumor,\" said Rafa's cousin. (deny)", "Rafa's cousin denied starting the rumor."),
          ("\"Don't believe everything you read online,\" Ana told Danny. (warn)", "Ana warned Danny not to believe everything he read online."),
          ("\"OK, I sold a lot of bread on Tuesday,\" said Mr. Nunes. (admit)", "Mr. Nunes admitted selling a lot of bread on Tuesday.")]
    rwl = "".join(f'<li><i>{d}</i><br>{R(i) if T else lines(1)}</li>' for d, i in rw)
    use = ["Have you ever admitted doing something wrong? What happened?", "What did your parents always warn you not to do?",
           "Has anyone ever accused you of something you didn't do?", "What have you promised to do this year?",
           "What would you advise a friend to do before sharing a story?"]
    b.page(f"""{sec(4, "Practice: he denied it, she warned us", "10 min")}
{sub("A", "Choose the correct words.", "3 min")}
<ol style="line-height:1.7;font-size:8.6pt;margin:0;columns:2;column-gap:6mm">{cl}</ol>
{sub("B", "Report what they said. Use the verb in brackets.", "4 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0">{rwl}</ol>
{talk(use, "USE IT: ANSWER OUT LOUD")}""",
    30, """<ol><li>A: 3 minutes. Ask each time: <i>Which pattern does this verb take?</i> Item 8: <i>suggested us to ask</i> is wrong; <i>suggested that we ask</i> is also correct.</li>
<li>B: also accept <i>denied that he had started the rumor</i>, <i>admitted that he had sold</i>, and <i>admitted having sold</i>.</li>
<li>Use it: 3 minutes, all oral. When the student answers, report it back: <i>So you admitted breaking…</i></li></ol>""")

    # Page 5 - Speaking
    heads = [("SHARE NOW!!! All banks will close for a month starting tomorrow", "warning signs: capital letters, urgency, no source"),
             ("City library to open on Sundays from March, says the city hall website", "looks reliable: named source; check the website"),
             ("Doctors HATE this: drink this juice and never get sick again", "warning signs: clickbait, a health promise that is too good"),
             ("Free flights this Friday! Just click the link and enter your card number", "a scam: never enter card details from a message"),
             ("Neighborhood bakery wins prize for best cheese bread", "probably real, but check local news"),
             ("Photo shows snow on a beach in Rio this morning", "warning sign: the photo may be old or edited; search for the image")]
    hl = "".join(f"<li><b>{h}</b>{(' ' + R('→ ' + a)) if T else ''}</li>" for h, a in heads)
    b.page(f"""{sec(5, "Speaking: real or fake?", "18 min")}
<div class="box sand" style="margin-top:0"><h4>FUNCTIONAL LANGUAGE: TALKING ABOUT NEWS AND SOURCES</h4>
<table style="margin:0;font-size:8.2pt"><tr><th>asking</th><th>doubting</th><th>checking</th><th>reporting</th></tr>
<tr><td><i>Where did you see / hear that? · Who sent it? · Is that true?</i></td><td><i>I'm not sure that's true. · It sounds too good to be true. · I don't buy it.</i></td><td><i>Let's check the source. · According to… · It was confirmed by…</i></td><td><i>They claimed that… · He denied… · She warned people not to…</i></td></tr></table></div>
{audiocard(["58.2"])}
{sub("A", "Listen and repeat. Link the verb and the -ing form: denied_closing, admitted_sharing.", "2 min", "58.2")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S582))}</p>
{sub("B", "Spot the fake. Read the headlines. Which ones show warning signs? Which seem reliable? Explain why.", "6 min")}
<ol style="line-height:1.45;font-size:8.4pt;margin:0">{hl}</ol>
{sub("C", "Discuss. Can most people spot fake news? Are you worried about its power? What can we do about it?", "3 min")}
{sub("D", "Long turn. Tell your teacher about a time you (or someone you know) believed or shared a story that wasn't true. Use reporting verbs.", "4 min")}""",
    30, """<ol><li>B replaces the Linguahouse real-or-fake news pictures: all the headlines are invented, so the student judges the warning signs, not the facts. Ask: <i>What would you do to check it?</i></li>
<li>C and D come from the Linguahouse talking point. Last 3 minutes: wrap-up (two corrections, and ask <i>Can you now report what people said and judge if a story is reliable?</i>).</li></ol>""")

    # Homework
    il = [("Mrs. Lima only started using", "social media", "last year, and now she's in ten group chats."), ("If you don't know the answer, look it up", "online", "."),
          ("Many", "websites", "copy stories from other sites without checking them."), ("Our", "internet provider", "also sells TV and phone packages."),
          ("Danny wrote three", "posts", "about the bakery story on his blog."), ("Social networks should take down illegal", "content", "quickly.")]
    ibank = sorted(w for _, w, _ in il)
    ill = "".join(f'<li>{a} {A(w, "min-width:24mm")}{"" if z == "." else " "}{z}</li>' for a, w, z in il)
    pc2 = [(["sharing", "to share"], "sharing"), (["not to forward", "not forwarding"], "not to forward"), (["checking", "to check"], "checking"),
           (["for spreading", "to spread"], "for spreading"), (["to call", "calling"], "to call")]
    p = [ch(o, a) for o, a in pc2]
    b.page(f"""{sec("H", "Homework", "at home")}
{sub("A", "Internet language. Complete the sentences with the words from the box.", "")}
<div class="bank">{" · ".join(ibank)}</div>
<ol style="line-height:1.55;font-size:8.6pt;margin:0">{ill}</ol>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("B", "Ana writes to the family group. Choose the correct words.", "")}</div>{img('C', 30, 19)}</div>
<div class="box" style="line-height:1.85;font-size:8.8pt;margin:.5mm 0">Hi everyone! After the bakery story, I want to ask you something. Please avoid {p[0]} messages that say URGENT or SHARE NOW. Grandma, I'm warning you {p[1]} the ones about miracle cures! I recommend {p[2]} the source and the date first. Nobody will blame you {p[3]} a mistake once, but it's better to stop and think. And if you're not sure, remember {p[4]} me. I'm a doctor, not a website! Love, Ana</div>
{lean.watch_out([("She suggested me to check the source.", "She suggested checking the source.", "<i>suggest</i> + -ing or <i>suggest that</i> + clause, never <i>suggest someone to</i>."), ("I read a news about the bakery.", "I read a piece of news / a news story about the bakery.", "<i>news</i> is uncountable: no <i>a</i>, no plural."), ("Fake news are dangerous.", "Fake news is dangerous.", "<i>news</i> takes a singular verb.")])}
{lean.writing_task(sub, "Write a post for Danny's blog: how to spot fake news. Give at least four tips and report a story you heard about.", "Before you share a message, ask yourself…", ["at least four tips", "a short example story", "at least three reporting verbs (warn, admit, deny, suggest…)", "100–150 words"], "I can talk about fake news, report what people said and judge if a story is reliable.")}""",
    25, """<p>Check A and B in 3 minutes at the start of the next class. A comes from the Linguahouse internet language exercise, with new sentences. In B, point out <i>avoid + -ing</i>, <i>recommend + -ing</i> and <i>remember to</i> (a future action). Read the writing at home and choose two mistakes to discuss in class.</p>""")

    script = "".join(f"<p style='margin:.5mm 0'>{t}</p>" for t in S581)
    b.extra("Audio script", f"""
{sub("58.1", "Danny's blog: the day the bakery closed (natural and slow; read by Danny)")}
<p style="font-size:8.4pt">The audio is the text on page 2, read in full.</p>
{sub("58.2", "Repeat: reporting verbs")}
<p>{" · ".join(S582)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progress 58 - Fake news")
