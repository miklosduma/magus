import random

from magus_constants import (HEAD_LIST, TORSO_LIST, RLEG_LIST, LLEG_LIST,
                             RARM_LIST, LARM_LIST)

BODY_PARTS_LIST = [
    HEAD_LIST, TORSO_LIST, TORSO_LIST, TORSO_LIST, TORSO_LIST,
    RARM_LIST, RARM_LIST, LARM_LIST, RLEG_LIST, LLEG_LIST
]


def pick_sub_parts(main_part=None):
    """
    Returns a randomly chosen sub-body part.
    """
    if main_part:
        body_part = [x for x in BODY_PARTS_LIST if x[0] == main_part][0]

    else:
        main_parts = BODY_PARTS_LIST
        body_part = random.choice(main_parts)

    [main_part, sub_parts] = body_part

    sub_part = random.choice(sub_parts)
    pen_part, sfe_part = sub_part
    return main_part, pen_part, sfe_part
