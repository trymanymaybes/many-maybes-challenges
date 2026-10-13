# Many Maybes - creative challenge code

Optional Python Turtle code for Challenge 01. Paper and ordinary drawing tools work too.
Try the challenge first: https://trymanymaybes.github.io/challenge-01.html

## Challenge 01: your first idea is only one

Keep all four original marks visible and preserve their relative positions. You may rotate or uniformly scale the whole starter, but do not move, erase or rotate individual marks. Explore an object, a place and something happening. Give your favourite interpretation a title and explain the assumption you changed. Rough sketches count. Examples are possibilities, not correct answers or participant submissions.

## Run

Python 3.10+ with the standard-library Turtle/Tkinter module installed. On some Linux systems install `python3-tk` separately. Windows and macOS Python installers normally provide Tkinter.

```sh
python -m venv .venv
# Activate .venv using the command for your operating system.
python -m pip install -r requirements.txt
python draw_cultural_park.py
python draw_richer_scenes.py
```

Outputs appear in `images/`: PNG, SVG and recorded drawing data. The park script also supports `--gui` to open a Turtle window. Headless export uses Turtle's `TNavigator` with a recording pen, then Pillow for raster rendering. It is not a screen recording. Font fallback supports different operating systems; typography can vary.

To regenerate just the fixed starter, run `python starter_turtle.py`. This optional SVG-backed generator uses svg-turtle and CairoSVG (Cairo libraries may need separate OS installation). The interpretation scripts need only Pillow plus standard-library modules and the bundled starter SVG; Cairo is not required for those.

## Files

- `starter_turtle.py`: fixed starting geometry.
- `challenge-01-turtle-starter.svg`: exact reference strokes.
- `turtle_engine.py`: Turtle movement recording and export helpers.
- `draw_cultural_park.py`: streets, tower terraces, theatre, garden and pavilion.
- `draw_richer_scenes.py`: underwater reflections and an inhabited artist's desk.
- `previous_scenes.py`: shared drawing foundations used by the richer scenes.

The export scripts assert that all reference starter segments remain unchanged under the common page offset. Changing starter coordinates is a separate experiment outside Challenge 01.

No accounts, credentials, network calls, participant data, voice models or video-production files are needed by this code. Generated files are ignored by Git. This repository provides publicly viewable source; no additional reuse licence is granted at this stage.
