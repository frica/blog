Title: Adding a favicon to a pelican site
Date: 2024-03-25 00:02
Category: Tech
Tags: pelican
Lang: en
Status: draft

After working this weekend on my new blog theme and getting very satisfying results, I wanted to polish a bit more and add a favicon (and get rid of the error at startup saying that no favicon was found).

I naively assumed that adding in the configuration file: 

    :::python
    FAVICON = "favicon.ico"

and putting my favicon in my (already defined as static) images directory would be enough. 

_But no._

To make the site html code points to the correct location you have to:

* create another folder at the root (content): I named it extra
* put the favicon there
* add some code to `pelicanconf.py`

    :::python
    STATIC_PATHS = ['images', 'extra', 'pages/assets']
    EXTRA_PATH_METADATA = {
        "extra/favicon.ico": {"path": "favicon.ico"},
    }

* in your `base.html`, below the title tag, add this line:

    :::html
    <link rel="icon" type="image/x-icon" href="{{ SITEURL }}/favicon.ico">

Seems overly complex for a simple favicon but it does the trick!

Note: The favicon was created thanks to [Favicon.io](https://favicon.io/).