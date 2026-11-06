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


def zero_first_conditional(b):
    """Unit 13: zero and first conditionals (cause and effect, facts and predictions)."""
    b.page(f"""{b.sec("+", "Grammar reference: zero and first conditionals", "")}
<div class="box" style="margin-top:0"><h4>CAUSE AND EFFECT</h4>Conditional sentences have <b>two clauses</b> (a clause = a subject + a verb): a <b>cause / condition</b> and an <b>effect / result</b>. The <b>zero conditional</b> talks about facts that are always true. The <b>first conditional</b> talks about a <b>possible future</b> and its result.</div>
{_tbl(["", "zero conditional", "first conditional"], [
    ["use", "facts, science, things that always happen", "predictions: a real possibility in the future"],
    ["form", "<b>When / If</b> + present simple, present simple", "<b>If</b> + present simple, <b>will / won't</b> + verb"],
    ["examples", "<i>When ice <b>melts</b>, sea levels <b>rise</b>.</i><br><i>If you <b>heat</b> water to 100 °C, it <b>boils</b>.</i>", "<i>If we <b>protect</b> forests, the trees <b>will help</b> us.</i><br><i>If it <b>rains</b> tomorrow, I<b>'ll stay</b> home.</i>"]])}
{_h("CLAUSE ORDER AND COMMAS")}
{_tbl(["condition first: use a comma", "result first: no comma"], [["<i>If we don't change<b>,</b> temperatures will keep rising.</i>", "<i>Temperatures will keep rising if we don't change.</i>"], ["<i>When you turn off the lights<b>,</b> you use less energy.</i>", "<i>You use less energy when you turn off the lights.</i>"]])}
{_h("WHEN OR IF?")}
<p class="small" style="margin:.5mm 0"><b>when</b> = it will happen / it always happens: <i>When I get home, I'll call you.</i> · <b>if</b> = maybe it happens: <i>If I get the job, I'll call you.</i> Also <b>as</b> (= when, while something changes): <i>As the Earth gets hotter, storms get stronger.</i></p>
{_h("NEGATIVES AND QUESTIONS")}
{_tbl(["form", "example"], [
    ["if + don't / doesn't", "<i>If we <b>don't stop</b> burning coal, the problem <b>will get</b> worse.</i>"],
    ["won't in the result", "<i>If you take the bus, you <b>won't need</b> to park.</i>"],
    ["questions", "<i>What <b>will happen</b> if sea levels rise? · <b>Will</b> you come if it rains?</i>"],
    ["unless (= if not)", "<i>Things won't change <b>unless</b> we act.</i>"]])}
<div class="box" style="margin-top:1.5mm"><h4>NO WILL IN THE IF CLAUSE</h4>The <b>if</b> part uses the present simple even when we talk about the future: <i>If it <b>rains</b> tomorrow…</i> (not <i>If it will rain</i>).</div>
{_dont([("If it will rain, I'll stay home.", "If it <b>rains</b>, I'll stay home."), ("If we protect forests, the trees help us tomorrow.", "… the trees <b>will help</b> us."), ("When ice melt, sea levels rises.", "When ice <b>melts</b>, sea levels <b>rise</b>."), ("If I will have time, I call you.", "If I <b>have</b> time, I<b>'ll call</b> you.")])}""",
    16, """<p>Portuguese uses a special future form after "if" and "when", so students put <i>will</i> in the if clause. Drill the "hump" intonation: the condition goes up, the result comes down.</p>""")


def conjunctions(b):
    """Unit 14: conjunctions that join two clauses (and, but, so, because, although, while, if) and commas."""
    b.page(f"""{b.sec("+", "Grammar reference: conjunctions and commas", "")}
<div class="box" style="margin-top:0"><h4>JOINING TWO IDEAS</h4>A <b>clause</b> is a part of a sentence with a <b>subject + verb</b>. A <b>conjunction</b> joins two clauses and shows the relationship between the ideas: <b>adding</b> information, <b>contrast</b> (a different idea), or <b>cause and effect</b> (reason and result).</div>
{_tbl(["relationship", "conjunctions", "examples"], [
    ["adding", "<b>and</b>", "<i>Solar power works in many places<b>, and</b> it's much cheaper now.</i>"],
    ["contrast", "<b>but · although · while</b>", "<i>Fossil fuels will run out<b>, but</b> the sun's energy won't.</i><br><i>Wind turbines are cheap to operate <b>although</b> they can be noisy.</i><br><i>Fossil fuels cause climate change <b>while</b> renewable energy is cleaner.</i>"],
    ["cause → effect", "<b>because</b> (cause) · <b>so</b> (result) · <b>if</b> (condition)", "<i>Heat pumps are reliable <b>because</b> they rarely break down.</i><br><i>Solar panels are cheaper now<b>, so</b> many people install them.</i><br><i><b>If</b> the rivers get low<b>,</b> there isn't enough water.</i>"]])}
{_h("BECAUSE OR SO?")}
<p class="small" style="margin:.5mm 0"><b>because</b> + the reason: <i>I take the bus <b>because</b> it's cheaper.</i> · <b>so</b> + the result: <i>The bus is cheaper<b>, so</b> I take it.</i> Use one or the other, never both in the same sentence.</p>
{_h("COMMAS: A SIMPLE GUIDE")}
{_tbl(["conjunction", "in the middle", "at the start"], [
    ["<b>and · but · so</b>", "comma before it (usual): <i>It's an old idea<b>, but</b> it's reliable.</i>", "not at the start of a sentence in writing"],
    ["<b>because · although · while · if</b>", "no comma: <i>We need a mix <b>because</b> every type has problems.</i>", "comma after the first clause: <i><b>Because</b> every type has problems<b>,</b> we need a mix.</i>"]])}
<p class="small" style="margin:.8mm 0"><b>One subject, two verbs = one clause, no comma:</b> <i>Solar panels don't work at night and take up a lot of space.</i> · <b>Two subjects = two clauses:</b> <i>Solar panels don't work at night<b>, and</b> they take up a lot of space.</i></p>
<div class="box" style="margin-top:1.5mm"><h4>EVERY CLAUSE NEEDS A SUBJECT</h4>In English, the second clause needs its own subject: <i>Although solar power works in most places, <b>it</b> takes up a lot of space.</i> (not <i>…, takes up a lot of space</i>)</div>
{_dont([("Because it's cheap, so I use it.", "<b>Because</b> it's cheap, I use it. / It's cheap, <b>so</b> I use it."), ("Although they're noisy, but they're cheap.", "<b>Although</b> they're noisy, they're cheap."), ("Hydropower is reliable, because is old.", "Hydropower is reliable because <b>it</b> is old."), ("I like wind turbines. Because they're beautiful.", "I like wind turbines <b>because</b> they're beautiful.")])}""",
    16, """<p>Portuguese often drops the subject and can use two connectors together (a cause word plus a result word, or a contrast word plus "but"), so students write <i>Because… so…</i> and <i>Although… but…</i>. Show the three relationships with colors on the board: green = adding, red = contrast, blue = cause and effect.</p>""")


