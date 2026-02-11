"""
Google Drive validation component using just an access token.

Validates OAuth token injection by calling the Google Drive API
with a Bearer token. Unlike LangFlow's built-in GoogleDriveSearchComponent
(which requires full OAuth credentials JSON), this component works with
just the access_token string that the platform injects.

Flow wiring:
    UserSettings → [user_data] → GoogleDriveValidator
    ChatInput → [search_query] → GoogleDriveValidator
    GoogleDriveValidator → ChatOutput
"""
import httpx
from langflow.custom import Component
from langflow.io import DataInput, MessageTextInput, Output
from langflow.schema.data import Data
from langflow.schema.message import Message


class GoogleDriveValidatorComponent(Component):
    """Searches Google Drive using a Bearer access token.

    Accepts user_data from UserSettings (which contains google_drive_token)
    and a search query. Calls the Google Drive REST API directly.
    """

    display_name = "Google Drive Validator"
    description = "Search Google Drive with an OAuth access token"
    icon = "GoogleDrive"
    name = "GoogleDriveValidator"

    inputs = [
        DataInput(
            name="user_data",
            display_name="User Data",
            info="Data from UserSettings containing google_drive_token",
        ),
        MessageTextInput(
            name="search_query",
            display_name="Search Query",
            info="Search term for Google Drive files",
            value="test",
        ),
    ]

    outputs = [
        Output(
            name="results",
            display_name="Results",
            method="search_drive",
        ),
    ]

    def search_drive(self) -> Message:
        # Extract token from UserSettings data
        token = None
        if self.user_data:
            if isinstance(self.user_data, Data):
                token = self.user_data.data.get("google_drive_token")
            elif isinstance(self.user_data, dict):
                token = self.user_data.get("google_drive_token")

        if not token:
            return Message(
                text="No google_drive_token found in User Data. "
                "Ensure UserSettings is connected and the platform "
                "is injecting the token via tweaks."
            )

        query = self.search_query or "test"

        response = httpx.get(
            "https://www.googleapis.com/drive/v3/files",
            params={
                "q": f"name contains '{query}'",
                "fields": "files(id,name,mimeType,modifiedTime)",
                "pageSize": 10,
            },
            headers={"Authorization": f"Bearer {token}"},
            timeout=30,
        )
        response.raise_for_status()
        files = response.json().get("files", [])

        if not files:
            return Message(text=f"No files found matching '{query}'")

        lines = [f"Found {len(files)} file(s) matching '{query}':\n"]
        for f in files:
            lines.append(
                f"- {f['name']} ({f.get('mimeType', 'unknown')})"
            )
        return Message(text="\n".join(lines))
