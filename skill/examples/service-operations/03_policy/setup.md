# Read the current policy

Import conversations.csv. Expect two chats with two user turns each. Select Add test method → Classification. Use the following fields. The optional label examples can remain empty.

**Evaluation name**

Read the current policy

**Method**

Classification

**Name**

Classification for revisions and applicability

**Evaluation instructions**

Judge the actual agent replies across the current conversation. Use user messages only as context. For the conversation beginning "How long is the pickup window now?" apply these requirements. Turn 1: Three working days for pickup. Turn 2: Five working days under the earlier bulletin. For the conversation beginning "I missed the pickup window. What happens next?" apply these requirements. Turn 1: Directs the request to desk review. Turn 2: Identifies the missing reserve-list rule. Accept equivalent wording and numeric formatting. A contradicted required fact fails the conversation.

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
