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
            ['gyf', 'rb*', 'gyf', '60%'],
            [mgc.MODERATE_BLEEDING, 'tb*', '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, '80%'],
            ['gyf', 'rb*', 'gyf', '60%'],
            [mgc.MODERATE_BLEEDING, 'tb*', '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_BLEEDING,
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_BLEEDING,
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'csonkolas'
        ]
    },
    mgc.THRUST:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '80%'],
            [mgc.SLIGHT_BLEEDING, 'rb*', '60%'],
            [mgc.SLIGHT_BLEEDING, 'tb*', 'mf', '40%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '80%'],
            [mgc.SLIGHT_BLEEDING, 'rb*', '60%'],
            [mgc.SLIGHT_BLEEDING, 'tb*', 'mf', '40%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'csonkolas'
        ]
    },

    mgc.BLUDGEON:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, '80%'],
            ['gyf', 'rb*', '50%'],
            ['tb*', 'mf', '30%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_HANDICAP, '80%'],
            ['gyf', 'rb*', '50%'],
            ['tb*', 'mf', '30%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_HANDICAP_1,
            ['rb*', 'gyf'],
            [mgc.SLIGHT_BLEEDING, 'tb*', 'mf'],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_HANDICAP_1,
            ['rb*', 'gyf'],
            [mgc.SLIGHT_BLEEDING, 'tb*', 'mf'],
            'maradando benulas'
        ]
    },
    mgc.CLAW:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, '90%'],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf', '60%'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'gyf', '30%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, '90%'],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf', '60%'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'gyf', '30%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, 'k6'],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, 'k6'],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'maradando benulas'
        ]
    },
    mgc.BITE:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '90%'],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf', '50%'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf', '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '90%'],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf', '50%'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf', '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            [mgc.SLIGHT_BLEEDING, mgc.SLIGHT_HANDICAP_1],
            [mgc.SLIGHT_BLEEDING, 'rb*', 'gyf'],
            [mgc.MODERATE_BLEEDING, 'tb*', 'mf'],
            'csonkolas'
        ]
    }
}
