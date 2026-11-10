# AI Risk Triage — Practical Python Portfolio Lab

**Built:** 10 November 2026  
**Status:** Assistant-authored, tested teaching prototype. **Not yet independently reviewed, modified or explained by the learner.**  
**Case studies:** Fictional HireSort AI recruitment and SepsisWatch AI clinical alert software.

## What it does
Uses Python's built-in CSV library to read fictional risks, validate inputs, calculate **inherent** risk scores (likelihood × impact), label a risk band, and output `scored_risks.csv` and `summary.md`. No third-party libraries, API keys or real applicant/patient data.

It deliberately **does not** assess residual risk, prove effectiveness of controls, make legal or clinical conclusions or authorise production deployments. The example scores are assumptions, not measured frequencies.

## Run on Windows or any computer with Python 3.10+
From this folder, run:

```bash
python risk_triage.py data/fictional_risks.csv --out outputs
python -m unittest discover -s tests -v
```

On Windows, you can use `py` instead of `python`.

Six automated tests check scoring thresholds, invalid values, duplicate identifiers, evidence-status integrity, reporting and the safeguard against claiming approval. They passed in the assistant's local test environment on 10 November 2026. To claim hands-on coding experience, the learner should also run and explain the script themselves.

## Files
- `risk_triage.py`: working script
- `data/fictional_risks.csv`: six fictional risks from Day 02 and Day 03
- `tests/test_risk_triage.py`: six automated tests
- `outputs/scored_risks.csv`: example machine-readable result
- `outputs/summary.md`: example risk/evidence-gap summary

## Governance considerations
A score alone cannot determine whether AI is lawful, safe, fair or deployable. Review the actual intended use, affected people, risk basis, quality of evidence, control effectiveness, owners and sign-off authority. The healthcare examples are learning scenarios, not clinical safety assessments.

**Simple next step:** Run the tool and explain why an R-04 score of 12 is not proof that a recruitment system can be deployed.
