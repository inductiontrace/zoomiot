"""WiFi client module."""

try:
    import network
except ImportError:  # pragma: no cover - MicroPython only
    network = None


class WifiClient:
    """Connects to a WiFi network."""

    def __init__(self, config):
        self.ssid = config.get("ssid", "")
        self.password = config.get("password", "")
        self.connected = False
        if network:
            self.sta = network.WLAN(network.STA_IF)
            self.sta.active(False)
        else:
            self.sta = None

    def tick(self, inbox, send_mail):
        if inbox:
            msg = inbox.pop(0)
            if msg.get("type") == "connect":
                self.ssid = msg.get("ssid", self.ssid)
                self.password = msg.get("password", self.password)
                if self.sta:
                    self.sta.active(True)
                    self.sta.connect(self.ssid, self.password)
                self.connected = True
            elif msg.get("type") == "disconnect":
                if self.sta:
                    self.sta.disconnect()
                    self.sta.active(False)
                self.connected = False
        send_mail(
            "core",
            {
                "type": "client_status",
                "connected": self.sta.isconnected() if self.sta else self.connected,
            },
        )
