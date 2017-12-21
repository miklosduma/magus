from __future__ import division

import math

from choose import pick_penalty, get_threshold, calculate_seriousness
from random_body import pick_sub_parts


def calculate_damage(sfe, damage, tulutes=False):
    """
    Calculates the actual ep and fp damage based on:
        - The SFE of the character
        - The actual damage
        - Whether it was a critical hit (tulutes=True) or not

    Returns the total ep and fp damage (if any)
    """
    damage -= sfe

    if tulutes:
        ep_damage = damage
        fp_damage = damage * 2
    else:
        ep_damage = math.floor(damage/5)
        fp_damage = damage

    return ep_damage, fp_damage