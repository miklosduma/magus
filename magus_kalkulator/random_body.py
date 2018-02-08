import random

from magus_kalkulator import magus_constants as mgc

BODY_PARTS_LIST = [
    mgc.HEAD_LIST, mgc.TORSO_LIST, mgc.TORSO_LIST, mgc.TORSO_LIST,
    mgc.TORSO_LIST, mgc.RARM_LIST, mgc.RARM_LIST, mgc.LARM_LIST,
    mgc.RLEG_LIST, mgc.LLEG_LIST]

BODY_PARTS_LIST_BEHIND = [
    mgc.HEAD_LIST, mgc.TORSO_LIST_BEHIND, mgc.TORSO_LIST_BEHIND,
    mgc.TORSO_LIST_BEHIND, mgc.TORSO_LIST_BEHIND, mgc.RARM_LIST,
    mgc.RARM_LIST, mgc.LARM_LIST,
    mgc.RLEG_LIST, mgc.LLEG_LIST]


def pick_sub_parts(main_part=None, sub_part=None, from_behind=False):
    """
    Returns a randomly chosen sub-body part.
    """
    if main_part and sub_part:
        pen_part, sfe_part = sub_part
        return main_part, pen_part, sfe_part

    if from_behind:
        body_parts_list = BODY_PARTS_LIST_BEHIND
    else:
        body_parts_list = BODY_PARTS_LIST

    if main_part:
        print(main_part)
        body_part = [x for x in body_parts_list if x[0] == main_part][0]

    else:
        main_parts = body_parts_list
        body_part = random.choice(main_parts)

    [main_part, sub_parts] = body_part

    sub_part = random.choice(sub_parts)
    pen_part, sfe_part = sub_part
    return main_part, pen_part, sfe_part
