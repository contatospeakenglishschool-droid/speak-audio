# Speak! grammar reference pages (extra SB/TB page at the end of a unit): page(b) adds the page to a Book.

_TIMELINE = """<svg viewBox="0 0 520 70" width="100%" height="17mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="38" x2="500" y2="38" stroke="#77acb5" stroke-width="2"/>
<polygon points="500,38 490,33 490,43" fill="#77acb5"/>
<text x="20" y="62" font-size="11" fill="#7d858a">PAST</text><text x="440" y="62" font-size="11" fill="#7d858a">NOW</text>
<line x1="450" y1="22" x2="450" y2="54" stroke="#176074" stroke-width="2"/>
<circle cx="230" cy="38" r="7" fill="#176074"/><text x="200" y="18" font-size="11" fill="#176074" font-weight="700">action / experience</text>
<path d="M237 32 Q340 0 446 30" fill="none" stroke="#cbbca0" stroke-width="2.5" stroke-dasharray="5 4"/>
<text x="300" y="62" font-size="11" fill="#9a7b4f" font-weight="700">connection to now</text></svg>"""


def present_perfect(b):
    """One-page reference for the present perfect at A2 (units 07-09)."""
    b.page(f"""{b.sec("+", "Grammar reference: the present perfect", "")}
<div class="box" style="margin-top:0"><h4>WHAT IS IT?</h4>The present perfect is a <b>bridge between the past and now</b>. Something happened in the past, but we are thinking about it <b>now</b>: the result is important now, or it's part of our life experience. We don't say <i>when</i> it happened.
{_TIMELINE}</div>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">1. FORM: have / has + past participle</h4>
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><th style="width:24mm"></th><th>I / you / we / they</th><th>he / she / it</th></tr>
<tr><td><b>positive</b></td><td>I <b>have</b> (I<b>'ve</b>) cut my finger.</td><td>She <b>has</b> (she<b>'s</b>) cut her finger.</td></tr>
<tr><td><b>negative</b></td><td>I <b>haven't</b> been to Florida.</td><td>He <b>hasn't</b> been to Florida.</td></tr>
<tr><td><b>question</b></td><td><b>Have</b> you ever ridden a horse?</td><td><b>Has</b> she ever ridden a horse?</td></tr>
<tr><td><b>short answers</b></td><td>Yes, I <b>have</b>. / No, I <b>haven't</b>.</td><td>Yes, she <b>has</b>. / No, she <b>hasn't</b>.</td></tr></table>
<p class="small" style="margin:.8mm 0"><b>Past participle:</b> regular verbs = <b>-ed</b>, like the past (climb → climbed → climbed). Irregular verbs have a third form: go → went → <b>gone</b> · see → saw → <b>seen</b> · do → did → <b>done</b> · break → broke → <b>broken</b>. Learn the three forms together!</p>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">2. TWO USES AT THIS LEVEL</h4>
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>A. Recent news with a result now</b> (Unit 07)<br>with <b>just</b> = a short time ago<br><i>I've just cut my finger.</i> (it's bleeding now)<br><i>She's just fallen off her bike.</i><br><i>What's happened?</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>B. Life experiences</b> (Unit 08)<br>with <b>ever</b> (questions), <b>never</b>, <b>before</b>, <b>twice</b>, <b>many times</b><br><i>Have you ever swum with manatees?</i><br><i>I've never camped. I've been to Orlando twice.</i></div></div>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">3. PRESENT PERFECT OR PAST SIMPLE?</h4>
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><th>present perfect: no finished time</th><th>past simple: a finished time</th></tr>
<tr><td>ever · never · just · before · twice · many times</td><td>yesterday · last year · in 2023 · two days ago · when I was twenty</td></tr>
<tr><td><i>I've ridden a horse.</i> (sometime in my life)</td><td><i>I rode a horse in Minas last summer.</i> (when? last summer)</td></tr></table>
<p class="small" style="margin:.8mm 0">A typical conversation <b>starts</b> with the present perfect and <b>continues</b> with the past simple: <i>Have you ever been to New York? — Yes, I have. — When did you go? — I went in 2022. It was amazing!</i></p>
<div class="two"><div class="box sand" style="margin-top:1mm"><h4>BEEN OR GONE?</h4><i>Carol has <b>been</b> to Miami.</i> (she went and came back)<br><i>Carol has <b>gone</b> to Miami.</i> (she's in Miami now)</div>
<div class="box sand" style="margin-top:1mm"><h4>DON'T SAY</h4><s>I have been in Florida last year.</s> → I <b>went</b> to Florida last year.<br><s>Have you ever went…?</s> → been · <s>Yes, I did.</s> → Yes, I <b>have</b>.</div></div>""",
    16, """<p>Use this page whenever the student hesitates between the present perfect and the past simple. Draw the timeline: the dot is the action, the dotted line connects it to now. The next units add more uses (<i>for / since, already / yet</i>). In American English the past simple is common with <i>just</i> (<i>I just ate</i>); both are correct.</p>""")


