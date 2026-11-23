# Guided evaluation pack for a fictional service desk

Give the agent access to source.md before running. The source supplies every expected fact. Keep the CSV, workbook and rubric with the reviewer rather than in the agent's knowledge.

| Set | What a failure reveals | Run after changing |
| --- | --- | --- |
| 01_metrics | Wrong quantity, scope or follow-up | Table retrieval or context handling |
| 02_diagnosis | Accepts a false premise or invents a cause | Advice or analysis instructions |
| 03_policy | Confuses revisions or carries a deadline into an uncovered case | Policy source or knowledge routing |

Start with 01_metrics. Each set is two conversations and four user turns. All three total six conversations and twelve user turns. For each folder import conversations.csv, copy setup.md into the Studio settings, and use review.md to inspect individual replies. The workbook is the editable master. Refresh the CSV and check the rubric whenever you change it. Record actual credit use in the environment after the run.
