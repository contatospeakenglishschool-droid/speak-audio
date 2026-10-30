# Speak! Bridge A2 - Unit 12 "Friendly emails" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 12", audio_json="audio_a2-unit-12.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-12"]
S122 = [x.split(": ", 1)[1] for x in _r["12.2 Repeat phrases"].split("\n")]
S123 = [x.split(": ", 1)[1] for x in _r["12.3 Repeat sentences"].split("\n")]
EMAIL_LINES = [x.split(": ", 1)[1] for x in _r["12.1 Email"].split("\n")]

# Carol's email with choices (letter, options, answer). {X} marks the place of each choice.
EMAIL = [
    "Hi Paulo,",
    "<u>It's great to hear from you!</u> Congratulations {A} your new tours in Brooklyn! What {B} the tourists like?",
    "<u>I'm writing to tell you that</u> I'm coming to New York next month, and I'd like {C} you if you're interested {D} showing me around.",
    "I'll be in the city from Friday to Sunday. We could go to that pizza place we {E} last year. Or maybe you have a new favorite place? <u>Let me know what you think.</u> I promise {F} on time this time!",
    "<u>Anyway, I have to go now.</u> I've {G} finished work, and I'm going to the gym. Did I tell you that I've given up {H} sugar? I haven't had any dessert {I} three weeks! And fruit {J} amazing now.",
    "<u>Love,</u><br>Carol"]
