Title: Friends challenge 3: Full Moon, PWA and fly.io
Date: 2024-03-27 22:26
Category: Tech
Tags: docker
Lang: en
Status: draft

# PWA



# CSS

* reuse of blog CSS

* Rounded corners

* background-image

# Fly.io

    :::bash
    winget search Microsoft.PowerShell

    :::bash
    powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

    :::bash
    fly auth signup

    :::bash
    C:\Users\fabie\.fly\bin\flyctl.exe launch (in the repo where the app is!)

    reads the DOckerfile and deploy magically.