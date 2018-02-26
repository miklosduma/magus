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
            ['gyv', '80%'],
            ['gyf', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            ['gyv', '80%'],
            ['gyf', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            'gyv',
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            'gyv',
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ]
    },
    mgc.THRUST:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '80%'],
            ['gyv', 'rb*', '60%'],
            ['gyv', 'tb*', 'mf', '40%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '80%'],
            ['gyv', 'rb*', '60%'],
            ['gyv', 'tb*', 'mf', '40%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            ['gyv', mgc.SLIGHT_HANDICAP_1],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            ['gyv', mgc.SLIGHT_HANDICAP_1],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
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
            ['gyv', 'tb*', 'mf'],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            mgc.SLIGHT_HANDICAP_1,
            ['rb*', 'gyf'],
            ['gyv', 'tb*', 'mf'],
            'maradando benulas'
        ]
    },
    mgc.CLAW:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            ['gyv', '90%'],
            ['gyv', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', 'gyf', '30%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            ['gyv', '90%'],
            ['gyv', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', 'gyf', '30%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            ['gyv', 'k6'],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            ['gyv', 'k6'],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'maradando benulas'
        ]
    },
    mgc.BITE:
    {
        mgc.RLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '90%'],
            ['gyv', 'rb*', 'gyf', '50%'],
            ['mv', 'tb*', 'mf', '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            mgc.NULL_HANDICAP,
            ['k6', '90%'],
            ['gyv', 'rb*', 'gyf', '50%'],
            ['mv', 'tb*', 'mf', '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            mgc.NULL_HANDICAP,
            ['gyv', mgc.SLIGHT_HANDICAP_1],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            mgc.NULL_HANDICAP,
            ['gyv', mgc.SLIGHT_HANDICAP_1],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ]
    }
}
