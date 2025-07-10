# -*- coding: utf-8 -*-
"""Inject inspiration when entropy is dangerously high."""
from ..core.utils import console, log_event

class GhostTouches:
    @staticmethod
    def inspire(entropy: float):
        console.print(f"[bright_magenta]✨ Ghost-Touch[/] «أسمعني عندما تلمس الفرشاة الهاوية» (entropy={entropy:.3%})")
        log_event(f"ghost_touch|entropy={entropy}")
