"""Illustrative AI risk-register triage. No dependencies; not a compliance certifier."""
from __future__ import annotations
import argparse
import csv
from collections import Counter
from datetime import date
from pathlib import Path

REQUIRED = ("risk_id", "system", "risk_event", "likelihood", "impact",
            "owner", "control", "evidence_status")
ALLOWED_EVIDENCE = {"missing", "requested", "received_unverified", "verified"}

def band(score: int) -> str:
    """Teaching-only banding adapted to the workbook's simple 5x5 matrix."""
    if not 1 <= score <= 25:
        raise ValueError("Risk score must be between 1 and 25")
    return "Low" if score <= 7 else "Medium" if score <= 14 else "High"

def assess(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Validate rows, calculate inherent scores, preserve evidence uncertainty."""
    result: list[dict[str, str]] = []
    seen: set[str] = set()
    for number, raw in enumerate(rows, start=2):
        missing = [field for field in REQUIRED if field not in raw]
        if missing:
            raise ValueError(f"CSV missing columns: {', '.join(missing)}")
        row = {field: str(raw[field] or "").strip() for field in REQUIRED}
        if not all(row.values()):
            raise ValueError(f"Row {number} has an empty required field")
        rid = row["risk_id"]
        if rid in seen:
            raise ValueError(f"Row {number} duplicates risk_id {rid}")
        seen.add(rid)
        try:
            likelihood = int(row["likelihood"])
            impact = int(row["impact"])
        except ValueError as exc:
            raise ValueError(f"Row {number}: likelihood and impact must be integers") from exc
        if not (1 <= likelihood <= 5 and 1 <= impact <= 5):
            raise ValueError(f"Row {number}: likelihood and impact must be between 1 and 5")
        evidence = row["evidence_status"].lower()
        if evidence not in ALLOWED_EVIDENCE:
            raise ValueError(f"Row {number}: invalid evidence_status '{evidence}'")
        score = likelihood * impact
        row.update(
            likelihood=str(likelihood), impact=str(impact),
            inherent_score=str(score), inherent_band=band(score),
            evidence_status=evidence,
            approval_status="NOT ASSESSED",
            residual_risk="NOT ASSESSED",
        )
        result.append(row)
    return result

def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("Input CSV requires a header")
        absent = [key for key in REQUIRED if key not in reader.fieldnames]
        if absent:
            raise ValueError(f"Input CSV missing columns: {', '.join(absent)}")
        return assess(list(reader))

def write_outputs(records: list[dict[str, str]], output_dir: Path, *, on_date: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    headings = (*REQUIRED, "inherent_score", "inherent_band", "residual_risk", "approval_status")
    with (output_dir / "scored_risks.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headings, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    bands = Counter(record["inherent_band"] for record in records)
    unverified = sum(record["evidence_status"] != "verified" for record in records)
    systems = sorted({record["system"] for record in records})
    lines = [
        "# Illustrative AI risk triage report", "", f"Generated: {on_date}", "",
        "**Not an assurance opinion, legal conclusion, clinical safety assessment, or approval.**", "",
        f"Systems assessed (fictional): {', '.join(systems) or 'none'}", "",
        f"Risk records: {len(records)}", f"High: {bands['High']}",
        f"Medium: {bands['Medium']}", f"Low: {bands['Low']}",
        f"Entries without verified evidence: {unverified}", "",
        "## Outstanding actions", "",
        "- Review scoring assumptions with a qualified owner and relevant stakeholders.",
        "- Obtain and evaluate evidence of actual control operation.",
        "- Do not infer residual risk or approve production deployment from this tool.", "",
    ]
    for record in records:
        if record["inherent_band"] == "High" or record["evidence_status"] != "verified":
            lines.append(
                f"- **{record['risk_id']}** ({record['system']}): "
                f"{record['inherent_band']} inherent risk, evidence "
                f"{record['evidence_status']}; owner: {record['owner']}."
            )
    (output_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input fictional-risk CSV")
    parser.add_argument("--out", type=Path, default=Path("outputs"), help="Output folder")
    args = parser.parse_args()
    records = load_csv(args.input)
    write_outputs(records, args.out, on_date=date.today().isoformat())
    print(f"Processed {len(records)} risks; wrote {args.out / 'scored_risks.csv'} and summary.md")

if __name__ == "__main__":
    main()
