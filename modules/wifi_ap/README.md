# WiFi Access Point

Brings up the Pico W as a WiFi access point using MicroPython so
clients can connect directly.

## Config

`config.json`

```json
{
  "ssid": "ZoomCar",
  "password": "zoomzoom"
}
```

## Messages

* Input: `{"type": "start"}` or `{"type": "stop"}`
* Output: `{"type": "ap_status", "active": bool}`
