# Revision 4 design plan

## Goal and scope

Preserve Many Maybes' additive drawing format. The starter now consists of ten simple pots, six containing shoots. Participants create meaning by adding around those marks. The earlier person-and-line and complete garden are superseded; no compatibility with the previous cutout coordinates is claimed.

## Geometry contract

Canvas 1200×1000. Pot centers x=200,390,580,790,980; bases y=460,700. Pot IDs 1–5 in first row, 6–10 in second. Growing IDs 1,2,3,6,7,8; bare IDs 4,5,9,10. All examples embed the exact same `fixed-starter` paths, in the same position, color, width and order. Additions occupy the surrounding space. All ten remain visible in the main illustrations.

The fixed mark is a pot rim, tapered sides and soil line, plus a two-leaf shoot for six pots. Labels and border artwork are additions, not starter constraints.

## Composition choices

| View | Feeling or thought | Added drawing system | Evidence left visible |
|---|---|---|---|
| Optimism | Appreciate growth | Six green/gold oval medallions, double grouping frame, scrollwork, ornament, journal typography and pencil | Four unframed bare pots remain visible at right |
| Pessimism | Missing growth dominates attention | Heavy rust inspection block at right, four rectangular frames, inward arrows, corner brackets and hatch marks | All six growing pots remain visible at left |
| Curiosity | Understand before judging | Equal-cell blue notebook grid, ruler marks, numbering, observation lines and question boxes | All ten receive equal visual treatment |

The drawings are different compositions, not an identical full garden with three side panels. No pot is enlarged, moved, obscured or altered in the main task. The sun-like journal seal is a page ornament, not a claim about different weather. Frames are illustrated editorial devices, not new facts about plant care.

## Thinking methodology

1. State the thought: “There is growth worth appreciating.”
2. Identify the existing evidence: six shoots.
3. Choose marks that make that evidence prominent: medallions, grouping, line weight, detail.
4. Keep the other evidence visible: four bare pots.
5. Ask a viewer what stands out. Intended emotion is not guaranteed.

For pessimism, use the same reasoning with the four missing shoots. For curiosity, organize all observations and ask for missing context. Do not treat a pleasing composition as proof of any psychological law.

## Turtle and screenplay sequence

Draw the simple starter once. Reset to the exact same starter before each illustration. Then animate only the additions, explaining each meaningful group while the visible turtle draws it. Ornate curves are sampled paths; all are reproducible from source. Use st() on drawing strokes and ht() on travel and clean holds. Typography may be written, but the illustrated frame must be drawn rather than faded in.

A separate warm-orange guide follows the turtle along the margins; use brief acrobatics between chapters. It must never cover or modify the fixed pots. Pause for 3 seconds on each finished composition. Long form explains all three thought-to-stroke decisions. The challenge short provides the starter and hints without showing all solutions. The illustration short explains the optimism example.

## Optional cutout stage

This is a second activity, after the additive drawings. Opaque page with transparent openings uses matching 1200×1000 coordinates. Selected-pot windows span x=center±37, y=base−139 through base+4. Wide curiosity window spans x100..1110 and y280..770. Print mask and chosen illustration at exactly the same scale; use one overlay at a time. Lift to restore the entire drawing. A physical print/cut test remains pending.

Primary stage retains all evidence and changes emphasis. Secondary stage hides evidence and demonstrates selective presentation. Explain this distinction explicitly. Optional mask controls in `review.html` are off initially.

## Deliverables

- Simple starter SVG/PNG and Turtle source.
- Three distinct full-page SVG/PNG illustrations and matching Turtle sources.
- Geometry data and manifest for exact fixed-mark validation.
- Three optional transparent masks and local review HTML.
- Three revised complete video screenplays in the private repository.

No audio/video rendering or publication. Website remains undeployed for this challenge.
