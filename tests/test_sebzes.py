import pytest
from magus_kalkulator.sebzes import calculate_damage, return_penalty


test_data_calculate = [
    (7, 13, True, (6, 12)),
    (3, 21, False, (3, 18)),
    (3, 2, False, (0, 0)),
    (3, 3, True, (0, 0))
]


@pytest.mark.parametrize('sfe,damage,tulutes,expected', test_data_calculate)
def test_calculate_damage(sfe, damage, tulutes, expected):
    result = calculate_damage(sfe, damage, tulutes=tulutes)
    assert result == expected


def test_return_penalty():
    result = return_penalty(7, 21, 14, 'Szur')
    expected_keys = ['ep_loss', 'fp_loss', 'hit_target', 'penalty']
    actual_keys = result.keys()
    assert all(x in actual_keys for x in expected_keys)

    assert result['ep_loss'] == 2
    assert result['fp_loss'] == 14

    target_parts = len(result['hit_target'])
    assert target_parts == 3

    penalty = result['penalty']

    assert isinstance(penalty, list) or penalty == 'nincs hatrany'