from logging import Logger

import pytest

from loggy import loggy


def test_log_initiates():
    log = loggy.get_loggy()

    assert type(log) == Logger

def test_log_formatter():

    log = loggy.LogFormatter(loggy.LOG_FORMAT)
    print(log.__dict__)

    assert 0 == 1

