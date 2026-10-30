# Challenge 12 — Cutout book design and production plan

Revision 3 · 30 October 2026 · design review · no video creation or publication.

## The intended experience

A viewer sees a detailed paper page with openings revealing part of a garden on the sheet behind it. They form an impression. The foreground page lifts away and the same complete garden appears. The moment of change is the discovery that the frame withheld evidence, not a transformation of the garden.

**Prompt:** Design three cutout pages that make one garden invite different readings: appreciative, disappointed, and curious. For each, explain what is visible, what is hidden, and how that choice could influence a viewer.

The previous person-and-line starter is retained within the underlying artwork, but the **active starter is now the complete fixed garden plus a blank overlay sheet**. This replaces the earlier rule that every pot must remain visible through every frame. Every pot remains present on the base; selective hiding is now the central mechanism.

## Fixed base illustration

Use `garden-base.svg` unchanged. The richly detailed setting includes a gardener, a planting bench with grain, bolts, supports and shelf, ten numbered terracotta pots with rim and soil detail, six shoots with leaf veins, four pots without shoots, fence slats, paving, a watering can and rose, an empty seed tray, gloves, hand tools and a seed envelope.

Known result: pots 1, 2, 3, 6, 7 and 8 grew; pots 4, 5, 9 and 10 did not. The base is reused byte-for-byte inside every composite. Never add leaves, alter growth, move plants, change weather, or replace a pot between reveals. Causes and expectations remain unknown.

## Page design specifications

| Page | Starting thought | Opening design | Foreground art | What becomes visible | Reveal and learning |
|---|---|---|---|---|---|
| Optimism: Look what grew | There is growth worth appreciating. | Six narrow rectangular openings, one over each growing pot. Each spans the shoot, leaves, soil and pot. | Two drawn greenhouse-like facades, roof lines, sills, book border and corner ornaments. Facades are drawings ON paper, not structures in the garden. | All six growing pots; no bare pot. Garden continuity is interrupted by opaque paper. | Lifting reveals four additional bare pots. Appreciation was based on a selected portion of the evidence. |
| Pessimism: Look what is missing | The missing growth dominates my view. | Four shorter rectangular openings aligned to the bare pots. | Four inspection frames and corner brackets, spacious paper, book border and quieter ornament. | Four bare pots; no shoots. | Lifting reveals the six growing plants. The absence seen through the openings was real but incomplete. |
| Curiosity: What else is there? | I want the whole result before judging. | One broad rectangular opening around the full garden scene. | Notebook-like surrounding frame, observation prompt and unanswered questions. | All ten pots, gardener and context. | Lifting adds the base's count caption. No false dramatic surprise: this frame already provided broad evidence. |

Mood is an intended reading, never a guaranteed psychological outcome. Accent colors, captions and decorative art also influence presentation; this is not an isolated laboratory test of aperture shape.

## Layer contract and coordinates

All layers: SVG viewBox `0 0 800 850`, nominal print size **200 × 212.5 mm**. The garden's existing 800 × 650 coordinates are translated by (0, 100); the geometry itself is unchanged. Full coordinates are recorded in `manifest.json`.

- Optimism: x centers 110, 155, 200, 510, 555, 600; openings x=center−18, y=358, width=36, height=94.
- Pessimism: x centers 245, 290, 645, 690; openings x=center−18, y=398, width=36, height=54.
- Curiosity: x=55, y=235, width=705, height=500.
- Alignment crosses: (30,120), (770,120), (30,800), (770,800).
- Left hinge guide: x=40. Keep binding outside the curiosity opening.

At nominal size, neighboring small windows retain 2.25 mm paper webs. This is a prototype tolerance, not a tested manufacturing specification. A larger print makes handling easier. Print every layer at the SAME scale. Never fit each page independently, because that breaks registration.

SVG overlays use an opaque compound path with **even-odd transparent holes**. White rectangles are not substitutes for holes. The only graphic in each hole is the underlying base; no duplicate plants are drawn into an overlay.

