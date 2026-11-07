# SepsisWatch AI — evidence request register and NIST AI RMF mapping

**Created:** 7 November 2026  
**Status:** Assistant-provided fictional training checklist; none of the requested evidence has been supplied or validated.

## Evidence request register

| Request ID | Artifact / question | Requested from (role) | Why it matters | Status |
|---|---|---|---|---|
| E-01 | Intended-purpose statement and scope, contraindications, clinical claims | Supplier + Clinical Sponsor | Fixes system boundary and medical-device screening | Missing |
| E-02 | Local clinical validation protocol and results, including sensitivity and specificity | Supplier + Clinical Validation Lead | Tests patient safety and claimed benefit | Missing |
| E-03 | Subgroup testing, data provenance and limitations | Supplier + Equality / Model Risk | Evaluates disparate effects and representativeness | Missing |
| E-04 | Clinical safety case, hazard log, DCB0129/0160 materials | Supplier + Clinical Safety Officer | Establishes clinical safety process | Missing |
| E-05 | Data-flow diagram, lawful-basis and Article 9 review, DPIA | DPO + Data Governance | Investigates privacy law and patient impact | Missing |
| E-06 | Security assessment, access design, contract and subprocessors | Information Security + Procurement | Tests confidentiality, integrity and vendor risk | Missing |
| E-07 | Human oversight SOP, training and interface/usability testing | Ward Clinical Lead | Tests effective intervention and automation bias | Missing |
| E-08 | Model update, drift monitoring, incident response and rollback | AI System Owner | Tests continuous control after launch | Missing |
| E-09 | Board/governance approval and residual risk acceptance | Governance Committee | Tests whether decision authority has exercised review | Missing |

**Important:** The 'Missing' label means **not provided within our fictional teaching case**, not verified non-compliance of any real organisation.

## NIST AI RMF mapping (illustrative)

| Function | Application to this case | Example evidence |
|---|---|---|
| GOVERN | Set policy, risk appetite, accountability and role of Clinical Safety Officer | Governance charter, RACI, decision minutes |
| MAP | Define clinical purpose, stakeholders, data flows, operating context and harms | AI inventory, workflow map, impact assessment |
| MEASURE | Evaluate sensitivity, subgroup performance, alert fatigue, integration safety and control design | Test reports, safety case, fairness/monitoring metrics |
| MANAGE | Require corrections, restrict use, assign remediation, monitor and suspend/rollback when necessary | Mitigation log, change approvals, incident response and monitoring |

**Crosswalk limitation:** This is a high-level teaching illustration, not a line-by-line NIST subcategory or ISO/IEC 42001 audit. Exact mapping and evidence evaluation remain future work.

## 30-minute interview rehearsal
**Question:** 'The clinical vendor insists the AI is 95% accurate. Would you approve it for sepsis detection?'

**Suggested reasoning sequence:** (1) Define what accuracy means and patient population; (2) test false-negative and false-positive effects; (3) review clinical safety, regulatory and data-protection evidence; (4) examine clinician oversight and integration; (5) request a supervised evaluation and board decision; (6) document HOLD if material gaps persist.

## Learner output to add later
A dated `learner-review-YYYY-MM-DD.md` with your own reasoning, source checks, and any corrected assumptions. Do not create this entry as completed unless you actually perform it.