_TIMELINE2 = """<svg viewBox="0 0 520 70" width="100%" height="17mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="38" x2="500" y2="38" stroke="#77acb5" stroke-width="2"/>
<polygon points="500,38 490,33 490,43" fill="#77acb5"/>
<text x="20" y="62" font-size="11" fill="#7d858a">PAST</text><text x="440" y="62" font-size="11" fill="#7d858a">NOW</text>
<line x1="450" y1="22" x2="450" y2="54" stroke="#176074" stroke-width="2"/>
<rect x="150" y="31" width="300" height="14" rx="3" fill="#cbbca0" opacity=".75"/>
<line x1="150" y1="20" x2="150" y2="54" stroke="#9a7b4f" stroke-width="2"/>
<text x="112" y="16" font-size="11" fill="#9a7b4f" font-weight="700">since 2015 (start)</text>
<text x="230" y="16" font-size="11" fill="#176074" font-weight="700">for eleven years (length) →</text>
<text x="168" y="62" font-size="11" fill="#9a7b4f">I've lived in Seattle… and I still live there</text></svg>"""


def present_perfect_for_since(b):
    """One-page reference: present perfect for unfinished situations + for / since + How long, with a recap of the three uses."""
    b.page(f"""{b.sec("+", "Grammar reference: present perfect with for and since", "")}
<div class="box" style="margin-top:0"><h4>A NEW USE: SITUATIONS THAT ARE NOT FINISHED</h4>We use the present perfect for something that <b>started in the past and is still true now</b>. Portuguese uses the present here, but English uses the present perfect.
{_TIMELINE2}</div>
<div class="two"><div><table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><th>finished (past simple)</th><th>not finished (present perfect)</th></tr>
<tr><td>I <b>lived</b> in Chicago for five years. (I don't live there now.)</td><td>I<b>'ve lived</b> in Seattle for eleven years. (I live there now.)</td></tr>
<tr><td>She <b>worked</b> at a bank. (not now)</td><td>She<b>'s worked</b> at the hospital since 2015. (still there)</td></tr></table></div>
<div><table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><th>for + a length of time</th><th>since + the start</th></tr>
<tr><td>for ten minutes · for two days · for six months · for eleven years · for ages · for a long time</td><td>since 9 o'clock · since Tuesday · since March · since 2015 · since I was a child · since college</td></tr></table></div></div>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">QUESTIONS AND ANSWERS</h4>
<table style="table-layout:fixed;margin-top:0;font-size:8.8pt"><tr><td><b>How long have you</b> lived here? — I've lived here <b>for</b> three years. / <b>since</b> 2023.</td><td><b>How long has she</b> had her dog? — She's had him <b>for</b> two years.</td></tr>
<tr><td><b>How long have you known</b> Megan? — I've known her <b>since</b> college.</td><td>I <b>haven't seen</b> you <b>for</b> ages! (negative = the time without it)</td></tr></table>
<p class="small" style="margin:.8mm 0">State verbs (be, have, know, live, work) are very common in this use: <i>We've been married for eight years. I've known her since 2010.</i></p>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">THE PRESENT PERFECT SO FAR: THREE USES</h4>
<table style="table-layout:fixed;margin-top:0;font-size:8.6pt"><tr><th>use</th><th>key words</th><th>example</th></tr>
<tr><td>A. recent news, result now (Unit 07)</td><td>just</td><td>I've just cut my finger.</td></tr>
<tr><td>B. life experiences (Unit 08)</td><td>ever · never · before · twice</td><td>Have you ever swum with manatees?</td></tr>
<tr><td>C. not finished: started in the past, true now (Unit 09)</td><td>for · since · How long…?</td><td>I've lived in Seattle for eleven years.</td></tr></table>
<div class="box sand" style="margin-top:1.5mm"><h4>DON'T SAY</h4><s>I live here since 2015.</s> → I<b>'ve lived</b> here since 2015. · <s>I know her for ten years.</s> → I<b>'ve known</b> her for ten years. · <s>since ten years</s> → <b>for</b> ten years · <s>for 2020</s> → <b>since</b> 2020 · <s>How long do you live here?</s> → How long <b>have you lived</b> here?</div>""",
    16, """<p>The most common Brazilian mistake: <i>I live here since…</i>. Draw the bar: it starts at <b>since</b>; its length is <b>for</b>. Convert: <i>since 2015 → for eleven years</i>.</p>""")


