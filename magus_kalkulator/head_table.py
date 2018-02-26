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
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "mf", "k6"],
            ["mv", mgc.SEVERE_HANDICAP, "mf"],
            ["mv(b)", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["mv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["hv", mgc.CRITICAL_HANDICAP, "mf"],
            ["hv", "tb", "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", mgc.SEVERE_HANDICAP, "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    },

    mgc.THRUST:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv", mgc.SEVERE_HANDICAP, "mf"],
            ["gyv(b)", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["mv", mgc.SLIGHT_HANDICAP, "k6"],
            ["mv", mgc.SEVERE_HANDICAP],
            ["hv", "tb"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv", mgc.SEVERE_HANDICAP, "mf"],
            ["mv(b)", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ]
    },

    mgc.BLUDGEON:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", mgc.SEVERE_HANDICAP, "mf", "k6"],
            ["gyv", "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            [mgc.SLIGHT_HANDICAP, "rosszullet"],
            ["kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", mgc.CRITICAL_HANDICAP, "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            [mgc.SLIGHT_HANDICAP, "gyf"],
            ["kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    },
    mgc.CLAW:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", mgc.SEVERE_HANDICAP, "mf", "k6"],
            ["mv", "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["hv", "tb", "hf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv", "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    },
    mgc.BITE:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "mf", "k6"],
            ["gyv", "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["hv", "tb", "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv", "kabulat", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    }
}
