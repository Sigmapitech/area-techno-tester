#!/usr/bin/env bash
set -euo pipefail

EXPECTED_OWNER="cizniarova"

WHOAMI_OUTPUT=$(eas whoami)

if echo "$WHOAMI_OUTPUT" | grep -q "Not logged in"; then
  echo "You are not logged in to Expo. Please run: eas login"
  exit 1
fi

USERNAME=$(echo "$WHOAMI_OUTPUT")

if [ "$USERNAME" != "$EXPECTED_OWNER" ]; then
  echo "Wrong account: $USERNAME"
  echo "Please log in as $EXPECTED_OWNER"
  exit 1
fi

npx eas build -p android --profile production --non-interactive
