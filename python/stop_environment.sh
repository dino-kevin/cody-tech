#!/bin/bash

# Check if the deactivate command exists in the current session
if declare -f deactivate > /dev/null; then
    echo "Deactivating the current virtual environment..."
    deactivate
    echo "✅ Environment deactivated. You are back to the system Python."
else
    echo "⚠️ No active virtual environment found to deactivate."
fi
