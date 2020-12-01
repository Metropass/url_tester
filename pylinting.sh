#!/bin/bash

if [$# -eq 0]; then
  sh -c "python -m pylint release0_1.py"
fi
