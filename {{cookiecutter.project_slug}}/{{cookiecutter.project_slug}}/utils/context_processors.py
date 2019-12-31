from django.conf import settings

from jovian_replication_manager.volume import models


def settings_context(_request):
    return {"settings": settings,
            "ClusterType": models.ClusterType}
