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

CSS_LINK = '<link rel=\"stylesheet\" type=\"text/css\" href=\"tables.css\">'
JS_LINK = '<script src=\"collapse.js\" type=\"text/javascript\"></script>'


def add_attributes(**attr):
    """
    Generator that iterates through all attributes
    and yields them formatted as HTML attributes.
        - attr:
            A Python dict. The function formats
            them as HTML attributes.
    """
    while attr:
        key = list(attr.keys())[0]
        value = attr[key]
        yield '{}=\"{}\"'.format(key, value)
        del attr[key]


def tag_builder(tag, **attr):
    """
    Creates the start tag for an element.
        - tag:
            The name of the HTML element. E.g. 'div' or 'table'.
        - attr:
            A Python dict with the attributes of the HTML element.
            E.g. {'style': 'color:red;', 'colspan:3}
    """

    # Since 'class' is a Python key word, use 'klass' instead.
    if 'klass' in attr.keys():
        class_value = attr.pop('klass')
        attr['class'] = class_value

    attr_generator = add_attributes(**attr)

    return '<{} {}>'.format(tag, ' '.join(attr_generator))


def html_wrapper(tag, **attr):
    """
    HTML wrapper. Wraps the content in start and
    end tags. The tags are built using the 'tag' and 'attr' arguments.

        - tag:
            The tag of the HTML element. E.g. 'div' or 'td'.
        - attr:
            A Python dict with the attributes of the HTML element.
            E.g. {'style': 'color:red;', 'colspan:3}
    """
    def real_decorator(fun):
        """
        Inner wrapper. It modifies the decorated function.
            - fun:
                The function being wrapped.
        """

        def wrapper(html_writer, *args, **kwargs):
            """
            Calls the actual function.
                - html_writer:
                    A co-routine all funs use to write the HTML file.
                - args:
                    Other positional arguments of the decorated function.
                - kwargs:
                    Other keyword arguments of the decorated function.
                    They can be used to override or extend the HTML attributes
                    defined on the wrapper.
            """
            # Calculate all attributes for HTML tag
            for key, value in kwargs.items():
                attr[key] = value

            start_tag = tag_builder(tag, **attr)

            # Write HTML start tag.
            html_writer.send(start_tag)

            # Invoke actual function to write content of HTML element.
            try:
                fun(html_writer, *args, **kwargs)

            # Close element with HTML end tag.
            finally:
                html_writer.send('</{}>'.format(tag))
        return wrapper

    return real_decorator


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


@html_wrapper('button', onclick='collapse(this)')
def create_button(html_writer, button_text, **_attr):
    """
    Creates a button element.
        - html_writer:
            A co-routine all funs use to write the HTML file.
        - button_text:
            The label of the button.
        - _attr:
            Any additional attributes for the button.

    The decorator writes the start and end tags of the button,
    and adds the onclick attribute to the start tag.
    """
    html_writer.send(button_text)


@html_wrapper('td')
def create_header_cell(html_writer, header_text, **_attr):
    """
    Creates a cell in the first row of the table.
     - html_writer:
            A co-routine all funs use to write the HTML file.
    - header_text:
        The text content of the cell.
    - _attr:
        Optional HTML arguments.
    """
    html_writer.send(header_text)
    create_button(html_writer, '<')


@html_wrapper('tr')
def create_header_row(html_writer, first_cells, **_attr):
    """
    Creates the first row of a penalty table.
    The row comprises an empty cell, and the weapon types,
    each having a colspan of 3 (one per penalty rank).
    """
    create_cell(html_writer, '')

    for cell_header, penalties in first_cells:
        create_header_cell(html_writer, cell_header, colspan=len(penalties))


@html_wrapper('td')
def create_cell(html_writer, cell_text, **_attr):
    """
    Creates a simple penalty cell in the table.
    - html_writer:
        A co-routine all funs use to write the HTML file.
    - cell_text:
        The penalty content of the cell.
    - _attr:
        Optional HTML arguments.
    """
    html_writer.send(cell_text)


@html_wrapper('tr')
def create_penalty_row(html_writer, body_part, cells, **_attr):
    """
    Writes a table row, where the first cell is the
    body part, the remaining cells contain the penalties.
    """
    create_cell(html_writer, body_part)

    for _cell_header, penalties in cells:
        for penalty in penalties:
            create_cell(html_writer, penalty)


@html_wrapper('table')
def create_table(html_writer, table, caption, **_attr):
    """
    Creates an HTML table using a generator that yields
    the cell content and the headers.
    """
    weapon_types = list(table.keys())
    body_parts = list(table[weapon_types[0]].keys())

    # Start generator.
    row_content = row_content_generator(table, weapon_types, body_parts)

    # Start HTML table, give it a title.
    html_writer.send('<caption>{}</caption>'.format(caption))

    first_body_part, first_cells = next(row_content)

    create_header_row(html_writer, first_cells)
    create_penalty_row(html_writer, first_body_part, first_cells)

    # Iterate through rest of the penalty cells and bodyparts.
    for body_part, cells in row_content:
        create_penalty_row(html_writer, body_part, cells)


@html_wrapper('head')
def write_head(html_writer, **_attr):
    """
    Creates the header of the HTML file.
    """
    # Link CSS file and JavaScript.
    html_writer.send(CSS_LINK)
    html_writer.send(JS_LINK)


@html_wrapper('body')
def write_body(html_writer, target_dicts, **_attr):
    """
    Writes the HTML tables into the HTML file.
    - html_writer:
        A co-routine all funs use to write the HTML file.
    - target_dicts:
        A list of tuples, where each tuple comprises:
            - A penalty dictionary
            - A caption for the table
    - _attr:
        Optional HTML arguments.
    """
    table_no = 1
    for table, caption in target_dicts:
        caption = 'Tablazat {}: {}'.format(
            table_no, caption)

        create_table(html_writer, table, caption)
        table_no += 1


@html_wrapper('html')
def process_target_dicts(html_writer, target_dicts, **_attr):
    """
    Builds an HTML page from the supplied penalty
    dictionaries.

    Returns the constructed HTML string.
    """
    write_head(html_writer)
    write_body(html_writer, target_dicts)


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


def writer(log_file_handle):
    """
    A co-routine that writes what it receives to a file.
        - log_file_handle:
            A handle to the file the co-routine writes to.
            The file must be opened in append mode.
    """
    while True:
        to_write = (yield)
        log_file_handle.write(to_write)


def start_html_page(path_to_html):
    """
    Creates the specified file or wipes its content if
    it already exists.
    Starts a co-routine that writes to this file, and sends the
    co-routine the current time.
    Returns the co-routine instance and a handle to
    the opened file.
    """
    # Create/wipe content of file.
    open(path_to_html, 'w').close()

    # Open file in append mode.
    html_handle = open(path_to_html, 'a')

    # Create and start co-routine.
    html_writer = writer(html_handle)
    html_writer.send(None)
    html_writer.send('<!DOCTYPE html>')

    # Return the co-routine and the file handle.
    return html_writer, html_handle


def transform_html(path_to_html):
    """
    Create the HTML file and write its content.
    """
    html_writer, html_handle = start_html_page(path_to_html)
    try:
        process_target_dicts(html_writer, TARGET_DICTS)

    finally:
        html_writer.close()
        html_handle.close()


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
        transform_html(HTML_PATH)

    return 'file://{}'.format(HTML_PATH)
