# hdhi-ui

This folder is where the Lovable-generated frontend project goes — wholesale,
as its own self-contained Vite/React project (its own `package.json`,
`src/`, etc. sitting directly inside this folder).

## How to fill this in

1. Run the prompt in `../../../docs/LOVABLE_FOUNDATION_PROMPT.md` in Lovable.
2. Export/download the generated project.
3. Copy its contents into this folder, replacing this README (or keeping it
   alongside — your call).
4. Commit as a normal part of this repo. Don't keep it as a separate git
   remote/submodule — it's a subfolder of this repo like any other.

Nothing else in this repo depends on this folder existing yet except the
Tracker's Phase 4+ goals, which assume this UI is in place before wiring
real data into it.
