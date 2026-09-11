# Motion judgment

Choose motion for a job: confirm input, explain causality, preserve spatial continuity, show truthful progress or create an intentional expressive moment. Sometimes an immediate state change does that job best.

Evaluate frequency, distance, content and user control together. Frequent work usually needs less ceremony; keyboard input is not itself a reason to ban motion. A short tab indicator can preserve orientation without delaying the tab. Do not make real completion slower to demonstrate a loading animation.

Treat duration/easing values as starting hypotheses within project tokens. Small feedback often needs less time than a large spatial transition; exit may be quicker than entrance. There is no universal 300ms ceiling, mandatory spring, fixed press scale or ban on ease-in, fade, bounce, blur or scaling from zero. Explain any unusual choice by its perceptual role and test it.

Keep trajectory and origin coherent with the trigger. Direct manipulation should track input without an artificial catch-up delay; release behavior may use velocity. Reversal should begin from the currently presented state rather than jumping to an assumed endpoint. Avoid mixing two engines that overwrite the same transform.

Reduced motion means removing or replacing nonessential movement while preserving state, meaning and access. A static equivalent may be better than a tiny animation. Handle the preference on initial load and when it changes; ensure skipped animation cannot strand hidden content, focus or pending state. Do not blindly apply a global 0.01ms rule to every animation-dependent component.

User control and accessibility remain separate from taste:

- Interaction-triggered nonessential motion can be disabled under WCAG 2.3.3 (AAA); honoring reduced motion is a useful product baseline even when the target is AA. [W3C](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
- Auto-starting moving/blinking/scrolling information lasting over five seconds alongside other content needs pause, stop or hide unless essential. Auto-updating parallel information has no five-second exception and may instead expose update-frequency control. Hover pause alone does not serve keyboard/touch users. [W3C](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- Keep focus indication stable, controls semantically operable and important status perceivable without animation. Do not use visual movement as the only confirmation or only way to perform an action.

Preserve source content as inspiration, not authority over the user/project. A library's demo can have a polished animation and incomplete interaction semantics at the same time.
