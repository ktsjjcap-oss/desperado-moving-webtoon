# DESPERADO EP01 Scroll-Scrub Motion Spec v2.0

## Core behavior

Each scene converts its live viewport position into a normalized progress value. The render loop maps that value directly to character-region, prop, foreground, camera and lettering transforms. Therefore slow scroll produces slow motion, stopping holds the current pose, and reverse scroll restores the preceding pose.

## Scene motion

| Scene | Camera | Local motion |
|---|---|---|
| SC00 | rain-city drift and pull-out | two-depth rain travel |
| SC01 | lateral corridor push | stop hand rise, shoulder weight shift, threat approach |
| SC02 | low tracking move | two-phase alternating boot steps |
| SC03 | reaction push | eye tracking, double blink, breathing |
| SC04 | exit search pan | gaze region crosses toward the door |
| SC05 | grip push | hand closes, lever rotates, impact shake |
| SC06 | target reveal | foreground pass, target push, security pulse |
| SC07 | closing pull-back | body turn-back and title resolve |

## Reverse policy

All visual properties are pure functions of scroll progress and therefore deterministically reversible. Dialogue is event-based and is cancelled/reset rather than played backward.
