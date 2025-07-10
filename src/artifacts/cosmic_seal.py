# -*- coding: utf-8 -*-
"""Final seal that can ‘lock’ or ‘unlock’ the entire simulation."""
from dataclasses import dataclass
from ..core.utils import console, log_event

@dataclass
class CosmicSeal:
    design: str = "OMEGA_217_ETERNITY_SEAL"
    locked: bool = False

    def impress(self):
        console.print(f"[cyan]𓋹 CosmicSeal[/] impressed ⇒ {self.design}")
        self.locked = True
        log_event(f"seal:{self.design}|locked")

    def break_open(self):
        console.print(f"[yellow]⚠️ CosmicSeal broken![/]")
        self.locked = False
        log_event("seal:broken")
