import magus_constants as mgc

TORZS_THRESHOLDS = [100, 75, 50, 25]


TORZS_TABLA = {
    mgc.SLASH:
    {
        mgc.COLLARBONE:
        [
            "nincs hatrany",
            ["mv", "zh", "k6"],
            ["mv", "rb*", "mf"],
            ["hv", "tb*", "jh"],
            "halal"
        ],
        mgc.CHEST:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["mv", "jh", "mf"],
            ["hv", "vh", "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["mv", "zh", "mf", "beteg"],
            ["hv", "vh", "hf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["zh", "gyf"],
            ["mv", "rb*", "mf"],
            ["mv", "beteg", "jh", "rb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", "gyf", "zh"],
            ["mv", "beteg", "zh", "mf"],
            ["mv", "beteg", "jh", "mf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", "gyf", "zh"],
            ["mv", "beteg", "zh", "mf"],
            ["mv", "beteg", "jh", "mf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", "zh", "50%"],
            ["mv", "zh", "gyf", "30%"],
            ["hv", "zh", "tb*", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["mv", "zh", "gyf", "k6"],
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
            ["mv", "zh*", "k6"],
            ["mv", "rb*", "gyf"],
            ["hv", "tb*",  "mf"],
            "halal"
        ],
        mgc.CHEST:
        [
            "nincs hatrany",
            ["zh", "gyf", "k6"],
            ["gyv(b)", "zh", "gyf", "beteg"],
            ["hv(b)", "vh", "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", "zh", "k10"],
            ["gyv(b)", "zh", "gyf", "k6", "beteg"],
            ["hv(b)", "jh", "mf"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["gyf"],
            ["gyv", "zh", "gyf", "k10"],
            ["mv(b)", "beteg", "vh", "hf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", "zh", "k6"],
            ["gyv(b)", "beteg", "jh", "mf"],
            ["mv(b)", "beteg", "jh", "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", "zh", "k6"],
            ["gyv(b)", "beteg", "jh", "mf"],
            ["mv(b)", "beteg", "jh", "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", "zh", "50%"],
            ["gyv", "zh", "gyf", "30%"],
            ["mv", "jh", "mf", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["mv", "zh", "gyf", "k6"],
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
            ["zh", "gyf"],
            ["gyv", "jh", "mf"],
            ["mv(b)", "jh", "mf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["kabulat1kor_zh", "k10"],
            ["gyv(b)", "kabulat2kor_zh", "gyf", "beteg"],
            ["mv(b)", "jh", "mf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["gyf"],
            ["gyv", "rb*", "mf"],
            ["mv", "zh", "tb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyf", "k6"],
            ["gyv(b)", "beteg", "zh", "mf"],
            ["mv(b)", "beteg", "vh", "mf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyf", "k6"],
            ["gyv(b)", "beteg", "zh", "mf"],
            ["mv(b)", "beteg", "vh", "mf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["mf", "80%"],
            ["zh", "rb*", "mf", "30%"],
            ["mv", "zh", "tb*", "hf"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["zh", "mf", "k6"],
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
            ["gyv", "zh", "gyf", "k6"],
            ["mv", "rb*", "mf"],
            ["hv", "zh", "tb*", "mf"],
            "halal"
        ],


        mgc.CHEST:
        [
            "nincs hatrany",
            ["gyv", "zh", "mf"],
            ["mv", "jh", "mf"],
            ["hv", "vh", "hf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["mv", "zh", "mf"],
            ["mv", "jh", "hf", "beteg"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["zh", "gyf"],
            ["gyv", "rb*", "mf"],
            ["mv", "jh", "rb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", "gyf", "k6"],
            ["mv", "zh", "mf"],
            ["mv", "beteg", "jh", "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", "gyf", "k6"],
            ["mv", "zh", "mf"],
            ["mv", "beteg", "jh", "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", "gyf", "80%"],
            ["gyv", "zh", "mf", "50%"],
            ["mv", "zh", "tb*", "mf", "20%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["mv", "zh", "gyf", "k6"],
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
            ["gyv", "zh*", "gyf", "k6"],
            ["mv", "rb*", "gyf", "k6"],
            ["hv", "zh", "tb*", "mf"],
            "halal"
        ],


        mgc.CHEST:
        [
            "nincs hatrany",
            ["zh", "gyf", "k6"],
            ["gyv(b)", "jh", "mf", "beteg"],
            ["mv(b)", "vh", "hf", "beteg"],
            "halal"
        ],
        mgc.STOMACH:
        [
            "nincs hatrany",
            ["gyv", "zh", "k6"],
            ["gyv(b)", "jh", "mf", "k6", "beteg"],
            ["mv(b)", "vh", "hf"],
            "halal"
        ],
        mgc.SHOULDERBLADE:
        [
            "nincs hatrany",
            ["gyv", "zh*", "gyf", "k6"],
            ["mv", "rb*", "gyf", "k6"],
            ["hv", "zh", "tb*", "mf"],
            "halal"
        ],
        mgc.BACK:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["gyv(b)", "beteg", "jh", "mf", "k6"],
            ["mv(b)", "beteg", "vh", "hf"],
            "halal"
        ],
        mgc.WAIST:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["gyv(b)", "beteg", "jh", "mf", "k6"],
            ["mv(b)", "beteg", "vh", "hf"],
            "halal"
        ],

        mgc.BUTTOCKS:
        [
            "nincs hatrany",
            ["gyv", "zh", "k6", "70%"],
            ["gyv", "jh", "mf", "60%"],
            ["mv", "zh", "tb*", "mf", "10%"],
            "halal"
        ],
        mgc.SPINE:
        [
            "nincs hatrany",
            ["ervenytelen", "ujradobas"],
            ["gyv(b)", "jh", "mf", "k6"],
            ["mv(b)", "beteg", "jh", "rb**", "hf"],
            "halal"
        ]

    }
}
