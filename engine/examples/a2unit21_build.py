# Speak! Bridge A2 - Unit 21 "Fables" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 21", audio_json="audio_a2-unit-21.json", img_dir="img")

PHOTOS = [("A", "fox · clever", "a fox"), ("B", "mouse · weak", "a mouse"), ("C", "goat · silly", "a goat"), ("D", "ant · hard-working", "an ant"),
          ("E", "tortoise · slow", "a tortoise"), ("F", "lion · strong", "a lion"), ("G", "hare · fast", "a hare"), ("H", "grasshopper · lazy", "a grasshopper")]

_r = json.load(open("roteiro.json"))["units"]["a2-unit-21"]
S211 = [x.split(": ", 1)[1] for x in _r["21.1 The Tortoise and the Hare"].split("\n")]
S212 = [x.split(": ", 1)[1] for x in _r["21.2 The Ants and the Grasshopper"].split("\n")]
S213 = [x.split(": ", 1)[1] for x in _r["21.3 Weak was and were"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'

    # Page 1
    cover = cover_html(T, "LEVEL A2 · UNIT 21", "Fables", "Animal stories · <b>past continuous and past simple</b>",
                       [("YOU CAN", "tell a story and describe what was happening in the past"),
                        ("LANGUAGE", "One day, a hare was watching a tortoise. · While the hare was sleeping, the tortoise passed him."),
                        ("PRONUNCIATION", "weak was /wəz/ · were /wər/ · strong in short answers: Yes, he WAS.")])
    b.page(f"""{sec(1, "Warm-up: animals in fables", "8 min")}
<p style="margin:0 0 1mm"><b>Fables</b> are short stories. The main characters are often animals, and at the end there's a <b>moral</b>: an important lesson we can learn from the story.</p>
{sub("A", "Write the animal. Then match each animal with the quality it often has in fables.", "5 min")}
<div class="bank">ant · fox · goat · grasshopper · hare · lion · mouse · tortoise</div>
<div class="bank" style="background:#fff">clever · fast · hard-working · lazy · silly · slow · strong · weak</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Talk about it.", "3 min")}
<ol><li>Do you know any fables about these animals? Which animals go together in the stories?</li><li>Did someone tell you stories when you were a child? Who?</li></ol>""",
    22, """<ol><li>A: qualities are a little cultural; accept any reasonable answer. A <b>hare</b> is a wild animal similar to a big rabbit. Drill <i>tortoise</i> /ˈtɔːrtəs/ (TOR-tus) and <i>hare</i> (= hair).</li>
<li>B: don't retell the stories now; they come later in the lesson.</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Animals and qualities in fables</td><td>1</td></tr>
<tr><td>2 Listening</td><td>10 min</td><td>Story time: The Tortoise and the Hare</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Past continuous vs past simple · while / when</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Past continuous: form, uses, state verbs</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>4 min</td><td>Weak and strong was / were</td><td>5</td></tr>
<tr><td>5 Practice</td><td>9 min</td><td>The Ants and the Grasshopper · Word builder: animal sounds</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Tell a fable: The Lion and the Mouse / The Fox and the Goat</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework</td><td>8</td></tr></table>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Tom is a teacher at a school in Chicago (voice Neural2-D). It's story time, and he reads <i>The Tortoise and the Hare</i> to his class from an old book. Facts: <i>The Aesop for Children</i>, with pictures by Milo Winter, was published in Chicago by Rand McNally &amp; Co. in 1919. It has more than 140 fables, it's in the public domain, and the Library of Congress has a free online version (Library of Congress, read.gov/aesop, and catalog record LCCN 19014083). Aesop was a storyteller in ancient Greece (Encyclopaedia Britannica). The original lesson says <i>rabbit</i>; the traditional English title is <i>The Tortoise and the Hare</i>.</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Students use the simple past for the background (<i>One day, a hare watched…</i>: possible, but less natural when setting a scene), forget <i>was/were</i> (<i>They working</i> ✗), mix <i>was/were</i> (<i>They was</i> ✗) and use state verbs with -ing (<i>I was knowing</i> ✗).</div>
<div class="box"><h4>AUDIO</h4>Track 21.1 The Tortoise and the Hare (slow and natural) · Track 21.2 The Ants and the Grasshopper · Track 21.3 Weak was and were</div>""")

    # Page 2
    vf = [(["watched", "was watching"], "was watching", "One day, a hare", "a tortoise. He", (["laughed", "was laughing"], "was laughing"), "because the tortoise was so slow."),
          (["thought", "was thinking"], "thought", "The hare", "this was a funny idea, but he agreed. They", (["decided", "were deciding"], "decided"), "on the start and finish lines."),
          (["looked", "was looking"], "looked", "After a few minutes, the hare", "back. He", (["didn't see", "wasn't seeing"], "didn't see"), "the tortoise."),
          (["slept", "was sleeping"], "was sleeping", "While the hare", ", the tortoise", (["walked", "was walking"], "was walking"), "as fast as he could.")]
    vfl = "".join(f"<li>{a} {ch(o, r)} {m} {ch(o2[0], o2[1])} {e}</li>" for o, r, a, m, o2, e in vf)
    mo = ["Don't laugh at other people.", "You should never take a rest.", "It's better to do things slowly and carefully, and not give up."]
    mol = "".join(f"<li>{m}{(' ' + R('✓ (best)')) if i == 2 else ''}</li>" for i, m in enumerate(mo))
    b.page(f"""{sec(2, "Listening: story time", "10 min")}
<div style="display:flex;gap:3mm;align-items:center"><p style="flex:1;margin:0">Tom is a teacher at a school in Chicago. It's story time, and he's reading to his class from a very old book. The story is <b>The Tortoise and the Hare</b>. Do you know it? What happens?</p>{img('I', 34, 22)}{img('E', 30, 22)}</div>
{audiocard(["21.1 · SLOW", "21.1 · NATURAL"])}
{sub("A", "Listen to the introduction. Answer the questions.", "2 min", "21.1 · SLOW")}
<ol><li>Where and when was the book published? {A("in Chicago, in 1919", "min-width:40mm")}</li><li>Who was Aesop? {A("a storyteller in ancient Greece", "min-width:50mm")}</li></ol>
{sub("B", "Listen to the story. Choose the best moral.", "2 min")}
<ol>{mol}</ol>
{sub("C", "Listen again. Choose the verb forms that you hear.", "5 min", "21.1 · NATURAL")}
<ol style="line-height:1.7">{vfl}</ol>""",
    22, """<p>A: <i>The Aesop for Children</i> (Chicago, 1919) is free online at the Library of Congress. B: 3 is the strongest lesson. C: let the student guess first, then listen.</p>""")

    # Page 3
    b.page(f"""{sec(3, "Language focus: past continuous and past simple", "10 min")}
{sub("A", "Study the sentences from the story.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. One day, a hare <b>was watching</b> a tortoise. He <b>was laughing</b> because the tortoise was so slow.<br>
2. The hare <b>thought</b> this was a funny idea, but he <b>agreed</b>. They <b>decided</b> on the start and finish lines.<br>
3. After a few minutes, the hare <b>looked</b> back. He <b>didn't see</b> the tortoise, so he <b>decided</b> to take a rest.<br>
4. <b>While</b> the hare <b>was sleeping</b>, the tortoise <b>passed</b> him.</div>
{sub("B", "Choose the best option to complete the rules.", "6 min")}
<ol style="line-height:1.75"><li>The verbs in 2 and 3 are {ch(["past continuous", "past simple"], "past simple")}. They describe {ch(["finished actions", "actions in progress"], "finished actions")}, one after the other.</li>
<li>The verbs in 1 are {ch(["past continuous", "past simple"], "past continuous")}. They describe {ch(["finished actions", "actions in progress"], "actions in progress")} at a time in the past.</li>
<li>We make the past continuous with {ch(["was / were + verb-ing", "is / are + verb-ing"], "was / were + verb-ing")}.</li>
<li>We often use the {ch(["past continuous", "past simple"], "past continuous")} at the beginning of a story to set the scene.</li>
<li>State verbs don't usually take -ing. In 1–3, two state verbs are {ch(["decide and look", "see and think"], "see and think")}.</li>
<li>In 4, the past continuous is the {ch(["long action", "short action"], "long action")}, and the past simple is the {ch(["long action", "short action"], "short action")} that happens in the middle of it.</li></ol>
<div class="box sand"><h4>RULE</h4><b>was / were + verb-ing</b> = an action in progress: <i>The ants were working.</i> Long action + short action: <i><b>While</b> I was walking home, it started to rain. / I was walking home <b>when</b> it started to rain.</i> More on the next page: <b>Grammar reference</b>.</div>""",
    24, """<ol><li>B: ask the student to justify each answer with the sentences in A. Drill the forms: <i>I was / you were / he was / they were</i>.</li>
<li>Personalize: <i>What were you doing at 8 o'clock last night? What were you doing when I arrived?</i></li></ol>""")

    grammar_ref.past_continuous(b)

    # Page 5
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>They working in the sun.</td><td><b>They were working in the sun.</b></td><td>was / were + -ing.</td></tr>
<tr><td>The ants was hungry.</td><td><b>The ants were hungry.</b></td><td>plural = were.</td></tr>
<tr><td>What you were doing?</td><td><b>What were you doing?</b></td><td>question: were + you.</td></tr>
<tr><td>I was knowing the answer.</td><td><b>I knew the answer.</b></td><td>state verb, no -ing.</td></tr>
<tr><td>I was sleeping when the phone was ringing.</td><td><b>…when the phone rang.</b></td><td>short action = past simple.</td></tr>
<tr><td>The hare was sleep under a tree.</td><td><b>The hare was sleeping…</b></td><td>was + verb-ing.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "4 min")}
{audiocard(["21.3"])}
{sub("A", "Listen and repeat. Notice the weak was /wəz/ and were /wər/ in sentences, and the strong forms in short answers.", "3 min", "21.3")}
<ol style="line-height:1.6">{"".join(f"<li>{s}</li>" for s in S213[2:])}</ol>
<div class="box" style="margin-top:1mm"><h4>WEAK AND STRONG</h4>In a sentence: <i>The hare <b>was</b> /wəz/ watching.</i> · <i>What <b>were</b> /wər/ you doing?</i><br>At the end of a short answer, say the strong form: <i>Yes, he <b>was</b> /wʌz/. · No, they <b>weren't</b>.</i></div>
{sub("B", "Your turn. Ask your teacher: What were you doing at… 7 a.m. / noon / 9 p.m. yesterday? Answer the same questions.", "1 min")}""",
    24, """<ol><li>4A: hum the rhythm: <i>the HARE was WATCHing</i>; <i>was</i> is almost invisible. Brazilians often stress every word.</li>
