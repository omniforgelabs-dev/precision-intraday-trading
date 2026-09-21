"""
content_m7.py — Module 7: Fast Intraday Trade Management.
Exposes build() -> str (the <main> body HTML for module-07.html).
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
    # 7.0 Introduction
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "Everything before this module got you into a structurally sound position with a defined stop "
        "and target. This module governs the minutes between entry and exit \u2014 and the single rule that "
        "overrides every other consideration in that window is this: <strong>manage by structure, never "
        "by the clock.</strong> A trade that has been open 8 minutes and a trade that has been open 80 "
        "minutes are managed with the exact same five questions. Elapsed time is never one of them."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Apply the five-question management decision tree continuously to an open trade, in the "
        "correct priority order.",
        "Distinguish leaving a winning trade alone from premature stop-tightening driven by impatience.",
        "Move a stop to breakeven only when new structure justifies it, never on an early wiggle.",
        "Take partial profit at genuine interim structure without turning it into arbitrary small-target "
        "profit-grabbing.",
        "Tell momentum loss (tighten, don't exit) apart from structural failure (exit immediately) in a "
        "live, moving trade.",
        "Recognise a genuine reversal signal against an open position and act on it regardless of "
        "unrealized profit.",
        "Trail a stop by structure alone, and explain precisely why the 10\u201360 minute window from "
        "Module 1 is a description, never a rule that forces an exit.",
    ]))

    out.append(warn("Prerequisite", [
        "This module assumes Module 4's distinction between a stop-loss price and structural "
        "invalidation, Module 5's candlestick reliability rules (used here to read reversal signals "
        "mid-trade), and Module 6's stop/target/R:R mechanics. Trade management operates entirely "
        "inside the boundaries those modules already defined \u2014 it does not redefine the stop or the "
        "target, it decides what to do with them as the trade develops."
    ]))

    out.append(h2("7.1", "The management decision tree"))
    out.append(p(
        "From the moment of entry until the moment of exit, exactly five questions govern every "
        "decision. They are asked continuously \u2014 not once at entry and not on a fixed schedule \u2014 and "
        "they are asked in this order, because an earlier \u201cyes\u201d makes later questions moot."
    ))
    out.append(chart(img("m7_management_tree.png"),
        "Figure 7.1 \u2014 Five questions asked continuously while a trade is open. None of them reference "
        "elapsed time. \u201cHow long has this been open\u201d never appears among them."))
    out.append(table(
        ["#", "Question", "If yes"],
        [
            ["1", "Has price structurally invalidated the thesis?", "Exit now, regardless of elapsed "
             "time or how close price is to the original stop-loss (Module 4, \u00a74.5)."],
            ["2", "Is the move still showing momentum in your favour?", "Leave the trade alone. Do not "
             "tighten the stop out of impatience or a desire to \u201clock something in.\u201d"],
            ["3", "Has price reached a level that justifies partial profit or breakeven?", "Apply the "
             "specific rule for that level \u2014 \u00a77.2 (leaving alone), \u00a77.3 (breakeven), or \u00a77.4 "
             "(partials)."],
            ["4", "Is momentum fading without structural failure yet?", "Tighten the stop to the newest "
             "confirmed structure. Do not force an exit on fading momentum alone."],
            ["5", "Has a genuine reversal signal appeared against the position?", "Exit or reduce. A "
             "qualifying reversal signal (Module 5) outranks an unrealized profit target."],
        ]
    ))
    out.append(warn("Duration is not one of the five questions", [
        "Module 1 described trades in this system as typically lasting 10\u201360 minutes. That was always "
        "a description of what tends to happen when a structurally sound setup plays out normally \u2014 "
        "never a rule that forces an entry, an exit, or a management decision at any specific elapsed "
        "time. \u00a77.8 below works through this directly with a side-by-side example."
    ]))

    # ------------------------------------------------------------------
    # 7.2 Leaving a trade alone vs premature tightening
    # ------------------------------------------------------------------
    out.append(h2("7.2", "Leaving a winning trade alone"))
    out.append(p(
        "The most common management error in a fast-moving intraday trade is not holding on too long "
        "\u2014 it is interfering too early. Every green candle creates pressure to \u201cprotect\u201d the position "
        "by moving the stop closer. If the move has not produced any new structural point to justify "
        "that move, tightening the stop only exposes the trade to being removed by ordinary volatility."
    ))
    out.append(chart(img("m7_leave_alone.png"),
        "Figure 7.2 \u2014 Left: the stop stays at the original structural level while two pullbacks occur, "
        "because neither pullback broke structure \u2014 the move is allowed to develop. Right: the stop is "
        "dragged up under every green candle out of impatience, and a normal pullback removes the "
        "position well before the move was finished."))
    out.append(table(
        ["Signal that a trade should be left alone", "Signal that tightening is being driven by impatience, not structure"],
        [
            ["Price is making new highs (long) / new lows (short) in the trade's direction",
             "The stop is moved after every single candle regardless of what that candle did"],
            ["Pullbacks are shallow and do not break the most recent confirmed swing",
             "The stop distance shrinks to a point tighter than normal 15M noise for the instrument"],
            ["No qualifying reversal signal (Module 5) has appeared",
             "The reason given for moving the stop is a feeling (\u201cI want to protect this\u201d) rather than "
             "a specific new structural point"],
        ]
    ))

    # ------------------------------------------------------------------
    # 7.3 Breakeven
    # ------------------------------------------------------------------
    out.append(h2("7.3", "Moving to breakeven"))
    out.append(key("The breakeven rule",
        "Move the stop to breakeven only when a genuine new structural point (a fresh swing high/low "
        "beyond entry) has formed to justify it. Moving to breakeven on an early bounce with no new "
        "structure behind it removes trades that had no structural problem at all, purely because of a "
        "normal retracement."
    ))
    out.append(chart(img("m7_breakeven.png"),
        "Figure 7.3 \u2014 Left: a fresh higher-low prints structurally above entry before the stop moves "
        "\u2014 breakeven now reflects real structure. Right: breakeven is moved after only a small, early "
        "bounce with no new swing point, and a normal retracement stops out a trade that had no "
        "structural problem."))
    out.append(p(
        "The test is identical to the one used for tightening in \u00a77.2: has a new, genuine structural "
        "point actually formed, or is the stop being moved because of how the trade feels? A breakeven "
        "move is a structural decision, made from the same evidence Module 2 uses to identify any other "
        "swing point \u2014 not a psychological reward for being briefly in profit."
    ))

    out.append(quiz(
        "A long trade is 12 pips into profit. Price has pulled back slightly twice, each time by 2\u20133 "
        "pips, without printing any new confirmed swing low above the entry price. Should the stop be "
        "moved to breakeven now?",
        [
            {"label": "Yes \u2014 12 pips of profit is enough of a buffer to justify locking in breakeven.",
             "correct": False,
             "feedback": "<p><strong>The size of the unrealized profit is not the test \u00a77.3 uses.</strong> "
                         "The breakeven rule requires a genuine new structural point \u2014 a fresh swing "
                         "beyond entry \u2014 not a specific amount of unrealized profit. Figure 7.3's right "
                         "panel shows exactly this mistake: moving the stop on a small early bounce, with "
                         "no new swing, gets the trade removed by a completely normal retracement.</p>"},
            {"label": "No \u2014 without a new confirmed swing point beyond entry, there is no structural "
             "basis for the move yet.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a77.3's rule is explicit: breakeven requires a "
                         "genuine new structural point, not a specific profit amount or a shallow bounce. "
                         "Two small pullbacks with no new confirmed swing low provide no such point. Moving "
                         "the stop now would expose the trade to being stopped out by the kind of ordinary "
                         "noise shown in Figure 7.3's right panel.</p>"},
            {"label": "Yes, but only if the original stop distance was more than 20 pips.",
             "correct": False,
             "feedback": "<p><strong>The original stop distance is not part of the breakeven test "
                         "either.</strong> \u00a77.3 evaluates whether new structure has formed beyond entry "
                         "\u2014 it says nothing about the size of the original stop. A wide original stop and "
                         "a narrow one are judged by the exact same structural criterion.</p>"},
        ],
        hint="Re-read the breakeven rule in \u00a77.3 \u2014 what specific thing does it require, and is it "
             "present here?"
    ))

    # ------------------------------------------------------------------
    # 7.4 Partial profit-taking
    # ------------------------------------------------------------------
    out.append(h2("7.4", "Partial profit-taking"))
    out.append(p(
        "Taking partial profit at a genuine interim structural level is not the same thing as the "
        "small-target profit-grabbing this system explicitly rejects (Module 1). The distinction is "
        "whether the level being used is real, opposing structure the price had to fight through on its "
        "way to the final target \u2014 not an arbitrary price chosen because it felt like \u201cenough.\u201d"
    ))
    out.append(chart(img("m7_partial_profit.png"),
        "Figure 7.4 \u2014 A portion of the position is closed at the first real opposing structure the "
        "move reaches. The remainder of the position stays open, still targeting the original structural "
        "level identified at entry (Module 6, \u00a76.3)."))
    out.append(table(
        ["Valid partial profit", "Invalid \u201cprofit-grabbing\u201d"],
        [
            ["Taken at a real, identifiable opposing structure (a prior swing high/low, a graded zone)",
             "Taken at an arbitrary price with no structural basis, purely because it felt like a "
             "reasonable gain"],
            ["A portion of size is closed; the remainder continues toward the original structural target",
             "The entire position is closed early, abandoning the structural target defined at entry"],
            ["Consistent with the plan defined before entry, not decided reactively mid-trade out of fear",
             "Decided in the moment out of a fear the gain might disappear"],
        ]
    ))

    # ------------------------------------------------------------------
    # 7.5 Momentum loss vs structural failure
    # ------------------------------------------------------------------
    out.append(h2("7.5", "Momentum loss vs structural failure"))
    out.append(p(
        "Both situations look similar in the moment: the trade stalls, candles shrink, progress slows. "
        "Only one of them requires an exit. The entire distinction rests on a single test: has the "
        "specific structural point the thesis depends on actually broken, or has the move simply lost "
        "speed while structure still holds?"
    ))
    out.append(chart(img("m7_momentum_vs_failure.png"),
        "Figure 7.5 \u2014 Left: candles shrink and progress stalls, but the last swing low the thesis "
        "depends on still holds \u2014 tighten the stop, do not exit. Right: the identical stall is followed "
        "by a genuine 15M close below that same swing low \u2014 structural failure, exit immediately "
        "without waiting for the original stop-loss price."))
    out.append(table(
        ["Test", "Momentum loss (tighten, hold)", "Structural failure (exit now)"],
        [
            ["Has the swing point the thesis depends on been closed through on the 15M?", "No", "Yes"],
            ["Candle size relative to the earlier part of the move", "Shrinking, indecisive",
             "Can be shrinking or large \u2014 irrelevant once the level breaks"],
            ["Correct response", "Tighten stop to newest confirmed structure; leave the trade open",
             "Exit immediately, regardless of the original stop-loss price"],
        ]
    ))
    out.append(dev("Developer's-eye analogy", [
        "Momentum loss is like a request-per-second graph flattening out during a load test \u2014 something "
        "is slowing down, worth watching closely, but no defined SLA has actually been breached yet. "
        "Structural failure is the SLA breach itself: a specific, pre-defined threshold has been crossed, "
        "and the correct response is the pre-agreed incident response, immediately \u2014 not waiting to see "
        "if the graph gets worse."
    ]))

    # ------------------------------------------------------------------
    # 7.6 Reversal signals
    # ------------------------------------------------------------------
    out.append(h2("7.6", "Reversal signals against an open position"))
    out.append(p(
        "A genuine reversal signal is evidence, exactly as defined in Module 5, and it does not lose "
        "its validity just because it appears against a position that is currently profitable. A trader "
        "who ignores a qualifying reversal signal purely because the trade is \u201cwinning\u201d is applying a "
        "double standard: the same candle at the same location would have been treated as meaningful "
        "evidence before entry."
    ))
    out.append(chart(img("m7_reversal_signal.png"),
        "Figure 7.6 \u2014 The position is still profitable and the original stop has not been touched. A "
        "strong bearish engulfing candle (Module 5, \u00a75.3) prints at the highs \u2014 a qualifying reversal "
        "signal that changes the picture regardless of unrealized profit."))
    out.append(warn("Not every wiggle is a reversal signal", [
        "This is not a license to exit on the first red candle inside a winning trade. The same Module 5 "
        "reliability criteria apply here as anywhere else: the candle must actually qualify (body-to-range "
        "ratio, location, liquidity context) as one of the named patterns \u2014 a rejection candle, an "
        "engulfing candle, a momentum candle against the position. A single ordinary red candle inside a "
        "healthy pullback is not a reversal signal, and question 5 in \u00a77.1's decision tree should only "
        "return \u201cyes\u201d when the Module 5 criteria are genuinely met."
    ]))

    out.append(quiz(
        "A long position is well into profit. A single small red candle prints with a body-to-range "
        "ratio around 50%, no long wick, at a random price with no zone or liquidity nearby. Does this "
        "qualify as a reversal signal under question 5 of \u00a77.1's decision tree?",
        [
            {"label": "Yes \u2014 any red candle against an open long is worth reducing risk over.",
             "correct": False,
             "feedback": "<p><strong>This is exactly the over-reaction \u00a77.6's warning box is written to "
                         "prevent.</strong> A red candle is not automatically a reversal signal. It must "
                         "actually meet one of the named, qualifying Module 5 patterns \u2014 a genuine "
                         "rejection candle, engulfing candle, or momentum candle \u2014 at a meaningful "
                         "location. An ordinary 50%-body candle with no long wick, at a random price with "
                         "no zone or liquidity nearby, meets none of those criteria.</p>"},
            {"label": "No \u2014 it does not meet any of the Module 5 pattern definitions or location "
             "requirements, so question 5 should return \u201cno\u201d here.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a77.6 is explicit that the same Module 5 "
                         "reliability criteria used before entry apply to reversal signals evaluated "
                         "mid-trade. An ordinary candle with a moderate body, no long wick, and no "
                         "supporting location does not qualify as a rejection candle, an engulfing candle, "
                         "or a momentum candle \u2014 so it provides no basis for question 5 to return "
                         "\u201cyes.\u201d The correct response is to continue applying the earlier questions in "
                         "\u00a77.1's tree as normal.</p>"},
            {"label": "It depends only on how much unrealized profit the trade currently has.",
             "correct": False,
             "feedback": "<p><strong>Unrealized profit size plays no role in whether a candle qualifies "
                         "as a reversal signal.</strong> The test is entirely about whether the candle "
                         "meets one of Module 5's defined pattern criteria at a meaningful location \u2014 "
                         "exactly the same test used before entry, applied without regard to the current "
                         "P&L of the position.</p>"},
        ],
        hint="Check the candle against Module 5's actual pattern definitions (body-to-range ratio, wick, "
             "location) rather than just its colour."
    ))

    # ------------------------------------------------------------------
    # 7.7 Structure-based trailing and full exit
    # ------------------------------------------------------------------
    out.append(h2("7.7", "Structure-based trailing and full exit"))
    out.append(p(
        "For a trade that continues in legs, the stop steps up (long) or down (short) behind each new "
        "confirmed swing as the move progresses \u2014 never on a timer, and never by a fixed pip distance "
        "disconnected from what the chart is actually doing."
    ))
    out.append(chart(img("m7_trailing.png"),
        "Figure 7.7 \u2014 The stop steps up behind each new confirmed swing low as the move progresses in "
        "three legs. Each move of the stop is triggered by a genuine new swing forming, never by elapsed "
        "time or a fixed pip trail."))
    out.append(table(
        ["Exit type", "Trigger"],
        [
            ["Full exit at structural invalidation", "The specific structural point the thesis depends "
             "on breaks (question 1, \u00a77.1) \u2014 highest priority, overrides everything else."],
            ["Full exit at the original structural target", "Price reaches the target defined at entry "
             "(Module 6, \u00a76.3) and the position (or its remaining portion) is closed there."],
            ["Full exit on a genuine reversal signal", "A qualifying Module 5 pattern appears against "
             "the position at a meaningful location (question 5, \u00a77.1)."],
            ["Trailed exit", "The trailed stop \u2014 stepped up behind each new confirmed swing \u2014 is "
             "eventually touched by a pullback that does not itself represent structural failure."],
        ]
    ))

    out.append(quiz(
        "A short position has trailed its stop down behind three confirmed swing highs as the move "
        "progressed in legs. Price has now pulled back and touched the current trailed stop, closing the "
        "position for a smaller profit than the peak unrealized gain. Was this exit correct?",
        [
            {"label": "No \u2014 the trade should have been held for the full move since the original "
             "structural target was never reached.",
             "correct": False,
             "feedback": "<p><strong>A trailed stop being touched is a designed outcome of trailing, not "
                         "a mistake.</strong> \u00a77.7 describes the stop stepping up behind each new "
                         "confirmed swing specifically so that a pullback that goes far enough will "
                         "eventually close the trade with some of the accumulated gain protected. Holding "
                         "past a legitimately trailed stop touch would mean the trailing stop was never "
                         "actually being respected.</p>"},
            {"label": "Yes \u2014 the stop was moved only behind genuine new swings as they formed, and "
             "being touched by a later pullback is the trailing mechanism working as intended.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a77.7 is explicit that a trailed exit \u2014 the "
                         "trailed stop eventually being touched by a pullback that isn't itself structural "
                         "failure \u2014 is one of the four defined exit types, distinct from exiting at the "
                         "original target or on invalidation. Closing with less than the peak unrealized "
                         "gain is the expected cost of trailing, not a sign anything went wrong.</p>"},
            {"label": "It cannot be judged without knowing how many minutes the trade was open.",
             "correct": False,
             "feedback": "<p><strong>Duration plays no role in judging this exit.</strong> \u00a77.1 and "
                         "\u00a77.7 both evaluate management decisions purely on structure \u2014 whether the "
                         "stop was moved only behind genuine new swings, and whether the eventual touch "
                         "represented the trailing mechanism working correctly. Elapsed time is never part "
                         "of that judgment.</p>"},
        ],
        hint="Re-read \u00a77.7's four exit types \u2014 is a trailed stop being touched a failure, or one of "
             "the defined, expected outcomes?"
    ))

    # ------------------------------------------------------------------
    # 7.8 Duration is descriptive, not a rule
    # ------------------------------------------------------------------
    out.append(h2("7.8", "Duration is descriptive, not a rule"))
    out.append(key("Why the 10\u201360 minute window is not a timer",
        "Module 1 introduced 10\u201360 minutes as typical for this system's trades \u2014 a description of how "
        "long a structurally sound 15M setup tends to take to reach its resolution, not a countdown that "
        "forces an exit. A trade that is still developing normally past 60 minutes, with no structural "
        "invalidation, no reversal signal, and momentum still intact, is held exactly as it would be at "
        "minute 25 \u2014 by the same five questions in \u00a77.1, asked again."
    ))
    out.append(chart(img("m7_time_not_a_rule.png"),
        "Figure 7.8 \u2014 Left: the identical trade is force-closed at the 60-minute mark purely on "
        "elapsed time, cutting off a move that was still fully valid by every structural measure. Right: "
        "the same trade is held because structure never failed, and it is managed to a materially better "
        "result using nothing but the tools already covered in this module."))
    out.append(p(
        "The reverse error is just as real: holding a trade well past its structural invalidation point "
        "purely because \u201cit hasn't been very long yet\u201d is the same mistake in the opposite direction. "
        "Neither a minimum holding time nor a maximum holding time exists in this system. Question 1 in "
        "\u00a77.1's decision tree \u2014 has the thesis structurally invalidated \u2014 can return \u201cyes\u201d at minute "
        "3 or minute 90, and the correct response is identical either way: exit immediately."
    ))

    # ------------------------------------------------------------------
    # 7.9 Instrument / session caveats
    # ------------------------------------------------------------------
    out.append(h2("7.9", "Instrument and session caveats"))
    out.append(table(
        ["Instrument / session", "Management notes"],
        [
            ["EURUSD, London 07:00\u201311:00 UK",
             "Pullbacks inside a valid trend leg are typically shallow (a few pips); a pullback deep "
             "enough to touch a properly-placed trailed stop is usually a genuine sign of exhaustion, "
             "not ordinary noise."],
            ["GBPUSD, London/NY overlap 13:00\u201316:00 UK",
             "Faster, larger pullbacks are normal here \u2014 a trailed stop needs to sit correspondingly "
             "further from price than on EURUSD to avoid being clipped by ordinary volatility rather than "
             "genuine reversal."],
            ["ES / NQ, NY cash 09:30\u201316:00 ET",
             "Momentum candles and fast retracements are both common; distinguishing momentum loss from "
             "structural failure requires watching the specific swing level closely rather than reacting "
             "to the size of individual candles, which can be large in both directions without breaking "
             "structure."],
            ["Any instrument, scheduled news mid-trade",
             "A scheduled release occurring while a trade is open can produce a large wick that looks "
             "like a reversal signal or a structural break but is really a liquidity/volatility spike "
             "(Module 5, \u00a75.4). Wait for the post-news 15M close before treating it as genuine "
             "evidence."],
        ]
    ))

    # ------------------------------------------------------------------
    # 7.10 Practicals
    # ------------------------------------------------------------------
    out.append(h2("7.10", "Practicals"))
    out.append(prac(
        "7.1", "The Five-Question Log",
        "A real-time or historical discipline drill.",
        "<ol>"
        "<li>For one open (or historical) trade, write down the five questions from \u00a77.1's decision "
        "tree.</li>"
        "<li>At 3\u20134 points as the trade develops, answer all five questions in writing, in order, "
        "based only on what the chart shows at that moment \u2014 not on how the trade feels.</li>"
        "<li>Note any moment where you were tempted to act based on elapsed time (\u201cthis has been open "
        "a while, I should do something\u201d) rather than a \"yes\" to one of the five questions. Write down "
        "what the correct, structure-based action was instead.</li>"
        "<li>After the trade closes, review whether any management decision was made for a reason "
        "outside the five questions. If so, identify which of \u00a77.2\u2013\u00a77.6's specific rules was "
        "violated.</li>"
        "</ol>"
    ))
    out.append(prac(
        "7.2", "The Breakeven/Partial Justification Test",
        "A pre-commitment drill to prevent reactive stop and target decisions.",
        "<ol>"
        "<li>Before entering your next 5 trades (real or simulated), write down in advance the specific "
        "structural condition that would justify moving to breakeven, and the specific structural level "
        "that would justify a partial profit, using \u00a77.3 and \u00a77.4's criteria.</li>"
        "<li>As each trade develops, only act on breakeven or partials when the pre-written condition is "
        "actually met \u2014 not when the trade merely reaches a round-number profit or \u201cfeels\u201d far enough "
        "along.</li>"
        "<li>Log any instance where you were tempted to act early, and what happened to price shortly "
        "afterward. Over enough trades, this builds direct evidence of whether premature action costs "
        "more than it protects.</li>"
        "</ol>"
    ))

    # ------------------------------------------------------------------
    # 7.11 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("7.11", "Vocabulary introduced in this module"))
    out.append(table(
        ["Term", "Definition"],
        [
            ["Momentum loss", "A slowdown in the pace or size of favourable price movement, without any "
             "structural point the thesis depends on actually breaking."],
            ["Structural failure (mid-trade)", "The specific structural point an open trade's thesis "
             "depends on breaking, independent of whether the original stop-loss price has been touched."],
            ["Breakeven", "Moving the stop to the entry price, justified only by a genuine new structural "
             "point (a fresh swing) forming beyond entry."],
            ["Partial profit-taking", "Closing a portion of a position at a genuine interim opposing "
             "structure while the remainder continues toward the original structural target."],
            ["Structure-based trailing", "Moving a stop behind each new confirmed swing as a move "
             "progresses in legs, as opposed to a fixed pip trail or a time-based adjustment."],
            ["Reversal signal (mid-trade)", "A qualifying Module 5 candlestick pattern appearing against "
             "an open position at a meaningful location, evaluated by the same reliability criteria as "
             "before entry."],
            ["Trailed exit", "A full exit that occurs when a structure-based trailing stop is eventually "
             "touched by a pullback that is not itself structural failure."],
        ]
    ))

    # ------------------------------------------------------------------
    # 7.12 Summary
    # ------------------------------------------------------------------
    out.append(h2("7.12", "Summary"))
    out.append(summary([
        "Trade management is governed by five continuously-asked questions; elapsed time is never one "
        "of them.",
        "A winning trade with intact momentum and no new structural failure should be left alone, not "
        "tightened out of impatience.",
        "Breakeven requires a genuine new structural point beyond entry \u2014 not a profit amount, not an "
        "early wiggle.",
        "Partial profit-taking is valid only at genuine interim opposing structure, with the remaining "
        "size still targeting the original structural level.",
        "Momentum loss (tighten, don't exit) and structural failure (exit immediately) are distinguished "
        "entirely by whether the swing point the thesis depends on has actually broken.",
        "A genuine Module 5 reversal signal against an open position outranks unrealized profit, "
        "regardless of how far into profit the trade is.",
        "Structure-based trailing steps the stop behind each new confirmed swing; a trailed stop being "
        "touched by a later pullback is the mechanism working as intended, not a failure.",
        "The 10\u201360 minute window from Module 1 is a description of typical duration, never a rule \u2014 "
        "exit on structural invalidation whenever it occurs, and hold past 60 minutes whenever structure "
        "still supports it.",
    ]))

    return "\n".join(out)
