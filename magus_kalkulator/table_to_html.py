import os
from yattag import Doc


def create_table(table, weapon_types, body_parts):

    while body_parts:
        body = body_parts[0]
        cells = []

        for wtype in weapon_types:
            cell_header = wtype

            penalties = [', '.join(penalty)
                         if isinstance(penalty, list)
                         else penalty for penalty in table[wtype][body][1:-1]]

            cells.append((cell_header, penalties))
        yield body, cells
        del body_parts[0]


def process_tables(tables):
    doc, tag, text, line = Doc().ttl()
    doc.asis('<!DOCTYPE html>')

    with tag('html', 'magus tables'):
        with tag('head', 'styles'):
            line('link', '', rel='stylesheet', href='tables.css')

        with tag('body', 'magus body'):
            line('script', '', type='text/javascript', src='collapse.js')

            table_no = 1
            for table, caption in tables:

                weapon_types = list(table.keys())
                body_parts = list(table[weapon_types[0]].keys())
                table_handler = create_table(table, weapon_types, body_parts)

                with tag('table'):
                    line('caption', 'Tablazat {}: {}'.format(table_no, caption))

                    header_added = False
                    for body_part, cells in table_handler:

                        if not header_added:
                            with tag('tr'):
                                line('td', '')

                                for cell_header, penalties in cells:
                                    with tag('td', cell_header,
                                         colspan=len(penalties), klass='wtype'):
                                        text(cell_header)
                                        line('button', '<', onclick='collapse(this)')
                            header_added = True

                        with tag('tr'):
                            line('td', body_part, klass='bodypart')

                            for cell_header, penalties in cells:
                                penalty_no = 1
                                for penalty in penalties:
                                    line('td', penalty, id='{}_{}'.format(cell_header, penalty_no))
                                    penalty_no += 1
                table_no += 1

        return doc.getvalue()


def tables_to_html(tables):
    full_path, _rest = os.path.dirname(__file__).split('magus_kalkulator')
    html_file = os.path.join(full_path,
                             'resources/index.html')
    html_content = process_tables(tables)
    with open(html_file, 'w') as index:
        index.write(html_content)
    return 'file://{}'.format(html_file)
