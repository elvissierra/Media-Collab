from django.db import models
from test_system.apps.teams.models import Team
from test_system.apps.organizations.models import Organization
import uuid


class User(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    team = models.ForeignKey(Team, related_name="users_team", on_delete=models.CASCADE)
    organization = models.ForeignKey(
        Organization,
        related_name="users_organization",
        on_delete=models.CASCADE,
    )
