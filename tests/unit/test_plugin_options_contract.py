"""Regression tests for the KohakuTerrarium BasePlugin options contract."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_BIOME_ROOT = Path(__file__).resolve().parents[2]
if str(_BIOME_ROOT) not in sys.path:
    sys.path.insert(0, str(_BIOME_ROOT))

from kt_biome.plugins.checkpoint import CheckpointPlugin  # noqa: E402
from kt_biome.plugins.circuit_breaker import CircuitBreakerPlugin  # noqa: E402
from kt_biome.plugins.context_files import ContextFilesPlugin  # noqa: E402
from kt_biome.plugins.cost_tracker import CostTrackerPlugin  # noqa: E402
from kt_biome.plugins.event_logger import EventLoggerPlugin  # noqa: E402
from kt_biome.plugins.family_guidance import FamilyGuidancePlugin  # noqa: E402
from kt_biome.plugins.injection_scanner import InjectionScannerPlugin  # noqa: E402
from kt_biome.plugins.multimodal_guard import MultimodalGuardPlugin  # noqa: E402
from kt_biome.plugins.pev_verifier import PEVVerifierPlugin  # noqa: E402
from kt_biome.plugins.seamless_memory import SeamlessMemoryPlugin  # noqa: E402

PLUGIN_CASES: list[tuple[type, dict[str, Any]]] = [
    (EventLoggerPlugin, {"include_content": True, "include_args": False}),
    (MultimodalGuardPlugin, {"placeholder": "[image omitted]"}),
    (CostTrackerPlugin, {"budget_usd": 1.0, "stop_at_budget": False}),
    (CheckpointPlugin, {"backend": "disabled"}),
    (CircuitBreakerPlugin, {"default": {"max_failures": 2}}),
    (InjectionScannerPlugin, {"tools_to_scan": ["read"], "include_defaults": False}),
    (ContextFilesPlugin, {"files": ["AGENTS.md"], "reload_per_turn": False}),
    (FamilyGuidancePlugin, {"include_defaults": False}),
    (SeamlessMemoryPlugin, {"model": "test/model", "min_turns_before_active": 1}),
    (PEVVerifierPlugin, {"acceptance_criteria": ["done"], "max_rounds": 1}),
]


def test_package_plugins_expose_base_options_contract() -> None:
    for plugin_cls, options in PLUGIN_CASES:
        plugin = plugin_cls(options=options)

        assert hasattr(plugin, "options"), plugin_cls.__name__
        assert plugin.get_options() == options


def test_package_plugins_without_options_expose_empty_options() -> None:
    for plugin_cls, _options in PLUGIN_CASES:
        plugin = plugin_cls()

        assert hasattr(plugin, "options"), plugin_cls.__name__
        assert plugin.get_options() == {}
