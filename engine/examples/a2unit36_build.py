# Speak! Bridge A2 - Unit 36 "Work emails" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 36", audio_json="audio_a2-unit-36.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-36"]
S361 = [x.split(": ", 1)[1] for x in _r["36.1 An email from Maya"].split("\n")]
S362 = [x.split(": ", 1)[1] for x in _r["36.2 Repeat: email phrases"].split("\n")]
S363 = [x.split(". ", 1)[1] for x in [y.split(": ", 1)[1] for y in _r["36.3 Formal or informal?"].split("\n")]]

EMAIL_SVG = """<svg viewBox="0 0 520 190" width="100%" height="50mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="4" y="4" width="512" height="182" rx="6" fill="#fff" stroke="#9fb7bd" stroke-width="1.2"/>
<rect x="4" y="4" width="512" height="24" rx="6" fill="#176074"/><rect x="4" y="18" width="512" height="10" fill="#176074"/>
<text x="16" y="21" font-size="11" fill="#fff" font-weight="600">New message</text>
<text x="490" y="21" font-size="12" fill="#fff">✕</text>
<g font-size="10" fill="#555"><text x="16" y="46">To</text><text x="50" y="46" fill="#222">paulo@…</text><text x="470" y="46">Cc Bcc</text>
<line x1="12" y1="53" x2="508" y2="53" stroke="#ddd"/>
<text x="16" y="70" fill="#222" font-weight="600">Meeting next Tuesday</text>
<line x1="12" y1="77" x2="508" y2="77" stroke="#ddd"/></g>
<g stroke="#cfd8da" stroke-width="5" stroke-linecap="round"><line x1="20" y1="94" x2="380" y2="94"/><line x1="20" y1="108" x2="440" y2="108"/><line x1="20" y1="122" x2="300" y2="122"/><line x1="20" y1="136" x2="350" y2="136"/></g>
<rect x="16" y="152" width="58" height="24" rx="12" fill="#176074"/><text x="45" y="168" font-size="11" fill="#fff" text-anchor="middle" font-weight="600">Send</text>
<g fill="none" stroke="#333" stroke-width="1.6">
<path d="M104 170 L104 157 a4 4 0 0 1 8 0 L112 172 a6 6 0 0 1 -12 0 L100 158"/>
<rect x="140" y="155" width="20" height="16" rx="2"/><path d="M142 169 L148 161 L152 166 L155 163 L159 169"/>
<circle cx="194" cy="164" r="9"/><circle cx="191" cy="161" r="1" fill="#333"/><circle cx="197" cy="161" r="1" fill="#333"/><path d="M189 166 a5 5 0 0 0 10 0"/>
<rect x="472" y="157" width="16" height="17" rx="2"/><line x1="468" y1="157" x2="492" y2="157"/><line x1="476" y1="153" x2="484" y2="153"/></g>
<g font-size="10" font-weight="700" fill="#fff">
<circle cx="250" cy="66" r="9" fill="#c0392b"/><text x="250" y="70" text-anchor="middle">1</text>
<circle cx="106" cy="141" r="9" fill="#c0392b"/><text x="106" y="145" text-anchor="middle">2</text>
<circle cx="150" cy="141" r="9" fill="#c0392b"/><text x="150" y="145" text-anchor="middle">3</text>
<circle cx="194" cy="141" r="9" fill="#c0392b"/><text x="194" y="145" text-anchor="middle">4</text>
<circle cx="480" cy="141" r="9" fill="#c0392b"/><text x="480" y="145" text-anchor="middle">5</text></g>
</svg>"""


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(l, opts, ans):
        return f"<sup><b>{l}</b></sup><b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def ul(x):
        return f'<span style="text-decoration:underline">{x}</span>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 36", "Work emails", "Writing at work · <b>email phrases, semi-formal and formal style</b>",
                       [("YOU CAN", "read and write a clear, polite work email with a greeting, a reason for writing and a call to action"),
                        ("LANGUAGE", "I'm writing to let you know… · Could you help her…? · Please let me know if… · I look forward to hearing from you."),
                        ("PRONUNCIATION", "polite email phrases · formal or informal?")])
    icons = [("the subject line", "1"), ("the paper clip", "2"), ("the mountains", "3"), ("the smiley face", "4"), ("the trash can", "5")]
    il = " · ".join(f"{w} {A(n, 'min-width:6mm;text-align:center')}" for w, n in icons)
    uses = [("attach a document", "2"), ("attach a photo", "3"), ("choose an emoji", "4"), ("delete the email", "5"), ("write what the email is about", "1")]
    ul_ = " · ".join(f"{w} {A(n, 'min-width:6mm;text-align:center')}" for w, n in uses)
    b.page(f"""{sec(1, "Warm-up: emails at work", "8 min")}
{sub("A", "Look at the email window. Write the numbers 1–5 next to the words.", "2 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{EMAIL_SVG}</div>{img('A', 36, 30)}</div>
<p style="margin:.5mm 0;font-size:9pt;line-height:1.7">{il}</p>
<p style="margin:0 0 .5mm;font-size:9pt;line-height:1.7"><b>Which number do you click or use to…</b> {ul_}</p>
{sub("B", "What's the difference?", "3 min")}
<ol style="margin:0;line-height:1.5"><li><b>reply</b> to an email and <b>forward</b> an email {A("reply = answer the sender; forward = send it on to another person", "min-width:20mm")}</li>
<li><b>CC</b> and <b>BCC</b> {A("CC: everyone can see who got a copy; BCC: the other people can't see it", "min-width:20mm")}</li></ol>
{sub("C", "Talk about it.", "3 min")}
<p style="margin:0">Do you write many emails at work or in your studies? Who to? In Brazil, do people use email or WhatsApp more at work? Why?</p>""",
    22, """<ol><li>A: <i>icon</i> /ˈaɪkɑːn/ = a small picture you click on a screen. <i>Attach</i> a file, an <i>attachment</i>.</li>
<li>B: CC = carbon copy, BCC = blind carbon copy. In many US offices, email is still the main channel for work; texting apps are for quick, informal messages.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Email vocabulary: subject line, attach, reply, forward, CC</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Maya's email to Paulo about a sales meeting (audio 36.1)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>A2 grammar review · the six parts of a work email</td><td>3</td></tr>
<tr><td>+ Language reference</td><td>–</td><td>Writing work emails: phrases and style</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Polite email phrases · formal or informal?</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Paulo's reply: cross out the extra word · subject lines</td><td>6</td></tr>
<tr><td>6 Writing and speaking</td><td>12 min</td><td>Answer questions on a call, then reply to an email</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo (Neural2-I) works at a travel agency in New York with his colleague Maya (Studio-O; Units 06 and 32). Paulo missed a team meeting, so Maya emails him about next Tuesday's sales meeting: Linda Brooks from the agency's head office in Boston is coming to give a talk. Paulo replies (Practice), and Linda writes to Maya (Homework). Linda, the head office and the meeting are invented. Penn Station is New York's main station for trains to Boston. Audio 36.1 is Maya reading her email aloud; the unit is a reading lesson, as in Linguahouse.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students write <i>Dear Ms. Linda</i> (title + first name), <i>Hi dear</i>, <i>I look forward to hear</i>, forget the call to action, and use very personal sign-offs. They also write one long paragraph.</div>
<div class="box"><h4>AUDIO</h4>Track 36.1 An email from Maya (slow and natural) · Track 36.2 Repeat: email phrases · Track 36.3 Formal or informal?</div>""")

    # Page 2
    gist = [("What's the relationship between Maya and Paulo?", "They're colleagues."), ("Why is Maya writing?", "to tell Paulo about the arrangements for the sales meeting"),
            ("Is the email formal, semi-formal or informal?", "semi-formal: friendly but professional, no contractions"), ("What does Paulo need to do?", "say if he's happy with the arrangements")]
    gl = "".join(f"<li>{q} {A(a, 'min-width:30mm')}</li>" for q, a in gist)
    email = f"""<div class="msg" style="max-width:none;padding:2.5mm 4mm;font-size:9pt;line-height:1.55;background:#fff;border:.8pt solid #c9dfe3">
<div class="small" style="color:#555;border-bottom:.6pt solid #ddd;margin-bottom:1.5mm;padding-bottom:1mm"><b>From:</b> Maya · <b>To:</b> Paulo · <b>Subject:</b> Sales meeting next Tuesday</div>
{ul("Hi Paulo,")}<br>
{ul("As you missed the last team meeting,")} I {ch("A", ["write", "am writing"], "am writing")} {ul("to let you know about")} the arrangements for next week's sales meeting. It {ch("B", ["starts", "starting"], "starts")} at 10:00 on Tuesday. Linda Brooks from our head office in Boston {ch("C", ["comes", "is coming"], "is coming")} to speak to us. I am meeting her at Penn Station at 9:00.<br>
Just like last year, we {ch("D", ["will", "are going to"], "are going to")} serve coffee and bagels from around 9:45. How about getting the bagels from that nice bakery near the office? Let's make sure we show Linda what a friendly team we are. {ch("E", ["Could", "May"], "Could")} you help her get ready for her talk? {ch("F", ["There are", "There is"], "There is")} a big screen in the meeting room, so she just needs to bring her slides.<br>
I am worried that Linda {ch("G", ["might", "can"], "might")} get a bit {ch("H", ["tiring", "tired"], "tired")} in the afternoon, and she has a long trip back to Boston, so why don't we try to finish early?<br>
{ul("Please let me know if you are happy with these arrangements.")} {ul("I am really looking forward to Tuesday.")} I have heard great things about Linda, so I think it is {ch("I", ["being", "going to be"], "going to be")} really {ch("J", ["interesting", "interested"], "interesting")}.<br>
{ul("Kind regards,")}<br>{ul("Maya")}</div>"""
    b.page(f"""{sec(2, "Reading: an email from Maya", "10 min")}
<div style="display:flex;gap:2.5mm;align-items:center"><p style="flex:1;margin:0">Paulo works at a travel agency in New York. He missed the last team meeting, so his colleague Maya is writing to him.</p>{img('B', 26, 18)}{img('C', 26, 18)}</div>
{sub("A", "Read the email quickly. Answer the questions.", "3 min")}
<ol style="margin:0;line-height:1.5;font-size:9pt">{gl}</ol>
{sub("B", "Read again and choose the best option in A–J. Then listen and check.", "5 min", "36.1 · NATURAL")}
{email}
{audiocard(["36.1 · SLOW", "36.1 · NATURAL"])}
{sub("C", "What three suggestions does Maya make?", "2 min")}
<p class="small" style="margin:0">{A("How about getting the bagels…? · Let's make sure we show Linda… · Why don't we try to finish early?", "min-width:80mm")}</p>""",
    24, """<ol><li>A: <i>semi-formal</i>: first names, but no contractions (<i>I am, it is</i>), so the style is professional.</li>
<li>B: many options review Units 25–34. The underlined phrases are for the Language focus. Bagels are a New York classic.</li></ol>""")

    # Page 3
    lp = [("a description of what you can find in a place", "F, There is"), ("a prediction based on evidence", "I, going to be"), ("a prediction that is not certain", "G, might"),
          ("a request for someone to do something", "E, Could"), ("a timetable", "B, starts"), ("an action happening around now", "A, am writing"),
          ("an adjective for a situation (how it makes us feel)", "J, interesting"), ("an adjective for someone's feelings", "H, tired"),
          ("an arrangement with another person", "C, is coming"), ("an intention or plan", "D, are going to")]
    lpl = [f'<li value="{i+1}">{s} {A(a, "min-width:22mm")}</li>' for i, (s, a) in enumerate(lp)]
    fn = [("greeting the reader", "Hi Paulo,"), ("opening: a recent event", "As you missed the last team meeting,"), ("reason for writing", "I am writing to let you know about…"),
          ("call to action: what the reader needs to do", "Please let me know if you are happy with these arrangements."), ("closing: a future event", "I am really looking forward to Tuesday."), ("signing", "Kind regards, Maya")]
    fnl = "".join(f"<tr><td style='width:62mm'><b>{i+1}</b> {f}</td><td>{A(p, 'min-width:70mm')}</td></tr>" for i, (f, p) in enumerate(fn))
    b.page(f"""{sec(3, "Language focus: a work email", "10 min")}
{sub("A", "Grammar review. Match your answers A–J from the email with these uses.", "4 min")}
<div style="font-size:8.6pt">{twocol(lpl, 6)}</div>
{sub("B", "The six parts of an email. Find the underlined phrases in Maya's email and write them.", "4 min")}
<table style="margin:0;font-size:8.8pt">{fnl}</table>
{sub("C", "How many paragraphs does Maya use? What's the topic of each one?", "2 min")}
<p class="small" style="margin:0">{A("Four: 1 the basic details of the meeting · 2 the arrangements on the day · 3 finishing early · 4 call to action and closing", "min-width:80mm")}</p>
<div class="box sand"><h4>RULE</h4>A good work email has a <b>greeting</b>, an <b>opening</b>, a <b>reason for writing</b>, a <b>call to action</b> (what the reader needs to do), a <b>closing</b> and a <b>signature</b>. Use <b>one paragraph for each topic</b>. <i>look forward to</i> + noun or verb-ing: <i>I look forward to hearing from you.</i> More on the next page: <b>Language reference</b>.</div>""",
    20, """<ol><li>A: a quick review of Units 25–34; skip it if time is short.</li>
<li>B: the student copies the phrases exactly, with the commas: accurate set phrases make a good impression.</li></ol>""")

    grammar_ref.work_emails(b)

    # Page 5
    fi = ["F", "I", "F", "I", "F", "I"]
    fil = "".join(f"<li>{A(f, 'min-width:10mm;text-align:center')}</li>" for f in fi)
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Dear Ms. Linda,</td><td><b>Dear Ms. Brooks,</b></td><td>title + last name.</td></tr>
<tr><td>Hi dear Paulo,</td><td><b>Hi Paulo,</b></td><td>don't mix hi and dear.</td></tr>
<tr><td>I look forward to hear from you.</td><td><b>I look forward to hearing from you.</b></td><td>to + verb-ing.</td></tr>
<tr><td>I write to inform about the meeting.</td><td><b>I'm writing to let you know about the meeting.</b></td><td>a natural phrase.</td></tr>
<tr><td>Kisses, Paulo</td><td><b>Best, Paulo</b></td><td>too personal for work.</td></tr>
<tr><td>(no call to action)</td><td><b>Please let me know by Friday.</b></td><td>say what you need.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["36.2", "36.3"])}
{sub("A", "Listen and repeat. Sound polite and professional.", "2 min", "36.2")}
{twocol([f'<li value="{i+1}">{s}</li>' for i, s in enumerate(S362)], 4)}
{sub("B", "Listen to six phrases from emails. Are they formal (F) or informal (I)?", "2 min", "36.3")}
<ol style="line-height:1.5;column-count:3;column-gap:5mm">{fil}</ol>""",
    29, """<ol><li>A: people often read work emails aloud in meetings or on calls. Stress: <i>I'm WRITing to let you KNOW…</i>; <i>looking forward to</i> links: /ˈlʊkɪŋ ˈfɔːrwərd tə/.</li>
