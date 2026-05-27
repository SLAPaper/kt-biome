# Contributing to kt-biome

Thank you for wanting to improve `kt-biome`.

`kt-biome` is the official batteries-included package for KohakuTerrarium. It is both a practical starter pack and a reference implementation for important agent-building paradigms. Because many users inherit from it directly, we keep the package focused, stable, and representative of patterns that are broadly useful.

This means contribution rules are a little stricter than for an examples repository: bug fixes are welcome as normal pull requests, but new creatures, terrariums, tools, plugins, triggers, I/O modules, and skills need a short design discussion first.

## What belongs in kt-biome

`kt-biome` is mainly for **important paradigm implementations**, not every specific feature request.

Good candidates are one of:

1. **A known popular paradigm**
   - Examples: SWE agent, reviewer loop, planner/researcher/synthesizer pipeline, driver/navigator pair, safety checkpointing, prompt-injection scanning.
   - The contribution should explain what existing product, common agent workflow, or widely used pattern it is derived from.

2. **A concrete implementation of an agent paper or well-known technique**
   - Reference the paper, blog post, benchmark, or technique.
   - Explain which part is implemented and which parts are intentionally omitted.

3. **A new pattern already discussed with maintainers**
   - Open an issue or forum discussion before implementation.
   - The discussion should converge on scope, API/config shape, maintenance burden, and why it belongs in the official biome rather than a separate package.

4. **A reusable cross-cutting module**
   - Plugins, tools, triggers, and skills are welcome when they support many downstream creatures or terrariums.
   - They should not encode one project’s private workflow unless that workflow is also a reusable paradigm.

Usually **not** good candidates:

- a creature for one small personal task
- a terrarium that only fits one private project
- a wrapper around a single niche service without broader design value
- a tiny prompt tweak that only helps one model/provider/task
- experimental agent ideas with no explanation of the pattern they represent

Those are still valuable, but they usually belong in your own package, an example, or an issue discussion first.

## Before opening a PR

### Bug fixes

Bug fixes may be opened directly as pull requests.

A good bug-fix PR includes:

- the observed behavior
- the expected behavior
- a focused fix
- a regression test when practical

### New features, modules, creatures, terrariums, and skills

Please discuss first in a GitHub issue or project forum before spending time on implementation.

This protects both sides:

- contributors do not waste time building something unlikely to be accepted
- maintainers do not need to reject large finished PRs because the scope does not fit the official package

Your proposal should answer:

- What paradigm, product, paper, or discussed pattern is this derived from?
- Who would use it besides the original author?
- Why should it live in `kt-biome` instead of a separate package?
- What new public config paths will it add? (`@kt-biome/creatures/...`, `@kt-biome/terrariums/...`, etc.)
- What framework features does it demonstrate?
- What maintenance burden does it create?
- What tests or examples will prove it works?

Do not treat “it is useful to me” as enough justification for inclusion in `kt-biome`. The bar is “this teaches or implements a reusable agent-system pattern.”

## Paradigm conventions

When adding or changing official biome content, keep these conventions in mind.

### Prefer inheritance over copying

New creatures should normally inherit from an existing base such as:

```yaml
base_config: "@kt-biome/creatures/general"
```

or:

```yaml
base_config: "@kt-biome/creatures/swe"
```

Only override the parts that define the new paradigm. Avoid copying large tool lists or prompt blocks from existing creatures.

### Keep controller prompts orchestration-focused

Creature prompts should teach the controller how to decide, dispatch, and coordinate. Long user-facing work should usually be delegated to tools, sub-agents, output wiring, or downstream creatures.

Avoid bloating `system.md` with:

- tool lists
- tool-call syntax
- full tool documentation

The framework generates tool listings and provides detailed docs through `##info <tool_name>##`.

### Separate vertical and horizontal composition

KohakuTerrarium has two composition levels:

- **Vertical:** inside one creature, using tools and sub-agents
- **Horizontal:** across creatures in a terrarium, using channels and output wiring

Do not blur these concepts in prompts or config. A terrarium should describe peer-to-peer coordination; a creature should not assume too much about the graph unless the terrarium prompt/config gives it that role.

### Use current terrarium primitives

For terrarium graph communication, prefer current group/channel concepts:

- `send_channel` for channel broadcasts
- `group_send` for direct creature delivery when available
- `group_status` for privileged graph snapshots
- output wiring for deterministic turn-end handoff

