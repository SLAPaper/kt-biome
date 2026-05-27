## Summary

<!-- What does this PR do? 1-3 sentences. -->

## PR Type

<!-- Check all that apply. -->

- [ ] Bug fix
- [ ] Documentation
- [ ] Tests only
- [ ] Refactor / maintenance
- [ ] New creature / terrarium / module / skill
- [ ] Behavior change to an existing public package path
- [ ] Breaking change

## kt-biome Scope Check

<!-- Required for new non-bugfix content. Bug fixes can state "N/A - bug fix". -->

- Related issue/discussion:
- What paradigm, product, paper, or discussed pattern is this based on?
- Why does this belong in the official `kt-biome` package instead of a separate package or example?
- Who would use it besides the original author?

## Changes

<!-- Bullet points of what changed. -->

-

## Public Paths / Manifest Changes

<!-- List any new or changed public references and kohaku.yaml entries. -->

- `@kt-biome/creatures/...`
- `@kt-biome/terrariums/...`
- `kt_biome.plugins...`
- `kt_biome.tools...`
- `kt_biome.triggers...`
- `skills/...`

## Paradigm / Prompt / Wiring Notes

<!-- For creatures and terrariums, explain the role contract and communication pattern. -->

- Base config / inheritance:
- Channels / output wiring:
- Tools or group_* assumptions:
- Required output formats or sentinels:

## Validation

<!-- How did you verify this works? Include exact commands and manual runs. -->

```bash
cd kt-biome
python -m pytest
```

Manual checks, if any:

```bash
# Example:
kt run @kt-biome/creatures/...
kt terrarium run @kt-biome/terrariums/...
```

## Checklist

- [ ] I read `CONTRIBUTING.md`.
- [ ] I kept this PR focused and did not include unrelated changes.
- [ ] For new non-bugfix content, I linked a prior issue/discussion and the scope was discussed before implementation.
- [ ] For new non-bugfix content, I justified the reusable paradigm/product/paper/pattern behind it.
- [ ] Public package entries are added/updated in `kohaku.yaml` when needed.
- [ ] README/docs are updated when user-facing paths, behavior, or workflow changed.
- [ ] Tests were added or updated where practical.
- [ ] `python -m pytest` passes from `kt-biome`, or I explain below why it could not be run.
- [ ] I did not duplicate generated tool docs or tool-call syntax in prompts.
- [ ] I used current terrarium communication concepts (`send_channel`, `group_status`, output wiring, etc.) where applicable.

## Related Issues / Discussions

<!-- Required for new creatures, terrariums, modules, skills, or substantial behavior changes.
Examples:
- Fixes #123
- Relates to #456
- Discussed in #789
-->

## Notes for Reviewers

<!-- Optional: call out risky areas, follow-ups, tradeoffs, or places where you'd like focused review. -->

## Screenshots / Logs (if applicable)

<!-- UI output, CLI logs, channel messages, stack traces, etc. -->

## Breaking Changes (if applicable)

<!-- Describe migration steps, compatibility impact, and what downstream users need to do. -->

## Exceptions / Not Run

<!-- If you skipped any checklist item, explain exactly why. -->
