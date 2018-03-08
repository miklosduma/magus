"""
Limb penalties table.
"""

import magus_kalkulator.magus_constants as mgc

VEGTAG_THRESHOLDS = [50, 25, 17, 9]


VEGTAG_TABLA = {
    mgc.SLASH:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.REDUCE_80],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_60],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.REDUCE_30],
            mgc.MAIMING
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.REDUCE_80],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_60],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.REDUCE_30],
            mgc.MAIMING
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_BLEEDING,
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.MAIMING
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_BLEEDING,
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.MAIMING
        ]
    },
    mgc.THRUST:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, mgc.REDUCE_80],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.REDUCE_60],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_40],
            mgc.LIMB_PARALYSIS
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, mgc.REDUCE_80],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.REDUCE_60],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_40],
            mgc.LIMB_PARALYSIS
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.MAIMING
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.MAIMING
        ]
    },

    mgc.BLUDGEON:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.REDUCE_80],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, mgc.REDUCE_50],
            [mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_30],
            mgc.LIMB_PARALYSIS
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, mgc.REDUCE_80],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, mgc.REDUCE_50],
            [mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_30],
            mgc.LIMB_PARALYSIS
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_HANDICAP_1,
            [mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.LIMB_PARALYSIS
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_HANDICAP_1,
            [mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.LIMB_PARALYSIS
        ]
    },
    mgc.CLAW:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.REDUCE_90],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_60],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_30],
            mgc.LIMB_PARALYSIS
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.REDUCE_90],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_60],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_30],
            mgc.LIMB_PARALYSIS
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.LIMB_PARALYSIS
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.LIMB_PARALYSIS
        ]
    },
    mgc.BITE:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, mgc.REDUCE_90],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_50],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_30],
            mgc.MAIMING
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, mgc.REDUCE_90],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, mgc.REDUCE_50],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, mgc.REDUCE_30],
            mgc.MAIMING
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.MAIMING
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            mgc.MAIMING
        ]
    }
}
