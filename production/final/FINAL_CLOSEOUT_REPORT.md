# DESPERADO EP01 Frame-Animation Rebuild — Closeout

- Production URL: https://desperado-moving-webtoon.ktsjjcap.workers.dev/episodes/ep01/pilot
- Deployed and production-tested SHA: the head SHA recorded by the latest successful `Deployed Visual QA` run
- Baseline content run: `34565037272` — SUCCESS
- Runtime: eight Canvas frame sequences; 64 illustrated runtime frames; exact reverse frame selection
- Art: real illustrated characters, faces, eyes, hands, boots, door, lever and corridor; no CSS character/prop substitute
- Sound: Korean voice tracks + 42-second continuous score + corridor ambience + scene-specific cloth, heel, latch and security foley
- Scroll: 6.49 viewport total; 0.68–1.08 viewport per scene
- Production browser: eight scenes and all Canvas sequences loaded; forward frame progression PASS; reverse 5→0 PASS; audio gate PASS; final title overflow fixed
- Automated production QA: mobile 390×844 and desktop 1440×900 PASS
- Visual captures inspected: SC00, SC02, SC05, SC06, SC07 PASS
- S issues: 0
- A issues: 0

The rejected single-still clipping/zoom implementation is not used by the active reader.
