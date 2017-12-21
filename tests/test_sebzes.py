import pytest
from magus_kalkulator.sebzes import calculate_damage


test_data_calculate = [
    (7, 13, True, (6, 12)),
    (3, 21, False, (3, 18))
]


@pytest.mark.parametrize('sfe,damage,tulutes,expected', test_data_calculate)
def test_calculate_damage(sfe, damage, tulutes, expected):
    result = calculate_damage(sfe, damage, tulutes=tulutes)
    assert result == expected