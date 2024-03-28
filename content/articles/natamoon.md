Title: Friends challenge 3: Full moon, PWA and fly.io
Date: 2024-03-27 22:26
Category: Tech
Tags: docker
Lang: en

This is the third part of what I call the friends challenge: implement ideas my friends gave me 2 weeks ago (see [Part 1]({filename}/articles/fake-app-real-learning.md) and [Part 2]({filename}/articles/photolocator-flask.md)).

# How it started

This time my friend Natacha wanted something to quickly tell her the date of the next full moon. Why? Some obscure reasons :smile:. Nevermind it looked like something doable so why not?

# Backend

I wanted to learn about REST APIs and I was sure I could find an API to give all the information I needed and I could find some indeed. But they were often too complicated, not free or under conditions I couldn't or didn't accept. I gave up.

After hours browsing the Internet, I found a Reddit post mentioning a Python library (of course) that provides the moon cycles: [pyephem](https://rhodesmill.org/pyephem/). It's based on astronomical calculations (Jean Meeus’s Astronomical Algorithms) that are deemed serious. 

_Please note that [Skyfield](https://rhodesmill.org/skyfield/) from the same author should be preferred for new projects but I overlooked it._

Eventually the only thing I used from that library is:

    :::python
    date_today = datetime.date.today()
    date_time_full_moon = ephem.next_full_moon(date_today)

# Frontend

## tkinter

I wanted first some kind of widget that would be on the system tray in Windows. It looked like a good idea at first, specially when I found that I could change properties of tk to make it look almost OK.

But having a stable consistent behavior in the tray was a challenge for me and I gave up. It was time to make a web app again.

## PWA

Progressive Web Applications (PWA) are web applications that are delivered through the web, built using common web technologies including HTML, CSS, JavaScript, and WebAssembly. It is intended to work on any platform with a standards-compliant browser, including desktop and mobile devices. **So it does not require separate bundling or distribution**. Looked easier if I wanted my friends to test it.

I stumbled upon that [article](https://medium.com/@tristan_4694/how-to-create-a-progressive-web-app-pwa-using-flask-f227d5854c49) ([linked repo](https://github.com/Trigo93/flask_pwa_example)) explaining the requirements to make a Flask page PWA compatible and liked the idea! Indeed it's pretty simple.

## CSS

It was time to some styling in CSS since the page was super simple:

* I re-used some of my blog CSS, especially the fonts and the centering
* I learned that you can do rounded corners in pure CSS and did it
* I set a background-image for the fun

# Deployment on fly.io

I wanted to host it somewhere to make it available to my friends and test the PWA thing. Since [fly.io](https://fly.io/) is mentioned in many active repos nowadays it was time to try out!

IT'S SUPER SIMPLE.

Of course you need an account but the billing for a "Hobby" plan is close to nothing.

A good way to deploy is to provide a Dockerfile at the root of your repo. I could re-use the one I made from a previous Flask project.

Like literally the same (of course requirements.txt was different in bother projects but it doesn't matter in the Dockerfile)

And then install `flyctl`.

To do so, a few simple steps (Windows 11):

    :::bash
    winget search Microsoft.PowerShell
    powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
    fly auth signup

In the folder where the app is:

    :::bash
    C:\Users\my_user\.fly\bin\flyctl.exe launch 

That reads the Dockerfile and deploy "magically" on fly.io. Even the resulting URL looks good!

# Lessons learned

* "There is a package for everything in Python". Just... sometimes it's hard to find, old, not maintained anymore, not doing exactly what you want... Don't give up and look for alternatives. For instance I wanted to get a moon picture corresponding to the moon phase. Couldn't find it from the REST API, couldn't find it from a Python package. Who cares in my case? I just changed strategy.

* You can re-use a lot of your previously acquired knowledge when you use always the same technologies. In this case, the CSS and the DockerFile knowledge I gained from my previous app `photolocator`helped me to finish the app in a couple of hours, between my parent's obligations.

* Modern deployment software like fly.io are amazing. I assume this is way more complex in a realistic scenario but this was such a relief to use fly.io instead of the cluttered and complex Google Cloud Run interface.

* NASA has lot of incredible material, [pictures](https://svs.gsfc.nasa.gov/gallery/moonphase/) and [tools](https://moon.nasa.gov/moon-observation/daily-moon-guide/?intent=021) available for free. They're really good. I love them.

* My friend Natacha felt good that I actually delivered something for her. She might not use it ever but it doesn't matter 🙂.

# The code

Code is available [here](https://github.com/frica/natamoon/).

---

### Sources

* [The article](https://medium.com/@tristan_4694/how-to-create-a-progressive-web-app-pwa-using-flask-f227d5854c49) that gave me the PWA idea