def present_perfect_already_yet(b):
    """One-page reference: already, yet, still (and just) with the present perfect, plus a recap of the four uses."""
    b.page(f"""{b.sec("+", "Grammar reference: already, yet, still and just", "")}
<div class="box" style="margin-top:0"><h4>WHAT ARE THEY FOR?</h4>When we check a list of things to do (a party, a trip, work), we use the present perfect with <b>already</b>, <b>yet</b>, <b>still</b> and <b>just</b>. They tell us if something is <b>done</b> or <b>not done</b>, and how we feel about it.</div>
<table style="table-layout:fixed;margin-top:1mm;font-size:8.8pt"><tr><th style="width:22mm">word</th><th>meaning</th><th>sentence type</th><th>position</th><th>example</th></tr>
<tr><td><b>already</b></td><td>done, maybe sooner than expected</td><td>positive (and surprised questions)</td><td>between <i>have</i> and the participle</td><td>We've <b>already</b> ordered the pizzas.</td></tr>
<tr><td><b>yet</b></td><td>not done, but we expect it</td><td>questions and negatives</td><td>at the end</td><td>Have you made the cake <b>yet</b>? · The pizzas haven't arrived <b>yet</b>.</td></tr>
<tr><td><b>still</b></td><td>not done, and it's a problem / a surprise</td><td>negatives</td><td>before <i>haven't / hasn't</i></td><td>I <b>still</b> haven't made the cake!</td></tr>
<tr><td><b>just</b></td><td>done a very short time ago</td><td>positive</td><td>between <i>have</i> and the participle</td><td>I've <b>just</b> cleaned the tables.</td></tr></table>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">A TYPICAL CHECKLIST CONVERSATION</h4>
<div class="msg" style="max-width:none;padding:1.5mm 4mm;font-size:8.8pt;line-height:1.5"><b>A:</b> Have you invited the guests <b>yet</b>? <b>B:</b> Yes, I've <b>already</b> invited them. I sent the messages last week.<br><b>A:</b> And the cake? <b>B:</b> No, I haven't made it <b>yet</b>. / Oh no, I <b>still</b> haven't made it! <b>A:</b> Don't worry. I've <b>just</b> bought the eggs.</div>
<p class="small" style="margin:.8mm 0">Remember: with a finished time, use the past simple: <i>I invited them <b>two weeks ago</b>.</i> In American English you will also hear the past simple with these words (<i>Did you eat yet? I already ate.</i>); both are correct, but learn the present perfect first.</p>
<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">THE PRESENT PERFECT: FOUR USES</h4>
<table style="table-layout:fixed;margin-top:0;font-size:8.6pt"><tr><th>use</th><th>key words</th><th>example</th></tr>
<tr><td>A. recent news, result now (Unit 07)</td><td>just</td><td>I've just cut my finger.</td></tr>
<tr><td>B. life experiences (Unit 08)</td><td>ever · never · before</td><td>Have you ever swum with manatees?</td></tr>
<tr><td>C. not finished, true now (Unit 09)</td><td>for · since · How long…?</td><td>I've lived here for eleven years.</td></tr>
<tr><td>D. checking what's done (Unit 11)</td><td>already · yet · still</td><td>Have you bought the present yet?</td></tr></table>
<div class="box sand" style="margin-top:1.5mm"><h4>DON'T SAY</h4><s>I haven't yet finished.</s> → I haven't finished <b>yet</b>. · <s>I already have done it.</s> → I'<b>ve already done</b> it. · <s>I still not have called.</s> → I <b>still haven't</b> called. · <s>Have you made it still?</s> → … <b>yet</b>? · <s>I've already sent it last week.</s> → I <b>sent</b> it last week.</div>""",
    16, """<p>Make a real checklist with the student (their week, a trip, a party) and ask <i>Have you… yet?</i> The student answers with <i>already / not… yet / still haven't</i>. Correct the word position first; meaning comes easily.</p>""")


