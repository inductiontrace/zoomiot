"""HTTP remote control module."""


class HttpRemote:
    """Provides a stub HTTP interface."""

    def __init__(self, config):
        self.port = int(config.get("port", 8080))
        self.active = False

    def tick(self, inbox, send_mail):
        if inbox:
            msg = inbox.pop(0)
            if msg.get("type") == "start":
                self.port = int(msg.get("port", self.port))
                self.active = True
            elif msg.get("type") == "stop":
                self.active = False
            elif msg.get("type") == "http_in":
                send_mail("core", {"type": "http_command", "command": msg.get("command", {})})
