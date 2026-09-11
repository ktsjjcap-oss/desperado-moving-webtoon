# EP01 Frame Animation Manifest v3.0

Status: IMPLEMENTED — replaces the rejected single-still crop/transform build.

| Scene | Frames | Actual pose change | Scroll mapping | Reverse acceptance |
|---|---:|---|---|---|
| SC00 | 8 | rain, cloud light, traffic and tower pulse | scene progress → frame 0–7 | exact 7→0 |
| SC01 | 8 | notice, eye shift, hand raise, partner stop, settle | direct scrub | exact 7→0 |
| SC02 | 8 | alternating heel lift, strike and weight transfer | direct scrub | exact 7→0; no refire |
| SC03 | 8 | eye dart, blink, lean, whisper mouth shapes | direct scrub | exact 7→0 |
| SC04 | 8 | blink-to-gaze acting beat | direct scrub | exact 7→0 |
| SC05 | 8 | approach, finger wrap, lever rotation, recoil | direct scrub | exact 7→0 |
| SC06 | 8 | hand signal, crouch, target reveal, body turn | direct scrub | exact 7→0 |
| SC07 | 8 | door close, red sweep, head/shoulder turn, final look | direct scrub | exact 7→0 |

The reader draws independent redrawn frames to Canvas. No character, hand, eye, boot, door, or prop is built from CSS. CSS is limited to reader chrome, lettering, grading and film texture. Stable frames are real illustrated cuts.

## Runtime lock

- Total scene travel: 6.49 viewport.
- Largest scene: 1.08 viewport.
- Frame changes follow scroll progress; scroll stop holds, reverse scroll selects descending frames.
- Dialogue/SFX overlays reveal independently of the painted frame and remain readable at stable captures.