# ---------- shared helpers for the A2 reference pages ----------
def _h(t):
    return f'<h4 style="color:#0f4a5a;margin:1.5mm 0 .5mm">{t}</h4>'


def _tbl(head, rows, size="8.8pt"):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table style="table-layout:fixed;margin-top:0;font-size:{size}"><tr>{th}</tr>{tr}</table>'


def _dont(items):
    return '<div class="box sand" style="margin-top:1.5mm"><h4>DON\'T SAY</h4>' + " · ".join(f"<s>{a}</s> → {b}" for a, b in items) + "</div>"


def questions_with_like(b):
    """Unit 01: four questions with like."""
    b.page(f"""{b.sec("+", "Grammar reference: four questions with like", "")}
<div class="box" style="margin-top:0"><h4>ONE WORD, FOUR QUESTIONS</h4><b>Like</b> can be a <b>preposition</b> (= similar to) or a <b>verb</b> (= enjoy). That's why English has four different questions with <i>like</i>. Each one asks for different information.</div>
{_tbl(["question", "it asks about…", "answer"], [
    ["<b>What's he like?</b>", "personality / character (preposition <i>like</i>)", "He's friendly, calm and a little lazy."],
    ["<b>What does he look like?</b>", "appearance (look + like)", "He's tall, with short brown hair. / He looks like his dad."],
    ["<b>What does he like (doing)?</b>", "preferences, hobbies (verb <i>like</i>)", "He likes playing ball. / He likes pizza."],
    ["<b>Would he like…?</b>", "a wish or an offer (would like = want, polite)", "Yes, he would. / He'd like a nap!"]])}
{_h("FORM")}
{_tbl(["", "personality", "appearance", "likes", "wishes"], [
    ["he / she / it", "What's she like?", "What does she look like?", "What does she like doing?", "Would she like a coffee?"],
    ["I / you / we / they", "What are they like?", "What do they look like?", "What do they like doing?", "Would you like to come?"]], "8.4pt")}
<p class="small" style="margin:.8mm 0">In the first two questions, <i>like</i> is a preposition, so it never changes: <i>What does she look <b>like</b>?</i> (not <i>likes</i>). After the verb <i>like</i>: <b>-ing</b> or <b>to</b> (<i>He likes playing / to play</i>). After <i>would like</i>: <b>to</b> + verb or a noun (<i>I'd like to go / I'd like a coffee</i>).</p>
{_h("DESCRIBING PEOPLE AND ANIMALS")}
{_tbl(["personality", "appearance", "colors and patterns"], [["friendly · calm · lazy · playful · shy · sociable · funny", "tall · short · slim · big · curly / straight hair · beard", "light / dark / bright / pale + color · spotted · striped · shiny"]])}
<div class="box" style="margin-top:1.5mm"><h4>SHORT ANSWERS</h4><i>Would you like a coffee?</i> → <b>Yes, I would. / Yes, please.</b> (not <i>Yes, I like</i>) · <i>Do you like coffee?</i> → <b>Yes, I do.</b></div>
{_dont([("How is he? (personality)", "<b>What's he like?</b>"), ("What does she looks like?", "What does she <b>look</b> like?"), ("He likes play.", "He likes <b>playing</b> / <b>to play</b>."), ("Would you like? — Yes, I like.", "<b>Yes, I would.</b>"), ("brown hairs", "brown <b>hair</b>")])}""",
    16, """<p><i>How is he?</i> asks about health. Practice the four questions with a real person or pet the student knows: you ask all four, then the student asks you.</p>""")