def sequencers(b):
    """Unit 15: sequencing words (first, second, then, next, finally, last) and at first / but then / at last."""
    b.page(f"""{b.sec("+", "Grammar reference: first, then, at first, at last", "")}
<div class="box" style="margin-top:0"><h4>ORGANIZING WHAT YOU SAY</h4><b>Sequencers</b> put ideas in order. They help the listener follow a list, a story, a recipe or an opinion. We usually put them at the <b>start</b> of the sentence, with a <b>comma</b>.</div>
{_tbl(["position", "words", "examples"], [
    ["start", "<b>First, · Firstly,</b>", "<i><b>First,</b> there's no meat in any of the burgers.</i>"],
    ["middle", "<b>Second, · Secondly, · Then, · Next, · After that,</b>", "<i><b>Second,</b> the buns are made with cricket flour. <b>Then,</b> there are no potato fries.</i>"],
    ["end", "<b>Finally, · Lastly, · The last thing is…</b>", "<i><b>Finally,</b> the shake is made with oat milk.</i>"]])}
<p class="small" style="margin:.8mm 0"><b>first, second, third, last</b> can also go before a noun: <i>the <b>first</b> burger · the <b>third</b> thing we ordered · the <b>last</b> strange thing</i>. Don't use <i>firstly / secondly / thirdly</i> before a noun.</p>
{_h("A CHANGE OF FEELING: AT FIRST … BUT THEN …")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>at first</b> = in the beginning (my first feeling)<br><b>but then</b> = my feeling changed<br><i><b>At first,</b> you didn't want to try it, <b>but then</b> you tasted mine and loved it!</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>at last</b> = finally, after a long wait (happy!)<br><i><b>At last,</b> something different!</i><br><i>The pizza is here. <b>At last!</b></i></div></div>
{_tbl(["don't mix them up", "meaning", "example"], [
    ["<b>first</b> vs <b>at first</b>", "number 1 in a list · my feeling in the beginning", "<i>First, we ordered burgers.</i> · <i>At first, I didn't like it.</i>"],
    ["<b>finally / lastly</b> vs <b>at last</b>", "the last item · after a long wait", "<i>Finally, we had a shake.</i> · <i>We waited an hour. At last!</i>"],
    ["<b>then</b> vs <b>than</b>", "next (time) · in comparisons", "<i>Then we had fries.</i> · <i>The fries were better than the burger.</i>"]])}
{_h("DESCRIBING FOOD: MADE WITH / FROM / OF")}
<p class="small" style="margin:.5mm 0"><b>made with</b> + an ingredient: <i>The shake is made with oat milk.</i> · <b>made from</b> + what it was before: <i>The fries are made from sweet potatoes.</i> · <b>made of</b> + a material: <i>The bags are made of recycled paper.</i></p>
{_dont([("Firstly burger was dry.", "<b>The first</b> burger was dry. / <b>First,</b> the burger was dry."), ("At first, we ordered fries. Second, …", "<b>First,</b> we ordered fries."), ("We waited an hour. Finally!", "… <b>At last!</b>"), ("It's bigger then the other one.", "bigger <b>than</b>")])}""",
    16, """<p>Students mix up <i>first / at first</i> and <i>finally / at last</i>. Mime it: count on your fingers for <i>first, second, then</i>; an unhappy face that turns happy for <i>at first … but then</i>; look at your watch and sigh for <i>at last</i>.</p>""")


def defining_relative_clauses(b):
    """Unit 16: defining relative clauses with who, which, that, where; leaving out the object pronoun."""
    b.page(f"""{b.sec("+", "Grammar reference: who, which, that, where", "")}
<div class="box" style="margin-top:0"><h4>WHAT IS A RELATIVE CLAUSE?</h4>A <b>defining relative clause</b> gives information that we <b>need</b> to know which person, thing or place we mean. It starts with <b>who, which, that</b> or <b>where</b> and has a verb. We use it a lot to <b>define</b> or explain things: <i>A thrift store is a store <b>where you can buy second-hand clothes</b>.</i></div>
{_tbl(["pronoun", "for…", "examples"], [
    ["<b>who</b> (or <b>that</b>)", "people", "<i>Grace is a designer <b>who</b> makes jackets out of old jeans.</i>"],
    ["<b>that</b> (or <b>which</b>)", "things, animals", "<i>Denim is a material <b>that</b> lasts for years.</i> (<i>that</i> is more common in American English)"],
    ["<b>where</b>", "places (= in that place)", "<i>She has a studio <b>where</b> she makes bags.</i>"]])}
{_h("TWO SENTENCES → ONE")}
{_tbl(["two sentences", "one sentence"], [
    ["Grace is a designer. <s>She</s> makes jackets.", "Grace is a designer <b>who</b> makes jackets."],
    ["She uses materials. <s>The materials</s> don't damage the environment.", "She uses materials <b>that</b> don't damage the environment."],
    ["She has a studio in Chicago. She makes bags <s>there</s>.", "She has a studio in Chicago <b>where</b> she makes bags."]])}
<p class="small" style="margin:.8mm 0">The pronoun <b>replaces</b> a word: don't repeat it. <i>The jeans that people throw away <s>them</s></i>. No comma before a defining relative clause.</p>
{_h("WHEN CAN WE LEAVE OUT WHO / WHICH / THAT?")}
<div class="two"><div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>Subject: keep it</b> (a verb comes next)<br><i>Grace is a designer <b>who makes</b> jackets.</i><br><i>It's something <b>that keeps</b> you warm.</i></div>
<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:8.8pt"><b>Object: you can leave it out</b> (a person/subject comes next)<br><i>the clothes (<b>that</b>) <b>we</b> don't wear</i><br><i>It's something (<b>that</b>) <b>you</b> wear on your feet.</i></div></div>
<div class="box" style="margin-top:1.5mm"><h4>DEFINITIONS GAME</h4><i>It's a person who… · It's something that / something you… · It's a place where…</i> → <i>It's a place where you buy clothes.</i> (a store)</div>
{_dont([("The dress that I bought it is small.", "The dress (that) I bought is small."), ("She's the designer which makes bags.", "… the designer <b>who</b> makes bags."), ("It's the store what I buy jeans.", "It's the store <b>where</b> I buy jeans."), ("A thrift store is a place that you can buy cheap clothes.", "… a place <b>where</b> you can buy…")])}""",
    16, """<p>Portuguese uses one word for all of these, so students say <i>the person which</i> or <i>the store what</i>, and they repeat the object (<i>the dress that I bought it</i>). Practice the definitions game: it uses all three pronouns naturally.</p>""")