Do not introduce new recipes that rely on deprecated `terrarium_*` tooling or old queue/broadcast assumptions. Graph channels are broadcast at the engine layer; document routing expectations accordingly.

### Make prompts specific, not huge

Prompts should encode the role contract and important failure modes. They should not become manuals for the whole framework.

A good official prompt:

- states the creature’s job clearly
- explains when to act and when to stay idle
- explains how to communicate with peers
- names important sentinels or output formats if needed
- avoids unnecessary repetition of framework docs

### Prefer reusable modules over hard-coded workflows

For plugins/tools/triggers/I/O, design the module so downstream packages can reuse it with options. Avoid baking one terrarium’s assumptions into Python code unless the module exists only to support that terrarium and the coupling is documented.

## Repository layout

```text
kt-biome/
  creatures/      reusable creature configs
  terrariums/     reusable terrarium configs
  prompts/        shared prompt fragments
  skills/         packaged SKILL.md bundles
  kt_biome/       Python package for plugins, tools, triggers, I/O, and libs
  tests/          unit tests for packaged modules/config behavior
  kohaku.yaml     package manifest
```

If you add a public creature, terrarium, plugin, tool, trigger, I/O module, or skill, update `kohaku.yaml` and the README when appropriate.

## Development setup

From a checkout of the main KohakuTerrarium repository with `kt-biome` present:

```bash
cd kt-biome
uv pip install -e ".[dev]"
```

You may also need an editable install of KohakuTerrarium itself, depending on your environment:

```bash
cd ..
uv pip install -e ".[dev]"
```

## Tests

Run the kt-biome unit tests from the `kt-biome` directory:

```bash
cd kt-biome
python -m pytest
```

Add or update tests for behavior changes whenever practical.

Suggested coverage expectations:

- plugin/tool/trigger code: unit tests for normal path and failure path
- config-only creatures/terrariums: tests or manifest checks when the config is non-trivial
- skills: tests that the bundle is discoverable and contains required procedural content
- prompt changes: tests only when the prompt contains a contract that code depends on

If tests cannot run in your environment, say so in the PR and include the error output.

## Style guidelines

### Python

- Target the Python version declared in `pyproject.toml`.
- Use modern type hints: `list`, `dict`, `X | None` rather than `List`, `Dict`, `Optional`.
- Keep imports at module top unless the dependency is optional or intentionally lazy.
- Avoid `print()` in library code; use logging where output is needed.
- Keep modules small and focused.

### YAML/config

- Prefer minimal overrides from a base config.
- Use package references such as `@kt-biome/creatures/general` rather than relative assumptions when defining public recipes.
- Keep names stable once released; users may depend on `@kt-biome/...` paths.
- Include short descriptions for public modules in `kohaku.yaml`.

### Prompts

- Keep prompts readable and role-specific.
- Do not duplicate tool documentation.
- Make communication expectations explicit for terrarium participants.
- Document any required output format or sentinel strings.

### Skills

A packaged skill should be broadly reusable and procedural. It should answer “how to do this repeatable task well,” not just encode a one-off preference.

## Pull request checklist

Before requesting review, check:

- [ ] For new non-bugfix content, an issue/forum discussion exists and is linked.
- [ ] The PR explains the paradigm, product, paper, or pattern behind the change.
- [ ] Public package entries are added/updated in `kohaku.yaml`.
- [ ] README/docs are updated when user-facing paths or behavior change.
- [ ] Tests were added/updated where practical.
- [ ] `python -m pytest` was run from `kt-biome`, or the PR explains why it could not be run.
- [ ] The change does not add narrow project-specific behavior to the official package.

## Commit messages

Use clear, reviewable commits. Conventional Commit-style subjects are preferred:

```text
feat(creatures): add <paradigm> creature
fix(plugins): handle missing checkpoint repo
refactor(terrariums): simplify research pipeline wiring
docs: explain contribution bar for new paradigms
```

Keep unrelated changes in separate commits.

## Maintainer review criteria

Maintainers may ask for a contribution to move to a separate package or example even if the implementation is correct. This is not a judgment of usefulness; it is how `kt-biome` stays coherent as the official package.

Review focuses on:

- paradigm fit
- reuse value
- prompt/config clarity
- compatibility with current KohakuTerrarium architecture
- maintenance cost
- tests and documentation

Thank you for helping keep `kt-biome` useful as both a starter ecosystem and a reference for strong agent-system patterns.