CH = {"A": (["on", "of"], "on"), "B": (["are", "do"], "are"), "C": (["to see", "seeing"], "to see"), "D": (["in", "about"], "in"),
      "E": (["went to", "have been to"], "went to"), "F": (["to be", "being"], "to be"), "G": (["just", "still"], "just"), "H": (["to eat", "eating"], "eating"),
      "I": (["for", "since"], "for"), "J": (["tastes", "is tasting"], "tastes")}


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: big photo + email vocabulary (abstract)
    cover = cover_html(T, "LEVEL A2 · UNIT 12", "Friendly emails", "Writing to friends · <b>email phrases + a review of Units 01–11</b>",
                       [("YOU CAN", "read and write a friendly email with the right phrases"),
                        ("LANGUAGE", "It's great to hear from you! · I'm writing to tell you… · Let me know… · Love, Carol"),
                        ("PRONUNCIATION", "weak to: looking forward to /tə/ · I'd like to")])
    vw = [("the place where your new emails arrive", "inbox"), ("the short title of an email", "subject"), ("add a file or a photo to an email", "attach"),
          ("answer an email", "reply"), ("send an email you received to another person", "forward"), ("emails you don't want, often ads", "spam")]
    vl = [f'<li value="{i+1}">{d} {A(w, "min-width:16mm")}</li>' for i, (d, w) in enumerate(vw)]
    b.page(f"""{sec(1, "Warm-up: you and your emails", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:56mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo('A')}" style="width:56mm;height:44mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "Email words. Complete with the words in the box.", "4 min")}
<div class="bank">attach · forward · inbox · reply · spam · subject</div>
<ol style="margin-top:1mm">{"".join(x.replace(f'<li value="{i+1}">', '<li>') for i, x in enumerate(vl))}</ol></div></div>
{sub("B", "Talk about it.", "4 min")}
<ol><li>How many times a day do you check your email? Do you use your phone or a computer?</li><li>Who do you write emails to: friends, family, colleagues? Do you prefer emails or messages?</li>
<li>How many emails are in your inbox right now? How many are spam?</li></ol>""",
    22, """<ol><li>A: also <b>CC</b> (send a copy), <b>sign off</b> (finish an email).</li>
<li>B: point out that emails are still essential at work, at university and in exams (Cambridge, IELTS General Training).</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Email vocabulary · email habits</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Carol's email to Paulo (with audio) · review of Units 01–11</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>The seven parts of a friendly email</td><td>3</td></tr>
<tr><td>+ Language reference</td><td>–</td><td>Friendly email phrases · informal or formal</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Email phrases · weak to</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Paulo's reply: cross out the extra words · Word builder: informal or formal</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Plan your reply · email or message?</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and writing homework (model + steps)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4><b>Carol</b> (Orlando) writes to her cousin <b>Paulo</b> in New York: she's visiting next month and wants him to show her around. She congratulates him on his new Brooklyn tours (Unit 06), suggests the pizza place they went to last year, and tells him she's given up sugar. Paulo replies in the Practice (he's busy on Friday, but suggests Saturday). The email reviews language from Units 01–11. Carol reads the email in the audio (voice: Chirp 3 HD Leda).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Translated email habits: <i>Dear Mr. Paulo</i> ✗ (first name with Mr.) → <b>Dear Paulo / Dear Mr. Silva</b>; <i>Waiting for your answer</i> ✗ → <b>I'm looking forward to hearing from you</b>; <i>Kisses</i> ✗ → <b>Love,</b>; the abbreviation for "regards" ✗ → <b>Best regards,</b>; <i>I'm writing to say about</i> ✗ → <b>to tell you about</b>; <i>looking forward to see</i> ✗ → <b>seeing</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 12.1 Carol's email (slow and natural) · Track 12.2 Email phrases · Track 12.3 Sentences</div>""")

    # Page 2: reading
    def fill(t):
        for k, (o, a) in CH.items():
            t = t.replace("{" + k + "}", f"<sup>{k}</sup>{ch(o, a)}")
        return t
    em = "".join(f"<p style='margin:0 0 1.2mm'>{fill(x)}</p>" for x in EMAIL)
    gist = [("What's the relationship between Carol and Paulo?", "They're cousins."), ("Why is Carol writing?", "She's coming to New York next month and wants to meet / wants him to show her around."),
            ("What's her interesting news?", "She's given up eating sugar.")]
    gl = "".join(f"<li>{q} {R(a)}</li>" for q, a in gist)
    b.page(f"""{sec(2, "Reading: an email from Carol", "10 min")}
<p>Carol, Ana's cousin in Orlando, writes to Paulo, who lives in New York. They're cousins too!</p>
{audiocard(["12.1 · SLOW", "12.1 · NATURAL"])}
<div style="border:1pt solid #c9dfe3;border-radius:2mm;padding:2mm 4mm;margin:1mm 0;font-size:9pt;line-height:1.55">
<div style="font-size:7pt;font-weight:800;letter-spacing:.14em;color:#7d858a">FROM: Carol · TO: Paulo · SUBJECT: New York next month!</div>{em}</div>
{sub("A", "Read quickly and answer.", "3 min", "12.1 · SLOW")}
<ol>{gl}</ol>
{sub("B", "Read again and choose the correct options A–J. Then listen and check.", "5 min", "12.1 · NATURAL")}
<p class="small">Which options review… a preposition after a noun or adjective (Unit 04)? {R("A, D")} · a question with like (01)? {R("B")} · verb + to / -ing (02)? {R("C, F, H")} · a state verb (03)? {R("J")} · the present perfect (07–11)? {R("G, I")} · the past simple with a finished time (08)? {R("E")}</p>""",
    20, """<p>A: skim first (2 minutes). B: the email reviews Units 01–11: ask the student to explain each choice. The underlined phrases are the set email phrases of page 3.</p>""")

    # Page 3
    parts = [("greeting", "Hi Paulo,"), ("opening", "It's great to hear from you!"), ("reason for writing", "I'm writing to tell you that…"),
             ("call to action", "Let me know what you think."), ("closing", "Anyway, I have to go now."), ("sign-off", "Love, Carol")]
    pt = "".join(f"<tr><td style='width:36mm'><b>{p}</b></td><td>{A(x, 'min-width:50mm')}</td></tr>" for p, x in parts)
    b.page(f"""{sec(3, "Language focus: the parts of a friendly email", "10 min")}
{sub("A", "Find the underlined phrases in Carol's email. Write them next to their job.", "4 min")}
<table style="table-layout:fixed;margin-top:0;font-size:9pt">{pt}</table>
{sub("B", "Choose the correct option.", "3 min")}
<ol><li>In a friendly email, we use {ch(["first names", "last names"], "first names")} and a {ch(["comma", "period"], "comma")} after the greeting.</li>
<li>The most important part is the {ch(["opening", "reason for writing"], "reason for writing")}.</li>
<li>The {ch(["call to action", "closing"], "call to action")} tells the reader what to do next.</li>
<li><i>Love,</i> is for {ch(["family and close friends", "your boss"], "family and close friends")}.</li></ol>
{sub("C", "Put the parts of an email in order (1–6).", "3 min")}
<div class="bank" style="background:#fff">☐ {R("5")} I'm looking forward to seeing you. · ☐ {R("1")} Hello Megan, · ☐ {R("3")} I just wanted to ask you about your trip. · ☐ {R("6")} Take care, Tom · ☐ {R("2")} I hope you're doing well. · ☐ {R("4")} Send me the details.</div>
<p class="small">All the phrases, plus formal emails, are on the next page: <b>Language reference</b>.</p>""",
    24, """<ol><li>A: the email has six of the seven parts' phrases underlined; the "details / news" part has no fixed phrase.</li>
<li>C: Tom writes to Megan (Unit 09). Ask the student to read it aloud in the correct order.</li></ol>""")

    grammar_ref.friendly_emails(b)

    # Page 4 (now 5)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't write</th><th>Write</th><th>Why?</th></tr>
