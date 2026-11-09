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


_ADV_POS = """<svg viewBox="0 0 520 58" width="100%" height="14mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="10" y="8" width="110" height="26" rx="5" fill="#d9ecef"/><text x="65" y="25" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">FRONT</text>
<rect x="130" y="8" width="70" height="26" rx="5" fill="#eef1f2"/><text x="165" y="25" font-size="12" fill="#43494d" text-anchor="middle">I'm</text>
<rect x="210" y="8" width="110" height="26" rx="5" fill="#d9ecef"/><text x="265" y="25" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">MID</text>
<rect x="330" y="8" width="70" height="26" rx="5" fill="#eef1f2"/><text x="365" y="25" font-size="12" fill="#43494d" text-anchor="middle">going…</text>
<rect x="410" y="8" width="100" height="26" rx="5" fill="#d9ecef"/><text x="460" y="25" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">END</text>
<text x="65" y="50" font-size="10.5" fill="#7d858a" text-anchor="middle">Today,</text><text x="265" y="50" font-size="10.5" fill="#7d858a" text-anchor="middle">probably / usually</text>
<text x="460" y="50" font-size="10.5" fill="#7d858a" text-anchor="middle">carefully · outside · today</text></svg>"""


def adverb_position(b):
    """A2 Unit 28: types of adverbs and their position in the sentence (front, mid, end, before an adjective)."""
    b.page(f"""{b.sec("+", "Grammar reference: adverbs and word order", "")}
<div class="box" style="margin-top:0"><h4>WHERE DOES THE ADVERB GO?</h4>Adverbs add information: <b>when, how often, how sure, how, where</b> or <b>how much</b>. Different types go in different positions.
{_ADV_POS}</div>
{_h("1. TYPES AND POSITIONS")}
{_tbl(["type", "examples", "position", "example sentence"], [
    ["<b>time</b> (when?)", "today · last year · yesterday · next week", "end or front", "<i>I started making ice cream <b>last year</b>. / <b>Today</b> I'm making strawberry.</i>"],
    ["<b>frequency</b> (how often?)", "always · usually · often · sometimes · never", "mid", "<i>People <b>usually</b> want to try something new.</i>"],
    ["<b>certainty</b> (how sure?)", "probably · definitely", "mid", "<i>I'm <b>probably</b> going to try seaweed. I'll <b>definitely</b> call you.</i>"],
    ["<b>manner</b> (how?)", "carefully · quickly · well · better · hard", "end", "<i>Research your recipe <b>carefully</b>. He plays the piano <b>well</b>.</i>"],
    ["<b>place</b> (where?)", "here · there · outside · inside · home", "end", "<i>People want to spend time <b>outside</b>.</i>"],
    ["<b>degree</b> (how much?)", "really · very · too · so", "before the adjective", "<i>That's <b>really</b> interesting. It's <b>too</b> spicy.</i>"]], "8.4pt")}
{_h("2. MID POSITION: BEFORE THE MAIN VERB, AFTER BE")}
{_tbl(["main verb", "be", "auxiliary (will, have, can…) + verb"], [
    ["<i>I <b>usually get</b> coffee on my way to work.</i>", "<i>It<b>'s always</b> time for ice cream! She<b>'s never</b> late.</i>", "<i>They<b>'ll definitely be</b> happy. I've <b>often fallen</b> asleep.</i>"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>Irregular adverbs:</b> good → <b>well</b> (not <s>goodly</s>) · fast → <b>fast</b> · hard → <b>hard</b> · comparative: well → <b>better</b>. Most others: adjective + <b>-ly</b> (careful → carefully, quick → quickly).<br>
<b>End position order:</b> how → where → when: <i>I worked <b>hard</b> <b>at home</b> <b>yesterday</b>.</i></p>
{_dont([("I get usually coffee.", "I <b>usually get</b> coffee."), ("I like very much ice cream.", "I like ice cream <b>very much</b>."), ("She speaks English good.", "She speaks English <b>well</b>."), ("I'm going to probably buy it.", "I'm <b>probably</b> going to buy it.")])}""",
    22, """<p>The biggest problem for Brazilians is putting the adverb between the verb and the object (<i>I like very much pizza</i>, <i>I drink always coffee</i>). Rule of thumb: never separate a verb from its object. Exceptions exist; at A2, the table is enough.</p>""")


def service_language(b):
    """A2 Unit 29: language in service situations (air travel): questions, requests, instructions, announcements; intonation."""
    b.page(f"""{b.sec("+", "Language reference: questions, requests and instructions", "")}
<div class="box" style="margin-top:0"><h4>WHAT KIND OF SENTENCE IS IT?</h4>At an airport, in a hotel or in a store, you hear four kinds of sentences. If you know which kind it is, you know how to respond: <b>answer</b>, <b>do something</b>, or <b>just listen</b>.</div>
{_h("1. FOUR KINDS OF SENTENCES")}
{_tbl(["kind", "what it does", "examples", "you…"], [
    ["<b>question</b>", "asks for information", "<i>Where are you flying to today? Are you checking any bags?</i>", "answer: <i>To São Paulo. Just this one.</i>"],
    ["<b>request</b>", "asks you to do something, politely", "<i>May I see your passport, please? Can you open your bag, please?</i>", "do it and say <i>Here you are. / Sure. / Of course.</i>"],
    ["<b>instruction</b>", "tells you what you need to do", "<i>Place your bag on the scale. Step this way, please.</i>", "do it (you can say <i>OK</i>)"],
    ["<b>announcement</b>", "information or instructions for many people", "<i>We are about to take off. Please fasten your seat belt.</i>", "listen and do it"]], "8.4pt")}
<p class="small" style="margin:.8mm 0">Requests with <b>may, can, could</b> sound polite, but at check-in or security you can't say no! <i>Could</i> is a little more polite than <i>can</i>. Passengers use requests too: <i>Could I have some water, please? Do you have any napkins?</i></p>
{_h("2. INTONATION")}
{_tbl(["", "examples", "intonation"], [
    ["<b>yes/no questions and requests</b>", "<i>Are you checking any bags? Can you open your bag?</i>", "rising ↗"],
    ["<b>wh- questions</b> (where, what, how many…)", "<i>Where are you flying to? Which gate is it?</i>", "falling ↘"]], "8.6pt")}
{_h("3. USEFUL WORDS AND PHRASES")}
{_tbl(["at the airport", "meaning"], [
    ["<b>step</b> this way · <b>place</b> your bag", "walk this way · put your bag (formal)"],
    ["<b>take off</b> your belt / the plane <b>takes off</b>", "remove (opposite: <b>put on</b>) / leave the ground (opposite: <b>land</b>)"],
    ["we're <b>about to</b> take off · we'll <b>shortly</b> be passing through the cabin", "very soon (about to = the next thing)"],
    ["<b>Sorry, which gate? / Could you repeat that, please?</b>", "ask for repetition when you don't understand"]], "8.4pt")}
{_dont([("Give me some water.", "<b>Could I have</b> some water, please?"), ("I need to take off my belt?", "<b>Do I need to</b> take off my belt?"), ("What?", "<b>Sorry?</b> / <b>Could you repeat that, please?</b>"), ("Here is.", "<b>Here you are.</b>")])}""",
    24, """<p>Brazilians often use imperatives as requests (<i>Give me a coffee</i>), which sounds rude in English. Practice <i>Could I have…, please?</i> with rising intonation. In the US, people say <i>flight attendant</i> more than <i>cabin crew</i>, and a <i>bin</i> at security.</p>""")


