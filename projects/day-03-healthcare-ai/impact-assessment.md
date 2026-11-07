# SepsisWatch AI — AI impact assessment and board recommendation

**Assessment date:** 7 November 2026  
**Scope:** Fictional adult inpatient sepsis-alert tool proposed for Safe Lives Hospital, England.  
**Status:** **Guided preliminary AI impact assessment, not a completed DPIA, clinical safety case, regulatory clearance or learner-authored independent opinion.**  
**Decision point:** Whether to allow live clinical use.

## 1. Purpose and necessity

**Proposed benefit:** Earlier escalation of patients who may be deteriorating, potentially supporting faster clinical review. A claimed clinical benefit has **not been verified**.

**Problem to validate:** Which existing triage, observation and sepsis pathways fail to identify deterioration quickly enough? What evidence shows that AI would improve patient outcomes **over** these existing pathways?

**Proportionality and alternatives:** Compare (a) usual observations and clinical escalation, (b) rule-based early warning scores, (c) supervised silent-mode AI evaluation, and (d) live AI alerts. Prefer the least risky option that can achieve the measured clinical benefit. Do not deploy solely on vendor marketing claims.

## 2. Stakeholders and effects

| Group | Potential benefit | Potential negative impact |
|---|---|---|
| Patients | Prompt recognition and assessment | Missed case, unnecessary testing, privacy intrusion, unequal performance |
| Clinicians | Decision support and prioritisation | Alarm fatigue, automation bias, unclear accountability |
| Clinical safety team | Systematic safety evaluation | Unmanaged incident response if roles are undefined |
| Hospital operations | More consistent escalation | Hidden integration cost and workflow disruption |
| Privacy/security teams | Opportunity to structure controls | New supplier access, breaches and retention risk |

## 3. Critical impact domains

| Impact | Evidence we would need before live deployment | Provisional status |
|---|---|---|
| Patient safety | Clinical validation, error trade-offs, safety case, human-factors testing, rollback | **Missing in scenario** |
| Equality and performance | Subgroup analysis, representative local validation, accessibility and harm assessment | **Missing** |
| Privacy and lawful processing | Article 6 basis and Article 9 condition, data map, transparency, DPIA where required | **Missing** |
| Human accountability | Named clinical owner; real authority to override alerts; documented escalation | **Unverified** |
| Medical-device requirements | Supplier intended purpose, classification rationale, conformity/registration documentation as applicable | **Unknown** |
| Cybersecurity | Supplier security assessment, access control, logging, incident procedures | **Missing** |
| Monitoring and post-market change | Drift, outcomes, incident, version and change-control programme | **Missing** |

## 4. Legal and standards screening — questions, not pre-judged conclusions

1. **MHRA medical-device scope:** Does the actual intended purpose and clinical function make the software a medical device? Request supplier classification rationale and applicable conformity evidence. 'Decision support' is not a blanket exemption.
2. **UK GDPR and DPA 2018:** Patient data include health information, usually special-category data. Determine a UK GDPR Article 6 lawful basis and **separate** Article 9 condition; identify the controller and processor relationships, notices, processing records, sharing and transfer conditions.
3. **DPIA:** Hospital should formally assess whether processing is likely high risk; large-scale sensitive health-data processing and consequential AI use make a DPIA strongly relevant, to be done before such processing when required. This document is **not** that DPIA.
4. **NHS clinical risk standards:** Review requirements for supplier DCB0129 and deploying health organisation DCB0160. Obtain safety case and hazard log; verify applicability and any updated requirements.
5. **NICE evidence standards:** Assess the strength of clinical effectiveness, safety, professional oversight, evidence quality and impact on care pathways. A model's test accuracy alone need not show clinical benefit.
6. **EU AI Act:** Do not automatically apply EU rules to a wholly UK use case. Reassess only where the actual product, market or activities fall within the Act's territorial and material scope.

## 5. Evaluation criteria before an authorised decision

The proposed clinical sponsor should demonstrate:
- a clear intended use, intended patient population and accountable clinical users;
- a defensible comparator and clinical benefit assessment;
- independent patient safety/human-factors and data quality analysis;
- representative test results, including subgroup limits;
- a documented, effective clinician escalation and override process;
- applicable clinical/medical-device and privacy compliance evidence;
- a monitoring, incident and model-update plan with assigned owners;
- a board/governance decision record stating remaining risks and rationale.

## 6. Draft board recommendation

> **HOLD live clinical deployment.** On the evidence currently stipulated by this fictional scenario, the Board cannot demonstrate adequate assurance of patient safety, clinical value, data protection, integration reliability, subgroup performance or accountable oversight. Commission a governed assurance phase, request the evidence above and appoint named clinical, privacy, technical and risk owners. Consider separate approval of a simulation or silent-mode assessment only after evaluating that activity's own safeguards. Return for formal review with measured results, documented residual risks and an accountable clinical safety recommendation.

**Authority boundary:** An AI Governance Analyst recommends; the proper organisational and clinical decision makers approve or reject. This is not a clinical opinion or legal determination.

## 7. What remains for the learner
- Independently review at least **two official sources** and date the review.
- Explain how a false negative might cause harm and how it should be monitored.
- Identify one lower-risk alternative and its trade-offs.
- Write your own 150-word board recommendation, referencing two risk IDs.
- Distinguish this AIA from a data protection impact assessment (DPIA).

Official source links: [sources.md](sources.md).
