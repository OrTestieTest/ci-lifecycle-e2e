# CI lifecycle end-to-end fixture

This is a fully synthetic Python repository for testing dependency-remediation pull request workflows. Its dependency versions are intentionally vulnerable so an SCA scanner can propose version bumps.

The `dependency-mirror` GitHub Actions check verifies that `constraints-lock.txt` mirrors every exact pin in `requirements.txt`. The project is a test fixture only and must not be deployed.

## Checks

- `dependency-mirror` verifies that `constraints-lock.txt` mirrors every exact pin in `requirements.txt`.
- `unit-tests` runs the stdlib `unittest` suite under `tests/`.
- `infra-gate` fails whenever `.ci/infra-gate.fail` is present. It stands in for an environment gate that repository code cannot satisfy.
