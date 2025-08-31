#!/usr/bin/env python3
"""Copy the prepared deploy folder to a Pico W using mpremote."""

import glob
import os
import subprocess

DEPLOY_DIR = "deploy"


def choose_port():
    ports = glob.glob("/dev/ttyACM*") + glob.glob("/dev/ttyUSB*")
    if not ports:
        raise SystemExit("No serial ports found")
    for idx, port in enumerate(ports, 1):
        print(f"  {idx}. {port}")
    choice = input("Select Pico device: ").strip()
    return ports[int(choice) - 1]


def main():
    if not os.path.isdir(DEPLOY_DIR):
        raise SystemExit("Run prepare_deploy.py first")
    port = choose_port()
    confirm = input(f"Copy {DEPLOY_DIR} to {port}? [y/N]: ").lower()
    if confirm != "y":
        return
    subprocess.run([
        "mpremote",
        "connect",
        port,
        "fs",
        "cp",
        "-r",
        f"{DEPLOY_DIR}/.",
        ":",
    ], check=True)
    subprocess.run(["mpremote", "connect", port, "reset"], check=True)
    print("Deployment finished")


if __name__ == "__main__":
    main()

