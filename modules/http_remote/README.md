# HTTP Remote Control

Minimal HTTP interface for remote control or status queries. Runs under
MicroPython on the Raspberry Pi Pico W.

## Config

`config.json`

```json
{
  "port": 8080
}
```

## Messages

* Input: `{"type": "start", "port": int}` or `{"type": "stop"}`
* Output: `{"type": "http_command", "command": dict}`