def phone_calls(b):
    """Unit 17 (functional): phone call routines, informal and formal, phrasal verbs, voicemail, numbers."""
    b.page(f"""{b.sec("+", "Language reference: phone calls", "")}
<div class="box" style="margin-top:0"><h4>PHONE ROUTINES</h4>Phone calls follow the same steps every time. Choose the <b>style</b>: <b>informal</b> with friends and family, <b>formal</b> with businesses and people you don't know. Phrases with ↔ work in both.</div>
{_tbl(["step", "informal", "formal"], [
    ["answer the phone", "Hello? · Hi! · Tom's phone.", "Hello, Lakeview Hotel. Linda speaking. How can I help you?"],
    ["ask for someone", "Is Tom there?", "Could I speak to Mr. Bennett, please?"],
    ["say who you are", "It's Kate. · This is Kate.", "It's Kate Miller, from Sweet Kate Bakery. ↔"],
    ["ask who is calling", "Who's this?", "Who's calling, please?"],
    ["ask someone to wait", "Hang on a minute.", "Please hold on a moment."],
    ["connect the call", "I'll get him.", "I'll put you through."],
    ["the person isn't there", "Sorry, he can't come to the phone. · He isn't here.", "I'm afraid Mr. Bennett isn't available."],
    ["messages", "Can you tell him (that) I called? · I'll pass that on.", "I'd like to leave a message, please. · I'll make sure he gets the message."],
    ["check and repeat", "Did you get that? · Sorry, can you speak up?", "Would you like me to say that again? · Could you say that again, please?"]], "8.4pt")}
{_h("PHRASAL VERBS FOR PHONES")}
<p class="small" style="margin:.5mm 0"><b>pick up</b> = answer · <b>hang up</b> = end the call · <b>hang up on someone</b> = end the call angrily · <b>speak up</b> = speak more loudly · <b>break up</b> = your voice is on and off · <b>get through (to)</b> = make contact · <b>put through</b> = connect · <b>hang on / hold on</b> = wait · <b>call back</b> = call again later</p>
<div class="two"><div class="box" style="margin-top:1mm"><h4>A VOICEMAIL IN 5 STEPS</h4>1 <i>Hi, Tom! It's Paulo here.</i> 2 <i>I'm calling to tell you that…</i> 3 details (time, place, number) 4 <i>Can you text me to confirm?</i> 5 <i>See you later! / Talk soon!</i></div>
<div class="box" style="margin-top:1mm"><h4>SAYING NUMBERS</h4>Say phone and order numbers one digit at a time: <i>4-7-2-9-1</i> = four, seven, two, nine, one. 0 = <i>oh</i> or <i>zero</i>. Repeat the number to check.</div></div>
{_dont([("Who is speaking?", "Who's <b>calling</b>, please? / Who's this?"), ("I'm Kate. (on the phone)", "<b>It's</b> Kate. / <b>This is</b> Kate."), ("Wait a moment. (formal)", "Please <b>hold on</b> a moment."), ("Can you talk more high?", "Can you <b>speak up</b>?")])}""",
    16, """<p>Brazilian students translate the Portuguese question word for word as <i>Who is speaking?</i> and say <i>I'm Kate</i> on the phone; in English we say <i>It's Kate / This is Kate</i>. Practice the calls back to back, like a real call.</p>""")


def so_neither(b):
    """Unit 18: agreeing and disagreeing with so / neither + auxiliary, me too / me neither."""
    b.page(f"""{b.sec("+", "Grammar reference: so am I, neither do I", "")}
<div class="box" style="margin-top:0"><h4>SAYING YOU HAVE SOMETHING IN COMMON</h4>To agree, we <b>don't repeat the main verb</b>. We use <b>so</b> (after a positive sentence) or <b>neither</b> (after a negative sentence) + the <b>auxiliary</b> + the subject. Informal and easy: <b>Me too · Me neither</b>.</div>
{_tbl(["the first sentence", "agree: positive", "agree: negative"], [
    ["be (am / is / are)", "<i>I'm hungry.</i> → <b>So am I.</b>", "<i>I'm not tired.</i> → <b>Neither am I.</b>"],
    ["present simple", "<i>I like comedies.</i> → <b>So do I.</b><br><i>Tom likes pizza.</i> → <b>So does Paulo.</b>", "<i>I don't like fast food.</i> → <b>Neither do I.</b>"],
    ["past simple", "<i>I loved it.</i> → <b>So did I.</b>", "<i>I didn't like the movie.</i> → <b>Neither did I.</b>"],
    ["can / will / should", "<i>I can swim.</i> → <b>So can I.</b>", "<i>I won't go.</i> → <b>Neither will I.</b>"],
    ["present perfect", "<i>I've been to Miami.</i> → <b>So have I.</b>", "<i>I haven't tried it.</i> → <b>Neither have I.</b>"],
    ["any sentence (informal)", "<b>Me too.</b>", "<b>Me neither.</b>"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>Word order:</b> so / neither + <b>auxiliary + subject</b>: <i>So <b>do I</b></i> (not <s>So I do</s>) · <i>Neither <b>did Kate</b></i>. <b>Same tense</b> as the first sentence: <i>I went</i> → <i>So <b>did</b> I</i>.</p>
{_h("DISAGREEING")}
{_tbl(["the first sentence", "disagree", "polite"], [
    ["<i>I like that actor.</i>", "<b>I don't.</b>", "<i>Really? Sorry, but I don't.</i>"],
    ["<i>I'm not hungry.</i>", "<b>I am.</b>", "<i>Oh, I am!</i>"],
    ["<i>I haven't been to New York.</i>", "<b>I have.</b>", "<i>I have! It's amazing.</i>"],
    ["<i>I can't cook.</i>", "<b>I can.</b>", "<i>Really? I can.</i>"]])}
<div class="box" style="margin-top:1.5mm"><h4>NEITHER: TWO PRONUNCIATIONS</h4><b>neither</b> = /ˈniːðər/ (NEE-ther) or /ˈnaɪðər/ (NIGH-ther). Both are correct in American English. In very informal American English you'll also hear <i>Me either</i>.</div>
{_dont([("I don't like fast food. – Me too.", "<b>Me neither.</b> / <b>Neither do I.</b>"), ("I like pizza. – So I do.", "<b>So do I.</b>"), ("I'm hungry. – So do I.", "<b>So am I.</b> (be → am)"), ("I didn't go. – Neither I.", "<b>Neither did I.</b>")])}""",
    16, """<p>Portuguese has no auxiliary in short answers, so students say <i>Me too</i> after negative sentences. Quick drill: say true sentences about yourself; the student answers fast (<i>So do I · Neither am I · I don't</i>).</p>""")


