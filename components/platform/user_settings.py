"""
UserSettings component for generic settings injection.

This component receives user context JSON from the platform via tweaks
and outputs it as a Data object for flows to consume.

The platform injects via tweaks: {"UserSettings": {"data": {...}}}
Flows can then wire the data output to components that need user context.
"""
from langflow.custom import Component
from langflow.io import NestedDictInput, Output
from langflow.schema.data import Data


class UserSettingsComponent(Component):
    """Receives user context JSON from platform tweaks.

    This replaces per-flow tweak mappings with a generic pattern.
    The backend sends: {"UserSettings": {"settings_data": {...}}}

    Flows can then wire the data output to components that need user context.

    Example data:
        {
            "google_drive_token": "oauth-token",
            "email": "user@example.com",
            "preferences": {...}
        }
    """

    display_name = "User Settings"
    description = "User context from platform (OAuth tokens, preferences)"
    icon = "User"
    name = "UserSettings"

    inputs = [
        NestedDictInput(
            name="settings_data",
            display_name="Settings Data",
            info="User settings injected by the platform via tweaks",
            value={},
            advanced=True,
        ),
    ]

    outputs = [
        Output(
            name="data",
            display_name="User Data",
            method="get_data",
            types=["Data"],
        ),
    ]

    def get_data(self) -> Data:
        """Return the injected user settings as Data.

        The platform injects via tweaks:
            {"UserSettings": {"settings_data": {...}}}

        Returns:
            Data: User settings as a Data object
        """
        raw = getattr(self, "settings_data", {})
        settings_dict = raw if isinstance(raw, dict) else {}
        return Data(data=settings_dict)
