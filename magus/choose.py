from __future__ import division
import pytest


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
        return error.message

    except IndexError as error:
        return error.message


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

