# SepsisWatch AI — AI system inventory (guided draft)

**Date:** 7 November 2026. **Status:** Illustrative intake, not a verified third-party inventory.  
**Jurisdiction assumed:** England, UK.  
**Classification discipline:** 'Scenario fact' means provided in this fictional exercise; 'Assumption' means introduced for teaching; 'Unknown' requires evidence.

| Inventory field | Proposed entry | Evidence status / next check |
|---|---|---|
| System ID | SLH-AI-001 | Assigned for this exercise |
| System name | SepsisWatch AI | Scenario fact (fictional) |
| Business owner | Director of Clinical Operations | Proposed; formal appointment unknown |
| Clinical safety owner | Hospital Clinical Safety Officer | Proposed; appointment not evidenced |
| Privacy owner | Hospital DPO | Proposed; appointment not evidenced |
| Supplier | MedSignal Analytics Ltd | Fictional; no vendor dossier |
| Use purpose | Surface early warnings of possible sepsis/deterioration for clinician review | Assumption; signed intended purpose required |
| Users | Registered clinicians and authorised clinical teams | Assumed; roles/permissions unknown |
| Affected population | Adult general-ward inpatients; excludes paediatric and maternity pathways | Assumed; population and contraindications require definition |
| Inputs | Observations such as heart rate, temperature, respiratory rate, oxygen saturation; selected lab results and timestamps | Assumed; complete feature/data dictionary needed |
| Outputs | Risk alert or prioritisation flag presented to clinicians | Assumed; thresholds, confidence and user interface unknown |
| Automation level | Advisory only; no autonomous diagnosis or treatment | Assumed; real workflow/alert behaviour to verify |
| Data types | Identifiable patient information, including health data | Special-category data; verify privacy data flow |
| Data flow | Hospital EHR → approved interface → model inference → clinical alert → audit log | Hypothetical; diagram, retention and subprocessors missing |
| Model type | Predictive machine-learning classifier, architecture unspecified | Unknown; model card, version and validation needed |
| Deployment | Proposed pre-production pilot | Fictional; no approval |
| Training data | Unknown; no evidence of provenance or representativeness | Request datasheet and development/validation details |
| Clinical claims | Possible clinical decision support; whether marketed as medical device **not determined** | Obtain supplier intended purpose and MHRA classification/registration evidence as applicable |
| Human oversight | Clinician assesses patient and decides clinical action | SOP, training and alert acknowledgement logging missing |
| Lawful basis | Not determined | Determine and document UK GDPR Article 6 lawful basis and Article 9 condition where applicable |
| DPIA | Not undertaken in this fictional case | A high-risk privacy assessment is likely and must be formally screened; complete where required |
| Security | Not verified | Access, logging, penetration testing, resilience and vendor arrangements needed |
| Retention | Not defined | Establish purpose-based retention/deletion schedule |
| Integration safety | Not verified | Identify and assess DCB0129 supplier/ DCB0160 deployer obligations and local clinical safety case |
| Monitoring | Not established | Measure clinical outcomes, subgroup performance, drift, override/alert fatigue and incidents |
| Incident response | Not established | Create reporting and rollback process, assess MHRA reporting where applicable |

## Sample intended-purpose statement (draft for analysis, not supplier-authorised)
'An advisory software tool intended to analyse routinely collected physiological observations and laboratory results from adults admitted to general medical wards, and to flag patterns suggestive of possible sepsis or deterioration for prompt review by trained hospital clinicians. It does not replace clinical judgement, diagnose sepsis independently or trigger treatment.'

**Analyst caution:** Labelling a tool 'advisory' does not by itself settle whether it is a medical device; the actual intended purpose, claims and function matter.

## First independent verification question
**What clinical action follows an alert, who must acknowledge it, and what happens if an alert is missed?** This question connects the technical output to potential patient harm.

References: [sources.md](sources.md). 
