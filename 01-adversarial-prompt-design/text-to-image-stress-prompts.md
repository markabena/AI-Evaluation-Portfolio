# Text-to-Image Stress Prompts

Ten original prompts written for this portfolio. Each one stacks several independent, checkable requirements. The notes under each prompt say what it targets and what to verify first.

---

### 1. Aircraft maintenance bay

> Close-up photograph of a mechanic's gloved left hand holding a torque wrench on the third of four visible bolts on an aircraft wheel hub. A yellow inspection tag hangs from the axle reading "INSP 14/03 – OK". Hangar lights reflect in a puddle of hydraulic fluid on the floor below.

**Targets:** hands gripping a tool, exact count (four bolts, third one engaged), legible text with a date format, reflection consistency.
**Check first:** bolt count and which bolt the wrench sits on; the tag string character by character; whether the puddle reflection matches the lights above it.

### 2. Market stall price board

> A fruit seller's chalkboard at a Kaduna market listing exactly five items with prices in naira: "Oranges ₦500", "Pawpaw ₦1,200", "Pineapple ₦1,500", "Mango ₦300", "Banana ₦800". The seller's hand is pointing at the pineapple line.

**Targets:** five exact text strings, a currency symbol models rarely see, a hand pointing at a specific line.
**Check first:** that all five lines exist and are spelled correctly; that ₦ renders as ₦ and not N or #; which line the finger actually points at.

### 3. Wall clock and mirror

> A kitchen wall clock showing 4:40, photographed so it also appears in a round mirror on the opposite wall. A woman stands between them, facing the mirror, adjusting an earring with her right hand.

**Targets:** a specific clock time, mirror reversal of the clock face, a person's reflection that has to match front and back, handedness.
**Check first:** the time on the real clock; whether the mirrored clock is correctly reversed; whether the mirror shows her face (it should); whether the mirror image uses the correct hand.

### 4. Bar chart on a laptop

> A laptop on a desk showing a bar chart titled "Q3 Deliveries" with four bars labelled Jul, Aug, Sep, Oct and values 12, 18, 9, 21 printed on top of each bar. A sticky note on the bezel reads "check Oct".

**Targets:** chart values that must match bar heights, axis labels, a title, a second text element.
**Check first:** whether bar heights are ordered 21 > 18 > 12 > 9; whether each printed value matches its label; title and sticky-note spelling. Note: the prompt says Q3 but includes October. That's deliberate: it tests whether the model follows the stated labels rather than "correcting" them. Don't mark the October bar as a defect.

### 5. Chess endgame

> Overhead photo of a wooden chessboard with only four pieces left: white king on g1, white rook on a7, black king on g8, black pawn on h7. A player's hand is lifting the white rook.

**Targets:** board geometry (8×8, alternating colours, light square at h1), exact piece placement, a hand lifting a small object.
**Check first:** square count and colouring; the piece count (exactly four, with one in the hand); the rook's origin square.

### 6. Pharmacy shelf

> Three rows of medicine boxes on a pharmacy shelf. The middle row has exactly six identical white boxes labelled "Paracetamol 500mg" with a blue stripe. One box in the middle row is turned sideways.

**Targets:** repetition with exact count, repeated label text, one deliberate break in the pattern.
**Check first:** six boxes in the middle row; label text on each visible face; exactly one box rotated.

### 7. Rare animal in context

> A pangolin curled halfway into a ball on a dirt path at dusk, with a park ranger in a khaki shirt crouched two metres behind it, holding a clipboard. Low sun from the left.

**Targets:** a less common animal (scale pattern, tail shape), relative distance and placement, lighting direction.
**Check first:** scale anatomy; whether the ranger is behind, not beside; whether shadows fall to the right.

### 8. Flag lineup

> Four national flags on poles outside a conference centre, left to right: Nigeria, Czech Republic, Ghana, Canada. Light breeze, flags partly unfurled.

**Targets:** real-world flag designs, left-to-right order, partial occlusion by folds.
**Check first:** each flag's design against the reference (Nigeria: green-white-green vertical; Czech Republic: white over red with a blue hoist triangle; Ghana: red-gold-green horizontal with a black star; Canada: red-white-red with a maple leaf); the order.

### 9. Lighting setup

> Studio portrait of an older man in a navy cardigan, lit with Rembrandt lighting from camera left, a small triangle of light on his left (shadow-side) cheek. He holds a pair of reading glasses by one arm; the lenses reflect a softbox.

**Targets:** a named lighting pattern with a specific signature, a hand holding a thin object, lens reflections that must match the light source.
**Check first:** triangle placement on the left, shadow-side cheek; glasses geometry (two lenses, two arms, one hinge each); the reflection matching the key light side.

### 10. Stacked spatial relations

> A red mug on top of a closed blue notebook, which sits on a stack of three hardback books. A pair of scissors lies open to the right of the stack, and a green pen is under the scissors.

**Targets:** four nested spatial relations, colour binding (models often swap colours between objects), an exact count.
**Check first:** each "on", "under", and "right of"; colours bound to the correct objects; three books in the stack.

---

## Why these work

Each prompt reads like a plausible photo brief, and every requirement can be verified by looking. None asks for a broken result. The failures that come back are the model's own.
