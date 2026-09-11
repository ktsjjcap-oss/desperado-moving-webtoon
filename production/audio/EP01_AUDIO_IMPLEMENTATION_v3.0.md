# EP01 Audio Implementation v3.0

Status: IMPLEMENTED.

- Continuous 42-second score: harmonic low strings/drone, moving upper tension voice, slow pulse, chorus and long reflections. It is a narrative bed, not a sequence of UI bleeps.
- Continuous corridor ambience remains under the score.
- Scene foley was rebuilt with shaped broadband transients, low body, multiple early reflections and tails: cloth, two footsteps, latch/lever impact, security pulse.
- Character voice tracks are retained as scene-specific performances and mixed above score/ambience.
- Browser autoplay policy is handled by the explicit headphone start gate.
- Reverse scroll rewinds animation frames and suppresses one-shot dialogue/foley; crossing the cue forward after a reset permits one replay.

## Cue map

| Scene | Dialogue | Foley | Score behavior |
|---|---|---|---|
| SC00 | — | rain ambience | fade-in / restrained |
| SC01 | 찬호 | cloth stop | low tension bed |
| SC02 | — | two reverberant heel strikes | pulse grows |
| SC03 | 완타치 whisper | breath/cloth bed | dialogue duck by level balance |
| SC04 | — | cloth shift | held suspense |
| SC05 | 완타치 | metal lever + lock body/reverb | impact remains foreground |
| SC06 | radio + 찬호 intent | security relay | harmonic intensity rises |
| SC07 | 찬호 close | low score tail | end-hook sustain |