_PHOTO_POS = """<svg viewBox="0 0 300 150" width="58mm" height="29mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="2" y="2" width="296" height="146" rx="6" fill="#f4f8f9" stroke="#77acb5" stroke-width="2"/>
<rect x="2" y="2" width="296" height="38" rx="6" fill="#e3eff1"/>
<text x="150" y="26" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">in the background / at the top</text>
<text x="40" y="84" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">on the left</text>
<text x="150" y="84" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">in the middle</text>
<text x="258" y="84" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">on the right</text>
<text x="150" y="135" font-size="12" fill="#176074" font-weight="700" text-anchor="middle">in the foreground / at the bottom</text></svg>"""


def describing_photos(b):
    """A2 Unit 31: describing a photo: there is/are, present continuous, look / look like / it looks like, maybe / perhaps, positions."""
    b.page(f"""{b.sec("+", "Language reference: describing a photo", "")}
<div class="box" style="margin-top:0;display:flex;gap:4mm;align-items:center"><div style="flex:1"><h4>FIVE TOOLS FOR ANY PHOTO</h4>Say <b>what</b> is in the photo, <b>where</b> it is, what people <b>are doing</b>, how they <b>look</b>, and what you <b>guess</b>. You don't need to describe everything. Native speakers use simple language, so you can too.</div>{_PHOTO_POS}</div>
{_h("1. WHAT AND WHERE: THERE IS / THERE ARE + POSITION")}
{_tbl(["", "examples", "careful"], [
    ["<b>there is</b> + singular", "<i><b>There's</b> a woman on the left. <b>There's</b> a window in the background.</i>", "<i>There's</i> = there is"],
    ["<b>there are</b> + plural", "<i><b>There are</b> two people in this photo. <b>There are</b> some tomatoes at the bottom.</i>", "not <s>There is two people</s>"],
    ["<b>positions</b>", "<b>in</b> the middle · <b>on</b> the left / right · <b>at</b> the top / bottom · <b>in</b> the background / foreground", "a photo <b>of</b> two people"]], "8.4pt")}
{_h("2. ACTIONS: PRESENT CONTINUOUS (BUT NOT WITH STATE VERBS)")}
{_tbl(["actions now", "states (no -ing)"], [
    ["<i>The man <b>is cutting</b> vegetables. They<b>'re cooking</b>.</i><br>am / is / are + verb-ing", "<i>I think they <b>live</b> together. They <b>look</b> happy. She <b>has</b> a phone.</i><br>live, look (= seem), like, know, have (= own)"]], "8.6pt")}
{_h("3. LOOK, LOOK LIKE, IT LOOKS LIKE")}
{_tbl(["form", "followed by", "example"], [
    ["<b>look</b>", "an adjective", "<i>They <b>look</b> very happy.</i>"],
    ["<b>look like</b>", "a noun", "<i>He <b>looks like</b> a chef.</i>"],
    ["<b>it looks like</b>", "a clause (subject + verb)", "<i><b>It looks like</b> they have a lot of time.</i>"]], "8.6pt")}
{_h("4. GUESSING: MAYBE, PERHAPS, I THINK")}
<p class="small" style="margin:.5mm 0"><b>Maybe</b> and <b>perhaps</b> go at the <b>beginning</b> of the sentence or clause: <i><b>Maybe</b> they're friends. <b>Perhaps</b> it's the weekend.</i> Also: <i>I think… · They might be…</i><br>
<b>Their / there / they're</b> sound the same /ðer/: <i><b>Their</b> kitchen</i> (possessive) · <i>over <b>there</b></i> (place) · <i><b>They're</b> cooking</i> (they are).</p>
{_dont([("There is two people.", "There <b>are</b> two people."), ("They look like happy.", "They <b>look</b> happy."), ("Can be she's his mother.", "<b>Maybe</b> she's his mother."), ("In the photo I can see a man.", "<b>There's</b> a man in the photo.")])}""",
    16, """<p>Brazilians often say <i>Can be…</i> (a direct translation) for guesses: practice <i>Maybe…</i> and <i>Perhaps…</i> at the start of the sentence. Exam tip: avoid repeating <i>I can see</i>; use <i>there is / there are</i> and positions.</p>""")


def present_for_future(b):
    """A2 Unit 32: present simple (timetables) and present continuous (arrangements) for the future."""
    b.page(f"""{b.sec("+", "Grammar reference: present tenses for the future", "")}
<div class="box" style="margin-top:0"><h4>TWO PRESENT TENSES, ONE FUTURE</h4>English often uses <b>present</b> tenses to talk about the <b>future</b>. The time expression (<i>on Monday, at seven, tomorrow</i>) shows that it's the future.<br>
<b>Present simple</b> = a fixed schedule or timetable (tours, transportation, classes, events). · <b>Present continuous</b> = a personal plan you have already arranged, often with other people.</div>
{_h("1. FORM AND USE")}
{_tbl(["", "present simple: timetables", "present continuous: arrangements"], [
    ["<b>positive</b>", "<i>The flight <b>lands</b> at two. The bus <b>leaves</b> at seven.</i>", "<i>We<b>'re having</b> dinner at six. I<b>'m going</b> on the photo tour.</i>"],
    ["<b>negative</b>", "<i>The bus <b>doesn't leave</b> until after lunch.</i>", "<i>I<b>'m not coming</b> on the boat trip.</i>"],
    ["<b>questions</b>", "<i>What time <b>does</b> the boat trip <b>start</b>?</i><br>(question word) + do / does + subject + verb", "<i><b>Are</b> you and Maya <b>coming</b>? What <b>are</b> you <b>doing</b> on Thursday?</i><br>(question word) + am / is / are + subject + verb-ing"],
    ["<b>typical verbs</b>", "start, finish, open, close, leave, arrive, land, take off", "meet, have dinner, see, go, come, stay, fly, visit"],
    ["<b>who decided?</b>", "a company, a school, a timetable", "you (and other people): it's in your calendar"]], "8.4pt")}
{_h("2. COMPARE")}
{_tbl(["sentence", "why?"], [
    ["<i>The museum <b>opens</b> at nine tomorrow.</i>", "official schedule"],
    ["<i>We<b>'re visiting</b> the museum tomorrow morning.</i>", "our arrangement"],
    ["<i>The movie <b>starts</b> at 8:30, so we<b>'re meeting</b> at eight.</i>", "both: the timetable + our plan"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>Remember the -s:</b> <i>the bus leave<b>s</b>, the flight land<b>s</b>, the tour start<b>s</b></i>. Linking helps you hear and say it: <i>leaves‿at seven, lands‿at two</i>.<br>
Later you will add <b>going to</b> (intentions) and <b>will</b> (decisions now, predictions). For fixed plans, the present continuous is the most natural choice.</p>
{_dont([("Tomorrow I meet my brother for coffee.", "Tomorrow I<b>'m meeting</b> my brother."), ("The bus is leaving at 7:00 every day.", "The bus <b>leaves</b> at 7:00 every day."), ("What time the tour starts?", "What time <b>does</b> the tour <b>start</b>?"), ("You are coming with us?", "<b>Are you</b> coming with us?")])}""",
    16, """<p>Brazilians often use the present simple for personal plans (<i>Tomorrow I go to the doctor</i>), because Portuguese allows it. Ask: <i>Is it a timetable or your plan?</i> Keep <i>going to / will</i> for later units; don't overload the student now.</p>""")


