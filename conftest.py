from typing import Dict

import pytest

from loggy.loggy import LogFormatter


class CustomLogFormatter(LogFormatter):
    """Adds a custom color to a level as an example."""

    def __init__(self, *args, color_dict: Dict = None, **kwargs) -> None:
        super().__init__()
        if color_dict:
            self.COLORS.update(color_dict)


