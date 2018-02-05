import magus_kalkulator.magus_constants as mgc

FEJ_THRESHOLDS = [75, 50, 34, 17]


FEJ_TABLA = {
    mgc.SLASH:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", "zh", "mf", "k6"],
            ["mv", "jh", "mf"],
            ["mv(b)", "vh", "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["mv", "zh", "gyf", "k6"],
            ["hv", "vh", "mf"],
            ["hv", "tb", "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["mv", "jh", "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    },
    mgc.THRUST:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["gyv", "jh", "mf"],
            ["gyv(b)", "vh", "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["mv", "zh", "k6"],
            ["mv", "jh"],
            ["hv", "tb"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["gyv", "jh", "mf"],
            ["mv(b)", "vh", "hf"],
            "halal"
        ]
    },

    mgc.BLUDGEON:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", "jh", "mf", "k6"],
            ["gyv", "kabulat", "zh", "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["zh", "rosszullet"],
            ["kabulat", "zh", "mf"],
            ["mv(b)", "vh", "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["zh", "gyf"],
            ["kabulat", "zh", "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    },
    mgc.CLAW:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", "jh", "mf", "k6"],
            ["mv", "kabulat", "zh", "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["mv", "kabulat", "zh", "mf"],
            ["hv", "tb", "hf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["gyv", "kabulat", "zh", "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    },
    mgc.BITE:
    {
        mgc.FACE:
        [
            "nincs hatrany",
            ["gyv", "zh", "mf", "k6"],
            ["gyv", "kabulat", "zh", "mf"],
            ["mv", "vh", "hf"],
            "halal"
        ],
        mgc.NECK:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["mv", "kabulat", "zh", "mf"],
            ["hv", "tb", "mf"],
            "halal"
        ],
        mgc.SKULL:
        [
            "nincs hatrany",
            ["gyv", "zh", "gyf", "k6"],
            ["gyv", "kabulat", "zh", "mf"],
            ["mv(b)", "ajulas"],
            "halal"
        ]
    }
}
