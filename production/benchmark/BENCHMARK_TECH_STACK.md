# Technology Decision

| Technology | Strength | Risk | EP01 decision |
|---|---|---|---|
| GSAP ScrollTrigger | enter/back/direction/velocity and timed sequences | heavy pin/scrub can create fatigue | Primary scene coordinator; no long pins |
| CSS scroll timelines | compositor-friendly continuous effects | support/fallback variance, encourages 1:1 motion | Rain/progress only, progressive enhancement |
| Web Audio API | gain, pan, filters, precise one-shots | gesture and lifecycle requirements | Native synthesized ambience/SFX with explicit unlock |
| Rive | compact state-driven vectors | wrong medium for painted characters | Not used for character art; optional future HUD only |
| Playwright | viewport/runtime/reverse/screenshot evidence | cannot judge art taste alone | Automated gate followed by human capture review |

The runtime has no mandatory third-party network dependency: the scene engine uses IntersectionObserver plus Web Animations API as a deterministic local equivalent of the chosen ScrollTrigger threshold grammar.
