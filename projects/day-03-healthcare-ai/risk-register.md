# SepsisWatch AI — illustrative risk register

**Date:** 7 November 2026. **Status: worked draft; no real-world testing or verification.**

**Risk scale:** likelihood (L) and impact (I), each 1–5; inherent score = L × I. Suggested teaching bands: low 1–7, medium 8–14, high 15–25. Do **not** treat these numbers as measured clinical risk. Residual risk = **not assessed**, because control effectiveness is unverified.

| ID | Risk event / potential harm | L | I | Score | Proposed owner | Evidence required |
|---|---|---:|---:|---:|---|---|
| H-01 | False negative: patient with possible sepsis receives no alert; clinical review is delayed, potentially worsening injury. | 3 | 5 | 15 | Clinical Safety Officer + Clinical Lead | Sensitivity/false-negative validation in relevant wards; missed-case review; hazard log |
| H-02 | False positive: excessive alerts cause alarm fatigue, unnecessary tests and diversion of staff attention. | 4 | 4 | 16 | Ward Clinical Lead | Precision/false-alarm analysis, workload study, user testing |
| H-03 | Performance variation: some age groups, disability-related presentations or other clinically relevant groups experience poorer model performance. | 3 | 5 | 15 | Model Validation Lead + Equality Lead | Stratified subgroup performance, sample sizes and fairness review |
| H-04 | Privacy breach: patient health information leaks through access, supplier processing or insecure data flow. | 3 | 5 | 15 | DPO + Information Security Lead | DPIA, data-flow map, access review, contracts, security assessment |
| H-05 | Automation bias: clinicians over-rely on AI recommendations and discount contradictory clinical signs. | 4 | 5 | 20 | Medical Director + Education Lead | Human-oversight SOP, training, simulation and override/incident logs |
| H-06 | Integration failure: stale observations, wrong-patient mapping, clock errors or missing laboratory results produce misleading alerts. | 3 | 5 | 15 | EHR Integration Lead + Clinical Safety Officer | Interface validation, timestamp checks, identity matching and fail-safe tests |
| H-07 | Model drift/update: clinical practice or population changes make performance worse after roll-out without detection. | 3 | 4 | 12 | Model Risk Lead | Model versioning, drift monitoring, change control and rollback tests |
| H-08 | Governance gap: ownership, incident escalation or approvals are unclear, delaying action when harm is suspected. | 4 | 5 | 20 | Hospital Board Sponsor + Risk Committee | RACI, clinical safety case, incident SOP, sign-off records |

## Proposed controls and how to test them

| Risk | Proposed control | Control effectiveness test (not yet done) |
|---|---|---|
| H-01 | Validate on representative local data; require conventional sepsis pathway regardless of AI alert | Independent sensitivity analysis and prospective pathway review |
| H-02 | Threshold tuning, escalation rules, alert-volume review and clinician co-design | Count alerts per ward shift; usability study and alert fatigue feedback |
| H-03 | Define and evaluate clinically meaningful subgroups and data limitations | Subgroup metrics with uncertainty intervals and mitigation review |
| H-04 | Least privilege, encryption, supplier contractual safeguards, retention/deletion and DPIA | Audit access and deletion; test supplier documentation and privacy risks |
| H-05 | Make AI advisory; clinician assessment and documented override, including escalation | Simulation of conflicting AI/clinical evidence and observed clinician response |
| H-06 | Validate interfaces; detect missing or old records; suppress unreliable alerts | Wrong-patient, time-zone and missing-data test cases |
| H-07 | Monitoring dashboard, release gate, periodic audit and rollback | Demonstrate triggered alerts, change records and successful rollback |
| H-08 | Named decision owner, change board, clinical safety officer and response playbook | Tabletop incident exercise and evidence of documented roles |

## Why likelihood and impact differ
The **likelihood** score estimates how plausible the risk event is under hypothetical conditions. **Impact** estimates severity if harm occurs. Serious clinical harms can justify high impact even without frequent occurrence. You must not infer these probability numbers from this document.

## Next analyst challenge
Choose **H-01** and **H-05**. Explain why a mandatory 'human in the loop' rule might not reduce risk unless the human has time, information, authority and training to intervene.

**Current disposition:** All risks open; residual scores and owner sign-off outstanding.
