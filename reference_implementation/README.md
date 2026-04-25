# Constitutional AI Reference Implementation (External-Safe)

This repository is an **external-safe reference implementation surface** for Constitutional AI under finite capacity.

It is **not** the full TER runtime and does **not** disclose proprietary, research-sensitive, or controller-internal logic.  
Its purpose is narrower:

- to show how a constitutional AI system can emit **explicit boundary acts**
- to show how it can preserve a **minimum witness-bearing evidence surface**
- to show how that surface can be **validated**
- to do so in a form that is **portable**, **public-safe**, and **not tied to one private codebase**

## What this repository contains

- `schemas/` — JSON Schemas for minimal constitutional artefacts
- `examples/minimal_run/` — a sample evidence pack
- `minimal_runtime/` — a tiny demonstrator that generates a public-safe example pack
- `validator/` — a small validator for package shape and integrity
- `docs/` — package map and usage notes

## What this repository does not contain

- the full TER Field-Lab runtime
- hidden thresholds or proprietary controller logic
- morphogenetic controller internals
- full field-lab escalation logic
- research-sensitive orchestration or private deployment code

## Constitutional mapping

This repository is designed to accompany the following conceptual objects:

1. **The Finite-Capacity AI Constitution**
2. **Constitutional Force and Applicability in the Finite-Capacity AI Constitution**
3. **Minimal Application Profile for Constitutional AI in AI Assistant Systems**
4. **Minimal Reviewable Evidence Specification for Constitutional AI**
5. **Questions, Limits, and Misreadings for Constitutional AI under Finite Capacity**

The repository does not replace those documents. It only demonstrates how their **minimum reviewable artefact layer** may be generated in a public-safe way.

## Minimal workflow

1. Generate an example pack
2. Inspect `manifest.json`, `actions.jsonl`, `certificate.json`
3. Verify `checksums.sha256`
4. Run the validator
5. Confirm that the package is structurally reviewable

## External-safe framing

This is a **reference implementation family**, not a mandated codebase.

Different systems may satisfy the same constitutional structure using different internal architectures, provided they preserve the relevant structural conditions:
- admissibility before execution
- explicit boundary acts
- witness
- reviewability
- declared scope
- evidence integrity

## Minimal reproducibility path

A minimal public-safe reproducibility path is included:

1. run `scripts/run_minimal_repro.sh`
2. generate a fresh example pack under `minimal_runtime/generated_pack/`
3. validate the pack shape and integrity
4. compare the generated pack structurally against `examples/minimal_run/`

This path demonstrates reproducibility of the **artefact family** and review surface, not identity with a private runtime.
