"""
content_m6.py — Module 6: Complete Trade Execution Blueprint.
Exposes build() -> str (the <main> body HTML for module-06.html).
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
    # 6.0 Introduction
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "Everything taught in Modules 2 through 5 answers the question <em>should I be interested "
        "here?</em> This module answers a completely different question: <em>given that I am interested, "
        "exactly how do I place, size, and defend this trade?</em> The eleven-link chain below has no "
        "room for a step chosen by feel. Every stop, target, and position size is a calculation that "
        "follows from structure already identified \u2014 never a number picked because it feels right."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Walk the complete eleven-link execution chain from 4H analysis through to exit, and explain "
        "why each link depends on the one before it.",
        "Place a stop-loss strictly from structure, and explain in one sentence why an arbitrary "
        "distance chosen to hit a target risk percentage is a discipline failure, not a shortcut.",
        "Place a take-profit strictly from the nearest genuine opposing structure, and reject a "
        "target manufactured to force a better-looking ratio.",
        "Calculate position size backward from a fixed dollar risk and a structural stop distance, for "
        "any account size.",
        "Apply the 1:2 reward-to-risk minimum as a pass/fail gate, not a suggestion.",
        "Correctly cancel a setup that never confirms, and refuse to chase price that moves without "
        "confirmation.",
        "Distinguish a valid re-entry (a fresh confirmation at the same structural zone) from a chase "
        "(entering mid-move with no structural reference at all).",
    ]))

    out.append(warn("Prerequisite", [
        "This module assumes fluency with Module 2's structure vocabulary, Module 3's zone "
        "construction, Module 4's thirteen-step entry sequence, and Module 5's candlestick reliability "
        "rules. What follows is the arithmetic and decision logic that turns a qualified Module 4 setup "
        "into an actual position with a defined stop, target, and size."
    ]))

    out.append(h2("6.1", "The execution chain, in full"))
    out.append(p(
        "The Module 4 entry sequence answered whether a setup qualifies. This chain restates the same "
        "underlying logic in eleven links focused specifically on execution mechanics \u2014 what happens "
        "at and after the moment of entry."
    ))
    out.append(chart(img("m6_execution_chain.png"),
        "Figure 6.1 \u2014 Eleven links from 4H analysis to exit. Each one only makes sense given the one "
        "before it. A break anywhere in the chain means no trade, not a smaller trade."))
    out.append(table(
        ["Link", "What happens here"],
        [
            ["1\u20132. 4H analysis \u2192 1H context", "Establishes the directional environment and the "
             "immediate 1H structure inside it (Module 2)."],
            ["3\u20134. Key S&R/supply/demand \u2192 liquidity location", "Identifies the specific graded "
             "zone and the liquidity resting around it (Module 3)."],
            ["5\u20137. 15M price interaction \u2192 15M confirmation \u2192 entry", "Waits for price to reach "
             "the zone, waits for a qualifying 15M close, then places the order (Modules 4\u20135)."],
            ["8\u20139. Structural stop \u2192 structural target", "The two risk-defining numbers, both "
             "derived from structure \u2014 covered in \u00a76.2 and \u00a76.3 below."],
            ["10\u201311. Trade management \u2192 exit", "What happens between entry and exit \u2014 covered in "
             "full in Module 7. This module only defines the boundaries the trade is managed within."],
        ]
    ))

    # ------------------------------------------------------------------
    # 6.2 Stop-loss logic
    # ------------------------------------------------------------------
    out.append(h2("6.2", "Stop-loss logic"))
    out.append(key("The stop-loss rule",
        "The stop must sit beyond the structural point that invalidates the thesis. No arbitrary "
        "distance chosen to satisfy a desired risk percentage. The exact stop location must be "
        "explainable from structure and price behaviour alone \u2014 if you cannot point to the specific "
        "swing, zone edge, or liquidity level the stop sits beyond, the stop is not valid."
    ))
    out.append(p(
        "This reverses the order most new traders use. The common (wrong) sequence is: decide how much "
        "dollar risk feels comfortable, then place the stop wherever that dollar amount lands, then hope "
        "structure agrees. The correct sequence is: find the structural point that would prove the trade "
        "wrong, place the stop just beyond it, then size the position to make that distance affordable."
    ))
    out.append(chart(img("m6_stop_logic.png"),
        "Figure 6.2 \u2014 Left: the stop sits beyond the swing low the long thesis depends on, wherever "
        "that lands. Right: a 4-pip stop chosen only to look like low risk, sitting inside ordinary 15M "
        "noise well above the level that actually invalidates the trade."))
    out.append(table(
        ["Direction", "Stop reference point"],
        [
            ["Long", "Beyond (below) the swing low / liquidity sweep low that the entry's structural "
             "case depends on. If that level fails, the reason for being long no longer applies."],
            ["Short", "Beyond (above) the swing high / liquidity sweep high that the entry's structural "
             "case depends on."],
        ]
    ))
    out.append(warn("The stop distance is an output, not an input", [
        "You do not choose the stop distance. You find the structural invalidation point, and the "
        "distance from entry to that point <em>is</em> the stop distance \u2014 whatever number that "
        "happens to be. If the resulting distance makes the position size uncomfortably small for your "
        "account, the correct response is to reduce size further or skip the trade, never to move the "
        "stop closer to manufacture a bigger position."
    ]))

    # ------------------------------------------------------------------
    # 6.3 Take-profit logic
    # ------------------------------------------------------------------
    out.append(h2("6.3", "Take-profit logic"))
    out.append(key("The take-profit rule",
        "Targets must be structural \u2014 the nearest genuine opposing structural level, significant S&R "
        "zone, supply/demand zone, or meaningful liquidity objective. Do not manufacture a target to "
        "create a favourable reward-to-risk ratio. If the genuine structural target does not offer at "
        "least 1:2 relative to the structural stop, the trade should normally be considered invalid. "
        "Never widen a target merely to make the mathematics look attractive."
    ))
    out.append(chart(img("m6_target_logic.png"),
        "Figure 6.3 \u2014 Left: the target is the nearest real opposing structure, a prior swing high that "
        "has already rejected price once \u2014 R:R \u2248 1:4.3. Right: an identical stop, but the target is "
        "stretched past all real structure to force R:R \u2248 1:4.5. The extra 0.2R is manufactured, not "
        "earned, because nothing supports price reversing at that exact price."))
    out.append(p(
        "The two setups in Figure 6.3 look almost identical on paper \u2014 both clear the 1:2 minimum with "
        "room to spare. The difference is that the left target is a real level with a documented prior "
        "reaction; the right target is empty air chosen because the resulting ratio looked slightly "
        "better. Only the left trade is valid. The lesson generalises: a manufactured target is not made "
        "safe by also clearing the 1:2 minimum \u2014 the rule against manufacturing targets applies "
        "regardless of what the resulting ratio happens to be."
    ))

    out.append(quiz(
        "A long setup has a structural stop 18 pips below entry. The nearest genuine opposing structure "
        "sits only 22 pips above entry (R:R \u2248 1:1.2). No other structure exists further out. What "
        "should happen?",
        [
            {"label": "Move the target to the next visible round number 55 pips out, since that would "
             "clear 1:2.",
             "correct": False,
             "feedback": "<p><strong>This is exactly the manufactured-target error \u00a76.3 warns "
                         "against.</strong> A round number with no structural basis is not a genuine "
                         "target no matter how good the resulting ratio looks. \u00a76.3's rule is explicit: "
                         "\u201cdo NOT manufacture a target to create favourable R:R\u201d \u2014 the arithmetic "
                         "being attractive is precisely the situation the rule exists to prevent.</p>"},
            {"label": "Reject the trade \u2014 the genuine structural target does not clear the 1:2 "
             "minimum, and no further structure exists to justify a farther target.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a76.3 states plainly: if the genuine structural "
                         "target does not offer at least 1:2 relative to the structural stop, the trade "
                         "should normally be considered invalid. There is no rule that allows manufacturing "
                         "a substitute target to rescue an otherwise-failing setup. This is the same "
                         "principle as Module 4 \u00a74.8's R:R gate \u2014 rejection at this step is a normal, "
                         "frequent outcome, not a failure of analysis.</p>"},
            {"label": "Take the trade at 1:1.2 anyway, since the setup is otherwise clean.",
             "correct": False,
             "feedback": "<p><strong>An otherwise-clean setup does not override the R:R gate.</strong> "
                         "\u00a76.3 (and Module 4 \u00a74.8) treat the 1:2 minimum as close to a hard "
                         "requirement, independent of how well the rest of the sequence qualified. A clean "
                         "setup with insufficient genuine reward is still a setup to stand aside from.</p>"},
        ],
        hint="Re-read the take-profit rule in \u00a76.3 \u2014 what exactly does it say happens when the "
             "genuine target falls short of 1:2?"
    ))

    out.append(quiz(
        "A long trade's structural stop sits 14 pips below entry, at a level clearly identified from the "
        "swing low the thesis depends on. The resulting position size feels uncomfortably small relative "
        "to the trader's usual position sizes. What is the correct response?",
        [
            {"label": "Move the stop 6 pips closer to make the position size feel more normal.",
             "correct": False,
             "feedback": "<p><strong>This is the exact discipline failure \u00a76.2 names directly.</strong> "
                         "The stop-loss rule states plainly that the stop must sit beyond the structural "
                         "invalidation point, with no arbitrary distance chosen to satisfy a desired risk "
                         "feeling. Moving the stop 6 pips closer places it inside the range price can move "
                         "through as ordinary noise \u2014 well before the thesis is actually disproven \u2014 "
                         "which produces stop-outs on trades that would otherwise have worked.</p>"},
            {"label": "Keep the stop where structure places it, and accept the resulting (smaller) "
             "position size.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a76.2 is explicit that stop distance is an "
                         "output of structure, not an input chosen for comfort. \u00a76.4 reinforces this: "
                         "position size is the only variable allowed to move to accommodate risk "
                         "preferences. A structurally correct stop with a smaller position size is a "
                         "completely normal, healthy outcome \u2014 it is not a sign anything is wrong with "
                         "the trade.</p>"},
            {"label": "Skip the trade entirely, since a 14-pip stop is unusually tight.",
             "correct": False,
             "feedback": "<p><strong>Stop distance alone is not a reason to skip a trade.</strong> A "
                         "tighter stop, provided it is genuinely structural, simply means a larger position "
                         "size can be taken for the same dollar risk \u2014 it does not make the setup itself "
                         "invalid. Nothing in \u00a76.2 or \u00a76.4 treats stop tightness as disqualifying on "
                         "its own; only the target/R:R gate (\u00a76.3, \u00a76.5) and the earlier Module 4 "
                         "conditions determine whether the setup qualifies.</p>"},
        ],
        hint="Re-read which variable \u00a76.4 says is allowed to change with comfort level, and which two "
             "are not."
    ))

    # ------------------------------------------------------------------
    # 6.4 Position sizing
    # ------------------------------------------------------------------
    out.append(h2("6.4", "Position sizing"))
    out.append(p(
        "Position size is the only variable in this entire process that is allowed to change with "
        "account size. Entry, stop, and target are all fixed by structure and are identical for every "
        "trader looking at the same chart. Position size is solved backward from a fixed dollar risk and "
        "the stop distance structure has already determined."
    ))
    out.append(table(
        ["Step", "Formula"],
        [
            ["1. Decide dollar risk", "Account balance \u00d7 risk-per-trade % = dollars risked on this trade."],
            ["2. Read the stop distance", "|Entry \u2212 structural stop|, converted to pips (FX) or points "
             "(indices/futures)."],
            ["3. Read the instrument's pip/point value", "The dollar value of one pip/point per standard "
             "lot or contract, for the specific instrument and account currency."],
            ["4. Solve for size", "Position size = Dollars risked \u00f7 (Stop distance \u00d7 pip/point "
             "value per unit)."],
        ]
    ))
    out.append(chart(img("m6_position_sizing.png"),
        "Figure 6.4 \u2014 An identical EURUSD setup with a 22-pip structural stop, sized for two different "
        "account balances at two different risk percentages. Entry and stop never change; only the "
        "resulting lot size does."))
    out.append(warn("No universal risk percentage", [
        "1.00% and 0.75% are used in Figure 6.4 purely to illustrate the calculation. This system never "
        "states a single risk-per-trade percentage as universally correct. Prop firms enforce their own "
        "maximum daily loss and maximum drawdown rules, and those rules can require a substantially "
        "smaller risk-per-trade than either example above \u2014 confirm your specific firm's or personal "
        "account's rules before sizing any real position. Position sizing and prop-firm risk math are "
        "covered in full depth in Module 9."
    ]))

    # ------------------------------------------------------------------
    # 6.5 Reward-to-risk as a gate
    # ------------------------------------------------------------------
    out.append(h2("6.5", "Reward-to-risk as a pass/fail gate"))
    out.append(p(
        "This is the same 1:2 minimum from \u00a76.3, restated as what it actually is in practice: a final "
        "binary gate applied after the stop and target are both known, before the trade is placed. It is "
        "not a score to be weighed against other positive factors \u2014 a setup that fails this gate is "
        "rejected regardless of how clean every earlier step looked."
    ))
    out.append(chart(img("m6_rr_calc.png"),
        "Figure 6.5 \u2014 Two NQ setups with an identical structural stop distance. Left: the nearest "
        "genuine opposing structure sits well beyond the 1:2 minimum \u2014 qualifies. Right: the identical "
        "stop, but the nearest genuine structure sits too close, with nothing further out to justify a "
        "farther target \u2014 rejected."))
    out.append(defn("Reward-to-risk (R:R)",
        "The ratio of distance from entry to target (reward) against distance from entry to stop (risk). "
        "Expressed as 1:X, where X is the number of risk-units the target represents. A 1:2 ratio means "
        "the target is twice as far from entry as the stop is."))

    # ------------------------------------------------------------------
    # 6.6 Invalidation, cancellation, and refusing to chase
    # ------------------------------------------------------------------
    out.append(h2("6.6", "Invalidation, cancellation, and refusing to chase"))
    out.append(p(
        "Three distinct situations get confused with each other constantly, and this system treats them "
        "as three separate concepts with three separate correct responses."
    ))
    out.append(table(
        ["Situation", "What it means", "Correct response"],
        [
            ["Structural invalidation (in an open trade)",
             "A structural point the live thesis depends on has failed, independent of whether the "
             "stop-loss price has been touched (Module 4, \u00a74.5).",
             "Exit immediately, do not wait for the stop-loss price."],
            ["Trade cancellation (before entry)",
             "Price interacted with the zone (step 5) but never produced a qualifying 15M confirmation "
             "(step 6) \u2014 instead it closed straight through.",
             "No entry was ever placed. Nothing to manage or exit \u2014 simply move on."],
            ["Refusing to chase (price moves without confirmation)",
             "Price leaves the zone in the expected direction without ever producing the 15M "
             "confirmation the sequence requires.",
             "Do not enter. The move happening without you is not evidence the analysis was wrong."],
        ]
    ))
    out.append(chart(img("m6_cancellation.png"),
        "Figure 6.6 \u2014 Price interacts with a 1H demand zone but the 15M candles close straight through "
        "it without ever producing a qualifying confirmation. No entry was ever placed \u2014 the setup is "
        "cancelled, not managed."))
    out.append(chart(img("m6_no_chase.png"),
        "Figure 6.7 \u2014 Price only wicks the edge of the zone, never confirms, then runs without a "
        "trade ever being taken. The correct response was to do nothing \u2014 the absence of a 15M "
        "confirmation was itself the answer, and the subsequent move does not retroactively make waiting "
        "the wrong decision."))
    out.append(dev("Developer's-eye analogy", [
        "Trade cancellation before entry is like a build that fails its test suite before ever reaching "
        "deployment \u2014 nothing was released, so there is nothing to roll back. Structural invalidation "
        "in an open trade is like a production incident: you already shipped, and now a monitored "
        "invariant has been violated, so you roll back immediately rather than waiting for a downstream "
        "alarm (the stop-loss) to also fire. Confusing the two means either rolling back code that was "
        "never deployed, or waiting for the loudest possible alarm before responding to an incident "
        "you've already detected."
    ]))

    out.append(quiz(
        "A trader was watching a 1H demand zone for a long. Price wicked the very edge of the zone once "
        "but never closed back inside it on the 15M, then ran 40 pips higher without them. Ten minutes "
        "later, price is now consolidating well above the original zone, with no new zone underneath it. "
        "Should the trader enter now to \u201ccatch up\u201d to the move?",
        [
            {"label": "Yes \u2014 the 4H/1H bias was correct, so the entry is justified by the original "
             "analysis.",
             "correct": False,
             "feedback": "<p><strong>Correct directional bias does not create a valid entry by itself.</strong> "
                         "\u00a76.7's chase test requires location at genuine structure, a fresh confirmation, "
                         "and a clear structural stop reference. None of those exist here \u2014 entering "
                         "now, as Figure 6.8's right panel shows, has no structural stop reference and no "
                         "fresh confirmation. Being directionally right is necessary but not sufficient.</p>"},
            {"label": "No \u2014 there is no zone under the current price, no fresh confirmation, and no "
             "structural point to place a stop beyond. This is a chase.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> This matches \u00a76.7's chase definition exactly: "
                         "entry with no structural zone underneath, no independent confirmation, and \u2014 "
                         "critically \u2014 no defensible stop-loss reference (Module 6.2's stop rule cannot "
                         "even be applied, since there is no structural point nearby to place a stop "
                         "beyond). The correct response is the same as in Figure 6.7: accept that this "
                         "specific move was missed, and wait for the next qualifying setup.</p>"},
            {"label": "Only if the position size is reduced to compensate for the added uncertainty.",
             "correct": False,
             "feedback": "<p><strong>Reducing size does not fix a structurally invalid entry.</strong> "
                         "The problem with a chase is not that the risk is too large \u2014 it is that there "
                         "is no structural basis for the stop or the entry at all. A smaller position taken "
                         "on the same unstructured basis is still an unstructured trade, just with less "
                         "money behind it.</p>"},
        ],
        hint="Apply all three tests from \u00a76.7's table \u2014 location, confirmation, and stop reference "
             "\u2014 not just the directional bias."
    ))

    # ------------------------------------------------------------------
    # 6.7 Re-entry rules
    # ------------------------------------------------------------------
    out.append(h2("6.7", "Re-entry rules"))
    out.append(p(
        "Missing an entry does not permanently disqualify the idea. It does mean the specific 15M "
        "confirmation that would have justified entry is gone, and a new one is required before any "
        "position is opened. The test is simple: is there a fresh, independent confirmation at "
        "structure, or is this an attempt to get into a move that has already happened?"
    ))
    out.append(chart(img("m6_reentry.png"),
        "Figure 6.8 \u2014 Left: price returns to the identical structural zone and the 15M chart produces "
        "a new, independent confirmation there \u2014 a valid re-entry. Right: price is chased mid-leg, far "
        "past the original zone, with no fresh confirmation and no structural stop reference \u2014 a "
        "chase, not a re-entry."))
    out.append(table(
        ["Test", "Valid re-entry", "Chase"],
        [
            ["Location", "Same structural zone that produced the original thesis", "Mid-move, no "
             "zone underneath the entry price"],
            ["Confirmation", "A new, independent 15M confirmation at that zone", "None \u2014 entry is "
             "based on the move already happening"],
            ["Stop reference", "Same structural stop logic as the original setup", "No clear structural "
             "point to place a stop beyond"],
            ["Underlying reason for entering", "The market re-tested the level and reacted again",
             "Fear of missing the move (FOMO), delayed by a few candles"],
        ]
    ))

    # ------------------------------------------------------------------
    # 6.8 Practicals
    # ------------------------------------------------------------------
    out.append(h2("6.8", "Practicals"))
    out.append(prac(
        "6.1", "The Full Execution Worksheet",
        "Complete this for one live or historical setup before moving to Module 7.",
        "<ol>"
        "<li>Identify a Module 4-qualified setup on any chart (real or your own historical data).</li>"
        "<li>Write down the exact structural point that would invalidate the thesis, and derive the "
        "stop-loss price from it. State the resulting stop distance in pips or points.</li>"
        "<li>Identify the nearest genuine opposing structure and derive the target from it. Calculate "
        "the resulting reward-to-risk ratio.</li>"
        "<li>If the R:R is below 1:2, write down explicitly why you are rejecting the setup rather than "
        "adjusting the target to force a pass.</li>"
        "<li>If the R:R clears 1:2, calculate position size for two different hypothetical account "
        "balances using the formula in \u00a76.4, using a risk-per-trade percentage you can justify against "
        "a specific prop firm's or personal risk rules.</li>"
        "</ol>"
    ))
    out.append(prac(
        "6.2", "The Cancellation Log",
        "A discipline drill for the situations in \u00a76.6.",
        "<ol>"
        "<li>Over your next 10 chart reviews (real-time or historical), find at least 3 instances where "
        "price interacted with a zone you were watching but never produced a qualifying 15M "
        "confirmation.</li>"
        "<li>For each, write one sentence confirming no entry was placed, and what happened to price "
        "afterward (whether it reversed, continued without you, or chopped).</li>"
        "<li>Separately, find one instance (if any) where you would have been tempted to chase a move "
        "that ran without confirmation. Write down what a chase entry at that point would have looked "
        "like, and why it lacked a structural stop reference.</li>"
        "<li>Review the log after a week. The goal is comfort with cancellation and refusal, not regret "
        "over missed moves \u2014 a move you correctly declined to chase is not a loss.</li>"
        "</ol>"
    ))

    # ------------------------------------------------------------------
    # 6.9 Instrument / session caveats
    # ------------------------------------------------------------------
    out.append(h2("6.9", "Instrument and session caveats"))
    out.append(table(
        ["Instrument / session", "Execution notes"],
        [
            ["EURUSD, London 07:00\u201311:00 UK",
             "Typical stop distances of 8\u201320 pips at genuine structure. Pip value for a USD-denominated "
             "account is straightforward (~$10/pip per standard lot); verify your broker's exact "
             "specification before sizing."],
            ["GBPUSD, London/NY overlap 13:00\u201316:00 UK",
             "Wider typical stop distances (15\u201330 pips) due to faster, deeper sweeps \u2014 position size "
             "correspondingly smaller for the same dollar risk. Verify spread costs are accounted for "
             "separately from the stop distance itself."],
            ["ES / NQ, NY cash 09:30\u201316:00 ET",
             "Stops and targets are typically expressed in points, not pips; point value depends on "
             "contract size (e.g. micro vs mini futures) and must be confirmed per contract "
             "specification. NQ's larger typical range means proportionally wider stops for equivalent "
             "structural distances versus ES."],
            ["Any instrument, prop-firm accounts",
             "Position sizing must additionally respect the firm's maximum daily loss and maximum "
             "overall drawdown rules, which can force a smaller risk-per-trade than the account balance "
             "alone would suggest. Never assume the percentages used for illustration in \u00a76.4 apply to "
             "your specific firm \u2014 full treatment in Module 9."],
        ]
    ))

    # ------------------------------------------------------------------
    # 6.10 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("6.10", "Vocabulary introduced in this module"))
    out.append(table(
        ["Term", "Definition"],
        [
            ["Structural stop", "A stop-loss placed beyond the specific structural point (swing, "
             "liquidity sweep, zone edge) that the trade's thesis depends on."],
            ["Structural target", "A take-profit placed at the nearest genuine opposing structure, "
             "never manufactured to force a favourable ratio."],
            ["Manufactured target", "A target chosen for its resulting reward-to-risk arithmetic rather "
             "than for any genuine structural basis \u2014 not a valid target under this system."],
            ["Position sizing", "Calculating the size of a trade (lots/contracts) backward from a fixed "
             "dollar risk and the structural stop distance."],
            ["Reward-to-risk (R:R)", "The ratio of distance-to-target against distance-to-stop, "
             "expressed as 1:X."],
            ["Trade cancellation", "The correct response when price interacts with a watched zone but "
             "never produces a qualifying confirmation \u2014 no entry occurs."],
            ["Chasing", "Entering a trade mid-move, after it has already left the structural zone, "
             "without a fresh confirmation or a valid structural stop reference."],
            ["Valid re-entry", "A new position taken after a missed entry, justified by a fresh, "
             "independent confirmation at the same (or an equally valid) structural zone."],
        ]
    ))

    # ------------------------------------------------------------------
    # 6.11 Summary
    # ------------------------------------------------------------------
    out.append(h2("6.11", "Summary"))
    out.append(summary([
        "The execution chain has eleven links; a break at any link means no trade, never a smaller "
        "trade.",
        "The stop-loss distance is an output of structure, never an input chosen to hit a comfortable "
        "risk percentage.",
        "The take-profit must be the nearest genuine opposing structure; manufacturing a farther target "
        "to force a better ratio is not permitted, even when the resulting math still clears the 1:2 "
        "minimum.",
        "If the genuine structural target does not clear 1:2 against the structural stop, the trade is "
        "normally invalid \u2014 rejection here is a routine, healthy outcome.",
        "Position size is solved backward from fixed dollar risk and the stop distance; it is the only "
        "quantity in the whole process allowed to vary by account size.",
        "No risk-per-trade percentage is universally correct across prop firms \u2014 firm-specific "
        "drawdown rules can require smaller risk than illustrated examples.",
        "Structural invalidation (exit immediately), trade cancellation (no entry ever occurred), and "
        "refusing to chase (declining an entry with no confirmation) are three distinct concepts with "
        "three distinct correct responses.",
        "A valid re-entry requires a fresh, independent confirmation at genuine structure; entering "
        "mid-move with no structural stop reference is a chase, not a re-entry.",
    ]))

    return "\n".join(out)
