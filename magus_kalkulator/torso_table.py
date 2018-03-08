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
            [mgc.MODERATE_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING,
             mgc.PARTIAL_NUMBNESS_1,
             mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING,
             mgc.NUMBNESS_1,
             mgc.SEVERE_HANDICAP],
            mgc.DEATH
        ],
        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING,
             mgc.SEVERE_HANDICAP,
             mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING,
             mgc.CRITICAL_HANDICAP,
             mgc.MODERATE_PAIN,
             mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN, mgc.DISEASE],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN, mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.SLIGHT_HANDICAP],
            [mgc.MODERATE_BLEEDING, mgc.DISEASE, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.SLIGHT_HANDICAP],
            [mgc.MODERATE_BLEEDING, mgc.DISEASE, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.REDUCE_50],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.REDUCE_30],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.REDUCE_10],
            mgc.DEATH
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS, mgc.SEVERE_PAIN],
            mgc.DEATH
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
            mgc.DEATH
        ],
        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.DISEASE],
            [mgc.SEVERE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, mgc.MODERATE_PAIN, mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K10],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6, mgc.DISEASE],
            [mgc.SEVERE_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K10],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.REDUCE_50],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.REDUCE_30],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.REDUCE_10],
            mgc.DEATH
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS, mgc.SEVERE_PAIN],
            mgc.DEATH
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
            mgc.DEATH
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.DAZE_1_SLIGHT_HANDICAP, mgc.EXTRA_K10],
            [mgc.SLIGHT_BLEEDING_INT, mgc.DAZE_2_SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.DISEASE],
            [mgc.MODERATE_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.DISEASE, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.CRITICAL_HANDICAP, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.DISEASE, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.CRITICAL_HANDICAP, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_PAIN, mgc.REDUCE_80],
            [mgc.SLIGHT_HANDICAP, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_30],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.NUMBNESS, mgc.SEVERE_PAIN],
            mgc.DEATH
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
            mgc.DEATH
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN, mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN, mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.SEVERE_HANDICAP, mgc.PARTIAL_NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_PAIN, mgc.REDUCE_80],
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.MODERATE_PAIN, mgc.REDUCE_50],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_20],
            mgc.DEATH
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS, mgc.MODERATE_PAIN],
            [mgc.SEVERE_BLEEDING, mgc.NUMBNESS, mgc.SEVERE_PAIN],
            mgc.DEATH
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
            mgc.DEATH
        ],


        mgc.CHEST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.DISEASE],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN, mgc.DISEASE],
            mgc.DEATH
        ],
        mgc.STOMACH:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6, mgc.DISEASE],
            [mgc.MODERATE_BLEEDING_INT, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],
        mgc.SHOULDERBLADE:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SEVERE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.DEATH
        ],
        mgc.BACK:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],
        mgc.WAIST:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.SLIGHT_PAIN, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING_INT, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.CRITICAL_HANDICAP, mgc.SEVERE_PAIN],
            mgc.DEATH
        ],

        mgc.BUTTOCKS:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.EXTRA_K6, mgc.REDUCE_70],
            [mgc.SLIGHT_BLEEDING, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.REDUCE_60],
            [mgc.MODERATE_BLEEDING, mgc.SLIGHT_HANDICAP, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_10],
            mgc.DEATH
        ],
        mgc.SPINE:
        [
            mgc.NULL_HANDICAP,
            ["ervenytelen"],
            [mgc.SLIGHT_BLEEDING_INT, mgc.SEVERE_HANDICAP, mgc.MODERATE_PAIN, mgc.EXTRA_K6],
            [mgc.MODERATE_BLEEDING_INT, mgc.DISEASE, mgc.SEVERE_HANDICAP, mgc.PARTIAL_NUMBNESS, mgc.SEVERE_PAIN],
            mgc.DEATH
        ]

    }
}
