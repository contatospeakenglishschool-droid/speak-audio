# Speak! Essentials A1 - Review 3 (Units 19-26), all English - built with the shared engine
import sys, json
sys.path.insert(0, "/home/claude/speak-audio/engine")
from speak_engine import *
setup(band="A1 · REVIEW 3", audio_json="audio_a1-review-3.json", img_dir="img")

PHOTOS = [("A", "sunny", "Unit 19"), ("B", "a beach", "Unit 20"), ("C", "cross the street", "Unit 21"), ("D", "the subway", "Unit 22"),
          ("E", "a soccer player", "Unit 23"), ("F", "a guitar", "Unit 24"), ("G", "get married", "Unit 25"), ("H", "eat pizza", "Unit 26")]

_r = json.load(open("roteiro.json"))["units"]["a1-review-3"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["R3.1 Video call"].split("\n")]
S33 = [tuple(x.split(": ", 1)) for x in _r["R3.3 Dialogues"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: cover + photo memory
    cover = cover_html(T, "LEVEL A1 · REVIEW 3", "Review 3", "Units 19–26 · present continuous · past simple · plans · directions",
                       [("YOU CAN", "check what you learned in Units 19–26 and plan what to practice"),
                        ("LANGUAGE", "I'm wearing… · We're meeting on Friday. · She was born… · I went… · Did you…?"),
                        ("PRONUNCIATION", "-ed: /d/ /t/ /ɪd/ · irregular verbs · polite questions")])
    b.page(f"""{sec(1, "Warm-up: photo memory", "5 min")}
{sub("A", "One photo from each unit. Write the word or phrase. Then say one sentence about it in the past.", "5 min")}
<div class="bank">a beach · cross the street · eat pizza · get married · a guitar · a soccer player · the subway · sunny</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Example:</b> sunny → <i>Last Sunday it was sunny, so I went to the park.</i></p>""",
    20, """<p>Photos A–H come from Units 19–26 in order. Accept any correct past sentence: <i>I took the subway yesterday. My parents got married in 1990. We ate pizza on Saturday.</i> Correct <b>was / were</b> and irregular verbs.</p>""", cover=cover)

    b.extra("Review overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Units</th><th>SB page</th></tr>
<tr><td>1 Warm-up: photo memory</td><td>5 min</td><td>19–26</td><td>1</td></tr>
<tr><td>2 Listening: Tom and Ana's video call</td><td>10 min</td><td>19–26</td><td>2</td></tr>
<tr><td>3 Grammar: the present (simple, continuous, plans)</td><td>8 min</td><td>19, 20, 22</td><td>3</td></tr>
<tr><td>4 Grammar: the past (was/were, regular, irregular, did)</td><td>10 min</td><td>23–26</td><td>4</td></tr>
<tr><td>5 Vocabulary</td><td>8 min</td><td>19–26</td><td>5</td></tr>
<tr><td>6 Pronunciation and social English</td><td>9 min</td><td>21, 24, 26</td><td>6</td></tr>
<tr><td>7 Reflect and homework</td><td>5 min</td><td>19–26</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. Audio scripts are on the last page. This is a review: don't teach everything again. Let the student work, then focus on the mistakes that come back.</div>
<div class="box sand"><h4>THE STORY SO FAR</h4>December. Tom is back in Chicago after his week in São Paulo (Units 22–23). On a video call, he and Ana talk about the weather (Unit 19), Tom's trip back and getting lost (Units 21–22), Paulo's video about Grandma Lourdes (Unit 25), Rita Lee (Unit 24), their weekends (Unit 26) and their plans for next weekend (Unit 22).</div>
<div class="box"><h4>THE TOP 5 MISTAKES TO WATCH</h4>1. <i>I'm usually taking the bus</i> → <b>I usually take</b>. 2. <i>She born in 1940</i> → <b>She was born</b>. 3. <i>I goed / buyed</i> → <b>went / bought</b>. 4. <i>Did you went?</i> → <b>Did you go?</b> 5. <i>work-ED</i> /ɪd/ → <b>worked</b> /t/.</div>
<div class="box"><h4>AUDIO</h4>Track R3.1 Video call (slow and natural) · Track R3.2 -ed endings · Track R3.3 Two dialogues</div>""")

    # Page 2: listening
    topics = [("the weather", True), ("Tom's trip back", True), ("a new job", False), ("Paulo's video", True), ("Rita Lee", True), ("last weekend", True), ("next weekend", True)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("It's cold and snowy in São Paulo.", "F: it's hot and sunny."), ("Leo is swimming in the pool.", "T"), ("Tom took a taxi to the airport.", "F: he took the train."),
          ("The flight took about ten hours.", "T"), ("Tom watched Paulo's video three times.", "T"), ("Tom went to a concert last weekend.", "F: he didn't do much. He's going to a concert next weekend."),
          ("Ana and Marcos went to a Japanese restaurant.", "T"), ("Next weekend, Ana is taking the bus to Santos.", "T")]
    tfl = "".join(f"<li>{s} <b>T / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Listening: a video call", "10 min")}
<p>It's December. Tom is back in Chicago. He's on a video call with Ana in São Paulo.</p>
{audiocard(["R3.1 · SLOW", "R3.1 · NATURAL"])}
{sub("A", "Listen. What do they talk about? Check (✓) six topics. One topic is extra.", "3 min", "R3.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "5 min", "R3.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Find one example in the conversation of each form.", "2 min")}
<table style="table-layout:fixed"><tr><td>present continuous (now)</td><td>{R("Leo is swimming / I'm wearing two sweaters")}</td></tr><tr><td>present continuous (plan)</td><td>{R("We're taking the bus / I'm meeting Kate")}</td></tr>
<tr><td>was / were</td><td>{R("the flight was fine / my battery was dead")}</td></tr><tr><td>past simple (irregular)</td><td>{R("took, got up, read, made, went")}</td></tr></table>""",
    18, """<p>A: extra topic = <span class="red">a new job</span>. B: in 6 the student must notice <i>next weekend</i> = a plan. C: let the student look at the audio script on your guide if needed.</p>""")

    # Page 3: grammar present
    pairs = [("It's very hot today, so I wearing a T-shirt.", "It's very hot today, so I'm wearing a T-shirt.", "B"),
             ("Ana is making a cake for Leo's birthday right now.", "Ana is makeing a cake for Leo's birthday right now.", "A"),
             ("She's not listening to me.", "She isn't listening to me.", "both"),
             ("My mother is really liking ice cream.", "My mother really likes ice cream.", "B"),
             ("Where is Leo? Is he swimming in the pool?", "Where is Leo? He is swimming in the pool?", "A"),
             ("Is the train leaving now? Yes, it is.", "Is the train leaving now? Yes, it leaves.", "A"),
             ("What are you doing? I'm writing an email.", "What do you do? I'm writing an email.", "A"),
             ("I am always taking the bus to work.", "I always take the bus to work.", "B")]
    pl = "".join(f"<li>A) {a}<br>B) {bb} {R('→ ' + c)}</li>" for a, bb, c in pairs)
    plan = [(["I meet", "I'm meeting"], "I'm meeting", "", "Kate on Saturday. We have tickets for a concert."), (["leaves", "is leaving"], "leaves", "The bus to Santos", "every hour."),
            (["are you doing", "do you do"], "are you doing", "What", "tonight?"), (["I need", "I'm needing"], "I need", "", "a new phone.")]
    pll = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in plan)
    b.page(f"""{sec(3, "Grammar: the present", "8 min")}
{sub("A", "Units 19–20. Which sentence is correct, A or B? Sometimes both are correct.", "5 min")}
<ol style="line-height:1.45">{pl}</ol>
{sub("B", "Units 20 and 22. Choose the correct form: habit, now, plan or state verb?", "3 min")}
<ol>{pll}</ol>""",
    27, """<ol><li>A: ask <i>why?</i> for each answer: 1 <i>am</i> is missing; 2 <i>making</i> (drop the e); 3 both contractions are fine; 4 state verb; 5 question = <i>Is he…?</i>; 6 short answer with <i>be</i>; 7 now = continuous; 8 habit = simple.</li>
<li>B: 1 plan with a day = continuous; 2 a timetable = simple; 4 <i>need</i> is a state verb.</li></ol>""")

    # Page 4: grammar past
    wb = [("Grandma Lourdes", "was", "born on a farm in Minas Gerais."), ("Her parents", "weren't", "rich."), ("", "Were", "the people at the exhibition friendly?"),
          ("When", "was", "Tom Jobim born?"), ("Carmen Miranda", "wasn't", "born in Brazil."), ("Rita Lee's hair", "was", "red.")]
    wbl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")} {c}</li>' for i, (a, x, c) in enumerate(wb)]
    rg = [("Where", "did you live", "(live) when you were a child?"), ("We", "moved", "(move) to a new house in 2010."), ("I", "didn't want", "(not want) to change school."),
          ("My mother", "started", "(start) a new job."), ("", "Did your parents work", "(your parents / work) on weekends?"), ("Yes, they", "did", ". My father", )]
    irr = [("eat", "ate", "We", "pizza on Saturday night."), ("take", "took", "Mia", "an Uber home."), ("see", "saw", "They", "a scary movie."),
           ("buy", "bought", "I", "new shoes."), ("go", "went", "Tom", "to Paulista Avenue."), ("feel", "felt", "Ana", "tired on Sunday."),
           ("have", "had", "We", "a great time."), ("read", "read", "I", "a book in bed.")]
    il = [f'<li value="{i+1}">{s} {A(p, "min-width:16mm")} {c} ({v})</li>' for i, (v, p, s, c) in enumerate(irr)]
    q = [("Did you went to the beach?", "Did you go to the beach?"), ("I didn't saw the movie.", "I didn't see the movie."),
         ("Where you were born?", "Where were you born?"), ("She born in 1960.", "She was born in 1960.")]
    ql = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in q)
    b.page(f"""{sec(4, "Grammar: the past", "10 min")}
{sub("A", "Unit 23. Complete with was, wasn't, were or weren't.", "2 min")}
{twocol(wbl, 4)}
{sub("B", "Unit 26. Complete with the past simple.", "3 min")}
{twocol(il, 5)}
{sub("C", "Units 24–26. Correct the mistakes.", "3 min")}
<ol>{ql}</ol>
{sub("D", "Unit 25. Ask your teacher three questions about their childhood with Did you…? and Where / When did you…?", "2 min")}
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: Carmen Miranda was born in Portugal (Unit 23), so 5 is negative.</li>
<li>D: answer in full and ask the student back: <i>Did you live in a big city? When did you start school?</i></li></ol>""")

    # Page 5: vocabulary
    wt = [("It's hot.", "sunny", "The sun is shining."), ("It's cold.", "snowy", "It's snowing."), ("It's rainy.", "wet", "It's raining."), ("It's stormy.", "windy", "The wind is blowing.")]
    wtr = "".join(f"<tr><td>{a}</td><td>It's {A(x, 'min-width:18mm')}.</td><td>{R(c) if T else '<span class=\"wline\" style=\"display:inline-block;min-width:40mm\"></span>'}</td></tr>" for a, x, c in wt)
    lv = [("Do you usually m", "meet", "friends on Friday nights?"), ("I always have a great t", "time", "on the weekend."), ("If I'm tired, I stay home and w", "watch", "a movie."),
          ("If you t", "take", "a taxi from the airport, it's expensive."), ("My sister usually g", "gets", "up late on Sundays."), ("On my birthday, we go to a nice r", "restaurant", ".")]
    lvl = "".join(f'<li>{a}{A(x[1:], "min-width:16mm")} {c}</li>' for a, x, c in lv)
    df = [("You buy medicine here.", "a pharmacy"), ("It's a train under the city.", "the subway"), ("A car that you call with an app.", "an Uber / a taxi"),
          ("You send letters here.", "a post office"), ("Red, yellow and green lights on the street.", "traffic lights"), ("You ride it with two wheels and no engine.", "a bike")]
    dfl = [f'<li value="{i+1}">{a} {A(x, "min-width:24mm")}</li>' for i, (a, x) in enumerate(df)]
    mu = [("She released her first", "album", "in 1970."), ("Her red hair attracted a lot of", "attention", "."), ("He started his", "career", "in a band."), ("Tim Maia was famous", "for", "soul music.")]
    mul = "".join(f'<li>{a} {A(x, "min-width:16mm")} {c}</li>' for a, x, c in mu)
    b.page(f"""{sec(5, "Vocabulary", "8 min")}
{sub("A", "Unit 19. Weather. Complete the table.", "2 min")}
<table style="table-layout:fixed;margin-top:0"><tr><th>adjective 1</th><th>adjective 2</th><th>present continuous</th></tr>{wtr}</table>
<p class="small">Say these years: 1998 · 2025 · 1906 {R("nineteen ninety-eight · twenty twenty-five · nineteen oh six")}</p>
{sub("B", "Units 20 and 26. Free time. Complete the words.", "2 min")}
<ol>{lvl}</ol>
{sub("C", "Units 21–22. Places and transportation. What is it?", "2 min")}
{twocol(dfl, 4)}
{sub("D", "Units 23–24. Music careers. Complete.", "2 min")}
<div class="bank">album · attention · career · for</div>
<ol>{mul}</ol>""",
    18, """<p>A: accept <i>freezing / icy</i> for cold. Years: before 2000 in two pairs; 2025 = <i>twenty twenty-five</i>. C: <i>traffic lights</i> is always plural.</p>""")

    # Page 6: pronunciation + social English
    ed = ["attracted", "died", "ended", "introduced", "listened", "played", "started", "traveled", "watched", "worked"]
    eda = {"/d/": "died, listened, played, traveled", "/t/": "introduced, watched, worked", "/ɪd/": "attracted, ended, started"}
    edr = "".join(f"<td style='height:16mm;vertical-align:top'>{R(eda[k])}</td>" for k in eda)
    d1 = [("A", "Excuse me. Can you say me the way to the bank?", "Can you tell me the way"), ("B", "Yes. Go straight ahead past the traffic lights, and then it's in the left.", "it's on the left"),
          ("A", "Thanks. And is there a supermarket close here?", "near here"), ("B", "Yes, there's one on the corner.", ""), ("A", "Great! It far?", "Is it far?")]
    d2 = [("A", "What you do over the weekend?", "What did you do"), ("B", "I met some friends, and we go shopping.", "we went shopping"),
          ("A", "What did you buy?", ""), ("B", "I bought some new shoes. What with you?", "What about you?"), ("A", "On Saturday I fell really tired, so I stayed home.", "I felt"),
          ("A", "On Sunday I drank three coffees and drived to the beach!", "drove")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Pronunciation and social English", "9 min")}
{audiocard(["R3.2", "R3.3"])}
{sub("A", "Unit 24. Listen. After each verb, write it in the correct column. Then say the verbs.", "3 min", "R3.2")}
<div class="bank" style="background:#fff">{" · ".join(ed)}</div>
<table style="table-layout:fixed;margin-top:0"><tr><th>/d/</th><th>/t/</th><th>/ɪd/</th></tr><tr>{edr}</tr></table>
{sub("B", "Units 21 and 26. Each dialogue has mistakes. Correct them. Then listen and check.", "4 min", "R3.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogue 1: directions</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogue 2: the weekend</b>{dl(d2)}</div></div>
{sub("C", "Role-play the dialogues with your teacher. Then change the details and make them true for you.", "2 min")}""",
    26, """<ol><li>A: the audio says the verbs in alphabetical order with a pause after each one: the student listens and writes the verb in the column. Only <i>t</i> and <i>d</i> endings get the extra syllable /ɪd/.</li>
<li>B: 4 mistakes in dialogue 1 and 5 in dialogue 2. The audio has the correct versions. In C, the student asks you for directions to a real place near their home.</li></ol>""")

    # Page 7: reflect
    cd = [("19", "I can talk about the weather and what is happening now."), ("20", "I can ask wh- questions: What are you doing?"),
          ("21", "I can ask for and give simple directions."), ("22", "I can talk about transportation and my plans."),
          ("23", "I can use was / were and say when I was born."), ("24", "I can use regular past verbs and say -ed correctly."),
          ("25", "I can ask and answer with did / didn't."), ("26", "I can use common irregular past verbs.")]
    cdr = "".join(f"<tr><td><b>Unit {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Reflect and homework", "5 min")}
{sub("A", "How are you doing? Check one box for each line.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{cdr}</table>
{sub("B", "My goals. What do you want to practice more? Write two things.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Homework", "1 min")}
<p><b>A message to Tom.</b> Write a message to Tom (70–90 words). Tell him about:</p>
<ol><li>the weather today and what you are doing now;</li><li>what you did last weekend (use 4 past verbs);</li><li>your plans for next weekend.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Look at the "Not yet" lines and plan two short review activities for the next classes. The homework uses all the grammar of Units 19–26: correct it carefully and keep it as a writing sample.</p>""")

    b.extra("Audio scripts", f"""
{sub("R3.1", "Video call (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R3.2", "-ed endings (alphabetical order, with pauses)")}
<p>{" · ".join(x.split(": ",1)[1].rstrip(".") for x in _r["R3.2 Write ed"].split("\n"))} (3-second pause after each verb)</p>
{sub("R3.3", "Two dialogues (correct versions)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S33)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 27 - Review 3")