_SCALE_PRED = """<svg viewBox="0 0 520 60" width="100%" height="14mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<defs><linearGradient id="gp" x1="0" x2="1"><stop offset="0" stop-color="#d9ecef"/><stop offset="1" stop-color="#176074"/></linearGradient></defs>
<rect x="10" y="22" width="500" height="12" rx="6" fill="url(#gp)"/>
<text x="10" y="14" font-size="11" fill="#7d858a">0% sure</text><text x="455" y="14" font-size="11" fill="#7d858a">100% sure</text>
<text x="12" y="52" font-size="10.5" fill="#176074" font-weight="700">won't · certainly won't</text>
<text x="150" y="52" font-size="10.5" fill="#176074" font-weight="700">unlikely to · probably won't</text>
<text x="300" y="52" font-size="10.5" fill="#176074" font-weight="700">may · might · could</text>
<text x="420" y="52" font-size="10.5" fill="#176074" font-weight="700">likely to · will</text></svg>"""


def predictions(b):
    """A2 Unit 33: making predictions: will / won't (+ probably, definitely), may / might / could, be likely / unlikely to."""
    b.page(f"""{b.sec("+", "Grammar reference: making predictions", "")}
<div class="box" style="margin-top:0"><h4>HOW SURE ARE YOU?</h4>When we talk about the future, we show how sure we are. Choose the words that match your opinion.
{_SCALE_PRED}</div>
{_h("1. FORM")}
{_tbl(["structure", "form", "examples"], [
    ["<b>will / won't</b>", "will + base form", "<i>The technology <b>will be</b> ready soon. It <b>won't be</b> cheap.</i>"],
    ["<b>will + adverb</b>", "will + <b>probably / definitely / certainly / possibly</b> + base form<br><b>probably / definitely</b> + won't", "<i>It<b>'ll probably be</b> better for the environment.</i><br><i>They <b>probably won't</b> be ready this year.</i>"],
    ["<b>may / might / could</b>", "+ base form (no <i>to</i>, no -s)", "<i>They <b>might prevent</b> accidents. We <b>could see</b> big changes.</i>"],
    ["<b>be likely / unlikely to</b>", "am / is / are + (un)likely + <b>to</b> + base form", "<i>Older people <b>are likely to</b> love them. It<b>'s unlikely to</b> happen soon.</i>"]], "8.4pt")}
{_h("2. USE")}
{_tbl(["", "meaning", "notes"], [
    ["<b>will / won't</b>", "we feel sure", "<i>'ll</i> in speech: <i>It'll be…</i> · <i>won't</i> /woʊnt/ ≠ <i>want</i> /wɑːnt/"],
    ["<b>may / might / could</b>", "maybe; we're less sure", "<i>may</i> is a little more formal, common in writing; negative: <i>may not, might not</i> (not <s>couldn't</s> for predictions)"],
    ["<b>if + present, … might / may</b>", "a real situation, but an uncertain result", "<i>If robotaxis <b>become</b> popular, this <b>might result</b> in big changes.</i>"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>Adverb position:</b> after <i>will</i>, before <i>won't</i>: <i>It will <b>probably</b> rain. · It <b>probably</b> won't rain.</i> (Unit 28: adverbs of certainty go in mid position.)<br>
<b>Likely</b> is an adjective, so it needs <b>be</b>: <i>It's likely to…</i>, not <s>It likely to…</s>. Opposite: <b>unlikely</b>.</p>
{_dont([("It will to be cheaper.", "It <b>will be</b> cheaper."), ("They might are safer.", "They <b>might be</b> safer."), ("It's likely be popular.", "It's likely <b>to be</b> popular."), ("I want go by car tomorrow. (= won't)", "I <b>won't</b> go by car tomorrow.")])}""",
    16, """<p>Brazilians often add <i>to</i> after modals (<i>might to</i>), confuse <i>want</i> and <i>won't</i> in speaking and listening, and use <i>will</i> for every prediction. Practice the scale: ask the student to rate each prediction from 0% to 100%.</p>""")


def future_forms(b):
    """A2 Unit 34: four future forms compared: present continuous, be going to, will, present simple."""
    b.page(f"""{b.sec("+", "Grammar reference: four ways to talk about the future", "")}
<div class="box" style="margin-top:0"><h4>WHICH FUTURE?</h4>English has no single "future tense". We choose the form that shows <b>what kind of future</b> it is: an arrangement, a plan, a prediction or a timetable. Sometimes two forms are possible; the meaning changes a little.</div>
{_h("1. THE FOUR FORMS")}
{_tbl(["form", "use", "examples"], [
    ["<b>present continuous</b><br>am / is / are + verb-ing", "<b>arrangements</b>: fixed plans, often with other people, with a time", "<i>I<b>'m starting</b> at the shelter next week. We<b>'re meeting</b> Danny tomorrow.</i>"],
    ["<b>be going to</b> + base form", "<b>plans and intentions</b>: you have decided", "<i>I<b>'m going to take</b> a year off. They<b>'re going to learn</b> Portuguese.</i>"],
    ["", "<b>predictions with evidence</b>: you can see it now", "<i>Look at those clouds. It<b>'s going to rain</b>. Look at the line: we<b>'re going to be</b> busy.</i>"],
    ["<b>will</b> + base form", "<b>predictions with opinion</b> (I think, I'm sure, probably)", "<i>I think he<b>'ll have</b> a great time. You<b>'ll love</b> it.</i>"],
    ["", "<b>decisions at the moment of speaking</b>, offers, promises", "<i>The phone's ringing. I<b>'ll get</b> it! I<b>'ll help</b> you.</i>"],
    ["<b>present simple</b>", "<b>timetables</b> and schedules (Unit 32)", "<i>The class <b>starts</b> in a few weeks. My lesson <b>is</b> on Friday.</i>"]], "8.3pt")}
{_h("2. GOING TO OR WILL?")}
{_tbl(["going to", "will"], [
    ["decided before: <i>I'm going to visit my parents this weekend.</i>", "decided now: <i>Oh, you're not busy? I'll visit you, then!</i>"],
    ["evidence: <i>He's driving too fast. He's going to have an accident!</i>", "opinion: <i>I think he'll have an accident one day.</i>"]], "8.6pt")}
<p class="small" style="margin:.8mm 0"><b>going to</b> in the first conditional: <i>If I get the internship, I<b>'m going to go</b> with the vets.</i> (also <i>will</i>)<br>
<b>gonna</b>: in fast, informal speech, <i>going to</i> often sounds like <i>gonna</i> /ˈɡʌnə/. Understand it and use it in speech if you like, but <b>never write it</b>.</p>
{_dont([("I will meet Danny tomorrow at six. (arranged)", "I<b>'m meeting</b> Danny tomorrow at six."), ("Look at the clouds! It will rain.", "It<b>'s going to</b> rain."), ("I think you're having a great time in Paris.", "I think you<b>'ll have</b> a great time."), ("I'm going to study tomorrow. I gonna study.", "I<b>'m going to</b> study.")])}""",
    16, """<p>This page brings together Units 32, 33 and 34. Brazilians tend to use <i>will</i> for everything, or the present simple for plans (<i>Tomorrow I travel</i>). Ask two questions: <i>Did you decide before? Do you have evidence?</i></p>""")


