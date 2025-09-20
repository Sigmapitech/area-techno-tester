# Consideration for Kotlin with Android Studio

## Overview

[Kotlin](https://kotlinlang.org/) is a modern programming language officially supported by Google for Android development.
Combined with **Android Studio**, it is the main toolset for building native Android apps. Kotlin is concise compared to Java,
integrates well with existing Java code, and has strong support from the Android ecosystem.

## Why we considered it?

Kotlin with Android Studio is the default, “official” way to build Android apps. Since it gives direct access to Android’s
native APIs, it allows better performance and smoother integration with device features compared to cross-platform solutions.

## Who in the group has prior knowledge about this tech?

Nobody in the group has prior experience with Kotlin or Android Studio.

## How could this tech allow us to improve our workflow?

* It allows us to produce a real, installable APK quickly without complicated setups.
* Native development ensures full compatibility with Android features.
* Good long-term maintainability since Google itself backs Kotlin for Android.

## What is the general feeling?

The overall feeling isn’t great. Android Studio is extremely heavy and eats a lot of RAM, which makes it unpleasant to use.
Kotlin itself didn’t feel very exciting either — while it is cleaner than Java, it still carries a lot of the same complexity.
The one clear positive was how easy it was to generate an APK compared to React Native. However, since this approach only works
for Android and doesn’t cover iOS, it doesn’t really fit our needs.

## Advantages

* Official language and tools for Android apps.
* Produces native, performant applications.
* Simple APK generation and deployment compared to some cross-platform options.
* Strong library and framework support (Jetpack, Compose, etc.).

## Disadvantages

* No one in the group has prior experience, so the learning curve is high.
* Android Studio is heavy and slow, especially on machines with limited RAM.
* Kotlin still feels a lot like Java, which isn’t very appealing to work with.
* Limited to Android only, which is a dealbreaker for cross-platform needs.

## Use Cases

* Apps targeting Android only.
* Projects that need deep integration with Android hardware features.

## Conclusion

While Kotlin with Android Studio is the official route for Android app development, it doesn’t suit our group.
The steep learning curve, resource-heavy tools, and Android-only limitation outweigh the benefits.
The ease of creating an APK was a highlight, but overall this tech wouldn’t be usable given our requirements.
