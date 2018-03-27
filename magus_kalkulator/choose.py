"""
Functions to calculate seriousness of damage and choose associated handicap.
"""

from __future__ import division
import random
import magus_kalkulator.magus_constants as mgc

from magus_kalkulator.torso_table import TORZS_TABLA, TORZS_THRESHOLDS
from magus_kalkulator.limbs_table import VEGTAG_TABLA, VEGTAG_THRESHOLDS
from magus_kalkulator.head_table import FEJ_TABLA, FEJ_THRESHOLDS

TABLE_PER_PART = {
    mgc.RLEG: VEGTAG_TABLA,
    mgc.LLEG: VEGTAG_TABLA,
    mgc.RARM: VEGTAG_TABLA,
    mgc.LARM: VEGTAG_TABLA,
    mgc.TORSO: TORZS_TABLA,
    mgc.HEAD: FEJ_TABLA
}

THRESHOLDS_PER_PART = {
    mgc.RLEG: VEGTAG_THRESHOLDS,
    mgc.LLEG: VEGTAG_THRESHOLDS,
    mgc.RARM: VEGTAG_THRESHOLDS,
    mgc.LARM: VEGTAG_THRESHOLDS,
    mgc.TORSO: TORZS_THRESHOLDS,
    mgc.HEAD: FEJ_THRESHOLDS
}

INVALIDS = [mgc.CARDIA, mgc.BREASTBONE, mgc.SPINE]

REPLACEMENTS_MINOR = {
    mgc.CARDIA: [mgc.STOMACH, mgc.GROINS],
    mgc.BREASTBONE: [mgc.HEART, mgc.LUNGS]}

REPLACEMENTS_MAJOR = {
    mgc.SPINE: [
        [mgc.SHOULDERBLADE, mgc.RSHOULDERBLADE],
        [mgc.SHOULDERBLADE, mgc.LSHOULDERBLADE],
        [mgc.BACK, mgc.RBACK], [mgc.BACK, mgc.LBACK],
        [mgc.WAIST, mgc.RWAIST], [mgc.WAIST, mgc.LWAIST],
        [mgc.BUTTOCKS, mgc.RBUTTOCKS], [mgc.BUTTOCKS, mgc.LBUTTOCKS]]}


def pick_penalty(table, wtype, bpart, rank):
    """
    Picks the relevant penalty from the
    specified penalty table based on:
        - The weapon type
        - The body part
        - The seriousness of the damage
    """
    try:
        return table[wtype][bpart][rank]

    except KeyError as error:
        return 'key_error', error.args[0]

    except IndexError as error:
        return 'index_error', error.args[0]


def get_threshold(max_ep, threshold):
    """
    Returns actual threshold values based on:
        - Max EP
        - Threshold percentage
    """
    return round(max_ep/100 * threshold)


def calculate_seriousness(damage, max_ep, thresholds):
    """
    Calculates the seriousness (index) of a damage based on:
        - The suffered EP damage
        - The max EP of the character
        - The thresholds (%) based on the body part

    Returns a value of 0 - 3 depending on the seriousness of the hit,
    or the string 'nincs hatrany' if the damage was below all thresholds.
    """
    thresholds = [get_threshold(max_ep, x) for x in thresholds]
    [vegzetes, kritikus, veszelyes, sulyos] = thresholds

    if damage < sulyos:
        return 0

    elif damage < veszelyes:
        return 1

    elif damage < kritikus:
        return 2

    elif damage < vegzetes:
        return 3

    return 4


def is_part_valid(wtype, bodypart, rank):
    """
    Checks against exceptions such as rank 1 bite damages
    to the spine. It returns False if the targeted body part
    is invalid in the given damage/weapon type category.
    """

    if wtype != mgc.BITE:
        return True

    if rank != 1:
        return True

    return bodypart not in INVALIDS


def replace_smallest_part(body_part):
    """
    In case of an invalid hit, replaces the body part
    with a neighbour body part. (Replaces smallest body
    parts , e.g. temple)
    """
    replacements = REPLACEMENTS_MINOR[body_part]
    new_part = random.choice(replacements)
    print('Replacing {} with {}'.format(body_part, new_part))
    return new_part


def replace_sub_part(body_part):
    """
    In case of an invalid hit, replaces the body part
    with a neighbour body part. (Replaces sub body
    part, e.g. skull)
    """
    [subpart, smallestpart] = random.choice(REPLACEMENTS_MAJOR[body_part])
    print('Replacing {} with {} and {}'.format(body_part,
                                               subpart,
                                               smallestpart))
    return subpart, smallestpart


def calculate_penalty(ep_damage, max_ep, wtype, bodyparts):
    """
    Calculates the penalty based on:
        - max_ep:
            The maximum EP of the character
        - ep_damage:
            The suffered EP damage
        - wtype:
            The type of attacking weapon
        - bodyparts:
            A tuple of body parts (e.g. Torso/Back/Right Back)
    """
    mainpart, subpart, smallest_part = bodyparts
    thresholds = THRESHOLDS_PER_PART[mainpart]
    rank = calculate_seriousness(ep_damage, max_ep, thresholds)

    is_valid_sub_part = is_part_valid(wtype, subpart, rank)

    if not is_valid_sub_part:
        subpart, smallest_part = replace_sub_part(subpart)

    is_valid_smallest = is_part_valid(wtype, smallest_part, rank)

    if not is_valid_smallest:
        smallest_part = replace_smallest_part(smallest_part)

    table = TABLE_PER_PART[mainpart]
    penalty = pick_penalty(table, wtype, subpart, rank)
    return rank, penalty, smallest_part
