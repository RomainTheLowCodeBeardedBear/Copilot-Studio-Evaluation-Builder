---
name: copilot-studio-evaluation-builder
description: Design or revise multi-turn conversation test sets for Microsoft Copilot Studio. Generate populated Excel workbooks, importable conversation CSV files, complete Classification settings, and turn-by-turn acceptance checks from a maker's use case and evidence.
---

# Build a conversation evaluation

## Choose the work product

Generate a finished pack from the agent brief and evidence. The builder writes the conversations, expected outcomes and grading criteria, populates the workbook, exports the import CSV and prepares the Studio settings for each set. Use the maker's language throughout. Templates and code are internal production aids. Ask the maker only for missing facts that affect the verdict. Read references/maker-runbook.md and references/studio-methods.md when building.

## Establish the test contract

Identify the agent under test, the decision or behavior at risk, the language, and the evidence for each expected outcome. Use the maker's current conversation import template. When it is unavailable, use the bundled example's three-column layout and state the assumption. Ask a focused question if the missing answer would change what counts as success. For a test with missing evidence, test the promised clarification or scope boundary, or mark the numerical expectation pending and keep that case out of the runnable set.

## Required import format

The import file has exactly three columns in this order: `conversationNumber`, `question`, `response`. Keep the third column even when its value is empty. One row represents one user turn. Give follow-ups the same conversation number and keep them in order. Put labels, methods, evidence and reviewer notes in separate files. Generate comma-delimited UTF-8 with BOM, double-quote every field, escape internal quotes by doubling them, and use CRLF row endings. This reproduces the serialization of a successfully imported conversation set. The XLSX is for authoring; export the CSV for Studio. If a fresh Studio template has a different header, stop and resolve the mismatch before delivering the file.

## Design a small set

Start with the smallest set that can expose the target error. A useful starting point is two independent chats with an opening question and one meaningful follow-up each. Give each chat its own number. Make the follow-up retain context, change one dimension, correct an earlier assumption, or ask for information outside the available source. Write natural user turns that still make sense if the previous agent reply was imperfect. Avoid putting the expected answer in the question.

Group conversations under one rubric only when their outcomes can be described unambiguously. Split sets by independently useful reruns. State conversations, user turns and the smallest rerun after a change. Estimate credits only when the maker provides a valid rate.

## Produce four completed files per runnable set

1. **conversations.csv**. Follow the supplied header, delimiter, encoding and current template limits. In the bundled layout use conversationNumber, question, response. Write one row per user turn, keep rows of each chat together and in order, and leave response empty when an example reply serves no purpose. Quote CSV fields correctly. Keep reviewer instructions out of the prompts. The optional reference reply is not an automatic correctness check.
2. **setup.md**. Write the set-specific import and configuration guide. Include the evaluation name, CSV filename, expected chat and turn counts, selected methods and reasons, profile prerequisites and the save/run steps. For each selected method give the exact fields to enter. For Classification supply the method name, full evaluation instructions and two labels. For each label provide its name, criteria and Pass or Fail designation. Use short ASCII label names such as MeetsCriteria and NeedsReview. Make criteria independently usable in Studio: embed the expected facts, accepted variants, tolerances and critical errors for each applicable scenario. Identify conversations by their topic or opening turn. Ask for one overall label for the current conversation based only on the agent's replies, using user turns for context. Never require an answer to a different conversation to earn a pass.
3. **review.md**. For each turn give the expected behavior, evidence locator, and an example of a material failure. Give the setup needed to reproduce the run, including any source version or role that affects the result. Record which evidence should be refreshed after a source change.

4. **authoring.xlsx**. Fill Conversations, Reviewer and Method from the same scenario data used for the CSV and setup guide. Remove every starter row. Verify the workbook exports back to the delivered CSV byte for byte.

In a file-capable host, generate actual files and return the ZIP. With Python and openpyxl, prepare a temporary JSON specification yourself and run scripts/build_set.py SPEC OUTPUT.zip for each set. The specification has three keys: conversations (a list of chats, each a list of turns with question, optional response, accept, evidence and fail), setup (localized Studio instructions including the set name and counts), and settings (an ordered mapping of Studio field labels to their finished text values). Include label designations and scenario-specific criteria. Deliver one folder per set in a combined ZIP when several sets are requested. Keep the temporary specification out of the deliverable. Other file-generation tools may implement the same output contract. If the host cannot create attachments, disclose which files could not be produced and provide the usable text outputs.

## Check before delivery

Parse the generated CSV and verify the exact header, grouping, order, field counts and limits. The example template permits up to 20 chats, six turns per chat and 1,000 characters per question. Resolve differences using the maker's current template. Match every runnable turn to evidence and a grading rule. Walk through one acceptable paraphrase and one plausible wrong answer; the rubric should distinguish them. Keep General quality separate from factual acceptance. When citation feedback conflicts with the transcript, inspect each reply and open the cited evidence before diagnosing the failure.

Use examples/service-operations/ for a complete three-set handoff and the files under examples/equipment-desk/ as a worked example. For public examples, author an independent fictional source and derive the expected answers from it.