def suggestions_offers(b):
    """A2 Unit 35: making plans together: suggestions (let's / why don't we / how about), offers (I'll / why don't I), plans and predictions."""
    b.page(f"""{b.sec("+", "Grammar reference: making plans together", "")}
<div class="box" style="margin-top:0"><h4>PLANNING WITH FRIENDS</h4>When we plan a day out, we do four things: we <b>suggest</b> ideas, we <b>offer</b> to help, we say what we have <b>already decided</b>, and we <b>predict</b> what will happen.</div>
{_h("1. SUGGESTIONS")}
{_tbl(["form", "grammar", "examples"], [
    ["<b>Let's</b>", "Let's + base form", "<i><b>Let's leave</b> early. <b>Let's not go</b> by car.</i>"],
    ["<b>Why don't we</b>", "Why don't we + base form?", "<i><b>Why don't we bring</b> our own drinks?</i>"],
    ["<b>How about / What about</b>", "How about + verb-ing / noun?", "<i><b>How about stopping</b> at the bakery? <b>What about</b> a picnic?</i>"]], "8.5pt")}
<p class="small" style="margin:.8mm 0"><b>Let's</b> = let us: don't forget the apostrophe. <b>Shall we…?</b> is possible but sounds formal or British in the US.<br>
<b>Answer a suggestion:</b> <i>Good idea! · That sounds great. · Sure, why not? · I'm not sure. How about…? · Sorry, I can't on Saturday.</i></p>
{_h("2. OFFERS AND PLANS")}
{_tbl(["", "form", "examples"], [
    ["<b>offer</b> (you decide now)", "I'll + base form · Why don't I + base form?", "<i>I<b>'ll bring</b> the sunscreen. <b>Why don't I get</b> some fruit?</i>"],
    ["<b>plan</b> (decided before)", "be going to + base form", "<i>I<b>'m going to plan</b> the hike tonight. (I decided this yesterday.)</i>"]], "8.5pt")}
{_h("3. PREDICTIONS")}
{_tbl(["", "form", "examples"], [
    ["<b>evidence</b> (a forecast, the sky)", "be going to", "<i>The forecast says it<b>'s going to be</b> hot.</i>"],
    ["<b>opinion</b>", "will", "<i>We<b>'ll need</b> hats. I think you<b>'ll love</b> the beach.</i>"]], "8.5pt")}
{_dont([("How about stop at the bakery?", "How about <b>stopping</b> at the bakery?"), ("Let's to go to the beach.", "Let's <b>go</b> to the beach."), ("Why we don't take the train?", "Why <b>don't we</b> take the train?"), ("Lets bring towels.", "<b>Let's</b> bring towels."), ("I bring the drinks! (offer)", "I<b>'ll</b> bring the drinks!")])}""",
    21, """<p>This page reviews Unit 34 (going to / will) in a new function: planning together. Brazilians often add <i>to</i> after <i>Let's</i>, use the base form after <i>How about</i>, and say <i>Why we don't…?</i> Drill the three suggestion forms with rising, friendly intonation.</p>""")


def work_emails(b):
    """A2 Unit 36: the six parts of a work email, semi-formal vs formal, useful phrases."""
    b.page(f"""{b.sec("+", "Language reference: writing work emails", "")}
<div class="box" style="margin-top:0"><h4>SIX PARTS OF A WORK EMAIL</h4>People are busy: make your email <b>clear</b> (one topic per paragraph), <b>polite</b> and <b>easy to answer</b> (say what you need). Choose the style for the reader: <b>semi-formal</b> for colleagues, <b>formal</b> for customers and people you have never met.</div>
{_h("1. USEFUL PHRASES")}
{_tbl(["part", "semi-formal (colleagues)", "formal (customers, new contacts)"], [
    ["<b>1 greeting</b>", "<i>Hi Paulo, · Hello Maya,</i>", "<i>Dear Ms. Brooks, · Dear Mr. Jones,</i>"],
    ["<b>2 opening</b>", "<i>Thanks for your email. · It was good to talk to you yesterday.</i>", "<i>Thank you for your email. · Following our meeting on March 5, …</i>"],
    ["<b>3 reason for writing</b>", "<i>I'm writing to let you know about… · I just wanted to check…</i>", "<i>I am writing to ask about… · I would like to confirm…</i>"],
    ["<b>4 call to action</b>", "<i>Let me know if that's OK. · Can you send me the details?</i>", "<i>Please let me know if you are happy with this. · Could you confirm…?</i>"],
    ["<b>5 closing</b>", "<i>See you on Tuesday! · Looking forward to it.</i>", "<i>I look forward to hearing from you. · I am looking forward to meeting you.</i>"],
    ["<b>6 signing</b>", "<i>Best, · Thanks, · All the best, + first name</i>", "<i>Kind regards, · Best regards, · Sincerely, + full name</i>"]], "8.2pt")}
{_h("2. STYLE TIPS")}
<ul class="small" style="margin:.5mm 0;line-height:1.5"><li><b>Commas:</b> put a comma after the greeting and after the sign-off: <i>Hi Paulo, … Kind regards, Maya</i>. In very formal American business letters, the greeting can end with a colon: <i>Dear Ms. Webster:</i></li>
<li><b>Contractions</b> (<i>I'm, don't</i>) make an email more informal. Formal emails use full forms: <i>I am, do not</i>.</li>
<li><b>Titles:</b> <i>Mr.</i> (man), <i>Ms.</i> (woman, married or not) + <b>last name</b>: <i>Dear Ms. Brooks</i>, never <i>Dear Ms. Linda</i>.</li>
<li><b>look forward to + noun / verb-ing:</b> <i>I look forward to <b>hearing</b> from you.</i> (to is a preposition here)</li>
<li><b>just</b> makes a request softer and more polite: <i>I just wanted to check the time.</i></li></ul>
{_dont([("Dear Ms. Linda,", "Dear Ms. <b>Brooks</b>,"), ("I look forward to hear from you.", "I look forward to <b>hearing</b> from you."), ("Hi dear Maya,", "Hi Maya, / Dear Maya,"), ("Kisses, Paulo", "Best, Paulo"), ("I write to inform about the meeting.", "I<b>'m writing</b> to let you know about the meeting.")])}""",
    23, """<p>Brazilians often bring Portuguese email habits into English: <i>Dear</i> + first name with a title, very long openings, and friendly sign-offs that are too personal for work. In the US, work emails are short and direct but polite; the call to action is essential.</p>""")