def past_simple_review(b):
    """Unit 19: past simple review: regular -ed (spelling and three sounds), irregular verbs, did questions and negatives."""
    b.page(f"""{b.sec("+", "Grammar reference: the past simple (review)", "")}
<div class="box" style="margin-top:0"><h4>FINISHED ACTIONS IN THE PAST</h4>We use the past simple for finished actions and events, often with a <b>time reference</b>: <i>in 1956 · last year · two days ago · when she was 16 · after high school</i>. It's the tense of biographies and stories.</div>
{_tbl(["", "form", "examples"], [
    ["positive", "verb + <b>-ed</b> or irregular form (all persons)", "<i>Grace <b>moved</b> to New York. She <b>met</b> the prince in 1955.</i>"],
    ["negative", "<b>didn't</b> + base verb", "<i>She <b>didn't make</b> any more movies.</i> (not <s>didn't made</s>)"],
    ["question", "<b>Did</b> + subject + base verb", "<i><b>Did</b> she <b>win</b> an Oscar? When <b>did</b> they <b>get</b> married?</i>"],
    ["short answer", "Yes, … did. / No, … didn't.", "<i>Yes, she <b>did</b>. / No, she <b>didn't</b>.</i>"],
    ["be", "was / were · wasn't / weren't", "<i>Her family <b>was</b> rich. They <b>were</b> happy. <b>Was</b> she American?</i>"]], "8.6pt")}
{_h("REGULAR VERBS: SPELLING")}
<p class="small" style="margin:.5mm 0">most verbs + <b>-ed</b>: work → worked · ends in <b>-e</b> + <b>-d</b>: move → moved · consonant + <b>y</b> → <b>-ied</b>: study → studied (but play → played) · short verb, one vowel + one consonant → double: stop → stopped, plan → planned</p>
{_h("REGULAR VERBS: THREE SOUNDS")}
{_tbl(["/t/", "/d/", "/ɪd/ (an extra syllable)"], [
    ["after p, k, s, sh, ch, f: <i>helped, worked, announced, watched</i>", "after other sounds: <i>moved, followed, called, studied, married</i>", "only after <b>t</b> or <b>d</b>: <i>wanted, started, visited, decided</i>"]])}
{_h("COMMON IRREGULAR VERBS")}
<p class="small" style="margin:.5mm 0">be → was/were · become → became · begin → began · feel → felt · get → got · give → gave · go → went · have → had · make → made · meet → met · speak → spoke · take → took · win → won · write → wrote</p>
{_dont([("Did she won an Oscar?", "Did she <b>win</b>…?"), ("She didn't made movies.", "She didn't <b>make</b>…"), ("They work-ED together. (2 syllables)", "worked = one syllable /wɜːrkt/"), ("When they got married?", "When <b>did</b> they <b>get</b> married?")])}""",
    16, """<p>Brazilian students often pronounce every <i>-ed</i> as an extra syllable (<i>work-ed, watch-ed</i>). The extra syllable is only after <b>t</b> or <b>d</b>. In questions with <i>did</i>, the main verb goes back to the base form.</p>""")


_TIMELINE_PC = """<svg viewBox="0 0 520 64" width="100%" height="15mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="34" x2="500" y2="34" stroke="#77acb5" stroke-width="2"/>
<polygon points="500,34 490,29 490,39" fill="#77acb5"/>
<text x="20" y="58" font-size="11" fill="#7d858a">PAST</text><text x="460" y="58" font-size="11" fill="#7d858a">NOW</text>
<path d="M110 34 Q170 14 230 34 Q290 54 350 34" fill="none" stroke="#cbbca0" stroke-width="3" stroke-dasharray="6 4"/>
<text x="120" y="12" font-size="11" fill="#9a7b4f" font-weight="700">was sleeping (long action, in progress)</text>
<line x1="245" y1="20" x2="245" y2="48" stroke="#176074" stroke-width="3"/>
<text x="252" y="58" font-size="11" fill="#176074" font-weight="700">passed (short action)</text></svg>"""


