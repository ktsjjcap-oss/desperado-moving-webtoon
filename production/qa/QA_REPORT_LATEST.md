# DESPERADO EP01 QA Report — Commercial Rebuild

Date: 2026-09-10 UTC  
Production: https://desperado-moving-webtoon.ktsjjcap.workers.dev/episodes/ep01/pilot

## Results

| Gate | Result | Evidence |
|---|---|---|
| Q0 Source / Assets | PASS | six 941×1672 production masters; runtime WebP set 0.96 MB; obsolete CSS placeholder assets removed |
| Q1 Storyboard | PASS | v1.0 locks purpose, states, framing, layers, cues, reverse and QA for SC00–SC07 |
| Q2 Art | PASS | illustrated humans, faces, anatomical hands, boots, door/lever, Korean facility and target zone inspected |
| Q3 Motion | PASS | continuous scroll-scrub: hand/shoulder, alternating boots, eye blink/breath, gaze, grip/lever, foreground/target and turn-back states; deterministic reverse |
| Q4 Scroll fatigue | PASS | total 7.05 viewport; median 0.85; max 1.15 |
| Q5 Audio | PASS | five AI voice tracks, tension score, corridor ambience and four Foley/SFX files; explicit gesture unlock; ON/OFF recovery; 11/11 assets HTTP 200 |
| Q6 Visual | PASS | production captures inspected after scrub-motion layer feathering plus automated 390×844 and 1440×900 capture suite |
| Q7 Runtime | PASS | deployed workflow runs 53 and 54 succeeded; build meta matched tested main SHA; no page-origin console failure |
| Q8 Human commercial art | PASS | no gray placeholder, CSS human/prop, floating eye, malformed hand, empty panel or repeated 210vh scene |

Production observation: 8 scenes, full story ratio approximately 7.10 viewport, all raster layers loaded at 941×1672. Direct production QA confirmed scroll-progress movement, reverse restoration, audio-enabled state, final title frame and zero page-origin console errors. A first-pass hard clip edge in SC01 was marked FAIL, feather-masked, redeployed and visually rechecked before closeout.

Final severity: S=0, A=0, B=0, C=0.
