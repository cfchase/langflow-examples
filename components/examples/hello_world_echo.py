"""Hello World Echo Component - Simple text echo for testing."""

from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema.message import Message


class HelloWorldEchoComponent(Component):
    """A simple component that echoes input text with a greeting.

    This component is used to verify custom component loading works correctly.
    """

    display_name = "Hello World Echo"
    description = "Echoes input text with a friendly greeting. Used for testing custom components."
    icon = "MessageSquare"
    name = "HelloWorldEcho"

    inputs = [
        MessageTextInput(
            name="input_text",
            display_name="Input Text",
            info="Text to echo back with a greeting",
        ),
    ]

    outputs = [
        Output(
            display_name="Message",
            name="output_message",
            method="echo_message",
        ),
    ]

    def echo_message(self) -> Message:
        """Echo the input with a greeting prefix."""
        greeting = f"Hello! You said: {self.input_text}"
        self.status = greeting
        return Message(text=greeting)