def gerunds(b):
    """A2 Unit 37: verb + -ing as a noun (gerund): subject, object, after prepositions, after certain verbs; other -ing uses; spelling."""
    b.page(f"""{b.sec("+", "Grammar reference: -ing forms (gerunds)", "")}
<div class="box" style="margin-top:0"><h4>A VERB THAT WORKS LIKE A NOUN</h4>When we use verb + <b>-ing</b> as a noun, it is called a <b>gerund</b>. It can go in the same places as a noun: <i><b>Yoga</b> is relaxing.</i> → <i><b>Swimming</b> is relaxing.</i></div>
{_h("1. WHERE GERUNDS GO")}
{_tbl(["position", "examples"], [
    ["<b>subject</b> of the sentence", "<i><b>Running</b> is an activity you can do in the park. <b>Walking</b> is great exercise.</i>"],
    ["<b>object</b> of the sentence", "<i>Today we're going to discuss <b>well-being</b>. My friends and I discuss <b>running</b> a lot.</i>"],
    ["after a <b>preposition</b> (about, for, at, of, before, after…)", "<i>Thanks for <b>joining</b> us. He's good at <b>swimming</b>. I'm thinking about <b>joining</b> a gym.</i>"]], "8.5pt")}
{_h("2. VERBS FOLLOWED BY A GERUND")}
{_tbl(["verbs", "examples"], [
    ["<b>enjoy · dislike · don't mind · miss</b>", "<i>I enjoy <b>running</b>. I miss <b>cycling</b> to work. I don't mind <b>getting</b> up early.</i>"],
    ["<b>avoid · keep · finish · stop</b>", "<i>I avoid <b>going</b> to the gym. You can keep <b>cycling</b> in bad weather.</i>"],
    ["<b>consider · suggest · think about</b>", "<i>You should consider <b>changing</b> activities.</i>"],
    ["<b>look forward to</b> (to = preposition)", "<i>I look forward to <b>running</b> in the snow.</i> ✗ <i>look forward to run</i>"]], "8.5pt")}
<p class="small" style="margin:.8mm 0">Compare: <b>want, would like, decide, plan, hope, need</b> + <b>to</b> + base form: <i>I want <b>to start</b> running.</i> <b>like, love, hate, start</b> can take both: <i>I love <b>swimming</b> / <b>to swim</b>.</i></p>
{_h("3. OTHER -ING FORMS (NOT GERUNDS) AND SPELLING")}
<p class="small" style="margin:.5mm 0"><b>continuous verb</b>: <i>It's <b>raining</b>.</i> · <b>adjective</b>: <i>Exercise can be <b>boring</b>. <b>swimming</b> goggles, <b>running</b> shoes</i> · <b>go + -ing</b> for activities: <i>go <b>running</b>, go <b>swimming</b>, go <b>hiking</b></i><br>
<b>Spelling:</b> most verbs + -ing (<i>walk → walking</i>) · final <b>-e</b> → drop it (<i>dance → dancing</i>) · one vowel + one consonant → double it (<i>run → running, swim → swimming</i>)</p>
{_dont([("To walk is the best exercise.", "<b>Walking</b> is the best exercise."), ("I enjoy to run.", "I enjoy <b>running</b>."), ("Thanks for help me.", "Thanks for <b>helping</b> me."), ("You should consider to walk to work.", "You should consider <b>walking</b> to work."), ("Let's go to swim.", "Let's go <b>swimming</b>.")])}""",
    20, """<p>Portuguese uses the infinitive in most of these places (subject, after prepositions), so Brazilians say <i>To walk is good</i> or <i>Thanks for help me</i>. Drill the verbs in section 2 with personal examples. Earlier units practiced verb + to + base form; here the focus is the gerund.</p>""")


def articles(b):
    """A2 Unit 38: a/an, the and zero article."""
    b.page(f"""{b.sec("+", "Grammar reference: articles (a/an, the, no article)", "")}
<div class="box" style="margin-top:0"><h4>WHICH THING?</h4><b>a/an</b> = one of many, or new information. <b>the</b> = we know exactly which one. <b>no article</b> = things in general, names, meals. Use <b>an</b> before a vowel <i>sound</i>: <i>an hour, an old house</i>, but <i>a university</i> (/juː/).</div>
{_h("1. A / AN")}
{_tbl(["use", "examples"], [
    ["the <b>first time</b> we mention something", "<i>There's <b>a</b> white fence outside the house.</i>"],
    ["<b>one of many</b> similar things", "<i>You'll have <b>a</b> great day. It's <b>a</b> big house on <b>a</b> hill.</i>"],
    ["<b>jobs</b>", "<i>Paulo is <b>a</b> travel agent. She's <b>an</b> engineer.</i>"],
    ["<b>how often</b>, prices and speed", "<i>three times <b>a</b> day · once <b>a</b> week · $20 <b>an</b> hour</i>"]], "8.5pt")}
{_h("2. THE")}
{_tbl(["use", "examples"], [
    ["the <b>second time</b> we mention something", "<i>There's a white fence… Everyone takes a photo at <b>the</b> fence.</i>"],
    ["we <b>know which one</b> (from the situation)", "<i>The museum is next to the house. Close <b>the</b> door, please.</i>"],
    ["there is <b>only one</b>", "<i><b>the</b> world, <b>the</b> sun, <b>the</b> internet</i>"],
    ["<b>superlatives</b> and ordinals", "<i><b>the</b> oldest cave, <b>the</b> best place, <b>the</b> first house</i>"],
    ["<b>rivers, oceans</b>, some countries, places in town", "<i><b>the</b> Mississippi, <b>the</b> Atlantic, <b>the</b> United States, go to <b>the</b> theater</i>"]], "8.5pt")}
{_h("3. NO ARTICLE")}
{_tbl(["use", "examples"], [
    ["plural and uncountable nouns <b>in general</b>", "<i>Kids love caves. I like history. Visitors love the town.</i>"],
    ["<b>names</b> of people, most cities, states, countries, continents", "<i>Mark Twain, Hannibal, Missouri, Brazil, South America</i>"],
    ["<b>meals</b>, days, months; go <b>to school / to work / home</b>", "<i>have dinner on Saturday · in April · go to work</i>"]], "8.5pt")}
{_dont([("The visitors love Hannibal. (in general)", "Visitors love Hannibal."), ("He is engineer.", "He's <b>an</b> engineer."), ("Mississippi is a long river.", "<b>The</b> Mississippi is a long river."), ("I live in the Brazil.", "I live in Brazil."), ("It's oldest cave in Missouri.", "It's <b>the</b> oldest cave in Missouri.")])}""",
    24, """<p>Portuguese uses the definite article for things in general (<i>the life is short</i> ✗), with names and countries (<i>the Brazil</i> ✗), and drops <i>a</i> with jobs. Ask the student: one of many, or exactly which one? Articles need regular review at every level.</p>""")


def noun_phrases(b):
    """A2 Unit 39: noun + noun, noun + preposition phrase, possessive 's / s', of for things."""
    b.page(f"""{b.sec("+", "Grammar reference: putting nouns together", "")}
<div class="box" style="margin-top:0"><h4>FOUR WAYS</h4>English joins nouns in four main ways: <b>noun + noun</b> (<i>a coffee cup</i>), <b>noun + preposition + noun</b> (<i>a story about a dog</i>), <b>'s</b> for people and animals (<i>Marcos's laptop</i>) and <b>of</b> for parts of things (<i>the back of the picture</i>).</div>
{_h("1. NOUN + NOUN: EVERYDAY THINGS")}
{_tbl(["rule", "examples"], [
    ["the <b>second</b> noun is the main thing; the first works like an <b>adjective</b>", "<i>milk chocolate</i> = a kind of chocolate · <i>chocolate milk</i> = a kind of milk"],
    ["the first noun is <b>singular</b>", "<i>a <b>shoe</b> store</i> (✗ shoes store) · <i>a <b>pencil</b> holder</i> · <i>a ten-<b>dollar</b> bill</i>"],
    ["<b>stress</b> the first noun", "<i>a KITchen table · a BUS stop · a BIRTHday cake</i>"]], "8.5pt")}
{_h("2. NOUN + PREPOSITION + NOUN: LESS USUAL THINGS")}
{_tbl(["", "examples"], [
    ["about · with · on · in · of (containers)", "<i>a story <b>about</b> a dog · the woman <b>with</b> the knife · the cake <b>on</b> the counter · a box <b>of</b> books</i>"]], "8.5pt")}
{_h("3. 'S AND OF: WHO OR WHAT IT BELONGS TO")}
{_tbl(["use", "examples"], [
    ["<b>'s</b>: people, animals, countries, organizations", "<i>Leo's ideas · Kate's dog · Brazil's coast · the company's website</i>"],
    ["plural owners ending in -s: <b>s'</b>", "<i>my parents' bedroom · the teachers' office</i> (irregular: <i>the children's school</i>)"],
    ["name ending in -s: <b>s's</b> or <b>s'</b>", "<i>Marcos's laptop</i> (also <i>Marcos' laptop</i>)"],
    ["<b>of</b>: things, places, parts", "<i>the back <b>of</b> the picture · the end <b>of</b> the story · the roof <b>of</b> the house</i>"]], "8.5pt")}
{_dont([("the laptop of Marcos", "Marcos's laptop"), ("the house's roof", "the roof of the house"), ("a shoes store", "a shoe store"), ("the kitchen's door", "the kitchen door"), ("a bike boy", "a boy with a bike")])}""",
    25, """<p>Portuguese puts the main noun first and links with <i>de</i>, so Brazilians say <i>the laptop of Marcos</i>, <i>a cup of coffee</i> when they mean the object (a <i>coffee cup</i> can be empty; a <i>cup of coffee</i> has coffee in it), or mix the order (<i>chocolate milk</i> vs <i>milk chocolate</i>). Ask: which is the main thing? It goes last.</p>""")


