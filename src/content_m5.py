"""
content_m5.py — Module 5: 15M Candlestick Triggers & Price Psychology.
Exposes build() -> str (the <main> body HTML for module-05.html).
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
    # 5.0 Introduction — the governing rule for this whole module
    # ------------------------------------------------------------------
    out.append(key(
        "The claim of this module",
        "A candlestick pattern is not a signal. It is a small, honest record of who won a very short "
        "fight between buyers and sellers. That record only becomes useful evidence when it happens at "
        "a location that already matters — a graded zone from Module 3, in a context set by the 4H and "
        "1H structure from Module 2. The identical candle shape, printed at a random point in the "
        "middle of a range, records the same fight but carries no trading information at all. This "
        "module teaches you to read the record and to refuse it when the location does not support it."
    ))

    out.append(look("By the end of this module you will be able to", [
        "Name and recognise every candlestick trigger in this system's vocabulary: rejection/pin bars, "
        "engulfing candles, strong-bodied candles, momentum candles, inside bars, failed breakouts, and "
        "compression-into-expansion sequences.",
        "Explain the psychological meaning behind each pattern — what buyers and sellers were actually "
        "doing during that candle, not just what shape it drew.",
        "State, for every pattern, where it is meaningful and where it is meaningless, using Module 2 "
        "structure and Module 3 zones as the deciding factor.",
        "Identify the specific structural support each pattern needs to be treated as evidence, and the "
        "specific condition that invalidates it.",
        "Explain how liquidity (Module 3, \u00a73.5\u2013\u00a73.7) and zone grading (Module 3, \u00a73.8) change the "
        "reliability of an otherwise-identical candle.",
        "Reject a textbook-perfect candle shape when the structural case for it is absent, and explain "
        "why in one sentence.",
    ]))

    out.append(warn("This is not a pattern-matching exercise", [
        "Every trader who has looked at a chart has been shown a list of candlestick shapes with names "
        "attached. That is not what this module is. A shape without context is trivia. The only "
        "question this system ever asks of a candle is: <strong>given everything Module 2 and Module 3 "
        "already told us about this location, does this candle's closing behaviour confirm or contradict "
        "the thesis?</strong> Every section below answers that question for one specific pattern."
    ]))

    out.append(h2("5.1", "Candle anatomy and what each part records"))
    out.append(p(
        "A single candle is a compressed record of every trade that happened during its 15-minute "
        "window, reduced to four numbers: <strong>open</strong>, <strong>high</strong>, "
        "<strong>low</strong>, and <strong>close</strong>. Everything this module teaches is built from "
        "reading the relationship between those four numbers, never from the candle's shape in "
        "isolation."
    ))
    out.append(table(
        ["Part", "What it is", "What it records"],
        [
            ["Body", "The rectangle between open and close.",
             "Who controlled the candle by its close. A large body means one side dominated "
             "from start to finish. A small body means the fight ended close to a draw."],
            ["Upper wick", "The line from the top of the body to the high.",
             "The highest price buyers could not hold, or the highest price sellers were able to "
             "push to before losing control. A long upper wick records rejection of higher prices."],
            ["Lower wick", "The line from the bottom of the body to the low.",
             "The lowest price sellers could not hold, or the lowest price buyers were able to push "
             "to before regaining control. A long lower wick records rejection of lower prices."],
            ["Close relative to range", "Where the close sits inside the full high-low range.",
             "The single most important number in this module. A close near the high of the range "
             "shows buyers won the last word. A close near the low shows sellers did, regardless of "
             "what happened in between."],
        ]
    ))
    out.append(chart(img("m5_anatomy.png"),
        "Figure 5.1 \u2014 Three candles with identical range but different body-to-range ratios: a "
        "strong-bodied candle (~86% body), a small-bodied long-wicked candle (~11% body), and a pin bar "
        "(~5% body). Same total range, three different stories about who won."))
    out.append(p(
        "Body-to-range ratio is the single measurement underlying almost every pattern in this module. "
        "A candle with an 86% body closed almost exactly where it traded at its extreme \u2014 one side "
        "won decisively and held the win. A candle with an 11% body traded through a wide range and "
        "closed near the middle \u2014 both sides fought hard and neither one held the advantage by the "
        "close. Learn to estimate this ratio by eye before reading any further; every trigger below is a "
        "named special case of this one measurement combined with location."
    ))

    out.append(defn("Body-to-range ratio",
        "The size of a candle's body (|close \u2212 open|) expressed as a percentage of its full range "
        "(high \u2212 low). High ratios (roughly &gt;70%) indicate one-sided control through the close. "
        "Low ratios (roughly &lt;30%) indicate a contested candle where the close did not confirm "
        "either extreme."))
    out.append(defn("Closing strength",
        "Where the close sits within the candle's full range, usually described as a percentage from "
        "the low. A close in the top 20% of the range is a strong bullish close; a close in the bottom "
        "20% is a strong bearish close, regardless of the candle's colour or body size."))

    # ------------------------------------------------------------------
    # 5.2 Rejection candles / pin bars / wick rejection
    # ------------------------------------------------------------------
    out.append(h2("5.2", "Rejection candles, pin bars, and wick rejection"))
    out.append(p(
        "A rejection candle (also called a pin bar) has a small body pushed to one end of a long wick "
        "on the opposite side. It is the clearest single-candle record of a level being tested and "
        "failing to hold."
    ))
    out.append(table(
        ["Point", "Answer"],
        [
            ["WHAT", "A candle with a body under roughly 30% of its total range, with the long wick on "
             "one side and the body pressed against the other. A bullish pin bar has its long wick "
             "below the body (rejection of lower prices); a bearish pin bar has its long wick above the "
             "body (rejection of higher prices)."],
            ["WHY it forms", "Price traded aggressively to an extreme, found enough opposing orders "
             "there to reverse within the same candle, and closed back near where it started. The wick "
             "is a record of orders being absorbed \u2014 stop-losses, limit orders, or fresh entries \u2014 at "
             "that specific price."],
            ["WHERE it is meaningful", "At a graded zone (Module 3, \u00a73.8) that the 4H/1H context "
             "(Module 2) already flagged as relevant, especially when the wick also swept resting "
             "liquidity (Module 3, \u00a73.5\u2013\u00a73.6) just beyond the zone before reversing."],
            ["HOW to identify it", "Measure the body-to-range ratio (under ~30%). Confirm the wick "
             "direction matches the thesis (long lower wick for a long, long upper wick for a short). "
             "Confirm the close sits back inside the zone, not just inside the wick."],
            ["HOW to use it", "As step 7 confirmation in the Module 4 entry sequence, when it occurs at "
             "a zone that has already satisfied steps 1\u20136 (4H bias, 1H context, valid zone, liquidity "
             "beyond it). Never as a standalone reason to enter."],
            ["WHEN unreliable", "In the middle of a range, on an untested/random price level, or in "
             "the absence of any liquidity beneath the wick. A pin bar with nothing underneath it to "
             "sweep is just a volatile candle, not a rejection of a level."],
            ["WHAT invalidates it", "The next 15M candle closing back through the pin bar's extreme in "
             "the direction the wick rejected \u2014 e.g. a bullish pin bar whose low is then closed below. "
             "This is a structural invalidation (Module 4, \u00a74.5), separate from the stop price."],
            ["Practical example", "See Figure 5.2 below: identical pin bar shape, opposite verdicts."],
        ]
    ))
    out.append(chart(img("m5_rejection_pin.png"),
        "Figure 5.2 \u2014 Left: a bullish pin bar at a fresh, graded 1H demand zone, with its lower wick "
        "sweeping resting liquidity just beneath the zone before closing back inside \u2014 meaningful. "
        "Right: the identical candle shape printed in the middle of an established range with no zone "
        "beneath it \u2014 meaningless. The candle did not change; the location did."))

    out.append(quiz(
        "A bullish pin bar forms with its lower wick sweeping below a well-graded 1H demand zone and "
        "closing back inside it with a strong close. The next 15M candle then closes below the pin "
        "bar's low. What should happen?",
        [
            {"label": "Hold the idea \u2014 the original pin bar was valid, so the thesis still stands.",
             "correct": False,
             "feedback": "<p><strong>This treats the pin bar as permanent evidence, which it is not.</strong> "
                         "A rejection candle is evidence about the fight that happened during its own 15 "
                         "minutes. A later candle closing back through its extreme is new evidence that "
                         "contradicts it \u2014 the level that appeared to hold has now failed. Clinging to the "
                         "first candle after the market has produced contradicting information is exactly "
                         "the discipline failure Module 4 \u00a74.5 describes as ignoring structural "
                         "invalidation.</p>"},
            {"label": "Treat the setup as structurally invalidated, regardless of where the stop-loss "
             "price sits.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> A close back through the rejection candle's extreme "
                         "is a direct contradiction of what the pin bar claimed to show. This is "
                         "structural invalidation exactly as defined in Module 4, \u00a74.5: the thesis is "
                         "false now, independent of whether the price has reached the stop-loss level. "
                         "The correct action is to exit or stand aside, not wait for a price to be "
                         "touched.</p>"
                         "<p>This is also consistent with \u00a75.2's own invalidation rule stated above: the "
                         "next candle closing back through the pin bar's extreme in the rejected direction "
                         "invalidates it.</p>"},
            {"label": "Add to the position, since the deeper low is a better price.",
             "correct": False,
             "feedback": "<p><strong>This confuses a better price with a better trade.</strong> The reason "
                         "the price is lower is that the rejection failed \u2014 the exact evidence the entry "
                         "was based on has been contradicted. A lower price obtained by averaging into a "
                         "broken thesis is not a discount; it is compounding a mistake. Nothing in this "
                         "system treats price alone as a reason to add risk.</p>"},
        ],
        hint="Ask what the second candle's close does to the specific claim the pin bar made, not what "
             "it does to the stop-loss price."
    ))

    # ------------------------------------------------------------------
    # 5.3 Engulfing candles
    # ------------------------------------------------------------------
    out.append(h2("5.3", "Engulfing candles"))
    out.append(table(
        ["Point", "Answer"],
        [
            ["WHAT", "A candle whose body fully covers the body of the candle immediately before it, in "
             "the opposite direction. A bullish engulfing candle opens at or below the prior candle's "
             "close and closes above the prior candle's open."],
            ["WHY it forms", "It records a complete reversal of control within a single 15-minute "
             "window \u2014 the side that was losing at the prior close is now dominant enough to trade "
             "through the entire previous range and close beyond it."],
            ["WHERE it is meaningful", "At a zone, after a liquidity sweep, when the engulfed candle was "
             "itself part of the move being reversed \u2014 e.g. a small down-candle poking into a demand "
             "zone, then engulfed by a large up-candle that closes back above the zone's origin."],
            ["HOW to identify it", "Compare the two candle bodies directly: open/close of the engulfing "
             "candle must fully contain open/close of the prior candle. Wicks are not part of the "
             "definition \u2014 only bodies."],
            ["HOW to use it", "As strong step 7/9 evidence (Module 4) when it occurs at a graded zone "
             "with liquidity swept beneath it \u2014 it is generally stronger evidence than a same-sized pin "
             "bar because it also shows the prior candle's move being actively reversed, not merely "
             "rejected."],
            ["WHEN unreliable", "In a chopping, directionless range where engulfing candles occur "
             "constantly by chance rather than at any structurally relevant point. On thin/low-liquidity "
             "sessions where a single large order can create the shape without genuine two-sided "
             "participation."],
            ["WHAT invalidates it", "Price re-entering and closing back inside the range that was just "
             "engulfed \u2014 this shows the reversal did not hold and the engulfing candle's move was "
             "itself absorbed."],
            ["Practical example", "See Figure 5.3 below."],
        ]
    ))
    out.append(chart(img("m5_engulfing.png"),
        "Figure 5.3 \u2014 A small bearish candle dips into a graded 1H demand zone, sweeping resting "
        "liquidity just beneath it. The next candle fully engulfs it and closes back above the zone's "
        "origin \u2014 a complete reversal of control confirmed within one candle."))

    # ------------------------------------------------------------------
    # 5.4 Strong-bodied and momentum candles
    # ------------------------------------------------------------------
    out.append(h2("5.4", "Strong-bodied candles and momentum candles"))
    out.append(p(
        "A strong-bodied candle has a high body-to-range ratio (roughly &gt;70%) with wicks on both "
        "ends short relative to the body. A momentum candle is a strong-bodied candle that is also "
        "unusually large relative to the recent candles around it \u2014 the same one-sided control, but "
        "with size added as evidence of urgency."
    ))
    out.append(table(
        ["Point", "Answer"],
        [
            ["WHAT", "Strong-bodied: body-to-range ratio high, short wicks both sides. Momentum: the "
             "same, plus a range visibly larger (commonly 1.5\u20132x or more) than the preceding several "
             "candles' average range."],
            ["WHY it forms", "One side of the market traded with control from open to close, with "
             "almost no meaningful pushback from the other side at either extreme. A momentum candle "
             "adds evidence that new participants entered aggressively rather than the move being a slow "
             "grind."],
            ["WHERE it is meaningful", "As Module 2's displacement candle (the 70%-body test, Module 2 "
             "\u00a72.6) breaking structure, or as continuation evidence once a trade is already open. Also "
             "meaningful at a zone as very strong step 7 confirmation \u2014 it shows conviction, not just "
             "rejection."],
            ["HOW to identify it", "Measure body-to-range ratio; compare candle size to a short lookback "
             "(commonly 10\u201320 candles) to judge whether it qualifies as a momentum candle specifically, "
             "versus merely a strong-bodied one."],
            ["HOW to use it", "As displacement/BOS evidence (Module 2, \u00a72.6\u2013\u00a72.7) and as the "
             "strongest form of step 7/9 confirmation in the Module 4 sequence. In trade management "
             "(Module 7), a momentum candle appearing against an open position is itself information."],
            ["WHEN unreliable", "Around scheduled news releases, where a large one-sided candle can "
             "reflect a liquidity/volatility spike rather than genuine directional conviction, and can "
             "reverse just as fast. Also unreliable late in an already-extended move, where it can mark "
             "exhaustion (a blow-off) rather than continuation \u2014 context from the 4H/1H structure "
             "decides which interpretation applies."],
            ["WHAT invalidates it", "A same-size or larger candle in the opposite direction immediately "
             "after it \u2014 this shows the apparent conviction was one participant, not the market, and it "
             "has already been answered."],
            ["Practical example", "See Figure 5.4 below."],
        ]
    ))
    out.append(chart(img("m5_momentum.png"),
        "Figure 5.4 \u2014 Left: a strong-bodied candle with an 89% body and short wicks both sides \u2014 "
        "one-sided control, ordinary size. Right: a momentum candle with a similar body ratio but roughly "
        "double the range of the candles preceding it \u2014 the same control, with urgency added."))

    out.append(quiz(
        "A large, strong-bodied bullish candle prints two minutes before a scheduled high-impact news "
        "release, breaking above a recent 15M swing high. Does this qualify as reliable displacement "
        "evidence for step 9 of the Module 4 sequence?",
        [
            {"label": "Yes \u2014 body-to-range ratio and size both qualify it as a momentum candle.",
             "correct": False,
             "feedback": "<p><strong>Meeting the shape criteria is not the same as meeting the reliability "
                         "criteria.</strong> \u00a75.4 explicitly flags candles around scheduled news as "
                         "unreliable, independent of how clean their body-to-range ratio looks. Volume and "
                         "positioning ahead of a known release can produce exactly this shape without "
                         "representing a genuine directional decision by the market.</p>"},
            {"label": "No \u2014 treat it as unreliable because of the news timing, and wait for "
             "post-release 15M closes to re-establish the picture.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> \u00a75.4's WHEN UNRELIABLE case names scheduled news "
                         "specifically: a large one-sided candle immediately before a release can reflect "
                         "positioning or a liquidity air-pocket rather than genuine conviction, and can "
                         "reverse immediately once the release actually prints. The structurally sound "
                         "response is to wait for 15M closes after the news to tell you what the market "
                         "actually decided, consistent with this system's rule that confirmation always "
                         "means completed 15M closes.</p>"},
            {"label": "It cannot be evaluated without knowing the candle's colour history.",
             "correct": False,
             "feedback": "<p><strong>Candle colour is not a factor this system evaluates.</strong> The "
                         "relevant variables are body-to-range ratio, relative size, location, and \u2014 in "
                         "this specific case \u2014 proximity to a scheduled news event. Colour history plays "
                         "no role in any of the eight points in this module.</p>"},
        ],
        hint="Re-read the WHEN UNRELIABLE row for momentum candles before answering."
    ))

    # ------------------------------------------------------------------
    # 5.5 Inside bars
    # ------------------------------------------------------------------
    out.append(h2("5.5", "Inside bars"))
    out.append(table(
        ["Point", "Answer"],
        [
            ["WHAT", "A candle whose entire high-low range sits within the high-low range of the "
             "candle immediately before it (the \u201cmother bar\u201d). Two or more consecutive inside bars "
             "compress the range further with each one."],
            ["WHY it forms", "Participation has temporarily dried up \u2014 neither side is committing new "
             "orders aggressively enough to extend the range. This is a pause, not a decision."],
            ["WHERE it is meaningful", "Where relevant: as a compression signature ahead of an "
             "expansion move (see \u00a75.8), particularly when it forms at a zone or after a strong "
             "directional leg, where the pause can represent absorption before continuation."],
            ["HOW to identify it", "Compare each candle's high and low directly against the candle "
             "before it. All of the inside candle's range must sit within the mother bar's range \u2014 a "
             "partial overlap does not qualify."],
            ["HOW to use it", "As a caution signal, not an entry trigger on its own: it tells you range "
             "is compressing and an expansion candle (\u00a75.8) is more likely soon, without telling you "
             "the direction. Combine with the zone/context already established before treating either "
             "side as favoured."],
            ["WHEN unreliable", "As a standalone reversal or continuation signal \u2014 an inside bar says "
             "nothing about direction by itself. Also unreliable in a low-volatility session lull (e.g. "
             "the hours between the Asia close and London open) where compression is simply a function "
             "of the session, not a meaningful structural pause."],
            ["WHAT invalidates it", "A subsequent candle closing outside the mother bar's range in "
             "either direction resolves the pattern \u2014 the compression is over, and the resolving "
             "candle's direction and closing strength become the new evidence to evaluate."],
            ["Practical example", "See Figure 5.5 below."],
        ]
    ))
    out.append(chart(img("m5_inside_bar.png"),
        "Figure 5.5 \u2014 Two consecutive candles trade fully within the range of the candle before them "
        "(the mother bar). Range compresses, then resolves with an expansion candle. The inside bars "
        "alone did not predict the direction of that resolution."))

    # ------------------------------------------------------------------
    # 5.6 Failed breakouts and closing strength
    # ------------------------------------------------------------------
    out.append(h2("5.6", "Failed breakouts and closing strength"))
    out.append(table(
        ["Point", "Answer"],
        [
            ["WHAT", "A candle (or short run of candles) that wicks through a well-known structural "
             "level \u2014 a prior swing high/low, a zone boundary, a session high/low \u2014 but closes back "
             "on the original side of it. The break attracted orders but failed to gain acceptance."],
            ["WHY it forms", "Breakout traders and stop-losses resting just beyond the level provide "
             "the liquidity that lets price wick through; once that liquidity is consumed, there are not "
             "enough real continuation orders to hold price beyond the level, and it snaps back."],
            ["WHERE it is meaningful", "At any level the 4H/1H context has already identified as "
             "significant (Module 2/3) \u2014 a failed breakout there is direct evidence that the level is "
             "defended, and frequently marks the exact liquidity sweep the Module 4 sequence (step 6) "
             "looks for before a reversal trade in the opposite direction."],
            ["HOW to identify it", "Confirm the candle's high (or low) trades beyond the level, and its "
             "close sits back on the original side. The further the close retraces back through the "
             "level, the stronger the failure."],
            ["HOW to use it", "As liquidity-sweep evidence supporting a reversal thesis at that level, "
             "combined with the location and context that made the level worth watching in the first "
             "place. It is the wick, not the direction of the overall candle colour, that is the "
             "signal."],
            ["WHEN unreliable", "In a strongly trending market where breakouts are genuinely being "
             "accepted most of the time \u2014 treating every wick through a level as a failure in a "
             "trending regime produces repeated false reversal reads against the dominant flow."],
            ["WHAT invalidates it", "A later close that reclaims and holds beyond the level after all "
             "\u2014 this shows the first failure was a pause, not a rejection, and the breakout is now "
             "being accepted."],
            ["Practical example", "See Figure 5.6 below."],
        ]
    ))
    out.append(chart(img("m5_failed_breakout.png"),
        "Figure 5.6 \u2014 Price wicks through a well-known prior structural high, attracting breakout "
        "buyers, then closes back beneath it within the same candle. The break failed to gain "
        "acceptance \u2014 the wick, not the close, is the signal."))

    out.append(defn("Acceptance",
        "Confirmation that price is willing to trade and close beyond a level over more than a single "
        "wick \u2014 typically one or more full 15M closes holding beyond it. A wick alone is an attempt; "
        "acceptance is what turns an attempt into a genuine break."))

    out.append(quiz(
        "Price wicks 6 pips above a well-known 4H swing high and closes 2 pips below it on a strong "
        "down-close candle. The 4H trend context (Module 2) is a clear, established uptrend. What is "
        "the most structurally sound read?",
        [
            {"label": "Treat it as a clean short setup \u2014 a failed breakout is bearish by definition.",
             "correct": False,
             "feedback": "<p><strong>\u00a75.6 explicitly warns against this.</strong> The WHEN UNRELIABLE "
                         "row states that in a strongly trending market, treating every wick through a "
                         "level as a failure produces false reversal reads against the dominant flow. A "
                         "single failed breakout against an established 4H uptrend is much weaker evidence "
                         "than the same pattern appearing with no trend opposing it, or at the end of an "
                         "extended move.</p>"},
            {"label": "Weigh it as one data point against a strong prevailing 4H uptrend, and require "
             "additional 1H/15M confirmation before treating it as a reversal thesis.",
             "correct": True,
             "feedback": "<p><strong>Correct.</strong> The candle is real evidence of a rejection at that "
                         "specific level, but \u00a75.6 is explicit that this pattern is unreliable as a "
                         "standalone reversal signal inside a strongly trending market. The chain-of-command "
                         "principle (Module 2/4) still applies: a 15M candle cannot overrule 4H context on "
                         "its own. This calls for more confirmation, not an outright rejection of the "
                         "signal or an outright acceptance of it.</p>"},
            {"label": "Ignore it completely \u2014 candlestick patterns are irrelevant inside a trend.",
             "correct": False,
             "feedback": "<p><strong>This overcorrects.</strong> The candle is still real information about "
                         "order flow at that level; it is simply weaker evidence in this specific context "
                         "than it would be elsewhere. \u00a75.0's governing rule is that location and context "
                         "decide reliability \u2014 not that trend context makes candlestick evidence "
                         "meaningless.</p>"},
        ],
        hint="Re-read the WHEN UNRELIABLE row for failed breakouts, and recall that 4H context outranks a "
             "single 15M candle."
    ))

    # ------------------------------------------------------------------
    # 5.7 Context dependence — the same shape, three verdicts
    # ------------------------------------------------------------------
    out.append(h2("5.7", "One shape, three verdicts: context decides everything"))
    out.append(p(
        "Every pattern in this module has now been given a location-dependent verdict. This section "
        "makes the point directly with a single example, because it is the idea most likely to be "
        "forgotten under the pressure of a live chart: <strong>the candle never changes; only the "
        "structure around it changes what it means.</strong>"
    ))
    out.append(chart(img("m5_context_dependence.png"),
        "Figure 5.7 \u2014 The same bullish pin bar shape, evaluated in three locations: a fresh graded "
        "demand zone with swept liquidity beneath it (high reliability), a third-touch partially "
        "depleted zone (reduced reliability), and the middle of a range with no supporting structure "
        "at all (no reliability)."))
    out.append(table(
        ["Location", "Verdict", "Reasoning"],
        [
            ["Fresh, graded demand zone + swept liquidity beneath it",
             "High reliability",
             "Location, liquidity, and rejection all agree \u2014 exactly what Module 4 step 6/7 looks for."],
            ["Third-touch, partially depleted zone (Module 3, \u00a73.4)",
             "Reduced reliability",
             "The pin bar is genuine, but the zone has already absorbed two prior reactions. Treat as "
             "weaker evidence, not disqualifying evidence."],
            ["Middle of a range, no zone, no liquidity, no structure",
             "No reliability",
             "The candle looks identical but there is no mechanism for it to mean anything. Module 4, "
             "\u00a74.6's stand-aside conditions apply."],
        ]
    ))
    out.append(dev("Developer's-eye analogy", [
        "This is identical in shape to a code review flagging the same line of code differently "
        "depending on which function calls it. A `return null` is unremarkable inside a lookup helper "
        "that expects misses, and a serious bug inside a constructor that every caller assumes always "
        "returns a valid object. The line of code did not change. The calling context decided whether it "
        "was fine or dangerous. Candlestick patterns work exactly the same way \u2014 read them relative to "
        "where they occur, never in isolation."
    ]))

    # ------------------------------------------------------------------
    # 5.8 Compression before expansion
    # ------------------------------------------------------------------
    out.append(h2("5.8", "Compression before expansion"))
    out.append(table(
        ["Point", "Answer"],
        [
            ["WHAT", "A visibly shrinking high-low range across several consecutive candles \u2014 each "
             "one's range smaller than the last \u2014 frequently followed by a candle whose range "
             "significantly exceeds the compressed run (an expansion or displacement candle)."],
            ["WHY it forms", "Orders accumulate quietly while neither side is willing to commit "
             "aggressively; once one side's resting orders are triggered (often by a liquidity sweep or "
             "a session open), the accumulated imbalance releases in one larger move."],
            ["WHERE it is meaningful", "At the edges of established ranges, ahead of session opens "
             "(e.g. London or NY open), or after a pause following a strong initial leg \u2014 anywhere the "
             "4H/1H context already gives a reason to expect a resolution."],
            ["HOW to identify it", "Track each candle's high-low range against the 2\u20133 candles before "
             "it; a genuine compression sequence should show the range visibly tightening across at "
             "least 3\u20134 candles, not just one quiet candle."],
            ["HOW to use it", "As a warning to prepare, not a trigger to enter: it flags that a move is "
             "increasingly likely soon without telling you the direction. The direction is read from the "
             "candle that resolves the compression \u2014 its close, body ratio, and whether it aligns with "
             "the existing 4H/1H context."],
            ["WHEN unreliable", "During predictably quiet periods (holidays, pre-news lulls, thin "
             "overnight sessions) where compression is a function of low participation rather than "
             "accumulating pressure, and the eventual \u201cexpansion\u201d may simply be the next session's "
             "normal volatility returning."],
            ["WHAT invalidates it", "A resolving candle that itself has a weak body-to-range ratio or "
             "closes back inside the compressed range \u2014 this shows the apparent breakout was itself "
             "absorbed, and the compression may resume rather than resolve."],
            ["Practical example", "See Figure 5.8 below."],
        ]
    ))
    out.append(chart(img("m5_compression_expansion.png"),
        "Figure 5.8 \u2014 A visibly shrinking range over several candles \u2014 each one's high-low span "
        "smaller than the last \u2014 frequently precedes a displacement leg. The compression does not "
        "predict direction on its own; the resolving candle's own body and context do."))

    # ------------------------------------------------------------------
    # 5.9 Liquidity and zone grading as reliability multipliers
    # ------------------------------------------------------------------
    out.append(h2("5.9", "How liquidity and zone grading change reliability"))
    out.append(p(
        "Two variables from Module 3 do more than anything else in this system to separate a "
        "meaningful candlestick trigger from a meaningless one: whether resting liquidity was swept "
        "immediately before the candle, and how the zone it occurred at is graded."
    ))
    out.append(table(
        ["Variable", "Effect on candle reliability"],
        [
            ["Liquidity swept beneath/above the candle (Module 3, \u00a73.5\u2013\u00a73.6)",
             "Raises reliability substantially. A rejection candle that also swept resting stop-losses "
             "or breakout orders shows the reaction consumed a specific, identifiable pool of opposing "
             "orders \u2014 not just a random pause."],
            ["No liquidity nearby",
             "Lowers reliability. A rejection candle with nothing resting beneath it has no obvious "
             "source of the opposing pressure that reversed it \u2014 it may simply be noise."],
            ["Fresh, high-graded zone (Module 3, \u00a73.8: origin + reaction quality + freshness)",
             "Raises reliability. The zone itself is strong evidence independent of the candle; the "
             "candle adds confirmation on top of an already-strong location."],
            ["Low-graded or heavily tested zone",
             "Lowers reliability, even with an identical candle shape. The location itself is weaker "
             "evidence, so the candle cannot compensate for it alone."],
        ]
    ))
    out.append(p(
        "The rule this system uses throughout: a candlestick trigger can raise or lower confidence "
        "<em>within</em> an already-valid setup. It cannot manufacture a valid setup out of a location "
        "that Module 2 and Module 3 have not already qualified. This is why every pattern in this "
        "module was given a WHERE and a WHEN UNRELIABLE row before anything else."
    ))

    # ------------------------------------------------------------------
    # 5.10 Instrument / session caveats
    # ------------------------------------------------------------------
    out.append(h2("5.10", "Instrument and session caveats"))
    out.append(table(
        ["Instrument / session", "How candlestick behaviour differs"],
        [
            ["EURUSD, London 07:00\u201311:00 UK",
             "Wicks tend to be measured and proportionate to the move; genuine rejection candles at "
             "well-known levels are comparatively reliable once liquidity has been swept. False signals "
             "cluster in the quiet hour before London open."],
            ["GBPUSD, London/NY overlap 13:00\u201316:00 UK",
             "Faster, deeper wicks (commonly 15\u201325 pips versus EURUSD's 8\u201315) mean pin bars and "
             "failed breakouts can look more dramatic without being proportionally more reliable \u2014 "
             "measure body-to-range ratio carefully rather than reacting to wick size alone."],
            ["ES / NQ, NY cash 09:30\u201316:00 ET",
             "Momentum candles are common and can be driven by index-wide flow rather than the specific "
             "level; NQ in particular is more prone to false breakouts that resolve within 1\u20132 candles. "
             "Anchor zone context to the prior day's high/low or the overnight range before trusting a "
             "single candle there."],
            ["Any instrument, scheduled high-impact news",
             "Suspend candlestick reading around the release window (commonly 2\u20135 minutes before to "
             "several minutes after) \u2014 spread widening and liquidity gaps distort body-to-range ratios "
             "independent of genuine order flow."],
        ]
    ))

    # ------------------------------------------------------------------
    # 5.11 Practicals
    # ------------------------------------------------------------------
    out.append(h2("5.11", "Practicals"))
    out.append(prac(
        "5.1", "The Eight-Point Drill",
        "Do this on your own chart before moving to Module 6.",
        "<ol>"
        "<li>Pull up any 15M chart with at least 100 candles of history on an instrument you already "
        "know the session behaviour for.</li>"
        "<li>Find one real example of each pattern in this module: rejection/pin bar, engulfing, "
        "strong-bodied, momentum, inside bar, failed breakout, and a compression-into-expansion "
        "sequence. Screenshot or note the time of each.</li>"
        "<li>For every example, write one sentence answering each of the 8 points (WHAT / WHY / WHERE / "
        "HOW to identify / HOW to use / WHEN unreliable / WHAT invalidates / your own worked example) "
        "using the actual zone and structure visible on your chart \u2014 not the illustrative figures "
        "from this module.</li>"
        "<li>For each example, state explicitly whether the location made it meaningful or meaningless, "
        "citing the specific zone grade, liquidity, or lack of either.</li>"
        "<li>Discard any example you cannot locate a genuine zone or liquidity reason for \u2014 that "
        "absence is itself the point of the drill.</li>"
        "</ol>"
    ))
    out.append(prac(
        "5.2", "The Invalidation Rewrite",
        "A discipline drill specifically for the confusion between rejection and reversal.",
        "<ol>"
        "<li>Take one of the examples you found in Practical 5.1 where a candle appeared to confirm a "
        "thesis (a pin bar, engulfing candle, or momentum candle at a zone).</li>"
        "<li>Write down, in one sentence, the exact price/close condition on a later candle that would "
        "structurally invalidate that specific pattern \u2014 use the WHAT INVALIDATES row for that pattern "
        "as your template, not a generic stop-loss price.</li>"
        "<li>Scroll forward on the chart and check whether that condition happened. If it did, note how "
        "many candles later, and whether a trader anchored to the original candle's shape (rather than "
        "the invalidation condition) would have exited too late.</li>"
        "<li>Repeat for a second example. The goal is to build the habit of writing the invalidation "
        "condition down <em>before</em> price moves, not diagnosing it after the fact.</li>"
        "</ol>"
    ))

    # ------------------------------------------------------------------
    # 5.12 Vocabulary
    # ------------------------------------------------------------------
    out.append(h2("5.12", "Vocabulary introduced in this module"))
    out.append(table(
        ["Term", "Definition"],
        [
            ["Body-to-range ratio", "|close \u2212 open| \u00f7 (high \u2212 low), expressed as a percentage. "
             "The core measurement behind every pattern in this module."],
            ["Closing strength", "Where a candle's close sits within its own high-low range, independent "
             "of the candle's colour or body size."],
            ["Rejection candle / pin bar", "A candle with a small body pushed to one end of a long wick "
             "on the opposite side, recording a failed test of a price level."],
            ["Engulfing candle", "A candle whose body fully covers the body of the candle immediately "
             "before it, in the opposite direction."],
            ["Strong-bodied candle", "A candle with a high body-to-range ratio and short wicks on both "
             "ends, showing one-sided control through the close."],
            ["Momentum candle", "A strong-bodied candle that is also unusually large relative to the "
             "candles preceding it, adding urgency to the evidence of control."],
            ["Inside bar", "A candle whose entire range sits within the range of the candle immediately "
             "before it (the mother bar)."],
            ["Mother bar", "The candle that an inside bar (or a run of inside bars) is contained "
             "within."],
            ["Failed breakout", "A candle that wicks through a structural level but closes back on the "
             "original side of it, showing the break did not gain acceptance."],
            ["Acceptance", "Confirmation that price is willing to close, not just wick, beyond a level, "
             "typically requiring more than a single candle."],
            ["Compression", "A visibly shrinking high-low range across several consecutive candles."],
            ["Expansion / displacement candle", "A candle whose range significantly exceeds the "
             "candles preceding it, typically resolving a compression sequence."],
        ]
    ))

    # ------------------------------------------------------------------
    # 5.13 Summary
    # ------------------------------------------------------------------
    out.append(h2("5.13", "Summary"))
    out.append(summary([
        "A candlestick is a compressed record of a 15-minute fight, reduced to open/high/low/close \u2014 "
        "never a magic signal on its own.",
        "Body-to-range ratio and closing strength are the two measurements underlying every named "
        "pattern in this module.",
        "Rejection candles/pin bars record a failed test of a level; they are meaningful with a graded "
        "zone and swept liquidity behind them, meaningless without either.",
        "Engulfing candles record a complete reversal of control within one candle; treat as stronger "
        "evidence than a same-size pin bar at the same location.",
        "Strong-bodied and momentum candles record one-sided control, with momentum adding size/urgency "
        "\u2014 both are unreliable immediately around scheduled news and late in an already-extended move.",
        "Inside bars record a pause in participation and warn of coming expansion, but never indicate "
        "direction on their own.",
        "Failed breakouts record a level being defended by consuming breakout liquidity \u2014 weaker "
        "evidence inside a strongly trending market against the trend.",
        "Compression-into-expansion sequences warn that a move is increasingly likely, again without "
        "specifying direction \u2014 the resolving candle's own body and context supply the direction.",
        "The same candle shape can be highly reliable, weakly reliable, or meaningless depending only "
        "on location, zone grade, and swept liquidity \u2014 never evaluate a candle in isolation.",
        "A candlestick trigger can raise or lower confidence inside an already-valid Module 4 setup; it "
        "cannot create a valid setup out of a location Module 2/3 has not already qualified.",
    ]))

    return "\n".join(out)
