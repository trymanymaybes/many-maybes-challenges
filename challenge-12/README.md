# Challenge 12 — Same garden. Different feeling.

Revision 2 replaces the bridge/stage/jetty exercise with **framing through captions and selective visual emphasis**. The creative question is: **Can you change how a garden feels without changing what happened?**

## Review the illustrations

- [Optimism — Look what has grown](challenge-12-optimism.svg)
- [Pessimism — Look what has not grown](challenge-12-pessimism.svg)
- [Curiosity — What can we learn?](challenge-12-curiosity.svg)

![Optimistic framing of the detailed garden](challenge-12-optimism.svg)
![Pessimistic framing of the identical garden](challenge-12-pessimism.svg)
![Curious framing of the identical garden](challenge-12-curiosity.svg)

## Starter and fixed facts

The original starter remains [one faceless figure and one horizontal line](challenge-12-starter.svg). In this revised exercise, that simple shape is supplemented by a fixed scene brief: a gardener and planting bench with ten numbered pots. Pots 1, 2, 3, 6, 7 and 8 have shoots; pots 4, 5, 9 and 10 do not. We describe the supplied result as six seedlings grew and four did not; the picture alone does not prove why or predict what happens next.

The bench, fence, paving, watering can, empty seed tray, seed envelope, gloves and tools provide a rich shared setting. They are identical across all versions. The character is a stylized fixed mark; do not change its expression or pose to communicate the viewpoint.

## Your challenge

1. Draw the shared garden once, retaining the original figure and line, or use the supplied complete garden.
2. Copy that complete scene three times. Preserve all objects, counts, growth, positions and details. Keep all ten pots visible and countable. You may uniformly scale the entire scene.
3. Create an optimistic, pessimistic and curious interpretation using a caption and visual emphasis. You may use an annotation frame, an enlarged copy of an existing detail, or a separate observation panel. Label repeated details as insets, not additional objects.
4. For each version, write **thought → evidence → drawing choice → intended feeling**. Make the connection concrete.
5. Show the pictures before naming the viewpoints. Ask what the viewer notices and feels. A different response is useful feedback, not a wrong answer.

Paper, freehand and Turtle all work. The text-only alternative is to describe the fixed garden and propose three captions plus the visual detail you would emphasize.

## Thought drives drawing

| Viewpoint | Thought | Evidence selected | Drawing decision | Intended reading |
|---|---|---|---|---|
| Optimism | There is growth worth appreciating. | Six shoots exist. | Repeat three existing growing pots at a larger scale; retain every leaf and vein; caption “Six seedlings grew — more than half.” | Appreciation of the growth, without erasing the missing growth. |
| Pessimism | The missing growth dominates my view. | Four pots have no shoots. | Repeat two existing bare pots at a larger scale; emphasize their soil and rims; caption “Four seedlings did not grow — two in five.” | Disappointment or concern about missing growth, without removing successful growth. |
| Curiosity | Understand the result before judging. | Both counts are known; causes and expectations are unknown. | Give the full scene equal attention; draw a separate observation sheet recording 6/4 and unanswered questions. | Interest in finding out more. Curiosity is an additional inquiry stance, not a claim of perfect neutrality. |

The inset is a selection, not a claim that it shows every pot in that outcome group. Pot numbers trace each magnified detail back to the complete garden. The observation sheet is an editorial annotation outside the scene, not an object that appears only in one physical garden.

## What the seedling example explains

“Six grew” and “Four did not grow” describe complementary parts of the same outcome. Their emphasis may influence interpretation. We now extend that idea to visual emphasis: the physical scene is fixed, while a caption and annotation guide attention. This is an illustrative creative exercise, not a psychological test or proof of a universal viewer response. Different accent colors are design choices; isolate caption effects separately if testing wording alone.

Do not add rain, dead plants, happy faces, butterflies, new growth, blame, or predictions to manufacture a viewpoint. Do not draw roots or causes we cannot see. A growing result cannot be judged good or bad without expectations or comparison.

Reflection: Which strokes were observations? Which were editorial choices? Did your intended feeling reach the viewer? What would you need to know before judging the garden?

## Files and use

`optimism.py`, `pessimism.py` and `curiosity.py` are standalone standard-library Turtle drawings. Run `python -i optimism.py` to keep the window open. `starter.py` preserves the original simple shape. All active strokes use `st()`; pen-up travel and final holds use `ht()`. No video or audio is created.

SVGs carry descriptive title/alt text. `scene.json` stores shared physical paths and pot identities; `manifest.json` records constraints. Private source includes a reproducible static asset builder and updated screenplays. Videos remain on hold, and the website is not deployed by this revision.
