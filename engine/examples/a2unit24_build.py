# Speak! Bridge A2 - Unit 24 "Writing a story" (all English, writing lesson) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 24", audio_json="audio_a2-unit-24.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-24"]
S241 = [x.split(": ", 1)[1] for x in _r["24.1 Pepper is a winner"].split("\n")]
S242 = [x.split(": ", 1)[1] for x in _r["24.2 Repeat: telling a story"].split("\n")]
S243 = [x.split(": ", 1)[1] for x in _r["24.3 My dog saved my life"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans, letter=""):
        lab = f"<sup><b>{letter}</b></sup>" if letter else ""
        return lab + "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def box(ans, w=7):
        return A(ans, f"min-width:{w}mm;text-align:center") if T else f'<span style="display:inline-block;width:{w}mm;border-bottom:.8pt solid #555">&nbsp;</span>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 24", "Writing a story", "Stories and storytelling · <b>A2 language in a story</b>",
                       [("YOU CAN", "plan, tell and write a short story of about 100 words"),
                        ("LANGUAGE", "Suddenly, … · At first, … but then … · \"Don't go in there,\" he shouted."),
                        ("PRONUNCIATION", "pauses and stress when you tell a story")])
    titles = ["The million-dollar dog", "My dog saved my life!", "The greedy dog", "My dog is a winner"]
    col = [("Don't read this", "story when you're alone in the house at night!", "ghost"),
           ("I have to tell you this", "story. It really made me laugh.", "funny"),
           ("I was reading an", "story about a trip to the Amazon, and I didn't sleep until midnight.", "adventure"),
           ("She reads every", "story and always guesses who did it.", "detective"),
           ("My nephew likes to", "crazy stories about his toys.", "make up"),
           ("Grandma, can you", "us a story about when you were young?", "tell")]
    coll = "".join(f"<li>{a} {A(w, 'min-width:18mm')} {e}</li>" for a, e, w in col)
    b.page(f"""{sec(1, "Warm-up: stories", "8 min")}
{sub("A", "Look at the story titles. What do you think happens in each story?", "3 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1"><ul style="margin:0;line-height:1.6;font-weight:600">{"".join(f"<li>{t}</li>" for t in titles)}</ul>
<p class="small" style="margin:1mm 0 0">Which story sounds the most interesting? Which could be true? (<b>greedy</b> = wanting more than you need)</p></div>{img('D', 44, 30)}</div>
{sub("B", "Story collocations. Complete the sentences with the words in the box.", "4 min")}
<div class="bank">adventure · detective · funny · ghost · make up · tell</div>
<ol style="line-height:1.65">{coll}</ol>
{sub("C", "When was the last time you told a story? Was it true or from your imagination?", "1 min")}""",
    22, """<ol><li>A: elicit ideas quickly; content is more important than accuracy now. People tell true stories at work and with friends every day.</li>
<li>B: other collocations: <i>a true story, a love story, a bedtime story, a news story</i>. Ask which types the student likes.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Story titles · story collocations</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Model story: Pepper is a winner (by Lucy)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>A2 language in a story · the task · direct speech · paragraphs</td><td>3</td></tr>
<tr><td>+ Language reference</td><td>–</td><td>Writing a story: four areas, direct speech, linkers, A2 checklist</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Telling a story: pauses and stress</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>Ana's story: My dog saved my life! · Word builder: reporting verbs</td><td>6</td></tr>
<tr><td>6 Writing</td><td>12 min</td><td>Plan and tell your story, then start writing</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Lucy (student and weekend barista at City Coffee, voice Neural2-C) is taking a writing class. Her story is about Pepper, the dog Kate adopted in Unit 22. In the practice, Ana (Neural2-F) remembers a childhood story from a beach house in Ubatuba, São Paulo, with her dog Mel. Both stories are fiction inside our story; no facts to check. The lesson reviews the A2 grammar of units 03–23 (checklist on the Language reference page). Writing a story is a task in Cambridge B1 Preliminary.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Punctuation of direct speech (Portuguese uses dashes for dialogue: students forget quotation marks or put the comma outside them), <i>Firstly</i> instead of <i>At first</i>, <i>Although… but…</i>, <i>said me</i> instead of <i>told me</i>, and changing from past to present in the middle of a story.</div>
<div class="box"><h4>AUDIO</h4>Track 24.1 Pepper is a winner (slow and natural) · Track 24.2 Repeat: telling a story · Track 24.3 My dog saved my life!</div>""")

    # Page 2
    story = (f"Last Sunday, I {ch(['played', 'was playing'], 'was playing', 'A')} in a soccer game in the park with some students {ch(['which', 'who'], 'who', 'B')} go to a different college. "
             f"The score was 2–2, {ch(['and', 'but'], 'and', 'C')} Kate's dog Pepper was watching. Pepper and I {ch(['used to practice', 'use to practice'], 'used to practice', 'D')} in the park every weekend, "
             f"so she {ch(['was knowing', 'knew'], 'knew', 'E')} how to play. Suddenly, Pepper ran onto the field and picked up the ball in her mouth. "
             f"{ch(['At first', 'Firstly'], 'At first', 'F')}, I thought she was going to bring the ball to me, {ch(['and next', 'but then'], 'but then', 'G')} she ran to the goal and dropped the ball in. "
             f"\"If Pepper {ch(['weren&#39;t', 'isn&#39;t'], 'weren&#39;t', 'H')} a dog, we {ch(['had', 'would'], 'would', 'I')} count that goal!\" laughed a player on the other team. "
             f"{ch(['Although', 'But'], 'Although', 'J')} we didn't win the game, Pepper was the hero of the day.")
    qs = [("Was this a professional game? How do you know?", "No. They were students playing in a park."),
          ("How often did Lucy and Pepper use to practice?", "every weekend"),
          ("Was Lucy surprised by what Pepper did? How do you know?", "Yes: suddenly, at first I thought…"),
          ("Why was Pepper's goal so important?", "The score was 2–2, so it was the winning goal.")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:36mm')}</li>" for q, a in qs)
    b.page(f"""{sec(2, "Reading: a model story", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Lucy is taking a writing class at her college. This was her homework: <i>Write a story about a pet that does something surprising. Write about 100 words.</i></p>{img('F', 30, 21)}{img('A', 30, 21)}</div>
{audiocard(["24.1 · SLOW", "24.1 · NATURAL"])}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.75"><h4 style="font-size:10.5pt;margin:0">Pepper is a winner <span style="font-weight:400;color:#555">· by Lucy</span></h4>{story}</div>
{sub("A", "Read the story quickly. Don't choose the options yet. Answer the questions.", "4 min")}
<ol style="line-height:1.5">{ql}</ol>
{sub("B", "Now read and listen. Choose the best option in A–J.", "4 min", "24.1 · SLOW")}
<p class="small" style="margin:0">Which title from page 1 is closest to Lucy's title? {A("My dog is a winner", "min-width:34mm")}</p>""",
    20, """<ol><li>A: give 1–2 minutes only. The options are a review of A2 grammar; they come next.</li>
<li>B: play the slow version and check A–J; then play the natural version while the student follows.</li></ol>""")

    # Page 3
    pts = [("a conjunction of contrast", "J"), ("a state verb with no continuous form", "E"), ("an imagined (unreal) present situation", "H"),
           ("a conjunction of addition", "C"), ("the first part of a changing situation", "F"), ("the second part of a changing situation", "G"),
           ("past continuous to set the scene", "A"), ("past repeated actions", "D"), ("a relative pronoun for people", "B"), ("the result of an unreal situation", "I")]
    ptl = [f'<li value="{i+1}">{p} {box(a)}</li>' for i, (p, a) in enumerate(pts)]
    tasks = ["Write a story. It must begin: <i>Soccer is my favorite game.</i> Write 50 words.",
             "Articles wanted! Pets and exercise: does your pet help you get in shape? Write 100 words.",
             "Write a story about a pet that does something surprising. Write about 100 words."]
    tl = "".join(f"<li>{t} {R('✓') if i == 2 else ''}</li>" for i, t in enumerate(tasks))
    ds = ["Don't go in there, he shouted. It's too dangerous.", "\"Don't go in there,\" he shouted. \"It's too dangerous.\"", "\"Don't go in there\" he shouted, \"it's too dangerous\"."]
    dsl = "".join(f"<li>{d} {R('✓') if i == 1 else ''}</li>" for i, d in enumerate(ds))
    b.page(f"""{sec(3, "Language focus: what makes a good story?", "10 min")}
{sub("A", "Language: match the options A–J in Lucy's story with the language points.", "4 min")}
{twocol(ptl, 6)}
{sub("B", "The task: which instructions match Lucy's story? Why are the others a bad match?", "2 min")}
<ol type="a" style="line-height:1.5">{tl}</ol>
{sub("C", "The reader: direct speech makes a story more alive. Which sentence has the correct punctuation?", "2 min")}
<ol type="a" style="line-height:1.5">{dsl}</ol>
{sub("D", "Organization: Lucy's story has two paragraphs. Where does the second paragraph begin? Find an adverb in the story.", "2 min")}
<p class="small" style="margin:0">{A("Paragraph 2 begins: Suddenly, Pepper ran onto the field… · Adverb: suddenly", "min-width:100mm")}</p>
<div class="box sand"><h4>RULE</h4>A good story <b>follows the task</b>, keeps the <b>reader</b> interested (direct speech, adverbs like <i>suddenly</i>), is <b>organized</b> in paragraphs, and shows a <b>range of language</b>. Direct speech: <i>\"Don't go in there<b>,</b>\" he shouted.</i> More on the next page: <b>Language reference</b>.</div>""",
    22, """<ol><li>B: a = wrong first sentence and only 50 words; b = an article, not a story; c = the best match.</li>
<li>C: in American English, the comma and the period go inside the quotation marks. Portuguese dialogue uses a dash, so this is new for many students.</li></ol>""")

    grammar_ref.story_writing(b)

    # Page 5
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>— Don't go in there — he shouted.</td><td><b>"Don't go in there," he shouted.</b></td><td>English uses quotation marks.</td></tr>
<tr><td>"Help me", she said.</td><td><b>"Help me," she said.</b></td><td>comma inside the quotes.</td></tr>
<tr><td>Firstly, I thought she was lost.</td><td><b>At first, I thought she was lost.</b></td><td>a change: at first … but then.</td></tr>
<tr><td>He said me, "Run!"</td><td><b>He said to me, "Run!" / He told me to run.</b></td><td>say to someone / tell someone.</td></tr>
<tr><td>Although it rained, but we played.</td><td><b>Although it rained, we played.</b></td><td>one conjunction only.</td></tr>
<tr><td>Suddenly, the dog runs to the goal.</td><td><b>Suddenly, the dog ran to the goal.</b></td><td>keep the story in the past.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab: telling a story", "4 min")}
{audiocard(["24.2"])}
{sub("A", "Listen and repeat. Notice the short pause after Suddenly and At first, and the stress on the surprising words.", "2 min", "24.2")}
<ol style="line-height:1.6">{"".join(f"<li>{s}</li>" for s in S242)}</ol>
{sub("B", "Read Lucy's story aloud like a storyteller. Mark the pauses ( / ) first. Then compare with track 24.1.", "2 min")}""",
    24, """<ol><li>A: a good storyteller slows down before the surprise (<i>but then… she ran to the goal!</i>) and changes the voice for direct speech.</li>
<li>B: no recording: the student just reads aloud. Give feedback on pauses, past -ed endings and <i>would</i>.</li></ol>""")

    # Page 6
    gaps = [("h", "had"), ("a", "and"), ("u", "used"), ("w", "walking"), ("b", "but"), ("w", "where"), ("s", "so"), ("w", "was"), ("s", "shouted"), ("S", "Suddenly")]
    g = [f"<sup>{i+1}</sup><b>{l}</b>" + A(w[1:] if T else "", "min-width:15mm") for i, (l, w) in enumerate(gaps)]
    ana = (f"When I was a child, my family {g[0]} a house at the beach in Ubatuba, {g[1]} we {g[2]} to go there every summer. One morning, I was {g[3]} on the beach with my dog, Mel. "
           f"I threw a ball to Mel, {g[4]} she didn't catch it. The ball went into a hole in the rocks. It was a cave!<br>When Mel and I went into the cave {g[5]} the ball was, we saw some drawings on the walls. "
           f"They looked very old. I wanted to stay and look at them, but Mel wasn't happy in the cave, {g[6]} she pulled me out. A fisherman {g[7]} walking past. "
           f"\"Don't go in there,\" he {g[8]}. \"It's too dangerous.\" {g[9]}, some rocks fell down and closed the cave forever.")
    rv = [("\"Shh! The baby is sleeping,\"", "she whispered."), ("\"Help! There's a fire!\"", "he shouted."), ("\"What time is it?\"", "she asked."),
          ("\"It's ten past six,\"", "he answered."), ("\"That's so funny!\"", "she laughed."), ("\"You press this button to start,\"", "he explained.")]
    rvl = [f'<li value="{i+1}">{a} he / she {A(v.split(" ", 1)[1].rstrip("."), "min-width:18mm")}.</li>' for i, (a, v) in enumerate(rv)]
    b.page(f"""{sec(5, "Practice", "9 min")}
{audiocard(["24.3"])}
{sub("A", "Read Ana's story. Complete it with one word in each gap. The first letter is given. Then listen and check.", "6 min", "24.3")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div class="msg" style="flex:1;max-width:none;font-size:9pt;line-height:1.85"><b>My dog saved my life!</b> <span class="small">· by Ana</span><br>{ana}</div>{img('B', 30, 40)}</div>
<p class="small" style="margin-top:1mm">Which title from page 1 matches Ana's story? Which A2 language points from page 3 can you find?</p>
{sub("B", "Word builder: reporting verbs. Complete with the best verb.", "3 min")}
<div class="bank">answered · asked · explained · laughed · shouted · whispered</div>
{twocol(rvl, 4)}""",
    22, """<ol><li>A: 3 <i>used</i> (to go) · 6 <i>where</i> (a relative clause for a place) · 8 <i>was</i> (past continuous). Ubatuba is a beach town on the north coast of São Paulo state.</li>
<li>B: the verb shows how the person speaks. Ask the student to say each line in that way.</li></ol>""")

    # Page 7
    model = ("I was walking down the street when I saw an unusual-looking dog. It was wearing a small green hat, and it was sitting outside a bakery. "
             "At first, I thought it was waiting for its owner, but then it walked into the bakery and came out with a bag of cookies in its mouth! "
             "\"Is that your dog?\" I asked the baker. \"No,\" she laughed. \"He comes every morning, and his owner pays at the end of the month.\" "
             "Although it sounds crazy, it's true. If I had a dog like that, I'd never go shopping again!")
    steps = ["a beginning: Where were you? What was the dog like?", "a surprise: Suddenly, … / At first, … but then …", "direct speech: one or two lines with quotation marks",
             "an ending: How did it end? How did you feel?", "two paragraphs and about 100 words", "at least five language points from page 4"]
    stl = "".join(f"<li>☐ {s}</li>" for s in steps)
    b.page(f"""{sec(6, "Writing: your story", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div class="box" style="flex:1;margin:0"><h4>YOUR TASK</h4>Your English teacher has asked you to write a story. Your story must begin with this sentence:<br><b><i>I was walking down the street when I saw an unusual-looking dog.</i></b><br>Write about <b>100 words</b>.</div>{img('E', 30, 30)}</div>
{sub("A", "Plan for two minutes. Write 10–12 key words. Don't write sentences yet.", "3 min")}
<div class="wline"></div><div class="wline"></div>
{sub("B", "Tell your story to your teacher. Your teacher will ask questions and give you advice.", "4 min")}
{sub("C", "Listen to your teacher's story. What was unusual about the dog? What happened at the end?", "2 min")}
<p class="small" style="margin:0">{R(model) if T else ''}</p>
{sub("D", "Start writing. Use this checklist.", "3 min")}
<ul style="list-style:none;padding-left:2mm;line-height:1.5;margin:0">{stl}</ul>""",
    24, """<ol><li>B: ask <i>Where were you going? What did the dog look like? What happened next? How did it end?</i> Suggest one change that makes the story more interesting.</li>
<li>C: read the red story with expression. The student finishes the story at home (homework 2) and sends it to you.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 21", "I can tell a story with the past continuous and the past simple."), ("A2 Unit 22", "I can compare my life then and now with used to."),
          ("A2 Unit 23", "I can imagine a different situation with the second conditional."), ("A2 Unit 24", "I can plan and write a short story with direct speech.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    gd = [("A dog was running home with a big, delicious bone.", "1"), ("As he was going over a little bridge, he looked down into the water.", "2"),
          ("He dropped his own bone and jumped into the river to fight the other dog.", "6"), ("He felt really stupid.", "9"),
          ("He saw himself in the water, like in a mirror, but he didn't understand that he was looking at himself.", "3"),
          ("He thought he saw another dog with a bone that was bigger than his.", "4"), ("Of course, soon he was swimming to the side of the river and trying to get out.", "7"),
          ("Suddenly, he understood.", "8"), ("\"That dog has a better bone than I do,\" said the dog to himself. \"I want his bone!\"", "5")]
    gdl = "".join(f"<tr><td style='width:9mm'>{box(n) if n != '1' else '<b>1</b>'}</td><td>{s}</td></tr>" for s, n in gd)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><p style="flex:1;margin:0"><b>1. The greedy dog.</b> Put the lines in order (1–9). Then write a conditional sentence with the moral of the story.</p>{img('C', 24, 16)}</div>
<table style="margin:.5mm 0;font-size:8.6pt">{gdl}</table>
<p class="small" style="margin:0">Moral: {A("If you are too greedy, you will lose everything.", "min-width:80mm")}</p>
<p style="margin-top:1.5mm"><b>2. Finish your story</b> from page 7 (about 100 words). Leave a line free between your lines so your teacher can write corrections.</p>""",
    20, """<p>1 is a fable (Unit 21). Check the order: 1, 2, 3, 4, 5, 6, 7, 8, 9 = A dog… / As he… / He saw himself… / He thought… / "That dog…" / He dropped… / Of course… / Suddenly… / He felt…. Mark story 2 for the task, organization, the reader and language (page 4).</p>""")

    b.extra("Audio script", f"""
{sub("24.1", "Pepper is a winner (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(S241)}</p>
{sub("24.2", "Repeat: telling a story")}
<p>{" · ".join(S242)}</p>
{sub("24.3", "My dog saved my life!")}
<p style="line-height:1.45">{"<br>".join(S243)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 24 - Writing a story")
