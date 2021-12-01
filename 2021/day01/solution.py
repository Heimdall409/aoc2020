#!/usr/bin/env python3

import contextlib

from pathlib import Path
from typing import List
from AoC.util import show


CWD = Path(__file__).parent


def read_input(filename: str = "input.txt") -> List[float]:
    input_file = CWD.joinpath(filename)
    with open(input_file, "r") as reader:
        return [float(l) for l in reader.readlines()]


@show
def first(l: List[float]) -> int:
    l2 = [v > l[i - 1] for i, v in enumerate(l) if i != 0]
    return sum(l2)


@show
def second(l: List[float]) -> int:
    l2 = [v + l[i+1] + l[i+2] for i, v in enumerate(l) if i < len(l)-2]
    with contextlib.redirect_stdout(None):
        return first(l2)


def test_example() -> None:
    with contextlib.redirect_stdout(None):
        example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        assert first(example) == 7
        assert second(example) == 5


test_example()
s = read_input()
first(s)  # 280
second(s)  # 1797
