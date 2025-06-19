import os
from django.core.exceptions import ValidationError
from django.db import models

from resource_management_backend import settings


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
    return f"trainers/images/{instance.id}_{instance.firstName}/{filename}"


def upload_trainer_cv(instance, filename):
    return f"trainers/images/{instance.id}_{instance.firstName}/{filename}"


class Trainer(models.Model):
    firstName = models.CharField(max_length=255, blank=False, null=False)
    lastName = models.CharField(max_length=255, blank=False, null=False)
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
        return f"{self.firstName} {self.lastName}"
