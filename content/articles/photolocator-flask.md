Title: Friends challenge 2: Picture Geolocalizer
Date: 2024-03-22 21:07
Category: Tech
Tags: github, flask, python, jinja, gcp
Lang: en

# How my journey started

([Part 1]({filename}/articles/fake-app-real-learning.md))

With my friends we play a game on WhatsApp called "Where am I?".

Someone posts a picture taken during a business trip or a holiday and the others need to guess where he/she was on the surface of the Earth. It's usually in France and it became a meme to answer "Châteauroux" because that city is not known to be the most beautiful in France (although some parts actually are).

So when I asked my friends which application they would like me to code, that came up quite quickly 🙂

It looked like something I could do with my technical level (compared to other more ambitious ideas) so I looked on the internet and found this [great article](https://auth0.com/blog/read-edit-exif-metadata-in-photos-with-python/). It explains how to read an image and its EXIF tags to extract the picture coordinates and retrieve the location.

_Yes, that's something Google Photos offers for ages._

# First step

Anyway, with the code in the article I could very quickly prototype a command-line version of the application and feed it some images to test it. It motivated me to continue my journey and wrap this code into something more usable for my non-techy friends.

I looked how I could make an Android app for it first because there are so many Python web frameworks that it was a bit overwhelming.

# Realizing I suck

After 1 hour upgrading/debugging Gradle and Kotlin dependencies on Android Studio's own sample application, **I realized I made a mistake**: I would never be smart/patient enough to learn mobile applications (but I learned how to enable developer's mode on Android and that's [funny](https://developer.android.com/studio/debug/dev-options)).

# Back to an old love

So I gave it all up and thought about [Flask](https://flask.palletsprojects.com/en/3.0.x/), a lightweight framework I used some years ago that stayed in my memory as simple and comprehensible for my limited brain.

But I needed a starting point. So I went looking for sample application in Flask I could inspire myself from. And I found [this article](https://dev.to/feranmiodugbemi/image-conversion-web-app-with-python-1e18) and the linked github repo. Appearance was nice from the start which was very motivating.

After a few adaptations I could merge my cli application into this Flask skeleton, not worrying about the outlook. Like for my [previous project]({filename}/articles/fake-app-real-learning.md) I wanted to do things correctly so I set up a [GitHub repo](https://github.com/frica/photolocator/) and looked for a way my friends could use it.

# The Deploy headache

This time the challenge was to make it available online for a cost of **0€**.

I finally chose Google Cloud Run:

1. I had quite some free credits on Google Cloud for doing a tutorial in the past weeks
2. I found this [article](https://medium.com/google-cloud/deploy-a-python-flask-server-using-google-cloud-run-d47f728cc864) saying it was simple for a Flask application
3. My future job uses it, so why not learn a bit upfront?

I read a few things (including [the official Google documentation](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)) and despite the very complex UI (for a noob like me) I managed to deploy it every time I push to my github repo.

**My friends tested it and it worked!**

_Some made it crash and I could debug and fix._

# Lessons learned

* Python really has an **amazing package ecosystem**: basically any processing task you want to do seems to have a package for it, that you can install with a simple `pip install`.

* There are some mandatory EXIF tags but the existence of the tags depends on so many factors that the application had to handle it carefully. For instance I have to use `get('tag')` instead of just accessing a tag member because as it's explained [here](https://exif.readthedocs.io/en/latest/usage.html#accessing-tags), it's handled more gracefully.

* My web app was working perfectly fine locally with the Flask web server but when packaged by Google to be deployed on their cloud, suddenly the syntax was incorrect. Hopefully [StackOverflow](https://stackoverflow.com/questions/72422403/python-syntaxerror-f-string-unmatched) came to the rescue. I think that `gunicorn` (the web server used by Google to package web apps) is somewhat more sensitive to syntax with single and double quotes.

* I could reuse the [Jinja template system](https://jinja.palletsprojects.com/en/3.1.x/) knowledge I learned before (from fiddling with my Pelican blog theme) when making a more modular set of web pages for my web app and it was very nice and easy.

* Web design is hard 😅: I tried some stuff with Bootstrap (what is used for the design of the app) and often I didn't get the behavior I wanted although my application is very simple.

* I'm very proud to be able to actually do stuff. Seeing that I can "assemble" knowledge from various sources and reach my end goal makes me feel good.

## TODO

I still am far from a semi-professional application (that was not the goal anyway), so there are a zillion things I could do to make it better. On my todo list I listed a few things:

* display EXIF info in a table
* view in Google Maps or OpenStreetMap
* add a GET server version API
* add proper logging
* create a docker file

# The code

Code is available [here](https://github.com/frica/photolocator/).

---

### Sources

* [The initial article about geolocalizing in Python](https://auth0.com/blog/read-edit-exif-metadata-in-photos-with-python/) from [Joey deVilla](https://www.globalnerdy.com/) (hope you find a job soon, man)
* [The Flask image uploader application](https://dev.to/feranmiodugbemi/image-conversion-web-app-with-python-1e18) from [FeranmiOdugbemi](https://github.com/feranmiodugbemi)
* [The Flask step by step deployment article](https://medium.com/google-cloud/deploy-a-python-flask-server-using-google-cloud-run-d47f728cc864): didn't work out of the box for me but gave me confidence.
