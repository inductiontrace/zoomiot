"""WiFi access point module."""

try:
    import network
except ImportError:  # pragma: no cover - MicroPython only
    network = None


class WifiAP:
    """Manages a simple WiFi access point."""

    def __init__(self, config):
        self.ssid = config.get("ssid", "ZoomCar")
        self.password = config.get("password", "zoomzoom")
        self.active = False
        if network:
            self.ap = network.WLAN(network.AP_IF)
            self.ap.active(False)
        else:
            self.ap = None

    def tick(self, inbox, send_mail):
        if inbox:
            msg = inbox.pop(0)
            if msg.get("type") == "start":
                if self.ap:
                    self.ap.config(essid=self.ssid, password=self.password)
                    self.ap.active(True)
                self.active = True
            elif msg.get("type") == "stop":
                if self.ap:
                    self.ap.active(False)
                self.active = False
        send_mail("core", {"type": "ap_status", "active": self.ap.active() if self.ap else self.active})
