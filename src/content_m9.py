"""
content_m9.py — Module 9: Prop-Firm Risk Management.
Exposes build() -> str (the <main> body HTML for module-09.html).
"""
import os
from sitegen import (
    h2, h3, p, chart, look, key, warn, dev, defn, table, flow, prac, pre,
    summary, split, quiz,
)

_IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")


def img(name):
    return os.path.join(_IMG_DIR, name)


def build():
    out = []

    # ------------------------------------------------------------------
    # 9.0 Introduction
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "Every module so far has produced structurally qualified trades. This module governs whether "
        "there is still an account left to trade them with next week. Prop-firm risk management is not "
        "an add-on to the strategy \u2014 it is the layer that determines whether a positive-expectancy "
        "system (Module 1) ever gets enough trades to express that edge before a single rule violation "
        "ends the account."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Calculate position size from a structural stop distance and a fixed percentage risk, for any "
        "account size.",
        "Apply a daily loss limit and stop trading before it is breached, not after.",
        "Explain max drawdown and design a pre-committed risk-reduction rule for consecutive losses.",
        "Identify correlated exposure across nominally separate positions and size it as one risk, not "
        "several.",
        "Treat scheduled news/event risk as an exposure problem, not a position-sizing problem.",
        "Recognise overtrading and revenge trading in an equity curve and name the discipline that "
        "prevents both.",
        "Explain why no single risk-per-trade percentage is appropriate across every prop firm.",
    ]))

    out.append(warn("Prerequisite", [
        "This module assumes Module 6's stop-loss and R:R mechanics (a structural stop is a fixed "
        "distance, never chosen to fit a desired risk percentage) and Module 8's stand-aside conditions "
        "(unusual volatility, scheduled news, correlated over-concentration). This module turns those "
        "qualitative warnings into worked, numeric risk controls."
    ]))

    # ------------------------------------------------------------------
    # 9.1 Position sizing from a structural stop
    # ------------------------------------------------------------------
    out.append(h2("9.1", "Position sizing: solved backward from risk"))
    out.append(key("The sizing formula",
        "Position size is never chosen first. The structural stop distance (Module 6, \u00a76.2) and the "
        "fixed risk percentage are the two independent inputs; the lot size is the output that makes the "
        "dollar risk come out exactly right:<br><br>"
        "<code>Lots = (Account balance \u00d7 Risk %) \u00f7 (Stop distance in pips \u00d7 Pip value per lot)</code>"
    ))
    out.append(chart(img("m9_sizing_by_stop.png"),
        "Figure 9.1 \u2014 Same $25,000 account, same 1.00% risk per trade, three different structural "
        "stop distances. Dollar risk at stake never changes \u2014 only the lot size solves for it, larger "
        "on the tight stop and smaller on the wide one."))
    out.append(table(
        ["Input", "Where it comes from", "Never do this"],
        [
            ["Stop distance", "The structural invalidation point identified in Module 6, \u00a76.2 \u2014 a "
             "property of the chart", "Never widen or narrow it to produce a preferred lot size"],
            ["Risk percentage", "A number fixed in advance by the trader's own rules and the specific "
             "prop firm's limits (\u00a79.7)", "Never raise it because a setup \u201cfeels\u201d stronger than "
             "usual"],
            ["Lot size", "Calculated from the two inputs above", "Never chosen first and then used to "
             "back into a stop distance"],
        ]
    ))

    # ------------------------------------------------------------------
    # 9.2 Daily loss limits
    # ------------------------------------------------------------------
    out.append(h2("9.2", "Daily loss limits"))
    out.append(p(
        "Most prop firms define a maximum loss permitted within a single trading day, expressed as a "
        "percentage of account balance or of the starting-of-day equity. The discipline is to stop "
        "trading once the cumulative loss for the day comes within one trade's worth of risk of that "
        "limit \u2014 not to keep trading until the limit is actually touched or breached."
    ))
    out.append(chart(img("m9_daily_loss_limit.png"),
        "Figure 9.2 \u2014 Five trades against a -3.0% daily loss limit. After trade 4, cumulative loss "
        "sits at -2.4% \u2014 one more full loss would breach the limit. Trading stops for the day at this "
        "point, regardless of how good the next setup looks."))
    out.append(warn("The limit is a stopping rule, not a target", [
        "A daily loss limit exists to prevent a single bad day from becoming an account-ending one. "
        "Treating it as a number to approach and then trade right up against \u2014 rather than a hard "
        "stopping point with a safety margin \u2014 defeats its purpose. The correct discipline stops with "
        "room to spare, not exactly at the line."
    ]))

    # ------------------------------------------------------------------
    # 9.3 Max drawdown and consecutive-loss risk reduction
    # ------------------------------------------------------------------
    out.append(h2("9.3", "Max drawdown and consecutive-loss risk reduction"))
    out.append(defn("Max drawdown",
        "The largest peak-to-trough decline in account equity a prop firm will tolerate before the "
        "account is closed, usually expressed as a percentage of either the initial balance or the "
        "highest equity the account has reached (a \u201chigh-water mark\u201d)."))
    out.append(p(
        "A losing streak is normal even for a positive-expectancy system (Module 1) \u2014 a 35% win rate "
        "at 1:2 R:R will produce strings of consecutive losses regularly. What separates a survivable "
        "streak from an account-ending one is whether risk per trade is reduced by a pre-committed rule "
        "as the streak develops, rather than left fixed or, worse, increased to \u201cwin it back\u201d "
        "(\u00a79.6)."
    ))
    out.append(chart(img("m9_drawdown_reduction.png"),
        "Figure 9.3 \u2014 Left: risk stays fixed at 1.0% through six consecutive losses, consuming the "
        "full 6% drawdown allowance. Right: the same six-loss streak, but risk is halved to 0.5% after "
        "the third consecutive loss by a rule written in advance \u2014 the drawdown decelerates instead of "
        "accelerating."))
    out.append(table(
        ["Element", "Written in advance", "Decided during the streak"],
        [
            ["Trigger", "\u201cAfter N consecutive losses, cut risk by X%\u201d, a specific number chosen "
             "before trading begins", "\u201cThis feels like a bad stretch, I should probably size down\u201d"],
            ["Reliability", "Applied identically every time the trigger condition is met",
             "Applied inconsistently depending on mood, fatigue, or how the losses felt"],
            ["Reversibility", "A pre-defined rule for returning to full risk (e.g. after 2 wins) is also "
             "written in advance", "No defined point to return to full size, risk stays arbitrarily small "
             "or arbitrarily large"],
        ]
    ))

    out.append(quiz(
        "A trader's written rule states: \u201cReduce risk per trade from 1.0% to 0.5% after 3 consecutive "
        "losses; return to 1.0% after 2 consecutive wins.\u201d After 2 consecutive losses, the trader feels "
        "uneasy and manually cuts risk to 0.3% for the next trade, then returns to 1.0% after that one "
        "trade wins. Does this comply with \u00a79.3's risk-reduction discipline?",
        [
            {"label": "Yes \u2014 reducing risk after losses is always the cautious, correct choice "
             "regardless of when it happens.",
             "correct": False,
             "feedback": "<p><strong>Caution alone does not make an action compliant with a written "
                         "rule.</strong> \u00a79.3 is explicit that the value of a risk-reduction rule comes "
                         "from being applied identically every time its specific trigger condition is met "
                         "\u2014 not from any reduction in risk happening to feel prudent in the moment. "
                         "Deviating from the written trigger (2 losses instead of 3, 0.3% instead of 0.5%, "
                         "return after 1 win instead of 2) breaks the very consistency the rule exists to "
                         "provide.</p>"},
            {"label": "No \u2014 the trigger point, the reduced size, and the return condition all "
             "deviated from what was written in advance, which defeats the purpose of having a "
             "pre-committed rule.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a79.3's table is explicit that a risk-reduction "
                         "rule's value comes from being written in advance and applied identically \u2014 not "
                         "from being adjusted in the moment based on how a streak feels. Cutting at 2 losses "
                         "instead of 3, to 0.3% instead of 0.5%, and returning after 1 win instead of 2 are "
                         "each an ad hoc deviation, indistinguishable in principle from the reactive sizing "
                         "\u00a79.6 warns against \u2014 even though this particular deviation happened to "
                         "reduce risk rather than increase it.</p>"},
            {"label": "It cannot be assessed without knowing whether the trade that followed won or "
             "lost.",
             "correct": False,
             "feedback": "<p><strong>The outcome of the following trade is irrelevant to whether the "
                         "rule was followed.</strong> \u00a79.3 evaluates compliance by whether the written "
                         "trigger, size, and return conditions were respected \u2014 not by whether the "
                         "deviation happened to work out. A rule that is only followed when convenient "
                         "provides none of the discipline it is meant to enforce.</p>"},
        ],
        hint="Compare exactly what was written in advance against exactly what was done \u2014 trigger "
             "point, reduced size, and return condition."
    ))

    # ------------------------------------------------------------------
    # 9.4 Correlation and max simultaneous exposure
    # ------------------------------------------------------------------
    out.append(h2("9.4", "Correlation risk and max simultaneous exposure"))
    out.append(p(
        "Two or more positions can each individually satisfy the 13-step entry sequence (Module 4) and "
        "each carry an individually correct 1.0% risk, while together representing far more than the sum "
        "of their nominal risk \u2014 because they depend on the same underlying driver moving the same "
        "way."
    ))
    out.append(chart(img("m9_correlation_exposure.png"),
        "Figure 9.4 \u2014 Three separate tickets, each individually risking 1.0% by its own stop-loss "
        "math. All three actually depend on one underlying view \u2014 USD weakness against EUR/GBP \u2014 so "
        "a single USD-strength reversal moves all three against the trader at once. Nominal risk reads "
        "3.0%; real correlated exposure behaves like a single 3.0% USD-direction bet."))
    out.append(table(
        ["Correlated grouping", "Why they move together"],
        [
            ["EURUSD long + GBPUSD long", "Both are effectively short USD; a broad USD-strength move "
             "hits both simultaneously"],
            ["Multiple equity index futures long (e.g. ES, NQ) at once", "Both driven heavily by "
             "broad market risk sentiment, not independent instrument-specific structure"],
            ["EURUSD long + EURGBP long", "Both are effectively long EUR; a EUR-specific move affects "
             "both"],
        ]
    ))
    out.append(warn("Max simultaneous exposure is a portfolio-level rule", [
        "This system's entry sequence evaluates one instrument at a time. A separate, portfolio-level "
        "check is required before adding a second or third position: does this new position share its "
        "underlying driver with anything already open? If so, size the group as a single position for "
        "risk purposes, not as independent 1.0% risks stacked on top of each other."
    ]))

    out.append(quiz(
        "A trader already holds a EURUSD long risking 1.0%. A new setup on GBPUSD long independently "
        "satisfies all 13 steps of the Module 4 entry sequence with an honest 1:2.3 R:R. The trader's "
        "written plan permits up to 3.0% of total correlated exposure per underlying driver. Taking the "
        "GBPUSD trade at its own calculated 1.0% risk would bring nominal risk to 2.0%. What is the "
        "correct assessment?",
        [
            {"label": "Take it at 1.0% \u2014 nominal risk of 2.0% is comfortably under any reasonable "
             "daily loss limit.",
             "correct": False,
             "feedback": "<p><strong>Comparing nominal risk to the daily loss limit skips the "
                         "correlation step entirely.</strong> \u00a79.4 is explicit that EURUSD long and "
                         "GBPUSD long are both effectively short-USD positions that move together under a "
                         "broad USD-strength reversal. The relevant comparison is real correlated exposure "
                         "against the 3.0% per-driver limit, not nominal risk against the daily loss "
                         "limit.</p>"},
            {"label": "Evaluate the combined correlated exposure against the shared USD driver before "
             "sizing \u2014 if the two positions' combined risk to a single USD move already approaches the "
             "3.0% per-driver limit, size the new position down accordingly rather than adding a full "
             "independent 1.0%.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a79.4's warning box is explicit that a "
                         "portfolio-level check is required before adding a correlated position: does the "
                         "new trade share its underlying driver with something already open? Here, both "
                         "positions are effectively short-USD, so they must be sized as a single combined "
                         "risk against the 3.0% per-driver limit \u2014 not stacked as two independent 1.0% "
                         "risks that happen to sum to a number under the daily loss limit.</p>"},
            {"label": "Skip the GBPUSD trade entirely \u2014 no two positions should ever be open on "
             "different instruments at the same time.",
             "correct": False,
             "feedback": "<p><strong>\u00a79.4 does not prohibit multiple simultaneous positions "
                         "outright.</strong> It requires evaluating whether they share an underlying "
                         "driver and, if so, sizing the group as one combined risk against the per-driver "
                         "limit. Two positions with genuinely independent drivers can both be held at "
                         "their own full calculated size.</p>"},
        ],
        hint="Check \u00a79.4's table \u2014 do EURUSD long and GBPUSD long share an underlying driver, and "
             "what limit governs that shared exposure?"
    ))

    # ------------------------------------------------------------------
    # 9.5 News/event risk
    # ------------------------------------------------------------------
    out.append(h2("9.5", "News and event risk"))
    out.append(p(
        "Module 8 (\u00a78.7) already established that major scheduled news makes structure temporarily "
        "unreliable. The risk-management implication goes further: a stop-loss order does not guarantee "
        "its stated fill price during a scheduled-release gap, so reducing position size does not "
        "actually fix the exposure \u2014 it only makes a still-unpriced gap smaller in dollar terms."
    ))
    out.append(chart(img("m9_news_event_risk.png"),
        "Figure 9.5 \u2014 A stop-loss order does not guarantee this fill price during a scheduled-release "
        "gap. Position sizing cannot price this kind of risk; the correct control is being flat or "
        "materially reduced ahead of the release, not simply smaller."))
    out.append(table(
        ["Wrong response to news risk", "Correct response"],
        [
            ["Keep the same position but risk only 0.5% instead of 1.0%", "The gap can still exceed the "
             "reduced size's effective stop by a wide margin \u2014 sizing down does not cap the risk"],
            ["Widen the stop to \u201cabsorb\u201d the expected volatility", "This changes the trade's R:R "
             "math without changing the actual gap risk, and contradicts Module 6's structural-stop rule"],
            ["Close or materially reduce the position ahead of the scheduled release", "Removes or "
             "shrinks the exposure to the event itself, rather than trying to price an unpriceable gap"],
        ]
    ))

    # ------------------------------------------------------------------
    # 9.6 Overtrading and revenge trading
    # ------------------------------------------------------------------
    out.append(h2("9.6", "Overtrading and revenge trading"))
    out.append(p(
        "Module 8 (\u00a78.8) named these as psychological patterns. Here they are shown as what they do "
        "to an equity curve directly: overtrading adds trades that never should have passed the Module 4 "
        "sequence, and revenge trading increases size specifically because of a prior loss rather than "
        "because of anything the chart is showing."
    ))
    out.append(chart(img("m9_overtrading_curve.png"),
        "Figure 9.6 \u2014 Left: risk stays at the pre-defined 1.0% regardless of outcome; two losses in a "
        "row do not change the size of the third trade. Right: risk is doubled and then tripled after "
        "losses specifically to \u201cwin it back\u201d \u2014 one bad trade at the escalated size erases the "
        "prior gain and drives the account below where it started."))
    out.append(key("The test that catches both",
        "Before increasing size on any trade, ask: is this larger size justified by something the chart "
        "is showing right now (a higher-conviction structural setup that independently qualifies under "
        "Module 4), or is it justified by wanting to recover a prior loss faster? Only the first answer "
        "is legitimate \u2014 and even then, sizing changes should follow a pre-written rule (\u00a79.3), not "
        "an in-the-moment decision."
    ))

    out.append(quiz(
        "After two consecutive losing trades, a trader identifies a new setup that independently "
        "satisfies all 13 steps of the Module 4 entry sequence with an honest 1:2.5 R:R. Their written "
        "risk plan calls for 1.0% per trade with no reduction until 3 consecutive losses. Wanting to "
        "recover the prior losses faster, the trader risks 2.0% instead. What is the correct assessment?",
        [
            {"label": "Acceptable \u2014 the setup is genuinely strong, with an R:R well above the 1:2 "
             "minimum, which justifies the larger size.",
             "correct": False,
             "feedback": "<p><strong>A qualifying R:R above 1:2 does not itself justify departing from "
                         "the written risk plan.</strong> \u00a79.6's test is explicit: a size increase is "
                         "legitimate only when it follows a pre-written rule tied to something the chart "
                         "shows, not a reaction to wanting to recover a prior loss. The trader's own "
                         "stated motive here \u2014 recovering the losses faster \u2014 is precisely the "
                         "revenge-trading pattern \u00a79.6 describes.</p>"},
            {"label": "This is revenge trading \u2014 the size increase is motivated by recovering the "
             "prior losses, not by a pre-written rule, even though the setup itself qualifies.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a79.6's key test asks whether a larger size is "
                         "justified by the chart under a pre-written rule, or by wanting to recover a "
                         "prior loss. The setup qualifying under Module 4 does not change the answer: the "
                         "size increase itself was motivated by the two prior losses, and the trader's own "
                         "written plan calls for no reduction (let alone an increase) until 3 consecutive "
                         "losses. The correct action was to take the trade at the plan's normal 1.0%.</p>"},
            {"label": "It cannot be judged until the outcome of this trade is known.",
             "correct": False,
             "feedback": "<p><strong>The outcome of the trade does not change whether the sizing decision "
                         "was correct.</strong> \u00a79.6 evaluates the decision at the moment it was made: "
                         "was the size increase justified by the written plan, or by a reaction to prior "
                         "losses? A winning outcome afterward would not retroactively make the reasoning "
                         "sound.</p>"},
        ],
        hint="Apply \u00a79.6's key test: was the larger size justified by the written plan and the chart, "
             "or by wanting to recover the prior losses?"
    ))

    # ------------------------------------------------------------------
    # 9.7 No universal risk level
    # ------------------------------------------------------------------
    out.append(h2("9.7", "No universal risk level across prop firms"))
    out.append(chart(img("m9_no_universal_risk.png"),
        "Figure 9.7 \u2014 Three illustrative prop-firm rule sets. Identical 1.0% per-trade risk consumes "
        "a very different fraction of each firm's own daily loss limit and consecutive-loss buffer \u2014 "
        "the correct percentage is derived from the specific firm's actual rules, never copied from "
        "another firm or from a generic \u201c1% rule.\u201d"))
    out.append(warn("This module names no single \u201ccorrect\u201d percentage", [
        "Every number in this module (1.0% per trade, 3.0% daily limit, 6% max drawdown) is illustrative "
        "\u2014 chosen to make the arithmetic in the figures concrete, not presented as a recommendation "
        "for any specific account. Before trading a specific prop-firm account, the trader's risk "
        "percentage must be derived from that firm's own published daily loss limit, max drawdown rule, "
        "and any scaling or consistency requirements \u2014 checked directly against the firm's current "
        "rules, not assumed from this or any other course."
    ]))

    # ------------------------------------------------------------------
    # 9.8 Instrument / session caveats
    # ------------------------------------------------------------------
    out.append(h2("9.8", "Instrument and session caveats"))
    out.append(table(
        ["Instrument / session", "Risk-management notes"],
        [
            ["EURUSD, London 07:00\u201311:00 UK",
             "Pip values on standard/mini/micro lots are straightforward in USD-quoted pairs; sizing "
             "arithmetic is simple, but tight structural stops (8\u201315 pips) mean small stop-distance "
             "errors move lot size proportionally more than on a wider-stop instrument."],
            ["GBPUSD, London/NY overlap 13:00\u201316:00 UK",
             "Wider typical stops (15\u201325 pips) and higher volatility both argue for treating this pair "
             "as carrying more correlation risk with other GBP or USD pairs traded the same session."],
            ["ES / NQ, NY cash 09:30\u201316:00 ET",
             "Point value per contract is fixed by the exchange, not calculated like forex pip value; "
             "position sizing must use the contract's actual dollar-per-point figure, and ES/NQ held "
             "simultaneously should be treated as highly correlated (\u00a79.4)."],
            ["Any instrument, prop-firm evaluation phase",
             "Some firms apply stricter daily-loss or consistency rules during an evaluation than on a "
             "funded account \u2014 confirm which rule set is active before sizing, since applying a funded "
             "account's more permissive numbers during an evaluation can breach the evaluation's own "
             "rules."],
        ]
    ))

    # ------------------------------------------------------------------
    # 9.9 Practicals
    # ------------------------------------------------------------------
    out.append(h2("9.9", "Practicals"))
    out.append(prac(
        "9.1", "The Sizing Worksheet",
        "A hands-on drill to make position sizing automatic rather than approximate.",
        "<ol>"
        "<li>For your next 10 trades (real or simulated), write down the structural stop distance in "
        "pips/points before entry, then calculate the exact lot/contract size using \u00a79.1's formula "
        "against your fixed risk percentage.</li>"
        "<li>Compare the calculated size to whatever size you would have picked \u201cby feel.\u201d Note any "
        "gap and what caused it (rounding, a forgotten pip-value figure, an urge to round up).</li>"
        "<li>After 10 trades, confirm that realized dollar risk across all 10 stayed within a tight band "
        "of the intended risk percentage \u2014 large variance indicates a sizing-process problem worth "
        "fixing before trading larger size.</li>"
        "</ol>"
    ))
    out.append(prac(
        "9.2", "The Correlation and Streak Audit",
        "A weekly review drill covering \u00a79.3 and \u00a79.4 together.",
        "<ol>"
        "<li>At the end of each trading week, list every position that was open simultaneously with "
        "another position, and identify whether they shared an underlying driver (\u00a79.4's table).</li>"
        "<li>For any week containing 3 or more consecutive losses, check whether your written "
        "risk-reduction rule (\u00a79.3) was actually applied at the correct trigger point, with the "
        "correct reduced size, and the correct return condition.</li>"
        "<li>Log any deviation from either rule, however small, and write down specifically what caused "
        "it \u2014 this is the same discipline the quiz in \u00a79.3 tests.</li>"
        "</ol>"
    ))

    # ------------------------------------------------------------------
    # 9.10 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("9.10", "Vocabulary introduced in this module"))
    out.append(table(
        ["Term", "Definition"],
        [
            ["Position sizing", "Calculating the lot/contract size that makes the dollar risk on a trade "
             "equal a fixed percentage of account balance, given a specific structural stop distance."],
            ["Daily loss limit", "A prop firm's maximum permitted cumulative loss within a single "
             "trading day, expressed as a percentage of balance or starting-of-day equity."],
            ["Max drawdown", "The largest peak-to-trough decline in account equity a prop firm will "
             "tolerate before closing the account."],
            ["Consecutive-loss risk reduction", "A pre-written rule that lowers risk per trade after a "
             "specific number of consecutive losing trades, applied identically every time the trigger is "
             "met."],
            ["Correlated exposure", "Multiple nominally separate positions that in practice depend on "
             "the same underlying driver, causing their real combined risk to exceed the sum of their "
             "individually calculated risks."],
            ["Max simultaneous exposure", "A portfolio-level limit on how much correlated risk may be "
             "open at once, evaluated separately from any single instrument's own entry sequence."],
            ["News/event risk", "The risk that a stop-loss order will not fill at its stated price during "
             "a scheduled-release gap, which position sizing alone cannot price away."],
            ["Overtrading", "Taking trades that do not genuinely satisfy the entry sequence's minimum "
             "conditions, purely to remain active."],
            ["Revenge trading", "Increasing position size specifically to recover a prior loss faster, "
             "rather than because the chart independently justifies it."],
        ]
    ))

    # ------------------------------------------------------------------
    # 9.11 Summary
    # ------------------------------------------------------------------
    out.append(h2("9.11", "Summary"))
    out.append(summary([
        "Position size is always solved backward from a fixed structural stop distance and a fixed risk "
        "percentage \u2014 never chosen first.",
        "A daily loss limit is a stopping rule with a safety margin, not a target to trade up against.",
        "Max drawdown accumulates across a losing streak; a pre-written, consistently-applied "
        "consecutive-loss risk-reduction rule slows that accumulation, and a reactive one provides none "
        "of the same protection even when it happens to reduce risk.",
        "Correlated positions must be sized as a single combined risk, not as independent risks stacked "
        "on top of each other.",
        "News/event risk cannot be priced away by reducing position size; the correct control is reduced "
        "or eliminated exposure ahead of the release.",
        "Overtrading adds trades that never should have qualified; revenge trading increases size for "
        "reasons unrelated to the chart. The same written-plan discipline prevents both.",
        "No single risk-per-trade percentage is appropriate across every prop firm \u2014 it must be "
        "derived from each firm's own daily loss limit, max drawdown, and consistency rules.",
    ]))

    return "\n".join(out)
