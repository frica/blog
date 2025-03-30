Title: Devbox, reproducible dev environments made easy
Date: 2025-03-30 23:00
Category: Tech
Tags: devbox, nix
Lang: en
Summary: First steps with the tool

I recently attended a Thoughtworks webinar about their [Technology Radar](https://www.thoughtworks.com/radar/) (cool idea, BTW) and I heard there about Devbox. After reading a bit about it on the [Jetify website](https://www.jetify.com/devbox), I decided to test it a bit.

## First steps

The installation is as easy as using `curl`:

    :::bash
    curl -fsSL https://get.jetify.com/devbox | bash

Now let's create a folder to test Devbox:

    :::bash
    mkdir devbox
    cd devbox/

We need to initialize the devbox environment:

    :::bash
    devbox init

This will create a devbox.json template in your folder.

Now let's add some packages. First we'll start with python. To include tkinter, which I sometimes need, I will add the package named `python-full` but bare python is also possible. If you don't specify a version, it will install the latest released version.

    :::bash
    devbox add python-full

Now if you open `devbox.json` you'll see that a package has been added to the packages section.
You can add more packages to include the tools you need for a clean functional development environment

    :::bash
    devbox add micro nnn git gh gh-dash lazygit difftastic

OK, we're are now ready to start the dev environment.

    :::bash
    devbox shell

The first time you run `devbox shell` will take a while to complete due to Devbox downloading prerequisites and package catalogs required by Nix. This delay is a one-time cost, and future invocations and package additions should resolve much faster.

You can test which version is installed. On my system I have the default ubuntu Python version 3.10.12, but after launching the devbox shell:

    :::bash
    python --version
    Python 3.13.2

To exit the devbox shell, just type `exit`.

## Additional features

Devbox also provides the option to perform actions when starting a new shell, via the `init_hook` property in the `devbox.json`. This is very powerful, as it can be used to further configure the development environment. For example, in a Node.js project, Devbox can automatically install npm packages.

For Python projects this is particularly helpful, as you can set up the virtual environment automatically at shell startup.

## Thoughts

I really like the idea:

* It reminds me of the Docker promise, without the complexity (for example with network settings) and the heaviness.

* It also abstracts the apparent complexity of Nix packages.

* I see it and use it as of sort of `makefiles` on steroids but easy to understand.

* Your regular tools are also available including environment variables and config settings. Example:

        :::bash
        git config --get user.name

* It seems ideal for onboarding new developers during the initial dev machine setup.

* But Devbox is not really cross-platform: on Windows it will only work if you use the WSL.

---

## Links

* [Devbox vs Docker: Lightweight, repeatable dev environments without container woes](https://www.jetify.com/blog/devbox-turn-a-1000-container-script-into-10-lines/)

* [A Long Journey to Cross Platform Developer Tooling Utopia (For Now)](https://eng.d2iq.com/blog/a-long-journey-to-cross-platform-developer-tooling-utopia-for-now/): nice comparison with make and asdf.

* [Upgrade your Development Environments with Devbox](https://alan.norbauer.com/articles/devbox-intro): comparison with Docker, chocolatey and Nix.

* [List of Python versions available on Nixhub.io](https://www.nixhub.io/packages/python-full)

* [Devbox — Create reproducible development environments](https://tech-talk.the-experts.nl/devbox-create-reproducible-development-environments-c7bf1af692a2)
