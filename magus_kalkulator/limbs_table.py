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
            [mgc.SLIGHT_BLEEDING, '80%'],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, '60%'],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, '80%'],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, '60%'],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_BLEEDING,
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_BLEEDING,
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'csonkolas'
        ]
    },
    mgc.THRUST:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, '80%'],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, '60%'],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, '40%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, '80%'],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, '60%'],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, '40%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'csonkolas'
        ]
    },

    mgc.BLUDGEON:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, '80%'],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, '50%'],
            [mgc.NUMBNESS_1, mgc.MODERATE_PAIN, '30%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, '80%'],
            [mgc.SLIGHT_PAIN, mgc.PARTIAL_NUMBNESS_1, '50%'],
            [mgc.NUMBNESS_1, mgc.MODERATE_PAIN, '30%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_HANDICAP_1,
            [mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_HANDICAP_1,
            [mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.SLIGHT_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'maradando benulas'
        ]
    },
    mgc.CLAW:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, '90%'],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, '60%'],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.SLIGHT_PAIN, '30%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, '90%'],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, '60%'],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.SLIGHT_PAIN, '30%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.EXTRA_K6],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'maradando benulas'
        ]
    },
    mgc.BITE:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, '90%'],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, '50%'],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.EXTRA_K6, '90%'],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN, '50%'],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN, '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, mgc.PARTIAL_NUMBNESS_1, mgc.SLIGHT_PAIN],
            [mgc.MODERATE_BLEEDING, mgc.NUMBNESS_1, mgc.MODERATE_PAIN],
            'csonkolas'
        ]
    }
}
