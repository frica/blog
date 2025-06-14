Title: How to know the date of the first commit of a git repository
Date: 2025-06-14 14:53
Category: Tech
Lang: en
Tags: git, tips
Summary: Review of some git log powerful options

Today I wanted to know the birthday of my blog. I knew I've started it early 2024 but I wasn't sure anymore.
Looking at the first blog post would have been a solution, but I figured I would ask in natural language in Warp.

The first attempt gave me the first commit:

    :::bash
    $ git log --reverse --oneline | head -1
    34b1bc8 initialize Pelican blog setup

The key here is the smart combination of `--reverse`, `--oneline` and the pipe to `head 1`.

* `--reverse` tells git log to start from the first commit
* `--oneline` allows to simplify each commit record to a single line, without details. It is a shorthand for `--pretty=oneline --abbrev-commit` used together.
* the pipe to `head 1` cuts the output of git log to the first line, which is the oldest commit record.

Nice. But it didn't give me a date! Second attempt gave me my answer.

    :::bash
    $ git --no-pager log --reverse --format="%ad %h %s" --date=format:"%Y-%m-%d %H:%M:%S" | head -1
    2024-02-22 14:12:20 34b1bc8 initialize Pelican blog setup

Here same approach with `--reverse` and `head 1` but a few extra options are passed:

* `--no-pager` will only show as many lines as your terminal can show, and will **not** allow you to see more, as you usually by hitting Space.
* `--format` allows you to specify an output format, less known and a level deeper in the git documentation.
    
    * %ad is the author date (and it respects --date= option)
    * %h is for the abbreviated commit hash
    * %s is the subject, i.e. the commit message

* `--date=format` makes it possible to specify the date time format for the date field.

You can also play with the date format and ask for a "relative" date:

    :::bash
    $ git --no-pager log --reverse --format="%ad %h %s" --date=relative | head -1
    1 year, 4 months ago 34b1bc8 initialize Pelican blog setup

Git is an extremely powerful tool with a quasi-endless list of command-line options, and it's proven again with `git log`.

And this blog is 1 year and 4 months old 😊!

---

Sources: [Git log commit formatting](https://git-scm.com/docs/git-log.html#_commit_formatting)
