# RC Car Firmware Modules

Welcome to **zoomiot**, a tiny collection of drop-in Python
modules for a Raspberry Pi Pico W running MicroPython. Copy the
modules you want onto the Pico's flash and the main driver will stitch
them together.

## How it works

Each module owns a small mailbox. The main driver cycles through the
modules and calls their `tick()` function. Messages placed in a
mailbox are processed on the next tick, keeping everything cooperative
and responsive.

Messages are plain dictionaries with a `type` field. A module can send
a message back to the driver which then forwards it to the destination
module.

Key rules for modules:

* Never block for more than **1 ms** inside `tick()`.
* Don't rely on being called more often than **every 100 ms**.

## Included modules

* **Motor controller** – low level motor PWM control.
* **Motion controller** – translates high level movement into motor
  commands.
* **BLE relay** – forwards commands and status over Bluetooth Low
  Energy.
* **WiFi AP** – sets up the car as an access point.
* **WiFi client** – connects the car to an existing network.
* **HTTP remote control** – tiny web interface for remote driving.

Each module lives in `modules/<name>` with its own README, Python file
and `config.json`.

## Adding your own modules

Create a new folder in `modules/` with a Python file implementing a
`tick(inbox, send_mail)` function. Drop the folder onto the Pico and
register it with the main driver.

