from magus_kalkulator.random_body import pick_sub_parts


def test_pick_sub_parts():
    """
    Tests sub part selection.
    Expects a tuple.
    """
    body_part, pen_part, sfe_part = pick_sub_parts()
    assert all(isinstance(x, str) for x in (body_part, pen_part, sfe_part))


def test_pick_sub_parts_specific():
    """
    Tests sub part selection.
    Expects a tuple.
    """
    body_part, pen_part, sfe_part = pick_sub_parts(main_part='Jkez')
    assert all(isinstance(x, str) for x in (body_part, pen_part, sfe_part))
    assert pen_part == body_part == 'Jkez'
    assert  sfe_part in ['Jfelkar', 'Jkonyok', 'Jalkar', 'Jcsuklo', 'Jkezfej',
                         'Jvall']