def verb_patterns(b):
    """Unit 02: verb + to, verb + -ing, verb + person + to."""
    b.page(f"""{b.sec("+", "Grammar reference: verb patterns", "")}
<div class="box" style="margin-top:0"><h4>WHAT COMES AFTER THE VERB?</h4>When two verbs are together, the <b>first verb</b> decides the form of the second: <b>to + verb</b>, <b>verb + -ing</b>, or <b>a person + to + verb</b>. There is no easy rule: learn the verb with its pattern, like a phrase.</div>
{_tbl(["verb + to", "verb + -ing", "verb + person + to"], [
    ["agree · decide · hope · learn · need · plan · promise · refuse · want · would like", "avoid · consider · dislike · don't mind · enjoy · finish · give up · keep · practice · recommend · stop · suggest · can't stand", "advise · allow · ask · invite · remind · teach · tell · want · warn"],
    ["<i>I need <b>to change</b> my password.</i>", "<i>Avoid <b>using</b> the same password.</i>", "<i>They warned <b>us to be</b> careful.</i>"]])}
{_h("BOTH ARE POSSIBLE")}
<p class="small" style="margin:.5mm 0"><b>like · love · hate · prefer · start · begin</b> + to or -ing, same meaning: <i>I like to cook / I like cooking.</i></p>
{_h("NEGATIVES AND PREPOSITIONS")}
{_tbl(["form", "example"], [
    ["verb + <b>not to</b>", "<i>Experts warn people <b>not to keep</b> the default password.</i>"],
    ["preposition + <b>-ing</b>", "<i>I'm interested <b>in learning</b>. Thanks <b>for helping</b>.</i>"],
    ["make / let + person + verb (no to)", "<i>My boss <b>let me leave</b> early. It <b>made me laugh</b>.</i>"]])}
<div class="box" style="margin-top:1.5mm"><h4>CAREFUL: SAME VERB, DIFFERENT MEANING</h4><b>stop + -ing</b> = not continue: <i>He stopped smoking.</i> · <b>stop + to</b> = stop in order to do something: <i>He stopped to buy coffee.</i><br><b>remember / forget + to</b> = a future duty: <i>Remember to call Mom!</i> · <b>remember + -ing</b> = a past memory: <i>I remember meeting her.</i></div>
{_dont([("I want that you help me.", "I want <b>you to help</b> me."), ("Avoid to use…", "Avoid <b>using</b>…"), ("I enjoy to cook.", "I enjoy <b>cooking</b>."), ("She suggested me to go.", "She suggested <b>going</b>."), ("I need change it.", "I need <b>to change</b> it.")])}""",
    16, """<p>Students should write new verbs in their notebook with the pattern: <i>avoid + -ing, want + (person) + to</i>. Quick drill: you say a verb, the student makes a true sentence.</p>""")


def action_state_verbs(b):
    """Unit 03: action and state verbs, sense verbs, simple vs continuous."""
    b.page(f"""{b.sec("+", "Grammar reference: action verbs and state verbs", "")}
<div class="box" style="margin-top:0"><h4>TWO KINDS OF VERBS</h4><b>Action verbs</b> describe things we <b>do</b> (walk, look at, touch): they can be continuous. <b>State verbs</b> describe things that just <b>are</b>: feelings, thoughts, senses, possession (love, know, hear, have). They are <b>not usually continuous</b>.</div>
{_tbl(["action verbs (simple or continuous)", "state verbs (usually simple)"], [
    ["walk · run · listen to · look at · touch · smell (a leaf) · taste (the soup) · take · talk", "<b>feelings:</b> love · like · hate · want · need · prefer<br><b>thinking:</b> know · understand · believe · remember · think (= opinion)<br><b>senses:</b> see · hear · smell / taste / feel / look / sound + adjective<br><b>possession:</b> have (= own) · belong"],
    ["<i>Right now we<b>'re walking</b> in the park.</i>", "<i>I <b>love</b> this place. I <b>hear</b> birds. I <b>understand</b>.</i>"]])}
{_h("SENSE VERBS: ACTION OR DESCRIPTION?")}
{_tbl(["action (continuous possible)", "description (simple + adjective)"], [
    ["I'm looking at the tree.", "It <b>looks</b> enormous."], ["I'm smelling the leaf.", "It <b>smells</b> fresh."],
    ["I'm tasting the soup.", "It <b>tastes</b> delicious."], ["I'm touching the bark.", "It <b>feels</b> rough."], ["I'm listening to the music.", "It <b>sounds</b> beautiful. · I <b>hear</b> it."]])}
<p class="small" style="margin:.8mm 0">After a sense verb, use an <b>adjective</b>, not an adverb: <i>It smells <b>good</b></i> (not <i>well</i>). With a noun, use <b>like</b>: <i>It smells <b>like</b> rain. She looks <b>like</b> her mother.</i></p>
{_h("PRESENT SIMPLE OR CONTINUOUS? (ACTION VERBS)")}
{_tbl(["present simple: routines, always true", "present continuous: now, around now"], [["<i>He <b>takes</b> visitors to the park every Saturday.</i>", "<i>Today we<b>'re walking</b> slowly.</i>"]])}
<div class="box" style="margin-top:1.5mm"><h4>TWO MEANINGS</h4><b>think</b>: <i>I think it's beautiful</i> (opinion) · <i>What are you thinking about?</i> (action). <b>have</b>: <i>She has a dog</i> (own) · <i>We're having lunch</i> (action: eat).</div>
{_dont([("I'm hearing a noise.", "I <b>hear</b> / <b>can hear</b> a noise."), ("The soup is tasting good.", "The soup <b>tastes</b> good."), ("It smells well.", "It smells <b>good</b>."), ("I'm understanding.", "I <b>understand</b>."), ("I feel the smell of coffee.", "I <b>can smell</b> coffee.")])}""",
    16, """<p>Test: can you say it with "right now, I am…" and it's something you choose to do? Then it's an action. Bring real objects (a lemon, a mug of coffee) and practice both forms.</p>""")


