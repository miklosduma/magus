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
            "nincs hatrany",
            ["mv", mgc.SLIGHT_HANDICAP, "k6"],
            ["mv", "rb*", "mf"],
            ["hv", "tb*", mgc.SEVERE_HANDICAP],
            "halal"
        ],
        mgc.CHEST:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", mgc.SEVERE_HANDICAP, "mf"],
            ["hv", mgc.CRITICAL_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", mgc.SLIGHT_HANDICAP, "mf", "beteg"],
            ["hv", mgc.CRITICAL_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            [mgc.SLIGHT_HANDICAP, "gyf"],
            ["mv", "rb*", "mf"],
            ["mv", "beteg", mgc.SEVERE_HANDICAP, "rb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", "gyf", mgc.SLIGHT_HANDICAP],
            ["mv", "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv", "beteg", mgc.SEVERE_HANDICAP, "mf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", "gyf", mgc.SLIGHT_HANDICAP],
            ["mv", "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv", "beteg", mgc.SEVERE_HANDICAP, "mf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "50%"],
            ["mv", mgc.SLIGHT_HANDICAP, "gyf", "30%"],
            ["hv", mgc.SLIGHT_HANDICAP, "tb*", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["mv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", "rb**", "mf"],
            ["hv", "tb", "hf"],
            "halal"
        ]
    },
    mgc.THRUST:
    {
        mgc.COLLARBONE:
        [
            "nincs hatrany",
            ["mv", mgc.SLIGHT_HANDICAP_1, "k6"],
            ["mv", "rb*", "gyf"],
            ["hv", "tb*", "mf"],
            "halal"
        ],
        mgc.CHEST:
        [
            "nincs hatrany",
            [mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv(b)", mgc.SLIGHT_HANDICAP, "gyf", "beteg"],
            ["hv(b)", mgc.CRITICAL_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "k10"],
            ["gyv(b)", mgc.SLIGHT_HANDICAP, "gyf", "k6", "beteg"],
            ["hv(b)", mgc.SEVERE_HANDICAP, "mf"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["gyf"],
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k10"],
            ["mv(b)", "beteg", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "k6"],
            ["gyv(b)", "beteg", mgc.SEVERE_HANDICAP, "mf"],
            ["mv(b)", "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "k6"],
            ["gyv(b)", "beteg", mgc.SEVERE_HANDICAP, "mf"],
            ["mv(b)", "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "50%"],
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "30%"],
            ["mv", mgc.SEVERE_HANDICAP, "mf", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["mv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", "rb**", "mf"],
            ["hv", "tb", "hf"],
            "halal"
        ]
    },

    mgc.BLUDGEON:
    {

        mgc.COLLARBONE:
        [
            "nincs hatrany",
            ["rb*", "gyf", "k6"],
            ["gyv", "rb*", "mf"],
            ["hv", "tb*", "hf"],
            "halal"
        ],


        mgc.CHEST:
        [
            "nincs hatrany",
            [mgc.SLIGHT_HANDICAP, "gyf"],
            ["gyv", mgc.SEVERE_HANDICAP, "mf"],
            ["mv(b)", mgc.SEVERE_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["kabulat1kor_zh", "k10"],
            ["gyv(b)", "kabulat2kor_zh", "gyf", "beteg"],
            ["mv(b)", mgc.SEVERE_HANDICAP, "mf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["gyf"],
            ["gyv", "rb*", "mf"],
            ["mv", mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyf", "k6"],
            ["gyv(b)", "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", "beteg", mgc.CRITICAL_HANDICAP, "mf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyf", "k6"],
            ["gyv(b)", "beteg", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv(b)", "beteg", mgc.CRITICAL_HANDICAP, "mf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["mf", "80%"],
            [mgc.SLIGHT_HANDICAP, "rb*", "mf", "30%"],
            ["mv", mgc.SLIGHT_HANDICAP, "tb*", "hf"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
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
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", "rb*", "mf"],
            ["hv", mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],


        mgc.CHEST:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv", mgc.SEVERE_HANDICAP, "mf"],
            ["hv", mgc.CRITICAL_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv", mgc.SEVERE_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            [mgc.SLIGHT_HANDICAP, "gyf"],
            ["gyv", "rb*", "mf"],
            ["mv", mgc.SEVERE_HANDICAP, "rb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", "gyf", "k6"],
            ["mv", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv", "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", "gyf", "k6"],
            ["mv", mgc.SLIGHT_HANDICAP, "mf"],
            ["mv", "beteg", mgc.SEVERE_HANDICAP, "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", "gyf", "80%"],
            ["gyv", mgc.SLIGHT_HANDICAP, "mf", "50%"],
            ["mv", mgc.SLIGHT_HANDICAP, "tb*", "mf", "20%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["mv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["mv", "rb**", "mf"],
            ["hv", "tb", "hf"],
            "halal"
        ]

    },
    mgc.BITE:
    {

        mgc.COLLARBONE:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP_1, "gyf", "k6"],
            ["mv", "rb*", "gyf", "k6"],
            ["hv", mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],


        mgc.CHEST:
        [
            "nincs hatrany",
            [mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv(b)", mgc.SEVERE_HANDICAP, "mf", "beteg"],
            ["mv(b)", mgc.CRITICAL_HANDICAP, "hf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "k6"],
            ["gyv(b)", mgc.SEVERE_HANDICAP, "mf", "k6", "beteg"],
            ["mv(b)", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP_1, "gyf", "k6"],
            ["mv", "rb*", "gyf", "k6"],
            ["hv", mgc.SLIGHT_HANDICAP, "tb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv(b)", "beteg", mgc.SEVERE_HANDICAP, "mf", "k6"],
            ["mv(b)", "beteg", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "gyf", "k6"],
            ["gyv(b)", "beteg", mgc.SEVERE_HANDICAP, "mf", "k6"],
            ["mv(b)", "beteg", mgc.CRITICAL_HANDICAP, "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", mgc.SLIGHT_HANDICAP, "k6", "70%"],
            ["gyv", mgc.SEVERE_HANDICAP, "mf", "60%"],
            ["mv", mgc.SLIGHT_HANDICAP, "tb*", "mf", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["ervenytelen", "ujradobas"],
            ["gyv(b)", mgc.SEVERE_HANDICAP, "mf", "k6"],
            ["mv(b)", "beteg", mgc.SEVERE_HANDICAP, "rb**", "hf"],
            "halal"
        ]

    }
}
