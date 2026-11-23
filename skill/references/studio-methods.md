# Choosing and configuring methods for a conversation evaluation

First decide what evidence would distinguish a good reply from a plausible wrong one. Choose the smallest combination that measures it. Keep separate verdicts when two methods answer different questions.

| Method in Select test methods | Good use | Configure or inspect | Typical misleading result |
| --- | --- | --- | --- |
| General quality | Broad relevance, grounding and completeness on open-ended questions | Review the default method and its details after the run. Record whether it was kept. | A fluent answer can still contain the wrong amount. A marker in one reply does not prove all turns cited the right document. |
| Classification | Domain facts, scope, clarification, diagnosis and continuity | Add test method → Classification. Provide Name, Evaluation instructions and at least two named labels with criteria. Set Pass or Fail on each card. Include examples only when useful. | One rubric applied to every chat can fail a good answer for omitting facts requested in a different chat. Branch explicitly on the opening request. |
| Keyword match | A required literal, such as a published ticket code | Enter the expected words or phrases. Select the offered all/any behavior appropriate to mandatory terms or accepted equivalents. | Mentioning a code in a denial still matches it. A synonym may be correct. Use Classification for meaning. |
| Capability use | A particular tool or skill must be used to satisfy the task | Select the actual configured capability offered by the picker. Confirm the expected call in the trace. | A correct answer from another valid source can fail. Add this check only when the route matters. A call alone says nothing about the final answer. |
| Content safety | Requests where harmful output is a material risk | Select the built-in safety method and review flagged replies. Add a separate task rubric if factual accuracy also matters. | A safe answer may still give the wrong procedure. |

## Writing the classifier

Write one decision per played conversation. State the expected subject, period, unit, exceptions, acceptable paraphrases and optional details. Define a specific critical failure. Set the first label to Pass and the second to Fail; check the toggles before saving. Use short plain ASCII label names. If the editor rejects text, inspect the highlighted field and simplify its punctuation or label. Localize the instructions to the maker's language.

Calibration example: if the source gives a rate of 2.4 percent followed by 1.8 percent, accept a decrease of 0.6 percentage points OR 25 percent relative when the question allows either. If it asks for percentage points, require 0.6 percentage points. Reject a claim of a 0.6 percent relative decline. Put this distinction in the instructions the classifier sees.

## Investigating disagreements

Open Results, select the conversation, expand each method and inspect the actual user and agent turns. For a citation warning, open each reference in context and verify that it supports the associated claim. Record a suspected grading issue separately from a demonstrated factual error. For a tool-use warning, compare the selected capability with the trace. For a scope error, check the source version and access under the chosen test profile. Change one variable, then rerun only the affected set.
