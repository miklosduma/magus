from __future__ import division

import math

from choose import calculate_penalty
from random_body import pick_sub_parts


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
    main_part, penalty_part, sfe_part = bp_list

    try:
        sfe = sfe_map[sfe_part]
    except KeyError:
        sfe = sfe_map[penalty_part]

    return sfe


def return_penalty(sfe, damage, atutes, max_ep, wtype, tulutes=False):
    """
    Gets the penalty associated with a damage.
    """
    body_parts_list = pick_sub_parts()
    sfe = get_sfe_per_part(sfe, body_parts_list)
    main_part, penalty_part, sfe_part = body_parts_list
    ep_loss, fp_loss = calculate_damage(sfe, damage, atutes, tulutes=tulutes)
    result = calculate_penalty(ep_loss, max_ep, wtype, main_part, penalty_part)
    return {
        'ep_loss': ep_loss,
        'fp_loss': fp_loss,
        'hit_target': [main_part, penalty_part, sfe_part],
        'penalty': result
    }