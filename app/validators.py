def validate_pdf(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'File must be PDF')


def validate_video(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.3gp', '.mp4', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'File must be Video')
