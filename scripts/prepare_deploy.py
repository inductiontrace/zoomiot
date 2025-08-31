#!/usr/bin/env python3
"""Build a deploy folder with selected modules.

The script lists the available modules, lets the user choose which ones
to include, prompts for config values, then writes the module `.py` file
and the modified `config.json` into `deploy/<module>/`.
"""

import json
import os
import shutil

MODULES_DIR = "modules"
DEPLOY_DIR = "deploy"


def prompt(msg, default):
    """Ask the user for a value with a default."""
    value = input(f"{msg} [{default}]: ").strip()
    return value or default


def select_modules():
    modules = [d for d in os.listdir(MODULES_DIR) if os.path.isdir(os.path.join(MODULES_DIR, d))]
    if not modules:
        print("No modules found")
        return []
    print("Available modules:")
    for idx, name in enumerate(modules, 1):
        print(f"  {idx}. {name}")
    picks = input("Select modules by number (space separated): ").split()
    chosen = []
    for p in picks:
        try:
            chosen.append(modules[int(p) - 1])
        except Exception:
            pass
    return chosen


def configure_module(name):
    src_dir = os.path.join(MODULES_DIR, name)
    cfg_path = os.path.join(src_dir, "config.json")
    with open(cfg_path) as f:
        cfg = json.load(f)
    for key, val in cfg.items():
        cfg[key] = prompt(f"{name} {key}", val)
    target = os.path.join(DEPLOY_DIR, name)
    os.makedirs(target, exist_ok=True)
    shutil.copy(os.path.join(src_dir, f"{name}.py"), target)
    with open(os.path.join(target, "config.json"), "w") as f:
        json.dump(cfg, f)


def main():
    if os.path.exists(DEPLOY_DIR):
        shutil.rmtree(DEPLOY_DIR)
    os.makedirs(DEPLOY_DIR)
    for mod in select_modules():
        configure_module(mod)
    print(f"Wrote selected modules to {DEPLOY_DIR}/")


if __name__ == "__main__":
    main()

