Title: Setting up a blog with Pelican
Date: 2024-02-23 10:47
Category: Tech
Tags: pelican, github
Lang: en

I will explain here the complete steps to build your static website with [Pelican](https://getpelican.com/) and deploy it on GitHub Pages.

But first, why use Pelican and not Wordpress or Dotclear, like back when I  started my first blog?

I was looking for:

* simplicity: Pelican uses markdown syntax in plain text files, site structure generated is simple and stylish enough
* ease of deployment: generating html from the markdown files is done by Pelican
* free solution: it can be hosted on GitHub pages, so it's perfect

## Installation

I used Ubuntu WSL on Windows because I had it setup from a Docker course that I followed recently and I quite liked it.

So in the Terminal, type

    sudo apt install python3
    sudo apt install pelican 
    sudo apt install pip

## Create a project

Go where you want to create your blog:

    mkdir blog
    cd blog
    pelican-quickstart

Leave the default values in the quickstart.

Create a file and write a dummy post:

    :::markdown
    Title: My First Review
    Date: 2024-02-23 10:20
    Category: Test

    This is a test.

Save it under blog/content.

Then run:

    pelican content

Your site has now been generated inside the output/ directory.

If you want to look at your generated site, run:

    pelican -l

## Hosting

In case you have a GitHub account, you can use the GitHub pages to host the generated website.

Make sure you are in your blog directory and initialize the git repo:

    git init

Commit all your files locally (except the files not needed for the git repo):

    echo "output/" >> .gitignore
    echo "__pycache__/" >> .gitignore
    git add -all
    git commit -m "Initialize blog"

**Note:**: the -A adds all unstaged files to the repo.

Setup your GitHub pages locally:

    pip install ghp-import
    ghp-import ./output -m "Initial upload"

**Note:** ghp-import will itself create your gh-pages branch and a new commit in it.

Go to you GitHub account and create an empty git repository with these properties:

    Name: Same as your local blog directory; in my case: blog
    Description: My blog
    Gitignore: None;
    Licence: None;
    Initialize with README: No

Set git remote

    git remote add origin git@github.com:<username>/blog.git

Push your gh-pages to GitHub

    git checkout gh-pages
    git push origin gh-pages

**Note:**
Normally, gh-pages should be set as your default branches now on GitHub.

Wait a few seconds and check your blog on:

    https://username.github.io/blog/

**Warning:** GitHub pages have of course limitations in site size and bandwith but that's good enough for me to write my articles and include some pictures.

---
**Optional:**

If you want to push your content and not only the generated site on GitHub, run:

    git add -A
    git commit -m "Initialize blog content"
    git push origin master

---

That's all folks!
