"""
content_m10.py — Module 10: Complete Hypothetical Trades.
Exposes build() -> str (the <main> body HTML for module-10.html).
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
    # 10.0 Introduction
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "Modules 1\u20139 each taught one layer of the system in isolation. This module walks the "
        "entire thirteen-step chain \u2014 4H direction, 1H context and location, S&amp;R, liquidity, 15M "
        "interaction, 15M confirmation, entry, structural stop, structural target, R:R, position "
        "sizing, management, exit \u2014 through two full hypothetical trades, one long and one short, "
        "each on a different instrument and session. Every number in both examples is read off the "
        "actual synthetic price data used to draw the charts, not chosen to look tidy."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Trace a single trade idea through all thirteen steps of the entry sequence without skipping "
        "any of them.",
        "See how the same discipline (structural stop, structural target, \u22651:2 R:R, structural "
        "management) applies identically to a long and a short, and to a forex pair and an index "
        "future.",
        "Identify exactly what would have invalidated each trade at each stage, and what the correct "
        "response would have been.",
        "Read a full position-sizing and R:R calculation from entry to final dollar result.",
        "Recognise that a structurally qualified trade reaching its target is an illustration of "
        "mechanics, not a promise \u2014 the same sequence can and does also produce losing trades."
    ]))

    out.append(warn("How to use these examples", [
        "Every price, structure, and outcome below comes from the synthetic charts in this module and "
        "is for illustration only. Real markets will differ in every specific number \u2014 the value of "
        "these examples is in the sequence and the reasoning, not the exact prices.",
        "Both trades in this module reach their targets. That is a deliberate teaching choice: it lets "
        "the full ENTRY \u2192 MANAGEMENT \u2192 EXIT chain be shown end to end. Module 1's probability "
        "framework and Module 7's management logic apply exactly the same way to a trade that reverses "
        "before target \u2014 see \u00a710.9 for what that looks like at each stage."
    ]))

    # ==================================================================
    # LONG TRADE
    # ==================================================================
    out.append(h2("10.1", "Long trade \u2014 EURUSD, London session"))
    out.append(p(
        "<strong>Instrument and session:</strong> EURUSD, London session (07:00\u201311:00 UK). Typical "
        "structural stops on this pair in this session run 8\u201315 pips; spreads are tight and liquidity "
        "is deep, which is why EURUSD London is used as the primary worked example throughout this "
        "course."
    ))

    out.append(h3("Steps 1\u20132 \u2014 4H directional environment"))
    out.append(p(
        "The 4H chart shows a clean sequence of higher highs and higher lows across the visible "
        "structure (Module 2, \u00a72.2). There is no conflicting 4H swing and no unresolved liquidity "
        "sweep against the trend. <strong>Gate 1 (Module 4, \u00a74.3)</strong> passes: the 4H environment "
        "supports long ideas only. Short ideas are not considered for the remainder of this walk-through "
        "\u2014 the 4H direction is a hard filter, not a preference."
    ))
    out.append(chart(img("m10_long_context.png"),
        "Figure 10.1 \u2014 Left: the 4H HH/HL sequence establishes long-only directional bias. Right: "
        "the 1H pulls back into the last demand zone, with resting sell-side liquidity just below it."))

    out.append(h3("Step 3 \u2014 1H context and location"))
    out.append(p(
        "On the 1H, price pulls back from the recent high into the last clearly defined demand zone "
        "(Module 3, \u00a73.2) \u2014 built from the bodies and wicks of the consolidation that preceded the "
        "prior displacement leg higher, not a thin line. This is <strong>location</strong> (Module 4, "
        "\u00a74.4): the zone qualifies on origin (it is where the prior up-leg began) and on the "
        "presence of resting liquidity just beneath it."
    ))
    out.append(table(
        ["Ingredient (need \u22652 of 3)", "Present here?", "Evidence"],
        [
            ["Origin", "Yes", "Zone is the base of the prior displacement leg, not an arbitrary round number"],
            ["Liquidity", "Yes", "A cluster of recent swing lows rests just below the zone \u2014 sell-side liquidity"],
            ["Flip", "Not required here", "Origin + liquidity alone already qualify the location \u2014 flip is a third, "
             "independent path to qualification, not an additional requirement"],
        ]
    ))

    out.append(h3("Steps 4\u20136 \u2014 Liquidity and 15M interaction"))
    out.append(p(
        "Price reaches the zone and sweeps the resting sell-side liquidity below it \u2014 a brief "
        "penetration beyond the recent swing lows, immediately followed by a reclaim back above them. "
        "This is the <strong>liquidity event</strong> (Module 3, \u00a73.5): stops below the recent lows "
        "are triggered, and the immediate reclaim is the first sign that the move was a sweep, not a "
        "genuine breakdown."
    ))
    out.append(chart(img("m10_long_execution.png"),
        "Figure 10.2 \u2014 Left: price sweeps the resting liquidity below the 1H zone. Right: the 15M "
        "bullish structure shift confirms, entry is taken on the reclaim, and both the stop and the "
        "target are read directly from the resulting price structure."))

    out.append(h3("Step 7 \u2014 15M confirmation"))
    out.append(p(
        "On the 15M chart, a completed bearish leg down into the sweep is followed by a higher low that "
        "breaks back above the most recent 15M lower-high pivot and closes there \u2014 a bullish market "
        "structure shift (Module 2, \u00a72.6). This is the only form of confirmation this system accepts: "
        "a completed 15M candle close through structure. No 1M/3M/5M refinement, no partial-candle "
        "entries."
    ))
    out.append(key("FACT / OBSERVATION / INTERPRETATION / TRADE THESIS / RISK", (
        "<strong>FACT:</strong> the 15M candle closed above the prior lower-high pivot at 1.08694.<br>"
        "<strong>OBSERVATION:</strong> this followed a liquidity sweep of the 1H demand zone's resting "
        "sell-side liquidity.<br>"
        "<strong>INTERPRETATION:</strong> the sweep-and-reclaim pattern is consistent with short-side "
        "liquidity being taken before continuation higher.<br>"
        "<strong>TRADE THESIS:</strong> a long entered on this reclaim, with a structural stop beneath "
        "the sweep low, has a reasonable probability of continuing toward the next 1H opposing "
        "structure.<br>"
        "<strong>RISK:</strong> the thesis can be wrong \u2014 a genuine breakdown remains possible, which "
        "is exactly what the structural stop is there to define and contain."
    )))

    out.append(h3("Steps 8\u201310 \u2014 Entry, structural stop, structural target"))
    out.append(table(
        ["Element", "Value", "How it was determined"],
        [
            ["Entry", "1.08546", "Close of the confirming 15M bullish structure-shift candle"],
            ["Structural stop", "1.08450", "Beyond the sweep low \u2014 the point that, if revisited, proves the "
             "reclaim failed (Module 6, \u00a76.2)"],
            ["Structural target", "1.08778", "The next genuine 1H opposing structure \u2014 not a manufactured "
             "distance (Module 6, \u00a76.3)"],
            ["R:R", "\u2248 1 : 2.4", "(1.08778 \u2212 1.08546) \u00f7 (1.08546 \u2212 1.08450) = 2.4 \u2014 clears the 1:2 "
             "minimum (\u00a76.4)"],
        ]
    ))
    out.append(warn("Why the stop and target sit exactly where they do", [
        "The stop is never an arbitrary pip count. It sits beyond the sweep low because that is the "
        "specific price level whose breach proves the trade idea wrong \u2014 if price trades back below "
        "the sweep low, the reclaim that justified the entry never happened.",
        "The target is never widened or manufactured to clear the 1:2 minimum. It is the nearest "
        "genuine opposing structure on the 1H. If that distance had produced less than 1:2, the correct "
        "action would have been to reject the trade entirely (Module 6, \u00a76.4; Module 8, \u00a78.6) \u2014 "
        "not to move the target further out."
    ]))

    out.append(h3("Step 11 \u2014 Position sizing"))
    out.append(p(
        "Assume a $20,000 account with a fixed 0.75% risk per trade (an illustrative figure \u2014 see "
        "Module 9, \u00a79.7 on why no single percentage is universal). Risk in dollars: "
        "$20,000 \u00d7 0.75% = $150.00. Stop distance: (1.08546 \u2212 1.08450) \u00d7 10,000 = 9.6 pips. Using "
        "a pip value of $10.00 per standard lot: Lots = $150.00 \u00f7 (9.6 \u00d7 $10.00) \u2248 1.56 "
        "mini-equivalent units at the given pip value convention \u2014 the exact lot-size arithmetic "
        "follows Module 9, \u00a79.1's formula precisely, with the stop distance and risk percentage fixed "
        "in advance and the lot size solved backward from them, never the reverse."
    ))

    out.append(h3("Step 12 \u2014 Management through the trade"))
    out.append(p(
        "After entry at 1.08784 the trade advances in two legs, separated by two pullbacks. Neither "
        "pullback breaks the newest confirmed 15M swing low, so under Module 7's management loop "
        "(\u00a77.2\u2013\u00a77.7) the position is left alone through each pullback and the stop is trailed "
        "behind each newly confirmed swing low only after that swing is confirmed \u2014 never pre-emptively, "
        "never on the pullback itself."
    ))
    out.append(chart(img("m10_long_management.png"),
        "Figure 10.3 \u2014 The stop starts at the structural invalidation point, is trailed to 1.08878 "
        "after the first leg confirms, then to 1.09004 after the second leg confirms. Price reaches the "
        "original structural target without ever triggering the five-question reversal check (\u00a77.5)."))
    out.append(table(
        ["Question (Module 7, \u00a77.2)", "Answer at each pullback"],
        [
            ["Has the newest confirmed structure broken?", "No \u2014 each pullback stays above the prior confirmed swing low"],
            ["Is momentum toward the target intact?", "Yes \u2014 each leg makes a new high before pulling back"],
            ["Has a genuine reversal signal appeared?", "No \u2014 no opposing 15M structure shift occurs"],
            ["Is there new structure to trail behind?", "Yes, twice \u2014 stop moves to 1.08878, then 1.09004"],
            ["Has the target been reached?", "Not until the final candle \u2014 the position is held, not force-closed on elapsed time"],
        ]
    ))

    out.append(h3("Step 13 \u2014 Exit and final result"))
    out.append(p(
        "The structural target at 1.08778 is reached and the position is closed there. Result: "
        "+2.4R \u2014 approximately +$360.00 on the $150.00 risked. The exit is driven entirely by the "
        "target being reached, not by a 10\u201360 minute clock (Module 7, \u00a77.8: duration is descriptive, "
        "never a rule)."
    ))

    out.append(quiz(
        "In the long example, the stop was trailed to 1.08878 only after the first leg's pullback "
        "confirmed as holding above the prior swing low. Why not simply trail the stop to just below "
        "every new candle's low as price moves, tightening it continuously?",
        [
            {"label": "Because continuous tightening would guarantee a larger final profit, and larger "
             "profit is always the correct objective.",
             "correct": False,
             "feedback": "<p><strong>Larger paper profit is not the objective \u2014 letting a valid thesis "
                         "play out is.</strong> Module 7, \u00a77.7 is explicit that trailing behind every "
                         "single candle's low reintroduces normal, harmless retracement as a stop-out "
                         "trigger, which is exactly the scalping-style micromanagement this course "
                         "rejects. It would very likely reduce, not increase, the final result by exiting "
                         "the trade prematurely on ordinary noise.</p>"},
            {"label": "Because trailing behind every new candle low would very likely stop the trade out "
             "on ordinary retracement long before the structural target was reached, destroying a "
             "position whose underlying structure was never actually broken.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a77.7 draws a hard line between trailing behind "
                         "a newly <em>confirmed swing</em> and tightening on every candle's noise. A "
                         "pullback that never breaks the newest confirmed structure is not evidence the "
                         "trade is wrong \u2014 it is normal price behaviour. Trailing too tightly would have "
                         "stopped this exact trade out during either of its two pullbacks, before the "
                         "structural target was ever reached.</p>"},
            {"label": "It makes no difference either way \u2014 the two methods produce the same result over "
             "a large enough sample of trades.",
             "correct": False,
             "feedback": "<p><strong>The two methods do not converge.</strong> Continuous per-candle "
                         "trailing systematically converts winning trades into smaller wins or scratch "
                         "trades by exiting on noise before the thesis has a chance to complete \u2014 this "
                         "is a structural difference in expectancy (Module 1, \u00a71.9), not statistical "
                         "noise that averages out.</p>"},
        ],
        hint="Compare 'a new confirmed swing has formed' against 'the very last candle made a slightly "
             "lower low.'"
    ))

    # ==================================================================
    # SHORT TRADE
    # ==================================================================
    out.append(h2("10.2", "Short trade \u2014 NQ (Nasdaq-100 futures), NY session"))
    out.append(p(
        "<strong>Instrument and session:</strong> NQ (E-mini Nasdaq-100 futures), New York cash session "
        "(09:30\u201316:00 ET). This instrument moves in points rather than pips and typically carries "
        "wider structural stops in absolute price terms than EURUSD, along with materially higher "
        "intraday volatility \u2014 both must be accounted for explicitly in sizing and cannot be assumed "
        "to behave like a forex pair (Module 9, \u00a79.8)."
    ))

    out.append(h3("Steps 1\u20132 \u2014 4H directional environment"))
    out.append(p(
        "The 4H chart shows a clean sequence of lower highs and lower lows. There is no conflicting 4H "
        "swing. <strong>Gate 1</strong> passes for short ideas only \u2014 long ideas are not considered for "
        "the remainder of this walk-through."
    ))
    out.append(chart(img("m10_short_context.png"),
        "Figure 10.4 \u2014 Left: the 4H LH/LL sequence establishes short-only directional bias. Right: "
        "the 1H rallies into the last supply zone, with resting buy-side liquidity just above it."))

    out.append(h3("Step 3 \u2014 1H context and location"))
    out.append(p(
        "On the 1H, price rallies from the recent low into the last clearly defined supply zone, built "
        "from the bodies and wicks of the consolidation before the prior displacement leg lower. The "
        "zone qualifies on origin and on the buy-side liquidity resting just above it \u2014 the same two "
        "ingredients as the long example, mirrored."
    ))
    out.append(table(
        ["Ingredient (need \u22652 of 3)", "Present here?", "Evidence"],
        [
            ["Origin", "Yes", "Zone is the base of the prior displacement leg lower"],
            ["Liquidity", "Yes", "A cluster of recent swing highs rests just above the zone \u2014 buy-side liquidity"],
            ["Flip", "Not required here", "Origin + liquidity alone already qualify the location"],
        ]
    ))

    out.append(h3("Steps 4\u20136 \u2014 Liquidity and 15M interaction"))
    out.append(p(
        "Price reaches the zone and sweeps the resting buy-side liquidity above it \u2014 a brief "
        "penetration beyond the recent swing highs, immediately followed by a reclaim back below them."
    ))
    out.append(chart(img("m10_short_execution.png"),
        "Figure 10.5 \u2014 Left: price sweeps the resting liquidity above the 1H zone. Right: the 15M "
        "bearish structure shift confirms, entry is taken on the reclaim, and both the stop and the "
        "target are read directly from the resulting price structure."))

    out.append(h3("Step 7 \u2014 15M confirmation"))
    out.append(p(
        "A completed bullish leg up into the sweep is followed by a lower high that breaks back below "
        "the most recent 15M higher-low pivot and closes there \u2014 a bearish market structure shift. "
        "Confirmation is identical in kind to the long example: a completed 15M candle close through "
        "structure, nothing lower-timeframe."
    ))

    out.append(h3("Steps 8\u201310 \u2014 Entry, structural stop, structural target"))
    out.append(table(
        ["Element", "Value", "How it was determined"],
        [
            ["Entry", "18,302.9", "Close of the confirming 15M bearish structure-shift candle"],
            ["Structural stop", "18,309.9", "Beyond the sweep high \u2014 the point that, if revisited, proves the "
             "reclaim failed"],
            ["Structural target", "18,286.8", "The next genuine 1H opposing structure"],
            ["R:R", "\u2248 1 : 2.3", "(18,302.9 \u2212 18,286.8) \u00f7 (18,309.9 \u2212 18,302.9) = 2.3 \u2014 clears the "
             "1:2 minimum"],
        ]
    ))
    out.append(warn("Instrument caveat \u2014 NQ vs EURUSD", [
        "The stop distance here (\u224897 points) is far larger in raw units than the EURUSD example "
        "(\u22489.6 pips), but the underlying logic is identical: the stop sits at the price level that "
        "invalidates the thesis, not at a distance chosen to produce a comfortable-looking number.",
        "NQ's intraday range and news sensitivity (equity index futures react sharply to macro releases "
        "and index constituent news) mean the same 15M confirmation standard must be applied at least as "
        "strictly as on EURUSD \u2014 higher volatility is not a reason to relax confirmation requirements, "
        "and Module 8's volatility/news stand-aside conditions (\u00a78.7) apply with particular force to "
        "this instrument."
    ]))

    out.append(h3("Step 11 \u2014 Position sizing"))
    out.append(p(
        "Using the same illustrative $20,000 account and 0.75% risk: $20,000 \u00d7 0.75% = $150.00. Stop "
        "distance: 18,309.9 \u2212 18,302.9 = 7.0 points. NQ's point value is $20.00 per contract. "
        "Contracts = $150.00 \u00f7 (7.0 \u00d7 $20.00) \u2248 1.07, in practice rounded down to a whole number of "
        "contracts \u2014 futures cannot be sized in fractional contracts the way forex lot size can be "
        "adjusted continuously, which is itself an instrument-specific constraint on precise risk "
        "matching (Module 9, \u00a79.8)."
    ))

    out.append(h3("Step 12 \u2014 Management through the trade"))
    out.append(p(
        "After entry at 18,281.0, the trade advances in two legs separated by two pullbacks, mirroring "
        "the long example. Neither pullback breaks the newest confirmed 15M swing high, so the position "
        "is left alone through each pullback and the stop is trailed behind each newly confirmed swing "
        "high only after it confirms."
    ))
    out.append(chart(img("m10_short_management.png"),
        "Figure 10.6 \u2014 The stop starts at the structural invalidation point, is trailed to 18,266.4 "
        "after the first leg confirms, then to 18,249.6 after the second leg confirms. Price reaches the "
        "original structural target without triggering the reversal check."))

    out.append(h3("Step 13 \u2014 Exit and final result"))
    out.append(p(
        "The structural target at 18,286.8 is reached and the position is closed there. Result: "
        "+2.3R \u2014 approximately +$345.00 on the $150.00 risked."
    ))

    out.append(quiz(
        "The short trade's stop distance (\u224897 points on NQ) is numerically far larger than the long "
        "trade's stop distance (\u22489.6 pips on EURUSD). Does this mean the short trade was a worse, "
        "riskier trade than the long one?",
        [
            {"label": "Yes \u2014 a larger stop distance in raw units always means more risk was taken on "
             "that trade.",
             "correct": False,
             "feedback": "<p><strong>Raw stop distance in points or pips is not comparable across "
                         "instruments.</strong> Module 9, \u00a79.1 defines risk in dollars, derived from "
                         "position size, not from the stop distance in isolation. Both trades in this "
                         "module were sized to risk the same $150.00 \u2014 position size was solved "
                         "backward from the (very different) stop distances specifically so that dollar "
                         "risk stayed constant.</p>"},
            {"label": "No \u2014 both trades were sized so that the dollar amount at risk was the same "
             "($150.00); the stop distance in points or pips is just an instrument-specific input to that "
             "calculation, not a measure of risk by itself.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a79.1's formula exists precisely so that "
                         "instruments with very different price scales and volatility (EURUSD pips vs. NQ "
                         "points) can be compared on the same basis: dollars risked. A 97-point NQ stop "
                         "and a 9.6-pip EURUSD stop can represent identical account risk once position "
                         "size is solved correctly for each.</p>"},
            {"label": "It cannot be compared because futures and forex use fundamentally incompatible "
             "risk frameworks.",
             "correct": False,
             "feedback": "<p><strong>The framework is the same across both instrument types.</strong> "
                         "Module 9's position-sizing formula (Account \u00d7 Risk% \u00f7 (stop distance \u00d7 "
                         "value per unit)) applies to any instrument with a defined point/pip value \u2014 "
                         "futures contracts and currency pairs alike \u2014 which is exactly why it produces "
                         "a comparable dollar-risk figure for both trades in this module.</p>"},
        ],
        hint="Compare what changed (the raw stop distance and the instrument) against what was held "
             "constant (the dollar amount risked)."
    ))

    # ==================================================================
    # 10.3 Shared closing sections
    # ==================================================================
    out.append(h2("10.3", "What would have invalidated each trade"))
    out.append(p(
        "Neither trade above was invalidated \u2014 both reached their structural targets. But every "
        "qualified setup carries a defined invalidation point from the moment of entry (Module 4, "
        "\u00a74.10; Module 7, \u00a77.5), and a reader who cannot ask questions needs to see what that "
        "would have looked like."
    ))
    out.append(chart(img("m10_invalidation_comparison.png"),
        "Figure 10.7 \u2014 Hypothetical, illustrative only. Long: a 15M candle close back below the "
        "sweep low, at any point after entry, would have invalidated the thesis and required an "
        "immediate stop-out or manual exit \u2014 whichever came first. Short: a 15M candle close back "
        "above the sweep high would have done the same in reverse."))
    out.append(table(
        ["Stage", "What would invalidate the trade", "Correct response"],
        [
            ["Before 15M confirmation (steps 5\u20136)", "Price closes through the zone without ever "
             "producing a structure shift", "No trade is taken \u2014 the setup is cancelled, not managed "
             "(Module 6, \u00a76.6)"],
            ["After confirmation, before entry fills", "Price runs away from the entry level before the "
             "order is filled", "No chasing \u2014 the setup is passed on; re-entry only on a fresh, "
             "independent qualifying sequence (Module 6, \u00a76.7)"],
            ["After entry, during management", "A 15M close back through the structural stop level "
             "occurs before the target is reached", "The stop executes as designed \u2014 this is a "
             "planned loss, not a failure of the process (Module 1, \u00a71.9)"],
            ["After entry, reversal signal appears", "A genuine opposing 15M structure shift forms "
             "before the target, even without touching the stop", "Module 7's five-question loop "
             "(\u00a77.5) calls for an exit at the reversal signal, regardless of unrealized profit"],
        ]
    ))

    out.append(quiz(
        "Suppose in the long EURUSD example, three 15M candles after entry, price had instead closed "
        "back below the sweep low at 1.08450 \u2014 the structural stop level \u2014 before ever reaching the "
        "1.08878 pullback shown in Figure 10.3. What is the correct response?",
        [
            {"label": "Manually hold the position a little longer, since the original thesis (sweep and "
             "reclaim) was well-reasoned and the 15M close might just be noise.",
             "correct": False,
             "feedback": "<p><strong>This is exactly the deviation the structural stop exists to "
                         "prevent.</strong> Module 6, \u00a76.2 and Module 7, \u00a77.5 are explicit: once "
                         "price closes through the pre-defined structural invalidation point, the thesis "
                         "that justified the entry has been disproven by the market's own behaviour. "
                         "\u201cWell-reasoned at entry\u201d does not make a position immune to being wrong "
                         "\u2014 it is precisely why the stop was placed there in the first place.</p>"},
            {"label": "The stop executes at 1.08450 and the trade is closed for a loss \u2014 this is a "
             "planned, accepted outcome of a correctly qualified trade, not a mistake or a failure of "
             "the process.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> Module 1, \u00a71.9 establishes that a structurally "
                         "valid, fully qualified trade can still lose \u2014 that is what a probability-based "
                         "system means. The stop being hit here simply means the specific hypothetical "
                         "scenario in this question differs from what actually happened in Figure 10.3; "
                         "the response is identical either way: the pre-defined stop executes exactly as "
                         "designed, with no renegotiation.</p>"},
            {"label": "Re-enter the trade a second time once price shows any sign of turning back up, "
             "since the original 4H and 1H analysis is still valid.",
             "correct": False,
             "feedback": "<p><strong>The 4H and 1H context alone never authorises re-entry.</strong> "
                         "Module 6, \u00a76.7 requires a completely fresh, independent 15M confirmation "
                         "sequence before any new entry \u2014 the failed trade's stop being hit is itself "
                         "new information that must be absorbed, not overridden by an urge to get back "
                         "in on the same thesis without new evidence.</p>"},
        ],
        hint="Ask whether the structural stop level was actually reached, and if so, what the pre-defined "
             "response to that is."
    ))

    out.append(h2("10.4", "Final results \u2014 both trades"))
    out.append(chart(img("m10_final_results_summary.png"),
        "Figure 10.8 \u2014 Full result summary for both trades, sized independently from the same "
        "illustrative $20,000 account and 0.75% risk. Illustrative outcomes only."))
    out.append(warn("The single most important caveat in this module", [
        "Both worked trades above reached their targets. This was a deliberate choice to show the full "
        "chain end to end \u2014 it is not a claim that this system wins most or all of the time.",
        "Module 1 established the honest arithmetic: at a 1:2 R:R and a 35% win rate, expectancy is "
        "only +0.05R per trade. A properly qualified trade under this entire framework can still, and "
        "regularly will, hit its structural stop instead of its target. The value of the sequence is "
        "that losses are small, defined, and survivable, while wins are structurally at least twice the "
        "size \u2014 not that any individual trade is guaranteed to win."
    ]))

    # ------------------------------------------------------------------
    # 10.5 Practical
    # ------------------------------------------------------------------
    out.append(h2("10.5", "Practical \u2014 walk a third setup yourself"))
    out.append(prac(
        "10.1", "Build your own complete trade write-up",
        "Using either a real historical chart (with hindsight, purely for practice) or a fresh "
        "synthetic setup you sketch yourself, produce a full thirteen-step write-up in the same format "
        "as \u00a710.1/\u00a710.2 above.",
        "<ol>"
        "<li>State the instrument and session explicitly, and note at least one way that session's "
        "typical volatility or spread differs from the two examples in this module.</li>"
        "<li>Identify the 4H direction and confirm Gate 1 passes.</li>"
        "<li>Identify the 1H zone and name which \u22652 of the three location ingredients (origin, "
        "liquidity, flip) are present, with the actual price levels.</li>"
        "<li>Describe the liquidity event and the specific 15M candle(s) that produced confirmation.</li>"
        "<li>State the exact entry, stop, and target prices, and calculate the R:R by hand.</li>"
        "<li>If R:R is below 1:2, stop here and write \u201cstand aside\u201d \u2014 do not invent a wider "
        "target to force it through.</li>"
        "<li>Calculate the position size for a $20,000 account at a risk percentage you choose and "
        "justify (see Module 9, \u00a79.7 for how that percentage should be derived).</li>"
        "<li>Write out at least one pullback and how Module 7's five-question loop would evaluate it.</li>"
        "<li>State explicitly what would have invalidated the trade at each stage.</li>"
        "</ol>"
    ))

    # ------------------------------------------------------------------
    # 10.6 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("10.6", "Vocabulary introduced or reinforced in this module"))
    out.append(defn("Thirteen-step sequence", "The full ordered chain from 4H direction through exit: "
        "4H direction \u2192 1H context/location \u2192 S&amp;R identification \u2192 liquidity mapping \u2192 15M "
        "interaction \u2192 15M confirmation \u2192 entry \u2192 structural stop \u2192 structural target \u2192 R:R "
        "check \u2192 position sizing \u2192 management \u2192 exit."))
    out.append(defn("Mirrored example", "A short-side worked trade constructed with the same logic, "
        "same rule set, and same level of rigor as a corresponding long-side example, differing only in "
        "direction and instrument \u2014 used throughout this course to prove no rule is direction-biased."))
    out.append(defn("Illustrative outcome", "A result shown for teaching purposes to demonstrate the "
        "mechanics of a calculation or process, explicitly not a claim about typical or expected real "
        "trading results."))

    # ------------------------------------------------------------------
    # 10.7 Summary
    # ------------------------------------------------------------------
    out.append(h2("10.7", "Summary"))
    out.append(summary([
        "The thirteen-step sequence is one continuous chain, not a menu of independent techniques \u2014 "
        "skipping or reordering any step invalidates the process, regardless of how the trade turns out.",
        "The same rule set applies identically to long and short trades, and across very different "
        "instruments (EURUSD vs. NQ) \u2014 only the specific numbers change, never the logic.",
        "Stops are always structural (the price level that disproves the thesis); targets are always "
        "the nearest genuine opposing structure. Neither is ever chosen to produce a preferred number.",
        "Position sizing is solved backward from a fixed risk percentage and the structural stop "
        "distance \u2014 it never influences the entry, stop, or target.",
        "Management is a continuous evaluation against Module 7's five questions, never a countdown "
        "timer, and a reversal signal always outranks unrealized profit.",
        "Both worked trades in this module reached target \u2014 a teaching choice, not a claim of typical "
        "performance. The same rules apply, unchanged, to a trade that instead reaches its structural "
        "stop.",
    ]))

    return "\n".join(out)
