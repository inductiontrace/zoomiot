# Main Driver

The main driver is the traffic cop of the system on a Raspberry Pi Pico
W running MicroPython. It registers modules, feeds them their mailboxes
and forwards messages between them.

## Usage

```python
from modules.main_driver.main_driver import MainDriver

md = MainDriver()
md.register('motor', motor_module)
md.run_once()  # call in your loop
```

The driver has no configuration file; modules are registered manually.
