# DESPERADO EP01 Audio Implementation v2.0

## Runtime contract

- Audio starts only after the explicit `음성과 함께 시작` gesture.
- Two loop buses run continuously: corridor ambience and tension score.
- Dialogue and Foley cues fire only when forward scroll crosses the authored scene threshold.
- Reverse scroll never plays dialogue backward. Active dialogue is cancelled when audio is disabled; a cue becomes eligible again after returning below its reset band.
- The score/ambience mix changes continuously with global scroll progress.

## Delivered tracks

| Bus | Files | Function |
|---|---|---|
| VOICE | `sc01-chano`, `sc03-wantachi`, `sc05-wantachi`, `sc06-radio`, `sc07-chano` | Chano, Wantachi and radio dialogue |
| BGM | `tension-score.ogg` | Low-frequency tension arc |
| AMBIENCE | `corridor-ambience.ogg` | HVAC/electrical corridor bed |
| FOLEY/SFX | `footstep`, `cloth`, `handle-lock`, `security-pulse` | Scene-specific physical and security cues |

## QA gate

- Every local audio URL must return HTTP 200.
- Sound gate, header toggle, loop start/stop and visibility pause/resume must work.
- Voice, BGM and SFX are independently represented; oscillator-only placeholder audio is prohibited.
