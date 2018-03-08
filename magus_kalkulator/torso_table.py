"""
Penalties depending on seriousness, weapon-type and actual place of hit.
"""

import magus_kalkulator.magus_constants as mgc

TORZS_THRESHOLDS = [100, 75, 50, 25]


TORZS_TABLA = {
    mgc.SLASH:
    {
        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "k6"],
            [mgc.MODERATE_BLEEDING, "rb*", "mf"],
            [mgc.SEVERE_BLEEDING, "tb*", mgc.SEVERE_HANDICAP],
            "halal"
        ],
        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, "mf"],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "mf", "beteg"],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "gyf"],
            [mgc.MODERATE_BLEEDING, "rb*", "mf"],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, "rb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, "gyf", mgc.SLIGHT_HANDICAP],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, "mf"],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, "gyf", mgc.SLIGHT_HANDICAP],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, "mf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "50%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "30%"],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "rb**", "mf"],
            [mgc.SEVERE_BLEEDING, "tb", "hf"],
            "halal"
        ]
    },
    mgc.THRUST:
    {
        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP_1, "k6"],
            [mgc.MODERATE_BLEEDING, "rb*", "gyf"],
            [mgc.SEVERE_BLEEDING, "tb*", "mf"],
            "halal"
        ],
        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SLIGHT_HANDICAP, "gyf", "beteg"],
            [mgc.SEVERE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "k10"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SLIGHT_HANDICAP, "gyf", "k6", "beteg"],
            [mgc.SEVERE_BLEEDING_INT, mgc.SEVERE_HANDICAP, "mf"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            ["gyf"],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k10"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "k6"],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "k6"],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "50%"],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "30%"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, "mf", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "rb**", "mf"],
            [mgc.SEVERE_BLEEDING, "tb", "hf"],
            "halal"
        ]
    },

    mgc.BLUDGEON:
    {

        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            ["rb*", "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING, "rb*", "mf"],
            [mgc.SEVERE_BLEEDING, "tb*", "hf"],
            "halal"
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "gyf"],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, mgc.SEVERE_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            ["kabulat1kor_zh", "k10"],
            [mgc.SLIGHT_BLEEDING_INT, "kabulat2kor_zh", "gyf", "beteg"],
            [mgc.MODERATE_BLEEDING_INT, mgc.SEVERE_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            ["gyf"],
            [mgc.SLIGHT_BLEEDING, "rb*", "mf"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            ["gyf", "k6"],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, "mf"],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            ["gyf", "k6"],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, "mf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            ["mf", "80%"],
            [mgc.SLIGHT_HANDICAP, "rb*", "mf", "30%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "hf"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "mf", "k6"],
            ["rb**", "mf"],
            ["tb", "hf"],
            "halal"
        ]

    },
    mgc.CLAW:
    {

        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "rb*", "mf"],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, "mf"],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "gyf"],
            [mgc.SLIGHT_BLEEDING, "rb*", "mf"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, "rb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "mf"],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, "gyf", "80%"],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "mf", "50%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "mf", "20%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "rb**", "mf"],
            [mgc.SEVERE_BLEEDING, "tb", "hf"],
            "halal"
        ]

    },
    mgc.BITE:
    {

        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "rb*", "gyf", "k6"],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, "mf", "beteg"],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "k6"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, "mf", "k6", "beteg"],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1, "gyf", "k6"],
            [mgc.MODERATE_BLEEDING, "rb*", "gyf", "k6"],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, "mf", "k6"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, "mf", "k6"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "k6", "70%"],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, "mf", "60%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, "tb*", "mf", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            ["ervenytelen", "ujradobas"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, "mf", "k6"],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, "rb**", "hf"],
            "halal"
        ]

    }
}
