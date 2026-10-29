# Rachel & Ron | Mark 4 evaluation protocol

## What 90% means
Do not claim 90% caption accuracy from passing mechanical checks. A valid 90% target requires a pre-registered, representative, independently reviewed set of real Reel cases and their evidence. Report separate mechanical screening, editorial quality, factual fidelity, and advertising-review scores.

## Test collection
Gather 20 or more diverse real Reels (listing tours, educational, market, humorous, personal, artistic), with verified transcripts, visible text, approved listing data, relevant jurisdiction, and reference captions. Keep 20% as unseen holdout cases. Do not tune the prompt on the holdout.

## Human review per case
Two reviewers independently score each dimension 0–4: (1) factual fidelity, (2) specificity to actual Reel, (3) Rachel & Ron brand voice, (4) useful hook and clarity, (5) appropriate CTA, (6) advertising/fair-housing risk handling. Record disagreements and reconcile. A material fabricated property fact or protected-class steering claim is a critical failure regardless of average score.

## Reporting
Show baseline Mark 2/3 and candidate Mark 4 results on identical evidence and model settings. Report sample size, per-dimension scores, critical failures, reviewer agreement, and holdout results. A 90% aggregate editorial rubric score is not 90% real-world correctness or legal approval. Engagement uplift needs a separate publishing experiment.

## Mechanical checks
Run `python eval_suite.py cases.json` after creating a JSON list of cases with `id`, `caption`, optional `required_terms`, `forbidden_claims`, `approved_urls`, and character/hashtag/emoji limits. These checks cannot determine whether claims are true. Do not optimize solely for this score.

## Current status
The repository has no real Reel evaluation dataset or model-generated candidate captions yet. No validated accuracy percentage can be reported.
