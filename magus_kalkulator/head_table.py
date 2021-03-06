"""
Table containing all penalties per weapon-type/seriousness/hit target.
"""

import magus_kalkulator.magus_constants as mgc

FEJ_THRESHOLDS = [75, 50, 34, 17]


FEJ_TABLA = {
    mgc.SLASH: {
        mgc.FACE: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN,
             mgc.EXTRA_K6],

            [mgc.MODERATE_BLEEDING,
             mgc.SEVERE_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.CRITICAL_HANDICAP,
             mgc.SEVERE_PAIN],

            mgc.DEATH],

        mgc.NECK: [
            mgc.NULL_HANDICAP,

            [mgc.MODERATE_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.SEVERE_BLEEDING,
             mgc.CRITICAL_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.SEVERE_BLEEDING,
             mgc.NUMBNESS,
             mgc.MODERATE_PAIN],

            mgc.DEATH],

        mgc.SKULL: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.MODERATE_BLEEDING,
             mgc.SEVERE_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.FAINTING],

            mgc.DEATH]},

    mgc.THRUST: {
        mgc.FACE: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.SLIGHT_BLEEDING,
             mgc.SEVERE_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.SLIGHT_BLEEDING_INT,
             mgc.CRITICAL_HANDICAP,
             mgc.SEVERE_PAIN],

            mgc.DEATH],

        mgc.NECK: [
            mgc.NULL_HANDICAP,

            [mgc.MODERATE_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.EXTRA_K6],

            [mgc.MODERATE_BLEEDING,
             mgc.SEVERE_HANDICAP],

            [mgc.SEVERE_BLEEDING,
             mgc.NUMBNESS],

            mgc.DEATH],

        mgc.SKULL: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.SLIGHT_BLEEDING,
             mgc.SEVERE_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.CRITICAL_HANDICAP,
             mgc.SEVERE_PAIN],

            mgc.DEATH]},

    mgc.BLUDGEON: {
        mgc.FACE: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SEVERE_HANDICAP,
             mgc.MODERATE_PAIN,
             mgc.EXTRA_K6],

            [mgc.SLIGHT_BLEEDING,
             mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.FAINTING],

            mgc.DEATH],

        mgc.NECK: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_HANDICAP,
             mgc.NAUSEA],

            [mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.CRITICAL_HANDICAP,
             mgc.MODERATE_PAIN],

            mgc.DEATH],

        mgc.SKULL: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN],

            [mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.FAINTING],

            mgc.DEATH]},

    mgc.CLAW: {
        mgc.FACE: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SEVERE_HANDICAP,
             mgc.MODERATE_PAIN,
             mgc.EXTRA_K6],

            [mgc.MODERATE_BLEEDING,
             mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.FAINTING],

            mgc.DEATH],

        mgc.NECK: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.MODERATE_BLEEDING,
             mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.SEVERE_BLEEDING,
             mgc.NUMBNESS,
             mgc.SEVERE_PAIN],

            mgc.DEATH],

        mgc.SKULL: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.SLIGHT_BLEEDING,
             mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.FAINTING],

            mgc.DEATH]},

    mgc.BITE: {
        mgc.FACE: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN,
             mgc.EXTRA_K6],

            [mgc.SLIGHT_BLEEDING,
             mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING,
             mgc.CRITICAL_HANDICAP,
             mgc.SEVERE_PAIN],

            mgc.DEATH],

        mgc.NECK: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.MODERATE_BLEEDING,
             mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.SEVERE_BLEEDING,
             mgc.NUMBNESS,
             mgc.MODERATE_PAIN],

            mgc.DEATH],

        mgc.SKULL: [
            mgc.NULL_HANDICAP,

            [mgc.SLIGHT_BLEEDING,
             mgc.SLIGHT_HANDICAP,
             mgc.SLIGHT_PAIN,
             mgc.EXTRA_K6],

            [mgc.SLIGHT_BLEEDING,
             mgc.DAZE,
             mgc.SLIGHT_HANDICAP,
             mgc.MODERATE_PAIN],

            [mgc.MODERATE_BLEEDING_INT,
             mgc.FAINTING],

            mgc.DEATH]}
}
