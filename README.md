# Copilot Studio Evaluation Builder

Give the builder an agent brief and trusted reference material. It designs the test conversations and generates a ready-to-use evaluation pack for Microsoft Copilot Studio.

[Download the builder skill](https://github.com/RomainTheLowCodeBeardedBear/Copilot-Studio-Evaluation-Builder/raw/refs/heads/main/downloads/copilot-studio-evaluation-builder.zip)

## Ask for a test plan

Add the skill to your design assistant and provide the behavior to test, a source for the expected answers, and any constraints on language or test volume. Include the conversation import template from your environment if available. Use a host that can generate downloadable files.

> From the attached service policy, generate two small conversation test sets for our help desk agent. Cover a change of topic on a follow-up and a question the policy cannot answer. Deliver the files and Studio settings in French.

## What you receive

Each set in the generated ZIP includes:

| File | How to use it |
| --- | --- |
| conversations.csv | Import directly into **Evaluate → Conversation** in the agent under test. |
| authoring.xlsx | Inspect the populated conversations, reference checks and scoring settings in Excel. |
| setup.md | Follow the set-specific steps. Copy the evaluation name, method instructions and label criteria into Studio after import. |
| review.md | Compare the actual replies with the expected facts and their evidence, turn by turn. |

After import, verify the chat grouping, apply the settings from setup.md, save and run the selected set. The CSV carries the conversations. Studio scoring methods are configured separately.

[Download a finished fictional pack](https://github.com/RomainTheLowCodeBeardedBear/Copilot-Studio-Evaluation-Builder/raw/refs/heads/main/downloads/example-evaluations.zip) · [Inspect its files](skill/examples/service-operations) · [Studio scoring methods](skill/references/studio-methods.md) · [Conversation import and setup guide](skill/references/maker-runbook.md)
