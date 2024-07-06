from django.core.exceptions import ValidationError


def validate_image_size(file):
    max_size_kb = 5 * 1024 * 1024
    if file.size > max_size_kb:
        raise ValidationError(
            f"Image file should not exceed {max_size_kb / (1024 * 1024)}MB."
        )
