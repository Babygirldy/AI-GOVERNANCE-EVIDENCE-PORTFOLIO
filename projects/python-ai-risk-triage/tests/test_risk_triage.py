"""Small reproducible test suite for the illustrative risk triage utility."""
import tempfile
import unittest
from pathlib import Path
from risk_triage import assess, band, load_csv, write_outputs

BASE = {
    "risk_id": "T-01", "system": "Test System", "risk_event": "Test risk",
    "likelihood": "3", "impact": "5", "owner": "Test Owner",
    "control": "Test Control", "evidence_status": "missing",
}

class RiskToolTests(unittest.TestCase):
    def test_band_boundaries(self):
        self.assertEqual([band(i) for i in (7, 8, 14, 15)],
                         ["Low", "Medium", "Medium", "High"])

    def test_scores_and_does_not_claim_approval(self):
        row = assess([BASE])[0]
        self.assertEqual(row["inherent_score"], "15")
        self.assertEqual(row["inherent_band"], "High")
        self.assertEqual(row["residual_risk"], "NOT ASSESSED")
        self.assertEqual(row["approval_status"], "NOT ASSESSED")

    def test_rejects_invalid_likelihood(self):
        with self.assertRaisesRegex(ValueError, "between 1 and 5"):
            assess([{**BASE, "likelihood": "6"}])

    def test_rejects_duplicate_risk_id(self):
        with self.assertRaisesRegex(ValueError, "duplicates risk_id"):
            assess([BASE, BASE])

    def test_rejects_unverified_evidence_label(self):
        with self.assertRaisesRegex(ValueError, "invalid evidence_status"):
            assess([{**BASE, "evidence_status": "approved"}])

    def test_csv_and_report(self):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / "risk.csv"
            file.write_text(
                "risk_id,system,risk_event,likelihood,impact,owner,control,evidence_status\n"
                "T-01,Test System,Test risk,3,5,Test Owner,Test Control,missing\n",
                encoding="utf-8",
            )
            rows = load_csv(file)
            write_outputs(rows, Path(temp) / "out", on_date="2026-11-10")
            summary = (Path(temp) / "out" / "summary.md").read_text()
            self.assertIn("High: 1", summary)
            self.assertIn("Entries without verified evidence: 1", summary)
            self.assertIn("Not an assurance opinion", summary)

if __name__ == "__main__":
    unittest.main()
