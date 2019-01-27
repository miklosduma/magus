from tkinter import Canvas, font


MESSAGE_BOX_COLOUR = "#F0FFF0"


def coroutine(canvas):
    my_font = '{} {}'.format(
        canvas.font_font.cget('family'),
        canvas.font_font.cget('size'))

    while True:
        (char, x, y) = yield
        canvas.configure(scrollregion=(0, 0, x, y))
        canvas.create_text(
            x, y, font=my_font, text=char, width=canvas.width, anchor='se')


def write_list(value_list, canvas, y, spaces):
    for elem in value_list:
        y += canvas.get_text_height()
        x = canvas.start_coords[0] + canvas.get_text_width(elem)

        for _n in range(0, spaces + 4):
            x += canvas.get_text_width(' ')

        canvas.coroutine.send((elem, x, y))
    return y


def write_value(canvas, value, y, spaces, key_text):
    if isinstance(value, dict):
        y += canvas.get_text_height()
        return write_dict(canvas, value, y=y, spaces=spaces + 4)

    elif isinstance(value, list):
        return write_list(value, canvas, y, spaces)

    else:
        x = canvas.start_coords[0]

        for _n in range(0, spaces + 1):
            x += canvas.get_text_width(' ')

        for text in key_text, value:
            x += canvas.get_text_width(text)

        canvas.coroutine.send((value, x, y))
        return y


def write_dict(canvas, value_dict, y=None, spaces=0):
    if not y:
        y = canvas.start_coords[1]

    for key, value in value_dict.items():
        key_text = '{}:'.format(key)
        x = canvas.start_coords[0] + canvas.get_text_width(key_text)

        if spaces:
            for _n in range(0, spaces):
                x += canvas.get_text_width(' ')

        canvas.coroutine.send((key_text, x, y))
        y = write_value(canvas, value, y, spaces, key_text)

        y += canvas.get_text_height()

    return y


class MagusCanvas(Canvas):
    def __init__(self, root):
        Canvas.__init__(self, root, width=400, bg=MESSAGE_BOX_COLOUR,
                        scrollregion=(0, 0, 0, 0))
        self.root = root
        self.start_coords = 10, 20
        self.width = self.get_width()
        self.font_font = font.Font(family='Helvetica', size=14)
        self.coroutine = coroutine(self)
        self.coroutine.send(None)

    def write_message(self, text):
        x, y = self.start_coords
        x = x + self.get_text_width(text)
        self.delete_message()
        self.coroutine.send((text, x, y))

    def delete_message(self):
        self.delete('all')

    def get_width(self):
        return int(self.cget('width'))

    def get_text_width(self, text):
        return self.font_font.measure(text)

    def get_text_height(self):
        return self.font_font.metrics('linespace')

    def get_header(self, text):
        width = self.get_width()
        text_width = self.get_text_width(text)
        sep_width = self.get_text_width('=')

        while text_width < width - sep_width * 2 - self.start_coords[0]:
            text = '{}{}{}'.format('=', text, '=')
            text_width = self.get_text_width(text)

        if text_width <= width - sep_width - self.start_coords[0]:
            text += '='

        return text

    def write_characters(self, chararcters_obj, all_characters):
        self.delete_message()
        y = self.start_coords[1]

        for character in all_characters:
            header = self.get_header(character)
            text_height = self.get_text_height()
            x = self.start_coords[0] + self.get_text_width(header)
            self.coroutine.send((header, x, y))
            y += text_height
            y = write_dict(self, chararcters_obj.get_character(character), y=y)
            y += text_height

    def write_damage(self, damage_struct, y=None):
        write_dict(self, damage_struct, y=y)