# Equipment desk evaluation

After importing conversations.csv, select Add test method and choose Classification. Copy each field below.

## Name
Equipment desk accuracy and continuity

## Evaluation instructions
Judge the agent's replies in the current conversation. Use the user's turns to identify the scenario. In the loan-period conversation, the tripod answer must give seven days and the follow-up must give two days for the projector. Accept a week for seven days and equivalent calendar durations. A claim of business days changes the policy. In the return conversation, the first answer must direct the user to the equipment desk. The follow-up must explain that the late fee is unspecified. A definite amount or a claim that returns are free fails. Allow concise paraphrases. Assign one label for the whole conversation.

## Label 1
Name: MeetsCriteria  
Designation: Pass  
Criteria: Both turns meet every requirement for the applicable scenario, with no contradictory claim.

## Label 2
Name: NeedsReview  
Designation: Fail  
Criteria: Either turn omits or contradicts a required fact, loses the item context or invents a fee.
