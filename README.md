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
register it with the main driver

## Installing on a Pico W (Linux)

The helper scripts use [`mpremote`](https://docs.micropython.org/en/latest/reference/mpremote.html)
to copy files over USB.

1. Install mpremote if you don't have it yet:
   ```sh
   pip install mpremote
   ```
   
2. Build a deploy folder with the modules you want:
   ```sh
   python scripts/prepare_deploy.py
   ```
   The script lists available modules, lets you tweak each `config.json`,
   then writes everything into a new `deploy/` folder.
   
3. Plug in the Pico W and flash the files:
   ```sh
   python scripts/flash_pico.py
   ```
   Pick the correct `/dev/tty*` device when prompted. The script copies
   the contents of `deploy/` onto the board and resets it.


