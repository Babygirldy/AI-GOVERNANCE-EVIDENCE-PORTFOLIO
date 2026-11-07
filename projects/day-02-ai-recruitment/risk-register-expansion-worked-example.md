# Day 02 — R-04 to R-07: guided risk-register expansion

**Prepared:** 7 November 2026  
**Status:** **Assistant-authored worked example — not learner-completed or vendor-verified.**  
**Scenario:** Fictional Northstar Talent UK using HireSort AI for candidate ranking.  
**Source workbook:** [Preserved original](Day_2_AI_Governance_Career_Lab.xlsx). Its R-04–R-07 entries remain blank; this document deliberately does **not** misrepresent them as learner submissions.

## Scoring method

Illustrative **inherent** likelihood (L) and impact (I) scored 1–5; score = L × I. Original workbook bands: low 1–7, medium 8–14, high 15–25. Numbers are teaching assumptions, **not measured frequencies or independent assurance results**. Residual risk must not be scored until control effectiveness is evidenced.

| ID | Category | Proposed risk event and consequence | L | I | Inherent score | Band | Proposed accountable owner |
|---|---|---|---:|---:|---:|---|---|
| R-04 | Performance and validity | Rankings may incorrectly deprioritise qualified applicants because training or validation data do not represent the current jobs, potentially excluding strong candidates. | 3 | 4 | 12 | Medium | Recruitment Analytics Lead |
| R-05 | Transparency and contestability | Applicants may not understand the use or effect of AI ranking, and lack an effective way to correct data or challenge consequential outcomes. | 4 | 4 | 16 | High | Head of Talent Acquisition + DPO |
| R-06 | Supplier security and confidentiality | Inadequate supplier controls or access management could expose CVs, sensitive inferences and contact details, causing privacy, reputational or regulatory harm. | 3 | 5 | 15 | High | Information Security + Procurement |
| R-07 | Model change and monitoring | An unreviewed vendor update or change in the applicant population could deteriorate performance or fairness after deployment without detection. | 3 | 4 | 12 | Medium | AI System Owner + Model Risk Lead |

## Control and evidence plan

### R-04 — Performance and validity
- **Proposed controls:** Validate on representative job families and applicant groups; define false-negative and selection-rate measures; test input-data quality; require independent review of low-ranked candidates.
- **Ask supplier for:** Model evaluation protocol; dataset provenance; performance by job family and relevant subgroups; error analysis and limitations.
- **Evidence status:** **Missing in fictional case**; do not claim that tests have passed.
- **How to reason about the score:** Likelihood 3 is a hypothetical midpoint because the training source is historical; impact 4 reflects potentially serious employment consequences. Revisit both after receiving data.

### R-05 — Transparency and contestability
- **Proposed controls:** Clear applicant privacy information; understandable explanation of where ranking is used; correction/review channels; recruiters able to reconsider independent evidence and record outcomes.
- **Ask for:** Candidate notice; workflow diagram; challenge and escalation procedure; complaint logs (if available).
- **Evidence status:** **Missing in fictional case**.
- **Legal nuance:** Assess how UK GDPR and other protections apply to the actual **degree of automation and significance of decisions**; do not assume all ranking is solely automated or all human involvement is meaningful.

### R-06 — Supplier security and confidentiality
- **Proposed controls:** Data-processing agreement where applicable; role-based access; encryption in transit/at rest; retention and deletion schedule; breach-response responsibilities; supplier security review.
- **Ask for:** Data-flow map; security review, penetration-test summary; subprocessor list; contractual protections; transfer assessment where relevant.
- **Evidence status:** **Missing in fictional case**.

### R-07 — Model change and monitoring
- **Proposed controls:** Version control and pre-release approval; quarterly or risk-triggered subgroup retesting; complaint and override analysis; rollback capability; documented monitoring thresholds.
- **Ask for:** Change log, model update policy, drift metrics, monitoring reports, incident escalation plan.
- **Evidence status:** **Missing in fictional case**.

## Suggested professional judgement

> Given the assumed material uncertainty around fairness, performance, transparency and supplier safeguards, I recommend **HOLD — no live deployment** until the organisation has obtained and reviewed the requested evidence, completed applicable assessments, assigned accountable owners and set proportionate monitoring thresholds. This is a recommendation from a fictional assessment; the final go/no-go authority belongs to authorised decision makers.

## Guided learner actions
1. Open the original Excel workbook and locate sheet `03 Risk Register`.
2. Read one row here (start with R-04), then explain in **your own words** why the risk matters to candidates and what evidence would make you reconsider the risk.
3. Enter and edit that row in a **new version** of the workbook, not the preserved original. Mark any hypothetical values as illustrative.
4. Repeat for R-05–R-07. Record the change date and what you learned in the learning log.
5. Link the revised workbook here only after personally reviewing your entries; never mark this worked example as verified completed work.

## Primary starting references
- UK government, Responsible AI in Recruitment: https://www.gov.uk/government/publications/responsible-ai-in-recruitment-guide/responsible-ai-in-recruitment
- ICO, Guidance on AI and data protection: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
- NIST AI RMF Playbook: https://airc.nist.gov/airmf-resources/playbook/

**Important:** Recheck exact current law and commencement dates when writing the independent legal assessment.
