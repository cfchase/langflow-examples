"""Hello World Dep Component - Demonstrates pip dependency usage."""

from langflow.custom import Component
from langflow.io import IntInput, Output
from langflow.schema.message import Message


class HelloWorldDepComponent(Component):
    """A component that uses the humanize library to format numbers.

    This component verifies that pip dependencies are correctly installed
    and importable by custom components.
    """

    display_name = "Hello World Humanize"
    description = "Formats a number using the humanize library. Tests pip dependency installation."
    icon = "Hash"
    name = "HelloWorldDep"

    inputs = [
        IntInput(
            name="number",
            display_name="Number",
            info="A number to humanize (e.g., 1000000 becomes '1.0 million')",
            value=1000000,
        ),
    ]

    outputs = [
        Output(
            display_name="Humanized",
            name="humanized_output",
            method="humanize_number",
        ),
    ]

    def humanize_number(self) -> Message:
        """Format the number using humanize library."""
        import humanize

        result = humanize.intword(self.number)
        self.status = result
        return Message(text=f"Humanized: {result}")
