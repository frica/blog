Title: .deb packages demystified
Date: 2024-11-11 18:00
Category: Tech
Tags: linux, tips
Lang: en
Summary: Learn how to create a .deb package from scratch with dpkg

Lately I took interest at how to create deb packages and I was amazed how **not** complicated it is. Is it the best format in 2024 for Linux packages? That's not sure, but it certainly works and it's easy to create when you understand the basics.

That's what I'm going to show here: the basics on how to create a deb package for your own application.

Let's say you have this dummy `hello` shell script as an application:

    :::bash
    #!/bin/bash
    echo "Hello, my friend!"

First, you need to follow a certain tree structure.

1. Create a root folder and a sub folder named DEBIAN.
In there you will place the control file.
2. For the application itself, you'll need to create a tree structure mimicking where you want to see it installed on the target computer.
Let's say you want to put your script in `usr/local/bin`: then you need to create the same tree structure under your root folder for the package.

You should end up with something like this:

    :::bash
    supportive-friend-pkg
    ├── DEBIAN
    │   └── control
    └── usr
        └── local
            └── bin
                └── hello.sh

Now what is the control file?

It's a simple text file containing the metadata for your package.
Note that there is no extension for this file.

    :::text
    Package: supportive-friend
    Version: 1.0
    Section: base 
    Priority: optional  
    Maintainer: Fabien Rica <fabien.rica@lol.com>
    Architecture: all
    Description: A message from a supportive friend
     <extended description over several lines>
    Homepage: https://frica.github.io/blog/

Let's see the explanation for some of the fields:

* _Section_: This field specifies an application area into which the package has been classified, for instance: devel, doc, editors, education, electronics, embedded, fonts, games, graphics etc.
* _Priority_: You can set the priority of the package, you can pick one of these types: required, important, important, optional, extra.
* _Architecture_ (mandatory field): You can define the architecture of the application: amd64, i386, or all if it applies for all architectures.

All fields are explained in the [official Debian documentation](https://www.debian.org/doc/debian-policy/ch-controlfields.html). They all follow some rules and some of them, like _Version_ or _Depends_ (not used in my example) are pretty important if you want to really distribute your application, so watch out!

Now we're ready to build the package.

First, install the `dpkg` package that will do all the magic:

    :::bash
    sudo apt install dpkg

Then build the package:

    :::bash
    cd ~
    dpkg-deb --build supportive-friend-pkg

You will see the newly created `supportive-friend-pkg.deb` in the folder.

To inspect the package newly created, use the `-info` (or `-I`) command:

    :::bash
    dpkg-deb --info supportive-friend-pkg.deb

It will show some info about the size of the package and the information of the control file.

If you want to install the package, you can use `dpkg` with sudo:

    :::bash
    sudo dpkg -i supportive-friend-pkg.deb

You can also use `sudo apt install` of course.

Then you can navigate to `/usr/local/bin` and you will see the script `hello.sh`.

# One step further

Obviously, my script is very limited.
In the real world, you'll need to:

* carefully describe the dependencies in the control file,
* mimick the entire tree structure of your app: you will end up with probably something in `opt/`, something in `var/log/`, maybe something in `etc/` if you want to start a service automatically...,
* set up a pre-install script (`preinst`) and/or a post-install script (`postinst`) together with some pre-install or postinstall cleanup  (`prerm` and `postrm` scripts) (see [the related section in the Debian doc](https://www.debian.org/doc/debian-policy/ch-maintainerscripts.html)),
* add a shortcut or a launcher for your application,
* ...


# Limitations

I noticed there are some limitations about the deb packages, inherent of the format:

* The name of the application is always lower case.
* You can not add an icon, nor screenshots to show nicely in any of the .deb installer GUI. If your goal is to have a nice description like the ones you can see in the Ubuntu Store, you will need to create a `snap` package and publish it on [snapcraft.io](snapcraft.io) 😅.
