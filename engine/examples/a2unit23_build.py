# Speak! Bridge A2 - Unit 23 "My team" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 23", audio_json="audio_a2-unit-23.json", img_dir="img")

PHOTOS = [("A", "stadium", "a stadium"), ("B", "fans", "fans"), ("C", "whistle", "a whistle"), ("D", "team", "a team"),
          ("E", "trophy", "a trophy"), ("F", "seats", "seats"), ("G", "training", "training"), ("H", "ball", "a ball")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-23"]
S231 = [x.split(": ", 1)[1] for x in _r["23.1 Lovable losers no more"].split("\n")]
S232 = [x.split(": ", 1)[1] for x in _r["23.2 Repeat: I'd and wouldn't"].split("\n")]
S233 = [x.split(": ", 1)[1] for x in _r["23.3 Will or would"].split("\n")]

# printed version of the article (digits, bold words for the Word builder)
ARTICLE = [
    "For more than a hundred years, the Chicago Cubs were baseball's favorite <b>underdog</b>. The team didn't win the World Series from 1908 to 2016. That's 108 years without a <b>title</b>, one of the longest waits in American sports.",
    "Many fans <b>blamed</b> a goat. According to a famous Chicago <b>legend</b>, in 1945 a local tavern owner, Billy Sianis, tried to bring his goat to a World Series game at Wrigley Field. The goat wasn't allowed in, and the story says that Sianis put a <b>curse</b> on the team. The Cubs didn't play in another World Series for 71 years.",
    "Then, in November 2016, everything changed. The Cubs were losing the World Series three games to one, but they won three games <b>in a row</b>. In Game 7, they beat Cleveland 8–7 in ten innings. That Friday, about five million people came to the victory <b>parade</b> and rally, according to city officials.",
    "Today, the Cubs are a normal team again. Some <b>seasons</b> are good, and some are bad. But the fans haven't changed. We asked people at a coffee shop in Chicago how they feel about their team.",
    "\"If the Cubs won every year, it wouldn't feel so special,\" says Tom, a teacher. Rita, the manager of the coffee shop, agrees. \"If I had more free time, I'd go to every home game. And if the tickets were cheaper, more families would go.\" For Kate, who owns a bakery, it isn't about winning. \"I'd still be a fan if they lost every game this season. That's what fans do.\"",
    "So, is winning the most important thing? Not in Chicago. As one fan told us, \"If winning were easy, nobody would care.\""]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 23", "My team", "Sports and fans · <b>the second conditional</b>",
                       [("YOU CAN", "imagine a different situation and talk about its results"),
                        ("LANGUAGE", "If I had more free time, I'd go to every game. · If they lost every game, I'd still be a fan."),
                        ("PRONUNCIATION", "I'd /aɪd/ or I'll /aɪl/? · wouldn't /ˈwʊdnt/")])
    b.page(f"""{sec(1, "Warm-up: going to a game", "8 min")}
{sub("A", "Write the words under the pictures.", "4 min")}
<div class="bank">ball · fans · seats · stadium · team · training · trophy · whistle</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "4 min")}
<ol><li>Do you support a sports team? Which one? How long have you been a fan?</li><li>Do you prefer to watch games at the stadium, at home or in a bar? Why?</li><li>Is your team usually a winner or an underdog (the team nobody expects to win)?</li></ol>""",
    24, """<ol><li>A: <i>fans</i> and <i>seats</i> are plural; <i>training</i> is uncountable. In American English, <i>soccer</i> = football; <i>football</i> = American football.</li>
<li>B: teach <b>underdog</b> now; it comes back in the reading. Most Brazilian students have a soccer team; let them talk.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Sports words · your team</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>Article: Why Chicago still loves the Cubs</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Second conditional · first or second?</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Second conditional: form, zero/first/second, reality → imagination</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>I'd / I'll · wouldn't</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>From reality to imagination · Word builder: words from the article</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guess my sentence</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>A Chicago newspaper writes about Cubs fans and interviews people at City Coffee: Tom (teacher), Rita (manager) and Kate (Sweet Kate Bakery). Read by the Reporter (Studio-O). Facts: the Cubs won the 2016 World Series, their first title since 1908, beating Cleveland 8–7 in ten innings in Game 7 after trailing the series 3–1 (AP, via NPR/MPR News, November 3, 2016). City officials estimated about five million people at the parade and rally on Friday, November 4, 2016 (CBS News; CNN). The Billy Goat legend: in 1945 tavern owner William "Billy Goat" Sianis was turned away from Game 4 at Wrigley Field with his goat; the "curse" is a story, and the details vary (Baseball-Reference Bullpen). The Cubs next played in a World Series in 2016. The original lesson is about a Scottish team; we replaced it with an American story.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses a special verb form in the <i>if</i> clause, so students say <i>If I would have money…</i> ✗. They also mix <i>will</i> and <i>would</i> (<i>If I had time, I will go</i> ✗), drop <i>would</i> in the result, and can't hear the difference between <i>I'd</i> and <i>I'll</i>.</div>
<div class="box"><h4>AUDIO</h4>Track 23.1 Lovable losers no more (article, slow and natural) · Track 23.2 Repeat: I'd and wouldn't · Track 23.3 Will or would</div>""")

    # Page 2
    qs = [("How long did Cubs fans wait for a World Series title?", "108 years (1908–2016)"),
          ("According to the legend, why did Billy Sianis put a curse on the team?", "his goat wasn't allowed in to a game at Wrigley Field"),
          ("How did the Cubs win the 2016 World Series?", "they won three games in a row and Game 7, 8–7 in ten innings"),
          ("How many people came to the parade?", "about five million"),
          ("Why does Tom think it's OK that the Cubs don't win every year?", "if they won every year, it wouldn't feel so special")]
    ql = "".join(f"<li>{q} {A(a, 'min-width:40mm')}</li>" for q, a in qs)
    art = "".join(f"<p style='margin:0 0 1mm'>{p}</p>" for p in ARTICLE)
    b.page(f"""{sec(2, "Reading: lovable losers", "10 min")}
{audiocard(["23.1 · SLOW", "23.1 · NATURAL"])}
<div class="box" style="margin-top:1mm;font-size:8.8pt;line-height:1.42"><div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1"><h4 style="font-size:11pt;margin:0 0 .5mm">Lovable losers no more? Why Chicago still loves the Cubs</h4>{art[:art.index('</p>') + 4]}</div>{img('I', 32, 24)}</div>{art[art.index('</p>') + 4:]}</div>
{sub("A", "Read and listen to the article. Answer the questions.", "6 min", "23.1 · SLOW")}
<ol style="line-height:1.5">{ql}</ol>
{sub("B", "Do you think that winning is the most important thing in sports? Why or why not?", "2 min")}""",
    18, """<ol><li>A: let the student read first, then play the natural version. <i>Lovable losers</i> is an old nickname for the Cubs. <i>Innings</i>: a baseball game usually has nine; Game 7 needed a tenth.</li>
<li>B: connect to Brazilian soccer: teams that waited a long time for a title, or fans who stay loyal after relegation.</li></ol>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: the second conditional", "10 min")}
{sub("A", "Study the sentences from the article.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. If the Cubs <b>won</b> every year, it <b>wouldn't feel</b> so special.<br>
2. If I <b>had</b> more free time, I<b>'d go</b> to every home game.<br>
3. If the tickets <b>were</b> cheaper, more families <b>would go</b>.<br>
4. I<b>'d still be</b> a fan if they <b>lost</b> every game this season.<br>
5. If winning <b>were</b> easy, nobody <b>would care</b>.</div>
{sub("B", "Choose the best option to complete the rules.", "5 min")}
<ol style="line-height:1.75"><li>The condition comes after {ch(["if", "would"], "if")}, and the verb there is in the {ch(["present simple", "past simple"], "past simple")}.</li>
<li>The result uses {ch(["will + verb", "would + verb"], "would + verb")}. <b>'d</b> is the short form of {ch(["would", "did"], "would")}.</li>
<li>These sentences are about {ch(["the past", "the present or future"], "the present or future")}. They describe situations that are {ch(["real and likely", "imagined or unlikely"], "imagined or unlikely")}.</li>
<li>Sentence 4 starts with the result. We {ch(["need", "don't need"], "don't need")} a comma.</li></ol>
{sub("C", "Compare. In which sentence does the speaker think the team will probably NOT win?", "3 min")}
<ol type="a"><li>If they <b>win</b> on Sunday, we<b>'ll</b> celebrate.</li><li>If they <b>won</b> on Sunday, we<b>'d</b> celebrate. {R("✓ (past form = unlikely)")}</li></ol>
<div class="box sand"><h4>RULE</h4><b>If + past simple, would / 'd + verb</b> = an imagined or unlikely situation now or in the future: <i>If I had more time, I'd go to every game.</i> (Reality: I don't have time.) With <b>be</b>: <i>If I were you…</i> More on the next page: <b>Grammar reference</b>.</div>""",
    22, """<ol><li>B: ask the student for the reality behind each sentence: 2 = Rita doesn't have much free time; 3 = the tickets are expensive.</li>
<li>C: review the first conditional from Unit 13. Drill with hump intonation: rise on the <i>if</i> clause, fall on the result.</li></ol>""")

    grammar_ref.second_conditional(b)

    # Page 5
    ans3 = ["I'll", "I'd", "we'd", "we'll", "she'd", "they'll"]
    pairs = [("I'll", "I'd"), ("I'll", "I'd"), ("we'll", "we'd"), ("we'll", "we'd"), ("she'll", "she'd"), ("they'll", "they'd")]
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>If I would have money, I would travel.</td><td><b>If I had money, I'd travel.</b></td><td>no would after if.</td></tr>
<tr><td>If I had time, I will go to the game.</td><td><b>…I would go to the game.</b></td><td>past + would.</td></tr>
<tr><td>If I won the lottery, I buy a house.</td><td><b>…I'd buy a house.</b></td><td>the result needs would.</td></tr>
<tr><td>We'd be happy if our team would win.</td><td><b>…if our team won.</b></td><td>if + past simple.</td></tr>
<tr><td>What you would do if you were rich?</td><td><b>What would you do…?</b></td><td>question: would + you.</td></tr>
<tr><td>If I am you, I'd talk to the coach.</td><td><b>If I were you…</b></td><td>advice: If I were you.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["23.2", "23.3"])}
{sub("A", "Listen and repeat. 'd is very short: I'd /aɪd/. wouldn't /ˈwʊdnt/ has no l sound.", "2 min", "23.2")}
<p style="line-height:1.55;margin:.5mm 0">{" · ".join(S232)}</p>
{sub("B", "Listen. Which do you hear? Choose while you listen.", "2 min", "23.3")}
{twocol([f'<li value="{i+1}">{ch(list(p), a)}</li>' for i, (p, a) in enumerate(zip(pairs, ans3))], 4)}""",
    24, """<ol><li>A: the <i>l</i> in <i>would</i> is silent. Students often pronounce <i>wouldn't</i> as <i>won't</i>; contrast /ˈwʊdnt/ and /woʊnt/.</li>
