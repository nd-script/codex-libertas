# -*- coding: utf-8 -*-
"""Great Renaissance = universe-wide creative reboot."""
from ..core.utils import console, log_event

class GreatRenaissance:
    @staticmethod
    def launch(entropy: float):
        console.print(f"[bold red]🚀 Great Renaissance[/] INITIATED! (entropy={entropy:.3%})")
        log_event(f"renaissance|entropy={entropy}")
        # TODO: broadcast reset events / reload plugins
