"""
content_m4.py — Module 4: The 15M Price-Action Entry Model.
Exposes build() -> str (the <main> body HTML for module-04.html).
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
    # 4.1 Introduction
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "A qualified trade is not a feeling that a level will hold. It is the output of a "
        "thirteen-step sequence that starts on the 4H chart and ends with an honest "
        "reward-to-risk number. If any minimum condition is missing, the sequence has "
        "already answered the question — the answer is <em>no trade</em>, and no amount of "
        "conviction changes that."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Walk the complete thirteen-step sequence from 4H bias to a qualified entry, for both longs and shorts.",
        "Separate the minimum conditions a setup must have from the conditions that merely strengthen it.",
        "Recognise the specific failure points that force you to stand aside, and explain why in structural terms.",
        "Distinguish a stop-loss price from structural invalidation, and act on the second even when the first has not been touched.",
        "Apply the same sequence to a long and a short without treating the short as a mirrored afterthought.",
        "State, in one sentence, why steps 12 and 13 can reject a setup that passed every other step cleanly.",
    ]))

    out.append(warn("Prerequisite", [
        "This module assumes Module 2's structure vocabulary (swing points, BOS, MSS, displacement) and "
        "Module 3's zone construction (four sources, fresh vs tested, the flip, liquidity, grading) as "
        "already-fluent tools. Every step below uses them without re-deriving them. If a term here feels "
        "unfamiliar, it was defined in Module 2 or 3 — the vocabulary list in \u00a74.12 maps each one back."
    ]))

    out.append(h2("4.1", "The sequence, in full"))
    out.append(p(
        "The thirteen steps are not thirteen independent checks performed in isolation and then "
        "totalled. They are a single chain of reasoning where each step only makes sense given the "
        "one before it. A 1H demand zone (step 3) is meaningless without a 4H uptrend (step 1) to "
        "explain why you are only looking for longs. A 15M bullish close (step 7) is meaningless "
        "without a liquidity sweep (step 6) for it to be a reaction <em>to</em>. The chain is the "
        "point — skipping a link and jumping to the ones that feel exciting is exactly the discipline "
        "failure this module exists to prevent."
    ))

    out.append(chart(img("m4_entry_sequence.png"),
        "<strong>Figure 4.1.</strong> The complete sequence grouped into four phases: 4H/1H bias, "
        "location, 15M confirmation, and the risk decision. Information only ever flows downward "
        "through this chain; a 15M candle can stop the sequence but it can never start one on its own."))

    out.append(table(
        ["Step", "Name", "Answers"],
        [
            ["1", "4H directional environment", "Which side am I even allowed to consider?"],
            ["2", "1H context", "Does the 1H agree with, or complicate, that direction?"],
            ["3", "Meaningful 1H/4H location", "Where, specifically, do I care about price arriving?"],
            ["4", "Relevant liquidity", "What unfilled orders make this location more than a shape on a chart?"],
            ["5", "Wait for interaction", "Has price actually arrived, or am I anticipating?"],
            ["6", "Liquidity event / structural reaction", "Did something happen when price arrived, or did it just pass through?"],
            ["7", "15M price-action confirmation", "Does the close, not just the wick, agree with my thesis?"],
            ["8", "15M structure shift / BOS", "Has the immediate 15M structure actually turned?"],
            ["9", "Displacement (where applicable)", "Is there force behind the move, or is it drifting?"],
            ["10", "Structural invalidation point", "At what exact price is my reasoning wrong?"],
            ["11", "Structural target", "What is the nearest genuine level that opposes me?"],
            ["12", "Reward-to-risk", "Does the honest arithmetic clear 1:2?"],
            ["13", "Qualification decision", "Given all of the above, does this trade exist?"],
        ]
    ))

    out.append(dev("A note on steps 8 and 9", [
        "Steps 8 and 9 are marked \u201cwhere appropriate\u201d in the governing specification deliberately. "
        "Not every valid 15M confirmation includes a textbook structure shift or a displacement candle "
        "that would pass Module 2's strict tests. A strong rejection candle at a well-graded zone (Module "
        "3, \u00a73.6) with a clean close can be enough on its own. What is not optional is step 7: some form "
        "of 15M closing evidence must exist. Steps 8 and 9, when present, make the case stronger — they do "
        "not replace the case."
    ]))

    out.append(quiz(
        "Price reaches a well-graded 1H demand zone. The 15M candle that touches the zone has a long lower "
        "wick and closes near its high, back inside the zone with conviction. There is no clean 15M BOS and "
        "no candle that would pass the strict 70%-body displacement test from Module 2. Has step 7 been "
        "satisfied?",
        [
            {"label": "No — without a qualifying BOS or a displacement candle, the sequence cannot proceed.",
             "correct": False,
             "feedback": "<p><strong>This overstates what steps 8 and 9 require.</strong> They are explicitly "
                         "conditional (\u201cwhere applicable\u201d) in this module's own framing. Step 7 asks only "
                         "whether the 15M <em>closes</em> agree with the thesis — whether the close, not the "
                         "wick, shows the reaction actually happened.</p>"
                         "<p>Demanding a textbook BOS and a 70%-body displacement candle on every single entry "
                         "turns a structural framework into a rigid checklist, which \u00a74.1 explicitly warns "
                         "against: \u201csubjective reasoning must not excuse a missing critical condition — and "
                         "contextual price action must not be reduced to an artificial checklist.\u201d A strong, "
                         "well-located rejection candle is real evidence even without those two extra "
                         "ingredients.</p>"},
            {"label": "Yes — the wick shows the sweep, and the close back inside the zone with conviction is the confirmation step 7 asks for.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> Step 7 only requires 15M closing evidence that the "
                         "location produced a reaction. The long lower wick is the liquidity event (step 6) — "
                         "price swept below the zone and found sellers exhausted or buyers stepping in. The "
                         "close back inside the zone, near the candle's high, is the confirmation: it shows "
                         "the reaction held into the close rather than just poking a wick and continuing "
                         "down.</p>"
                         "<p>Steps 8 (structure shift) and 9 (displacement) would strengthen this further if "
                         "present, but their absence does not fail step 7. What would fail step 7 is a candle "
                         "that swept the zone and closed near its <em>low</em> — a wick with no closing "
                         "conviction behind it, which is exactly the false-breakout pattern from Module 3, "
                         "\u00a73.7.</p>"},
            {"label": "It cannot be answered without knowing the 4H trend.",
             "correct": False,
             "feedback": "<p><strong>The 4H trend belongs to step 1, not step 7.</strong> By the time price is "
                         "interacting with a 1H zone at step 6\u20137, steps 1\u20133 are assumed already resolved — "
                         "that is precisely why the location was worth watching in the first place. Step 7 is "
                         "a narrow, specific question about the closing behaviour of the reaction candle "
                         "itself, and it can be answered from the 15M chart alone.</p>"
                         "<p>This does not mean the 4H trend is irrelevant to the trade as a whole — it is the "
                         "reason a long was being considered at all — only that it is not what step 7 is "
                         "asking about.</p>"},
        ],
        hint="Re-read what step 7 actually asks (\u00a74.1's table) before deciding what evidence satisfies it."
    ))

    # ------------------------------------------------------------------
    # 4.2 Long sequence worked example
    # ------------------------------------------------------------------
    out.append(h2("4.2", "Full sequence — long (EURUSD, London session)"))
    out.append(p(
        "EURUSD, London session (07:00\u201311:00 UK). The 4H chart has been printing higher highs and "
        "higher lows for the past eight sessions — step 1 is resolved: longs only. The 1H chart shows "
        "the same structure and is now pulling back from a fresh high, which is normal continuation "
        "behaviour, not reversal evidence — step 2 confirms rather than complicates step 1."
    ))
    out.append(chart(img("m4_long_setup.png"),
        "<strong>Figure 4.2.</strong> Left: the 1H pullback reaches a demand zone built from the origin "
        "of the prior displacement leg (Module 3, \u00a73.3), with resting sell-side liquidity just beneath "
        "it — stops from the last swing low, plus breakout orders. Right: the 15M chart zoomed into the "
        "reaction. Illustrative synthetic data."))

    out.append(look("Walking the long through the sequence", [
        "<strong>Step 3 — location:</strong> the pullback lands on a 1H demand zone with three of the four ORIGIN/REACTION/LIQUIDITY/FLIP ingredients (Module 3, \u00a73.3) — it is an origin zone, it has an obvious reaction history, and sell-side liquidity sits just below it.",
        "<strong>Step 4 — liquidity:</strong> the sell-side liquidity is the stop cluster below the last 1H higher low. A move that sweeps it and reverses is more informative than a move that simply arrives at the zone and reacts.",
        "<strong>Step 5 — wait:</strong> nothing is done until price actually trades into the zone. Anticipating the reaction and entering early is the single most common way this sequence gets abused.",
        "<strong>Step 6 — reaction:</strong> price wicks below the zone low, sweeping the resting liquidity, then reclaims the zone within the same 15M candle.",
        "<strong>Step 7 — 15M confirmation:</strong> the 15M candle that swept the liquidity closes back above the zone — a real close, not a wick that happened to poke through.",
        "<strong>Step 8 — structure shift:</strong> the 15M sequence of lower highs and lower lows that formed during the pullback breaks — a new higher low prints above the sweep low.",
        "<strong>Step 9 — displacement:</strong> the reclaim candle and the one after it move with real range and small opposing wicks — force is visible, not just a slow grind back up.",
        "<strong>Step 10 — invalidation:</strong> the stop sits below the sweep low. If price trades back below it, the sweep was not a sweep — it was the start of a genuine breakdown, and the thesis is wrong.",
        "<strong>Step 11 — target:</strong> the nearest genuine opposing structure is the prior 1H swing high.",
        "<strong>Step 12 — R:R:</strong> roughly 1:2.3 on the numbers in Figure 4.2 — comfortably clears the 1:2 floor from Module 1.",
        "<strong>Step 13 — qualifies.</strong>",
    ]))

    out.append(defn("Retest entry",
        "Entering not at the exact low of the sweep, but on the candle (or the next one) that closes back "
        "inside the zone, confirming the reaction rather than guessing that the wick will hold. This costs "
        "a small amount of the total move in exchange for confirmation — Module 5 covers the specific "
        "candlestick patterns that make this entry timing precise."))

    # ------------------------------------------------------------------
    # 4.3 Short sequence worked example
    # ------------------------------------------------------------------
    out.append(h2("4.3", "Full sequence — short (GBPUSD, NY session overlap)"))
    out.append(p(
        "GBPUSD, London/NY overlap (13:00\u201316:00 UK) — the highest-liquidity window for cable, and the "
        "session assumption that matters here: GBPUSD zones tend to sweep 15\u201325 pips deep before reacting "
        "(Module 3, \u00a73.10), noticeably more than EURUSD. A stop or a patience threshold sized for EURUSD "
        "will be triggered by normal GBPUSD noise. The 4H chart has been printing lower highs and lower "
        "lows — step 1 resolves to shorts only."
    ))
    out.append(chart(img("m4_short_setup.png"),
        "<strong>Figure 4.3.</strong> Left: the 1H rally reaches a supply zone with resting buy-side "
        "liquidity above it — breakout buy stops and protective stops from the last swing high. Right: "
        "15M reaction, structure shift down, and entry on the retest. Illustrative synthetic data."))

    out.append(p(
        "The short is not a mirror image executed by rote — it is the same reasoning chain applied to a "
        "market currently trading the other way. Three differences from the long worth naming explicitly:"
    ))

    out.append(table(
        ["Aspect", "Long (\u00a74.2)", "Short (\u00a74.3)"],
        [
            ["Location", "Demand zone, origin of an up-leg", "Supply zone, origin of a down-leg"],
            ["Liquidity swept", "Sell-side (stops below a higher low)", "Buy-side (stops above a lower high)"],
            ["15M confirmation", "Close back above the zone", "Close back below the zone"],
            ["Structural stop", "Below the sweep low", "Above the sweep high"],
            ["Instrument/session caveat used here", "EURUSD, London \u2014 typical zone depth 8\u201315 pips", "GBPUSD, NY overlap \u2014 typical zone depth 15\u201325 pips, size the stop and patience accordingly"],
        ]
    ))

    out.append(warn("The short is not the long with the sign flipped", [
        "A genuinely common execution error is treating shorts as an afterthought — waiting for the same "
        "visual pattern that worked on a long and assuming the mirror holds pip-for-pip. It usually does "
        "not, for a structural reason: many instruments (equity indices especially) fall faster than they "
        "rise, so displacement legs down can be sharper and shorter than the up-legs that preceded them. "
        "Grade the short's zone, liquidity and confirmation on their own evidence — never on the assumption "
        "that the down move will behave like the up move in reverse."
    ]))

    # ------------------------------------------------------------------
    # 4.4 Confirmation quality
    # ------------------------------------------------------------------
    out.append(h2("4.4", "What makes step 7 pass or fail"))
    out.append(p(
        "Step 7 is the step most often satisfied dishonestly, because a wick alone is genuinely exciting "
        "to watch. The distinction is not new — it is Module 2's only-closes-count rule applied at the "
        "single-candle level: what the close does after the sweep is the evidence; what the wick did "
        "during the sweep is only the event."
    ))
    out.append(chart(img("m4_confirmation_quality.png"),
        "<strong>Figure 4.4.</strong> Identical location, identical sweep. Left: the candle closes in the "
        "top of its range — the aggression that produced the sweep is still visible at the close. Right: "
        "the candle closes near the middle of its range with a long upper wick — the sweep happened, but "
        "the close shows indecision, not confirmation. Illustrative synthetic data."))

    out.append(look("Reading a confirmation candle in three questions", [
        "<strong>Where does the body sit in the candle's own range?</strong> A close in the outer third of the range (top third for a bullish confirmation, bottom third for bearish) is meaningfully stronger than a close near the middle.",
        "<strong>Did the wick get rejected, or did the close retrace back toward it?</strong> A long wick with a close that crawls back toward the wick's extreme is the market re-testing its own rejection — treat it as unresolved, not confirmed.",
        "<strong>Does the next candle agree?</strong> One strong close is a candidate. A second candle that fails to build on it (a doji, an opposing close) demotes the confirmation without necessarily invalidating the location.",
    ], ordered=False))

    # ------------------------------------------------------------------
    # 4.5 Invalidation vs stop price
    # ------------------------------------------------------------------
    out.append(h2("4.5", "Invalidation is structural, not just a stop price"))
    out.append(p(
        "The stop-loss order and the invalidation condition are related but not identical. The stop order "
        "is the mechanical instruction that limits the loss if the thesis is wrong. Invalidation is the "
        "<em>reason</em> the thesis is wrong. They usually sit at the same price, and it is tempting to "
        "treat them as the same concept — but structure can invalidate a trade before the stop price is "
        "ever touched, and when that happens, waiting for the stop to fill is not discipline, it is delay."
    ))
    out.append(chart(img("m4_invalidation.png"),
        "<strong>Figure 4.5.</strong> A long entered correctly on the sequence in \u00a74.2's pattern. Before "
        "price reaches either the stop or the target, a new structural lower low forms below the entry "
        "structure — the higher-low pattern that justified the entry is gone. The stop order has not "
        "filled, but the reason for being long no longer exists. Illustrative synthetic data."))

    out.append(key("The rule", "A stop-loss order limits how wrong you can be. It does not tell you when "
        "you have become wrong. Structure does that, and structure can announce it earlier."))

    out.append(quiz(
        "You are long from a 15M confirmation at a 1H demand zone. Fifteen minutes after entry, a new 15M "
        "candle prints a lower low below the most recent higher low that had formed after your entry — but "
        "price is still 30 pips above your stop-loss order. What should you do?",
        [
            {"label": "Nothing — the stop-loss order has not been hit, so the trade is still valid by definition.",
             "correct": False,
             "feedback": "<p><strong>This confuses the stop order with the invalidation condition, which is "
                         "exactly the trap \u00a74.5 names.</strong> The stop-loss price is where the loss is "
                         "capped if you are wrong; it is not evidence that you are still right. A new lower "
                         "low breaking the higher-low structure that formed after entry is direct structural "
                         "evidence against the long thesis, independent of how far price currently sits from "
                         "the stop order.</p>"
                         "<p>Holding on the logic \u201cthe stop hasn't been hit\u201d turns a risk-management tool "
                         "into a permission slip to ignore new information. The 30 pips of cushion are not "
                         "protection here — they are just distance the position has to give back before the "
                         "stop order finally agrees with what the structure already showed.</p>"},
            {"label": "Move the stop closer to reduce risk, but keep the position open.",
             "correct": False,
             "feedback": "<p><strong>This treats a structural problem as a sizing problem, which Module 1 "
                         "specifically warned against</strong> (tightening a stop changes your loss rate, it "
                         "does not change whether the thesis is still true). If the higher-low structure that "
                         "justified the entry has broken, the location no longer supports the trade — no stop "
                         "distance fixes that, because the problem is not \u201chow much am I risking,\u201d it is "
                         "\u201cis my reason for being in this trade still correct.\u201d</p>"
                         "<p>Tightening the stop in this situation typically produces the worst outcome: you "
                         "stay in a trade whose thesis has failed, and a small adverse wick now stops you out "
                         "at a worse average result than an immediate exit would have.</p>"},
            {"label": "Exit. The structural condition that justified the trade no longer holds, regardless of where the stop-loss order sits.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> The entry was justified by a specific structural claim: "
                         "price would hold above the reclaimed zone and continue printing higher lows. A new "
                         "lower low breaking that pattern is a direct falsification of the claim, and it "
                         "arrived before the stop order — the mechanical backstop for a wrong thesis — had a "
                         "chance to fire.</p>"
                         "<p>This is Module 7 territory in more depth (trade management), but the principle "
                         "belongs here: invalidation is a structural event, and a structural event can happen "
                         "at any price, not only at the price you pre-selected for your stop order. Exiting "
                         "here typically produces a smaller loss (or a smaller giveback of profit) than "
                         "waiting for the stop to eventually fill.</p>"},
        ],
        hint="Ask which of the two — the stop order or the structural pattern — was the actual reason you entered."
    ))

    # ------------------------------------------------------------------
    # 4.6 Stand aside
    # ------------------------------------------------------------------
    out.append(h2("4.6", "When the sequence correctly produces no trade"))
    out.append(p(
        "Not finding a trade is not a failure of the sequence — it is frequently the correct output of it. "
        "A wide, directionless range on the 4H and 1H charts fails the sequence at steps 1, 3 and 4 "
        "simultaneously: there is no directional environment to establish, no origin or reaction zone "
        "worth marking because nothing displaced strongly enough to leave one, and no liquidity picture "
        "worth reading because there is no obvious level for stops to cluster around."
    ))
    out.append(chart(img("m4_stand_aside.png"),
        "<strong>Figure 4.6.</strong> Thirty bars of range-bound, noisy price action with no HH/HL or "
        "LH/LL sequence, no displacement leg, and no zone with a coherent origin. The sequence terminates "
        "at step 3\u20134 rather than at step 13 — there was nothing to reject at the end because there was "
        "nothing to build toward at the start. Illustrative synthetic data."))

    out.append(split([
        ("bad", "\u201cI can't find a trade\u201d (accurate)",
         "4H and 1H structure is genuinely unclear \u2014 no HH/HL or LH/LL sequence resolvable. There is no zone "
         "with a defensible origin. This is the sequence working correctly and reporting that no valid "
         "setup exists right now."),
        ("neutral", "\u201cI'm afraid to take a valid trade\u201d (a different problem)",
         "Every step from 1 through 12 has resolved cleanly and the arithmetic clears 1:2, but hesitation, "
         "a recent loss, or a desire for more confirmation than the sequence requires delays or skips the "
         "entry. This is not the sequence rejecting the trade \u2014 the sequence already qualified it. Module 8 "
         "covers this distinction and its psychology in depth."),
    ]))

    out.append(h2("4.7", "Minimum, strengthening, and invalidating conditions"))
    out.append(p(
        "None of the three lists below is exhaustive, and none is a scored checklist where a majority of "
        "ticks wins. The minimum column is a floor — every item must be true or the sequence has already "
        "ended. The strengthening column adds confidence to a setup that already cleared the floor; it "
        "cannot substitute for a missing minimum condition. The invalidating column, if any single item "
        "is true, ends the sequence regardless of how many boxes elsewhere look attractive."
    ))
    out.append(chart(img("m4_condition_grid.png"),
        "<strong>Figure 4.7.</strong> The three condition sets side by side. A setup can score well on the "
        "middle column and still fail on a single item in the right column \u2014 conditions are not additive "
        "against each other."))

    out.append(warn("Do not turn this into a scored checklist", [
        "The specification for this course is explicit on this point: \u201csubjective reasoning must not "
        "excuse a missing critical condition — and contextual price action must not be reduced to an "
        "artificial checklist.\u201d Treating the minimum column as \u201c5 out of 6 is good enough\u201d is exactly "
        "the failure mode this warns against. A missing 4H direction (step 1) is not offset by a beautifully "
        "fresh zone and a textbook displacement candle — the 4H disagreement means the whole line of "
        "reasoning is being applied in the wrong direction."
    ]))

    # ------------------------------------------------------------------
    # 4.8 R:R math as the final gate
    # ------------------------------------------------------------------
    out.append(h2("4.8", "Steps 12 and 13 — the arithmetic that ends the sequence"))
    out.append(p(
        "Two trades can pass every qualitative step identically — same directional environment, same "
        "quality of zone, same clean 15M confirmation, same structural stop distance — and still resolve "
        "differently at step 13, because the honest distance to the next genuine structural level differs "
        "by less than a point."
    ))
    out.append(chart(img("m4_rr_math.png"),
        "<strong>Figure 4.8.</strong> Both setups share an identical stop distance of 0.45. In the left "
        "panel the nearest genuine opposing structural level sits 1.53 away, giving 1:3.4. In the right "
        "panel the nearest genuine level is only 0.63 away, giving 1:1.4 \u2014 below the 1:2 floor from "
        "Module 1. The correct response to the right panel is rejection, not a manufactured farther "
        "target."))

    out.append(key("Module 6's rule, previewed here because step 11 depends on it",
        "\u201cIf the genuine structural target does not offer at least 1:2 relative to the structural stop, "
        "the trade should normally be considered invalid. Never widen a target merely to make the "
        "mathematics look attractive.\u201d The target is read off the chart from existing structure — it is "
        "never selected to hit a ratio."))

    out.append(quiz(
        "A setup clears steps 1\u201310 cleanly: 4H and 1H agree, the zone grades 5/6 on Module 3's rubric, "
        "the 15M confirmation closes with conviction, and the structural stop sits a defensible distance "
        "beyond the sweep. The nearest genuine opposing structural level, however, is only 1.3\u00d7 the stop "
        "distance away. What should happen at step 13?",
        [
            {"label": "Take the trade — steps 1\u201310 are the hard part, and a 1.3R target is still profit if it works.",
             "correct": False,
             "feedback": "<p><strong>This drops the arithmetic gate entirely, which is exactly what step 12 "
                         "exists to prevent.</strong> A 1:1.3 setup requires a win rate above roughly 43% just "
                         "to break even (Module 1's expectancy formula: E = win%\u00d7R:R \u2212 loss%\u00d71). Most "
                         "honestly graded discretionary setups do not clear that bar consistently enough to "
                         "make 1:1.3 trades a viable long-run edge, which is precisely why Module 1 sets 1:2 "
                         "as the floor rather than an aspiration.</p>"
                         "<p>The quality of steps 1\u201310 does not change the arithmetic of step 12. A perfectly "
                         "identified location with an insufficient reward-to-risk is still an insufficient "
                         "reward-to-risk.</p>"},
            {"label": "Look further out on the chart for a farther level that would produce a better ratio, and use that as the target.",
             "correct": False,
             "feedback": "<p><strong>This is manufacturing a target, which the specification names directly: "
                         "\u201cnever widen a target merely to make the mathematics look attractive.\u201d</strong> "
                         "The target in step 11 has to be the <em>nearest genuine</em> opposing structural "
                         "level — the first real obstacle price is likely to encounter. Reaching past it to a "
                         "level that merely produces a flattering ratio ignores the much higher probability "
                         "that price reacts at the nearer level first, which means the trade is very unlikely "
                         "to realise the ratio being quoted.</p>"
                         "<p>If price does clear the near level cleanly with displacement, that is a "
                         "legitimate reason to extend a runner in trade management (Module 7) — but it is not "
                         "a legitimate basis for the original qualification decision.</p>"},
            {"label": "Reject the trade at step 13. A well-identified location with an insufficient reward-to-risk is still a rejected trade.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> Step 13 is a genuine gate, not a formality once steps "
                         "1\u201310 look good. \u00a74.8's rule is explicit: a genuine R:R below roughly 1:2 means "
                         "the trade should normally be considered invalid, full stop, regardless of how clean "
                         "the upstream analysis was.</p>"
                         "<p>The correct response is exactly the phrase from Module 1: this is \u201cvalid "
                         "analysis, invalid trade.\u201d The 4H direction, the 1H location, and the 15M "
                         "confirmation were all real and worth logging for pattern recognition — the setup "
                         "simply does not clear the bar that turns analysis into a position. Waiting for the "
                         "same location to set up again with a farther genuine target, or waiting for a "
                         "different location entirely, are the two acceptable paths forward.</p>"},
        ],
        hint="Re-read the exact wording of the rule quoted in \u00a74.8 before choosing."
    ))

    # ------------------------------------------------------------------
    # 4.9 Instrument & session caveats
    # ------------------------------------------------------------------
    out.append(h2("4.9", "Instrument and session caveats"))
    out.append(table(
        ["Instrument", "Session assumed", "What changes in the sequence"],
        [
            ["EURUSD", "London 07:00\u201311:00 UK, overlap 13:00\u201316:00 UK",
             "Baseline behaviour used throughout this module. Zones typically 8\u201315 pips wide (Module 3, \u00a73.10). Liquidity sweeps tend to be shallow and quick."],
            ["GBPUSD", "London/NY overlap 13:00\u201316:00 UK",
             "Deeper, faster sweeps (15\u201325 pips typical). A stop distance or a patience threshold copied from EURUSD will be triggered by ordinary GBPUSD noise \u2014 size step 10 to the instrument, not to a habit."],
            ["ES / NQ (index futures)", "NY cash session 09:30\u201316:00 ET",
             "Zones frequently anchor to the prior day's high/low or the overnight range rather than a pure intraday displacement origin. NQ in particular produces more false breaks at obvious levels (Module 3, \u00a73.10) \u2014 step 6 (the reaction) deserves extra scrutiny before step 7 is granted."],
        ]
    ))
    out.append(warn("No universal stop or target distance", [
        "This module deliberately gives ranges, not fixed numbers, for zone width and sweep depth. A "
        "structural stop is always derived from the specific chart in front of you (Module 6 covers the "
        "exact placement rules) \u2014 never copied from a table like the one above. The table exists so you "
        "recognise when a stop distance that felt normal on one instrument is actually too tight for "
        "another, not so you memorise a number to apply blindly."
    ]))

    # ------------------------------------------------------------------
    # 4.10 Failure map
    # ------------------------------------------------------------------
    out.append(h2("4.10", "Where the sequence most often breaks down"))
    out.append(table(
        ["Step", "Common failure", "What it looks like", "Correct response"],
        [
            ["1\u20132", "Fighting the higher timeframe", "Taking a short because a 15M chart looks weak while the 4H is still in a clean uptrend.", "Stand aside, or wait for the 4H to actually turn before considering the opposite direction."],
            ["3", "Treating any prior reaction as a location", "Marking a level because price touched it once, without checking for the ORIGIN/REACTION/LIQUIDITY/FLIP ingredients from Module 3.", "Score the location; 0\u20131 ingredients is just a price, not a location."],
            ["6\u20137", "Reacting to the wick, not the close", "Entering the instant price touches the zone, before the 15M candle has closed.", "Wait for the close. A wick is an event; a close is evidence."],
            ["9", "Requiring displacement on every entry", "Discarding a valid setup because the confirmation candle does not pass the strict 70%-body test.", "Displacement strengthens a setup; its absence does not fail step 7 on its own."],
            ["10", "Confusing the stop order with invalidation", "Holding a position after the structural pattern has broken, because the stop order has not filled yet.", "Exit on structural invalidation; do not wait for the mechanical backstop."],
            ["11", "Reaching for a target to flatter the ratio", "Selecting a farther level specifically because the nearer one gives an insufficient R:R.", "Target the nearest genuine level. If the ratio fails, the trade fails."],
            ["13", "Overriding a failed gate with conviction", "\u201cEverything else lines up so well, I'll take it anyway\u201d on a setup that failed one minimum condition.", "A failed minimum condition is a rejection. Confidence in the rest of the analysis does not offset it."],
        ]
    ))

    # ------------------------------------------------------------------
    # 4.11 Practicals
    # ------------------------------------------------------------------
    out.append(h2("4.11", "Practicals"))
    out.append(prac("4.1", "The Sequence Walkthrough Drill",
        "Time: ~2 hours \u00b7 Tools: charting platform, no indicators",
        "<div class=\"look\"><h4>Procedure</h4><ol>"
        "<li>Open your chosen instrument's 4H chart and identify the current directional environment. "
        "Write down the last three swing points that justify your read.</li>"
        "<li>Drop to the 1H chart. Mark the most recent zone that a Module 3 four-source test supports, and "
        "identify the liquidity sitting on the far side of it.</li>"
        "<li>Scroll forward candle by candle on the 15M chart until price interacts with the zone. Do not "
        "look ahead \u2014 the point is to practise waiting.</li>"
        "<li>For each interaction, write down explicitly: did step 7 pass or fail, and why (cite the close, "
        "not the wick)? If it passed, note whether steps 8 and 9 were present.</li>"
        "<li>For every setup that reached step 10, calculate the honest R:R using the nearest genuine "
        "structural level. Record whether it qualified.</li>"
        "<li>Repeat for ten separate interactions, mixing long and short scenarios. Tally how many reached "
        "step 13 and qualified versus how many were correctly rejected, and at which step each rejection "
        "happened.</li>"
        "</ol></div>"))

    out.append(prac("4.2", "The Invalidation Journal",
        "Time: ongoing, ~10 minutes per trade \u00b7 Tools: trade journal (spreadsheet or notebook)",
        "<div class=\"look\"><h4>Procedure</h4><ol>"
        "<li>For every trade you take (real, demo, or paper), write down the structural invalidation "
        "condition <em>before</em> entry, in plain language \u2014 not just the stop price, but the specific "
        "structural pattern whose failure would prove the thesis wrong.</li>"
        "<li>After the trade closes, record whether the exit happened because the stop order filled, or "
        "because you recognised structural invalidation before the stop was touched, or because the target "
        "was reached.</li>"
        "<li>After twenty trades, review how often the structural invalidation preceded the stop fill, and "
        "estimate what those early exits saved (or cost, if you exited too early on noise rather than "
        "genuine invalidation \u2014 both errors are worth seeing in your own data).</li>"
        "</ol></div>"))

    # ------------------------------------------------------------------
    # 4.12 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("4.12", "Vocabulary"))
    out.append(defn("Confirmation (15M)", "Closing evidence, on the 15M timeframe, that a location produced "
        "the reaction the thesis predicted. Distinguished from a mere touch or wick by where the candle "
        "closes within its own range."))
    out.append(defn("Structural invalidation", "The specific price-structure event whose occurrence proves "
        "the trade thesis wrong, independent of whether the stop-loss order has filled at that point."))
    out.append(defn("Stop-loss order (as distinct from invalidation)", "The mechanical order that caps the "
        "loss if the thesis is wrong. Normally placed at or beyond the invalidation point, but its filling "
        "is not the definition of \u201cwrong\u201d \u2014 only the backstop for it."))
    out.append(defn("Structural target", "The nearest genuine opposing structural level (swing point, zone, "
        "or liquidity objective) that price would need to clear for the thesis to keep extending. Never "
        "selected to produce a specific ratio."))
    out.append(defn("Qualification (step 13)", "The binary decision that results from steps 1\u201312: either "
        "every minimum condition and the R:R floor are satisfied, and the trade exists, or one is missing, "
        "and it does not \u2014 regardless of how attractive the rest of the picture looks."))
    out.append(defn("Stand aside", "The correct, deliberate outcome when the sequence terminates before "
        "step 13 because a minimum condition (most often steps 1, 3, 4 or 12) is not met. Distinct from "
        "fear-based avoidance of a setup that did qualify (Module 8)."))

    # ------------------------------------------------------------------
    # 4.13 Summary
    # ------------------------------------------------------------------
    out.append(h2("4.13", "Summary"))
    out.append(summary([
        "<b>The sequence is a chain, not a checklist.</b> Each step only means something given the step before it; skipping to the exciting steps without the earlier ones defeats the purpose.",
        "<b>Direction and location come from the 4H and 1H; permission to act comes from the 15M.</b> The 15M can veto a trade the higher timeframes support. It cannot authorise one they do not.",
        "<b>Step 7 asks about the close, not the wick.</b> A sweep is an event. A close that holds the reaction is evidence.",
        "<b>Steps 8 and 9 strengthen a setup; they are not always required to satisfy step 7.</b> Do not turn a structural framework into a rigid checklist that a valid confirmation can never pass.",
        "<b>Invalidation is structural, not just a stop price.</b> A pattern can fail before the stop order fills. Exit on the structural failure, not on the mechanical backstop alone.",
        "<b>The short is not the long with the sign flipped.</b> Grade the zone, the liquidity, and the confirmation on the short's own evidence, and respect instrument-specific differences (GBPUSD sweeps deeper than EURUSD; index futures anchor to prior-day levels).",
        "<b>Steps 12 and 13 are a genuine gate.</b> A setup that is perfect through step 10 is still rejected if the honest R:R fails to clear roughly 1:2.",
        "<b>Never manufacture a target to fix a failing ratio.</b> The target is the nearest genuine structural level, read off the chart, not selected to flatter the arithmetic.",
        "<b>\u201cNo trade\u201d is frequently the correct output.</b> A wide, directionless range failing steps 1, 3 and 4 is the sequence working, not the sequence failing.",
        "<b>Distinguish \u201cno trade exists\u201d from \u201cI am afraid to take a valid trade.\u201d</b> The first is the sequence's output; the second is a psychology problem covered in Module 8.",
        "<b>State the instrument and session in every application of this sequence.</b> Zone depth, sweep behaviour and false-break frequency all vary by instrument \u2014 a stop or a patience threshold that is normal on one instrument can be wrong on another.",
        "<b>A missing minimum condition is a rejection, never a size-down.</b> Confidence in the rest of the analysis does not offset a failed gate \u2014 this is the same principle Module 1 established for the five gates and it applies unchanged here.",
    ]))

    return "".join(out)
