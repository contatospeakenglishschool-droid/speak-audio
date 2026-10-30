# Speak! Bridge A2 - Unit 06 "Nice guy" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 06", audio_json="audio_a2-unit-06.json", img_dir="img")

PHOTOS = [("A", "colleagues", "colleagues"), ("B", "neighbors", "houses"), ("C", "classmates", "students"), ("D", "partners", "couple"),
          ("E", "best friends", "friends"), ("F", "roommates", "roommates"), ("G", "teammates", "team"), ("H", "a boss", "boss")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-06"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["06.1 Conversations"].split("\n")]
S062 = [x.split(": ", 1)[1] for x in _r["06.2 Repeat phrases"].split("\n")]
S063 = [x.split(": ", 1)[1] for x in _r["06.3 Repeat responses"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: 8 photos (relationships)
    cover = cover_html(T, "LEVEL A2 · UNIT 06", "Nice guy", "Being nice in English · <b>compliments, congratulations and praise</b>",
                       [("YOU CAN", "say nice things to people and answer compliments politely"),
                        ("LANGUAGE", "Well done! · Congratulations on the new baby! · That color really suits you. · You're too kind."),
                        ("PRONUNCIATION", "congratuLAtions · sounding enthusiastic · suit /suːt/")])
    b.page(f"""{sec(1, "Warm-up: people in your life", "8 min")}
{sub("A", "Look at the photos. Write the words under the photos.", "3 min")}
<div class="bank">a boss · best friends · classmates · colleagues · neighbors · partners · roommates · teammates</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Answer the questions.", "5 min")}
<ol><li><i>Buddies</i> and <i>pals</i> are informal words for which people in A? {R("friends (best friends, roommates, teammates)")}</li>
<li>When did you last say something nice to one of these people? What did you say?</li></ol>""",
    22, """<ol><li>A: <b>colleagues</b> has two syllables: /ˈkɑliɡz/. <b>partner</b> = husband, wife, boyfriend or girlfriend (also used when you don't want to say which). <b>roommates</b> share an apartment.</li>
<li>B: give your own example first: <i>I told my neighbor her garden looked beautiful.</i></li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Relationships</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Four short conversations: Paulo is a nice guy</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Praising, complimenting, congratulating · polite responses</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Praising, complimenting, congratulating · responses</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Enthusiastic intonation · responses</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Cross out the extra words · Word builder: personality adjectives</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Make me say it! · compliments in Brazil and the US</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Paulo is a nice guy. In New York he praises Maya, a colleague at the travel agency (invented), for her Brooklyn food tour; he congratulates his neighbor on the new baby, Olivia; he congratulates Tom, who ran the Chicago Marathon; and on a video call he compliments his cousin <b>Carol</b> in Orlando. <b>Carol speaks for the first time</b> (fixed voice: Chirp 3 HD Leda). Maya uses the voice for one-off women (Studio-O), the neighbor a natural male voice (Chirp 3 HD Charon).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>In Portuguese one word covers birthdays and achievements, so students say <i>Congratulations!</i> ✗ on someone's birthday → <b>Happy birthday!</b> Congratulations is for achievements and news (a new job, a baby, a wedding). Also: <i>Congratulations for</i> ✗ → <b>on</b>; <i>That dress suits to you</i> ✗ → <b>suits you</b>; <i>You made a great job</i> ✗ → <b>did</b>. And Brazilians often reject compliments (<i>Oh, this old thing?</i>): in English, a simple <b>Thanks!</b> is better.</div>
<div class="box"><h4>AUDIO</h4>Track 06.1 Four conversations (slow and natural) · Track 06.2 Nice phrases · Track 06.3 Responses</div>""")

    # Page 2: listening
    who = [("Conversation 1", "a colleague"), ("Conversation 2", "a neighbor"), ("Conversation 3", "a friend"), ("Conversation 4", "a cousin")]
    wl = "".join(f"<tr><td style='width:34mm'><b>{c}</b></td><td>{A(w, 'min-width:30mm')}</td></tr>" for c, w in who)
    cw = [(["do", "done", "doing"], "done", "Well", "! Twenty five-star reviews this month!"), (["talk", "talking", "talked"], "talking", "I know you're really good at", "to tourists."),
          (["Keep up", "Make up", "Do up"], "Keep up", "", "the good work!"), (["for", "with", "on"], "on", "Congratulations", "the new baby!"),
          (["That's", "What", "Which"], "What", "", "a cute little girl!"), (["Bad", "Sad", "Glad"], "Glad", "", "to hear it. Good luck!"),
          (["job", "done", "made"], "job", "Wow, good", "!"), (["helps", "makes", "suits"], "suits", "That dress really", "you.")]
    cwl = [f'<li value="{i+1}">{a} {ch(o, r)} {c}</li>' for i, (o, r, a, c) in enumerate(cw)]
    b.page(f"""{sec(2, "Listening: is Paulo a nice guy?", "10 min")}
<p>Listen to four conversations Paulo has in New York. Who is he speaking to? One option is extra.</p>
{audiocard(["06.1 · SLOW", "06.1 · NATURAL"])}
{sub("A", "Listen and complete with these people.", "3 min", "06.1 · SLOW")}
<div class="bank">a classmate · a colleague · a cousin · a friend · a neighbor</div>
<table style="table-layout:fixed;margin-top:0;width:70%">{wl}</table>
<p class="small">Extra: {R("a classmate")} · Is Paulo a nice guy? Why? {R("Yes: he says something positive in every conversation.")}</p>
{sub("B", "Choose the correct word. Then listen again and check.", "5 min", "06.1 · NATURAL")}
{twocol(cwl, 5)}
{sub("C", "Which conversation do you like best? Why?", "2 min")}""",
    22, """<p>A: play the slow version; stop after each conversation if needed. Ask for clues: <i>travel agency, new baby, marathon, video call</i>. B: the student guesses, then listens. If there's time, read one conversation each from the script (TB last page), with lots of enthusiasm!</p>""")

    # Page 3
    fx = [("Well done.", "praising"), ("What a cute little girl!", "complimenting"), ("Congratulations on the new baby!", "congratulating"),
          ("I know you're good at talking to tourists.", "praising"), ("You look great today!", "complimenting"), ("Glad to hear it. Good luck!", "congratulating"),
          ("Keep up the good work!", "praising"), ("That dress really suits you.", "complimenting")]
    cols = {"praising": [], "complimenting": [], "congratulating": []}
    for p, f in fx:
        cols[f].append(p)
    rs = [("Thanks!", "g"), ("Actually, my boss gave it to me.", "c"), ("You too!", "d"), ("You're too kind.", "a"), ("I'll take that, thanks!", "b"),
          ("It was a team effort.", "f"), ("I'm glad you like it.", "e")]
    mean = ["a. a polite, more formal way to accept a compliment", "b. an informal way to accept praise", "c. you explain where or how you got something",
            "d. you return the compliment", "e. you talk about the other person's feelings", "f. you share the praise with other people", "g. the standard answer to everything"]
    rl = "".join(f"<tr><td style='width:62mm'>{i+1}. {r} {R(m)}</td><td class='small'>{mean[i]}</td></tr>" for i, (r, m) in enumerate(rs))
    b.page(f"""{sec(3, "Language focus: being nice", "10 min")}
{sub("A", "Read the three functions. Then write each phrase from the listening in the correct column.", "4 min")}
<p class="small"><b>praising</b> = saying someone's work or actions are good · <b>complimenting</b> = saying something nice about how someone looks or what they have · <b>congratulating</b> = reacting to good news</p>
<div class="bank" style="background:#fff">{" · ".join(p for p, _ in fx)}</div>
<table style="table-layout:fixed;margin-top:0;font-size:9pt"><tr><th>praising</th><th>complimenting</th><th>congratulating</th></tr>
<tr>{"".join(f"<td style='vertical-align:top;height:16mm'>{R('<br>'.join(cols[k]))}</td>" for k in ("praising", "complimenting", "congratulating"))}</tr></table>
{sub("B", "Polite responses. Match each response with its meaning.", "4 min")}
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt">{rl}</table>
<div class="box sand"><h4>PATTERNS</h4><b>What a</b> + adjective + noun: <i>What a nice boss!</i> · <b>What</b> + adjective + plural/uncountable noun: <i>What beautiful eyes! What great hair!</i><br><b>Congratulations on</b> + noun / -ing: <i>Congratulations on your new job / on passing the test!</i> · <b>good at</b> + -ing (Unit 04!)</div>""",
    24, """<ol><li>A: drill each phrase with real enthusiasm. The fixed part (<i>What a…</i>, <i>Congratulations on…</i>) never changes; change only the adjective and noun.</li>
<li>B: ask: <i>In Brazil, do people accept compliments easily?</i> In the US, a simple <i>Thanks!</i> is normal.</li></ol>""")

    # Grammar reference (before Common mistakes)
    grammar_ref.being_nice(b)

    # Page 4
    b.page(f"""{sub("C", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>Congratulations! (on a birthday)</td><td><b>Happy birthday!</b></td><td>congratulations = achievements, news.</td></tr>
<tr><td>Congratulations for your new job!</td><td><b>Congratulations on your new job!</b></td><td>congratulations on.</td></tr>
<tr><td>That dress suits to you.</td><td><b>That dress suits you.</b></td><td>no preposition.</td></tr>
<tr><td>You made a great job.</td><td><b>You did a great job.</b></td><td>do a job.</td></tr>
<tr><td>You're too much kind.</td><td><b>You're too kind.</b></td><td>too + adjective.</td></tr>
<tr><td>What a beautiful!</td><td><b>What a beautiful dress!</b></td><td>what a + adjective + noun.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["06.2", "06.3"])}
{sub("A", "Nice phrases. Listen and repeat. Sound happy!", "2 min", "06.2")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S062)}</div>
{sub("B", "Responses. Listen and repeat.", "2 min", "06.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S063)}</div>
<div class="box" style="margin-top:1mm"><h4>SOUND ENTHUSIASTIC</h4>Start high and go down on the important word: <i>Well <b>DONE</b>! What a <b>CUTE</b> baby!</i> Stress: congratu<b>LA</b>tions (5 syllables). <b>suit</b> = /suːt/, one syllable (not "su-EE-t").</div>""",
    24, """<ol><li>4A: Brazilians often sound flat in English. Exaggerate the pitch; a flat <i>Well done</i> can sound sarcastic.</li>
<li>4B: <i>effort</i> = <b>EF</b>-fort; <i>too kind</i>: stress <b>KIND</b>.</li></ol>""")

    # Page 5
    dg = [("Classmates", [("A:", "Can I read your essay? I know you're good at <s>the</s> writing."), ("B:", "Sure. Here you are."), ("A:", "Wow, this is amazing. Well <s>you</s> done!"), ("B:", "You're too <s>much</s> kind.")]),
          ("Colleagues", [("A:", "I just wanted to say that you <s>made</s> did a great job on the report."), ("B:", "Thanks, but it was <s>our</s> a team effort."), ("A:", "Keep <s>it</s> up the good work.")]),
          ("Partners", [("A:", "I have a new haircut. What do you think?"), ("B:", "It looks great! It really suits <s>to</s> you."), ("A:", "Thanks. I'll take that <s>up</s>. Your new sweater looks good too."), ("B:", "I'm glad you <s>are</s> like it.")])]
    def line(t):
        import re
        return re.sub(r"<s>(.*?)</s>", (lambda m: f"<s style='color:#c0392b'>{m.group(1)}</s>") if T else (lambda m: m.group(1)), t)
    dgh = "".join(f"<div style='flex:1;border:1pt solid #c9dfe3;border-radius:2mm;padding:1.5mm 2.5mm;font-size:8.8pt'><b style='color:#0f4a5a'>{h if T else f'Dialogue {i+1}'}</b><br>" + "<br>".join(f"<b>{s}</b> {line(t)}" for s, t in ls) + "</div>" for i, (h, ls) in enumerate(dg))
    adj = [("kind", "nice and caring to other people"), ("generous", "happy to give money, time or help"), ("polite", "says please and thank you"),
           ("modest", "doesn't talk about how good they are"), ("big-headed", "thinks they are better than other people"), ("helpful", "always ready to help")]
    al = [f'<li value="{i+1}">{A(w, "min-width:20mm")} = {d}</li>' for i, (w, d) in enumerate(adj)]
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Each dialogue has extra words that we don't need. Cross them out. Who are the speakers: classmates, colleagues or partners?", "4 min")}
<div style="display:flex;gap:2mm">{dgh}</div>
<p class="small">{R("Dialogue 1 extra words: the · you · much · Dialogue 2: made · our · it · Dialogue 3: to · up · are")}</p>
{sub("B", "Word builder: personality. Complete with the adjectives.", "4 min")}
<div class="bank">big-headed · generous · helpful · kind · modest · polite</div>
{twocol(al, 4)}
<p class="small">Which adjectives describe Paulo? And you?</p>""",
    22, """<ol><li>A: then the student reads the dialogues aloud with you, with good intonation.</li>
<li>B: from the bonus lesson <i>Character and behaviour</i> (Vocabulary to Go). <b>big-headed</b> is the opposite of <b>modest</b>. Responses like <i>It was a team effort</i> sound modest.</li></ol>""")

    # Page 6
    cards = {"compliments": ["That … really suits you.", "Where did you get it?", "What a …!", "You look … today."],
             "congratulations": ["Congratulations on …!", "Glad to hear it.", "Good luck!", "Happy birthday!"],
             "praise": ["Well done!", "Good job!", "I know you're good at …", "Keep up the good work!"],
             "responses": ["Thanks!", "You too!", "You're too kind.", "It was a team effort.", "I'm glad you like it.", "Actually, my … gave it to me."]}
    ct = "".join(f"<td style='vertical-align:top;font-size:8.6pt'>" + "".join(f"☐ {x}<br>" for x in v) + "</td>" for v in cards.values())
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Make me say it! Secretly check (✓) two phrases in each column. Then create situations and make your teacher say your phrases. Then change roles.", "7 min")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<th>{k}</th>" for k in cards)}</tr><tr>{ct}</tr></table>
<div class="msg" style="max-width:none;padding:1.5mm 4mm;line-height:1.5"><b>You</b> (checked <i>What a …!</i>): Look, this is my new puppy! <b>Teacher:</b> Congratulations! <b>You:</b> No, try again. Look at him! <b>Teacher:</b> What a cute dog! <b>You:</b> Yes!</div>
{sub("B", "Compliments in Brazil and in the US.", "5 min")}
<ol><li>When did someone last give you a compliment? What did you say?</li><li>In Brazil, is it normal to say the price of something when someone likes it?</li>
<li>Is it OK to compliment a colleague on their clothes at work? What about their work?</li><li>Who is the nicest person you know? Why?</li></ol>""",
    26, """<ol><li>A: use mime and real objects (a mug, your shirt, a photo on your phone). Don't accept the phrase until it's exact. Then change roles: you check phrases and the student has to guess.</li>
<li>B: in American workplaces, people usually praise work more than appearance.</li></ol>""")

    # Page 7
    pc = [("A2 Unit 02", "I can use verb + to, verb + -ing and verb + person + to."), ("A2 Unit 03", "I can describe a place with my senses and use state verbs correctly."),
          ("A2 Unit 04", "I can use adjectives and nouns with the right preposition."), ("A2 Unit 05", "I can ask about words in class and name parts of speech."),
          ("A2 Unit 06", "I can praise, compliment and congratulate people, and respond politely.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    ow = [("ring / a / What / beautiful / !", "What a beautiful ring!"), ("did / get / it / Where / you / ?", "Where did you get it?"),
          ("on / Congratulations / the wedding / !", "Congratulations on the wedding!"), ("presentation / done / Well / great / your / was / . / , ", "Well done, your presentation was great."),
          ("glad / it / I'm / enjoyed / you / .", "I'm glad you enjoyed it.")]
    owl = "".join(f"<li><i>{p}</i><div class='wline'>{R(s)}</div></li>" for p, s in ow)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Put the words in order.</b></p>
<ol>{owl}</ol>
<p style="margin-top:2mm"><b>2. Greeting cards (50–75 words).</b> Write two short card messages for people in your life: choose from a new baby, a graduation, a new job, a wedding anniversary or passing a driving test. Use phrases from page 3.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: the student reads the cards; you respond politely with a phrase from page 3. Check <i>congratulations on</i> and the <i>What a…!</i> pattern.</p>""")

    b.extra("Audio scripts", f"""
{sub("06.1", "Four conversations (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(f"<b>{n}:</b> {t}" if n != "Narrator" else f"<i>{t}</i>" for n, t in SCRIPT)}</p>
{sub("06.2", "Nice phrases")}
<p>{" · ".join(S062)}</p>
{sub("06.3", "Responses")}
<p>{" ".join(S063)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 06 - Nice guy")
