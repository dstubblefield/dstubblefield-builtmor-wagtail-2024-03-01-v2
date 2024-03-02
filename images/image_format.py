from wagtail.images.formats import Format, register_image_format

register_image_format(Format(
    'full-width', 'Full width', 'richtext-image full-width', 'max-1200x1200'
    ))