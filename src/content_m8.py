"""
content_m8.py — Module 8: When NOT to Trade.
Exposes build() -> str (the <main> body HTML for module-08.html).
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
    # 8.0 Introduction
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "Everything so far has described what a valid trade looks like. This module describes what one "
        "does <em>not</em> look like \u2014 and it matters just as much, because the sequence in Module 4 "
        "only works if every condition it names is checked honestly. A trader who forces a trade through "
        "a gap in the sequence has not found an exception to the system; they have simply stopped using "
        "it for that decision."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Recognise sixteen specific, nameable conditions under which the entry sequence should not "
        "produce a trade.",
        "Distinguish chop from a readable trend, and conflicting HTF context from aligned context.",
        "Identify an excessively tested zone, poor liquidity, and weak 15M confirmation as reasons to "
        "stand aside, not reasons to lower the bar.",
        "Recognise chasing an extended move, and tell a genuinely poor R:R setup apart from one with a "
        "manufactured target.",
        "Treat unusual volatility and major scheduled news as conditions that suspend the reliability of "
        "structure, not conditions to trade through.",
        "Distinguish \u201cno trade exists\u201d from \u201cI am afraid to take a valid trade,\u201d and name FOMO, "
        "revenge trading, overtrading, and confirmation bias when they appear.",
    ]))

    out.append(warn("Prerequisite", [
        "This module assumes the full 13-step sequence from Module 4, the S&R/zone-quality vocabulary "
        "from Module 3, the candlestick reliability criteria from Module 5, and the R:R and stop/target "
        "rules from Module 6. Every condition named here is a specific, earlier-defined term failing to "
        "hold \u2014 nothing in this module introduces a new subjective judgement call."
    ]))

    out.append(h2("8.1", "Sixteen conditions that end the sequence"))
    out.append(p(
        "Any one of the following is sufficient, on its own, to end the sequence before it reaches a "
        "qualified trade. They do not need to occur together, and none of them requires a discretionary "
        "read under pressure \u2014 each is a specific term already defined in an earlier module."
    ))
    out.append(chart(img("m8_stand_aside_grid.png"),
        "Figure 8.1 \u2014 Sixteen specific, nameable conditions grouped by where in the sequence they "
        "appear: market condition, location/confirmation, or execution/risk. Any single item is "
        "sufficient on its own to end the sequence."))
    out.append(table(
        ["Category", "Condition", "Where it breaks the sequence"],
        [
            ["Market condition", "Chop", "Step 1\u20132 (Module 4): no HH/HL or LH/LL structure to "
             "establish direction from."],
            ["Market condition", "Low-quality range", "Step 1\u20132: no expansion, no defined edges to "
             "read."],
            ["Market condition", "Poor 4H/1H structure", "Step 1\u20132: swings are not clean enough to "
             "identify with confidence."],
            ["Market condition", "Conflicting HTF context", "Step 1: 4H and 1H disagree on direction, "
             "so no coherent bias exists (\u00a78.2)."],
            ["Market condition", "Abnormal market behaviour", "Any step: price is moving in a way that "
             "does not resemble ordinary structural behaviour."],
            ["Location & confirmation", "Weak/unclear S&R", "Step 3 (Module 3): no real reaction history "
             "behind the level."],
            ["Location & confirmation", "Excessively tested zone", "Step 3 (\u00a73.7): the zone's "
             "potency has been consumed by repeated reactions (\u00a78.4)."],
            ["Location & confirmation", "Poor liquidity", "Step 4: nothing resting nearby for price to "
             "react against."],
            ["Location & confirmation", "Weak 15M confirmation", "Step 7 (Module 4, \u00a74.4): the 15M "
             "candle closes without conviction."],
            ["Location & confirmation", "Unclear invalidation", "Step 10: no sensible, nearby place to "
             "define a structural stop."],
            ["Execution & risk", "Late entry / chasing", "Step 6\u20137: entry is taken far from the "
             "structure that would justify it (\u00a78.5)."],
            ["Execution & risk", "Poor R:R", "Step 12\u201313 (Module 6, \u00a76.3): the genuine structural "
             "target gives less than 1:2 (\u00a78.6)."],
            ["Execution & risk", "Excessive spread/slippage", "Execution: transaction cost materially "
             "erodes the honest edge of the setup."],
            ["Execution & risk", "Unusual volatility", "Any step: ranges far outside the instrument's "
             "normal behaviour make structure unreliable (\u00a78.7)."],
            ["Execution & risk", "Major scheduled news", "Any step: the coming price move will be driven "
             "by an event outcome, not by price action (\u00a78.7)."],
            ["Execution & risk", "Correlated over-concentration", "Portfolio level: multiple open "
             "positions carry the same underlying risk despite looking like separate trades (Module 9)."],
        ]
    ))

    # ------------------------------------------------------------------
    # 8.2 Chop and conflicting context
    # ------------------------------------------------------------------
    out.append(h2("8.2", "Chop, low-quality ranges, and conflicting context"))
    out.append(p(
        "The entry sequence begins with 4H direction and 1H context. If those two conditions cannot be "
        "established with confidence, nothing downstream can be trusted \u2014 a confirmation candle at an "
        "unclear location is not more valid just because it looks decisive on the 15M."
    ))
    out.append(chart(img("m8_chop_vs_trend.png"),
        "Figure 8.2 \u2014 Left: price oscillates without ever printing a clean HH/HL or LH/LL sequence \u2014 "
        "no directional structure exists to build a thesis on. Right: each pullback holds above the prior "
        "higher low, giving the entry model unambiguous structure to work with."))
    out.append(chart(img("m8_conflicting_context.png"),
        "Figure 8.3 \u2014 Left: the 4H remains bullish while the 1H is printing a clean LH/LL downtrend "
        "against it \u2014 no single coherent direction exists yet. Right: 4H and 1H agree, giving one "
        "readable direction to trade in."))
    out.append(warn("Neither timeframe is ignored to force alignment", [
        "When 4H and 1H disagree, the correct response is not to pick whichever one supports the trade "
        "idea already forming. Both readings are genuine; the conflict itself is the information. The "
        "correct action is to wait until one timeframe's structure actually changes, not to override the "
        "one that is inconvenient."
    ]))

    # ------------------------------------------------------------------
    # 8.3 Weak S&R, poor liquidity, weak confirmation
    # ------------------------------------------------------------------
    out.append(h2("8.3", "Weak location, poor liquidity, weak confirmation"))
    out.append(p(
        "Steps 3, 4, and 7 of the entry sequence each have a minimum quality bar. A price level with no "
        "real reaction history behind it is not S&R just because a horizontal line can be drawn through "
        "it (Module 3); a location with nothing resting nearby gives price no reason to react in the "
        "first place; and a 15M candle that closes mid-range provides no more conviction than a coin "
        "flip (Module 4, \u00a74.4)."
    ))
    out.append(table(
        ["Weak version (stand aside)", "Why it fails the minimum bar"],
        [
            ["A price plotted from a single old wick with no repeated reaction",
             "No history of price actually respecting the level (Module 3, \u00a73.2)"],
            ["A location with no resting stops, no obvious swing, no round-number confluence",
             "Nothing for price to react against \u2014 liquidity absent, not just unclear"],
            ["A 15M candle with a small body closing in the middle of its range",
             "No conviction in either direction \u2014 fails Module 4's confirmation-quality test"],
            ["A stop that would need to sit an arbitrary distance away with no structural anchor",
             "Invalidation point is unclear \u2014 the stop cannot be justified from structure"],
        ]
    ))

    # ------------------------------------------------------------------
    # 8.4 Excessively tested zones
    # ------------------------------------------------------------------
    out.append(h2("8.4", "Excessively tested zones"))
    out.append(p(
        "Module 3 (\u00a73.7) established that every reaction off a zone consumes some of the resting "
        "orders that made the level meaningful in the first place. A zone on its fifth test carries "
        "materially less weight than the same zone on its first, even though both are drawn from "
        "identical-looking price behaviour."
    ))
    out.append(chart(img("m8_overtested_zone.png"),
        "Figure 8.4 \u2014 Left: five separate reactions off the same demand zone, each producing a "
        "smaller bounce than the last \u2014 the zone's reliability is exhausted. Right: the origin of a "
        "displacement leg, never revisited since \u2014 the first test carries the most weight."))

    # ------------------------------------------------------------------
    # 8.5 Late entries and chasing
    # ------------------------------------------------------------------
    out.append(h2("8.5", "Late entries and chasing"))
    out.append(key("The chasing test",
        "If entry is taken at a price with no nearby structure to define a stop against, the position "
        "has no honest risk definition \u2014 regardless of how strong the move looks. Chasing is not a "
        "sizing problem to be solved with a wider stop; it is a location problem with no fix except "
        "waiting for the next genuine pullback into structure."
    ))
    out.append(chart(img("m8_late_entry_chase.png"),
        "Figure 8.5 \u2014 Left: entry is taken far from any structure after the move has already run, "
        "purely to avoid missing it \u2014 there is no nearby structure to place a sensible stop against. "
        "Right: entry waits for the pullback into the most recent higher low, giving the position a "
        "defensible, structural invalidation point."))

    out.append(quiz(
        "A trader watches EURUSD run 60 pips in a strong uptrend without any pullback. Wanting exposure "
        "before it \u201cgets away,\u201d they buy at the current market price with a stop placed an arbitrary "
        "15 pips below, since there is no recent swing low nearby. What is the correct assessment?",
        [
            {"label": "Reasonable \u2014 the trend is clearly strong, and a 15-pip stop is a normal size "
             "for this instrument.",
             "correct": False,
             "feedback": "<p><strong>A normal-looking stop distance does not make the entry "
                         "structural.</strong> \u00a78.5's test is whether the stop is placed beyond a "
                         "specific structural point that invalidates the thesis (Module 6, \u00a76.2) \u2014 "
                         "not whether its size looks reasonable in isolation. An arbitrary 15 pips chosen "
                         "only because nothing structural exists nearby is exactly the chasing pattern "
                         "Figure 8.5's left panel illustrates.</p>"},
            {"label": "This is chasing \u2014 there is no nearby structure to justify the stop location, "
             "so the trade should be skipped in favour of waiting for a genuine pullback.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a78.5 defines chasing precisely by this test: an "
                         "entry taken with no nearby structure to place a defensible stop against. The "
                         "strength of the preceding move does not substitute for a structural invalidation "
                         "point. The correct response is to stand aside and wait for the pullback into the "
                         "most recent genuine swing, exactly as shown in Figure 8.5's right panel.</p>"},
            {"label": "It depends on whether the trader's account can tolerate a 15-pip loss.",
             "correct": False,
             "feedback": "<p><strong>Account tolerance for the loss is a position-sizing question "
                         "(Module 9), not a chasing test.</strong> \u00a78.5 evaluates whether the entry has "
                         "a structural basis at all \u2014 whether risk can be defined from the chart, not "
                         "whether the trader can financially absorb whatever stop distance results.</p>"},
        ],
        hint="Ask whether the 15-pip stop was placed beyond a specific structural point, or chosen only "
             "because nothing structural was nearby."
    ))

    # ------------------------------------------------------------------
    # 8.6 Poor R:R vs manufactured R:R
    # ------------------------------------------------------------------
    out.append(h2("8.6", "Genuinely poor R:R vs a manufactured target"))
    out.append(p(
        "Module 6 (\u00a76.3) already established that a target must be the nearest genuine opposing "
        "structure, and that a trade offering less than 1:2 against a structural stop should normally be "
        "rejected. Two different-looking mistakes both lead back to a rejected trade: accepting a "
        "genuinely close target, or stretching a target artificially far to make the ratio look "
        "acceptable."
    ))
    out.append(chart(img("m8_poor_rr.png"),
        "Figure 8.6 \u2014 Left: the nearest real opposing structure sits close enough to entry that R:R "
        "comes out below 1:2 \u2014 correctly rejected on structural grounds. Right: the same entry and stop, "
        "with the target pushed out past where real structure actually ends \u2014 the ratio looks "
        "acceptable on paper but the target has no structural basis, and is rejected for a different "
        "reason."))
    out.append(warn("Both are rejections, not the same rejection", [
        "The left panel is rejected because the market genuinely does not offer enough room. The right "
        "panel is rejected because the number on paper was manufactured rather than observed. Confusing "
        "the two is dangerous: a trader who \u201cfixes\u201d a poor R:R by pushing the target out has not "
        "solved the problem, they have hidden it behind a larger, less honest number."
    ]))

    out.append(quiz(
        "A structural stop sits 18 pips from entry. The nearest genuine opposing structure sits 30 pips "
        "away, giving an honest R:R of about 1:1.7. A trader considers moving the target to a round "
        "number 40 pips away, which has no opposing structure behind it, purely to clear the 1:2 "
        "threshold. What is the correct assessment?",
        [
            {"label": "Acceptable \u2014 40 pips is still a reasonable distance for this instrument, and "
             "1:2.2 clears the minimum comfortably.",
             "correct": False,
             "feedback": "<p><strong>The distance being \u201creasonable\u201d for the instrument is not the "
                         "test.</strong> Module 6 (\u00a76.3) and \u00a78.6 both require the target to be the "
                         "nearest genuine opposing structure, not a round number chosen to clear a "
                         "threshold. A target with no structural basis behind it is a manufactured target "
                         "regardless of how plausible its distance looks.</p>"},
            {"label": "The trade should be rejected \u2014 the genuine target gives less than 1:2, and "
             "moving the target past real structure only manufactures a better-looking ratio without "
             "changing the actual setup.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a78.6 is explicit that stretching a target "
                         "beyond the nearest genuine opposing structure to force the R:R above 1:2 is a "
                         "rejection in its own right, distinct from (but just as final as) a genuinely poor "
                         "R:R. The honest target here gives roughly 1:1.7, which fails Module 6's 1:2 "
                         "minimum \u2014 the trade should be passed on, not repaired with a fictional "
                         "target.</p>"},
            {"label": "It depends on whether the trader's overall win rate is high enough to offset the "
             "lower R:R.",
             "correct": False,
             "feedback": "<p><strong>Win rate is not part of the per-trade R:R test in \u00a76.3 or "
                         "\u00a78.6.</strong> The rule evaluates whether the nearest genuine structural "
                         "target clears 1:2 on this specific setup. Win-rate-based expectancy reasoning "
                         "(Module 1) describes the system's overall edge; it does not license manufacturing "
                         "an individual trade's target to hit a number.</p>"},
        ],
        hint="Ask whether the 40-pip target is backed by real opposing structure, or chosen only to "
             "clear the 1:2 threshold."
    ))

    # ------------------------------------------------------------------
    # 8.7 Unusual volatility and scheduled news
    # ------------------------------------------------------------------
    out.append(h2("8.7", "Unusual volatility and major scheduled news"))
    out.append(p(
        "Structure, stops, and targets are all built on the assumption that price behaviour reflects "
        "ordinary participant activity. Around a major scheduled release, that assumption breaks: a "
        "single 15M candle can move many times the session's normal range in a way driven by the news "
        "outcome itself, not by the structural forces this system reads."
    ))
    out.append(chart(img("m8_volatility_news.png"),
        "Figure 8.7 \u2014 Normal 15M ranges in this session run 8\u201312 pips. The two candles bracketing "
        "the scheduled release each exceed 70 pips in a single bar \u2014 any structure, stop, or target "
        "built on this data is unreliable until the range normalises."))
    out.append(table(
        ["Signal of unusual volatility", "Correct response"],
        [
            ["A single 15M range several multiples of the session's typical range", "Stand aside; do "
             "not treat the wick or the close as meaningful structure"],
            ["A scheduled high-impact release due within the next 15\u201330 minutes", "Stand aside before "
             "the release; wait for the post-news 15M close to re-establish structure"],
            ["Spread widening well beyond its normal level around the release", "Treat as a cost signal "
             "on top of the volatility signal \u2014 both argue for standing aside"],
        ]
    ))

    # ------------------------------------------------------------------
    # 8.8 No trade vs fear; psychology
    # ------------------------------------------------------------------
    out.append(h2("8.8", "\u201cNo trade exists\u201d vs \u201cI am afraid to take a valid trade\u201d"))
    out.append(key("The distinguishing test",
        "\u201cNo trade exists\u201d means one or more of the sixteen conditions in \u00a78.1 is genuinely "
        "present, or the 13-step sequence (Module 4) has not actually completed. \u201cI am afraid of a "
        "valid trade\u201d means every step has genuinely completed and R:R clears 1:2, but hesitation comes "
        "from something other than the chart \u2014 a recent loss, account size, or fear of being wrong. "
        "The chart does not change based on which of these is happening; only the correct response does."
    ))
    out.append(chart(img("m8_psychology_matrix.png"),
        "Figure 8.8 \u2014 The sequence itself is what tells the two situations apart, never how the trade "
        "feels. Below: four named biases and the same countermeasure for each \u2014 the written sequence is "
        "the only permission to enter or exit."))
    out.append(table(
        ["Bias", "What it looks like", "Countermeasure"],
        [
            ["FOMO", "Entering late or oversized because a move is already happening without you",
             "The entry sequence has a defined location and confirmation requirement (Module 4); a move "
             "already extended past that location fails step 6\u20137 regardless of how it feels to watch "
             "it run"],
            ["Revenge trading", "Re-entering immediately after a loss to \u201cwin it back,\u201d skipping "
             "steps of the sequence", "A loss on a correctly-qualified trade is not evidence anything was "
             "wrong (Module 1); the next trade must independently pass all 13 steps"],
            ["Overtrading", "Taking setups below the minimum conditions in \u00a78.1 just to stay active",
             "The minimum conditions do not loosen because no qualifying trade has appeared recently"],
            ["Confirmation bias", "Reading ambiguous structure as supporting a view already formed",
             "The 8-point framework (WHAT/WHY/WHERE/HOW to identify/HOW to use/WHEN unreliable/WHAT "
             "invalidates/example) forces an explicit check against a fixed set of criteria, not a "
             "feeling"],
        ]
    ))

    out.append(quiz(
        "A trader takes a small loss on a trade that satisfied all 13 steps of the entry sequence and had "
        "an honest 1:2.4 R:R. Ten minutes later, on the same instrument, a new setup appears that also "
        "satisfies all 13 steps with an honest R:R. The trader hesitates, feeling like they should \u201clet "
        "the market calm down first.\u201d What does this situation represent?",
        [
            {"label": "No trade exists \u2014 two losses close together mean market conditions have become "
             "unreliable.",
             "correct": False,
             "feedback": "<p><strong>A prior loss on a correctly-qualified trade is not one of the "
                         "sixteen conditions in \u00a78.1.</strong> \u00a78.8 is explicit that Module 1 already "
                         "established a properly qualified trade can still lose \u2014 that is normal "
                         "probability, not evidence the market has become unreadable. The new setup "
                         "described here has independently passed all 13 steps with an honest R:R.</p>"},
            {"label": "Fear of a valid trade \u2014 the new setup has genuinely passed the sequence; the "
             "hesitation comes from the prior loss, not from the chart.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a78.8's test asks whether the sequence has "
                         "genuinely completed with an acceptable R:R \u2014 it has. The hesitation traces back "
                         "to the recent loss, which is precisely the \u201cafraid of a valid trade\u201d case "
                         "\u00a78.8 describes, and revenge-trading's mirror image: instead of overtrading out "
                         "of frustration, this is under-trading out of fear. The correct action is to take "
                         "the new trade at its normal defined size.</p>"},
            {"label": "It cannot be assessed without knowing the trader's win rate for the day so far.",
             "correct": False,
             "feedback": "<p><strong>The day's win rate so far is not part of \u00a78.8's test.</strong> "
                         "The distinguishing question is only whether the 13-step sequence has genuinely "
                         "completed with an acceptable R:R on this specific new setup \u2014 which it has "
                         "\u2014 regardless of how the day has gone up to this point.</p>"},
        ],
        hint="Apply \u00a78.8's exact test: has the sequence genuinely completed on the new setup, or not?"
    ))

    # ------------------------------------------------------------------
    # 8.9 Instrument / session caveats
    # ------------------------------------------------------------------
    out.append(h2("8.9", "Instrument and session caveats"))
    out.append(table(
        ["Instrument / session", "Stand-aside notes specific to this context"],
        [
            ["EURUSD, London 07:00\u201311:00 UK",
             "The Asian session range immediately prior often qualifies as a low-quality range in its "
             "own right \u2014 do not treat consolidation carried over from Asia as a tradable London setup "
             "on its own."],
            ["GBPUSD, London/NY overlap 13:00\u201316:00 UK",
             "Spread and slippage both tend to widen briefly around the London close (\u224816:00 UK); "
             "treat that window itself as a mild version of the excessive-cost condition in \u00a78.1."],
            ["ES / NQ, NY cash 09:30\u201316:00 ET",
             "The first 2\u20133 minutes after the open frequently produce erratic, non-structural price "
             "action; most professional discretion here treats this as a version of unusual volatility "
             "(\u00a78.7) rather than a tradable structural move."],
            ["Any instrument, correlated books",
             "Two separate \u201cvalid\u201d trades on, for example, EURUSD long and GBPUSD long during the "
             "same session may represent one real risk exposure rather than two independent ones \u2014 see "
             "Module 9 for the full correlation treatment."],
        ]
    ))

    # ------------------------------------------------------------------
    # 8.10 Practicals
    # ------------------------------------------------------------------
    out.append(h2("8.10", "Practicals"))
    out.append(prac(
        "8.1", "The Stand-Aside Log",
        "A discipline drill for building comfort with doing nothing.",
        "<ol>"
        "<li>Over one full trading session, for every setup you consider and reject, write down which "
        "specific item from \u00a78.1's sixteen-condition list applied \u2014 not a vague \u201cdidn't feel "
        "right.\u201d</li>"
        "<li>At the end of the session, count how many potential setups were rejected versus how many "
        "were taken.</li>"
        "<li>Review the rejected setups the next day: did the specific condition you cited actually hold "
        "up (e.g. did the excessively tested zone in fact fail, did the chop in fact stay unreadable)? "
        "This builds calibration between your stand-aside judgment and what the chart actually did.</li>"
        "</ol>"
    ))
    out.append(prac(
        "8.2", "The Bias Tag",
        "A drill for catching FOMO, revenge trading, overtrading, and confirmation bias in real time.",
        "<ol>"
        "<li>Before entering any trade, explicitly write down: has anything happened in the last 30 "
        "minutes (a loss, a missed move, a flat stretch) that could be influencing this decision?</li>"
        "<li>If yes, name which of the four biases in \u00a78.8's table it most resembles, then re-run the "
        "13-step sequence from scratch as if that recent event had not happened.</li>"
        "<li>Only take the trade if it independently passes the sequence on its own merits. Log every "
        "instance where naming the bias changed the decision.</li>"
        "</ol>"
    ))

    # ------------------------------------------------------------------
    # 8.11 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("8.11", "Vocabulary introduced in this module"))
    out.append(table(
        ["Term", "Definition"],
        [
            ["Chop", "Price movement with no clean HH/HL or LH/LL sequence \u2014 directionally "
             "unreadable."],
            ["Conflicting HTF context", "The 4H and 1H timeframes disagree on direction, leaving no "
             "single coherent bias to build a thesis around."],
            ["Excessively tested zone", "A zone whose resting liquidity has been substantially consumed "
             "by repeated prior reactions, reducing its reliability on a subsequent test."],
            ["Chasing", "Entering at a price with no nearby structure to place a defensible stop against, "
             "typically because a move has already run without the trader."],
            ["Manufactured target", "A take-profit level placed beyond the nearest genuine opposing "
             "structure purely to make the R:R arithmetic appear acceptable."],
            ["Unusual volatility", "Price ranges materially outside an instrument's normal behaviour for "
             "the session, making structure temporarily unreliable."],
            ["\u201cNo trade exists\u201d", "A state in which one or more of the sixteen stand-aside "
             "conditions is genuinely present, or the 13-step sequence has not completed."],
            ["\u201cAfraid of a valid trade\u201d", "A state in which the 13-step sequence has genuinely "
             "completed with an acceptable R:R, but hesitation arises from a factor unrelated to the "
             "chart."],
            ["FOMO", "Entering late or oversized because a move is happening without the trader."],
            ["Revenge trading", "Re-entering immediately after a loss specifically to recover it, "
             "bypassing the entry sequence."],
            ["Overtrading", "Taking setups that fall below the sequence's minimum conditions purely to "
             "remain active in the market."],
            ["Confirmation bias", "Interpreting ambiguous structure as supporting a view already held, "
             "rather than evaluating it against the 8-point framework independently."],
        ]
    ))

    # ------------------------------------------------------------------
    # 8.12 Summary
    # ------------------------------------------------------------------
    out.append(h2("8.12", "Summary"))
    out.append(summary([
        "Sixteen specific, nameable conditions \u2014 spanning market condition, location/confirmation, "
        "and execution/risk \u2014 are each independently sufficient to end the entry sequence before it "
        "reaches a trade.",
        "Chop and conflicting HTF context both mean no coherent direction exists yet; neither timeframe "
        "is overridden to force alignment.",
        "Weak S&R, poor liquidity, and weak 15M confirmation each fail a specific minimum bar defined in "
        "earlier modules, not a subjective feeling.",
        "An excessively tested zone has consumed some of its own reliability; a fresh zone's first test "
        "carries the most weight.",
        "Chasing means entering with no nearby structure to justify the stop \u2014 no stop distance fixes "
        "a location problem.",
        "A genuinely poor R:R and a manufactured target are both rejections, but for different reasons: "
        "one reflects the market's real terms, the other hides a bad setup behind dishonest arithmetic.",
        "Unusual volatility and major scheduled news suspend the reliability of structure itself, not "
        "just the specific setup being considered.",
        "\u201cNo trade exists\u201d and \u201cafraid of a valid trade\u201d are distinguished entirely by whether "
        "the 13-step sequence has genuinely completed \u2014 never by how the trade feels.",
        "FOMO, revenge trading, overtrading, and confirmation bias share the same countermeasure: the "
        "written sequence is the only permission to enter or exit, independent of recent results.",
    ]))

    return "\n".join(out)