<li>4B: correct the form, not only the pronunciation: <i>I was having breakfast.</i></li></ol>""")

    # Page 6
    ag = [("was working", "work"), ("were picking up", "pick up"), ("saving", "save"), ("stopped", "stop"), ("had", "have"), ("asked", "ask"),
          ("were", "be"), ("were you doing", "you / do"), ("answered", "answer"), ("was playing", "play"), ("continued", "continue"), ("don't help", "not help")]
    o = [f"<sup>{i+1}</sup>" + A(w, "min-width:18mm") + f" ({v})" for i, (w, v) in enumerate(ag)]
    sn = [("dog", "bark"), ("bee", "buzz"), ("lion", "roar"), ("snake", "hiss"), ("mouse", "squeak"), ("horse", "neigh"), ("bear", "growl"), ("goat / sheep", "bleat")]
    snl = [f'<li value="{i+1}">a {a} → {A(w, "min-width:14mm")}</li>' for i, (a, w) in enumerate(sn)]
    b.page(f"""{sec(5, "Practice", "9 min")}
{audiocard(["21.2"])}
{sub("A", "Complete the fable with the past simple or past continuous. Then listen and check.", "5 min", "21.2")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('D', 30, 22)}<div class="msg" style="flex:1;max-width:none;font-size:9pt;line-height:1.75"><b>The Ants and the Grasshopper</b><br>
One fall, a family of ants {o[0]} in the sunshine. They {o[1]} food and {o[2]} it for the winter. A hungry grasshopper {o[3]} to talk to them. He {o[4]} a violin.
"Can I have something to eat, please?" {o[5]} the grasshopper. The ants {o[6]} surprised. "Why don't you have any food? What {o[7]} all last summer?"
The grasshopper {o[8]}, "I didn't have any time to look for food. I {o[9]} music all summer on my violin." The ants {o[10]} with their work. "We can't help you if you {o[11]} yourself."</div></div>
<p class="small" style="margin-top:1mm">What's the moral of this story? {A("Work today and be ready for the future. / You can't ask others to help you if you don't work.", "min-width:60mm")}</p>
{sub("B", "Word builder: animal sounds. Match the animals and the verbs. Say them aloud!", "4 min")}
<div class="bank">bark · bleat · buzz · growl · hiss · neigh · roar · squeak</div>
{twocol(snl, 4)}
<p class="small">Which verbs sound like the animal? How do you say these sounds in your language?</p>""",
    22, """<ol><li>A: read the whole text first, without writing. 3: <i>saving</i> (were picking up and saving). 12: present simple in a conditional (Unit 13). <i>Fall</i> = autumn in American English.</li>