<tr><td>Dear Mr. Paulo,</td><td><b>Dear Paulo,</b> / <b>Dear Mr. Silva,</b></td><td>Mr. + last name.</td></tr>
<tr><td>Waiting for your answer.</td><td><b>I'm looking forward to hearing from you.</b></td><td>set phrase.</td></tr>
<tr><td>Kisses, Carol</td><td><b>Love, Carol</b></td><td>English sign-off.</td></tr>
<tr><td>I'm writing to say about my trip.</td><td><b>I'm writing to tell you about my trip.</b></td><td>tell someone about.</td></tr>
<tr><td>I'm looking forward to see you.</td><td><b>I'm looking forward to seeing you.</b></td><td>to + -ing here.</td></tr>
<tr><td>Call to me later.</td><td><b>Call me later.</b></td><td>no preposition.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["12.2", "12.3"])}
{sub("A", "Email phrases. Listen and repeat. Sound friendly!", "2 min", "12.2")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S122)}</div>
{sub("B", "Sentences. Listen and repeat. To is weak: /tə/.", "2 min", "12.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S123)}</div>
<div class="box" style="margin-top:1mm"><h4>WEAK TO, LINKED WORDS</h4><i>I'd like to</i> = "I'd like-tə" · <i>looking forward to</i> = "looking forwar-də" · <i>hear from you</i> = "hear-frəm-you". Stress the important words: <i>It's <b>GREAT</b> to <b>HEAR</b> from you!</i></div>""",
    24, """<ol><li>4A: these phrases also work in voice messages and phone calls.</li>
<li>4B: Brazilians often pronounce <i>to</i> as a full /tu/; keep it short.</li></ol>""")

    # Page 5 (now 6)
    rp = [("Hello <s>to</s> Carol,", "to"), ("Thanks <s>you</s> a lot for writing!", "you"), ("I'm writing to <s>say</s> tell you that I'd love to see you.", "say"),
          ("I'm busy on Friday, and I'm worried about <s>to</s> finishing a big project.", "to"), ("I've worked here <s>since</s> for six months, and it's crazy!", "since"),
          ("Let me <s>to</s> suggest Saturday.", "to"), ("I've <s>still</s> walked past a new pizza place a few times.", "still"), ("It always <s>can</s> smells delicious.", "can"),
          ("Call <s>to</s> me later.", "to"), ("I'm looking forward to seeing <s>of</s> you.", "of"), ("Take care <s>of</s>,<br>Paulo", "of")]
    def line(t):
        import re
        return re.sub(r"<s>(.*?)</s>", (lambda m: f"<s style='color:#c0392b'>{m.group(1)}</s>") if T else (lambda m: m.group(1)), t)
    rpl = "".join(f"<p style='margin:0 0 .8mm'><sup>{i+1}</sup> {line(t)}</p>" for i, (t, _) in enumerate(rp))
    fi = [("Hi Carol,", "Dear Ms. Clark,"), ("Thanks a lot for writing!", "Thank you for your email."), ("Let me know.", "Please let me know."),
          ("I'm looking forward to seeing you!", "I look forward to hearing from you."), ("Take care,", "Best regards,")]
    fil = "".join(f"<tr><td>{a}</td><td>{A(b_, 'min-width:46mm')}</td></tr>" for a, b_ in fi)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Paulo's reply. Each line has one extra word. Cross it out.", "4 min")}
<div style="border:1pt solid #c9dfe3;border-radius:2mm;padding:2mm 4mm;font-size:9pt;line-height:1.45">{rpl}</div>
{sub("B", "Word builder: friendly or formal? Write the formal phrase from the box.", "4 min")}
<div class="bank">Best regards, · Dear Ms. Clark, · I look forward to hearing from you. · Please let me know. · Thank you for your email.</div>
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>friendly</th><th>formal</th></tr>{fil}</table>""",
    22, """<ol><li>A: some lines review older units: 4 (Unit 04: preposition + -ing), 5 (09: for), 7 (11: still), 8 (03: smells). Ask the student to read the corrected email aloud.</li>
<li>B: formal emails use full names, no contractions and <i>I look forward to hearing from you</i>.</li></ol>""")

    # Page 6 (now 7)
    plan = [("greeting", ""), ("opening", ""), ("answer her questions", "Which activities? Are you still a vegetarian?"), ("your own idea", ""), ("call to action", ""), ("closing + sign-off", "")]
    plt = "".join(f"<tr><td style='width:42mm'><b>{p}</b><br><span class='small'>{h}</span></td><td style='height:8mm'></td></tr>" for p, h in plan)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Read the email from your friend Emma. Then plan your reply with your teacher. Say your ideas aloud before you write.", "8 min")}
<div class="msg" style="max-width:none;padding:2mm 4mm;font-size:9pt;line-height:1.5">Hi! I hope you're doing well. I'm so happy you're coming to visit me in Chicago next week! I'm writing to ask what you'd like to do. We could go to Millennium Park, take a boat tour on the river or go shopping. There's also a great pizza place near my apartment. Are you still a vegetarian? Tell me what you'd like to do. I'm looking forward to seeing you! Love, Emma</div>
<table style="table-layout:fixed;margin-top:1mm;font-size:9pt">{plt}</table>
{sub("B", "Email or message?", "4 min")}
<ol><li>When do you prefer to send an email? When do you send a text message?</li><li>Have you ever sent an email to the wrong person? What happened?</li></ol>""",
    26, """<ol><li>A: the student plans orally, part by part, using the Language reference. Don't write the full email yet: that's the homework (page 8).</li>
<li>Millennium Park and the Chicago river boat tours are real attractions in Chicago.</li></ol>""")

    # Page 7 (now 8)
    pc = [("A2 Unit 07", "I can talk about accidents that just happened with the present perfect."), ("A2 Unit 08", "I can ask about life experiences and give details with the past simple."),
          ("A2 Unit 09", "I can say how long things have been true with for and since."), ("A2 Unit 11", "I can check what's done and not done with already, yet and still."),
          ("A2 Unit 12", "I can write a friendly email with the right phrases.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    model = ("Hi Emma,<br>Thanks a lot for writing! I'm so excited about my trip. I'd love to go to Millennium Park and take the boat tour. "
             "And yes, I'm still a vegetarian, so the pizza place sounds perfect! Could we also visit the Art Institute? Let me know what you think. "
             "I'm looking forward to seeing you!<br>Love, Lia")
    steps = ["Greeting + opening (Hi…, Thanks a lot for writing!)", "Answer every question in the email", "Add one idea of your own", "Call to action (Let me know… / Send me…)", "Closing + sign-off (I'm looking forward to… / Love,)", "Check: commas, contractions, 50–75 words"]
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework: reply to Emma (50–75 words)", "1 min")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.6pt;line-height:1.45"><b>Model</b><br>{model}</div>
<div><p class="small" style="margin:0"><b>Step by step</b></p><ol class="small" style="margin-top:.5mm">{"".join(f"<li>{s}</li>" for s in steps)}</ol></div></div>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: check the email part by part with the Language reference (page 4). Mark the set phrases first, then grammar. The Art Institute of Chicago is a real museum.</p>""")

    b.extra("Audio scripts", f"""
{sub("12.1", "Carol's email (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(EMAIL_LINES)}</p>
{sub("12.2", "Email phrases")}
<p>{" · ".join(S122)}</p>
{sub("12.3", "Sentences")}
<p>{" ".join(S123)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 12 - Friendly emails")