def past_continuous(b):
    """Unit 21: past continuous, and past continuous + past simple (while / when)."""
    b.page(f"""{b.sec("+", "Grammar reference: the past continuous", "")}
<div class="box" style="margin-top:0"><h4>AN ACTION IN PROGRESS IN THE PAST</h4>The past continuous describes an action that was <b>in progress</b> at a moment in the past. It often sets the scene at the start of a story; the past simple tells the events, one after the other.
{_TIMELINE_PC}
<p class="small" style="margin:0"><i>While the hare <b>was sleeping</b>, the tortoise <b>passed</b> him.</i></p></div>
{_h("1. FORM: was / were + verb-ing")}
{_tbl(["", "I / he / she / it", "you / we / they"], [
    ["<b>positive</b>", "The hare <b>was watching</b> the tortoise.", "The ants <b>were working</b>."],
    ["<b>negative</b>", "He <b>wasn't listening</b>.", "They <b>weren't playing</b>."],
    ["<b>question</b>", "<b>Was</b> he <b>sleeping</b>?", "What <b>were</b> you <b>doing</b>?"],
    ["<b>short answers</b>", "Yes, he <b>was</b>. / No, he <b>wasn't</b>.", "Yes, they <b>were</b>. / No, they <b>weren't</b>."]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>-ing spelling:</b> work → working · take → taking (no <b>e</b>) · run → running, sit → sitting (double) · lie → lying</p>
{_h("2. PAST SIMPLE OR PAST CONTINUOUS?")}
{_tbl(["past simple: finished actions, events in order", "past continuous: a longer action in progress, the background"], [
    ["<i>The hare <b>looked</b> back. He <b>didn't see</b> the tortoise, so he <b>decided</b> to rest.</i>", "<i>One day, a hare <b>was watching</b> a tortoise. He <b>was laughing</b>.</i>"],
    ["<b>when</b> + short action: <i>I was cooking <b>when</b> the phone rang.</i>", "<b>while</b> + long action: <i><b>While</b> I was cooking, the phone rang.</i>"]], "8.6pt")}
{_h("3. STATE VERBS: NO -ING")}
<p class="small" style="margin:.5mm 0">Verbs for thoughts, feelings and senses don't usually take <b>-ing</b>: <b>know, think</b> (= believe), <b>believe, want, like, love, see, hear, need</b>. <i>The hare <b>thought</b> it was funny.</i> (not <s>was thinking</s>) · <i>He <b>didn't see</b> the tortoise.</i> (not <s>wasn't seeing</s>)</p>
{_dont([("I was knowing the answer.", "I <b>knew</b> the answer."), ("I was cooking when the phone was ringing.", "…when the phone <b>rang</b>."), ("They was working.", "They <b>were</b> working."), ("What you were doing?", "What <b>were you</b> doing?")])}""",
    16, """<p>Draw the timeline: the wavy line is the long action, the short line is the event that interrupts it. In natural speech <i>was</i> and <i>were</i> are weak (/wəz/, /wər/), but strong in short answers: <i>Yes, I was.</i></p>""")


_TIMELINE_UT = """<svg viewBox="0 0 520 64" width="100%" height="15mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="20" y1="34" x2="500" y2="34" stroke="#77acb5" stroke-width="2"/>
<polygon points="500,34 490,29 490,39" fill="#77acb5"/>
<text x="20" y="58" font-size="11" fill="#7d858a">PAST</text><text x="460" y="58" font-size="11" fill="#7d858a">NOW</text>
<g fill="#cbbca0"><circle cx="70" cy="34" r="5"/><circle cx="110" cy="34" r="5"/><circle cx="150" cy="34" r="5"/><circle cx="190" cy="34" r="5"/><circle cx="230" cy="34" r="5"/><circle cx="270" cy="34" r="5"/></g>
<text x="60" y="14" font-size="11" fill="#9a7b4f" font-weight="700">used to watch TV every evening (a habit then)</text>
<line x1="320" y1="20" x2="320" y2="48" stroke="#176074" stroke-width="2" stroke-dasharray="3 3"/>
<text x="330" y="58" font-size="11" fill="#7d858a">Pepper arrives</text>
<text x="360" y="14" font-size="11" fill="#176074" font-weight="700">now: walks every day</text></svg>"""


def used_to(b):
    """A2 Unit 22: used to / didn't use to for past habits and states."""
    b.page(f"""{b.sec("+", "Grammar reference: used to", "")}
<div class="box" style="margin-top:0"><h4>THINGS THAT WERE TRUE BEFORE, BUT NOT NOW</h4><b>used to + verb</b> talks about <b>habits</b> (repeated actions) and <b>states</b> in the past that are different now. It is great for comparing <b>then</b> and <b>now</b>.
{_TIMELINE_UT}
<p class="small" style="margin:0"><i>I <b>used to watch</b> TV every evening. Now I go out for walks with Pepper.</i></p></div>
{_h("1. FORM: the same for all persons")}
{_tbl(["", "example", "remember"], [
    ["<b>positive</b>", "I / She / They <b>used to</b> work all day.", "<b>used</b> with <b>-d</b>"],
    ["<b>negative</b>", "I <b>didn't use to</b> know my neighbors.", "<b>didn't</b> + <b>use</b> (no -d)"],
    ["<b>yes/no question</b>", "<b>Did</b> you <b>use to</b> have a pet?", "<b>did</b> + <b>use</b> (no -d)"],
    ["<b>short answers</b>", "Yes, I <b>did</b>. / No, I <b>didn't</b>.", "not <s>Yes, I used.</s>"],
    ["<b>wh- question</b>", "What kind of dogs <b>did</b> she <b>use to</b> have?", "wh- + did + subject + use to"]], "8.6pt")}
{_h("2. HABITS AND STATES")}
{_tbl(["habits: repeated actions", "states: be, have, know, like, live, think"], [
    ["<i>She <b>used to</b> walk her dogs twice a day.</i>", "<i>I <b>used to</b> be so stressed.</i>"],
    ["<i>We <b>used to</b> go to the beach every summer.</i>", "<i>They <b>used to</b> have a cat.</i>"]], "8.6pt")}
{_h("3. USED TO OR PAST SIMPLE?")}
{_tbl(["used to: repeated or for a long time, and different now", "past simple: one time, or a fixed number of times"], [
    ["<i>I <b>used to</b> visit my grandmother on Sundays.</i>", "<i>I <b>visited</b> my grandmother last Sunday.</i>"],
    ["<i>He <b>used to</b> live in Recife.</i>", "<i>He <b>lived</b> in Recife for ten years.</i> (also OK)"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>Now = present simple + usually:</b> <i>I <b>usually</b> get up at six.</i> (not <s>I use to get up at six</s>). <b>used to</b> is only for the past.<br><b>Pronunciation:</b> <i>used to</i> = /ˈjuːstə/ (like <i>yoost-tuh</i>). <i>I <b>used</b> a map</i> (= utilized) = /juːzd/.</p>
{_dont([("I use to live in Recife.", "I <b>used</b> to live in Recife."), ("I didn't used to like coffee.", "I didn't <b>use</b> to like coffee."), ("I use to get up at six. (now)", "I <b>usually</b> get up at six."), ("I used to go to Paris last year.", "I <b>went</b> to Paris last year.")])}""",
    22, """<p>In Portuguese, one verb works for past and present habits, so Brazilians often use <i>use to</i> for the present too. Contrast: <i>I used to drink soda. Now I usually drink water.</i> In fast speech the <i>-d</i> of <i>used</i> disappears, which is why students write <i>use to</i> in positive sentences.</p>""")