## Practical book assembly

1. Print the base and desired overlays on separate sheets. The local `review.html` print button outputs the base followed by the three overlay pages at a common size.
2. Use `*-cut-template.svg` if you want plain cutting guides. Cut only the solid inner rectangles marked CUT. Keep outside page boundaries, hinge margin and alignment marks.
3. Put the base flat behind ONE overlay. Align all four registration crosses before fixing the left edge with removable tape or a paper hinge. Use suitable cutting tools and assistance for narrow windows as needed.
4. Lift and lower the overlay to test reveal and registration.
5. Swap overlays, or mount each as a separate removable flap over the same base. **Do not stack the three opaque overlays:** their holes would intersect and block the intended views.
6. For a bound-book prototype, place a duplicate print of the identical base behind each overlay spread. These prints must use the same source, not regenerated alternate scenes.

The digital proof of concept has a left-hinged CSS lift. It is a review interaction, not a final page-curl animation or a video. Reduced-motion users receive an immediate state change. Print dimensions and hand-cut assembly require a physical trial; none is claimed yet.

## Turtle drawing and reveal choreography

1. Build the base: original mark, bench structure, pots, shoots and shared environment. The visible turtle traces active strokes with `st()`; use `ht()` for travel and clean holds.
2. Draw the foreground page on its own opaque working surface. The turtle traces border, facade or inspection decoration, and each aperture boundary. It must not draw new plants on this layer.
3. A clearly depicted cut/remove action turns the outlined interiors transparent. Use the geometry in the SVG, not a wipe that accidentally reveals a different scene.
4. Align the page above the base. Let the viewer inspect it for 3–4 seconds without guiding facial reactions.
5. Animate the overlay lifting about the left hinge for roughly 1–1.5 seconds. The base remains still, same size and position. Hold the full reveal for 4 seconds.
6. Explain the selection and repeat with the next page. Curiosity uses a calmer lift because the main garden is already visible.

The faceless gardener in the base never animates. The separate warm-orange stick-figure guide follows the turtle in the page margin, performs a small cartwheel between chapters, and looks puzzled during the first reveal. It never covers an aperture or acts out an emotion that the viewer is supposedly required to share.

## Three-video package

- Long YouTube video, approximately 6–7 minutes: custom hook, first-impression exercise, seedling caption analogy, rich base construction, all three overlay walkthroughs, reveals, limitations and invitation.
- Challenge short, approximately 55–65 seconds: one brief mask/reveal demonstration, explain the task, offer aperture-design hints, leave detailed solutions to viewers.
- Illustration short, approximately 70–85 seconds: construct the optimism overlay, explain the placement and purpose of all six openings, then lift to reveal hidden bare pots.

Detailed complete narration and scene directions are in the private `challenge-studio/media/12/` folder. Video generation remains on hold. No voice, music, rendered film or upload is part of this revision.

## What the principle is—and is not

The seedling captions emphasize complementary facts without necessarily hiding the image. A cutout **withholds part of the visual evidence**. We therefore describe this as selective presentation or visual framing, related to the framing-effect introduction. Do not call the two mechanisms identical. Do not imply that incomplete evidence justifies false counts or claims about causes.

The design practices asking: What can I see? What might the frame conceal? What am I inferring? What would I ask to reveal? A participant can submit three mask drawings and a written reveal explanation without cutting paper.

## Acceptance checklist

- Same complete base underneath all three pages; six growing and four bare pots.
- Optimism reveals exactly the six designated pot silhouettes; pessimism exactly the four designated bare pots; curiosity all ten and their surrounding scene.
- Small cutouts fit within pots' allotted columns and leave intact paper webs.
- No duplicate or fabricated plants inside the overlay.
- Closed and open states read differently, with registration unchanged.
- Readable instructions, descriptive SVG text, keyboard controls and reduced-motion support.
- Static visual review and geometry checks recorded; physical cutting and final video QA deferred.
