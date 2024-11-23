Title: Browsing and editing files from the terminal with nnn and micro
Date: 2024-11-23 18:00
Category: Tech
Tags: linux, terminal
Lang: en
Summary: A step by step configuration of nnn and micro to improve my productivity in the terminal.

In the last weeks I discovered several terminal tools that looked promising and I wanted to see how practical they were. The goal there is to improve my productivity in the command-line while working on Linux or in the WSL on Windows.

Simple requirements:

* I want to be able to browse the filesystem with [nnn](https://github.com/jarun/nnn)
* I want to open text files easily with [micro](https://micro-editor.github.io/)

# Basic installation

To install nnn (version 4.3-1 on Ubuntu 22.04):

    :::bash
    sudo apt install nnn

To install micro (version 2.0.9 on Ubuntu 22.04):

    :::bash
    sudo apt install micro

# Configuration

nnn comes with a number or arguments to specify the default behavior when called.

One smart thing to do is then to create an alias:

    :::bash
    alias nnn='nnn -d -e -H -r'

and put it in your `.bashrc`. 

In my case, because I use [Oh-My-Bash](https://github.com/ohmybash/oh-my-bash), I put it in `/home/fari/.oh-my-bash/custom` in a file named `general.aliases.sh`

Here is an explanation of all parameters I use:

| Flag | Description |
|----|--------------|
| -e |     text in $VISUAL/$EDITOR/ |
| -d |     detail mode |
| -H |     show hidden files |
| -r |     use advcpmv patched cp, mv |


By default, `-e` uses vi and I don't really like it so if you're like me, you need to set up the `$EDITOR` environment variable in `.bashrc` to link it to micro:

    :::bash
    export EDITOR='micro'

And then it works! I can browser files in the terminal, hit **Enter** and it opens my text files in micro.

{% img {static}/images/demo_nnn_micro.gif "Demo of the workflow" "Demo of the workflow" %}

# nnn usage

nnn has some nice keyboard shortcuts:

| Shortcut   | Action                     |
|---|---------------------|
| . | Toggle hidden files |
| t (or Ctrl-T) |  Sort toggles |  
| Ctrl-R |  Rename/dup |
| x (Ctrl-X) | Delete or trash |
| q | Quit |

# Configuration of micro

To change your micro colorscheme, press `Ctrl-e` in micro to bring up the command prompt, and type:

    :::bash
    set colorscheme solarized

This one is translucent and it integrates nicely with the default nnn setup.

If, like me, you want to be able to wrap lines with the same shortcut as in VSCode, put the following lines in your `~/.config/micro/settings.json` file:

    :::bash
    {
        "Alt-z": "command:set wordwrap off,command:set softwrap off",
        "Alt-Z": "command:set wordwrap on,command:set softwrap on",
    }

# The end

And this concludes this post: my initial goal is achieved!
I can now browse and edit from the terminal! There are probably plenty of possible improvements but it feels pretty good already.

PS: This setup is especially handy also if you're using WSL on Windows.
