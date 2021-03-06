from django.db import models
from core import models as core_models

class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled")
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    chech_in = models.DateField()
    chech_out = models.DateField()
    guest = models.ForeignKey("users.User",  related_name="reservation", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room",  related_name="reservation", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room}-{self.chech_in}'