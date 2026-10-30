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
