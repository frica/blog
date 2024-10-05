Title: Snap sucks
Date: 2024-10-05 12:00
Category: Tech
Tags: ubuntu, snap, rye, textual
Lang: en
Summary: How a simple install procedure turned out to be an unnecessary hassle on Ubuntu because of snap

# Posting, a piece of geek art

[Posting](https://posting.sh/) is a software created by Darren Burns, who works for Textual. It's a clone for Postman but terminal-based. I consider it as the killer demo application for [Textual](https://textual.textualize.io/), the Python TUI framework used under the hood. I like the look, the usability and the fact that it's just a joy to use, while feeling like Neo in Matrix.

# Installing on Ubuntu 22.04

So interesting enough, it requires Python 3.11, which is not installed by default on Ubuntu 22.04, which has 3.10 as default. 

No problem in these times where alternatives for virtual environments start to rise, I figure there would be a way to handle it nicely. The website mentions 2 options:

* pipx 
* rye

Now I know a bit about pipx from it but on my machine it was not yet installed. Additionally rye was recommended by the author so I became curious and I chose to check this out.

The [website](https://posting.sh/guide/#rye-recommended) explains:

    :::bash
    # Install Rye (on MacOS/Linux only - Windows users see below)
    $ curl -sSf https://rye.astral.sh/get | bash
    
    # install Posting
    $ rye install posting

Another fancy application procedure with bash script, OK. Let's try to first install rye...

    :::bash
    This script will automatically download and install rye (latest) for you.
    ######################################################################## 100.0%
    gzip: /tmp/.ryeinstall.5SKpZcDT.gz: No such file or directory

# Not today, Ubuntu, not to me

Very surprising that the "recommended" procedure wouldn't work, I dug into the issue and 5 minutes later found out it's [because of the way curl is installed/packaged on Ubuntu](https://askubuntu.com/questions/1356327/cant-write-to-a-hidden-path-using-curl) 🤦🏼. So you need to first uninstall the `snap` curl and reinstall it with `apt`:

    :::bash
    $ sudo snap remove curl
    $ sudo apt install curl

Then it works like a charm:

    :::bash
    $ curl -sSf https://rye.astral.sh/get | bash
    This script will automatically download and install rye (latest) for you.
    ######################################################################## 100,0%
    Welcome to Rye!
    ...
    All done!

And you can install `posting`:

    :::bash
    $ rye install posting
    Resolved 35 packages in 1.74s
    Built pyperclip==1.9.0
    Prepared 34 packages in 450ms
    Installed 35 packages in 9ms
    + annotated-types==0.7.0
    + anyio==4.6.0
    + brotli==1.1.0
    + certifi==2024.8.30
    + click==8.1.7
    + click-default-group==1.2.4
    + h11==0.14.0
    + httpcore==1.0.6
    + httpx==0.27.2
    + idna==3.10
    + linkify-it-py==2.0.3
    + markdown-it-py==3.0.0
    + mdit-py-plugins==0.4.2
    + mdurl==0.1.2
    + platformdirs==4.3.6
    + posting==1.13.0
    + pydantic==2.9.0
    + pydantic-core==2.23.2
    + pydantic-settings==2.4.0
    + pygments==2.18.0
    + pyperclip==1.9.0
    + python-dotenv==1.0.1
    + pyyaml==6.0.2
    + rich==13.9.2
    + setuptools==75.1.0
    + sniffio==1.3.1
    + textual==0.79.1
    + textual-autocomplete==3.0.0a9
    + tree-sitter==0.20.4
    + tree-sitter-languages==1.10.2
    + typing-extensions==4.12.2
    + tzdata==2024.2
    + uc-micro-py==1.0.3
    + watchfiles==0.24.0
    + xdg-base-dirs==6.0.1

    Installed scripts:
    - posting

    note: additional scripts were encountered in non-installed dependencies.

And TADA:

{% img {static}/images/posting_app.png 800 "Posting" "" %}

