# QA REPORT — MOVING WEBTOON ENGINE BASELINE v1.1

## INPUT
- Current deployed Cloudflare/GitHub technical demo
- User mobile/desktop screenshots from first external deployment
- Current `episodes/ep01/index.html`, `assets/style.css`, `assets/reader.js`
- Latest DESPERADO Production Bible / source-master material available in project library

## VERDICT BEFORE FIX
**C — TECHNICAL DEMO / FINAL FAIL**
Commercial confirmation prohibited.

## S0 / S1 FINDINGS
### S0-01 Silver Lily semantic error
The technical placeholder represented Silver Lily as a literal flower-like object. Current production rules define Silver Lily as a realistic luxury glove/artifact: ivory silk, royal-blue accent, platinum detail, deep-blue stone, approx. 23–25 cm. A flower-shaped placeholder risks corrupting production direction.

### S0-02 Presentation-card visual grammar
Reaction/hand placeholders appeared as isolated rounded cards. This reproduces the exact Storyboard/Presentation look prohibited by the commercial QA gate.

### S1-01 Reverse audio retrigger risk
Footstep triggers used a simple threshold state. Small up/down scroll oscillation could retrigger audio too easily. Moving webtoon requires hysteresis/reset behavior.

### S1-02 Commercial art absent
No approved character art, Service Corridor master plate, actual Silver Lily master, case master, or production audio is integrated. Therefore webtoon identity cannot be graded A.

### S1-03 Sound design is synthetic test only
Current WebAudio beeps validate browser interaction but do not validate ambience, spatial footsteps, mechanical hum, or commercial mix.

## TARGETED FIX COMPLETED
1. Replaced flower placeholder with a neutral glove-shaped Silver Lily structural placeholder. It remains explicitly non-final and does not claim to be the production design.
2. Removed rounded presentation-card treatment from reaction/command placeholders; changed to frameless strips/cut-ins.
3. Added audio trigger hysteresis with separate arm/reset thresholds to reduce duplicate retriggers during reverse/oscillating scroll.
4. Added reduced-motion protection for decorative home rain.
5. End-state label changed from implying a finished pilot to `PILOT ENGINE QA`.

## POST-FIX VERDICT
**C — TECHNICAL ENGINE BASELINE PASS / COMMERCIAL CONTENT NOT STARTED**

### PASS
- External deployment pipeline works.
- Mobile-centered vertical reader works.
- Scroll progress controls opacity/transform state.
- Up-scroll reverses scrubbed visual state.
- User-gesture sound enablement works.
- Basic threshold/hysteresis logic exists.
- Silver Lily placeholder no longer contradicts the locked artifact category.

### NOT YET PASSABLE
- Commercial Webtoon Identity
- Character fidelity
- Location fidelity
- Final Silver Lily / case fidelity
- Commercial lettering integration
- Real sound design
- Final scroll pacing
- Blind-reader A verdict

## NEXT GATE
Do not ask the user to judge this baseline again.
Next internal cycle must be:
1. Resolve and use approved Service Corridor / Silver Lily / Character masters.
2. Produce production-grade still assets for Corridor and Silver Lily Reveal only.
3. Integrate assets into the existing engine.
4. Run deployed-mobile QA internally.
5. FAIL → targeted revision → redeploy → re-QA.
6. Show user only when blind verdict reaches **A — Commercial moving-webtoon pilot ready to show externally** with no S/A issue.
