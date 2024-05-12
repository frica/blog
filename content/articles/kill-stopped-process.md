Title: How to kill a stopped process in Linux terminal
Date: 2024-05-12 17:00
Category: Tech
Tags: linux, WSL
Lang: en

Let's say you started an application via the terminal and you used **Ctrl-Z** instead of **Ctrl-C** to continue working in your console. By doing so, your process was put in the background.

How kill it easily then? On Windows WSL, sometimes you won't be able to kill it from the Windows taskbar. But one way to find back the process in stopped state, is to use the `-T` option of `ps`.

The `T` option selects all processes associated with your terminal. It's identical to the `t`  option without any argument.

Grab the Process ID (PID) and then with the command `kill -9 <PID>`, you'll get rid of the process.
