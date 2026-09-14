# DESPERADO EP01 Moving Webtoon v4 — Closeout

> **STATUS: RELEASE CANDIDATE — 2026-09-14.** The rejected stepped-frame presentation has been replaced with continuous adjacent-frame dissolves, independent scroll-linked atmosphere/effects, timed dialogue beats, and a corrected Silver Lily hero reveal. The artifact now matches the locked ivory glove, platinum lily metalwork, deep-blue stone, and rectangular ballistic-glass display.

- Runtime: exact bidirectional scroll playhead with continuous adjacent-frame blending; freeze on stop and reverse on upward scroll.
- Story presentation: eight authored shots with sequential dialogue, narration, SFX typography, target identification and end hook.
- Visual effects: rain, corridor light sweep, floor ripple, latch contact, security scan and alarm sweep move independently of the camera.
- Audio: opt-in Korean voices, continuous score, ambience and scene Foley retained.
- Responsive target: mobile-first 9:16 reader with desktop framing and reduced-motion fallback.
- Release asset correction: Silver Lily is now a clean, text-free target master rather than the previously incorrect corridor frame.

> **STATUS WITHDRAWN / FAIL — 2026-09-14.** Director review found that the eight-frame sequences read as a slideshow/zoom animatic, not a commercial moving toon. The S/A=0 claims below are retained only as a historical record and are no longer valid. The governing corrective design is `production/benchmark/GLOBAL_MOVINGTOON_RESEARCH_AND_REBUILD_ARCHITECTURE_v3.0.md`.

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