def quantifiers(b):
    """A2 Unit 41: countable/uncountable nouns; some, any, a few, a little, much, many, a lot of, too much/many, enough, plenty of."""
    b.page(f"""{b.sec("+", "Grammar reference: countable and uncountable nouns, quantifiers", "")}
<div class="box" style="margin-top:0"><h4>CAN YOU COUNT IT?</h4><b>Countable</b> nouns have a singular and a plural: <i>a chili, two chilies, an onion, onions</i>. <b>Uncountable</b> nouns have no plural and no <i>a/an</i>: <i>rice, milk, spinach, chicken</i> (the meat), <i>money, time, advice, bread</i>. To count them, use a container or unit: <i>a bag of spinach, a can of tomatoes, two pounds of chicken, a piece of advice</i>.</div>
{_h("1. QUANTIFIERS")}
{_tbl(["", "plural countable (onions)", "uncountable (rice)", "use"], [
    ["<b>some</b>", "<i>some onions</i>", "<i>some rice</i>", "positive sentences, offers and requests (<i>Would you like some…?</i>)"],
    ["<b>any</b>", "<i>any onions</i>", "<i>any rice</i>", "negatives and questions"],
    ["<b>a few / a little</b>", "<i>a few onions</i>", "<i>a little rice</i>", "a small amount (but enough)"],
    ["<b>many / much</b>", "<i>many onions</i>", "<i>much rice</i>", "mostly negatives and questions: <i>How many…? How much…?</i>"],
    ["<b>a lot of / lots of</b>", "<i>a lot of onions</i>", "<i>a lot of rice</i>", "positive sentences (more natural than <i>many / much</i>)"],
    ["<b>too many / too much</b>", "<i>too many onions</i>", "<i>too much rice</i>", "more than we want: a problem"],
    ["<b>enough</b>", "<i>enough onions</i>", "<i>enough rice</i>", "the amount we need"],
    ["<b>plenty of</b>", "<i>plenty of onions</i>", "<i>plenty of rice</i>", "more than enough, with extra: no problem"]], "8.2pt")}
{_h("2. FOOD: COUNTABLE OR UNCOUNTABLE?")}
<p class="small" style="margin:.5mm 0"><b>a chicken</b> (the animal) / <b>chicken</b> (the meat) · <b>a coffee, a juice, a cake</b> (one, for one person) / <b>coffee, juice, cake</b> (in general, or to share): <i>I'll have <b>a</b> coffee, please. · Do you want some cake?</i></p>
{_dont([("I need an advice.", "I need some advice. / a piece of advice"), ("How many money do you have?", "How <b>much</b> money do you have?"), ("I have many time.", "I have <b>a lot of</b> time."), ("We have plenty rice.", "We have plenty <b>of</b> rice."), ("There are too much people here.", "There are too <b>many</b> people here.")])}""",
    25, """<p>Some nouns are countable in Portuguese but uncountable in English: <i>advice, information, news, furniture, bread, money</i>. Brazilians also say <i>many money</i> and forget <i>of</i> after <i>plenty</i>. <i>A few / a little</i> sound positive; <i>few / little</i> (without <i>a</i>) mean "not enough".</p>""")


def advice_instructions(b):
    """A2 Unit 42: advice vs instructions: should, it's a good idea to, I recommend; must, have to, need to, can't, it's important that."""
    b.page(f"""{b.sec("+", "Grammar reference: advice and instructions", "")}
<div class="box" style="margin-top:0"><h4>A GOOD IDEA OR NECESSARY?</h4><b>Advice</b> = a good idea (you can choose). <b>Instructions</b> = necessary (you don't have a choice). Pharmacists, doctors and nurses use both, so listen carefully!</div>
{_h("1. ADVICE")}
{_tbl(["form", "grammar", "examples"], [
    ["<b>should / shouldn't</b>", "+ base form", "<i>You should check his temperature regularly. You shouldn't stay in the sun.</i>"],
    ["<b>it's a good idea to</b>", "+ base form", "<i>It's a good idea to do some eye exercises every day.</i>"],
    ["<b>I recommend</b>", "+ noun · + (that) you + base form", "<i>I recommend this sunscreen. I recommend (that) you buy two bottles.</i>"]], "8.5pt")}
{_h("2. INSTRUCTIONS")}
{_tbl(["form", "grammar", "examples"], [
    ["<b>must / have to / need to</b>", "must + base form · have to / need to + base form", "<i>You must take this before meals. You have to put more on every two hours. You need to call the doctor.</i>"],
    ["<b>can't / must not</b>", "+ base form", "<i>You can't drive while you're taking this medicine.</i>"],
    ["<b>it's important that</b>", "+ subject + verb (a clause)", "<i>It's important that you limit your time on the computer.</i>"]], "8.5pt")}
<p class="small" style="margin:.8mm 0"><b>Modal verbs</b> (<i>should, must, can't</i>) have no <i>to</i> after them and no <i>-s</i>: <i>She <b>must take</b></i> ✗ <i>She musts to take</i>. In everyday American English, <i>have to</i> is more common than <i>must</i>.<br>
<b>Check you understand:</b> <i>Sorry, could you repeat that? · So, let me check: I have to take two pills now and two before bed?</i></p>
{_dont([("You must to take one pill.", "You must <b>take</b> one pill."), ("She can't to drive.", "She can't <b>drive</b>."), ("I recommend you this.", "I recommend <b>this</b>. / I recommend (that) you try this."), ("It's important you must rest.", "It's important that you rest."), ("You should to drink water.", "You should <b>drink</b> water.")])}""",
    20, """<p>Brazilians often put <i>to</i> after modals (<i>must to, should to</i>) and say <i>I recommend you this</i>. Drill with a build-up chain: <i>should → should check → You should check → You should check his temperature → … regularly.</i></p>""")


