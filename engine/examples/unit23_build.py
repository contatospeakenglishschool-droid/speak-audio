# Speak! Essentials A1 - Unit 23 "20th century lives" (all English) - built with the shared engine
import sys
sys.path.insert(0, "/home/claude/speak-audio/engine")
from speak_engine import *
setup(band="A1 · UNIT 23", audio_json="audio_a1-unit-23.json", img_dir="img")

PHOTOS = [("A", "a singer", "singer"), ("B", "a painter", "painter"), ("C", "a scientist", "scientist"), ("D", "a writer", "writer"),
          ("E", "a soccer player", "soccer player"), ("F", "a pilot", "pilot"), ("G", "an architect", "architect"), ("H", "a race car driver", "race car driver")]

SCRIPT = [("Narrator", "It's Saturday afternoon. Tom and Ana are at an exhibition about famous Brazilians."),
          ("Tom", "This is a great exhibition! Who's this man with the soccer ball?"),
          ("Ana", "That's Pelé! He was a famous soccer player, the best in the world. He was born in 1940 in Minas Gerais. His family was very poor, but his father was a soccer player too."),
          ("Tom", "Wow! Was he in the World Cup?"),
          ("Ana", "Yes, he was! He was a champion three times: in 1958, 1962 and 1970."),
          ("Tom", "And who's this woman with the fruit on her hat?"),
          ("Ana", "That's Carmen Miranda. She was a singer and an actress, and she was very famous in Hollywood."),
          ("Tom", "Was she from Rio?"),
          ("Ana", "No, she wasn't! She was born in Portugal in 1909, but her home was Rio."),
          ("Tom", "Interesting! And this painting is beautiful. Who was the painter?"),
          ("Ana", "Tarsila do Amaral. She was born in 1886 in São Paulo. Her parents were rich coffee farmers. She was famous for her colorful paintings of Brazil."),
          ("Tom", "Was she famous in her time?"),
          ("Ana", "Yes, she was. She was in Paris in the 1920s too. And this is my favorite room! He was a musician from Rio, and he was famous for bossa nova. His name was Tom Jobim."),
          ("Tom", "Tom? Like me! Were you a fan of bossa nova when you were young?"),
          ("Ana", "Yes, I was! My parents were big fans too. The Girl from Ipanema is still my favorite song.")]
