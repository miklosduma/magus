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
    [SKULL, FOREHEAD],[SKULL, TEMPLES],
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
    [CHEST, BREASTBONE],[CHEST, HEART],
    [CHEST, LUNGS], [STOMACH, CARDIA],
    [STOMACH, CARDIA], [STOMACH, STOMACH],
    [STOMACH, STOMACH], [STOMACH, GROINS]]]

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

LTHIGH = 'Jcomb'
LKNEE = 'Jterd'
LSHIN = 'Jlabszar'
LANKLE = 'Jboka'
LFOOT = 'Jlabfej'

LLEG_LIST = [LLEG, [
    [LLEG, LTHIGH], [LLEG, LTHIGH],
    [LLEG, LTHIGH], [LLEG, LTHIGH],
    [LLEG, LTHIGH], [LLEG, LKNEE],
    [LLEG, LSHIN], [LLEG, LSHIN],
    [LLEG, LANKLE], [LLEG, LFOOT]
]]