def rules_modals(b):
    """A2 Unit 43: rules and choice: have to, must, can't, don't have to, can, should, be allowed to, be supposed to."""
    b.page(f"""{b.sec("+", "Grammar reference: talking about rules", "")}
<div class="box" style="margin-top:0"><h4>NECESSARY, NOT ALLOWED OR YOUR CHOICE?</h4>When we explain a game, a job or a school, we say what is <b>necessary</b>, what is <b>not allowed</b>, what is <b>not necessary</b> (your choice) and what is a <b>good idea</b>.</div>
{_h("1. THE FORMS")}
{_tbl(["meaning", "forms", "examples"], [
    ["<b>necessary</b>", "have to / has to · must", "<i>We have to take turns. It must be a real word.</i>"],
    ["<b>not allowed</b>", "can't · not allowed to · not supposed to", "<i>You can't say that. You're not allowed to give a clue. You're not supposed to tell me the word.</i>"],
    ["<b>not necessary</b> (you can choose)", "don't have to / doesn't have to", "<i>You don't have to wait to make a guess.</i>"],
    ["<b>allowed / possible</b>", "can · be allowed to", "<i>Can I say that? You're allowed to ask for a little help.</i>"],
    ["<b>a good idea</b> (advice)", "should / shouldn't", "<i>You should explain that rule at the beginning.</i>"]], "8.5pt")}
{_h("2. GRAMMAR")}
<ul class="small" style="margin:.5mm 0;line-height:1.5"><li><b>must, can, can't, should</b> + base form (no <i>to</i>, no <i>-s</i>): <i>He must say a letter.</i></li>
<li><b>have to, be allowed to, be supposed to</b> + <b>to</b> + base form, and they change: <i>She <b>has</b> to… · You'<b>re</b> not allowed to… · They <b>were</b> supposed to…</i></li>
<li><b>be supposed to</b> = the rule or what people expect (but people don't always follow it): <i>You're supposed to keep the word secret.</i></li></ul>
{_h("3. BIG DIFFERENCE: MUSTN'T vs DON'T HAVE TO")}
{_tbl(["can't / mustn't", "don't have to"], [["= it's not allowed: <i>You can't use your phone.</i>", "= it's not necessary, but you can if you want: <i>You don't have to start with A.</i>"]], "8.6pt")}
<p class="small" style="margin:.5mm 0"><b>Pronunciation:</b> <i>have to</i> /ˈhæftə/, <i>has to</i> /ˈhæstə/, <i>supposed to</i> /səˈpoʊstə/ (the d is silent), <i>allowed</i> /əˈlaʊd/.</p>
{_dont([("You must to wait.", "You must <b>wait</b>."), ("She have to choose a word.", "She <b>has</b> to choose a word."), ("You don't have to cheat! (not allowed)", "You <b>can't</b> cheat!"), ("You're not allow to look.", "You're not <b>allowed</b> to look."), ("You're suppose to listen.", "You're suppos<b>ed</b> to listen.")])}""",
    25, """<p>The key confusion: <i>don't have to</i> looks like "not allowed" to Brazilians (the direct translation into Portuguese can mean both). Make the student say the meaning out loud: necessary? not allowed? your choice? Also watch <i>allow / allowed</i> and <i>suppose / supposed</i> (the -ed is written but hard to hear).</p>""")


def purpose_method(b):
    """A2 Unit 44: purpose and method: to / in order to + base form, for + noun, by + verb-ing, because + clause."""
    b.page(f"""{b.sec("+", "Grammar reference: explaining how and why", "")}
<div class="box" style="margin-top:0"><h4>THE RESULT YOU WANT, HOW TO GET IT, AND WHY</h4>A life hack has two parts: the <b>result</b> you want (<i>white sneakers</i>) and <b>how</b> to get it (<i>use toothpaste</i>). Sometimes we also say <b>why</b> it works (<i>because…</i>).</div>
{_h("1. THE RESULT YOU WANT (PURPOSE)")}
{_tbl(["form", "grammar", "examples"], [
    ["<b>to</b>", "to + base form", "<i>Paint your sneakers with beeswax <b>to make</b> them waterproof.</i>"],
    ["<b>in order to</b>", "in order to + base form (more formal)", "<i><b>In order to remove</b> bad smells, put tea bags in your shoes.</i>"],
    ["<b>for</b>", "for + noun phrase", "<i><b>For super white sneakers</b>, use toothpaste.</i>"]], "8.5pt")}
{_h("2. HOW TO GET IT (METHOD)")}
{_tbl(["form", "grammar", "examples"], [
    ["<b>by</b>", "by + verb-ing", "<i>Keep your socks together <b>by putting</b> them in a mesh bag.</i>"]], "8.5pt")}
{_h("3. WHY (REASON)")}
{_tbl(["form", "grammar", "examples"], [
    ["<b>because</b>", "because + subject + verb", "<i>This works <b>because the ice melts</b> and turns into steam.</i>"]], "8.5pt")}
<p class="small" style="margin:.8mm 0"><b>Word order and commas:</b> result first → comma: <i>To fix a zipper, use a pencil.</i> · how first → no comma: <i>Use a pencil to fix a zipper.</i><br>
<b>for</b> + noun, never for + verb: <i>I came here <b>to learn</b> English.</i> ✗ <i>for learn</i> · <b>to</b> answers "Why?": <i>Why did you go to the store? <b>To buy</b> tea bags.</i></p>
{_dont([("I came here for learn English.", "I came here <b>to learn</b> English."), ("Clean it by use a toothbrush.", "Clean it by <b>using</b> a toothbrush."), ("For to fix a zipper, use a candle.", "<b>To</b> fix a zipper, use a candle."), ("I study English for get a better job.", "I study English <b>to get</b> a better job."), ("It works because of the ice melts.", "It works <b>because</b> the ice melts.")])}""",
    20, """<p>The most common Brazilian mistake in this area is <i>for</i> + verb (<i>for learn, for get</i>), because Portuguese uses one word for both purpose and benefit. Drill: <i>Why are you studying English? To…</i></p>""")


def passive_present(b):
    """A2 Unit 45: present simple passive: am/is/are + past participle; by + agent; active vs passive; irregular participles."""
    b.page(f"""{b.sec("+", "Grammar reference: the passive (present simple)", "")}
<div class="box" style="margin-top:0"><h4>ACTIVE OR PASSIVE?</h4><b>Active:</b> the subject does the action: <i><b>Marlon</b> creates the models.</i> <b>Passive:</b> the subject receives the action: <i><b>The models</b> are created.</i> We use the passive when the action is more important than who does it, or when we don't know or don't care who does it.</div>
{_h("1. FORM: AM / IS / ARE + PAST PARTICIPLE")}
{_tbl(["", "singular", "plural"], [
    ["<b>positive</b>", "<i>The game <b>is tested</b>.</i>", "<i>The videos <b>are made</b>.</i>"],
    ["<b>negative</b>", "<i>The budget <b>isn't agreed</b> yet.</i>", "<i>The bugs <b>aren't found</b> easily.</i>"],
    ["<b>question</b>", "<i><b>Is</b> the game <b>tested</b> by players?</i>", "<i>How <b>are</b> the videos <b>made</b>?</i>"]], "8.5pt")}
{_h("2. ACTIVE → PASSIVE")}
{_tbl(["active", "passive"], [
    ["<i>Annie <b>produces</b> the artwork.</i>", "<i>The artwork <b>is produced</b> (by Annie).</i>"],
    ["<i>Lots of people <b>test</b> the game.</i>", "<i>The game <b>is tested</b> by lots of people.</i>"]], "8.5pt")}
<p class="small" style="margin:.8mm 0">The object of the active sentence becomes the subject of the passive. Use <b>by</b> + person only when it's important or interesting.<br>
<b>Processes</b> and <b>formal texts</b> often use the passive: <i>First the coffee beans <b>are picked</b>. Then they <b>are dried</b> in the sun…</i></p>
{_h("3. PAST PARTICIPLES")}
<p class="small" style="margin:.5mm 0"><b>regular:</b> agree → agreed, test → tested, record → recorded · <b>irregular:</b> choose → <b>chosen</b>, find → <b>found</b>, make → <b>made</b>, put → <b>put</b>, write → <b>written</b>, build → <b>built</b>, send → <b>sent</b>, take → <b>taken</b></p>
{_dont([("The game is test by players.", "The game is <b>tested</b> by players."), ("The videos is made.", "The videos <b>are</b> made."), ("The budget agreed first.", "The budget <b>is</b> agreed first."), ("The artwork is produced for Annie.", "The artwork is produced <b>by</b> Annie."), ("The target audience is choosed.", "The target audience is <b>chosen</b>.")])}""",
    20, """<p>Brazilians often forget <i>be</i> (<i>The budget agreed</i>), use the base form instead of the participle (<i>is test</i>), or use <i>for</i> instead of <i>by</i>. Only the present simple passive is practiced here; other tenses come at B1.</p>""")


