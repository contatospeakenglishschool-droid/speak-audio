# Speak! Essentials A1 - Unit 25 "This is your life" (all English) - built with the shared engine
import sys
sys.path.insert(0, "/home/claude/speak-audio/engine")
from speak_engine import *
setup(band="A1 · UNIT 25", audio_json="audio_a1-unit-25.json", img_dir="img")

PHOTOS = [("A", "move to a new house", "move"), ("B", "study", "study"), ("C", "graduate", "graduate"), ("D", "get married", "get married"),
          ("E", "start a job", "start a job"), ("F", "travel", "travel"), ("G", "learn to drive", "learn to drive"), ("H", "retire", "retire")]

SCRIPT = [("Narrator", "Paulo is making a video for his grandmother's birthday. He's asking her questions about her life."),
          ("Paulo", "Hi Grandma! Today is your birthday, and you're ninety-five years old!"),
          ("Lourdes", "Ninety-five? No! I'm ninety-six!"),
          ("Paulo", "Oh, sorry! Happy birthday! You were born on a farm in Minas Gerais. When did you move to São Paulo, and why?"),
          ("Lourdes", "We moved when I was ten years old. My parents wanted a good school for me and my brothers."),
          ("Paulo", "Where did you study?"),
          ("Lourdes", "I studied at a school for girls near Paulista Avenue. I was a good student, but I didn't finish school."),
          ("Paulo", "Why didn't you finish school? Did you need to work?"),
          ("Lourdes", "Yes, I did. My family needed money, so I started work when I was fifteen. I worked in a fabric shop in Brás."),
          ("Paulo", "Did you stay there for a long time?"),
          ("Lourdes", "No, I didn't. I married your grandfather Antônio when I was nineteen. At that time, most women didn't work after they married."),
          ("Paulo", "And then you and Grandpa moved to Rio, right?"),
          ("Lourdes", "No, we didn't move to Rio de Janeiro. We moved to Rio Claro, a small city near São Paulo!"),
          ("Paulo", "Oh, my mistake! How long did you live in Rio Claro?"),
          ("Lourdes", "We lived there for forty years, and we loved it! Then we moved back to São Paulo to live near our grandchildren."),
          ("Paulo", "What a beautiful story! Let's stop for a short break now. There's more after the cake!")]
