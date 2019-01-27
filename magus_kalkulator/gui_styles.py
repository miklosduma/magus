from tkinter import ttk


BASE_BACKGROUND = 'white'
HIGHLIGHT_BACKGROUND = '#e5ffe5'

FONT_COLOUR = '#324F17'
BUTTON_COLOUR = '#ccffcc'
FIELD_COLOR_ERROR = '#ff6464'


CSS = {
        'TLabelframe': {
            'configure': {
                'background': BASE_BACKGROUND,
                'padding': 4
            }
        },

        'TPanedwindow': {
            'configure': {
                'background': BASE_BACKGROUND
            }
        },

        'TNotebook': {
            'configure': {
                'background': BASE_BACKGROUND,
                'tabposition': 'nesw',
                'borderwidth': 0
            }
        },

        'TNotebook.Tab': {
            'configure': {
                'background': HIGHLIGHT_BACKGROUND,
                'foreground': FONT_COLOUR,
                'font': ('Helvetica', 14, 'bold'),
                'padding': 4,
                'borderwidth': 0,
                'focuscolor': HIGHLIGHT_BACKGROUND
            },
            'map': {
                'background': [('selected', BUTTON_COLOUR)],
                'expand': [('selected', [1, 1, 0, 0])],
                'borderwidth': [('selected', 0)]
            }
        },

        'TFrame': {
            'configure': {
                'background': BASE_BACKGROUND
            }
        },

        'TLabel': {
            'configure': {
                'background': BASE_BACKGROUND,
                'foreground': FONT_COLOUR,
                'font': ('Helvetica', 14),
                'padding': 2
            }
        },

        'Label': {
            'configure': {
                'background': BASE_BACKGROUND,
                'foreground': FONT_COLOUR,
                'font': ('Helvetica', 14, 'bold')
            }
        },

        'TEntry': {
            'configure': {
                'fieldbackground': BASE_BACKGROUND,
                'foreground': FONT_COLOUR,
                'borderwidth': 1
            },

            'map': {
                'fieldbackground': [('invalid', FIELD_COLOR_ERROR),
                                    ('disabled', 'gray'),
                                    ('focus', HIGHLIGHT_BACKGROUND)]
            }
        },

        'TCheckbutton': {
            'configure': {
                'background': BASE_BACKGROUND,
                'indicatorcolor': BASE_BACKGROUND,
                'focuscolor': BASE_BACKGROUND,
                'foreground': FONT_COLOUR,
                'padding': (5, 0)
            },
            'map': {
                'indicatorcolor': [('selected', BUTTON_COLOUR)]
            }
        },

        'TButton': {
            'configure': {
                'background': BUTTON_COLOUR,
                'foreground': FONT_COLOUR,
                'padding': 2,
                'focuscolor': BUTTON_COLOUR,
                'relief': 'raised'
            },

            'map': {
                'relief': [('pressed', 'sunken')],
                'border': [('focus', '0')]
            }
        },

        'TCombobox': {
            'configure': {
                'selectbackground': BASE_BACKGROUND,
                'selectforeground': FONT_COLOUR,
                'foreground': FONT_COLOUR,
                'background': BUTTON_COLOUR,
                'fieldbackground': BASE_BACKGROUND,
                'arrowcolor': FONT_COLOUR,
                'arrowsize': 14,
                'borderwidth': 1
            },

            'map': {
                'fieldbackground': [('disabled', 'gray')]
            }
        },

        'TSpinbox': {
            'configure': {
                'selectbackground': BASE_BACKGROUND,
                'selectforeground': FONT_COLOUR,
                'foreground': FONT_COLOUR,
                'arrowcolor': FONT_COLOUR,
                'background': BUTTON_COLOUR
            },

            'map': {
                'fieldbackground': [('focus', HIGHLIGHT_BACKGROUND)],
                'selectbackground': [('focus', HIGHLIGHT_BACKGROUND)]
            }
        }
    }


def apply_style(root, my_style='minimal'):

    style = ttk.Style()
    style.theme_create(my_style, settings=CSS)

    # Highlight colour for combobox drop-down.
    root.option_add('*TCombobox*Listbox.selectBackground', BUTTON_COLOUR)
    style.theme_use(my_style)
