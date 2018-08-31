"""
Utility function that creates an HTML page from the penalty dicts
(e.g. head_table.py).

Each penalty dict becomes an HTML table. The dicts look like:

Weapon type:
    body part:
        level1_penalties
        level2_penalties

    body part2:
        level1_penalties
        level2_penalties

Weapon type2:
    body_part:
        level1_penalties
        level2_penalties

    body_part2:
        level1_penalties
        level2_penalties

The output HTML tables look like:
           |Weapon type  |Weapon type2 |
|body part |l1_pen|l2_pen|l1_pen|l2_pen|
|body part2|l1_pen|l2_pen|l1_pen|l2_pen|
"""

from yattag import Doc

from magus_kalkulator.interface_elements import get_relative_dir


HTML_PATH = get_relative_dir('resources/index.html')


def create_rows(target_dict, weapon_types, body_parts):
    """
    Generator that yields row content for an HTML table.
        - target_dict:
            One of the penalty tables.

    """

    while body_parts:
        body = body_parts[0]
        cells = []

        for wtype in weapon_types:
            cell_header = wtype

            penalties = [', '.join(penalty)
                         if isinstance(penalty, list)
                         else penalty for penalty
                         in target_dict[wtype][body][1:-1]]

            cells.append((cell_header, penalties))
        yield body, cells
        del body_parts[0]


def process_target_dicts(target_dicts):
    """
    Builds an HTML page from the supplied penalty
    dictionaries.

    Returns the constructed HTML string.
    """
    doc, tag, text, line = Doc().ttl()
    doc.asis('<!DOCTYPE html>')

    with tag('html', 'magus tables'):
        with tag('head', 'styles'):
            line('link', '', rel='stylesheet', href='tables.css')

        with tag('body', 'magus body'):
            line('script', '', type='text/javascript', src='collapse.js')

            table_no = 1
            for table, caption in target_dicts:

                weapon_types = list(table.keys())
                body_parts = list(table[weapon_types[0]].keys())
                row_creater = create_rows(table, weapon_types, body_parts)

                with tag('table'):
                    line('caption', 'Tablazat {}: {}'.format(
                        table_no, caption))

                    header_added = False
                    for body_part, cells in row_creater:

                        if not header_added:
                            with tag('tr'):
                                line('td', '')

                                for cell_header, penalties in cells:
                                    with tag('td', cell_header,
                                             colspan=len(penalties)):
                                        text(cell_header)
                                        line('button', '<',
                                             onclick='collapse(this)')
                            header_added = True

                        with tag('tr'):
                            line('td', body_part, klass='bodypart')

                            for cell_header, penalties in cells:
                                penalty_no = 1
                                for penalty in penalties:
                                    line('td', penalty, id='{}_{}'.format(
                                        cell_header, penalty_no))
                                    penalty_no += 1
                table_no += 1

        return doc.getvalue()


def target_dicts_to_html(target_dicts):
    """
    Transforms 'target_dicts' to HTML, writes
    the result into file, and returns the
    path to the file appended with the 'file://' protocol.
    """
    html_content = process_target_dicts(target_dicts)
    with open(HTML_PATH, 'w') as index:
        index.write(html_content)
    return 'file://{}'.format(HTML_PATH)
