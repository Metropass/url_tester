#!/bin/bash
set -e
if [$# -eq 0]; then
  sh -c "python -m black release0_1.py"
fi
