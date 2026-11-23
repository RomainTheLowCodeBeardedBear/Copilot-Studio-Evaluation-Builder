# Metrics and context

Import conversations.csv. Expect two chats with two user turns each. Select Add test method → Classification. Use the following fields. The optional label examples can remain empty.

**Evaluation name**

Metrics and context

**Method**

Classification

**Name**

Classification for quantities and scope

**Evaluation instructions**

Judge the actual agent replies across the current conversation. Use user messages only as context. For the conversation beginning "How many requests were closed in quarter 2 across all locations?" apply these requirements. Turn 1: 150 completed requests across all locations in Q2. Turn 2: 120 completed requests for Q1, same scope. For the conversation beginning "How much did completed requests grow from quarter 1 to quarter 2 in percent?" apply these requirements. Turn 1: 25 percent growth from 120 to 150; accept equivalent notation. Turn 2: Explains that a north-only growth rate needs location-level counts. Accept equivalent wording and numeric formatting. A contradicted required fact fails the conversation.

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
