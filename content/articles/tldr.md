Title: tldr, a useful CLI tool for goldfish-memory tech workers
Date: 2025-08-31
Category: Tech
Lang: en
Tags: tools, tips
Summary: Quick presentation of tldr

One toxic behavior of the Linux community for many years when someone was asking for help was *RTFM* (Read The Fucking Manual). "All the help is right there, just type `man <command>`, you noob.". Fair enough: most tools have very often an embedded help reachable with `man`, but it is sometimes a very long list of arguments and not very clear how to actually perform standard operations.

Also I have a awful memory and if I don't use a tool or a command daily, I'm getting frustrated when I know that I can do something on the CLI tools but I have forgotten the right arguments and syntax.

That's when the project [`tldr`](https://github.com/tldr-pages/tldr) comes to help! "TL;DR" stands for "too long, didn't read" and is internet slang, often used to introduce a summary of an online post or news article.

(It is also used as a mean comment that a block of text has been ignored due to its length, but here we'll focus on the positive aspect)

> The **tldr-pages** project is a collection of community-maintained help pages for command-line tools, that aims to be a simpler, more approachable complement to traditional [man pages](https://en.wikipedia.org/wiki/Man_page).

On Ubuntu 24.04,you can install `tldr` via apt  but you will get version `0.9.2`.

If you actually want the latest release of the [python client](https://github.com/tldr-pages/tldr-python-client) on Ubuntu you better install the snap package.

    :::bash
    $ sudo snap install tldr

Then choose your console tool and type `tldr <tool>`! It will fetch the help files stored locally in `.local/share/tldr/pages/` and display it in a flash.

Example with `ripgrep`, a tool I like very much but often forgets the syntax:

    :::bash
    $ tldr rg

    rg

    Ripgrep, a recursive line-oriented search tool.
    Aims to be a faster alternative to grep.
    More information: https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md.

    - Recursively search current directory for a pattern (regex):
    rg pattern

    - Recursively search for a pattern in a file or directory:
    rg pattern path/to/file_or_directory

    - Include hidden files and entries listed in .gitignore:
    rg [-.|--hidden] --no-ignore pattern

    - Only search the files whose names match the glob pattern(s) (e.g. README.*):
    rg pattern [-g|--glob] filename_glob_pattern

    - Recursively list filenames in the current directory that match a pattern:
    rg --files | rg pattern

    - Only list matched files (useful when piping to other commands):
    rg [-l|--files-with-matches] pattern

    - Show lines that do not match the pattern:
    rg [-v|--invert-match] pattern

    - Search for a literal string pattern:
    rg [-F|--fixed-strings] -- string

I also discovered another cool tool in the same spirit, but online this time: [Cheat.sh](https://cheat.sh/). I still prefer to not be distracted by my browser when working in the terminal, but it's a very cool initiative too!

Hope this helps 🙂!