def phrasal_verbs(b):
    """A2 Unit 46: phrasal verbs: form, meaning, grammar; four types; separable with pronouns."""
    b.page(f"""{b.sec("+", "Grammar reference: phrasal verbs", "")}
<div class="box" style="margin-top:0"><h4>VERB + PARTICLE</h4>A <b>phrasal verb</b> is a verb + a <b>particle</b> (a small word like <i>up, out, at, in, down, on</i>). The meaning is often different from the verb alone: <i>pick</i> (choose) → <i>pick up</i> (go and get) → <i>pick at</i> (eat very little). Learn three things: the <b>form</b>, the <b>meaning</b> and the <b>grammar</b>.</div>
{_h("1. FOOD PHRASAL VERBS FROM THIS UNIT")}
{_tbl(["phrasal verb", "meaning", "example"], [
    ["<b>eat out</b>", "have a meal in a restaurant", "<i>We eat out on special occasions.</i>"],
    ["<b>pick up</b>", "go and get something quickly", "<i>I'll pick up some takeout.</i>"],
    ["<b>pig out</b> (informal)", "eat a lot", "<i>We always pig out at Grandma's.</i>"],
    ["<b>pick at</b>", "eat very little, without enjoying it", "<i>She picked at her salad.</i>"],
    ["<b>cut down on</b> / <b>give up</b>", "use less of / stop completely", "<i>I'm cutting down on sugar. He gave up meat.</i>"],
    ["<b>heat up</b> / <b>turn up</b>", "make hot / make stronger", "<i>Heat up the soup. Turn up the heat.</i>"],
    ["<b>cut up</b> / <b>mix in</b>", "cut into small pieces / add and mix", "<i>Cut up the strawberries and mix them in.</i>"]], "8.2pt")}
{_h("2. FOUR TYPES")}
{_tbl(["type", "grammar", "examples"], [
    ["1 no object", "verb + particle", "<i>Let's eat out. We pigged out.</i>"],
    ["2 object, can't separate", "verb + particle + object", "<i>Don't pick at your food.</i> ✗ <i>pick your food at</i>"],
    ["3 object, can separate", "verb + object + particle / verb + particle + object", "<i>Cut up the onions. / Cut the onions up.</i>"],
    ["4 three parts", "verb + 2 particles + object", "<i>I'm cutting down on snacks.</i>"]], "8.2pt")}
<p class="small" style="margin:.8mm 0"><b>Pronouns with type 3:</b> you <b>must</b> separate: <i>Cut <b>them</b> up.</i> ✗ <i>Cut up them.</i> · <i>Heat <b>it</b> up.</i> ✗ <i>Heat up it.</i><br>
Not sure if it separates? Put the noun <b>after</b> the particle: <i>I gave up chocolate.</i> That order is always safe with a noun.</p>
{_dont([("Heat up it, please.", "Heat <b>it</b> up, please."), ("Mix in them.", "Mix <b>them</b> in."), ("Let's eat up tonight.", "Let's eat <b>out</b> tonight."), ("I'm cutting down sugar.", "I'm cutting down <b>on</b> sugar."), ("Stop picking your food at.", "Stop picking <b>at</b> your food.")])}""",
    25, """<p>Phrasal verbs are very common in spoken and informal written American English. Encourage the student to keep a phrasal verb notebook with three columns: form, meaning, example sentence. A good learner's dictionary shows if a phrasal verb separates.</p>""")


def question_forms(b):
    """A2 Unit 47: questions in all tenses: do/does/did in simple forms, inversion with be/have/will/would/going to, subject questions, intonation."""
    b.page(f"""{b.sec("+", "Grammar reference: making questions", "")}
<div class="box" style="margin-top:0"><h4>QUESTION WORD + AUXILIARY + SUBJECT + VERB</h4>Most English questions follow this order: <b>(question word) + auxiliary + subject + main verb</b>. The auxiliary changes with the tense.</div>
{_h("1. SIMPLE FORMS: ADD DO / DOES / DID")}
{_tbl(["tense", "question", "auxiliary"], [
    ["present simple", "<i>How many rings <b>does</b> Saturn <b>have</b>?</i>", "do / does + base form"],
    ["past simple", "<i>When <b>did</b> the last dodo <b>die</b>?</i>", "did + base form"],
    ["used to", "<i>What <b>did</b> people <b>use to</b> believe?</i>", "did + use to (no -d)"]], "8.5pt")}
{_h("2. MULTI-WORD FORMS: CHANGE THE ORDER")}
{_tbl(["tense", "statement", "question"], [
    ["present continuous", "<i>The Earth <b>is</b> moving.</i>", "<i>How fast <b>is</b> the Earth moving?</i>"],
    ["present perfect", "<i>They <b>have</b> sent robots.</i>", "<i>Where <b>have</b> they sent robots?</i>"],
    ["will (prediction)", "<i>It <b>will</b> approach Earth.</i>", "<i>When <b>will</b> it approach Earth?</i>"],
    ["going to (plan)", "<i>It<b>'s</b> going to travel to Titan.</i>", "<i>Where <b>is</b> it going to travel?</i>"],
    ["second conditional", "<i>They <b>would</b> weigh 20 pounds.</i>", "<i>What <b>would</b> they weigh?</i>"]], "8.5pt")}
{_h("3. SUBJECT QUESTIONS: NO AUXILIARY")}
<p class="small" style="margin:.5mm 0">When <b>who, what</b> or <b>which</b> is the subject, use statement word order: <i><b>Who discovered</b> the galaxies?</i> (Hubble discovered them.) · <i><b>Which country is going to send</b> people to Mars?</i> Compare: <i>Who <b>did</b> Hubble <b>work</b> with?</i> (object question)</p>
<p class="small" style="margin:.5mm 0"><b>Intonation:</b> yes/no questions usually go <b>up</b> ↗ (<i>Are you ready?</i>); wh- questions usually go <b>down</b> ↘ (<i>Where do you live?</i>).</p>
{_dont([("How many rings Saturn has?", "How many rings <b>does</b> Saturn <b>have</b>?"), ("Who did discover the galaxies?", "Who <b>discovered</b> the galaxies?"), ("Where you are going?", "Where <b>are you</b> going?"), ("Did you used to play?", "Did you <b>use</b> to play?"), ("What will it to do?", "What will it <b>do</b>?")])}""",
    20, """<p>Portuguese makes many questions with intonation only, so Brazilians often keep statement order (<i>Where you live?</i>) or add <i>did</i> to subject questions. Drill a few questions in each tense and keep the intonation rule.</p>""")
