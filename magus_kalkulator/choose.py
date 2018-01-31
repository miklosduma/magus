from __future__ import division

import magus_constants as mgc

from torso_table import TORZS_TABLA, TORZS_THRESHOLDS
from limbs_table import VEGTAG_TABLA, VEGTAG_THRESHOLDS
from head_table import FEJ_TABLA, FEJ_THRESHOLDS

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
        return 'key_error', error.message

    except IndexError as error:
        return 'index_error', error.message


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

    else:
        return 4


def calculate_penalty(ep_damage, max_ep, wtype, mainpart, subpart):
    """
    Calculates the penalty based on:
        - max_ep:
            The maximum EP of the character
        - ep_damage:
            The suffered EP damage
        - wtype:
            The type of attacking weapon
        - mainpart:
            E.g. Torzs/Jlab/Fej
        - subpart:
            E.g. Halantek/Gyomorszaj/etc
    """
    thresholds = THRESHOLDS_PER_PART[mainpart]
    rank = calculate_seriousness(ep_damage, max_ep, thresholds)
    table = TABLE_PER_PART[mainpart]
    return pick_penalty(table, wtype, subpart, rank)