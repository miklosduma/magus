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
import os

from yattag import Doc

from magus_kalkulator.interface_elements import get_relative_dir
from magus_kalkulator import head_table
from magus_kalkulator import torso_table
from magus_kalkulator import limbs_table


HTML_PATH = get_relative_dir('resources/index.html')

TARGET_DICT_PATHS = [os.path.abspath(head_table.__file__),
                     os.path.abspath(torso_table.__file__),
                     os.path.abspath(limbs_table.__file__)]

TARGET_DICTS = [
    (head_table.FEJ_TABLA, 'Fej'),
    (limbs_table.VEGTAG_TABLA, 'Vegtagok'),
    (torso_table.TORZS_TABLA, 'Torzs')]


def row_content_generator(target_dict, weapon_types, body_parts):
    """
    Generator that yields row content for an HTML table.
        - target_dict:
            One of the penalty tables.

    """
    while body_parts:
        body = body_parts[0]
        cells = []

        for wtype in weapon_types:

            penalties = [', '.join(penalty)
                         if isinstance(penalty, list)
                         else penalty for penalty
                         in target_dict[wtype][body][1:-1]]

            cells.append((wtype, penalties))
        yield body, cells
        del body_parts[0]


def create_header_row(tag, line, text, first_cells):
    """
    Creates the first row of a penalty table.
    The row comprises an empty cell, and the weapon types,
    each having a colspan of 3 (one per penalty rank).
    """
    with tag('tr'):
        line('td', '')

        for cell_header, penalties in first_cells:
            with tag('td', cell_header,
                     colspan=len(penalties)):
                text(cell_header)
                line('button', '<',
                     onclick='collapse(this)')


def create_penalty_row(tag, line, body_part, cells):
    """
    Writes a table row, where the first cell is the
    body part, the remaining cells contain the penalties.
    """
    with tag('tr'):
        line('td', body_part)

        for _cell_header, penalties in cells:
            for penalty in penalties:
                line('td', penalty)


def create_table(table, caption, tag, line, text):
    """
    Creates an HTML table using a generator that yields
    the cell content and the headers.
    """
    weapon_types = list(table.keys())
    body_parts = list(table[weapon_types[0]].keys())

    # Start generator.
    row_content = row_content_generator(table, weapon_types, body_parts)

    # Start HTML table, give it a title.
    with tag('table'):
        line('caption', caption)

        # Use first yield from generator to fill header row besides writing
        # a penalty row.
        first_body_part, first_cells = next(row_content)

        create_header_row(tag, line, text, first_cells)
        create_penalty_row(tag, line, first_body_part, first_cells)

        # Iterate through rest of the penalty cells and bodyparts.
        for body_part, cells in row_content:
            create_penalty_row(tag, line, body_part, cells)


def process_target_dicts(target_dicts):
    """
    Builds an HTML page from the supplied penalty
    dictionaries.

    Returns the constructed HTML string.
    """

    # Create yattag HTML instances.
    doc, tag, text, line = Doc().ttl()

    # Create doc type declaration.
    doc.asis('<!DOCTYPE html>')

    with tag('html', 'magus tables'):

        # Reference CSS and JavaScript.
        with tag('head', 'styles'):
            line('link', '', rel='stylesheet', href='tables.css')

        with tag('body', 'magus body'):
            line('script', '', type='text/javascript', src='collapse.js')

            # Create HTML Tables.
            table_no = 1
            for table, caption in target_dicts:
                caption = 'Tablazat {}: {}'.format(
                    table_no, caption)

                create_table(table, caption, tag, line, text)
                table_no += 1

        return doc.getvalue()


def get_latest_mod(src_file):
    """
    Gets the last modification date of
    the specified file.
    """
    # Get date of latest modification
    stats = os.stat(src_file)
    latest_mod = stats[8]
    return latest_mod


def any_change_to_target_dicts(html_file, target_modules):
    """
    Checks whether any of the target dict files
    (e.g. head_table.py) was changed after the
    creation of the HTML page.

    Returns either:
        - True:
            One of the target dicts was modified
            after the creation of the page or
            the page has not been created.
        - False:
            The page is created and up-to-date with
            the target dict files.
    """
    try:
        html_ch_date = get_latest_mod(html_file)

    # Return True if the HTML page has not been created.
    except FileNotFoundError:
        return True

    target_dict_ch_dates = [get_latest_mod(target_module)
                            for target_module in target_modules]

    # Check if any target dict file was modified after the page.
    true_or_false = any(target_ch_date > html_ch_date
                        for target_ch_date in target_dict_ch_dates)

    return true_or_false


def target_dicts_to_html():
    """
    Transforms all target_dict files to HTML, writes
    the result into file, and returns the
    path to the file appended with the 'file://' protocol.

    If the HTML page has already been created, and none of the
    target dict files changed after it, the function simply
    returns the path to the HTML file.
    """
    if any_change_to_target_dicts(HTML_PATH, TARGET_DICT_PATHS):
        html_content = process_target_dicts(TARGET_DICTS)

        with open(HTML_PATH, 'w') as index:
            index.write(html_content)

    return 'file://{}'.format(HTML_PATH)