def word_prepositions(b):
    """Unit 04: adjective + preposition, noun + preposition."""
    b.page(f"""{b.sec("+", "Grammar reference: words + prepositions", "")}
<div class="box" style="margin-top:0"><h4>FIXED PAIRS</h4>Many adjectives and nouns are followed by a <b>fixed preposition</b>. The preposition is often different from Portuguese, so learn the word and the preposition together, like one phrase. After the preposition: a <b>noun</b>, a <b>pronoun</b> or <b>verb + -ing</b>.</div>
{_tbl(["adjective + preposition", "example"], [
    ["afraid <b>of</b> · scared <b>of</b> · tired <b>of</b> · proud <b>of</b>", "<i>I'm afraid of losing my phone.</i>"],
    ["worried <b>about</b> · excited <b>about</b> · happy <b>about</b>", "<i>She's worried about the test.</i>"],
    ["interested <b>in</b> · good <b>at</b> · bad <b>at</b>", "<i>He's interested in art. I'm good at cooking.</i>"],
    ["familiar <b>with</b> · bored <b>with</b> · in contact <b>with</b>", "<i>Are you familiar with this app?</i>"],
    ["responsible <b>for</b> · famous <b>for</b> · married <b>to</b> · different <b>from</b>", "<i>Who's responsible for the money?</i>"]])}
{_tbl(["noun + preposition", "example"], [
    ["the fear <b>of</b> · a photo <b>of</b>", "<i>the fear of being without your phone</i>"],
    ["an increase <b>in</b> · interest <b>in</b>", "<i>an increase in online shopping</i>"],
    ["a reason <b>for</b> · a need <b>for</b>", "<i>the reasons for the problem</i>"],
    ["a solution <b>to</b> · an answer <b>to</b>", "<i>a solution to the problem</i>"],
    ["separation <b>from</b> · a message <b>from</b>", "<i>separation from your phone</i>"]])}
{_h("VERBS + PREPOSITIONS (USEFUL TOO)")}
<p class="small" style="margin:.5mm 0">depend <b>on</b> · listen <b>to</b> · wait <b>for</b> · look <b>for</b> · think <b>about</b> · talk <b>to</b> someone <b>about</b> something · belong <b>to</b></p>
<div class="box" style="margin-top:1.5mm"><h4>STUDY TIP</h4>Make a diagram: one circle for each preposition (<b>of</b>, <b>about</b>, <b>in</b>, <b>with</b>, <b>for</b>, <b>to</b>), and write the words inside. Add new words when you find them in a text.</div>
{_dont([("worried with", "worried <b>about</b>"), ("married with", "married <b>to</b>"), ("different of", "different <b>from</b>"), ("good in", "good <b>at</b>"), ("depend of", "depend <b>on</b>"), ("tired of wait", "tired of <b>waiting</b>")])}""",
    16, """<p>Quick game: you say the word, the student says the preposition and a true sentence (<i>proud… of: I'm proud of my son</i>). Correct the Portuguese-style prepositions immediately.</p>""")


