# Motor Controller

Drives the left and right motors using MicroPython's `PWM` on the Pico
W. Expects a mailbox message to set the speed for each side.

## Config

`config.json`

```json
{
  "left_pin": 17,
  "right_pin": 18
}
```

## Messages

* Input: `{"type": "set_speed", "left": 0.0-1.0, "right": 0.0-1.0}`
* Output: `{"type": "report_speed", "left": float, "right": float}`