<li>B: script: 1 Dear Ms. Brooks. 2 Hey! What's up? 3 I would like to ask you about the invoice. 4 Thanks a lot! See you soon! 5 Sincerely. 6 Talk soon!</li></ol>""")

    # Page 6
    def x(w):
        return R(f"<s>{w}</s>") if T else w
    reply = f"""<div class="msg" style="max-width:none;padding:2.5mm 4mm;font-size:9pt;line-height:1.6;background:#fff;border:.8pt solid #c9dfe3">
<b>(1) Hi {x("dear")} Maya,</b><br>
<b>(2) {x("I")} thank you for your email</b> about the arrangements for the meeting. <b>(3) I am writing {x("it")} to confirm</b> your suggestions. First of all, I think it is a great idea to have coffee and bagels ready for Ms. Brooks when she arrives. However, I think we should get the bagels from a different place. The bakery near the office is <b>(4) too {x("much")} expensive</b>. <b>(5) Let's {x("us")} try</b> the deli across the street. I am very happy to help Ms. Brooks get ready for her talk. <b>(6) I am {x("often")} going down</b> to the meeting room later today to meet a client, so I can check the computer and the screen then. Finally, I agree that we should try to finish early. <b>(7) I will {x("to")} check</b> the train times to Boston for Ms. Brooks, so we have an idea about when we should finish. I will let you know what the options are. <b>(8) I am looking {x("up")} forward</b> to the meeting too.<br>
<b>(9) All the best {x("wishes")},</b><br><b>(10) {x("From:")} Paulo</b></div>"""
    sl = [("command", "Keep your workspace clean"), ("hurry up", "Don't miss your chance to book vacation days!"), ("information", "Sales meeting: Tuesday, 10:00 a.m."),
          ("instructions", "How to use the new time sheet"), ("list", "5 things to do before our team review"), ("personal", "Great to meet you last week!"),
          ("question", "Have you done your safety training?"), ("statistics", "45% of workers have tired eyes from screens")]
    ex = sorted(e for _, e in sl)
    sll = "".join(f"<li>{t} {A('abcdefgh'[ex.index(e)], 'min-width:6mm;text-align:center')}</li>" for t, e in sl)
    exl = "".join(f"<li>{e}</li>" for e in ex)
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "Read Paulo's reply. Each phrase in bold has one extra word. Cross it out.", "4 min")}
{reply}
<p class="small" style="margin:.8mm 0">Paulo didn't use paragraphs. Where should each new paragraph start? {A("Thank you… / First of all, … / I am very happy… / Finally, … / I will let you know…", "min-width:60mm")}</p>
{sub("B", "Subject lines. Match the types 1–8 with the examples a–h.", "4 min")}
<div style="display:flex;gap:4mm;font-size:8.8pt"><ol style="flex:.7;line-height:1.5;margin:0">{sll}</ol><ol type="a" style="flex:1.3;line-height:1.5;margin:0">{exl}</ol></div>
<p class="small" style="margin:.8mm 0">Write a better subject line for Paulo's reply. {A("e.g. Re: Sales meeting: bagels, screen and trains", "min-width:50mm")}</p>""",
    22, """<ol><li>A: do number 1 together. Then the student works from memory before checking the Language focus. A <i>deli</i> (delicatessen) is a shop that sells sandwiches, meat and cheese.</li>
<li>B: <i>Re:</i> at the start of a subject line means it's a reply.</li></ol>""")

    # Page 7
    mark = """<div class="msg" style="max-width:none;padding:2.5mm 4mm;font-size:9pt;line-height:1.55;background:#fff;border:.8pt solid #c9dfe3">
<div class="small" style="color:#555;border-bottom:.6pt solid #ddd;margin-bottom:1.5mm;padding-bottom:1mm"><b>From:</b> Mark Ellis · <b>Subject:</b> Your customer survey</div>
Hello,<br>It was good to meet you when you came to the head office last week. I am writing to ask you for more details about the customer survey that you told us about. I am interested because my team did a similar project last year.<br>
First of all, when are you starting to interview customers? How many people do you think you will speak to? I can share some customer contact details with you if you need more people.<br>
Also, could you let us know if you are going to talk to customers face to face or online?<br>
It sounds like we are doing very similar things, so let's keep in touch. I look forward to hearing from you.<br>Regards,<br>Mark Ellis</div>"""
    b.page(f"""{sec(6, "Writing and speaking: reply to an email", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">{mark}</div>{img('D', 30, 36)}</div>
{sub("A", "Read and answer: Who is Mark? Why is he writing? What do you need to tell him?", "2 min")}
<p class="small" style="margin:0">{A("a colleague from head office you met last week · he wants details about your survey · when you start, how many people, face to face or online, and if you want his contacts", "min-width:80mm")}</p>
{sub("B", "Mark calls you. Your teacher is Mark: answer his questions. Invent the details.", "3 min")}
<p class="small" style="margin:0">{R("Teacher as Mark: Hi! Thanks for taking my call. So, when are you starting the interviews? … How many customers are you going to talk to? … Face to face or online? … Do you need more contacts?") if T else "When are you starting? · How many customers? · Face to face or online? · Do you need more contacts?"}</p>
{sub("C", "Now write your reply to Mark (70–90 words). Use the six parts of an email and paragraphs.", "7 min")}
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>B: the call lets the student plan the content orally before writing; use the future forms from Units 32–34 (<i>We're starting on May 2. I think we'll talk to about fifty people.</i>).</li>
<li>C: check the six parts, the paragraphs and the call to action first, then the grammar. The student can finish at home.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 33", "I can make predictions and say how sure I am."), ("A2 Unit 34", "I can choose the right future form: going to, will or the present continuous."),
          ("A2 Unit 35", "I can make suggestions and offers when I plan a day out."), ("A2 Unit 36", "I can write a clear, polite work email.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    order = ["Dear Maya,", "I was so pleased to receive the invitation to speak at your meeting.", "I am just writing to check some of the arrangements.",
             "First of all, there has been a change in my travel plans.", "I am going to drive to New York, so you don't need to meet me at the station.",
             "However, could you tell me the best place to park?", "I am also a little worried about the meeting room.", "I am going to show some slides during my talk.",
             "Could you confirm that I can use the company intranet on that computer?", "Thank you for your help.",
             "I'm looking forward to your reply and, of course, to seeing you next week.", "Best wishes,", "Linda"]
    sh = sorted(order[1:])
    ol = f"<li>{order[0]} <b>1</b></li>" + "".join(f"<li>{s} {A(str(order.index(s) + 1), 'min-width:6mm;text-align:center')}</li>" for s in sh)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p style="margin:.5mm 0"><b>1. Linda writes to Maya. Put her email in order (1–13).</b></p>
<ul style="line-height:1.45;font-size:8.8pt;list-style:none;padding-left:2mm;margin:0">{ol}</ul>
<p style="margin-top:1.5mm"><b>2. An email to a colleague (50–75 words).</b> Invite a colleague to a meeting next week. Give the day, time and place, ask them to bring something, and include a call to action.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Paragraphs in Linda's email: I was so pleased… / First of all… / I am also… / Thank you for your help. Next class: check the order, then read the student's invitation and reply to it as the colleague.</p>""")

    b.extra("Audio script", f"""
{sub("36.1", "An email from Maya (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(S361)}</p>
{sub("36.2", "Repeat: email phrases")}
<p>{" · ".join(S362)}</p>
{sub("36.3", "Formal or informal? (3-second pause)")}
<p>{" · ".join(S363)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 36 - Work emails")
