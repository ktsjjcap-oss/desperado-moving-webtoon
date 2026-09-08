# DESPERADO Interactive Scroll Motion Webtoon — Commercial Master Spec v2

## Primary benchmark stack
- Commercial motion language: WEBTOON Video Episodes / The Mafia Nanny — dynamic motion, immersive sound/music, human voice acting.
- Reader-controlled grammar: continuous vertical scrollytelling and reversible scroll timeline.
- DESPERADO rule: preserve modern Korean webtoon identity; motion supports acting, suspense and comprehension rather than becoming an animation demo.

## Hard definition
A scene is NOT a moving-webtoon scene merely because CSS transform values change. PASS requires visible narrative state change.

Every major sequence must contain at least 3 of:
1. Character acting state change (eyes/head/arm/body/reaction)
2. Object state change (door/handle/shadow/prop)
3. Camera state change with meaningful reframing
4. Lighting/VFX state change
5. Dialogue/balloon timed to acting
6. Voice/Foley/Ambient/Music cue tied to the beat

## Pilot sequence grammar
S01 Corridor approach: movement → sound cue → stop → eye/head reaction → arm stop → camera push.
S02 Footstep threat: off-screen Foley → shadow approach → hold → listener reaction.
S03 Locked door: hand/handle action → resistance → impact/SFX → reaction.
S04 Guard passage: foreground occlusion → moving shadow → breath/eye tracking → release.
S05 Silver Lily: darkness → case silhouette → reflection sweep → ivory glove → platinum lily → blue stone → reaction/voice.
S06 Exit hook: target confirmed → route closes → suspense bridge.

## Scroll timeline
Scroll position is the playback head. Animation must pause with scroll and reverse coherently when scrolling upward. Autonomous micro-motion is permitted only for ambience (light flicker, breath, dust) and must never replace scroll-driven acting.

## Sound
Five logical buses: Ambient / Foley / SFX / Voice / Music. SOUND OFF is default for browser policy; after user opt-in, cues follow scene progression. Re-entry must not create uncontrolled overlapping voice playback.

## Commercial hard fails
- static panel + tiny zoom presented as motion
- repeated still image used as fake BG/Mid/FG layers
- long empty scroll used to hide absence of animation
- master-sheet edges or adjacent panels visible
- baked AI lettering in clean art
- dialogue detached from visual acting
- character identity drift
- asset/network/console errors
- motion that does not visibly change narrative state

## QA gates
1. Asset/Network/Console/Glyph/Layout QA
2. Scroll-state QA at 0/25/50/75/100 for every sequence
3. Visible-state QA: screenshots must show different narrative states, not only different matrices
4. Reverse QA
5. Audio trigger/re-entry QA
6. Director visual QA from evidence
7. Blind-reader gate: without explanation, the result must immediately read as an interactive moving webtoon.

No Production PASS until all gates pass and S/A issues = 0.