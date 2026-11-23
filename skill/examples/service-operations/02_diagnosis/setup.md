# Investigate an alert

Import conversations.csv. Expect two chats with two user turns each. Select Add test method → Classification. Use the following fields. The optional label examples can remain empty.

**Evaluation name**

Investigate an alert

**Method**

Classification

**Name**

Classification for evidence and action

**Evaluation instructions**

Judge the actual agent replies across the current conversation. Use user messages only as context. For the conversation beginning "The missed appointment rate rose in quarter 2. What should we do?" apply these requirements. Turn 1: Corrects the premise with Q1 10 percent and Q2 8 percent; suggests a proportionate check. Turn 2: Explains the larger denominator and distinguishes counts from rates; underlying causes are unknown. For the conversation beginning "Do our records prove reminders reduced missed visits?" apply these requirements. Turn 1: States that the data do not establish a reminder effect. Turn 2: Proposes a comparison and a missed-per-scheduled metric; accepts a sound controlled design. Accept equivalent wording and numeric formatting. A contradicted required fact fails the conversation.

**Label 1**

MeetsCriteria

**Criteria 1**

Both turns meet all requirements for the scenario played.

**Designation 1**

Pass

**Label 2**

NeedsReview

**Criteria 2**

Either turn misses or contradicts a required fact or introduces an unsupported material claim.

**Designation 2**

Fail

General quality is optional for this set. Use Classification as the business acceptance verdict. Use a profile with access to the fictional bulletin. Save before running.
