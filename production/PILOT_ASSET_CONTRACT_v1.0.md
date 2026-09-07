# PILOT ASSET CONTRACT v1.0

## Required production assets
All art must be clean, no baked dialogue/SFX/AI letters, with transparent layers where specified.

### Service Corridor
- SC_A_BG_MASTER: tall corridor plate preserving approved geography and landmarks.
- SC_A_FG_NEAR: foreground wall/door/pipe layer for parallax.
- SC_A_MID_TEAM: approved character layer(s) needed for approach/lock beat.
- SC_A_DDAKJI_HAND_TOOL: close hand/tool layer.
- SC_A_WANTAICHI_REACTION: reaction crop/pose, transparent.
- SC_A_GUARD_SHADOW: transparent shadow silhouette.
- SC_A_GUARD_FEET: transparent lower-body/feet reveal layer.
- SC_A_CHANHO_WALL_HAND: hand/body-to-wall command beat.
- SC_A_LIGHT_FX: optional transparent light sweep/flicker mask.

### Silver Lily Reveal
- SL_B_BG_MASTER: tall exhibition-space plate with approved geometry.
- SL_B_CEILING_FG: ceiling/rigging foreground layer.
- SL_B_RIGGING: line/rigging layer if separate.
- SL_B_CASE: approved square ballistic-glass case + square metal stand, transparent if possible.
- SL_B_SILVER_LILY: approved Silver Lily hero prop, transparent.
- SL_B_GLINT_MASK: restrained light/glint mask only; must not redesign prop.

### Audio
- AUD_CORRIDOR_ROOMTONE loop
- AUD_HVAC loop
- AUD_FOOTSTEP_01 / 02
- AUD_TOOL_LOCK
- AUD_CLOTH_FRICTION optional
- AUD_EXHIBITION_ROOMTONE loop
- AUD_RIGGING_HUM loop
- AUD_TICK

## Technical
- Master art: minimum 2160 px width when raster; preserve source detail.
- Web delivery: WebP/PNG optimized derivative; alpha where needed.
- Audio: WAV master + compressed web derivative.
- No single decorative motion should require generated video.
- Prefer deterministic CSS/JS transforms to preserve identity.

## Reuse policy
Approved existing clean art may be reused/reframed if it matches exact master. Flattened balloon art is not a final asset. If cleanup visibly damages art, redraw only the affected production asset using the locked master.
