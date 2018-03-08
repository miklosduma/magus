"""
Table containing all penalties per weapon-type/seriousness/hit target.
"""

import magus_kalkulator.magus_constants as mgc

FEJ_THRESHOLDS = [75, 50, 34, 17]


FEJ_TABLA = {
    mgc.SLASH:
    {
        mgc.FACE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "mf", "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, "mf"],
            [mgc.SEVERE_BLEEDING, "tb", "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "ajulas"],
            "halal"
        ]
    },

    mgc.THRUST:
    {
        mgc.FACE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, "mf"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP],
            [mgc.SEVERE_BLEEDING, "tb"],
            "halal"
        ],
        mgc.SKULL:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ]
    },

    mgc.BLUDGEON:
    {
        mgc.FACE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, "mf", "k6"],
            [mgc.SLIGHT_BLEEDING, "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "ajulas"],
            "halal"
        ],
        mgc.NECK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "rosszullet"],
            ["kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "gyf"],
            ["kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "ajulas"],
            "halal"
        ]
    },
    mgc.CLAW:
    {
        mgc.FACE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, "mf", "k6"],
            [mgc.MODERATE_BLEEDING, "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "ajulas"],
            "halal"
        ],
        mgc.NECK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.SEVERE_BLEEDING, "tb", "hf"],
            "halal"
        ],
        mgc.SKULL:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING, "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "ajulas"],
            "halal"
        ]
    },
    mgc.BITE:
    {
        mgc.FACE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "mf", "k6"],
            [mgc.SLIGHT_BLEEDING, "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING, mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.SEVERE_BLEEDING, "tb", "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING, "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "ajulas"],
            "halal"
        ]
    }
}
