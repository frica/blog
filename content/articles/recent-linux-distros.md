Title: 2026, the year of the desktop for Linux?
Date: 2026-01-08
Category: Tech
Tags: linux, distro
Lang: en
Summary: A quick overview of some modern Linux distributions

During my Christmas break I had one afternoon free from family duties. And what did I do? Of course I spent some time "geeking"!

Long-time Ubuntu and Gnome user, I'm pretty used to it. I like the overall consistency and the fact that it just works. But I was curious 🙂

I installed a variety of Linux distributions to see how the landscape is evolving. I did not spent a lot of time testing them, I'm using Linux for enough time to know quickly if I would like to use a distribution daily: tt has to be **frictionless**, consistent, and if it is beautiful, even better.

Here is a list of the ones I took for a spin: Pop!_OS, Zorin OS, Linux Mint, elementary OS, Bazzite, CachyOS, and EndeavourOS.

To test all of them except Mint, I used the extremely neat [Gnome Boxes](https://apps.gnome.org/Boxes/) with 8GB of RAM and a disk size of 30 GB.

## Pop!_OS

* **First Release:** October 2017
* **Latest Release:** 24.04 LTS
* **Base:** Ubuntu
* **Package Management:** APT, Flatpak
* [Site](https://system76.com/pop/)

Pop!_OS is developed by System76. It features a customized GNOME desktop (COSMIC) designed for workflow efficiency.

![Pop!_OS Desktop]({static}/images/linux-distribs/PopOS.png)

It looks very nice and consistent. I liked the tiling mechanism that I could activate easily from the top toolbar. It was all in all the best experience from all distributions.

## Zorin OS

* **First Release:** July 2009
* **Latest Release:** 18
* **Base:** Ubuntu
* **Package Management:** APT, Snap, Flatpak
* [Site](https://zorin.com/os/)

Zorin OS focuses on being a user-friendly alternative to Windows and macOS, offering a familiar interface and ease of use.

![Zorin OS Desktop]({static}/images/linux-distribs/ZorinOS.png)

![Zorin OS Applications]({static}/images/linux-distribs/ZorinOS-3.png)

The design is nice. But what's with the extra options only in the paid version? I didn't like that, even if the price for the full version is like 50$.

## Linux Mint

* **First Release:** August 2006
* **Latest Release:** 22.2
* **Base:** Ubuntu
* **Package Management:** APT, Flatpak
* [Site](https://www.linuxmint.com/)

Linux Mint is a classic favorite known for its stability and the Cinnamon desktop environment. It provides a traditional desktop experience out of the box.

I can't remember what grudge they originally held against Ubuntu, maybe it was against `snap`, maybe it was `systemd`... Anyway. It looks nice, it's consistent, a bit like a 2015 clean, workable Linux. My main disapointment is that on my old laptop (i3, 4GB) it is pretty slow. It's actually not made for old machines. There is nothing minimal in Gnome today anyway, not really their fault.

## Elementary OS

* **First Release:** March 2011
* **Latest Release:** 8.1
* **Base:** Ubuntu
* **Package Management:** APT, Flatpak (AppCenter)
* [Site](https://elementary.io/)

Elementary OS focuses on a curated and polished experience with its own Pantheon desktop environment.

![elementary OS Desktop]({static}/images/linux-distribs/ElementaryOS.png)

In practice, it's looks like a MacOS design from 2010. There is no tiling (at least by default). Also where is my button to minimize a window? I was not impressed at all.

## Bazzite

* **First Release:** 2023
* **Latest Release:** 43.20260101 (follows Fedora)
* **Base:** Fedora Atomic (Universal Blue)
* **Package Management:** rpm-ostree, Flatpak
* [Site](https://bazzite.gg/)

Bazzite is extremely hype at the moment. it's an OCI image for Fedora Atomic Desktops, designed specifically for gaming. It's utilizing an immutable file system (not that it matters to me). I was only interested in the gaming aspect, since it ships with Steam and Lutris.

Unfortunately in my first try it was very slow in my emulated version. Second try on my work laptop was much better. The desktop is minimalistic and very polished. Their app store (Bazaar) is neat.

![Bazzite Desktop]({static}/images/linux-distribs/Bazzite-1.png)

(Extremely cool default background wallpaper.)

![Bazzite wallpaper]({static}/images/linux-distribs/Bazzite-2.png)

## CachyOS

* **First Release:** 2021
* **Latest Release:** 25.11.29 (Rolling Release)
* **Base:** Arch Linux
* **Package Management:** Pacman
* [Site](https://cachyos.org/)

CachyOS is another distribution often mentioned for gaming purpose, in general optimized for performance. This time, it's Arch-based and it comes with KDE by default.

![CachyOS Desktop]({static}/images/linux-distribs/CachyOS.png)

In my first try, it was so slow in my emulated version that I gave up. But second time on my beast laptop with a real GPU, performance was acceptable. I realized I don't like KDE anymore (days of me liking Suse are long gone). I liked the fact that Alacritty is there by default though.

## EndeavourOS

* **First Release:** July 2019
* **Latest Release:** Ganymede
* **Base:** Arch Linux
* **Package Management:** Pacman, Flatpak, AUR
* [Site](https://endeavouros.com/)

EndeavourOS is an Arch-based distribution that "aims to provide a user-friendly Arch Linux experience". The installer is simple and works well. It comes with multiple desktop environment options: I chose Gnome.

![EndeavourOS Desktop]({static}/images/linux-distribs/EnadeavourOS.png)

They got me with the space wallpaper but the UI feels clunky and inconsistent. Not impressed. The website also doesn't look super professional (which is, in a world of bullshit, kind of refreshing).

## Conclusion

I will not immediately hop to another distro! But if I had to I would consider Pop!_OS for a work computer and Bazzite/CachyOS for a gaming workstation.

That's all folks!
