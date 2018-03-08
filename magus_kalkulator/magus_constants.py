"""
Generic constants.
"""

# Head parts
HEAD = 'Fej'

SKULL = 'Koponya'
FACE = 'Arc'
NECK = 'Nyak'
FOREHEAD = 'Homlok'
TEMPLES = 'Halantek'

HEAD_LIST = [HEAD, [
    [SKULL, SKULL], [SKULL, SKULL],
    [SKULL, SKULL], [SKULL, FOREHEAD],
    [SKULL, FOREHEAD], [SKULL, TEMPLES],
    [FACE, FACE], [FACE, FACE],
    [NECK, NECK], [NECK, NECK]]]

# Torso parts
TORSO = 'Torzs'

COLLARBONE = 'Kulcscsont'
RCOLLARBONE = 'Jkulcs'
LCOLLARBONE = 'Bkulcs'
CHEST = 'Mellkas'
LUNGS = 'Tudo'
BREASTBONE = 'Szegycsont'
HEART = 'Sziv'
STOMACH = 'Has'
CARDIA = 'Gyomorszaj'
GROINS = 'Agyek'

TORSO_LIST = [TORSO, [
    [COLLARBONE, RCOLLARBONE], [COLLARBONE, LCOLLARBONE],
    [CHEST, BREASTBONE], [CHEST, HEART],
    [CHEST, LUNGS], [STOMACH, CARDIA],
    [STOMACH, CARDIA], [STOMACH, STOMACH],
    [STOMACH, STOMACH], [STOMACH, GROINS]]]

# Torso parts from behind
SHOULDERBLADE = 'Lapocka'
RSHOULDERBLADE = 'Jlapocka'
LSHOULDERBLADE = 'Blapocka'
BACK = 'Hat'
RBACK = 'Jhat'
LBACK = 'Bhat'
WAIST = 'Derek'
RWAIST = 'Jobb derek'
LWAIST = 'Bderek'
BUTTOCKS = 'Ulep'
RBUTTOCKS = 'Julep'
LBUTTOCKS = 'Bulep'
SPINE = 'Gerinc'
SPINE_UPPER = 'Also gerinc'
SPINE_LOWER = 'Felso gerinc'

TORSO_LIST_BEHIND = [TORSO, [
    [SHOULDERBLADE, RSHOULDERBLADE], [SHOULDERBLADE, LSHOULDERBLADE],
    [BACK, RBACK], [BACK, LBACK],
    [WAIST, RWAIST], [WAIST, LWAIST],
    [BUTTOCKS, RBUTTOCKS], [BUTTOCKS, LBUTTOCKS],
    [SPINE, SPINE_UPPER], [SPINE, SPINE_LOWER]
]]

# Right arm parts
RARM = 'Jkez'
RSHOULDSERS = 'Jvall'
RUPPERARM = 'Jfelkar'
RELBOW = 'Jkonyok'
RLOWERARM = 'Jalkar'
RWRIST = 'Jcsuklo'
RHAND = 'Jkezfej'

RARM_LIST = [RARM, [
    [RARM, RSHOULDSERS], [RARM, RSHOULDSERS],
    [RARM, RSHOULDSERS], [RARM, RUPPERARM],
    [RARM, RUPPERARM], [RARM, RELBOW],
    [RARM, RLOWERARM], [RARM, RLOWERARM],
    [RARM, RWRIST], [RARM, RHAND]]]

# Left arm parts
LARM = 'Bkez'
LSHOULDSERS = 'Bvall'
LUPPERARM = 'Bfelkar'
LELBOW = 'Bkonyok'
LLOWERARM = 'Balkar'
LWRIST = 'Bcsuklo'
LHAND = 'Bkezfej'

LARM_LIST = [LARM, [
    [LARM, LSHOULDSERS], [LARM, LSHOULDSERS],
    [LARM, LSHOULDSERS], [LARM, LUPPERARM],
    [LARM, LUPPERARM], [LARM, LELBOW],
    [LARM, LLOWERARM], [LARM, LLOWERARM],
    [LARM, LWRIST], [LARM, LHAND]]]

# Right leg parts
RLEG = 'Jlab'
RTHIGH = 'Jcomb'
RKNEE = 'Jterd'
RSHIN = 'Jlabszar'
RANKLE = 'Jboka'
RFOOT = 'Jlabfej'

RLEG_LIST = [RLEG, [
    [RLEG, RTHIGH], [RLEG, RTHIGH],
    [RLEG, RTHIGH], [RLEG, RTHIGH],
    [RLEG, RTHIGH], [RLEG, RKNEE],
    [RLEG, RSHIN], [RLEG, RSHIN],
    [RLEG, RANKLE], [RLEG, RFOOT]
]]

# Left leg parts
LLEG = 'Blab'

LTHIGH = 'Bcomb'
LKNEE = 'Bterd'
LSHIN = 'Blabszar'
LANKLE = 'Bboka'
LFOOT = 'Blabfej'

LLEG_LIST = [LLEG, [
    [LLEG, LTHIGH], [LLEG, LTHIGH],
    [LLEG, LTHIGH], [LLEG, LTHIGH],
    [LLEG, LTHIGH], [LLEG, LKNEE],
    [LLEG, LSHIN], [LLEG, LSHIN],
    [LLEG, LANKLE], [LLEG, LFOOT]
]]

# Weapon types
THRUST = 'Szuras'
SLASH = 'Vagas'
BLUDGEON = 'Zuzas'
BITE = 'Harapas'
CLAW = 'Karmolas'

# Penalties
HANDICAP = 'Hatrany'
NULL_HANDICAP = 'Nincs hatrany'
SLIGHT_HANDICAP = 'Zavaro hatrany'
SLIGHT_HANDICAP_1 = 'Zavaro hatrany az adott oldalon'
SEVERE_HANDICAP = 'Jelentos hatrany'
SEVERE_HANDICAP_1 = 'Jelentos hatrany az adott oldalon'
CRITICAL_HANDICAP = 'Vegzetes hatrany'
PARTIAL_NUMBNESS = 'Reszleges benulas'
PARTIAL_NUMBNESS_1 = 'Reszleges benulas az adott oldalon'
NUMBNESS = 'Teljes benulas'
NUMBNESS_1 = 'Teljes benulas az adott oldalon'

# Bleeding
SLIGHT_BLEEDING = 'Gyenge verzes'
SLIGHT_BLEEDING_INT = 'Gyenge belso verzes'
MODERATE_BLEEDING = 'Mersekelt verzes'
MODERATE_BLEEDING_INT = 'Mersekelt belso verzes'
SEVERE_BLEEDING = 'Heves verzes'
SEVERE_BLEEDING_INT = 'Heves belso verzes'

# Pain
SLIGHT_PAIN = 'Gyenge fajdalom'
MODERATE_PAIN = 'Mersekelt fajdalom'
SEVERE_PAIN = 'Heves fajdalom'
