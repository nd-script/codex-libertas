# -*- coding: utf-8 -*-
"""Represents the holographic statue & its passive effects."""
from dataclasses import dataclass
from ..core.utils import console, log_event

@dataclass
class EternalLegend:
    title: str = "Codex Libertas Ω217"
    active: bool = True

    def radiate(self):
        """Emit a faint ‘creative aura’ every call."""
        if self.active:
            console.print(f"[magenta]▣ Aura radiates[/] from «{self.title}»")
            log_event("legend:radiate")
