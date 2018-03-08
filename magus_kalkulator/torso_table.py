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
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS_1, mgc.SEVERE_HANDICAP],
            "halal"
        ],
        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, mgc.MODERATE_PAIN, "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN, "beteg"],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN, "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.SLIGHT_HANDICAP],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.SLIGHT_HANDICAP],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "50%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, "30%"],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS, mgc.SEVERE_PAIN],
            "halal"
        ]
    },
    mgc.THRUST:
    {
        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP_1, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, "beteg"],
            [mgc.SEVERE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, mgc.MODERATE_PAIN, "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K10],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6, "beteg"],
            [mgc.SEVERE_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K10],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, "50%"],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, "30%"],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS, mgc.SEVERE_PAIN],
            "halal"
        ]
    },

    mgc.BLUDGEON:
    {

        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS_1, mgc.SEVERE_PAIN],
            "halal"
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            ["kabulat1kor_zh", mgc.EXTRA_K10],
            [mgc.SLIGHT_BLEEDING_INT, "kabulat2kor_zh", mgc.SLIGHT_PAIN, "beteg"],
            [mgc.MODERATE_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, mgc.MODERATE_PAIN],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_PAIN, "80%"],
            [mgc.SLIGHT_HANDICAP, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN, "30%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.SEVERE_PAIN],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.NUMBNESS, mgc.SEVERE_PAIN],
            "halal"
        ]

    },
    mgc.CLAW:
    {

        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            "halal"
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN, "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN, "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, "beteg", mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, "80%"],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN, "50%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, "20%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS, mgc.SEVERE_PAIN],
            "halal"
        ]

    },
    mgc.BITE:
    {

        mgc.COLLARBONE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            "halal"
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, "beteg"],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN, "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6, "beteg"],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            "halal"
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6, "70%"],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, "60%"],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            ["ervenytelen", "ujradobas"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING_INT, "beteg", mgc.SEVERE_HANDICAP, mgc.PARTIAL_NUMBNESS, mgc.SEVERE_PAIN],
            "halal"
        ]

    }
}
