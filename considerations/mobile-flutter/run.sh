#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/flutter_con_mobile"

# clean dependencies before building APK
flutter clean
flutter build apk --release

APK_PATH="build/app/outputs/flutter-apk/app-release.apk"

if [ ! -f "$APK_PATH" ]; then
  echo "APK not found at $APK_PATH"
  exit 1
fi

cp "$APK_PATH" ../app-release.apk

cd ".."

echo "APK copied at ./app-release.apk"