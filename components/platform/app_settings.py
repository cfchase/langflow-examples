"""
AppSettings component for application context injection.

This component receives application-level context JSON from the platform via tweaks
and outputs it as a Data object for flows to consume.

The platform injects via tweaks: {"App Settings": {"settings_data": {...}}}
Flows can then wire the data output to components that need app context.

IMPORTANT: AppSettings does NOT carry API keys. API keys are injected via
LangFlow environment variables (config/langflow.env).
"""
from langflow.custom import Component
from langflow.io import NestedDictInput, Output
from langflow.schema.data import Data


class AppSettingsComponent(Component):
    """Receives application context JSON from platform tweaks.

    This component provides non-secret application configuration:
    - App name
    - Feature flags
    - Version info

    The backend sends: {"App Settings": {"settings_data": {...}}}

    Example data:
        {
            "app_name": "enterprise-agent",
            "features": {"rag_enabled": True},
            "version": "1.0.0"
        }
    """

    display_name = "App Settings"
    description = "Application context from platform (feature flags, config)"
    icon = "Settings"
    name = "AppSettings"

    inputs = [
        NestedDictInput(
            name="settings_data",
            display_name="Settings Data",
            info="App settings injected by the platform via tweaks",
            value={},
            advanced=True,
        ),
    ]

    outputs = [
        Output(
            name="data",
            display_name="App Data",
            method="get_data",
            types=["Data"],
        ),
    ]

    def get_data(self) -> Data:
        """Return the injected app settings as Data.

        The platform injects via tweaks:
            {"App Settings": {"settings_data": {...}}}

        Returns:
            Data: App settings as a Data object
        """
        raw = getattr(self, "settings_data", {})
        settings_dict = raw if isinstance(raw, dict) else {}
        return Data(data=settings_dict)
