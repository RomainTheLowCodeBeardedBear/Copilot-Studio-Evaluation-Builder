---
name: copilot-studio-evaluation-builder
description: Design or revise multi-turn conversation test sets for Microsoft Copilot Studio. Generate importable conversation CSV files, complete Classification settings, and turn-by-turn acceptance checks from a maker's use case and evidence.
---

# Build a conversation evaluation

## Choose the work product

For a new evaluation, read references/maker-runbook.md and references/studio-methods.md. For an existing CSV, validate the original first and identify whether a failure comes from grouping, agent behavior, evidence or grading. For a guided handoff, deliver a ZIP organized like examples/service-operations/. Use templates/conversations.xlsx for Excel authoring and scripts/export_conversations.py for export and validation when the host can run Python. With no workbook tooling, use the CSV template and explicitly identify the outputs actually produced.

## Establish the test contract

Identify the agent under test, the decision or behavior at risk, the language, and the evidence for each expected outcome. Use the maker's current conversation import template. When it is unavailable, use the bundled example's three-column layout and state the assumption. Ask a focused question if the missing answer would change what counts as success. For a test with missing evidence, test the promised clarification or scope boundary, or mark the numerical expectation pending and keep that case out of the runnable set.

## Required import format

The import file has exactly three columns in this order: `conversationNumber`, `question`, `response`. Keep the third column even when its value is empty. One row represents one user turn. Give follow-ups the same conversation number and keep them in order. Put labels, methods, evidence and reviewer notes in separate files. Generate comma-delimited UTF-8 with BOM, double-quote every field, escape internal quotes by doubling them, and use CRLF row endings. This reproduces the serialization of a successfully imported conversation set. The XLSX is for authoring; export the CSV for Studio. If a fresh Studio template has a different header, stop and resolve the mismatch before delivering the file.

## Design a small set

Start with the smallest set that can expose the target error. A useful starting point is two independent chats with an opening question and one meaningful follow-up each. Give each chat its own number. Make the follow-up retain context, change one dimension, correct an earlier assumption, or ask for information outside the available source. Write natural user turns that still make sense if the previous agent reply was imperfect. Avoid putting the expected answer in the question.

Group conversations under one rubric only when their outcomes can be described unambiguously. Split sets by independently useful reruns. State conversations, user turns and the smallest rerun after a change. Estimate credits only when the maker provides a valid rate.

## Produce three files per runnable set

1. **conversations.csv**. Follow the supplied header, delimiter, encoding and current template limits. In the bundled layout use conversationNumber, question, response. Write one row per user turn, keep rows of each chat together and in order, and leave response empty when an example reply serves no purpose. Quote CSV fields correctly. Keep reviewer instructions out of the prompts. The optional reference reply is not an automatic correctness check.
2. **classification.md**. Supply the method name, full evaluation instructions and two labels. For each label provide its name, criteria and Pass or Fail designation. Use short ASCII label names such as MeetsCriteria and NeedsReview. Make criteria independently usable in Studio: embed the expected facts, accepted variants, tolerances and critical errors for each applicable scenario. Identify conversations by their topic or opening turn. Ask for one overall label for the current conversation based only on the agent's replies, using user turns for context. Never require an answer to a different conversation to earn a pass.
3. **review.md**. For each turn give the expected behavior, evidence locator, and an example of a material failure. Give the setup needed to reproduce the run, including any source version or role that affects the result. Record which evidence should be refreshed after a source change.

Return download links where supported, otherwise provide each filename and its complete contents. Use the maker's language for all three files unless asked otherwise.

## Check before delivery

Parse the generated CSV and verify the exact header, grouping, order, field counts and limits. The example template permits up to 20 chats, six turns per chat and 1,000 characters per question. Resolve differences using the maker's current template. Match every runnable turn to evidence and a grading rule. Walk through one acceptable paraphrase and one plausible wrong answer; the rubric should distinguish them. Keep General quality separate from factual acceptance. When citation feedback conflicts with the transcript, inspect each reply and open the cited evidence before diagnosing the failure.

Use examples/service-operations/ for a complete three-set handoff and the files under examples/equipment-desk/ as a worked example. For public examples, author an independent fictional source and derive the expected answers from it.
