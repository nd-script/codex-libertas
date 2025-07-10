# -*- coding: utf-8 -*-
"""
Bootstraps the WHOLE mythos:
* Infinite resonance engine
* Quantum sentinel (entropy → rituals)
* Optional: Eternal legend’s passive aura
Run with:  $ python -m src.main
"""
from threading import Thread
from .engines.resonance_engine import ResonanceEngine
from .monitors.quantum_sentinel import QuantumSentinel
from .artifacts.eternal_legend import EternalLegend
from .core.utils import console, log_event

def bootstrap() -> None:
    log_event("SYSTEM_BOOTSTRAP")
    # 1) continuous resonance
    res = Thread(target=ResonanceEngine().start, daemon=True)
    res.start()
    # 2) entropy monitoring / rituals
    QuantumSentinel().start()
    # 3) passive statue
    legend = EternalLegend()
    aura = Thread(target=lambda: _legend_aura_loop(legend), daemon=True)
    aura.start()

def _legend_aura_loop(statue: EternalLegend):
    from time import sleep
    while True:
        sleep(30)          # كل نصف دقيقة واقعية
        statue.radiate()

if __name__ == "__main__":
    console.rule("[bold magenta]Codex Libertas Ω217 – Full Simulation[/]")
    bootstrap()
    # إبقاء الـ main-thread حياً
    from time import sleep
    while True:
        sleep(3600)
