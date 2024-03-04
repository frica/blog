Title: Switching remote git repo URLs from HTTPS to SSH
Date: 2024-02-29 10:00
Category: Tech
Tags: git
Lang: en

Let's say, like me, you always forget to initialize/clone correctly the git repo with SSH and you did by mistake:

    git clone https://github.com/frica/<repo>.git <my folder>

Then when you want to push to main you will be blocked by GitHub:

    Username for 'https://github.com': ***
    Password for 'https://<user>@github.com': ***
    remote: Support for password authentication was removed on August 13, 2021.
    remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
    fatal: Authentication failed for 'https://github.com/<user>/<repo>.git/'

In fact the fix is extremely simple, don't bother with the link they give you.

Just type:

    git remote set-url origin git@github.com:<user>/<repo>.git

And BAM, your local repo is linked to the remote one with SSH as it should be 😊
