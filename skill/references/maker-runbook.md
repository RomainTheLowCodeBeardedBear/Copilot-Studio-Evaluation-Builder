# From a maker brief to a guided evaluation pack

## Prepare the evidence

Ask for the agent's instructions, supported actions or knowledge boundaries, examples of realistic user questions, trusted reference facts and the conversation template downloaded from Evaluate. Accept a small sample of each. A transcript is an observed answer; verify it against the source before using it as a reference. If coverage is partial, preserve that boundary in the test. For a changing fact, capture the source revision and exact location in the reviewer sheet.

Map each risk to one observable mistake and one decision: release blocker, exploratory check or deferred case. For a new agent, start with a small smoke set. For a repair, reproduce the reported phrasing, add a follow-up that changes one dimension, and preserve one known-good case. For advice tasks, check the premise, the evidence, a proportionate next action and how the user could verify its effect.

## Workbook and CSV

Use templates/conversations.xlsx to draft one set per copy. Edit the Conversations sheet. The other sheets help the maker prepare evidence and method settings. Only the conversation table goes into the import. The optional response is a reference reply; include all grading facts separately in the Classification instructions. Keep private evidence out of the questions. The starter CSV is available when spreadsheet support is unavailable.

Export comma-delimited UTF-8 CSV. Excel regional settings can produce semicolons, and Excel may change IDs or interpret formulas. Use the exporter when possible, then parse the actual exported file. Check quoted commas, embedded quotes, accents and empty response cells. Keep the three headers in their original order. Remove spreadsheet notes and blank introductory rows; the helper also accepts the single-column comment preamble in the Studio sample. If the supplied template differs, inspect its limits and adapt the export before promising compatibility.

## Configure each set in Studio

1. Open the agent under test → Evaluate → create an evaluation → Conversation. Download the template when offered. Upload one set CSV and give the evaluation the name on its setup sheet.
2. In Review data set, open the conversations. Compare the opening questions, grouping and sequence to the reviewer sheet. With two filled question/response pairs in a chat the preview can show four messages. Count user turns separately.
3. In Select test methods, inspect the default General quality method. For a domain verdict choose Add test method → Classification → OK. Paste the name and full instructions. Fill both label cards, criteria and designations, then confirm. Follow the method sheet for any additional method.
4. In Additional configuration, select the intended user profile when access affects the outcome. Confirm source visibility and tool availability in that context. Use a test environment for side-effecting agents and design dry-run scenarios where appropriate.
5. Save before running. Start with the smallest affected set; report planned conversations and user turns. Studio shows credit use. Keep cost estimates separate from observed consumption.
6. In Results, select a chat and inspect each method and each reply. Record the build, profile, source revision, failure type and evidence. Recheck the same scope after a fix. Record unexecuted cases as pending.

## Deliver the pack

Generate one folder per set containing conversations.csv, setup.md and review.md. Add an editable workbook if requested or useful, and a short root index with set selection, prerequisites, counts and rerun order. ZIP these folders for handoff. A maker imports each CSV inside this archive individually. For a new design provide a smoke set first, then targeted sets for remaining risks. Verify the ZIP by reopening it and checking each referenced path.
