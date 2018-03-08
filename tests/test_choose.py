"""
Tests for choosing penalty.
"""

import pytest

from magus_kalkulator import magus_constants as mgc

from magus_kalkulator.choose import (pick_penalty, calculate_seriousness,
                                     get_threshold, calculate_penalty)
from magus_kalkulator.torso_table import TORZS_TABLA, TORZS_THRESHOLDS
from magus_kalkulator.head_table import FEJ_TABLA, FEJ_THRESHOLDS
from magus_kalkulator.limbs_table import VEGTAG_TABLA, VEGTAG_THRESHOLDS

TEST_DATA_PENALTY = [
    (TORZS_TABLA, mgc.SLASH, mgc.CHEST, 1, [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP,
                                            'gyf', 'k6']),
    (FEJ_TABLA, mgc.THRUST, mgc.FACE, 0, mgc.NULL_HANDICAP),
    (VEGTAG_TABLA, mgc.BLUDGEON, mgc.RARM, 4, 'maradando benulas'),
    (VEGTAG_TABLA, 'Foo', mgc.RARM, 4, ('key_error', 'Foo')),
    (TORZS_TABLA, mgc.SLASH, mgc.CHEST, 5, ('index_error',
                                            'list index out of range'))
]


@pytest.mark.parametrize('table,wp_type,target,index,expected',
                         TEST_DATA_PENALTY)
def test_pick_penalty(table, wp_type, target, index, expected):
    """
    Expects the correct penalties to be chosen.
    """
    result = pick_penalty(table, wp_type, target, index)
    assert result == expected


TEST_DATA_THRESHOLD = [
    (13, 17, 2)
]


@pytest.mark.parametrize('max_ep,threshold,expected', TEST_DATA_THRESHOLD)
def test_get_threshold(max_ep, threshold, expected):
    """
    Expects the correct penalties to be chosen.
    """
    result = get_threshold(max_ep, threshold)
    assert result == expected


TEST_DATA_SERIOUSNESS = [
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


@pytest.mark.parametrize('damage,max_ep,thresholds,expected',
                         TEST_DATA_SERIOUSNESS)
def test_calculate_seriousness(damage, max_ep, thresholds, expected):
    """
    Expects the correct penalties to be chosen.
    """
    result = calculate_seriousness(damage, max_ep, thresholds)
    assert result == expected


TEST_DATA_PENALTY_MAP = [

    {
        'damage': 3,
        'max_ep': 13,
        'wtype': mgc.THRUST,
        'mainpart': mgc.RARM,
        'subpart': mgc.RARM,
        'expected': [mgc.MODERATE_BLEEDING, 'tb*', 'mf']},

    {
        'damage': 7,
        'max_ep': 14,
        'wtype': mgc.SLASH,
        'mainpart': mgc.TORSO,
        'subpart': mgc.CHEST,
        'expected': [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, 'mf']},

    {
        'damage': 11,
        'max_ep': 15,
        'wtype': mgc.THRUST,
        'mainpart': mgc.HEAD,
        'subpart': mgc.SKULL,
        'expected': 'halal'}
]


@pytest.mark.parametrize('data_map',
                         TEST_DATA_PENALTY_MAP)
def test_calculate_penalty(data_map):
    """
    Tests full round penalty calculation.
    """
    damage = data_map['damage']
    max_ep = data_map['max_ep']
    wtype = data_map['wtype']
    mainpart = data_map['mainpart']
    subpart = data_map['subpart']

    result = calculate_penalty(damage, max_ep, wtype, mainpart, subpart)
    assert result == data_map['expected']
