import random


BODY_PARTS = {
    'Jlab': [
        ('Jlab', 'Jcomb', 5),
        ('Jlab', 'Jterd', 1),
        ('Jlab', 'Jlabszar', 2),
        ('Jlab', 'Jboka', 1),
        ('Jlab', 'Jlabfej', 1)],
    'Blab': [
        ('Blab', 'Bcomb', 5),
        ('Blab', 'Bterd', 1),
        ('Blab', 'Blabszar', 2),
        ('Blab', 'Bboka', 1),
        ('Blab', 'Blabfej', 1)],
    'Jkez': [
        ('Jkez', 'Jvall', 3),
        ('Jkez', 'Jfelkar', 2),
        ('Jkez', 'Jkonyok', 1),
        ('Jkez', 'Jalkar', 2),
        ('Jkez', 'Jcsuklo', 1),
        ('Jkez', 'Jkezfej', 1)],
    'Bkez': [
        ('Bkez', 'Bvall', 3),
        ('Bkez', 'Bfelkar', 2),
        ('Bkez', 'Bkonyok', 1),
        ('Bkez', 'Balkar', 2),
        ('Bkez', 'Bcsuklo', 1),
        ('Bkez', 'Bkezfej', 1)],
    'Torzs' : [
        ('Kulcscsont', 'Jkulcs', 1),
        ('Kulcscsont', 'Bkulcs', 1),
        ('Mellkas', 'Szegycsont', 1),
        ('Mellkas', 'Sziv', 1),
        ('Mellkas', 'Tudo', 1),
        ('Has', 'Gyomorszaj', 2),
        ('Has', 'Has', 2),
        ('Has', 'Agyek', 1)],
    'Fej': [
        ('Koponya', 'Koponya', 3),
        ('Koponya', 'Homlok', 2),
        ('Koponya', 'Halantek', 1),
        ('Arc', 'Arc', 2),
        ('Nyak', 'Nyak', 2)]
}


def add_n_times_to_list(elem, n, candidates=None):
    """
    Adds a given value 'n' times to the
    specified list.
    """
    if not candidates:
        candidates = [elem]

    count = candidates.count(elem)

    while count < n:
        candidates.append(elem)
        random.shuffle(candidates)
        count = candidates.count(elem)

    return candidates


def build_main_table():
    """
    Adds all main body part tables to a list a specified number of times.

    E.g. Fej must be in the list once, Torzs four times and Vegtag 5 times.
    """
    main_table = add_n_times_to_list('Torzs',4)
    main_table = add_n_times_to_list('Fej',1,candidates=main_table)
    main_table = add_n_times_to_list('Jkez',2,candidates=main_table)
    main_table = add_n_times_to_list('Bkez', 1, candidates=main_table)
    main_table = add_n_times_to_list('Jlab', 1, candidates=main_table)
    main_table = add_n_times_to_list('Blab', 1, candidates=main_table)
    return main_table


def get_sub_parts(main_part):
    """
    Adds all sub parts for a specified main body part.
    The number of times the sub parts are to be added are
    specified in their specific map.

    Each sub-part comprises the name of the part that gets
    selected from the penalty table and the name of the part
    that is checked for SFE.
    """
    sub_parts = []
    for penalty_part, sfe_part, n in BODY_PARTS[main_part]:
        elem = (penalty_part, sfe_part)
        sub_parts = add_n_times_to_list(elem, n, candidates=sub_parts)

    return sub_parts


def pick_sub_parts(main_part=None):
    """
    Returns a randomly chosen sub-body part.
    """
    if main_part:
        body_part = main_part
    else:
        main_parts = build_main_table()
        body_part = random.choice(main_parts)

    sub_parts = get_sub_parts(body_part)
    return random.choice(sub_parts)
