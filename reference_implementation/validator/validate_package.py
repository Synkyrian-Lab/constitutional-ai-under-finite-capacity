#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import sys

REQUIRED = ["manifest.json", "actions.jsonl", "certificate.json", "checksums.sha256", "README.md"]

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def validate_checksums(root: Path) -> list[str]:
    errors = []
    checksum_path = root / "checksums.sha256"
    lines = checksum_path.read_text(encoding="utf-8").strip().splitlines()
    for line in lines:
        if "  " not in line:
            errors.append(f"Malformed checksum line: {line}")
            continue
        digest, filename = line.split("  ", 1)
        target = root / filename
        if not target.exists():
            errors.append(f"Missing file listed in checksum: {filename}")
            continue
        actual = sha256_file(target)
        if actual != digest:
            errors.append(f"Checksum mismatch for {filename}")
    return errors

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_package.py <package_dir>")
        return 2
    root = Path(sys.argv[1])
    if not root.exists():
        print(f"Package directory not found: {root}")
        return 2

    errors = []
    for req in REQUIRED:
        if not (root / req).exists():
            errors.append(f"Missing required file: {req}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    try:
        json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"manifest.json invalid JSON: {exc}")

    try:
        json.loads((root / "certificate.json").read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"certificate.json invalid JSON: {exc}")

    try:
        with (root / "actions.jsonl").open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    json.loads(line)
    except Exception as exc:
        errors.append(f"actions.jsonl invalid JSONL: {exc}")

    errors.extend(validate_checksums(root))

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    print("PASS: package is structurally valid and checksums match.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
