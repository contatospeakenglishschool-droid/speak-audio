# Speak! Bridge A2 - Unit 02 "Passwords" (all English) - built with the shared engine
import sys, os, json
for _d in ("/home/claude/speak-audio/engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "speak-audio", "engine"),
           os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")):
    if os.path.exists(os.path.join(_d, "speak_engine.py")):
        sys.path.insert(0, _d); break
import speak_engine as _se
from speak_engine import *
import grammar_ref
_se.SERIES = "Bridge"
setup(band="A2 · UNIT 02", audio_json="audio_a2-unit-02.json", img_dir="img")

_r = json.load(open("roteiro.json"))["units"]["a2-unit-02"]
S022 = [x.split(": ", 1)[1] for x in _r["02.2 Repeat words"].split("\n")]
S023 = [x.split(": ", 1)[1] for x in _r["02.3 Repeat sentences"].split("\n")]
S021 = [x.split(": ", 1)[1] for x in _r["02.1 Article"].split("\n")]

ARTICLE = [
    ("", "For years, companies told us to create complex passwords full of numbers and symbols, and to change them every few months. Today, security experts in the United States give different advice."),
    ("1. Longer is better", "The Cybersecurity and Infrastructure Security Agency (CISA) <b>recommends</b> using passwords of at least 16 characters. A passphrase of five to seven random words, like <i>pizza river lamp yellow tiger</i>, is easy to remember but very difficult to hack."),
    ("2. Change the default password", "Experts <b>warn</b> people not to keep the default password on a new phone, computer or router. Attackers often know these passwords."),
    ("3. One password for each account", "You should <b>avoid</b> using the same password on different websites. If attackers hack one account, they can try the same password everywhere."),
    ("4. Don't write it down", "Many people write their passwords on paper or in a document on their computer. Experts say we should <b>stop</b> doing this, because other people can find them easily."),
    ("5. Fewer rules", "NIST, another government agency, says companies shouldn't force people to change their passwords on a schedule. They should <b>allow</b> people to use long, simple passphrases."),
    ("6. Let software help", "If you don't <b>want</b> to lose your accounts, <b>consider</b> using a password manager. It's software that creates and remembers strong passwords for you. Computers don't <b>mind</b> remembering hundreds of long passwords. That's what they're designed to do! And if you <b>need</b> to protect important accounts, turn on multifactor authentication, like a code by text message or your fingerprint."),
]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: one big photo + vocabulary (abstract topic)
    cover = cover_html(T, "LEVEL A2 · UNIT 02", "Passwords", "Online security · <b>verb + to, verb + -ing, verb + object + to</b>",
                       [("YOU CAN", "read a news article and talk about online security habits"),
                        ("LANGUAGE", "Avoid using the same password. · I want you to help me. · They warned us not to click."),
                        ("PRONUNCIATION", "seCURity · TECHnology · SOFTware · deFAULT / DEfault")])
    wv = [("This password is easy to guess. It's", "weak"), ("This password is difficult to guess. It's", "strong"), ("This password isn't simple. It's", "complex"),
          ("You get this password with a new phone or computer. It's the ___ password.", "default"), ("People need to keep the information on their computers safe. They need good", "security"),
          ("Attackers ___ computers to find private information.", "hack"), ("The information ___ (IT) department helps a company with its computers.", "technology"),
          ("A computer program that tells the computer what to do is", "software")]
    def wl(s, w):
        return s.replace("___", A(w, "min-width:18mm")) if "___" in s else f"{s} {A(w, 'min-width:18mm')}."
    wvl = [f'<li value="{i+1}">{wl(s, w)}</li>' for i, (s, w) in enumerate(wv)]
    src = photo("A")
    b.page(f"""{sec(1, "Warm-up: online security", "8 min")}
<div style="display:flex;gap:4mm;align-items:flex-start">
<div style="width:58mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{src}" style="width:58mm;height:44mm;object-fit:cover;display:block"></div>
<div style="flex:1">{sub("A", "Complete the sentences with the words in the box.", "5 min")}
<div class="bank">complex · default · hack · security · software · strong · technology · weak</div></div></div>
{twocol(wvl, 5)}
{sub("B", "Talk about it.", "3 min")}
<ol><li>Do you ever forget your passwords? What do you do?</li><li>How many passwords do you use every day?</li></ol>""",
    22, """<ol><li>A: <b>complex</b> can be stressed on either syllable. <b>default</b>: Americans often say <i>DEfault</i>. <b>hack</b> is a verb; <b>a hacker / an attacker</b> is the person.</li>
<li>B: don't ask the student to tell you any real password!</li></ol>""", cover=cover)

    b.extra("Lesson overview · 55 min", """
<table><tr><th>Stage</th><th>Time</th><th>Aim</th><th>SB page</th></tr>
<tr><td>1 Warm-up</td><td>8 min</td><td>Online security vocabulary</td><td>1</td></tr>
<tr><td>2 Reading</td><td>10 min</td><td>A news article: "Is your password strong enough?" (with audio)</td><td>2</td></tr>
<tr><td>3 Language focus</td><td>10 min</td><td>Verbs from the article · verb + to / verb + -ing / verb + object + to</td><td>3</td></tr>
<tr><td>+ Grammar reference</td><td>–</td><td>Verb + to, verb + -ing, verb + person + to</td><td>4</td></tr>
<tr><td>4 Pronunciation lab</td><td>5 min</td><td>Word stress in tech words · verb patterns in sentences</td><td>5</td></tr>
<tr><td>5 Practice</td><td>8 min</td><td>Make sentences · Word builder: internet verbs</td><td>6</td></tr>
<tr><td>6 Speaking</td><td>12 min</td><td>Guess the verb · your online habits</td><td>7</td></tr>
<tr><td>7 Wrap-up</td><td>2 min</td><td>Progress check and homework (50–75 words)</td><td>8</td></tr></table>
<div class="box"><h4>HOW THIS GUIDE WORKS</h4>Every page looks like the Student Book page with the same number. Your notes are in the <b>yellow box</b>; <span class="red">answers in red</span> are not in the Student Book. This is the first Speak! Bridge reading: the article is original, and the audio (track 02.1) lets the student read and listen.</div>
<div class="box sand"><h4>THE STORY CONTINUES</h4>Last week someone hacked the email account of Kate's bakery in Chicago. Her brother Tom sends her an article from an American tech news website about strong passwords. Facts in the article come from CISA (Cybersecurity and Infrastructure Security Agency, cisa.gov, "Use Strong Passwords": at least 16 characters, or a passphrase of 5–7 random words; a different password for each account; a password manager; multifactor authentication) and NIST (National Institute of Standards and Technology, Digital Identity Guidelines SP 800-63B: no forced password changes on a schedule; allow long passphrases).</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>Portuguese uses <i>que</i> + a clause where English uses an object + to: <i>I want that you help me</i> ✗ → <b>I want you to help me</b>. Students also use <i>to</i> after verbs that need <i>-ing</i>: <i>avoid to use, enjoy to cook</i> ✗ → <b>avoid using, enjoy cooking</b>; and <i>suggest me to</i> ✗ → <b>suggest + -ing</b>.</div>
<div class="box"><h4>AUDIO</h4>Track 02.1 The article (slow and natural) · Track 02.2 Tech words · Track 02.3 Sentences</div>""")

    # Page 2: reading with audio
    tf = [("Complex passwords are always better than long passwords.", "F: longer is better (at least 16 characters)."), ("You should change the default password on a new phone.", "T"),
          ("It's a good idea to use one password for all your websites.", "F: one password for each account."), ("You should keep your passwords in a document on your computer.", "F: stop doing this."),
          ("Companies should make people change their passwords every month.", "F: no changes on a schedule."), ("A password manager remembers your passwords for you.", "T")]
    tfl = [f'<li value="{i+1}">{s} <b>T / F</b> {R(a)}</li>' for i, (s, a) in enumerate(tf)]
    art = "".join(f"<p style='margin:0 0 1.4mm'>{('<b style=\"color:#0f4a5a\">' + h + '</b><br>') if h else ''}{t}</p>" for h, t in ARTICLE)
    b.page(f"""{sec(2, "Reading: is your password strong enough?", "10 min")}
<p>Somebody hacked the email account of Kate's bakery last week. Her brother Tom sends her this article from an American tech news website.</p>
{sub("A", "Before you read, guess: true (T) or false (F)? Then read and listen to check.", "4 min", "02.1 · NATURAL")}
{twocol(tfl, 4)}
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
<div style="border:1pt solid #c9dfe3;border-radius:2mm;padding:2.5mm 4mm;margin-top:1mm">
<div style="font-size:7pt;font-weight:800;letter-spacing:.14em;color:#7d858a">TECH TODAY · CHICAGO</div>
<div style="font-size:14pt;font-weight:800;color:#0f4a5a;margin:.5mm 0 1.5mm">Is your password strong enough?</div>
<div style="column-count:2;column-gap:6mm;font-size:8.9pt;line-height:1.42">{art}</div></div>""",
    20, """<p>A: the student guesses first, then reads while listening (slow version first if needed). Ask where in the text each answer is. Explain <b>a passphrase</b> (several words together) and <b>multifactor authentication</b> (a password + a code or your fingerprint). The article is original; facts from CISA and NIST (see the story box).</p>""")

    # Page 3
    mean = [("give advice about the best thing to do", "recommend"), ("tell people about a danger", "warn"), ("try not to do something", "avoid"),
            ("not continue an activity", "stop"), ("say that people can do something", "allow"), ("think about doing something", "consider"),
            ("not have a problem with something", "mind"), ("feel that something is necessary", "need")]
    ml = [f'<li value="{i+1}">{m} {A(v, "min-width:20mm")}</li>' for i, (m, v) in enumerate(mean)]
    b.page(f"""{sec(3, "Language focus: verb patterns", "10 min")}
{sub("A", "Find the verbs in bold in the article for these meanings. One bold verb is extra.", "3 min")}
{twocol(ml, 5)}
<p class="small">The extra verb: {R("want")}</p>
{sub("B", "Read the sentences. Then choose the correct option.", "3 min")}
<div class="bank" style="background:#fff;font-weight:600">You should <u>avoid using</u> the same password. · We should <u>stop doing</u> this. · If you don't <u>want to lose</u> your accounts… · Experts <u>warn people not to keep</u> the default password.</div>
<ol><li>After <i>avoid</i> and <i>stop</i>, we use {ch(["verb + -ing", "to + verb"], "verb + -ing")}.</li>
<li>After <i>want</i> and <i>need</i>, we use {ch(["verb + -ing", "to + verb"], "to + verb")}.</li>
<li>After <i>warn</i> and <i>allow</i>, we use {ch(["to + verb directly", "a person + to + verb"], "a person + to + verb")}.</li></ol>
{sub("C", "Complete the table with the verbs from the article.", "4 min")}
<table style="table-layout:fixed;font-size:9pt"><tr><th>verb + to</th><th>verb + -ing</th><th>verb + person + to</th></tr>
<tr><td>{A("want, need", "min-width:30mm")}<br><span class="small">agree, decide, hope, learn, plan, promise, refuse, would like</span></td>
<td>{A("recommend, avoid, stop, consider, mind", "min-width:40mm")}<br><span class="small">dislike, enjoy, finish, give up, practice, suggest, can't stand</span></td>
<td>{A("warn, allow", "min-width:24mm")}<br><span class="small">ask, tell, want (I want you to…)</span></td></tr></table>
<div class="box sand"><h4>BOTH ARE OK</h4><b>like, love, hate, prefer</b> + to or -ing: I like to cook / I like cooking. · Negative with an object: They warned us <b>not to</b> click the link.</div>""",
    24, """<ol><li>A: <i>want</i> is the extra verb. Check the meanings with real examples from the student's life.</li>
<li>C: <i>dislike</i> is only + -ing. <i>stop + -ing</i> = not continue; <i>stop to + verb</i> = stop in order to do something (He stopped to buy coffee) — mention it only if the student asks.</li></ol>""")

    # Grammar reference (before Common mistakes)
    grammar_ref.verb_patterns(b)

    # Page 4
    b.page(f"""{sub("D", "Common mistakes for Brazilians", "2 min")}
<div class="box sand"><h4>WATCH OUT: COMMON MISTAKES</h4>
<table style="margin:0"><tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>
<tr><td>I want that you help me.</td><td><b>I want you to help me.</b></td><td>want + person + to.</td></tr>
<tr><td>Avoid to use the same password.</td><td><b>Avoid using the same password.</b></td><td>avoid + -ing.</td></tr>
<tr><td>I enjoy to cook on Sundays.</td><td><b>I enjoy cooking on Sundays.</b></td><td>enjoy + -ing.</td></tr>
<tr><td>She suggested me to change it.</td><td><b>She suggested changing it.</b></td><td>suggest + -ing.</td></tr>
<tr><td>They allowed me use my phone.</td><td><b>They allowed me to use my phone.</b></td><td>allow + person + to.</td></tr>
<tr><td>I need change my password.</td><td><b>I need to change my password.</b></td><td>need + to.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Pronunciation lab", "5 min")}
{audiocard(["02.2", "02.3"])}
{sub("A", "Tech words. Listen and repeat. Underline the stressed syllable.", "2 min", "02.2")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join(f"<td style='text-align:center'><b>{w}</b></td>" for w in S022)}</tr></table>
<p class="small">{R("COMplex · DEfault · hack · seCUrity · SOFTware · strong · techNOLogy · weak")}</p>
{sub("B", "Sentences. Listen and repeat.", "2 min", "02.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S023)}</div>
<div class="box" style="margin-top:1mm"><h4>WEAK TO</h4>In <b>want to</b>, <b>need to</b>, <b>warn us not to</b>, the word <i>to</i> is short: /tə/. <i>want to</i> often sounds like <i>wanna</i> in fast speech.</div>""",
    24, """<ol><li>4A: Brazilians often say <i>TECHnology</i>: it's tech<b>NOL</b>ogy. <i>security</i> = se<b>CU</b>rity.</li>
<li>4B: the stress is on the main verbs: <i>a<b>VOID</b> <b>US</b>ing</i>.</li></ol>""")

    # Page 5
    ms = [("The boys / dislike / wash / the car.", "The boys dislike washing the car."), ("My dog / can't stand / have / a bath.", "My dog can't stand having a bath."),
          ("We / hope / visit / New York / next year.", "We hope to visit New York next year."), ("I / not mind / wait / for you / after class.", "I don't mind waiting for you after class."),
          ("She / need / practice / her pronunciation.", "She needs to practice her pronunciation."), ("They / promise / help me / last week.", "They promised to help me last week."),
          ("The teacher / tell / the students / speak English.", "The teacher told the students to speak English."), ("The police / warn / us / not go / there / yesterday.", "The police warned us not to go there yesterday.")]
    msl = [f'<li value="{i+1}"><i>{p}</i><div class="wline">{R(s)}</div></li>' for i, (p, s) in enumerate(ms)]
    wb = [("log in", "enter your username and password"), ("sign up", "create a new account"), ("update", "install a new version of an app"),
          ("download", "copy a file from the internet to your device"), ("log out", "close your account on a device")]
    wbl = "".join(f"<li>{A(w, 'min-width:18mm')} = {d}</li>" for w, d in wb)
    b.page(f"""{sec(5, "Practice", "8 min")}
{sub("A", "Make sentences. Change the verb forms and tenses when necessary.", "5 min")}
{twocol(msl, 5)}
{sub("B", "Word builder: the internet. Complete with the verbs in the box.", "3 min")}
<div class="bank">download · log in · log out · sign up · update</div>
<ol>{wbl}</ol>""",
    22, """<p>A: the student writes full sentences; then cover them and rebuild them orally from the prompts. B: more words in the bonus lesson <i>The internet</i> (Vocabulary to Go). Ask: <i>Do you always log out on public computers?</i></p>""")

    # Page 6
    b.page(f"""{sec(6, "Speaking", "12 min")}
{sub("A", "Guess the verb. Write six true phrases about you in the boxes, but don't write the first verb. Use verbs from page 3. Your teacher guesses the verb.", "7 min")}
<table style="table-layout:fixed;margin-top:0"><tr>{"".join("<td style='height:16mm;vertical-align:bottom'><span class='small' style='color:#9aa'>…</span></td>" for _ in range(3))}</tr><tr>{"".join("<td style='height:16mm;vertical-align:bottom'><span class='small' style='color:#9aa'>…</span></td>" for _ in range(3))}</tr></table>
<div class="msg" style="max-width:none;padding:2mm 4mm;line-height:1.55"><b>You wrote:</b> "watching movies in English"<br><b>Teacher:</b> Do you enjoy watching movies in English?<br><b>You:</b> No, try again! <b>Teacher:</b> Do you practice watching…? / Do you hope to…? <b>You:</b> I'm planning to start!</div>
{sub("B", "Your online life.", "5 min")}
<ol><li>Do you use the same password for different websites? (You don't need to say it!)</li><li>Did a website or bank ever ask you to change your password? Why?</li>
<li>Would you consider using a password manager? Why / why not?</li><li>What do you avoid doing online?</li></ol>""",
    26, """<ol><li>A: the student writes phrases like <i>to travel alone / cooking for friends / me to call my mother</i>. You guess the first verb with a full question; the student answers <i>Yes / No, try again</i>. Then change roles: you write and the student guesses.</li>
<li>B: correct the verb patterns, especially <i>avoid / consider + -ing</i>.</li></ol>""")

    # Page 7
    pc = [("A1 Unit 33", "I can make predictions with will / won't."), ("A1 Unit 34", "I can give advice with should, could and imperatives."),
          ("A1 Unit 35", "I can explain rules with must, mustn't, can and can't."), ("A2 Unit 01", "I can ask about appearance, personality, likes and wishes."),
          ("A2 Unit 02", "I can use verb + to, verb + -ing and verb + person + to.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [(["to come", "coming"], "to come", "My parents never allowed me", "home after midnight."), (["to sell", "selling"], "selling", "They considered", "their old car."),
          (["to spend", "spending"], "spending", "Most people enjoy", "time with their families."), (["to clean", "cleaning"], "cleaning", "When will you finish", "the kitchen?"),
          (["to ride", "riding"], "to ride", "I'm learning", "a horse."), (["to visit", "visiting"], "visiting", "My father suggested", "the museum.")]
    hl = "".join(f"<li>{a} {ch(o, r)} {c}</li>" for o, r, a, c in hw)
    b.page(f"""{sec(7, "Wrap-up and homework", "2 min")}
{sub("A", "Progress check", "1 min")}
<table class="ck"><tr><th style="width:22mm"></th><th>In English…</th><th style="width:18mm">Easy!</th><th style="width:18mm">Sometimes</th><th style="width:18mm">Not yet</th></tr>{pcr}</table>
{sub("B", "Homework", "1 min")}
<p><b>1. Choose the correct form.</b></p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. A message to Kate (50–75 words).</b> Kate's account was hacked. Write her a message with advice. Use at least four verbs from page 3 (recommend, avoid, stop, consider, need, want…).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Next class: start with homework 2 and check every verb pattern. Ask: <i>Which tip from the article are you going to follow?</i></p>""")

    b.extra("Audio scripts", f"""
{sub("02.1", "The article (slow and natural)")}
<p style="line-height:1.45">{"<br>".join(S021)}</p>
{sub("02.2", "Tech words")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "Sentences")}
<p>{" ".join(S023)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Bridge 02 - Passwords")
