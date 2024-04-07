Title: Friends challenge 4: Lasagnapp or my styling experiments with NiceGUI
Date: 2024-04-07 23:00
Category: Tech
Tags: python, nicegui, cooking
Lang: en

# How this project started

([Part 1]({filename}/articles/fake-app-real-learning.md))
([Part 2]({filename}/articles/photolocator-flask.md))
([Part 3]({filename}/articles/natamoon.md))

During my sabbatical time after my Agfa Healthcare career, I did a few things.

Oh, nothing crazy.

Repaired properly my arm, did yoga, went for many school activities with my kids, rented a van for a week with the family, that sort of things.

And I learned **how to cook lasagnas**. Not just from a book, but with an Italian friend of mine, Vittorio, a fantastic cook who makes the best [pizza "al taglio"](https://en.wikipedia.org/wiki/Pizza_al_taglio) and lasagnas of Gent, Belgium.

I took me HOURS of work but my 4th attempt was actually a success: everyone loved it at home.

Of course I bragged about it with my friends.

Of course my friends made fun of me, jobless and obsessed by lasagnas.

So when I asked recently about what I could code as applications, one of them (Alex) came only with a name: "Lasagnapp". And I knew it was a good name 😁

# The "recipe" control

NiceGUI is a very complete UI framework for Python. A couple of times I thought "I'm sure they don't have this control ahah"... and it was covered in details in the documentation.

One day, I saw the NiceGUI [`stepper`](https://nicegui.io/documentation/stepper) control and I immediately said to myself it would be perfect for a cooking recipe.

I connected the dots in my brain and decided to make my Lasagnapp.

# Very simple app but styling headache

The application itself is dumb as most of my recent experiments and was the occasion to put on paper the pieces of recipe I gathered on separate Google Keep notes. The control does all the job and I wasn't planning to add any other feature (except translations).

The default NiceGUI style (white and blue) wasn't great in my case. In my app arewebro, it didn't matter so much but I wanted this time to compensate the void of the app by a nicer styling.

Aaaaand it was _painful_.

You have to realize that NiceGUI is based on Quasar web components AND Tailwind styles. I know none of them, although they seem well-known in the modern Web world. That allows NiceGUI to have a very modular and solid frontend (without re-inventing the wheel) but it also abstracts totally the different attributes for the developer.

If you want something else than the default NiceGUI look and feel, you need to dive into the extensive Quasar and Tailwind documentation. 

# I'm glad I can change in my IDE and just reload my page 

For a small brain like mine, who more or less understands html and CSS-styling, that's a whole new gymnastic.

For example, you want a footer that is black letters on white background:

    :::python
    with ui.footer().style('background-color: white') as footer:
        ui.label('Copyright (c) 2024 Fabien Rica').style('color: black; font-size : 14px')

Ok so you can use `.style(...)` to each components with the usual CSS attributes. No big deal.

But let's say you want your stepper control to be vertical and occupy the full width:

    :::python
    with ui.stepper().props('vertical').classes('w-full') as stepper:

Then you need to use `.props(...)` (Quasar) and `.classes(...)` (Tailwind).

You want to use a `tree` control to expand and collapse text? Yes NiceGUI has one. But if you want a particular style with no lines between node and leaves and almost no vertical padding, then go check the Quasar doc and try something like this:

    :::python
    ui.tree([{'id': ' Step 1', 'children': 
        [{'id': 'instruction 1'},
        {'id': 'Instruction 2'}]},
    ], label_key='id').props("simple dense no-connectors")

Next level, you want a special font size for the Step 1 label of the tree? Then you need to _overload the Quasar control property_ thanks to `ui.add_css` (introduced in NiceGui 1.4.20):

    :::python
    ui.add_css('.q-stepper__title { font-size: 18px; color: black}')

NiceGUI maintainers are aware of the issue. In fact one of the pinned discussion on their great GitHub repo is called "How to simplify styling?" and shows they are taking it seriously. The different options are even quite properly [documented](https://nicegui.io/documentation/section_styling_appearance).

A few things have been added for the people like me, coming from a more old-school way of styling web pages:

* `ui.add_css()` as mentioned above, to set up CSS properties
* `ui.add_head_html()`: to write html code in the head of your html, to define fonts for instance
* `ui.colors()`: to define the primary/secundary colors to be used in the app
* `ui.query()`: to set up CSS properties for specific html elements like

        :::python 
        ui.query('body').style('background-color: #ffeedd')

You see? it's VERY flexible. It's actually great! 

But it's scattered, you can reach your goal in different ways and sometimes difficult to know where to look.

Someone wrote on Bluesky that NiceGUI people, as backend dev, hate so much designers that they tried to abstract all design aspects to get rid of them.

I disagree but I see where this comes from.

Anyway, this is not a rant. Most of my issues come from my ignorance and I like this framework a lot. And I'm personally proud of the result!

(Also the maintainers are [very reactive](https://github.com/zauberzeug/nicegui/discussions/2839), probably the best project I follow on GitHub with that regard.)

# The code

Code is available [here](https://github.com/frica/lasagnapp/). Have a look if you want some basic styling examples!

App can be seen [here](https://lasagnapp.fly.dev/) (in French).
