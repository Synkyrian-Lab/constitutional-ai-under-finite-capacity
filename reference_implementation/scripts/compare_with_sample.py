#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json
import sys

EXPECTED = ["manifest.json", "actions.jsonl", "certificate.json", "checksums.sha256", "README.md"]

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def count_jsonl(path: Path) -> int:
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())

def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: compare_with_sample.py <generated_pack> <sample_pack>")
        return 2
    gen = Path(sys.argv[1])
    sample = Path(sys.argv[2])

    if not gen.exists() or not sample.exists():
        print("ERROR: one or both directories do not exist")
        return 2

    print("Comparing generated pack to sample pack")
    print(f"- generated: {gen}")
    print(f"- sample:    {sample}")

    missing_gen = [name for name in EXPECTED if not (gen / name).exists()]
    missing_sample = [name for name in EXPECTED if not (sample / name).exists()]
    if missing_gen:
        print(f"ERROR: generated pack missing files: {', '.join(missing_gen)}")
        return 1
    if missing_sample:
        print(f"ERROR: sample pack missing files: {', '.join(missing_sample)}")
        return 1

    gen_manifest = load_json(gen / "manifest.json")
    sample_manifest = load_json(sample / "manifest.json")
    gen_cert = load_json(gen / "certificate.json")
    sample_cert = load_json(sample / "certificate.json")
    gen_actions = count_jsonl(gen / "actions.jsonl")
    sample_actions = count_jsonl(sample / "actions.jsonl")

    print("\nStructural comparison")
    print(f"- required files present: yes")
    print(f"- generated action rows: {gen_actions}")
    print(f"- sample action rows:    {sample_actions}")
    print(f"- generated manifest keys: {len(gen_manifest.keys())}")
    print(f"- sample manifest keys:    {len(sample_manifest.keys())}")
    print(f"- generated certificate type: {gen_cert.get('certificate_type')}")
    print(f"- sample certificate type:    {sample_cert.get('certificate_type')}")

    print("\nInterpretation")
    print("- The generated pack need not be byte-identical to the sample pack.")
    print("- The point of comparison is structural reproducibility: same artefact family, same reviewable shape, valid package semantics.")
    print("- Timestamp, run_label, and action content may differ while remaining valid.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
