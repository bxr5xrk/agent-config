# Security review

Perform a focused review of the changed trust boundaries. Use a dedicated installed security workflow for a requested deep audit; a small UI change does not need a whole-system security scan.

Read the [shared context and model policy](../../references/context.md); recall only approved applicable security lessons.

1. Read the brief, architecture, changed files and callers. Identify actors, assets, entry points and trusted/untrusted transitions affected by the change.
2. Use [boundary checks](references/boundaries.md) and current relevant official guidance. Trace candidate issues to a reachable path and concrete impact; separate validated findings from hypotheses.
3. Validate safely in local tests or an authorized test environment. Do not send real customer messages, trigger purchases or mutate production data merely to prove a path.
4. Return location, preconditions, affected actor/data, evidence and smallest effective fix. Do not report a theoretical issue as confirmed or label a focused review a security certification.
5. After the owner fixes an accepted finding, repeat the negative-path check and inspect the final code. Check that the fix preserves intended access and recovery.

Retain only redacted technical evidence. Secrets and private payloads do not belong in global specialist learning.
