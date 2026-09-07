# PILOT COMMERCIAL QA GATE v1.1 — AUTONOMOUS PRE-USER QA

Reviewer must inspect the deployed mobile URL, not only source files.

## ABSOLUTE USER-HANDOFF RULE
**사용자에게 보여주기 전에 내부 QA를 먼저 끝낸다.**
작업자가 결과물을 만들었다고 바로 사용자에게 컨펌을 요청하지 않는다.

Production flow:
1. Build/assemble candidate.
2. Deploy candidate to the test/live URL.
3. Run full QA below as an independent reviewer.
4. If any valid S/A issue exists, DO NOT ask the user to review.
5. Perform Root Cause → Targeted Fix → redeploy → full re-QA.
6. Repeat until Final Blind Verdict = A and all hard gates pass.
7. Only then notify the user that a reviewable candidate is ready.

The user is **final creative approval**, not routine QA labor.

## QA INDEPENDENCE
Creator and Reviewer roles are separate. Reviewer evaluates the actual deployed mobile experience first and does not use production excuses as PASS evidence.

## Gate 1 — Webtoon Identity
Freeze at 8 representative scroll positions. Each must look like a publishable Korean webtoon frame/continuous panel, not a motion graphic mockup.

## Gate 2 — Scroll Storytelling
Verify reveal order at slow, normal, fast scroll. Guard and Silver Lily must not leak before intended threshold. Pausing must create a meaningful readable composition.

## Gate 3 — Motion Restraint
List every moving element and justify narrative value. Decorative motion with no value is removed. Static sections are required.

## Gate 4 — Reverse
Reverse from at least 10 arbitrary points. Scrubbed layers return continuously. No stuck opacity, jump cuts, duplicate balloon state, or audio machine-gun retriggers.

## Gate 5 — Dialogue
Read at 390px width. No balloon over focal face/eye/hand/tool/prop. Reading order remains obvious while scrolling both directions.

## Gate 6 — Sound
Sound OFF: story fully understandable. Sound ON: suspense/space materially improves. Browser autoplay policy respected. Audio trigger cooldown/hysteresis verified.

## Gate 7 — Continuity
Character masters, Service Corridor geography, Silver Lily, square case, rigging, lighting, glove/hand orientation remain consistent.

## Gate 8 — Cheap Motion Comic Detector
FAIL if the strongest impression is: Ken Burns zooms, slideshow, animated PPT, random parallax, excessive shake, generated-video wobble, or 'effects pasted on still images'.

## Gate 9 — Mobile Friction
Test at representative mobile viewport(s), including ~390×844 logical CSS px. Check scroll speed, thumb-friendly controls, no layout jump, no accidental horizontal scroll, no unreadable text, no sticky-layer tearing.

## Gate 10 — Regression After Fix
After every targeted fix, re-read the full pilot from the beginning. A fix may not break a previously passing beat, reverse behavior, continuity, sound state, or reveal timing.

## AUTONOMOUS FIX LOOP
For every FAIL:
- identify exact viewport/scroll range;
- state observed symptom;
- identify root cause;
- choose smallest targeted fix;
- rebuild/redeploy;
- retest the affected beat;
- then rerun the full pilot QA.

If the same root cause fails twice, the same implementation strategy is banned; redesign that beat instead of patching it repeatedly.

## Final blind verdict
Choose one:
A Commercial moving-webtoon pilot ready to show externally
B Promising prototype
C Technical demo
D Failed experiment
Only A passes.

Before A, reviewer must search for 10 reasons to downgrade it. Any valid S/A issue blocks A.

## USER HANDOFF CONDITION
Notify the user only when all are true:
- Final verdict A
- S/A issues = 0
- Sound OFF comprehension PASS
- Sound ON enhancement PASS
- Reverse PASS
- Webtoon Identity PASS
- Cheap Motion Comic Detector PASS
- Full regression PASS

When these are not met, continue the internal revision loop instead of asking the user to inspect an unfinished candidate.
