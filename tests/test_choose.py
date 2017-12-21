import pytest

from magus.choose import pick_penalty, calculate_seriousness, get_threshold
from magus.torzs import TORZS_TABLA, TORZS_THRESHOLDS
from magus.fej import FEJ_TABLA, FEJ_THRESHOLDS
from magus.vegtag import VEGTAG_TABLA, VEGTAG_THRESHOLDS

test_data_penalty = [
    (TORZS_TABLA, 'Vag', 'Mellkas', 1, ['gyv', 'zh', 'gyf', 'k6']),
    (FEJ_TABLA, 'Szur', 'Arc', 0, 'nincs hatrany'),
    (VEGTAG_TABLA, 'Zuz', 'Jkez', 4, 'maradando benulas'),
    (VEGTAG_TABLA, 'Foo', 'Jkez', 4, 'Foo'),
    (TORZS_TABLA, 'Vag', 'Mellkas', 5, 'list index out of range')
]


@pytest.mark.parametrize('table,type,target,index,expected', test_data_penalty)
def test_pick_penalty(table, type, target, index, expected):
    """
    Expects the correct penalties to be chosen.
    """
    result = pick_penalty(table, type, target, index)
    assert result == expected


test_data_threshold = [
    (13, 17, 2)
]


@pytest.mark.parametrize('max_ep,threshold,expected', test_data_threshold)
def test_get_threshold(max_ep, threshold, expected):
    """
    Expects the correct penalties to be chosen.
    """
    result = get_threshold(max_ep, threshold)
    assert result == expected


test_data_seriousness = [
    (1, 13, FEJ_THRESHOLDS, 0),
    (3, 13, FEJ_THRESHOLDS, 1),
    (4, 13, FEJ_THRESHOLDS, 2),
    (7, 13, FEJ_THRESHOLDS, 3),
    (10, 13, FEJ_THRESHOLDS, 4),
    (3, 16, TORZS_THRESHOLDS, 0),
    (7, 16, TORZS_THRESHOLDS, 1),
    (8, 16, TORZS_THRESHOLDS, 2),
    (12, 16, TORZS_THRESHOLDS, 3),
    (17, 16, TORZS_THRESHOLDS, 4),
    (1, 14, VEGTAG_THRESHOLDS, 1),
    (3, 14, VEGTAG_THRESHOLDS, 2),
    (6, 14, VEGTAG_THRESHOLDS, 3),
    (7, 14, VEGTAG_THRESHOLDS, 4)
]


@pytest.mark.parametrize('damage,max_ep,thresholds,expected', test_data_seriousness)
def test_calculate_seriousness(damage, max_ep, thresholds, expected):
    """
    Expects the correct penalties to be chosen.
    """
    result = calculate_seriousness(damage, max_ep, thresholds)
    assert result == expected
