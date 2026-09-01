#!/usr/bin/env python3
"""Verify that requirements.txt exactly matches constraints-lock.txt."""

from pathlib import Path
import sys


REQUIREMENTS_PATH = Path("requirements.txt")
MIRROR_PATH = Path("constraints-lock.txt")


def read_pins(path: Path) -> dict[str, str]:
    pins = {}
    for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.count("==") != 1:
            raise ValueError(f"{path}:{line_number} must use package==version syntax")
        name, version = line.split("==")
        if not name or not version:
            raise ValueError(f"{path}:{line_number} must use package==version syntax")
        pins[name] = version
    return pins


def main() -> int:
    requirement_pins = read_pins(REQUIREMENTS_PATH)
    mirror_pins = read_pins(MIRROR_PATH)
    if requirement_pins == mirror_pins:
        print(f"Dependency mirror is in sync: {MIRROR_PATH}")
        return 0

    differences = []
    for name in sorted(requirement_pins.keys() | mirror_pins.keys(), key=str.lower):
        requirement_version = requirement_pins.get(name, "<missing>")
        mirror_version = mirror_pins.get(name, "<missing>")
        if requirement_version != mirror_version:
            differences.append(
                f"  - {name}: {REQUIREMENTS_PATH}={requirement_version}; "
                f"{MIRROR_PATH}={mirror_version}"
            )

    print("ERROR: Dependency mirror is out of sync.", file=sys.stderr)
    print("\n".join(differences), file=sys.stderr)
    print(
        f"FIX: Edit {MIRROR_PATH} so every package==version line exactly matches "
        f"{REQUIREMENTS_PATH}, then commit the updated mirror file.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"ERROR: Could not validate dependency mirror: {error}", file=sys.stderr)
        raise SystemExit(1)
