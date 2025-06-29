
# package greyhoundDashboard.services.service_base
# -*- coding: utf-8 -*-
# This file is part of Greyhound Dashboard.

from greyhoundDashboard.services.service_base import ServiceBase

class AccentService(ServiceBase):
    id = "accent"
    name = "Accent Reviews"
    description = "A service for reviewing accents and dialects."
    tags = ["review", "linguistics", "accent"]

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def get(self) -> "ServiceBase":
        return super().get()

    # Example of an extra method specific to Accent service
    def fetch_reviews(self):
        # Placeholder for method to fetch user reviews
        pass

AccentService.register()
