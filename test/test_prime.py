from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.wrapper import is_prime

import pytest

# テストケースと期待している結果を書く
@pytest.mark.parametrize(("number", "expected"),
    [
        (1,  False),
        (2,  True),
        (3,  True),
        (4,  False),
        (5,  True),
        (6,  False),
        (7,  True),
        (8,  False),
        (9,  False),
        (10, False),
    ]
)

def test_is_prime(number: int, expected: bool):
    assert is_prime(number) == expected