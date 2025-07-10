# -*- coding: utf-8 -*-
"""Infinite creative-energy generator."""
from dataclasses import dataclass
from typing import Generator, Iterable
from ..core.config import CREATIVE_UNITS_PER_PULSE
from ..core.utils import log_event

@dataclass
class EnergyPacket:
    units: float = CREATIVE_UNITS_PER_PULSE

class EternalEngine:
    """Stream `EnergyPacket`s forever."""

    def stream(self) -> Iterable[EnergyPacket]:
        log_event("[green]EternalEngine[/] started.")
        while True:
            yield EnergyPacket()
