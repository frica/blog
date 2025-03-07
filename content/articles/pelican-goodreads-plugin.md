Title: Displaying reading activity on your blog
Date: 2025-03-06 23:00
Category: Tech
Tags: pelican, reading
Lang: en
Summary: How to install the Goodreads Activity plugin for Pelican

It's been more than a year than I created this blog and I missed its birthday! I always wanted to focus on the writing and less on the styling and even if I miss sometimes fancy features in other blog engines, I cherish my simple static blog. But I saw on another blog a list of **"Currently Reading"** books and I thought it would make sense to integrate something like this. 

## There's a plugin for everything (almost)

Turns out it's not that hard, since someone already took the time to create a Pelican plugin named **Goodreads Activity**. Thank you [Talha Mansoor](https://github.com/talha131)!

The list of available Pelican plugins can be found [here](https://github.com/getpelican/pelican-plugins). Unfortunately the Goodreads Activity plugin has not been migrated to the new [Pelican Plugins](https://github.com/pelican-plugins) organization, "a place for plugin authors to collaborate more broadly with Pelican maintainers and other members of the community".

Which means you need to do a little bit of extra work to make it work, compared to the [sitemap](https://github.com/pelican-plugins/sitemap) plugin, for example. Let's dive in.

## Include the plugin in your blog repository

* Clone the `pelican-plugins` repo and copy the `goodreads_activity` folder under or download the 3 files needed for the plugin.
* Copy the folder to a folder named `plugins`, at the same level as your `content` folder.
* Commit and push to your repository.

## Plugin configuration

Add in your pelicanconf.py:

    :::bash
    PLUGIN_PATHS = ['plugins/']
    
    PLUGINS = ['liquid_tags',
               'sitemap',
               'goodreads_activity'] <!-- add this -->

    GOODREADS_ACTIVITY_FEED='RSS_LINK_TO_YOUR_FEED'

`GOODREADS_ACTIVITY_FEED` should point to the activity feed of your bookshelf.

To find your self's activity feed,

* Go to [Goodreads](https://www.goodreads.com/) and login
* Click on My Books in the top navigational bar
* Select the bookshelf you are interested in from the left hand column
* Look for the RSS icon in the footer of the page. That's the link you need to copy.

## Dependencies

Add the `feedparser` package in your requirements.txt, it's needed by the plugin:

    :::bash
    ...
    feedparser==6.0.11

## Blog integration

To display the bookshelf, you'll need to a piece of code in the `jinja` template, as explained in the plugin [README](https://github.com/getpelican/pelican-plugins/blob/master/goodreads_activity/Readme.md).

I chose to modify my "About" page and I changed my theme `page` template to show the cover images (medium size) with each image being clickable:

    :::html
    {% if GOODREADS_ACTIVITY_FEED %}
        <h2>Currently reading</h2>
        <div class="book-list">
        {% for book in goodreads_activity.books %}
            <a href="{{book.link}}" target="_blank" class="book-item">
            <img src="{{book.m_cover}}" class="book-cover"/>
            </a>
        {% endfor %}
        </div>
    {% endif %}

## Deployment

* If you're using a github action to deploy you need to install the additional package by adding `-r requirements.txt` (see [Pelican documentation](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow)) in your GitHub action.

How it looks in my pelican.yml:

    :::yml
    requirements: "pelican[markdown] 
        pelican-liquid-tags 
        pelican-sitemap 
        -r requirements.txt"

And that should all work nicely!

{% img {static}/images/currently-reading.png 600 "Display of the bookshelf in Pelican" %}
