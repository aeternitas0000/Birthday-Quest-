[app]
title = Birthday Quest
package.name = birthdayquest
package.domain = com.birthdayquest

source.dir = .
source.include_exts = py,png,jpg,mp3,wav

version = 0.1

requirements = python3==3.14,pygame,pyjnius

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

[buildozer]
log_level = 2
warn_on_root = 1
