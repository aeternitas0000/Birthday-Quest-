[app]
title = Birthday Quest
package.name = birthdayquest
package.domain = com.birthdayquest

source.dir = .
source.include_exts = py,png,jpg,mp3,wav

version = 0.1

# Use python3.11 without pinning to specific patch version
# This allows p4a to manage compatible versions
# Include cython for pygame compilation
requirements = python3,cython,pygame==2.5.2,pyjnius

orientation = landscape
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.features = android.hardware.touchscreen

# Ensure proper audio handling
p4a.local_recipes = ./recipes
p4a.bootstrap = sdl2

# Icon and presplash
android.presplash_lottie = 1

# Explicitly set Python version for consistency
p4a.python_version = 3.11

# Disable version check conflicts
p4a.ignore_setup_py = 1

[buildozer]
log_level = 2
warn_on_root = 1
