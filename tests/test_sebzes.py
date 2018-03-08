"""
Tests damage calculation.
"""

import pytest
from magus_kalkulator.sebzes import calculate_damage, return_penalty
from magus_kalkulator import magus_constants as mgc


TEST_DATA_CALCULATE = [
    (7, 13, 2, True, (8, 16)),
    (3, 21, 1, False, (3, 19)),
    (3, 2, 1, False, (0, 0)),
    (3, 3, 0, True, (0, 0)),
    (0, 7, 2, False, (1, 7))
]

TEST_SFE_MAP = {
    'Bboka': 4, 'Jfelkar': 4, 'Jlabszar': 4, 'Bkulcs': 4, 'Jlabfej': 4,
    'Has': 4, 'Jvall': 4, 'Jkonyok': 4, 'Bcomb': 4, 'Nyak': 4, 'Jkezfej': 4,
    'Jterd': 4, 'Bcsuklo': 4, 'Bkonyok': 4, 'Balkar': 4, 'Jkulcs': 4,
    'Bfelkar': 4, 'Agyek': 4, 'Jcomb': 4, 'Blabszar': 4, 'Jboka': 4,
    'Jalkar': 4, 'Bvall': 4, 'Mellkas': 4, 'Bterd': 4, 'Jcsuklo': 4,
    'Blabfej': 4, 'Arc': 4, 'Bkezfej': 4, 'Koponya': 4
}


@pytest.mark.parametrize('sfe,damage,atutes,tulutes,expected',
                         TEST_DATA_CALCULATE)
def test_calculate_damage(sfe, damage, atutes, tulutes, expected):
    """
    Tests damage calculation using sfe, damage, etc and a randomly-picked
    body part.
    """
    result = calculate_damage(sfe, damage, atutes, tulutes=tulutes)
    assert result == expected


def test_return_penalty():
    """
    Tests the penalty returned on hitting a specific body part
    with pre-specified damage.
    """
    result = return_penalty(TEST_SFE_MAP, 21,
                            ('Fej', 'Koponya', 'Koponya'),
                            14, mgc.THRUST, atutes=3)
    expected_keys = ['ep_loss', 'fp_loss', 'hit_target', 'penalty']
    actual_keys = result.keys()
    assert all(x in actual_keys for x in expected_keys)

    assert result['ep_loss'] == 4
    assert result['fp_loss'] == 20

    target_parts = len(result['hit_target'])
    assert target_parts == 3

    penalty = result['penalty']

    assert isinstance(penalty, list)
    assert penalty == [mgc.SLIGHT_BLEEDING,
                       mgc.SLIGHT_HANDICAP,
                       mgc.SLIGHT_PAIN,
                       mgc.EXTRA_K6]