def parts_of_speech(b):
    """Unit 05: parts of speech, word families, classroom questions."""
    b.page(f"""{b.sec("+", "Grammar reference: parts of speech and word families", "")}
<div class="box" style="margin-top:0"><h4>WHY IT MATTERS</h4>Knowing the <b>part of speech</b> of a word tells you <b>where it goes</b> in a sentence and <b>how it changes</b>. A good dictionary always shows it: <b>humid</b> <i>adj.</i>, <b>humidity</b> <i>n.</i></div>
{_tbl(["part of speech", "job", "examples", "what to learn"], [
    ["<b>noun</b> <i>n.</i>", "a person, thing, place, idea", "cousin, receipt, beach, humidity", "countable or uncountable? plural?"],
    ["<b>verb</b> <i>v.</i>", "an action or a state", "spell, mean, go, know", "regular or irregular? (go – went – gone)"],
    ["<b>adjective</b> <i>adj.</i>", "describes a noun", "humid, terrible, silent", "comparative? (hotter, more humid)"],
    ["<b>adverb</b> <i>adv.</i>", "describes a verb or adjective", "slowly, really, always", "how? how often? position"],
    ["<b>pronoun</b> <i>pron.</i>", "replaces a noun", "she, her, it, them", "subject or object?"],
    ["<b>preposition</b> <i>prep.</i>", "connects a word to a noun", "at, on, from, next to", "time or place?"]], "8.5pt")}
{_h("WORD FAMILIES: USEFUL ENDINGS")}
{_tbl(["change", "endings", "examples"], [
    ["adjective → noun", "-ity · -ness", "humid → humidity · electric → electricity · happy → happiness"],
    ["verb → noun", "-tion · -sion · -ment", "inform → information · decide → decision · pronounce → pronunciation · move → movement"],
    ["adjective → adverb", "-ly", "careful → carefully · easy → easily (good → <b>well</b>!)"]], "8.4pt")}
{_h("CLASSROOM QUESTIONS")}
{_tbl(["you want to know…", "ask"], [
    ["a word / the meaning", "<b>How do you say</b> this in English? · <b>What does</b> humid <b>mean</b>?"], ["if it's correct / the part of speech", "<b>Can we say</b> this? · <b>What kind of word is it?</b>"],
    ["spelling, pronunciation, names", "<b>How do you spell / pronounce</b> it? · <b>What do you call</b> this?"]], "8.4pt")}
{_dont([("How do you call this?", "<b>What do you call</b> this?"), ("What means humid?", "What <b>does</b> humid <b>mean</b>?"), ("How you spell it?", "How <b>do you</b> spell it?"), ("I have a doubt.", "I have a <b>question</b>.")])}""",
    16, """<p>Encourage the student to write every new word with its part of speech and one example. Use the classroom questions in every class: don't answer questions asked in Portuguese structure; ask the student to rephrase.</p>""")