def second_conditional(b):
    """A2 Unit 23: second conditional (unreal or unlikely present/future), compared with zero and first."""
    b.page(f"""{b.sec("+", "Grammar reference: the second conditional", "")}
<div class="box" style="margin-top:0"><h4>IMAGINING A DIFFERENT REALITY</h4>The <b>second conditional</b> talks about situations in the <b>present or future</b> that are <b>not real</b> or <b>not likely</b>. We use a past form after <b>if</b>, but the meaning is <b>not past</b>.<br>
<span class="small"><b>Reality:</b> <i>I don't have much free time, so I don't go to many games.</i> → <b>Imagined:</b> <i>If I <b>had</b> more free time, I<b>'d go</b> to every home game.</i></span></div>
{_h("1. FORM")}
{_tbl(["condition (if clause)", "result"], [
    ["<b>If</b> + past simple<br><i>If the tickets <b>were</b> cheaper,</i>", "<b>would / wouldn't</b> + verb<br><i>more families <b>would go</b>.</i>"],
    ["<i>If I <b>had</b> more money,</i>", "<i>I<b>'d buy</b> a season ticket.</i> ('d = would)"],
    ["<i>If they <b>didn't train</b>,</i>", "<i>they <b>wouldn't win</b>.</i>"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>Question:</b> <i>What <b>would</b> you <b>do</b> if you <b>won</b> the lottery?</i> · <b>Short answers:</b> <i>Yes, I <b>would</b>. / No, I <b>wouldn't</b>.</i><br>
<b>Order:</b> <i>If I had time, I'd go.</i> = <i>I'd go if I had time.</i> (comma only when <b>if</b> comes first)<br>
<b>be:</b> <i>If I / he / she / it <b>were</b>…</i> is correct in all English; <i>was</i> is common in conversation. Advice: <i>If I <b>were</b> you, I'd…</i></p>
{_h("2. ZERO, FIRST OR SECOND?")}
{_tbl(["", "form", "example", "meaning"], [
    ["<b>zero</b>", "if + present, present", "<i>If you heat ice, it melts.</i>", "always true"],
    ["<b>first</b>", "if + present, will", "<i>If we win on Sunday, we'll celebrate.</i>", "real, possible"],
    ["<b>second</b>", "if + past, would", "<i>If we won every game, it wouldn't be special.</i>", "imagined, unlikely"]], "8.4pt")}
{_h("3. FROM REALITY TO IMAGINATION")}
<p class="small" style="margin:.5mm 0">Change the tense and, very often, positive ↔ negative: <i>He <b>doesn't like</b> training, so he <b>isn't</b> fit.</i> → <i>If he <b>liked</b> training, he<b>'d be</b> fit.</i></p>
{_dont([("If I would have money, I would travel.", "If I <b>had</b> money, I'd travel."), ("If I had time, I will go.", "…I <b>would</b> go."), ("If I won, I travel the world.", "…I <b>would travel</b>…"), ("I would be happy if they would win.", "…if they <b>won</b>.")])}""",
    20, """<p>The key Brazilian error is <i>would</i> in the if clause. Use the hump intonation: rising on the condition, falling on the result. In speech, <i>I'd</i> /aɪd/ and <i>I'll</i> /aɪl/ are easy to confuse; drill both.</p>""")


def story_writing(b):
    """A2 Unit 24 (writing lesson): language reference for writing a story: four areas, direct speech, linkers, A2 checklist."""
    b.page(f"""{b.sec("+", "Language reference: writing a story", "")}
<div class="box" style="margin-top:0"><h4>WHAT MAKES A GOOD STORY?</h4>Teachers and exams (for example, Cambridge B1 Preliminary) look at <b>four areas</b>: <b>1. the task</b> (follow the instructions: first sentence, topic, number of words), <b>2. the reader</b> (keep them interested until the end), <b>3. organization</b> (a clear order and paragraphs) and <b>4. language</b> (a good range of grammar and vocabulary, few mistakes with easy language).</div>
{_h("1. DIRECT SPEECH: American punctuation")}
{_tbl(["rule", "example"], [
    ["double quotation marks \" \" around the exact words", "<i><b>\"</b>Don't go in there,<b>\"</b> he shouted.</i>"],
    ["the comma, ? or ! goes <b>inside</b> the quotation marks", "<i>\"It's too dangerous<b>,</b>\" he said. · \"Are you OK<b>?</b>\" she asked.</i>"],
    ["a new sentence inside the speech starts with a capital letter", "<i>\"Don't go in there,\" he shouted. \"<b>I</b>t's too dangerous.\"</i>"],
    ["reporting verbs make speech more alive", "<b>said · asked · shouted · whispered · laughed · answered · explained · cried</b>"]], "8.6pt")}
{_h("2. LINKERS FOR A STORY")}
{_tbl(["start / set the scene", "events in order", "surprise or change", "contrast and end"], [
    ["<i>Last Sunday, … · One morning, … · When I was a child, …</i>", "<i>First, … · Then, … · After that, … · Later, …</i>", "<i>Suddenly, … · At first, … but then … · To my surprise, …</i>", "<i>Although … · In the end, … · Finally, …</i>"]], "8.4pt")}
{_h("3. YOUR A2 CHECKLIST: show what you know")}
{_tbl(["language", "example", "unit"], [
    ["past continuous to set the scene", "<i>I <b>was playing</b> in a soccer game.</i>", "21"],
    ["past simple for the events", "<i>Pepper <b>ran</b> onto the field.</i>", "19"],
    ["used to for past habits", "<i>We <b>used to</b> practice every weekend.</i>", "22"],
    ["state verbs without -ing", "<i>She <b>knew</b> how to play.</i> (not <s>was knowing</s>)", "03"],
    ["relative clauses", "<i>students <b>who</b> go to a different college · the cave <b>where</b> the ball was</i>", "16"],
    ["conjunctions", "<i>and · but · so · although</i>", "14"],
    ["second conditional", "<i>If Pepper <b>weren't</b> a dog, we <b>would</b> count that goal!</i>", "23"]], "8.4pt")}
<p class="small" style="margin:.8mm 0"><b>Before you finish:</b> plan for one minute (10–12 key words) · use two or three paragraphs · count your words · check your verbs, punctuation and spelling.</p>
{_dont([("Don't go in there, he shouted.", "<b>\"</b>Don't go in there,<b>\"</b> he shouted."), ("\"It's dangerous\", he said.", "\"It's dangerous<b>,</b>\" he said."), ("Firstly, I thought she…", "<b>At first,</b> I thought she…"), ("Although we lost, but she was a hero.", "<b>Although</b> we lost, she was a hero.")])}""",
    16, """<p>A story doesn't need to be true; personal experience is a great starting point. <i>Firstly</i> lists points in an essay; <i>At first … but then</i> shows a change in a story.</p>""")


