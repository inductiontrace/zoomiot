# Module Protocol

Designed for MicroPython on the Raspberry Pi Pico W. All communication
happens through tiny mailboxes. Messages are Python dictionaries with at
least a `type` field. The main driver calls each module's
`tick(inbox, send_mail)` once per cycle, handing in a list of incoming
messages and a callback for outgoing mail.

`send_mail(target, message)` queues `message` for the named module.

## Motor controller

**Input**
- `{"type": "set_speed", "left": float, "right": float}` – set PWM
  values for each motor.

**Output**
- `{"type": "report_speed", "left": float, "right": float}` –
  optional status update.

## Motion controller

**Input**
- `{"type": "drive", "direction": "forward"|"backward"|"left"|"right", "speed": float}`
  – request a basic movement.

**Output**
- `target="motor_controller", message={"type": "set_speed", ...}` –
  translated low level command for the motor controller.

## BLE relay

**Input**
- `{"type": "send", "payload": str}` – transmit a string over BLE.

**Output**
- `{"type": "ble_command", "payload": str}` – command received from
  a BLE peer.

## WiFi access point

**Input**
- `{"type": "start"}` – enable the AP.
- `{"type": "stop"}` – disable it.

**Output**
- `{"type": "ap_status", "active": bool}` – report current state.

## WiFi client

**Input**
- `{"type": "connect", "ssid": str, "password": str}` – join a
  network.
- `{"type": "disconnect"}` – leave the network.

**Output**
- `{"type": "client_status", "connected": bool}` – connection state.

## HTTP remote control

**Input**
- `{"type": "start", "port": int}` – start the web server.
- `{"type": "stop"}` – shut it down.

**Output**
- `{"type": "http_command", "command": dict}` – command received via
  HTTP.

