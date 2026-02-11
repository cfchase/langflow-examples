"""
Platform components for multi-agent-platform integration.

These components provide the interface between the platform backend
and LangFlow flows. Any flow running on the platform can use these.

- UserSettings: Receives per-user context (OAuth tokens, preferences) via tweaks
- AppSettings: Receives app-level context (feature flags, config) via tweaks
- GoogleDriveValidator: Searches Google Drive using a Bearer access token
"""
from components.platform.user_settings import UserSettingsComponent
from components.platform.app_settings import AppSettingsComponent
from components.platform.google_drive_validator import GoogleDriveValidatorComponent

__all__ = [
    "UserSettingsComponent",
    "AppSettingsComponent",
    "GoogleDriveValidatorComponent",
]
