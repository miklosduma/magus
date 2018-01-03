import pytest
from magus_kalkulator.sebzes import calculate_damage, return_penalty


test_data_calculate = [
    (7, 13, 2, True, (8, 16)),
    (3, 21, 1, False, (3, 19)),
    (3, 2, 1, False, (0, 0)),
    (3, 3, 0, True, (0, 0)),
    (0, 7, 2, False, (1, 7))
]


@pytest.mark.parametrize('sfe,damage,atutes,tulutes,expected',
                         test_data_calculate)
def test_calculate_damage(sfe, damage, atutes, tulutes, expected):
    result = calculate_damage(sfe, damage, atutes, tulutes=tulutes)
    assert result == expected


def test_return_penalty():
    result = return_penalty(7, 21, 3, 14, 'Szur')
    expected_keys = ['ep_loss', 'fp_loss', 'hit_target', 'penalty']
    actual_keys = result.keys()
    assert all(x in actual_keys for x in expected_keys)

    assert result['ep_loss'] == 3
    assert result['fp_loss'] == 17

    target_parts = len(result['hit_target'])
    assert target_parts == 3

    penalty = result['penalty']

    assert isinstance(penalty, list) or penalty == 'nincs hatrany'