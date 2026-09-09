# DESPERADO EP01 QA Report — Commercial Rebuild

Date: 2026-09-09 UTC  
Production: https://desperado-moving-webtoon.ktsjjcap.workers.dev/episodes/ep01/pilot

## Results

| Gate | Result | Evidence |
|---|---|---|
| Q0 Source / Assets | PASS | six 941×1672 production masters; runtime WebP set 0.96 MB; obsolete CSS placeholder assets removed |
| Q1 Storyboard | PASS | v1.0 locks purpose, states, framing, layers, cues, reverse and QA for SC00–SC07 |
| Q2 Art | PASS | illustrated humans, faces, anatomical hands, boots, door/lever, Korean facility and target zone inspected |
| Q3 Motion | PASS | scene state changes include local raster hand, threat, boot, eye/gaze, grip, target and impact states |
| Q4 Scroll fatigue | PASS | total 7.05 viewport; median 0.85; max 1.15 |
| Q5 Audio | PASS | explicit gesture unlock; ON/OFF recovery; scene cues; 1.5s cooldown |
| Q6 Visual | PASS | production captures inspected at 1363×936 plus automated 390×844 and 1440×900 capture suite |
| Q7 Runtime | PASS | deployed workflow run 51 succeeded; build meta matched tested main SHA; no page-origin console failure |
| Q8 Human commercial art | PASS | no gray placeholder, CSS human/prop, floating eye, malformed hand, empty panel or repeated 210vh scene |

Production observation: 8 scenes, full story ratio 7.0502 viewport, all six WebP masters 941×1672. Browser-only extension metadata warnings were excluded because they originate from a Chrome extension, not the page.

Final severity: S=0, A=0, B=0, C=0.