def ed_ing_adjectives(b):
    """A2 Unit 25: -ed and -ing adjectives (feelings vs things that cause them), be/get/feel, prepositions."""
    b.page(f"""{b.sec("+", "Grammar reference: -ed and -ing adjectives", "")}
<div class="box" style="margin-top:0"><h4>HOW I FEEL OR WHAT MAKES ME FEEL?</h4>Many adjectives come from verbs (<i>bore, interest, excite</i>) and have two forms.<br>
<b>-ed</b> = the <b>feeling</b> (usually a person): <i>I was <b>bored</b>.</i> · <b>-ing</b> = the <b>thing or person that causes</b> the feeling: <i>The show was <b>boring</b>.</i><br>
<span class="small">Careful: <i>I'm <b>boring</b></i> means other people feel bored with you!</span></div>
{_h("1. FORM AND VERBS")}
{_tbl(["", "-ed: feelings", "-ing: the cause"], [
    ["<b>verbs</b>", "<b>be</b> (a state) · <b>get</b> (a change) · <b>feel</b>: <i>I <b>got</b> annoyed after five minutes. I often <b>feel</b> shocked.</i>", "<b>be</b>, with subjects like <b>it, that, what</b> or a thing: <i><b>That</b> was surprising. <b>What</b>'s confusing is…</i>"],
    ["<b>spelling</b>", "bore → bored · worry → worried · shock → shocked", "bore → boring (no <b>e</b>) · surprise → surprising · confuse → confusing"],
    ["<b>pronunciation</b>", "/d/ amazed, bored · /t/ shocked, relaxed · /ɪd/ excited, interested", "-ing /ɪŋ/: don't add an extra sound: <i>boring</i>, not <i>boringue</i>"]], "8.6pt")}
{_h("2. -ED ADJECTIVE + PREPOSITION")}
{_tbl(["about", "by", "in", "of", "with"], [
    ["annoyed · confused · excited · worried", "amazed · shocked · surprised", "interested", "bored · frightened · scared", "bored"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><i>I'm <b>interested in</b> history. · She was <b>shocked by</b> the price. · Are you <b>scared of</b> snakes? · I'm <b>bored with / of</b> this show.</i><br>
<b>Special form:</b> <i>scared</i> → <b>scary</b> (not <s>scaring</s>): <i>That was a <b>scary</b> movie.</i></p>
{_h("3. COMMON PAIRS")}
{_tbl(["feeling (-ed)", "cause (-ing)", "feeling (-ed)", "cause (-ing)"], [
    ["amazed", "amazing", "excited", "exciting"], ["annoyed", "annoying", "frightened", "frightening"], ["confused", "confusing", "interested", "interesting"],
    ["depressed", "depressing", "surprised", "surprising"]], "8.4pt")}
{_dont([("I'm boring. Let's go out!", "I'm <b>bored</b>. Let's go out!"), ("I'm interesting in music.", "I'm <b>interested in</b> music."), ("The trip was excited.", "The trip was <b>exciting</b>."), ("It was a scaring movie.", "It was a <b>scary</b> movie.")])}""",
    16, """<p>Brazilian students very often say <i>I'm boring</i> when they mean they feel bored, and they laugh when they discover what it means. Quick test: if you can add <i>very</i> and it describes how a person feels, use -ed.</p>""")


_SCALE_MOD = """<svg viewBox="0 0 520 64" width="100%" height="15mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<defs><linearGradient id="gm" x1="0" x2="1"><stop offset="0" stop-color="#d9ecef"/><stop offset="1" stop-color="#176074"/></linearGradient></defs>
<rect x="20" y="26" width="360" height="12" rx="6" fill="url(#gm)"/>
<text x="20" y="18" font-size="11" fill="#7d858a">weaker</text><text x="330" y="18" font-size="11" fill="#7d858a">stronger</text>
<text x="22" y="56" font-size="11.5" fill="#176074" font-weight="700">a bit / a little</text>
<text x="150" y="56" font-size="11.5" fill="#176074" font-weight="700">(no word)</text>
<text x="250" y="56" font-size="11.5" fill="#176074" font-weight="700">really / very · so</text>
<rect x="400" y="22" width="104" height="20" rx="4" fill="#f6efe2" stroke="#cbbca0"/>
<text x="413" y="36" font-size="11.5" fill="#9a4b2f" font-weight="700">too = a problem</text></svg>"""


