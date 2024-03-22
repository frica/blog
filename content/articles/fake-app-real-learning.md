Title: Friends challenge 1: Bromance application
Date: 2024-03-20 10:00
Category: Tech
Tags: github, nicegui, python, pytest
Lang: en


_Preamble: I suck at programming. In my friends group I probably am the nerdiest guy but I have been working with so many brilliant developers minds in my career that I have a low (or acute) self-esteem with regards to my programming skills. But truth is: I do develop for 20 years in one way or another and I like it._

---

What I like is a goal. Something that I know will be useful, for me or someone else. That includes self-learning by doing, making someone laugh, or making the world better in all kinds of way.

That's the main reason I worked in Healthcare IT for 20 years.

Recently I've been very curious to test myself and see if I could still **create something** with my development knowledge.

So a couple of days ago I asked my friends:

* What app do you need?
* What app do you miss?
* What app would be fun?

Shy at first, they woke up and the ideas started to pop up in the chat. Some waaaay too ambitious, some interesting, and lots of funny ones.

That's where the "arewebro" application comes from. A stupid UI that would reassure you that indeed you are "bro" (= friend) with someone from our friends group.

# UI is the key

I [tried NiceGUI]({filename}/articles/python-nicegui.md) already and I was impressed by its sleek design and its great documentation. The project itself is very active and maintained by at least 2 people, with extra contributors. I checked several other frameworks but I decided to build up on my first try with it.

After creating a simple command-line application to check if two names were in the same list and say "Yes, you are bro with other_friend" (lol), I decided to use NiceGUI to explore the possibilities.

Lucky enough the UI was very simple: 2 [text fields](https://nicegui.io/documentation/input) and 1 button. I started from the documentation and built the first prototype, calling the code I created for the CLI app.

Worked OK as a web application.

Then I wanted to load a text and an image if the two persons were friends and again success: `ui.image(...)` can load everything, even gifs. Very motivating start!

I added a second button to be able to clear the UI. There I learned about the `ui.refresh()` and the `@ui.refreshable` annotation. Took me a bit of time but eventually I understood. Another success.

Scrolling the documentation I found the so-called [native mode](https://nicegui.io/documentation/section_configuration_deployment#native_mode). By specifying `native=True` in the `ui.run` function, I got indeed a standalone application running.

Don't forget also the `Reload=false` to avoid the server kept up when you close the window in Native mode!

At that stage I was very satisfied and ready to learn something extra.

# Unit testing in Python

I went for Pytest and created my first unit tests in Python ever. Everything went fine because in PyCharm you can tell "this is my src folder". From the IDE, I could trigger the tests and get the results.

But of course as a CI/CD guy I wanted the tests to be executed in GitHub at every push and I was confident I could achieve it easily with the [GitHub actions]({filename}/articles/github-actions.md). What could go wrong, right?

Well, the Pytest source discovery was somehow a nightmare. For some reason it didn't understand where the source code is when executed in GitHub or in a shell, with my project tree structure. After reading 47 different answers on StackOverflow, I found out that I had to import in a specific way:

    :::python
    from src.utils import are_we_bro
    # have to import like this otherwise pytest plays dumb

    def test_arewebro_not_bros():
        """ test negative scenario """
        assert are_we_bro("Fabien", "Dark Vador") is False

and add a `conftest.py` in the project root directory:

    :::python
    pytest_plugins = ['src']

With that solution it finally worked with my Github action. Next.

# Standalone executable in Python

The next challenge was: since none of my friend will ever grab the code in GitHub and run it with Python, how can I distribute it as an executable?

## PyInstaller

There is a section about [NiceGUI and PyInstaller](https://nicegui.io/documentation/section_configuration_deployment#package_for_installation) in the official documentation so I went for it.

And that was painful. The `build.py` in the doc didn't work for me so I went command-line. It kind of worked then but my project static files (images) weren't displayed because they weren't included. The official [usage page](https://www.pyinstaller.org/en/stable/usage.html) has tons of parameters and options and I was a bit lost at first.

I had to learn how to handle static resources and it wasn't the best part of that project. I managed, using TOC files and [Tree()](
https://pyinstaller.org/en/v6.5.0/advanced-topics.html#the-toc-and-tree-classes) (see also [this](https://stackoverflow.com/questions/20602727/pyinstaller-generate-exe-file-folder-in-onefile-mode/20677118#20677118)):

    :::python
    exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    Tree('..\\img', prefix='img'),
    a.datas,
    ...)

I also had to adapt the path to the images in my code, depending if it was dynamically executed or run in the PyInstaller package (see [this](https://stackoverflow.com/questions/70685214/how-to-use-pyinstaller-to-include-images-in-the-exe
)). Eventually the code to get a random image has to be modified like this (see [documentation](https://pyinstaller.org/en/latest/runtime-information.html)):

    :::python
    def pick_random_image():
    """ pick a random image in the img folder
     :return filepath of an image
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        pa = Path(__file__) # needed for PyInstaller
        p = pa.joinpath("../img")
    else:
        p = Path("../img")
    files = [x for x in p.iterdir() if x.is_file()]
    if not files:
        return None

    random_file = random.choice(files)
    return resource_path(random_file)

Last point: when creating your package you typically want to hide the cmd window BUT to debug it can be useful to show it and you can do it by setting `noconsole=False` in the Spec file.

Spec files are pretty cool when you understand them BTW. Once I made a working one, all I needed to build my app is to run:

    :::python
    pyinstaller Bromance.spec

# Github is way more than a repo

I had all my pieces. Now I wanted to "do it right" and GitHub.

## GitHub release and tags

To make a release from a git code repository, it's a good idea to tag the repo at a certain moment. PyCharm handles it [easily](https://www.jetbrains.com/help/pycharm/use-tags-to-mark-specific-commits.html#push-tag) of course (if you notice the Push tags checkbox).

To create a release in **GitHub** and the related announcement, you **need** to have a tag. Because I wanted to mimic a serious workflow I followed the instructions [here](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository), drag & dropped my executable and created my first release announcement (see [here](https://github.com/frica/arewebro/releases/tag/v1.0.0)). I made it look real and I was quite happy about myself at that moment.

## Nicer Readme

To make your project look cool, you can use [GitHub badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge). Of course that's what I did, even if my project is not serious.

The most useful to me was to show if your latest tests run was successful. Since I had this information from the mini-CI pipeline, I added in the README markdown:

    :::markdown
    ![unit tests](https://github.com/github/docs/actions/workflows/test.yml/badge.svg)

where `test.yml` is the name of the GitHub action and voilà, a nice green check and a nicer README.

# Lessons learned

* GitHub is well-designed and easy to use. It's not quite like JIRA (maybe more repo-centric?) but I wouldn't mind working professionally with GitHub Enterprise.
* Packaging with Python is hard. Maybe packaging is hard in general but my experience was painful. I understand why so many Python devs go for web applications.
* It was really satisfying to overcome the challenges and to see a friend test this weird .exe and showing me a screenshot. 

At the end I thought:

> It was a fake application but some real learning.

# The code

Code is available [here](https://github.com/frica/arewebro/).

---

### Sources

* [NiceGUI documentation](https://nicegui.io/documentation)
* [PyInstaller usage](https://pyinstaller.org/en/stable/usage.html)