S232 = ["He was a famous soccer player.", "She was born in Portugal.", "His family was very poor.", "Her parents were rich.", "Where was she born?", "When were you born?"]
S233 = ["Was he in the World Cup? Yes, he was.", "Was she from Rio? No, she wasn't.", "Were they rich? Yes, they were.", "Were they famous? No, they weren't.", "I was born in 1990."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LEVEL A1 · UNIT 23", "20th Century Lives", "Jobs and life stories · <b>was / were</b> (past of <i>be</i>)",
                       [("YOU CAN", "talk about the life of a famous person and about your past"),
                        ("LANGUAGE", "He was born in 1940. · Her parents were rich. · Was she from Rio? No, she wasn't."),
                        ("PRONUNCIATION", "weak was /wəz/ · strong wasn't · Yes, he was.")])
    words = ["an architect", "a painter", "a pilot", "a race car driver", "a scientist", "a singer", "a soccer player", "a writer"]
    mt = [("to be born in", "1960", "c"), ("to be famous for", "his music", "e"), ("to be from", "a singer", "a"), ("to be", "Portuguese", "g"),
          ("to be Brazilian or", "Rio", "b"), ("to be married or", "poor", "h"), ("to be beautiful or", "handsome", "f"), ("to be rich or", "single", "d")]
    # left beginnings 1-8, right endings a-h (shuffled). key: 1c 2e 3b 4a 5g 6d 7f 8h
    ends = ["a singer", "Rio", "1960", "single", "his music", "handsome", "Portuguese", "poor"]
    key = {1: "c", 2: "e", 3: "b", 4: "a", 5: "g", 6: "d", 7: "f", 8: "h"}
    begins = ["to be born in", "to be famous for", "to be from", "to be", "to be Brazilian or", "to be married or", "to be beautiful or", "to be rich or"]
    bl = [f'<li value="{i+1}">{x} {A(key[i+1], "min-width:8mm")}</li>' for i, x in enumerate(begins)]
    eb = " &nbsp;·&nbsp; ".join(f"{chr(97+i)}. {e}" for i, e in enumerate(ends))
    b.page(f"""{sec(1, "Warm-up: famous jobs", "8 min")}
{sub("A", "Look, listen and repeat. Then write the job under the photo.", "3 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Life stories. Match 1–8 with a–h. Which words are opposites?", "5 min")}
<div class="bank" style="background:#fff">{eb}</div>
{twocol(bl, 5)}""",
    18, """<ol><li>A: ask: <i>Who is a famous Brazilian soccer player? A famous singer?</i></li>
<li>B: <span class="red">married ≠ single, rich ≠ poor</span>. <b>beautiful</b>: usually women; <b>handsome</b>: men.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>8 jobs with photos · phrases about life stories</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Tom and Ana at an exhibition about famous Brazilians</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>was / were: positive, negative, questions, short answers · be born</td><td>3</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>weak <i>was / were</i> · strong short answers</td><td>4</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Questions and answers about Elis Regina and Oscar Niemeyer · was / were</td><td>5</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Information gap: Ayrton Senna × Santos-Dumont · your past</td><td>6</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>7</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>.
<span class="red">Answers in red</span> are not in the Student Book. The <span class="time">5 min</span> chips show the time for each activity. Audio scripts are on the last page.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Tom is in São Paulo (Unit 22). On Saturday afternoon he visits an exhibition about famous Brazilians with Ana: Pelé, Carmen Miranda, Tarsila do Amaral and Tom Jobim. Tom is surprised that Carmen Miranda was born in Portugal, and he loves that the bossa nova star has his name.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4><i>She born in 1909</i> ✗ → <b>She was born in 1909</b> (<i>nasceu</i> = two words in English). <i>Her parents was rich</i> ✗ → <b>were</b>. <i>Where Pelé was born?</i> ✗ → <b>Where was Pelé born?</b> <i>famous of</i> ✗ → <b>famous for</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 23.1 At the exhibition (slow and natural) · Track 23.2 Weak was / were · Track 23.3 Short answers</div>""")

    # Page 2
    people = [("Pelé", "a soccer player"), ("Carmen Miranda", "a singer and an actress"), ("Tarsila do Amaral", "a painter"), ("Tom Jobim", "a musician")]
    pr = "".join(f'<td style="width:25%"><b>{n}</b><br>{A(j, "min-width:30mm;font-size:8pt")}</td>' for n, j in people)
    gaps = [("Pelé was born in", "1940", "in Minas Gerais. His family was very"), ("", "poor", ". He was a World Cup champion three times."),
            ("Carmen Miranda was born in", "Portugal", ", but her home was Rio. She was famous in"), ("", "Hollywood", "."),
            ("Tarsila do Amaral's parents were", "rich", "coffee farmers. She was famous for her colorful"), ("", "paintings", "of Brazil."),
            ("Tom Jobim was from", "Rio", ". He was famous for"), ("", "bossa nova", ".")]
    def card(t, a1, m1, a2, e2):
        return f'<div class="msg" style="max-width:none;margin-bottom:2mm;padding:2mm 4mm;line-height:1.9">{t} {A(a1)} {m1} {A(a2)}{e2}</div>'
    cards = "".join(card(gaps[i][0], gaps[i][1], gaps[i][2], gaps[i+1][1], gaps[i+1][2]) for i in range(0, 8, 2))
    b.page(f"""{sec(2, "Listening: famous Brazilians", "10 min")}
<p>It's Saturday afternoon in São Paulo. Tom and Ana are at an exhibition about famous Brazilians from the 20th century.</p>
{audiocard(["23.1 · SLOW", "23.1 · NATURAL"])}
{sub("A", "Listen. What was each person's job?", "3 min", "23.1 · SLOW")}
<table class="ck"><tr>{pr}</tr></table>
{sub("B", "Listen again and complete the life stories.", "5 min", "23.1 · NATURAL")}
<div class="bank">1940 · bossa nova · Hollywood · paintings · poor · Portugal · rich · Rio</div>
{cards}
{sub("C", "Why is Tom happy in the last room? Were Ana's parents fans of bossa nova?", "2 min")}
<div class="wline">{R("The musician's name was Tom, like him! Yes, they were. They were big fans.")}</div>""",
    22, """<ol><li>A: <b>slow</b> version. <b>actress</b> = a woman actor. Carmen Miranda is famous for her hats with fruit.</li>
<li>B: <b>natural</b> version. Don't explain the grammar yet; just ask: <i>Is this about now or the past?</i> (the past)</li>
<li>Extra: <i>Do you know other famous Brazilians from the 20th century?</i></li></ol>""")

    # Page 3
    rules = [("With <i>I</i> and <i>he/she/it</i>, we use", "the same form: was", "different forms"),
             ("In positive sentences, we", "don't make contractions", "make contractions"),
             ("<i>wasn't</i> and <i>weren't</i> are", "informal", "formal"),
             ("In short answers, we", "don't repeat the adjective", "repeat the adjective")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b>.</li>"
    b.page(f"""{sec(3, "Language focus: was / were", "10 min")}
{sub("A", "Read the sentences from the exhibition.", "2 min")}
<div class="bank" style="background:#fff;font-weight:600">He was a famous soccer player. · Her parents were rich. · She wasn't from Rio. · Was she famous in her time? Yes, she was.</div>
{sub("B", "Study the table.", "4 min")}
<table style="table-layout:fixed"><tr><th style="width:28mm"></th><th>Positive</th><th>Negative</th><th>Question</th><th>Short answers</th></tr>
<tr><td><b>I / he / she / it</b></td><td>I <b>was</b> happy.<br>She <b>was</b> a singer.</td><td>I <b>wasn't</b> at home.<br>He <b>wasn't</b> rich.</td><td><b>Was</b> she famous?</td><td>Yes, she <b>was</b>.<br>No, she <b>wasn't</b>.</td></tr>
<tr><td><b>you / we / they</b></td><td>We <b>were</b> at work.<br>They <b>were</b> poor.</td><td>You <b>weren't</b> late.<br>They <b>weren't</b> famous.</td><td><b>Were</b> they rich?</td><td>Yes, they <b>were</b>.<br>No, they <b>weren't</b>.</td></tr>
<tr><td><b>Wh- questions</b></td><td colspan="4">Where <b>was</b> she born? · When <b>were</b> you born? · Who <b>was</b> the painter? · What <b>was</b> he famous for?</td></tr></table>
{sub("C", "Choose the correct option.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="two"><div class="box" style="margin-top:1mm"><h4>NOW AND THE PAST</h4>am / is → <b>was</b><br>are → <b>were</b><br>I'm / she's (contractions) → I <b>was</b> / she <b>was</b> (no contractions)</div>
<div class="box sand" style="margin-top:1mm"><h4>BE BORN</h4>I <b>was born</b> in 1990. (year)<br>She <b>was born</b> in Portugal. (country, city)<br>He <b>was born</b> on May 15. (date)</div></div>""",
    24, """<ol><li>B: present has three forms (<i>am, is, are</i>); the past has only two (<i>was, were</i>). Drill the table: you say <i>she</i>, the student says <i>she was / she wasn't / Was she…?</i></li>
<li>BE BORN: in Portuguese one word (<i>nasci</i>), in English two: <b>was born</b>. Ask: <i>When were you born?</i></li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>She born in 1909.</td><td><b>She was born in 1909.</b></td><td><i>be born</i> = two words.</td></tr>
<tr><td>Her parents was rich.</td><td><b>Her parents were rich.</b></td><td>They = <i>were</i>.</td></tr>
<tr><td>Where Pelé was born?</td><td><b>Where was Pelé born?</b></td><td>Question: <i>was</i> before the name.</td></tr>
<tr><td>He was famous of his music.</td><td><b>He was famous for his music.</b></td><td>famous <i>for</i>.</td></tr>
<tr><td>Was she from Rio? Yes, she was from Rio.</td><td><b>Yes, she was.</b></td><td>Short answer: no repeat.</td></tr>
<tr><td>I was born in May 15.</td><td><b>I was born on May 15.</b></td><td>Date = <i>on</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["23.2", "23.3"])}
{sub("A", "Weak forms. Listen and repeat. In sentences, was and were are short and soft: was /wəz/, were /wər/.", "2 min", "23.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S232)}</div>
{sub("B", "Short answers. Listen and repeat. At the end, was and wasn't are strong: /wʌz/, /ˈwʌzənt/.", "3 min", "23.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S233)}</div>
{sub("C", "Strong and weak words. Read the sentences. Say the words in bold strongly.", "")}
<p style="line-height:1.8">He was a <b>German scientist</b>. &nbsp;·&nbsp; She was <b>famous</b> for her <b>paintings</b>. &nbsp;·&nbsp; His <b>father</b> was a <b>soccer player</b>.</p>""",
    32, """<ol><li>Mistakes: <i>She born</i> is the number one problem. Correct it every time the student talks about the past.</li>
<li>4A: weak <i>was</i> = /wəz/ (like "wuz"). The important words are long and loud; <i>was, a, for, his</i> are short.</li>
<li>4B–C: in short answers <i>was</i> is strong. Then ask fast questions: <i>Was Pelé a singer?</i> (No, he wasn't.)</li></ol>""")

    # Page 5
    qa = [("Text A", "Elis Regina was a famous Brazilian singer. She was born in 1945 in Porto Alegre. She was famous for her strong voice. She was married twice, and her daughter Maria Rita is a singer too.",
           [("Was Elis Regina a famous painter?", None, "No, she wasn't. She was a famous singer."),
            (None, "She was born in Porto Alegre.", "Where was Elis Regina born?"),
            ("What was she famous for?", None, "She was famous for her strong voice."),
            (None, "Yes, she was. She was married twice.", "Was Elis Regina married?")]),
          ("Text B", "Oscar Niemeyer was a Brazilian architect. He was born in 1907 in Rio de Janeiro. He was famous for his white buildings in Brasília. He was an architect for more than 70 years.",
           [("Who was Oscar Niemeyer?", None, "He was a Brazilian architect."),
            ("Was he from São Paulo?", None, "No, he wasn't. He was from Rio de Janeiro."),
            (None, "He was born in 1907.", "When was Oscar Niemeyer born?"),
            (None, "They were in Brasília.", "Where were his famous buildings?")])]
    blk = ""
    n = 0
    for title, text, items in qa:
        blk += f'<p style="margin:2mm 0 1mm;font-weight:800;color:{TEAL}">{title}</p><div class="msg" style="max-width:none;padding:2mm 4mm;margin-bottom:1.5mm">{text}</div><ol style="line-height:1.75">'
        for q, a, ans in items:
            n += 1
            if q:
                blk += f'<li value="{n}">{q} {A(ans, "min-width:70mm;text-align:left")}</li>'
            else:
                blk += f'<li value="{n}">{A(ans, "min-width:70mm;text-align:left")}? {a}</li>'
        blk += "</ol>"
    fill = [("The exhibition", "was", "great."), ("Tom and Ana", "were", "there on Saturday."), ("Pelé's parents", "weren't", "rich."),
            ("Carmen Miranda", "wasn't", "born in Brazil."), ("", "Were", "you born in São Paulo?"), ("Where", "was", "Tom Jobim from?")]
    fl = "".join(f'<li value="{n+i+1}">{a} {A(x, "min-width:18mm")} {c}</li>' for i, (a, x, c) in enumerate(fill))
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Read the texts. Write the answer or the question. Use full sentences.", "6 min")}
{blk}
{sub("B", "Complete with was, were, wasn't or weren't.", "2 min")}
<div class="two"><div><ol>{fl[:fl.index(f'<li value="{n+4}">')]}</ol></div><div><ol>{fl[fl.index(f'<li value="{n+4}">'):]}</ol></div></div>""",
    18, """<p>A: show the two examples first (questions 1 and 2). If the answer is "no", the student corrects the information, like Ana: <i>No, she wasn't. She was born in Portugal.</i> B: check with the story: <i>Were Pelé's parents rich?</i> (No, they weren't.)</p>""")

    # Page 6
    senna = [("Ayrton Senna was", "a race car driver", "Who was Ayrton Senna?"), ("He was born in", "1960", "When was he born?"),
             ("He was from", "São Paulo", "Where was he from?"), ("He was famous for his races in", "Formula 1", "What was he famous for?"),
             ("He was world champion", "three times", "How many times was he world champion?"), ("His father was", "a businessman", "Was his father a race car driver too?")]
    sl = "".join(f'<li>{a} {A(x, "min-width:32mm")}. {R("→ " + q) if T else ""}</li>' for a, x, q in senna)
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Card 1: ask your teacher questions and complete the life story.", "4 min")}
<div class="msg" style="max-width:none;padding:2mm 4mm"><ol style="line-height:1.8;margin:0">{sl}</ol></div>
<div class="bank" style="background:#fff">Who…? · When…? · Where…? · What… famous for? · How many times…? · Was his father…?</div>
{sub("B", "Card 2: answer your teacher's questions. Use full sentences.", "3 min")}
<div class="msg" style="max-width:none;padding:2mm 4mm">Alberto Santos-Dumont was an inventor and a pilot. He was born in 1873 in Minas Gerais. He was famous for his airplane, the 14-bis. His flight in Paris in 1906 was very famous. His parents were rich: his father was an engineer and a coffee farmer. He wasn't married.</div>
{sub("C", "Your past. Answer your teacher's questions.", "5 min")}
<ol><li>When and where were you born?</li><li>Who was your favorite singer or band when you were a teenager?</li><li>Was your first teacher nice? Where was your first school?</li><li>Where were you last Saturday? Who were you with?</li><li>Who is a famous person from your city or state? What was he or she famous for?</li></ol>""",
    32, """<ol><li>A: <b>Card 1 for you</b>: <i>Ayrton Senna was a race car driver. He was born in 1960. He was from São Paulo. He was famous for his races in Formula 1. He was world champion three times (1988, 1990, 1991). His father wasn't a race car driver. He was a businessman.</i></li>
<li>B: ask: <i>Who was Santos-Dumont? When was he born? What was he famous for? Were his parents poor? Was he married?</i></li></ol>""")

    # Page 7
    pc = [("Unit 20", "I can ask wh- questions: What are you doing?"), ("Unit 21", "I can ask for and give simple directions."),
          ("Unit 22", "I can talk about transportation and my plans."), ("Unit 23", "I can use was / were and say when and where I was born."),
          ("Unit 23", "I can talk about the life of a famous person.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Tom Jobim was a famous musician.", "correct"), ("He born in Rio in 1927.", "He was born in Rio in 1927."),
          ("He was famous of bossa nova.", "He was famous for bossa nova."), ("Where Tom Jobim was from?", "Where was Tom Jobim from?"),
          ("His songs was very popular in the USA.", "His songs were very popular in the USA."),
          ("Was Clarice Lispector a singer? No, she was. She was a writer.", "No, she wasn't."),
          ("She was born on 1920.", "She was born in 1920."), ("Her books were famous in many countries.", "correct")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:15mm"></th><th>In English…</th><th style="width:20mm">Easy!</th><th style="width:20mm">Sometimes</th><th style="width:20mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Correct the mistakes.</b> Six sentences have a mistake. Two sentences are correct.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. A famous life.</b> Write about a famous person from your city or state (5–6 sentences). Who was he or she? When and where was he or she born? What was he or she famous for?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the text and you ask questions about the person: <i>Was he rich? Where was he from?</i> Correct <b>was born</b> and short answers.</p>""")

    b.extra("Audio scripts", f"""
{sub("23.1", "At the exhibition (slow and natural)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("23.2", "Weak was / were")}
<p>{" ".join(S232)}</p>
{sub("23.3", "Short answers")}
<p>{" ".join(S233)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essentials 23 - 20th century lives")