<li>B: after checking, the student says each sentence and the teacher points to the form they hear.</li></ol>""")

    # Page 6
    pp = [("Rita doesn't have much free time, so she doesn't go to many games.", "If Rita had more free time, she'd go to more games."),
          ("The tickets are expensive, so many families stay at home.", "If the tickets weren't so expensive, more families would go."),
          ("Tom isn't a professional player, so he doesn't play at Wrigley Field.", "If Tom were a professional player, he'd play at Wrigley Field."),
          ("The team doesn't train much, so the players aren't very fit.", "If the team trained more, the players would be fitter."),
          ("I live far from the stadium, so I watch the games on TV.", "If I lived near the stadium, I wouldn't watch the games on TV."),
          ("We lose a lot of games because our best player is injured.", "We wouldn't lose so many games if our best player weren't injured.")]
    ppl = "".join(f"<li>{a}<br>{A(c, 'min-width:110mm')}</li>" for a, c in pp)
    wb = [("blame", "to say that someone or something caused a problem"), ("curse", "magic words that bring bad luck"),
          ("in a row", "one after another, with no break"), ("legend", "an old, famous story that may not be true"),
          ("parade", "a public event where people walk or ride through the streets to celebrate"), ("season", "the part of the year when a sport is played"),
          ("title", "the prize for being the best team in a competition"), ("underdog", "the team or person that nobody expects to win")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:16mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Practice", "9 min")}
{sub("A", "From reality to imagination. Rewrite the sentences with the second conditional. Use 'd and wouldn't when you can.", "5 min")}
<p class="small" style="margin:0 0 .5mm"><b>Example:</b> He doesn't like training, so he isn't very fit. → <i>If he liked training, he'd be fitter.</i></p>
<ol style="line-height:1.55">{ppl}</ol>
{sub("B", "Word builder: words from the article. Write the words in bold from the article next to their meanings.", "4 min")}
<div class="bank">blame · curse · in a row · legend · parade · season · title · underdog</div>
<ol style="line-height:1.5;font-size:9pt">{"".join(wbl)}</ol>""",
    25, """<ol><li>A: remind the student that positive often becomes negative and vice versa. Other correct answers are fine (e.g. 2: <i>If the tickets were cheaper, many families wouldn't stay at home</i>). In 6, the result comes first.</li>
<li>B: ask: <i>Which Brazilian team is a famous underdog? Have you ever been to a victory parade?</i></li></ol>""")

    # Page 7
    frames = [("If I ________, I'd celebrate with my friends and family.", "won the lottery"),
              ("If my team lost ten games in a row, I'd ________.", "still watch every game"),
              ("If ________, more tourists would visit Brazil.", "our cities were safer"),
              ("If I were a professional athlete, I'd ________.", "play volleyball"),
              ("If I had more free time, I'd ________.", "learn to play the guitar")]
    fl = "".join(f"<li>{f} {R('(teacher: ' + a + ')') if T else ''}</li>" for f, a in frames)
    b.page(f"""{sec(6, "Speaking: guess my sentence", "12 min")}
{sub("A", "Complete the sentences with your own ideas. Don't show your teacher.", "3 min")}
<ol style="line-height:1.85">{fl}</ol>
{sub("B", "Your teacher tries to guess your words. They have three guesses for each sentence. Help them. Then guess your teacher's sentences.", "6 min")}
<div class="box" style="margin-top:1mm;font-size:9pt"><h4>USEFUL LANGUAGE</h4>The first word is… · A key word is… · The next word starts with the letter S. · There are four words. · That's the right idea. Try again! · You're close! · Nope, sorry!</div>
{sub("C", "Talk about it.", "3 min")}
<ol><li>If you could meet any athlete, who would it be? What would you ask?</li><li>If your team won the most important title this year, how would you celebrate?</li><li>If you were the coach of your favorite team, what would you change?</li></ol>""",
    26, """<ol><li>B: the student guesses the red sentences; the teacher gives clues with the useful language. Insist on full sentences: <i>If you won the lottery, you'd celebrate.</i></li>
<li>C: listen for <i>would</i> in the if clause and correct it at the end.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 19", "I can tell the story of someone's life with the past simple."), ("A2 Unit 21", "I can tell a story with the past continuous and the past simple."),
          ("A2 Unit 22", "I can compare my life then and now with used to."), ("A2 Unit 23", "I can imagine a different situation with the second conditional.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("If we would win the game, we'd celebrate.", "If we won the game…"), ("I'd buy a ticket if I had the money.", "✓"),
          ("If she were the coach, she will change the team.", "…she'd change the team."), ("If they trained more, they win more games.", "…they'd win more games."),
          ("If I lived in Chicago, I'd go to Wrigley Field.", "✓"), ("What you would do if you won the lottery?", "What would you do…?")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:40mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Find and correct the mistakes. Two sentences are correct.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. If I were the coach (50–75 words).</b> Imagine you are the coach of your favorite team, or the team of your city. What would you change? What would you do on your first day? What would the fans say?</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the text aloud. Ask follow-up questions: <i>What would you do if the team lost the first game?</i></p>""")

    b.extra("Audio script", f"""
{sub("23.1", "Lovable losers no more (slow and natural)")}
<p style="line-height:1.4">{"<br>".join(S231)}</p>
{sub("23.2", "Repeat: I'd and wouldn't")}
<p>{" · ".join(S232)}</p>
{sub("23.3", "Will or would")}
<p>{" · ".join(S233)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 23 - My team")
