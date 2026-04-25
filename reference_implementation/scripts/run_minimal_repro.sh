#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GEN_DIR="$ROOT/minimal_runtime"
VAL_DIR="$ROOT/validator"
OUT_DIR="$GEN_DIR/generated_pack"

printf '== Generating public-safe example pack ==\n'
(
  cd "$GEN_DIR"
  python3 generate_example_pack.py
)

printf '\n== Validating generated pack ==\n'
python3 "$VAL_DIR/validate_package.py" "$OUT_DIR"

printf '\n== Comparing generated pack to sample example ==\n'
python3 "$ROOT/scripts/compare_with_sample.py" \
  "$OUT_DIR" \
  "$ROOT/examples/minimal_run"

printf '\nDone. Generated pack: %s\n' "$OUT_DIR"