S252 = ["Did you move?", "Did you study English at school?", "Where did you live?", "When did you start work?", "No, I didn't.", "I didn't finish school."]
S253 = ["1822 eighteen twenty-two", "1906 nineteen oh six", "1958 nineteen fifty-eight", "1960 nineteen sixty", "2007 two thousand seven", "2016 twenty sixteen"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 25", "This Is Your Life", "Life events · <b>past simple: questions and negatives</b> · years",
                       [("YOU CAN", "ask and answer questions about someone's life"),
                        ("LANGUAGE", "When did you move? · Did you finish school? No, I didn't. · I didn't work."),
                        ("PRONUNCIATION", "Did you…? /ˈdɪdʒə/ · didn't · nineteen fifty-eight")])
    words = ["get married", "graduate", "learn to drive", "move to a new house", "retire", "start a job", "study", "travel"]
    ev = [("Brazil's independence", "1822"), ("Santos-Dumont's flight in Paris", "1906"), ("Brazil's first World Cup title", "1958"),
          ("Brasília, the new capital", "1960"), ("The first iPhone", "2007"), ("The Olympic Games in Rio", "2016")]
    el = [f'<li value="{i+1}">{e} {A(y, "min-width:14mm")}</li>' for i, (e, y) in enumerate(ev)]
    b.page(f"""{sec(1, "Warm-up: life events and years", "8 min")}
{sub("A", "Look, listen and repeat. Then write the life event under the photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Match the events with the years. Say the years. Which events were in the 20th century?", "5 min")}
<div class="bank" style="background:#fff">1822 · 1906 · 1958 · 1960 · 2007 · 2016</div>
{twocol(el, 4)}""",
    24, """<ol><li>B: 1822 = <i>eighteen twenty-two</i>, 1906 = <i>nineteen oh six</i>, 2007 = <i>two thousand seven</i>, 2016 = <i>twenty sixteen</i>. The 20th century = the 1900s: <span class="red">1906, 1958, 1960</span>.</li>
<li>Ask: <i>What year were you born? Say the year of your 50th birthday.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 life events with photos · saying years and centuries</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Paulo interviews his grandmother on her birthday</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Past simple: <i>did / didn't</i> + base verb · short answers · wh- questions</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Did you…? /ˈdɪdʒə/ · intonation · years</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>More of Grandma Lourdes' life: questions and negatives</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Truth or lie? Questions about your life · decades</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>It's Grandma Lourdes' birthday. She is Ana and Paulo's grandmother (Rosa's mother). Paulo, the photographer, makes a video for the family and asks her about her life: a farm in Minas Gerais, school in São Paulo, a job in a fabric shop in Brás, her husband Antônio and forty years in Rio Claro. Paulo gets her age wrong (she's 96, not 95) and thinks Rio Claro is Rio de Janeiro!</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>After <i>did / didn't</i>, the verb goes back to the base form: <i>I didn't finished</i> ✗ → <b>I didn't finish</b>. <i>Did you moved?</i> ✗ → <b>Did you move?</b> Questions need <i>did</i>: <i>When you started?</i> ✗ → <b>When did you start?</b> Short answer: <i>Yes, I needed</i> ✗ → <b>Yes, I did</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 25.1 Grandma's birthday video (slow and natural) · Track 25.2 Questions and negatives · Track 25.3 Years</div>""")

    # Page 2
    evs = [("Lived on a farm in Minas Gerais", "1"), ("Moved to São Paulo", "2"), ("Studied at a school for girls", "3"), ("Worked in a fabric shop", "4"),
           ("Married Antônio", "5"), ("Moved to Rio Claro", "6"), ("Studied at a university", "✗"), ("Moved back to São Paulo", "7")]
    evl = [f'<li value="{chr(97+i)}" style="list-style:none">{chr(97+i)}. {e} {A(n, "min-width:8mm")}</li>' for i, (e, n) in enumerate(evs)]
    evh = "".join(f'<div style="margin-bottom:1.2mm">{chr(97+i)}. {e} {A(n, "min-width:8mm")}</div>' for i, (e, n) in enumerate(evs))
    tf = [("Lourdes is 95 years old.", "F: she's 96."), ("Her parents wanted a good school for her.", "T"), ("She finished school.", "F: she didn't finish school."),
          ("She worked in the fabric shop for a long time.", "F: she didn't stay there for a long time."),
          ("At that time, most women didn't work after they married.", "T"), ("Lourdes and Antônio moved to Rio de Janeiro.", "F: they moved to Rio Claro."),
          ("They lived in Rio Claro for forty years.", "T")]
    tfl = "".join(f'<li>{s} <b>T / F</b> {R(a)}</li>' for s, a in tf)
    b.page(f"""{sec(2, "Listening: Grandma's birthday video", "10 min")}
<p>Today is Grandma Lourdes' birthday. She is Ana and Paulo's grandmother. Paulo is making a video about her life for the family.</p>
{audiocard(["25.1 · SLOW", "25.1 · NATURAL"])}
{sub("A", "Listen. Put Lourdes' life events in order (1–7). One event is extra.", "4 min", "25.1 · SLOW")}
<div class="two"><div>{evh[:evh.index('<div style="margin-bottom:1.2mm">e.')]}</div><div>{evh[evh.index('<div style="margin-bottom:1.2mm">e.'):]}</div></div>
{sub("B", "Listen again. True (T) or false (F)? Correct the false sentences.", "5 min", "25.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Is there an older person in your family with an interesting life story?", "1 min")}""",
    22, """<ol><li>A: <b>slow</b> version. The extra event is <span class="red">g (university)</span>. <b>fabric</b> = <i>tecido</i>. Brás is a neighborhood in São Paulo famous for fabric and clothes shops.</li>
<li>B: the student corrects with <b>didn't</b>: <i>She didn't finish school.</i> This prepares page 3.</li></ol>""")

    # Page 3
    rules = [("To make past questions, we use", "did", "do / does"), ("To make past negatives, we use", "didn't", "don't / doesn't"),
             ("After <i>did</i> and <i>didn't</i>, the verb is in the", "base form (move)", "past form (moved)"),
             ("<i>Did</i> is", "the same for all people", "different with he / she")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b>.</li>"
    b.page(f"""{sec(3, "Language focus: did and didn't", "10 min")}
{sub("A", "Read the sentences from the video.", "2 min")}
<div class="bank" style="background:#fff;font-weight:600">When <u>did</u> you <u>move</u> to São Paulo? · I <u>didn't finish</u> school. · Why <u>didn't</u> you <u>finish</u> school? · <u>Did</u> you <u>need</u> to work? Yes, I <u>did</u>.</div>
{sub("B", "Choose the correct option.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
{sub("C", "Study the table.", "4 min")}
<table style="table-layout:fixed"><tr><th style="width:30mm"></th><th>I / you / he / she / it / we / they</th></tr>
<tr><td><b>Positive</b></td><td>She <b>lived</b> in Rio Claro.</td></tr>
<tr><td><b>Negative</b></td><td>She <b>didn't live</b> in Rio de Janeiro. (didn't = did not)</td></tr>
<tr><td><b>Yes/no question</b></td><td><b>Did</b> she <b>live</b> in Rio Claro?</td></tr>
<tr><td><b>Short answers</b></td><td>Yes, she <b>did</b>. · No, she <b>didn't</b>.</td></tr>
<tr><td><b>Wh- questions</b></td><td>Where <b>did</b> she <b>live</b>? · When <b>did</b> they <b>move</b>? · How long <b>did</b> you <b>work</b> there? · Why <b>didn't</b> you <b>stay</b>?</td></tr></table>
<div class="box"><h4>PRESENT AND PAST</h4>Present: <b>do / does</b>, <b>don't / doesn't</b> (two forms) → Past: <b>did</b>, <b>didn't</b> (one form for everybody!).<br>
Do you work? → <b>Did</b> you work? · She doesn't work. → She <b>didn't</b> work.</div>""",
    27, """<ol><li>B: compare with Unit 6 (<i>do / does</i>). The good news: the past is easier, <b>did</b> for all people.</li>
<li>C: drill with the student's life: <i>Did you live in another city? Where did you study?</i> Insist on short answers: <i>Yes, I did.</i></li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I didn't finished school.</td><td><b>I didn't finish school.</b></td><td>After <i>didn't</i>: base verb.</td></tr>
<tr><td>Did you moved to Rio?</td><td><b>Did you move to Rio?</b></td><td>After <i>did</i>: base verb.</td></tr>
<tr><td>When you started your job?</td><td><b>When did you start your job?</b></td><td>Past questions need <i>did</i>.</td></tr>
<tr><td>Did you need money? Yes, I needed.</td><td><b>Yes, I did.</b></td><td>Short answer with <i>did</i>.</td></tr>
<tr><td>She don't work after she married.</td><td><b>She didn't work after she married.</b></td><td>Past: <i>didn't</i>.</td></tr>
<tr><td>I was born in nineteen and fifty.</td><td><b>I was born in nineteen fifty.</b></td><td>Years: no <i>and</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["25.2", "25.3"])}
{sub("A", "Questions and negatives. Listen and repeat. Did you sounds like /ˈdɪdʒə/. Yes/no questions go up ↗; wh- questions go down ↘.", "3 min", "25.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S252)}</div>
{sub("B", "Years. Listen and repeat.", "2 min", "25.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(f"<b>{x.split(' ', 1)[0]}</b> {x.split(' ', 1)[1]}" for x in S253)} &nbsp;·&nbsp; the 20th century = the 1900s &nbsp;·&nbsp; the 21st century = the 2000s</div>""",
    36, """<ol><li>Mistakes: <i>didn't finished</i> and <i>Did you moved</i> are the most common. Correct them every time: the past is in <b>did</b>, so the verb doesn't change.</li>
<li>4A: <i>Did you</i> links: /ˈdɪdʒə/. <i>didn't</i> /ˈdɪdənt/: the final <i>t</i> is very soft.</li>
<li>4B: years before 2000 = two pairs (19 / 58). 2000–2009 = <i>two thousand…</i>; from 2010 we usually say <i>twenty ten, twenty sixteen</i>.</li></ol>""")

    # Page 5
    items = [("q", "What", "did she learn", "to make? → She learned to make dresses."),
             ("n", "Lourdes opened a big store downtown.", "She didn't open a big store downtown. She opened a small dress shop in her house.", ""),
             ("q", "How long", "did she work", "in the shop? → She worked there for twenty-five years."),
             ("n", "Antônio helped her every day.", "He didn't help her every day. He helped her on Saturdays.", ""),
             ("q", "", "Did they travel", "all over Brazil by plane? → No, they didn't. They traveled by bus."),
             ("n", "They visited ten states.", "They didn't visit ten states. They visited twenty states.", "")]
    il = ""
    for i, (k, a, ans, c) in enumerate(items):
        if k == "q":
            il += f'<li>{a} {A(ans, "min-width:30mm")} {c if T else c.split(" → ")[0]}</li>'
        else:
            il += f'<li>{a}<div class="wline">{R(ans)}</div></li>'
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "After the cake, Lourdes tells Paulo more. Read her story.", "2 min")}
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.6">"In Rio Claro, I wanted to do something new, so I started a sewing course. I learned to make dresses, and I opened a small dress shop in our house. I worked there for twenty-five years. Antônio helped me in the shop on Saturdays. When we stopped working, we traveled all over Brazil by bus. We visited twenty states!"</div>
{sub("B", "Complete the questions, or correct the wrong sentences with didn't. Look at the examples.", "6 min")}
<p class="small"><b>Examples:</b> When <u>did Lourdes start</u> a course? (In Rio Claro.) · <i>She started a cooking course.</i> → She <u>didn't start</u> a cooking course. She started a sewing course.</p>
<ol style="line-height:1.8">{il}</ol>""",
    24, """<p>Questions 1, 3 and 5: ask the student to answer too, in full sentences. In 5, the short answer is <span class="red">No, they didn't</span>. Then: <i>Which question is a yes/no question?</i> (<span class="red">5</span>). Extra: <i>What did your grandparents do?</i></p>""")

    # Page 6
    qs = [("live / Where / when you were a child? / did you", "Where did you live when you were a child?"),
          ("move / Did you / to a new house / last year?", "Did you move to a new house last year?"),
          ("learn / When / to ride a bike? / did you", "When did you learn to ride a bike?"),
          ("study English / Did you / at school?", "Did you study English at school?"),
          ("want / What job / did you / when you were a child?", "What job did you want when you were a child?"),
          ("start / When / your first job? / did you", "When did you start your first job?"),
          ("decide / Why / to study English? / did you", "Why did you decide to study English?"),
          ("travel / Did you / a lot / last year?", "Did you travel a lot last year?")]
    ql = [f'<li value="{i+1}">{s}<div class="wline" style="min-height:5.5mm">{R(a)}</div></li>' for i, (s, a) in enumerate(qs)]
    b.page(f"""{sec(6, "Speaking: truth or lie?", "12 min")}
{sub("A", "Put the words in order to make questions.", "4 min")}
{twocol(ql, 5)}
{sub("B", "Truth or lie? Answer your teacher's questions. You can tell the truth or tell a lie! Your teacher guesses. Then change roles.", "6 min")}
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.6"><b>A:</b> Did you travel a lot last year?<br><b>B:</b> Yes, I did. I traveled to Japan.<br><b>A:</b> I think that's a lie!<br><b>B:</b> You're right. I didn't travel to Japan. I traveled to Bahia.</div>
{sub("C", "Decades. Answer the questions.", "2 min")}
<div class="bank" style="background:#fff">the 1980s = the eighties · the 1990s = the nineties · the 2000s · the 2010s = the twenty-tens</div>
<ol><li>What music did you listen to in the 2000s?</li><li>Where did you live in the 2010s?</li></ol>""",
    22, """<ol><li>B: answer the student's questions too: tell one or two lies so the student must guess. Correct <i>Yes, I did</i> and the base verb after <i>did</i>.</li>
<li>C: past answers with regular verbs or <i>was / were</i>: <i>I listened to…, I lived in…</i></li></ol>""")

    # Page 7
    pc = [("Unit 22", "I can talk about transportation and my plans."), ("Unit 23", "I can use was / were and say when I was born."),
          ("Unit 24", "I can say -ed correctly: played, worked, started."), ("Unit 25", "I can make past questions and negatives with did / didn't."),
          ("Unit 25", "I can say years: nineteen fifty-eight, twenty sixteen.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Did you finish school? No, I don't.", "No, I didn't."), ("Lourdes did work in a fabric shop.", "Lourdes worked in a fabric shop."),
          ("She didn't married at twenty.", "She didn't marry at twenty."), ("Paulo did ask a lot of questions?", "Did Paulo ask a lot of questions?"),
          ("Did they need money? Yes, they needed.", "Yes, they did."), ("How long you did live in Rio Claro?", "How long did you live in Rio Claro?"),
          ("When you started your first job?", "When did you start your first job?"), ("He didn't wanted a big party.", "He didn't want a big party.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes.</b> There is one mistake in each sentence.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Truth or lie?</b> Write 5 sentences about your past: 3 are true and 2 are lies. Use regular verbs and <i>didn't</i>. Next class, your teacher guesses!</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the 5 sentences; you ask questions with <i>did</i> to find the lies: <i>When did you…? Why did you…?</i></p>""")

    b.extra("Audio scripts", f"""
{sub("25.1", "Grandma's birthday video (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("25.2", "Questions and negatives")}
<p>{" ".join(S252)}</p>
{sub("25.3", "Years")}
<p>{" · ".join(S253)} · the twentieth century · the twenty-first century</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 25 - This is your life")
