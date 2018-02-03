import magus_constants as mgc

VEGTAG_THRESHOLDS = [50, 25, 17, 9]


VEGTAG_TABLA = {
    mgc.SLASH:
    {
        mgc.RLEG:
        [
            'nincs hatrany',
            ['gyv', '80%'],
            ['gyf', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            'nincs hatrany',
            ['gyv', '80%'],
            ['gyf', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            'nincs hatrany',
            'gyv',
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            'nincs hatrany',
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
            'nincs hatrany',
            ['k6', '80%'],
            ['gyv', 'rb*', '60%'],
            ['gyv', 'tb*', 'mf', '40%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            'nincs hatrany',
            ['k6', '80%'],
            ['gyv', 'rb*', '60%'],
            ['gyv', 'tb*', 'mf', '40%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            'nincs hatrany',
            ['gyv', 'zh*'],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            'nincs hatrany',
            ['gyv', 'zh*'],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ]
    },

    mgc.BLUDGEON:
    {
        mgc.RLEG:
        [
            'nincs hatrany',
            ['zh', '80%'],
            ['gyf', 'rb*', '50%'],
            ['tb*', 'mf', '30%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            'nincs hatrany',
            ['zh', '80%'],
            ['gyf', 'rb*', '50%'],
            ['tb*', 'mf', '30%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            'nincs hatrany',
            'zh*',
            ['rb*', 'gyf'],
            ['gyv', 'tb*', 'mf'],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            'nincs hatrany',
            'zh*',
            ['rb*', 'gyf'],
            ['gyv', 'tb*', 'mf'],
            'maradando benulas'
        ]
    },
    mgc.CLAW:
    {
        mgc.RLEG:
        [
            'nincs hatrany',
            ['gyv', '90%'],
            ['gyv', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', 'gyf', '30%'],
            'maradando benulas'
        ],
        mgc.LLEG:
        [
            'nincs hatrany',
            ['gyv', '90%'],
            ['gyv', 'rb*', 'gyf', '60%'],
            ['mv', 'tb*', 'gyf', '30%'],
            'maradando benulas'
        ],
        mgc.RARM:
        [
            'nincs hatrany',
            ['gyv', 'k6'],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'maradando benulas'
        ],

        mgc.LARM:
        [
            'nincs hatrany',
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
            'nincs hatrany',
            ['k6', '90%'],
            ['gyv', 'rb*', 'gyf', '50%'],
            ['mv', 'tb*', 'mf', '30%'],
            'csonkolas'
        ],
        mgc.LLEG:
        [
            'nincs hatrany',
            ['k6', '90%'],
            ['gyv', 'rb*', 'gyf', '50%'],
            ['mv', 'tb*', 'mf', '30%'],
            'csonkolas'
        ],
        mgc.RARM:
        [
            'nincs hatrany',
            ['gyv', 'zh*'],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ],

        mgc.LARM:
        [
            'nincs hatrany',
            ['gyv', 'zh*'],
            ['gyv', 'rb*', 'gyf'],
            ['mv', 'tb*', 'mf'],
            'csonkolas'
        ]
    }
}