def adjective_modifiers(b):
    """A2 Unit 26: personality adjectives with modifiers (a bit, a little, really, very, so, too) and seem / sound."""
    b.page(f"""{b.sec("+", "Grammar reference: modifiers · seem and sound", "")}
<div class="box" style="margin-top:0"><h4>WHAT ARE MODIFIERS?</h4>Modifiers are small words that go <b>before an adjective</b> and make it stronger or weaker: <i>She's <b>really</b> smart. He's <b>a bit</b> shy.</i>
{_SCALE_MOD}</div>
{_h("1. FORM AND USE")}
{_tbl(["modifier", "use", "examples"], [
    ["<b>really · very</b>", "make the adjective stronger; positive or negative adjectives", "<i>She's <b>really</b> smart. That's <b>very</b> rude.</i>"],
    ["<b>so</b>", "stronger, often with emotion; usually about information we already have", "<i>She says thank you. She's <b>so</b> polite!</i>"],
    ["<b>a bit · a little</b>", "make a <b>negative</b> adjective softer and more polite", "<i>He's <b>a bit</b> dishonest. He's <b>a little</b> miserable.</i>"],
    ["<b>too</b>", "more than we want: there is a <b>problem</b>", "<i>He's <b>too</b> shy to share an apartment.</i>"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>Very or too?</b> <i>The coffee is <b>very</b> hot.</i> (but I can drink it) · <i>The coffee is <b>too</b> hot.</i> (I can't drink it!)</p>
{_h("2. SEEM AND SOUND: WHEN WE AREN'T SURE")}
{_tbl(["", "+ adjective", "+ like + noun", "when?"], [
    ["<b>be</b>", "<i>She <b>is</b> cheerful.</i>", "<i>She<b>'s</b> a cheerful person.</i>", "we know the person"],
    ["<b>seem</b>", "<i>She <b>seems</b> cheerful.</i>", "<i>She <b>seems like</b> a nice person.</i>", "from what we see or know"],
    ["<b>sound</b>", "<i>She <b>sounds</b> great!</i>", "<i>He <b>sounds like</b> trouble.</i>", "from what we hear or read"]], "8.6pt")}
{_h("3. OPPOSITES")}
{_tbl(["positive", "negative", "positive", "negative"], [
    ["confident", "shy", "honest", "<b>dis</b>honest"], ["polite", "rude", "friendly", "<b>un</b>friendly"], ["smart", "not very smart", "interesting", "boring"],
    ["cheerful", "miserable", "relaxed", "stressed"]], "8.4pt")}
{_dont([("He is too nice. I like him!", "He's <b>really / very</b> nice. I like him!"), ("She's a bit friendly.", "She's <b>really</b> friendly."), ("He seems a nice person.", "He <b>seems like</b> a nice person."), ("She sounds greatly.", "She <b>sounds great</b>.")])}""",
    16, """<p>The key problem is <i>too</i>: Brazilians translate <i>muito</i> as <i>too</i> (<i>too beautiful</i> ✗). Check with: <i>Is it a problem?</i> If not, use <i>really</i> or <i>very</i>. Before a noun, use <i>really</i> or <i>very</i> (<i>a really nice guy</i>), not <i>so</i> or <i>too</i>.</p>""")


def comparatives_superlatives(b):
    """A2 Unit 27: comparatives and superlatives, with modifiers (slightly, a bit, a little, much, a lot)."""
    b.page(f"""{b.sec("+", "Grammar reference: comparatives and superlatives", "")}
<div class="box" style="margin-top:0"><h4>TWO THINGS OR THE WHOLE GROUP?</h4><b>Comparative</b> = we compare <b>two</b> people or things, usually with <b>than</b>: <i>Black coffee drinkers are <b>moodier than</b> latte drinkers.</i><br>
<b>Superlative</b> = we compare one with <b>all the others</b> in a group, with <b>the</b>: <i>Latte drinkers are <b>the most generous</b>.</i></div>
{_h("1. FORM")}
{_tbl(["adjective", "comparative", "superlative", "spelling"], [
    ["<b>one syllable</b><br>rude · strong · big", "rud<b>er</b> than · strong<b>er</b> than · bi<b>gger</b> than", "<b>the</b> rud<b>est</b> · <b>the</b> strong<b>est</b> · <b>the</b> bi<b>ggest</b>", "-e → -r / -st · one vowel + one consonant: double it (big → bigger)"],
    ["<b>two syllables ending in -y</b><br>moody · happy · easy", "mood<b>ier</b> than · happ<b>ier</b> than", "<b>the</b> mood<b>iest</b> · <b>the</b> happ<b>iest</b>", "y → i"],
    ["<b>two or more syllables</b><br>(also -ed / -ing adjectives)", "<b>more</b> anxious than · <b>more</b> relaxed than", "<b>the most</b> anxious · <b>the most</b> relaxed", "no -er / -est"],
    ["<b>irregular</b><br>good · bad · far", "<b>better</b> · <b>worse</b> · <b>farther</b> than", "<b>the best</b> · <b>the worst</b> · <b>the farthest</b>", "learn them!"]], "8.4pt")}
{_h("2. HOW BIG IS THE DIFFERENCE?")}
{_tbl(["small difference", "big difference"], [
    ["<b>slightly · a bit · a little</b> + comparative<br><i>Lattes are <b>slightly</b> more bitter than cappuccinos.</i><br><i>I'm <b>a bit</b> more patient than my brother.</i>",
     "<b>much · a lot</b> + comparative<br><i>Black coffee is <b>much</b> stronger than a latte.</i><br><i>They're <b>a lot</b> more relaxed about their health.</i>"]], "8.6pt")}
<p class="small" style="margin:.8mm 0">Modifiers go <b>before</b> the comparative. We don't use <i>very</i> with comparatives: <s>very stronger</s> → <b>much</b> stronger.<br>
<b>Superlative + group:</b> <i>the most creative <b>in</b> my family · the best coffee <b>of</b> all · the worst coffee I've <b>ever</b> had</i></p>
{_dont([("It's more better.", "It's <b>better</b>."), ("He's more rude than me.", "He's <b>ruder than</b> me."), ("She's the most happiest.", "She's <b>the happiest</b>."), ("Lattes are sweeter then black coffee.", "sweeter <b>than</b>"), ("It's very stronger.", "It's <b>much</b> stronger.")])}""",
    16, """<p>In fast speech, <i>than</i> is weak /ðən/ and <i>the</i> is weak /ðə/; stress the adjectives. Brazilians often say <i>more better</i>, a direct translation from Portuguese, and confuse <i>than</i> and <i>then</i> in writing. <i>Further</i> is also correct for distance.</p>""")
