import os
from django.core.exceptions import ValidationError
from django.db import models


# Validators
def validate_image(file):
    max_size_mb = 1
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image file size should not exceed {max_size_mb} MB.")
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in [".jpg", ".jpeg", ".png"]:
        raise ValidationError("Only JPEG and PNG images are allowed.")


def validate_cv(file):
    max_size_mb = 2
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"CV file size should not exceed {max_size_mb} MB.")
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in [".pdf", ".doc", ".docx"]:
        raise ValidationError("Only PDF, DOC, or DOCX files are allowed.")


def upload_trainer_image(instance, filename):
    return f"trainers/images/{instance.id}_{instance.first_name}/{filename}"


def upload_trainer_cv(instance, filename):
    return f"trainers/images/{instance.id}_{instance.first_name}/{filename}"


class Trainer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    image = models.ImageField(
        upload_to=upload_trainer_image,
        validators=[validate_image],
        blank=True,
        null=True,
    )
    cv = models.FileField(
        upload_to=upload_trainer_cv, validators=[validate_cv], blank=True, null=True
    )
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_full_name(self):
        # Filter out empty strings and None values from the name components
        name_components = [part for part in [self.first_name, self.last_name] if part]

        # Join the non-empty components with a space
        return " ".join(name_components)

    @property
    def get_age(self, date):
        date_of_birth = self.dob

        if date_of_birth:
            age = (
                date.year
                - date_of_birth.year
                - ((date.month, date.day) < (date_of_birth.month, date_of_birth.day))
            )
            return age

        return None
