Title: Tuning my Pelican usage and setup
Date: 2024-02-25 10:19
Category: Tech
Tags: pelican, github
Lang: en

Here are some things I learned after a few days working with Pelican (read [here]({filename}/articles/setup_pelican.md) an explanation about the initial setup).

# ghp-import

 The useful [ghp-import](https://pypi.org/project/ghp-import/) tool is a non-standard git command mentioned in every article about Pelican setup. A quick look at the `--help` command reveals interesting options.

I now use:

    ghp-import -op ./output -m "Upload content"

The `-p` option pushes to origin/master, which spares you an extra command.

The `-o` overwrites the history of the gh-pages.

From the help:

> The -o option will discard any previous history and ensure that only a single commit is always pushed to the gh-pages branch. This is useful to avoid bloating the repository size and is **highly recommended**.

# Pelican plugins

I discovered the amazing world of Pelican plugins. While I don't need most of them at the moment, I still configured my blog to use one of them, liquid_tags for a easier media integration.

You can configure the plugins in your `pelicanconf.py`:

    PLUGIN_PATHS = ['pelican-plugins']
    PLUGINS = ['liquid_tags']
    LIQUID_TAGS = ["img", "literal", "video", "youtube",
               "vimeo"]

Example:

{% vimeo 364868276 %}

# Date format

I always disliked the US time format. But as my blog is configured in English, I override it to display it to my taste. In my `pelicanconf.py` I added:

    # European date format
    DEFAULT_DATE_FORMAT = '%d-%m-%Y'


# Syntax highlighting

Since I have the ambition to post articles with code, I wanted to have syntax highlighting. Good news, Pelican uses the extension codehilite (that uses [Pygments](https://pygments.org)). It works out of the box without configuration.

[This link from the Pelican FAQ](https://docs.getpelican.com/en/latest/faq.html#i-m-creating-my-own-theme-how-do-i-use-pygments-for-syntax-highlighting) explains everything you need to know, **if you create your new theme**.

I wanted to reuse the `notmyidea` and only extend the css to use my own pygment.css to use the `dracula` colorset, but I didn't succeed...

Anyway it looks like this by default with the default theme:

    :::python
    # This program adds two numbers
    num1 = 1.5
    num2 = 6.3

    # Add two numbers
    sum = num1 + num2

    # Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))