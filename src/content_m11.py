"""
content_m11.py — Module 11: The Final Rulebook.
Exposes build() -> str (the <main> body HTML for module-11.html).
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
    # 11.0 Introduction
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "This module does not introduce new concepts. Every rule below is a restatement of something "
        "already taught, in Modules 1\u201310, compressed into a form that can be read in under a minute "
        "before a trade and reviewed in a few minutes after one. If a rule here contradicts your memory "
        "of an earlier module, the earlier module's fuller explanation is correct \u2014 this is a summary, "
        "not a replacement."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Recite the six core, non-negotiable principles that every other rule in this course derives "
        "from.",
        "Locate the specific rule governing any decision point in the trade sequence, organised by "
        "category.",
        "Run a pre-trade checklist that either clears a setup or correctly stands you aside.",
        "Run a post-trade review that distinguishes a correctly-priced loss from an execution mistake.",
        "Describe the backtesting \u2192 forward testing \u2192 demo \u2192 live pipeline and why no stage may be "
        "skipped.",
        "Journal a trade so that recurring mistakes become visible instead of invisible.",
    ]))

    # ------------------------------------------------------------------
    # 11.1 Core principles
    # ------------------------------------------------------------------
    out.append(h2("11.1", "Core principles"))
    out.append(p(
        "Every rule in \u00a711.2 is a specific application of one of the six statements below. When a "
        "rule seems ambiguous in a live situation, resolve the ambiguity by asking which of these six it "
        "is protecting \u2014 not by guessing."
    ))
    out.append(chart(img("m11_core_principles.png"),
        "Figure 11.1 \u2014 The six non-negotiable statements underneath every other rule in this course."))
    out.append(table(
        ["#", "Principle", "Where it was established"],
        [
            ["1", "Direction is set on the 4H, refined on the 1H, executed on the 15M \u2014 never the "
             "reverse.", "Module 1, \u00a71.4; Module 4, \u00a74.2\u2013\u00a74.3"],
            ["2", "A completed 15M candle close is the only form of confirmation this system accepts.",
             "Module 1, \u00a71.6; Module 4, \u00a74.6"],
            ["3", "Stops and targets are structural, read from price \u2014 never arbitrary distances or "
             "manufactured to fit a number.", "Module 6, \u00a76.2\u2013\u00a76.3"],
            ["4", "No trade clears the sequence below a 1:2 reward-to-risk ratio, without exception.",
             "Module 1, \u00a71.9; Module 6, \u00a76.4"],
            ["5", "Position size is solved backward from a fixed risk percentage and the stop distance "
             "\u2014 never chosen first.", "Module 9, \u00a79.1"],
            ["6", "Standing aside is a valid, frequent, and often correct outcome of running the "
             "sequence.", "Module 8, entire module"],
        ]
    ))

    # ------------------------------------------------------------------
    # 11.2 The complete rule map
    # ------------------------------------------------------------------
    out.append(h2("11.2", "The complete rule map"))
    out.append(p(
        "Sixteen rule categories, grouped into five functional clusters. Each table below states the "
        "rule and cites the module section it was derived from \u2014 nothing here is new; it is compressed."
    ))
    out.append(chart(img("m11_rule_map.png"),
        "Figure 11.2 \u2014 The sixteen categories and how they cluster into direction/context, "
        "structure/liquidity, execution, protection, and discipline."))

    out.append(h3("Direction &amp; context"))
    out.append(table(
        ["Category", "Rule"],
        [
            ["4H rules", "4H direction must show an unambiguous HH/HL or LH/LL sequence with no "
             "conflicting recent swing. This is Gate 1 \u2014 a binary pass/fail, not a preference "
             "(Module 2, \u00a72.2; Module 4, \u00a74.3)."],
            ["1H rules", "1H must supply a location that satisfies \u22652 of origin, liquidity, or flip "
             "(Module 3, \u00a73.2\u2013\u00a73.4; Module 4, \u00a74.4). The 1H never overrides the 4H direction."],
            ["15M rules", "15M supplies confirmation only, never direction. No timeframe below 15M is "
             "used for entry refinement (Module 1, \u00a71.7; Module 4, \u00a74.6\u2013\u00a74.7)."],
        ]
    ))

    out.append(h3("Structure &amp; liquidity"))
    out.append(table(
        ["Category", "Rule"],
        [
            ["S&amp;R rules", "Zones are built from bodies, wicks, repeated reaction, displacement "
             "origin, or pre-expansion consolidation \u2014 never a single thin line (Module 3, \u00a73.1\u2013"
             "\u00a73.2). Zone width is derived from the price behaviour that created it."],
            ["Liquidity rules", "Liquidity is mapped as resting orders around obvious swing points before "
             "a trade is considered; a genuine sweep-and-reclaim strengthens a setup, an unresolved sweep "
             "against it weakens one (Module 3, \u00a73.5)."],
        ]
    ))

    out.append(h3("Execution"))
    out.append(table(
        ["Category", "Rule"],
        [
            ["Entry rules", "Entry occurs only after a completed 15M structure shift closes through the "
             "relevant level \u2014 never on an open or forming candle, never on anticipation (Module 4, "
             "\u00a74.6\u2013\u00a74.8; Module 6, \u00a76.7 on not chasing)."],
            ["Stop rules", "The stop sits beyond the specific price level that disproves the trade "
             "thesis \u2014 never a fixed pip/point count chosen to fit a preferred position size (Module 6, "
             "\u00a76.2)."],
            ["Take-profit rules", "The target is the nearest genuine opposing structure \u2014 never widened "
             "or manufactured to clear the R:R minimum (Module 6, \u00a76.3)."],
            ["R:R rules", "Minimum 1:2, calculated from actual entry/stop/target prices, before entry. "
             "Below 1:2 \u2192 stand aside, do not adjust the target to compensate (Module 6, \u00a76.4; Module "
             "8, \u00a78.6)."],
            ["Management rules", "A continuous five-question loop (invalidation? momentum? "
             "breakeven/partial level? fading momentum? reversal signal?) replaces any clock-based exit. "
             "A reversal signal outranks unrealized profit (Module 7, \u00a77.2\u2013\u00a77.5)."],
        ]
    ))

    out.append(h3("Protection"))
    out.append(table(
        ["Category", "Rule"],
        [
            ["No-trade rules", "Any one of the sixteen stand-aside conditions (Module 8, Fig 8.1) is "
             "independently sufficient to end the sequence \u2014 conditions do not need to occur together."],
            ["Risk rules", "Position size = (Account \u00d7 Risk %) \u00f7 (Stop distance \u00d7 value per unit). "
             "Risk % is fixed in advance and derived from the specific prop firm's own limits, never a "
             "generic number (Module 9, \u00a79.1, \u00a79.7)."],
            ["News/event rules", "Scheduled high-impact news is a stand-aside or flatten-exposure "
             "condition, not a sizing problem \u2014 a stop-loss does not guarantee fill price during a gap "
             "(Module 9, \u00a79.5)."],
            ["Correlation rules", "Positions sharing an underlying driver are sized as one combined risk "
             "against a per-driver limit, never stacked independently (Module 9, \u00a79.4)."],
        ]
    ))

    out.append(h3("Discipline"))
    out.append(table(
        ["Category", "Rule"],
        [
            ["Psychology rules", "FOMO, revenge trading, overtrading, and confirmation bias are named "
             "and countered by one rule: the written sequence is the only permission to enter or exit "
             "(Module 8, \u00a78.8)."],
            ["Trade-review rules", "Every trade, win or loss, is logged and reviewed against the "
             "checklist that preceded it \u2014 see \u00a711.4 and \u00a711.6 below."],
        ]
    ))

    out.append(quiz(
        "A trader identifies a 4H uptrend, a qualifying 1H demand zone, and a valid 15M bullish "
        "structure shift. The calculated R:R to the nearest genuine opposing structure is 1:1.6. There "
        "is no scheduled news, no correlated exposure, and no other stand-aside condition present. "
        "According to the rule map, what should happen?",
        [
            {"label": "Take the trade at a reduced size, since every other condition is favourable and "
             "1:1.6 is close to the minimum.",
             "correct": False,
             "feedback": "<p><strong>\u201cClose to the minimum\u201d is not the minimum.</strong> The R:R "
                         "rule (\u00a76.4, restated in \u00a711.2) sets 1:2 as a hard floor, not a target to "
                         "approximate. Reducing size does not fix an R:R shortfall \u2014 it only reduces the "
                         "dollar amount of a trade that still fails the rule.</p>"},
            {"label": "Stand aside \u2014 the R:R rule is a hard floor, and every other favourable condition "
             "does not compensate for a single failed gate.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> Principle 4 and \u00a76.4 are explicit: no trade "
                         "clears the sequence below 1:2, without exception. This mirrors Module 8's "
                         "point that any single stand-aside condition is independently sufficient to end "
                         "the sequence \u2014 the other gates passing does not offset the one that failed.</p>"},
            {"label": "Widen the target slightly to the next visible price level so the R:R clears 1:2.",
             "correct": False,
             "feedback": "<p><strong>This is exactly the manufactured target \u00a76.3 forbids.</strong> "
                         "The target must be the nearest genuine opposing structure \u2014 selecting a "
                         "different, more distant level purely to make the arithmetic clear the minimum "
                         "is manufacturing the number, not finding it in the chart.</p>"},
        ],
        hint="Check whether every one of the four gates in \u00a76 and \u00a78 independently passed, not "
             "whether the overall picture 'feels' good."
    ))

    # ------------------------------------------------------------------
    # 11.3 Pre-trade checklist
    # ------------------------------------------------------------------
    out.append(h2("11.3", "Pre-trade checklist"))
    out.append(p(
        "Run every item before every entry, in order. This checklist does not award partial credit \u2014 "
        "a single \u201cno\u201d means stand aside, regardless of how strong the other items are."
    ))
    out.append(chart(img("m11_pretrade_checklist.png"),
        "Figure 11.3 \u2014 The complete pre-trade checklist, thirteen items, run top to bottom before "
        "every entry."))
    out.append(warn("How to use this checklist in practice", [
        "Write the answer down, even briefly \u2014 \u201cyes\u201d thought silently under time pressure is far "
        "easier to talk yourself past than \u201cyes\u201d written on paper or typed into a journal.",
        "The final item (\u201cI am taking this size because the checklist passed\u201d) exists specifically to "
        "catch chasing and revenge trading (Module 8, \u00a78.8) \u2014 answer it honestly even when every "
        "technical item has passed."
    ]))

    # ------------------------------------------------------------------
    # 11.4 Post-trade review checklist
    # ------------------------------------------------------------------
    out.append(h2("11.4", "Post-trade review checklist"))
    out.append(p(
        "Complete this for every closed trade \u2014 wins included \u2014 before taking the next one. This is "
        "the single habit most responsible for turning a strategy with a real edge into an account that "
        "survives long enough to realise it."
    ))
    out.append(chart(img("m11_posttrade_checklist.png"),
        "Figure 11.4 \u2014 The complete post-trade review checklist, nine items, completed after every "
        "closed trade regardless of outcome."))

    # ------------------------------------------------------------------
    # 11.5 Strategy failure vs execution failure
    # ------------------------------------------------------------------
    out.append(h2("11.5", "Strategy failure vs execution failure"))
    out.append(p(
        "Every loss falls into exactly one of these two categories, and confusing them causes two "
        "opposite mistakes: abandoning a genuinely sound method after a normal losing streak, or "
        "persisting with a genuinely broken process because \u201cthe market was just against me.\u201d"
    ))
    out.append(chart(img("m11_failure_types.png"),
        "Figure 11.6 \u2014 The single diagnostic question that separates a strategy-consistent loss from "
        "an execution failure, and the correct response to each."))
    out.append(table(
        ["", "Execution failure", "Strategy failure (strategy-consistent loss)"],
        [
            ["What happened", "A rule was skipped or bent \u2014 chased entry, moved stop, oversized, "
             "skipped a checklist item", "Every rule was followed exactly, and the trade still lost"],
            ["What it means", "The written sequence would likely have produced a different outcome",
             "This is expected, priced-in behaviour \u2014 Module 1's expectancy math assumes real losses"],
            ["Correct response", "Retrain the specific discipline that slipped \u2014 identify it precisely "
             "using the post-trade checklist", "Nothing changes after one loss; look for patterns over "
             "many trades, not single outcomes"],
        ]
    ))

    out.append(quiz(
        "A trader takes a fully qualified long trade: every pre-trade checklist item passes, entry, "
        "stop, and target are exactly where the structure indicates, and the position is managed "
        "according to the five-question loop throughout. The trade is stopped out for a full 1R loss "
        "when a genuine, valid 15M bearish structure shift invalidates the setup. How should this loss "
        "be classified and treated?",
        [
            {"label": "Execution failure \u2014 the trader should have exited earlier to avoid the full "
             "loss.",
             "correct": False,
             "feedback": "<p><strong>Exiting earlier without a rule-based trigger would itself be an "
                         "execution failure.</strong> The scenario states the five-question loop was "
                         "followed throughout \u2014 there was no premature or overdue action. A stop that "
                         "executes exactly where it was structurally placed, on a genuine invalidation, "
                         "is the system working as designed.</p>"},
            {"label": "Strategy failure \u2014 the entry model itself needs to be revised after this loss.",
             "correct": False,
             "feedback": "<p><strong>A single loss, correctly taken, is not evidence the method needs "
                         "revising.</strong> Module 1's honest expectancy arithmetic (\u00a71.9) assumes a "
                         "meaningful fraction of qualified trades will lose. \u00a711.5 explicitly warns "
                         "against treating one strategy-consistent loss as grounds to abandon or rebuild "
                         "the method \u2014 that judgement requires a pattern across many trades.</p>"},
            {"label": "A strategy-consistent loss \u2014 every rule was followed, the outcome was one of "
             "the expected possibilities, and nothing about the process needs to change based on this "
             "single trade.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> The diagnostic question in Fig 11.6 (\u201cwas the "
                         "checklist genuinely satisfied and management followed exactly as written?\u201d) "
                         "answers yes here. This is the expected, priced-in downside of a positive-"
                         "expectancy system \u2014 recorded in the journal as data, not as a mistake to "
                         "correct.</p>"},
        ],
        hint="Ask the single diagnostic question from Figure 11.6 and follow where the 'yes' branch leads."
    ))

    # ------------------------------------------------------------------
    # 11.6 Testing pipeline: backtest, forward test, demo, live
    # ------------------------------------------------------------------
    out.append(h2("11.6", "Backtesting, forward testing, demo, and live execution"))
    out.append(p(
        "The sequence taught in this course is not ready for real capital simply because it is "
        "understood intellectually. Four stages exist, in order, each catching a different category of "
        "problem before it costs money."
    ))
    out.append(chart(img("m11_testing_pipeline.png"),
        "Figure 11.5 \u2014 The four-stage pipeline from backtesting to live trading, with journaling "
        "running underneath every stage."))
    out.append(table(
        ["Stage", "What it tests", "What it cannot test"],
        [
            ["Backtesting", "Whether the rules, applied with discipline to historical charts, produce "
             "qualifying setups often enough to matter, and whether the qualifying setups have a "
             "reasonable, honestly-assessed win/loss pattern", "Whether the trader can follow the rules "
             "under the pressure of live, unfolding uncertainty \u2014 hindsight removes that pressure "
             "entirely"],
            ["Forward testing", "Whether the sequence can be identified and would have been followed in "
             "real time, with no hindsight and no capital at risk", "Emotional response to real money "
             "moving \u2014 paper trading materially understates the psychological pressure of live P&amp;L"],
            ["Demo execution", "Order execution mechanics, platform behaviour, slippage assumptions, and "
             "emotional response to live-feeling but not-real P&amp;L swings", "The specific pressure of "
             "capital that, if lost, cannot be replaced by resetting a demo account"],
            ["Live", "Everything \u2014 but only after the first three stages have shown consistent "
             "rule-following", "Nothing \u2014 this is the real test, which is exactly why it should not be "
             "reached prematurely"],
        ]
    ))
    out.append(warn("What each stage is actually measuring", [
        "None of the four stages exist to prove the strategy is profitable. Module 1 already establishes "
        "that a sound, positive-expectancy method can still show a losing stretch over any small sample. "
        "What each stage measures is consistency of rule-following under progressively more realistic "
        "pressure \u2014 that is the variable actually being tested, and the only one within the trader's "
        "control."
    ]))

    # ------------------------------------------------------------------
    # 11.7 Journaling
    # ------------------------------------------------------------------
    out.append(h2("11.7", "Journaling"))
    out.append(p(
        "A journal entry is written for every trade \u2014 real or simulated, win or loss \u2014 before the "
        "next trade is taken. Without it, none of the four pipeline stages in \u00a711.6 can be evaluated "
        "honestly, because memory of past trades is reliably distorted by their outcomes."
    ))
    out.append(table(
        ["Field", "Why it is recorded"],
        [
            ["Instrument and session", "Enables later analysis of whether performance varies by "
             "instrument or session (Module 9, \u00a79.8)"],
            ["4H/1H/15M evidence at entry", "Allows a later, honest check of whether the checklist was "
             "genuinely satisfied or retroactively justified"],
            ["Entry, stop, target, calculated R:R", "The exact numbers used to compute expectancy over "
             "time, and to check for target manufacturing after the fact"],
            ["Position size and % risked", "Confirms the sizing formula (Module 9, \u00a79.1) was actually "
             "applied, not adjusted by feel"],
            ["Management actions taken", "Reveals whether the five-question loop (Module 7, \u00a77.2) was "
             "followed or overridden by impatience or fear"],
            ["Outcome and R multiple", "Raw data for the expectancy calculation and for spotting patterns "
             "across many trades"],
            ["Post-trade review answers", "The strategy-failure/execution-failure classification (\u00a711.5) "
             "for every trade, not just losses"],
        ]
    ))

    # ------------------------------------------------------------------
    # 11.8 Reviewing winners and losers, and finding recurring mistakes
    # ------------------------------------------------------------------
    out.append(h2("11.8", "Reviewing winners and losers, and finding recurring mistakes"))
    out.append(p(
        "A journal that only examines losing trades misses two things: recurring mistakes hidden inside "
        "wins, and the difference between skill and luck. Both winners and losers are reviewed against "
        "the same checklist."
    ))
    out.append(chart(img("m11_review_winners_losers.png"),
        "Figure 11.7 \u2014 The same rigor applied to reviewing winning trades as losing ones, plus how "
        "recurring mistakes are identified across many journal entries."))
    out.append(warn("A win that breaks the rules is not a good trade", [
        "If a trade entered without full confirmation, sized outside the pre-committed risk percentage, "
        "or held past a genuine reversal signal still happens to win, the outcome does not retroactively "
        "make the process correct. Reviewing wins with the same rigor as losses is how a trader avoids "
        "learning the wrong lesson from a lucky outcome \u2014 and how rule-breaking habits get caught "
        "before they compound into a large loss."
    ]))
    out.append(p(
        "A single loss, or a single rule deviation, is noise \u2014 it happens to every trader occasionally "
        "and proves little on its own. A recurring mistake is the same specific rule violation appearing "
        "across three or more journal entries: chasing entries, moving stops away from structure, "
        "oversizing after a loss, or skipping the same checklist item repeatedly. Patterns, not isolated "
        "events, are what the review process exists to surface."
    ))

    out.append(quiz(
        "A trader's journal shows three separate trades over two weeks where the entry price recorded "
        "is noticeably worse than the 15M confirmation candle's close \u2014 in each case, the trader "
        "entered a few pips late after price had already started moving toward the target. All three "
        "trades still won. What does this pattern indicate, and what should happen?",
        [
            {"label": "Nothing needs to change \u2014 all three trades were profitable, so the entry timing "
             "clearly is not a problem in practice.",
             "correct": False,
             "feedback": "<p><strong>Winning outcomes do not validate a rule deviation.</strong> \u00a711.8 "
                         "is explicit that a win achieved by breaking or bending a rule (here, entering "
                         "later than the confirmed level) does not retroactively make the process "
                         "correct \u2014 it means the trader got away with chasing three times, not that "
                         "chasing is safe. The same habit will eventually enter on a move that reverses "
                         "before target.</p>"},
            {"label": "This is a recurring mistake \u2014 the same specific deviation (late entry after the "
             "confirmed level) appearing three times is a pattern worth correcting, even though these "
             "particular trades happened to win.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a711.8 defines a recurring mistake as the same "
                         "specific rule violation appearing across three or more journal entries. The "
                         "outcome of those three trades is irrelevant to whether the pattern is worth "
                         "addressing \u2014 what matters is that entries are drifting from the confirmed "
                         "price, which will eventually erode the R:R calculated at the checklist stage or "
                         "cause a missed entry entirely.</p>"},
            {"label": "It cannot be assessed as a pattern until at least ten trades have been reviewed, "
             "regardless of how many entries already show the same deviation.",
             "correct": False,
             "feedback": "<p><strong>\u00a711.8 sets the threshold at three or more occurrences, not "
                         "ten.</strong> Waiting for a much larger sample before acting on a clearly "
                         "repeating, specific rule violation delays a correction that could prevent "
                         "several more entries at worse-than-planned prices in the meantime.</p>"},
        ],
        hint="Separate the outcome of the trades (win or loss) from whether a specific rule was actually "
             "followed."
    ))

    # ------------------------------------------------------------------
    # 11.9 Practical
    # ------------------------------------------------------------------
    out.append(h2("11.9", "Practical \u2014 build your own working rulebook"))
    out.append(prac(
        "11.1", "Assemble a one-page rulebook you can actually use",
        "Using the tables in \u00a711.1\u2013\u00a711.2 and the two checklists in \u00a711.3\u2013\u00a711.4, build a single "
        "page (physical or digital) that you could realistically read in under a minute before every "
        "trade.",
        "<ol>"
        "<li>Write out the six core principles from \u00a711.1 in your own words, short enough to fit on "
        "one line each.</li>"
        "<li>Copy the thirteen-item pre-trade checklist from Figure 11.3 exactly \u2014 do not shorten it "
        "yet; use it as written for at least ten qualifying setups first.</li>"
        "<li>Copy the nine-item post-trade review checklist from Figure 11.4 exactly, for the same "
        "reason.</li>"
        "<li>State, in one sentence each, the specific prop firm rules (or personal account rules) that "
        "determine your risk percentage per \u00a79.7 \u2014 do not copy a number from this course or from "
        "anywhere else without checking it against your own actual limits.</li>"
        "<li>After ten logged trades, review your journal specifically for any checklist item that was "
        "never the actual cause of a stand-aside decision \u2014 that item may be redundant for your "
        "instrument and session, or it may mean you have not yet encountered the condition it is "
        "guarding against. Do not delete an item just because it has not fired yet.</li>"
        "</ol>"
    ))
    out.append(prac(
        "11.2", "Run one full post-trade review",
        "Take the most recent trade you can find \u2014 real, demo, or from Module 10's worked examples "
        "\u2014 and complete the entire nine-item checklist from Figure 11.4 in writing, including an "
        "explicit strategy-failure/execution-failure classification per \u00a711.5.",
        "<p>If you use one of Module 10's worked trades, note that both reached target, so the review "
        "will land on \u201cstrategy-consistent win\u201d for every item \u2014 the value of the exercise is "
        "practicing the specific questions, not producing a dramatic finding.</p>"
    ))

    # ------------------------------------------------------------------
    # 11.10 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("11.10", "Vocabulary introduced or reinforced in this module"))
    out.append(defn("Core principle", "One of six foundational statements that every specific rule in "
        "this course is a direct application of; used to resolve ambiguity when a specific rule's "
        "wording seems unclear in a live situation."))
    out.append(defn("Pre-trade checklist", "A fixed, ordered list of conditions run before every entry; "
        "any single unmet condition means standing aside, with no partial credit for the items that did "
        "pass."))
    out.append(defn("Post-trade review", "A fixed, ordered set of questions completed after every closed "
        "trade, win or loss, used to classify the outcome and detect rule deviations."))
    out.append(defn("Execution failure", "A loss or suboptimal outcome caused by a rule being skipped or "
        "bent, where following the written sequence would likely have produced a different result."))
    out.append(defn("Strategy-consistent loss", "A loss that occurred despite every rule being followed "
        "exactly \u2014 the expected, priced-in downside of a positive-expectancy method, not a signal "
        "that the method is broken."))
    out.append(defn("Forward testing", "Applying the trading sequence to live, unfolding price with no "
        "capital at risk, to test whether the rules can be followed in real time without the benefit of "
        "hindsight."))
    out.append(defn("Recurring mistake", "The same specific rule violation appearing across three or "
        "more journal entries, as distinct from a single isolated deviation."))

    # ------------------------------------------------------------------
    # 11.11 Summary
    # ------------------------------------------------------------------
    out.append(h2("11.11", "Summary \u2014 and the end of this course"))
    out.append(summary([
        "Six core principles underlie every specific rule taught across all eleven modules: direction "
        "flows 4H \u2192 1H \u2192 15M; confirmation is a completed 15M close; stops and targets are "
        "structural; the 1:2 R:R minimum has no exceptions; position size is solved backward from risk; "
        "standing aside is a normal, correct, frequent outcome.",
        "The sixteen rule categories in \u00a711.2 map every decision point in the sequence to a specific, "
        "checkable rule \u2014 none of them require an in-the-moment judgement call made under pressure.",
        "The pre-trade checklist (13 items) and post-trade review (9 items) are meant to be used exactly "
        "as written, every time, not summarised from memory.",
        "Every loss is classified as either a strategy-consistent loss (the process worked, this "
        "outcome was always possible) or an execution failure (a rule was skipped) \u2014 confusing the two "
        "leads either to abandoning a sound method or persisting with a broken one.",
        "Backtesting, forward testing, demo execution, and live trading form a mandatory sequence, each "
        "stage testing a different kind of readiness; none may be skipped to reach live trading faster.",
        "A journal that records every trade \u2014 win or loss, real or simulated \u2014 and is reviewed with "
        "equal rigor in both directions is what turns isolated outcomes into visible, correctable "
        "patterns.",
        "This concludes the eleven-module course. The framework taught throughout \u2014 4H direction, 1H "
        "location, 15M confirmation, structural stops and targets, honest R:R, disciplined risk "
        "management, and the judgement to stand aside \u2014 does not eliminate uncertainty. It makes that "
        "uncertainty measurable, and makes the risk taken against it deliberate and defined."
    ]))

    return "\n".join(out)