def being_nice(b):
    """Unit 06: functional language: praising, complimenting, congratulating."""
    b.page(f"""{b.sec("+", "Language reference: being nice in English", "")}
<div class="box" style="margin-top:0"><h4>FUNCTIONS</h4>Some phrases do a <b>job</b> in a conversation. The fixed part never changes; you only change the adjective or noun. Say them with <b>energy</b>: a flat <i>Well done</i> can sound sarcastic.</div>
{_tbl(["function", "when?", "phrases"], [
    ["<b>praising</b>", "someone's work, actions or choices", "Well done! · Good job! · Great work! · Keep up the good work! · I know you're good at… · I really like the… you chose."],
    ["<b>complimenting</b>", "how someone looks or what they have", "You look great today! · That color really suits you. · What a beautiful dress! · I love your… · Where did you get it?"],
    ["<b>congratulating</b>", "good news, achievements", "Congratulations on your new job! · Glad to hear it! · Good luck! · That's wonderful news!"]], "8.6pt")}
{_h("PATTERNS")}
{_tbl(["pattern", "example"], [
    ["What a + adjective + singular noun!", "<i>What a cute baby! What a nice boss!</i>"],
    ["What + adjective + plural / uncountable noun!", "<i>What beautiful eyes! What great hair!</i>"],
    ["Congratulations on + noun / -ing", "<i>Congratulations on the baby / on passing the test!</i>"],
    ], "8.4pt")}
{_h("RESPONDING POLITELY")}
{_tbl(["response", "use it to…"], [
    ["Thanks! · You're too kind.", "accept praise or a compliment"], ["It was a team effort.", "share the praise (modest)"],
    ["You too! · I'm glad you like it.", "return it / react to their feelings"], ["Actually, my sister gave it to me.", "explain where you got something"]], "8.4pt")}
{_dont([("Congratulations! (birthday)", "<b>Happy birthday!</b>"), ("Congratulations for…", "Congratulations <b>on</b>…"), ("That dress suits to you.", "That dress <b>suits you</b>."), ("You made a great job.", "You <b>did</b> a great job."), ("You're too much kind.", "You're <b>too kind</b>."), ("What a beautiful!", "What a beautiful <b>dress</b>!")])}""",
    16, """<p>Brazilians often reject compliments ("Oh, this old thing?"). In English, accepting with <i>Thanks!</i> is polite. Practice: compliment the student on something real and wait for a natural response.</p>""")


def friendly_emails(b):
    """Unit 12: informal email structure, phrases, informal vs formal."""
    b.page(f"""{b.sec("+", "Language reference: writing a friendly email", "")}
<div class="box" style="margin-top:0"><h4>SEVEN PARTS, ALWAYS IN THIS ORDER</h4>A friendly email to a friend, a cousin or a colleague you know well is <b>informal</b>: first names, contractions (<i>I'm, it's</i>) and set phrases. The set phrases must be exact: one small mistake changes the impression.</div>
{_tbl(["part", "job", "phrases"], [
    ["1 greeting", "say hello (first name + comma)", "Hi Paulo, · Hello Paulo, · Dear Paulo,"],
    ["2 opening", "connect with the last contact", "It's great to hear from you! · I hope you're doing well. · Thanks a lot for writing! · I'm sorry to hear that…"],
    ["3 reason for writing", "the main point (most important)", "I'm writing to tell you that… · I just wanted to ask you… · I wanted to let you know that…"],
    ["4 details / news", "plans, suggestions, news", "We could… · How about…? · Did I tell you that…? · Guess what?"],
    ["5 call to action", "what the reader should do next", "Let me know what you think. · Call me later. · Send me the details. · Tell me what you'd like to do."],
    ["6 closing", "finish the email", "Anyway, I have to go now. · I'm looking forward to seeing you. · I hope to hear from you soon."],
    ["7 sign-off", "say goodbye + your first name", "Love, Carol (family, close friends) · Take care, · Best wishes, · Cheers,"]], "8.4pt")}
{_h("INFORMAL OR FORMAL?")}
{_tbl(["", "friendly email", "formal email"], [
    ["greeting", "Hi Paulo,", "Dear Mr. Silva, / Dear Ms. Clark, (last name!)"],
    ["style", "contractions: I'm, it's, don't", "full forms: I am, it is, do not"],
    ["closing", "I'm looking forward to seeing you!", "I look forward to hearing from you."],
    ["sign-off", "Love, / Take care, / Cheers,", "Best regards, / Sincerely, + full name"]], "8.4pt")}
<p class="small" style="margin:.8mm 0"><b>Punctuation:</b> a comma after the greeting and the sign-off; start the first sentence with a capital letter. <b>looking forward to + -ing</b> (to is a preposition): <i>looking forward to <b>seeing</b> you</i>.</p>
{_dont([("Dear Mr. Paulo,", "Dear Paulo, / Dear Mr. Silva,"), ("Hello to David,", "Hello David,"), ("I'm writing to say about…", "I'm writing to <b>tell you about</b>…"), ("Waiting for your answer.", "I'm looking forward to hearing from you."), ("Kisses, / Att.", "Love, / Best regards,"), ("looking forward to see you", "looking forward to <b>seeing</b> you")])}""",
    16, """<p>Many Brazilians translate their Portuguese email habits (the abbreviation for "regards", "kisses", "waiting for your answer"). Show the seven parts as a checklist: the student checks their own email part by part before sending it.</p>""")
