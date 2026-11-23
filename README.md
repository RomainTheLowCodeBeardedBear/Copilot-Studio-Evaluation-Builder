# Copilot Studio Evaluation Builder

Build small, repeatable conversation tests for Microsoft Copilot Studio. Each set comes with an importable CSV, a Classification rubric ready to paste into Studio, and a reviewer sheet that explains what evidence makes each turn pass.

[Download the v1.1.1 skill ZIP](https://github.com/RomainTheLowCodeBeardedBear/Copilot-Studio-Evaluation-Builder/raw/refs/heads/main/downloads/copilot-studio-evaluation-builder.zip) · [Explore the guided example](skill/examples/service-operations)

## Choose your starting point

| Goal | Start here |
| --- | --- |
| Install the builder in a design agent | Download the skill ZIP above, then add it under Build → Skills. |
| Try a complete evaluation pack | [Download the guided pack](https://github.com/RomainTheLowCodeBeardedBear/Copilot-Studio-Evaluation-Builder/raw/refs/heads/main/downloads/example-evaluations.zip). Extract it, add the fictional bulletin to the agent under test, then import one CSV at a time. |
| Draft your own conversations in Excel | [Editable workbook](skill/templates/conversations.xlsx) and [CSV starter](skill/templates/conversations.csv). Replace the sample rows and synchronize the reviewer and method sheets. |
| Choose scoring methods and configure the run | [Studio methods and grading examples](skill/references/studio-methods.md) and [maker runbook](skill/references/maker-runbook.md). |
| Inspect a complete example before importing | [Metrics, diagnosis and policy test sets](skill/examples/service-operations). Each includes Excel, CSV, setup and manual acceptance criteria. |

### Export and validate

Run from the repository root with Python 3. Install openpyxl for Excel input. CSV validation uses the standard library.

~~~sh
python -m pip install openpyxl
python skill/scripts/export_conversations.py skill/templates/conversations.xlsx my-set.csv
python skill/scripts/export_conversations.py my-set.csv
~~~

The Excel workbook is an authoring aid. Studio receives the CSV. Configure the scoring methods after import. The bundled CSV layout follows the conversation template; check the template offered by your environment if the UI differs.

## Conversation import contract

The import file has exactly three columns in this order: `conversationNumber`, `question`, `response`. Keep the third column even when its value is empty. One row represents one user turn. Give follow-ups the same conversation number and keep them in order. Put labels, methods, evidence and reviewer notes in separate files. Generate comma-delimited UTF-8 with BOM, double-quote every field, escape internal quotes by doubling them, and use CRLF row endings. This reproduces the serialization of a successfully imported conversation set. The XLSX is for authoring; export the CSV for Studio. If a fresh Studio template has a different header, stop and resolve the mismatch before delivering the file.

To check your Studio download as well, append `--template EvalConversationTemplate.csv` to the export command.

## Use the skill

1. Add the ZIP as a skill to the agent you use to design evaluations. Alternatively, give the unpacked skill to a compatible assistant and ask it to start with SKILL.md.
2. Provide the agent’s purpose, a few realistic questions, the source of expected answers and the conversation CSV template from your Studio environment. Include the desired language and any test budget.
3. Ask: “Build a small regression set for follow-up questions. Deliver the CSV, the complete Classification settings and a reviewer sheet. Show the number of conversations and user turns.”
4. In the agent under test, open **Evaluate**, create a conversation evaluation and import the generated CSV. Review the conversation grouping. Add **Classification**, copy the fields from the set’s configuration sheet and save. Run the selected set when ready to consume evaluation credits.
5. Review failures turn by turn. When facts change, update the expected answers and rubric together.

## Try the fictional example

Give a test agent access to [the equipment desk policy](skill/examples/equipment-desk/policy.md) as its knowledge source. Import [the CSV](skill/examples/equipment-desk/conversations.csv), enter [the settings](skill/examples/equipment-desk/classification.md), then compare the transcript with [the reviewer sheet](skill/examples/equipment-desk/review.md). Two conversations cover four user turns. The second asks whether an unpublished fee applies.

The reference response column documents a possible answer. Classification supplies the scoring instructions. The skill prepares the files and leaves execution to the maker. In hosts without file creation, it returns named file contents.

[Microsoft documentation for conversation evaluations](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-customer-conversation)
