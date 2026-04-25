#!/usr/bin/env python3
from pathlib import Path
import json
import hashlib
import datetime

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    out = Path("generated_pack")
    out.mkdir(exist_ok=True)
    ts = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    manifest = {
        "system_name": "constitutional-ai-reference",
        "profile_name": "ai_assistant_minimal_profile",
        "version": "0.1.0",
        "run_label": "generated_example",
        "timestamp_utc": ts,
        "package_contents": ["manifest.json", "actions.jsonl", "certificate.json", "checksums.sha256", "README.md"],
        "scope": [
            "demonstrate explicit constitutional acts",
            "demonstrate witness-bearing trace",
            "demonstrate bounded verdict surface",
            "demonstrate package integrity"
        ],
        "non_claims": [
            "not a full TER runtime",
            "not a legal compliance certification",
            "not a deployment-readiness claim"
        ],
        "integrity_method": "sha256"
    }
    actions = [{
        "event_id": 1,
        "timestamp_utc": ts,
        "action_type": "ACCEPT",
        "reason_code": "ADMISSIBLE_CONTINUATION",
        "profile_version": "ai_assistant_minimal_profile@0.1.0",
        "witness": {"summary": "Example admissible continuation."}
    }]
    certificate = {
        "certificate_type": "constitutional_minimal_example",
        "scope": ["public-safe generated example"],
        "status": "REVIEWABLE_MINIMAL_PASS",
        "qualifications": ["example-only", "minimal artefact demonstration"],
        "evidence_refs": ["manifest.json", "actions.jsonl"],
        "non_claims": ["not evidence of richer runtime semantics"]
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    with (out / "actions.jsonl").open("w", encoding="utf-8") as f:
        for row in actions:
            f.write(json.dumps(row) + "\n")
    (out / "certificate.json").write_text(json.dumps(certificate, indent=2), encoding="utf-8")
    (out / "README.md").write_text("Generated public-safe constitutional example pack.\n", encoding="utf-8")
    checksum_lines = []
    for name in ["manifest.json", "actions.jsonl", "certificate.json", "README.md"]:
        checksum_lines.append(f"{sha256_file(out / name)}  {name}")
    (out / "checksums.sha256").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    print(f"Wrote example pack to {out.resolve()}")

if __name__ == "__main__":
    main()
