# WiFi Client

Connects the Pico W to an existing WiFi network with MicroPython.

## Config

`config.json`

```json
{
  "ssid": "",
  "password": ""
}
```

## Messages

* Input: `{"type": "connect", "ssid": str, "password": str}`
* Input: `{"type": "disconnect"}`
* Output: `{"type": "client_status", "connected": bool}`
