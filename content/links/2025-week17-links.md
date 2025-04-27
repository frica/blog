Title: Interesting links - WK 17
Date: 2025-04-27 20:00
Category: Links
Tags: warp, python, ubuntu, netbsd
Lang: en
Summary: Week 17

* Spent a few evenings playing with [wrkflw](https://github.com/bahdotsh/wrkflw). Because of my testing, I learned a bit about Docker and Podman on Linux. I reported 2 bugs and they were both fixed in a couple of days. Nice to see the creator listening and fixing issues. It's a bit frustrating that I don't know Rust and can't really comment on the code without the help of a coding agent.

* [Warp](https://www.warp.dev/) has become my main terminal on all my computers. It just works. And a few times per month I'm able to spend my free credits to use their master feature: asking on the CLI in natural language 😉

* I upgraded my work PC to Ubuntu 24.04 (Noble Numbat). Pretty smooth experience. Then of course I tried the gnome extensions and tweaks to make it fancier. I realized pretty quickly that there was always something broken, inconsistent or not compatible with my monitors setup. Went back to defaults settings (except for some icons)...

* [Npm audit but for Python](https://pypi.org/project/pip-audit/). It uses the [Python Packaging Advisory Database](https://github.com/pypa/advisory-database).

* [Your software is rotting](https://terminal.ahumanfuture.co/posts/2025-04-19/your-software-is-rotting/). The introduction is a bit click-baitey, but the interesting piece is after, when the author explains how to slow down the decay of software.

About software dependencies:

> Every external dependency is a commitment and each evolves at its own pace, sometimes faster, sometimes slower than your software. Like any relationship, dependency management requires ongoing maintenance and can become a liability if not thoughtfully cared for.

About tech debt:

> In an industry where speed often determines success, the decision to remain completely debt-free can be unintuitively, a bad one - one that costs you opportunity, and market position. The ambition isn't to avoid technical debt entirely, but to manage it with the same care and intention as any other cost you take onboard.

* [NetBSD on the Wii](https://blog.infected.systems/posts/2025-04-21-this-blog-is-hosted-on-a-nintendo-wii/). Yes, some people are weird in an amazing way. This guy really hosted his blog on a Wii.

* Walrus operator! Advanced f-string string formatting! Plenty of big and small things to learn in [Advanced Python features](https://blog.edward-li.com/tech/advanced-python-features/). Example:

        :::python
        # The Walrus operator: define & evaluate all in one
        if response := get_user_input():
            print('You pressed:', response)
        else:
            print('You pressed nothing')

That's all, folks!
