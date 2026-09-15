# Browser, visual, and accessibility verification

Exercise the real route and journey in an actual browser. Verify loading, empty,
success, validation, permission-denied, provider/network failure, retry/recovery,
and destructive confirmation states that apply. Check navigation, refresh/deep
link, back/forward, session expiry, and persisted state where relevant.

For visual changes inspect screenshots at the actual target viewports rather than
inferring from CSS or a component snapshot. At minimum cover the primary desktop
width and a realistic mobile width; include intermediate/tablet when layout logic
changes there. Check overflow, clipping, text wrapping, touch targets, sticky
surfaces, modals, virtual keyboards, orientation, and reduced motion.

Accessibility evidence should include keyboard-only completion, visible focus,
semantic names/roles, label/error association, focus movement for dialogs and
route changes, contrast, zoom/reflow, screen-reader announcements for dynamic
state, and pointer alternatives. An automated scan is useful but not sufficient.

Inspect console errors, failed requests, hydration warnings, and asset/loading
behavior. Confirm that apparent success corresponds to the expected server/data
effect when the journey mutates state.

Capture final-state screenshots after fonts/assets/data settle and identify route,
viewport, build/environment, and relevant test identity. Do not treat a single
cropped screenshot as proof of interaction or responsiveness.
