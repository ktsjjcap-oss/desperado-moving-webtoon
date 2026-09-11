# DESPERADO EP01 Production QA — Frame Animation v3

Date: 2026-09-11 UTC  
Production: https://desperado-moving-webtoon.ktsjjcap.workers.dev/episodes/ep01/pilot  
Tested/deployed SHA: the head SHA recorded by the latest successful `Deployed Visual QA` run

| Gate | Result | Evidence |
|---|---|---|
| Local asset validation | PASS | 64/64 runtime WebP frames decode at 470×836; five v3 audio assets decode |
| Storyboard | PASS | SC00–SC07 purpose, acting, sound, trigger and reverse states locked |
| Visual | PASS | production captures show illustrated city, faces, eyes, hands, boots, door and security area |
| Scroll fatigue | PASS | 6.49 viewport total; max 1.08 viewport |
| Reverse scroll | PASS | SC07 frame index observed descending from 5 to 0 |
| Sound | PASS | explicit audio unlock changes to VOICE · SCORE · FOLEY; continuous score and scene cues return HTTP 200 in automated suite |
| Responsive | PASS | GitHub Actions mobile 390×844 + desktop 1440×900 |
| Performance | PASS | 64 compressed frames total 4.3 MB; DPR capped at 2; frame redraw only on index change |
| Deploy | PASS | Cloudflare production updated from main |
| Production browser | PASS | eight scenes, eight Canvas players, ratio 6.4904, unique v3 stylesheet loaded |
| Commercial art | PASS | no gray field, CSS person/hand/door, empty scene, oversized gap or clipped ending title |

Final severity: S=0, A=0.
