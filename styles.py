class Styles:

    # Colors
    colors = {
        'background': 'black',
        'foreground': 'white'
    }

    # object styles
    object_styles = {
        'label': {
            'bg': colors['background'],
            'fg': colors['foreground'],
            'font': 'none 12 bold',
            'text': 'Add Label Text'
        },

        'entry': {
            'width': 20,
            'bg': 'white'
        }
    }

    def __new__(cls, style_name, other_styles=None):
        cls.style_name = style_name
        default_styles = cls.object_styles[style_name].copy()

        if other_styles:
            default_styles.update(other_styles)

        return default_styles

