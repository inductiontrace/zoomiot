# Motion Controller

Turns high level drive commands into messages for the motor controller
on MicroPython running on the Raspberry Pi Pico W.

## Config

`config.json`

```json
{
  "default_speed": 0.5
}
```

## Messages

* Input: `{"type": "drive", "direction": "forward|backward|left|right", "speed": float}`
* Output: forwards `set_speed` to the motor controller
