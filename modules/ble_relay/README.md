# BLE Relay

Relays commands and status over Bluetooth Low Energy. Designed for
MicroPython on the Raspberry Pi Pico W (currently a stub until BLE
support lands).

## Config

`config.json`

```json
{
  "device_name": "rc-car"
}
```

## Messages

* Input: `{"type": "send", "payload": str}`
* Output: `{"type": "ble_command", "payload": str}`
