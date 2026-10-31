# Revision 5 validation

- SVG starter group is byte-identical across starter and all three completed scenes.
- All additions are unfilled line art; no opaque mask covers starter marks.
- Four Turtle programs executed against a recorder: 60 / 440 / 321 / 343 visible drawing segments. Every drawing movement had turtle visibility enabled; final turtle was hidden.
- SVGs rasterized successfully to 1200×1000 PNGs using Sharp. All three compositions visually inspected together for distinct silhouettes, legible headings and no clipped art.
- A GUI Turtle window and browser review page were not interactively tested. Recorder checks validate drawing calls, not actual rendering speed or narration timing.
- No audio, video or social upload was generated. Storyboards remain drafts.

Reproduce: `python build.py` then `python validate.py`. PNG export additionally requires an SVG rasterizer such as Sharp.