<li>B: <i>neigh</i> = /neɪ/ (like <i>nay</i>). <i>Buzz</i> and <i>hiss</i> sound most like the animals.</li></ol>""")

    # Page 7
    lion = ("A lion <b>was sleeping</b> in the forest. A little mouse <b>was running</b> around, and by mistake she ran across the lion's nose and woke him up. The lion was angry and wanted to kill her. "
            "\"Please don't kill me!\" said the mouse. \"If you let me go, one day I'll help you.\" The lion laughed, but he let her go. A few days later, the lion <b>was hunting</b> when he got caught in a hunter's <b>trap</b>, a big <b>net</b>. "
            "He roared and roared. The mouse heard him and ran to help. She <b>cut</b> the net with her teeth, and soon the lion was free. \"You laughed at me,\" said the mouse. \"But a little mouse helped a big lion!\"")
    goat = ("<b>The Fox and the Goat</b> (teacher only): A fox was walking by a farm when he fell into a well (a deep hole with water). He tried to get out, but it was too deep. He was calling for help when a goat heard him. "
            "The goat thought the fox was drinking the water. \"Is that good water?\" he asked. \"The best in the country!\" said the fox. \"Jump in and try it!\" The goat jumped in and started to drink. "
            "The fox quickly jumped onto the goat's back and climbed out. The goat was angry and asked the fox to help him out too, but the fox was already far away.")
    b.page(f"""{sec(6, "Speaking: tell a fable", "12 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><p style="flex:1;margin:0">You and your teacher each have a different fable. Read yours, prepare, and tell it from your notes. Then listen to your teacher's fable.</p>{img('F', 26, 18)}{img('B', 26, 18)}</div>
{sub("A", "Read your fable: The Lion and the Mouse.", "3 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.55">{lion}</div>
<p class="small" style="margin:.5mm 0"><b>Glossary:</b> a <b>trap</b> = something people use to catch animals · a <b>net</b> = a material with holes, used to catch fish or animals</p>
{sub("B", "Write 8–10 key words to help you remember the story. Close the text and tell it to your teacher. Use the past continuous and the past simple.", "5 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Listen to your teacher's fable: The Fox and the Goat. Choose the best moral.", "4 min")}
<ol><li>Don't help other people when they're in trouble.</li><li>Don't ask other people for help.</li><li>Look carefully at a new situation before you do something. {R("✓")}</li></ol>
<p class="small">{R(goat)}</p>""",
    26, """<ol><li>B: when the student tells the lion story, ask for its moral: <i>If you are kind to someone, they will be kind to you.</i> Note mistakes for feedback at the end.</li>
<li>C: read the red text slowly, with the past continuous in <i>was walking, was calling, was drinking</i>. Teach <b>well</b> first.</li></ol>""")

    # Page 8
    pc = [("A2 Unit 17", "I can make phone calls, take a message and leave a voicemail."), ("A2 Unit 18", "I can agree and disagree with so, neither, me too and me neither."),
          ("A2 Unit 19", "I can tell the story of someone's life with the past simple."), ("A2 Unit 21", "I can tell a story with the past continuous and the past simple.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["was", "were"], "were", "Two friends", "traveling together. They"), (["were walking", "walked"], "were walking", "", "through the forest when they"),
          (["were seeing", "saw"], "saw", "", "a bear. One man quickly"), (["was climbing", "climbed"], "climbed", "", "up a tree. The other man"),
          (["didn't have", "wasn't having"], "didn't have", "", "time, so he lay down on the ground and pretended to be dead. The bear smelled his face and ears, and then it left. The first man came down and asked, \"What did the bear say to you while it"),
          (["smelled", "was smelling"], "was smelling", "", "your ears?\" \"It said: a real friend doesn't leave you alone when you're in danger!\"")]
    hwt = " ".join(f"{a} {ch(o, r)} {m}" for o, r, a, m in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. The Travelers and the Bear.</b> Choose the correct verb forms. What's the moral?</p>
<div class="msg" style="max-width:none;font-size:9pt;line-height:1.75">{hwt}</div>
<p class="small">Moral: {A("In a dangerous situation, you find out who your real friends are.", "min-width:70mm")}</p>
<p style="margin-top:2mm"><b>2. A true story (60–80 words).</b> Write about something surprising that happened to you. Start with the scene: <i>It was a sunny Saturday. I was walking in the park when…</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>1: <i>lay</i> is the past of <i>lie</i> (lie down). More fables: the Library of Congress has <i>The Aesop for Children</i> free online, with the 1919 pictures. Next class: the student reads the true story aloud; ask <i>What were you doing when…?</i></p>""")

    b.extra("Audio script", f"""
{sub("21.1", "Story time: The Tortoise and the Hare (slow and natural)")}
<p style="line-height:1.42">{"<br>".join(S211)}</p>
{sub("21.2", "The Ants and the Grasshopper")}
<p style="line-height:1.42">{"<br>".join(S212)}</p>
{sub("21.3", "Weak was and were")}
<p>{" · ".join(S213)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 21 - Fables")
