"""
Functions to calculate actual damage.
"""

from __future__ import division

import math

from magus_kalkulator.choose import calculate_penalty
import magus_kalkulator.magus_constants as mgc


def calculate_damage(sfe, damage, atutes, tulutes=False):
    """
    Calculates the actual ep and fp damage based on:
        - The SFE of the character
        - The actual damage
        - The armour piercing of the attacking weapon
        - Whether it was a critical hit (tulutes=True) or not

    Returns the total ep and fp damage (if any)
    """
    sfe -= atutes

    if sfe < 0:
        sfe = 0

    damage -= sfe

    if damage <= 0:
        return 0, 0

    if tulutes:
        ep_damage = damage
        fp_damage = damage * 2
    else:
        ep_damage = int(math.floor(damage/5))
        fp_damage = damage

    return ep_damage, fp_damage


def get_sfe_per_part(sfe_map, bp_list):
    """
    Tries to retrieve the sfe per body part.
    The corresponding body part will be either
    the second or the third element of the body parts list.
    """
    _main_part, penalty_part, sfe_part = bp_list

    try:
        sfe = sfe_map[sfe_part]
    except KeyError:
        sfe = sfe_map[penalty_part]

    return sfe


def add_disease(penalties, sub_body_part, rank):

    penalties = [x for x in penalties if x != mgc.DISEASE]

    # It may happen that depending on the damage and main part
    # a disease is possible but the sub part hit does not have
    # any sickness associated with it, in this case the disease
    # is only deleted from the penalties
    try:
        disease = mgc.DISEASE_MAP[sub_body_part]

        # E.g. in the case of a rank2 damage, disease has level0
        disease_level_prefix = mgc.DISEASE_LEVEL.format(rank - 2)
        disease = '{} {}'.format(disease_level_prefix, disease)

        return penalties + [disease]

    except KeyError:
        return penalties


def return_penalty(sfe, damage, body_parts_list, max_ep, wtype, **kwargs):
    """
    Gets the penalty associated with a damage.
    """
    tulutes = kwargs.get('tulutes', False)
    atutes = kwargs.get('atutes', 0)
    sfe = get_sfe_per_part(sfe, body_parts_list)
    main_part, penalty_part, sfe_part = body_parts_list
    ep_loss, fp_loss = calculate_damage(sfe, damage, atutes, tulutes=tulutes)
    rank, penalties, sfe_part = calculate_penalty(ep_loss,
                                                  max_ep,
                                                  wtype,
                                                  body_parts_list)

    if mgc.DISEASE in penalties:
        penalties = add_disease(penalties, sfe_part, rank)

    return {
        'ep_loss': ep_loss,
        'fp_loss': fp_loss,
        'hit_target': [main_part, penalty_part, sfe_part],
        'penalty': penalties}
