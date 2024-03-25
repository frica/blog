Title: How to center elements in NiceGUI
Date: 2024-03-25 23:00
Category: Tech
Tags: nicegui, quasar, tailwind
Lang: en

My pet project [arewebro](https://github.com/frica/arewebro) as useless as it was, deserved a little bit of extra love in terms of UI.

I noticed afterwards that the UI elements were annoyingly not centered in the frame I declared in Native mode.

Thanks to a Reddit post, I discovered that you can use a whole set of CSS properties inherited from Quasar and Tailwind. And indeed in the [documentation](https://nicegui.io/documentation/section_styling_appearance#styling) you can read:

> NiceGUI uses the **Quasar** Framework version 1.0 and hence has its full design power. Each NiceGUI element provides a props method whose content is passed to the Quasar component: Have a look at the Quasar documentation for all styling props. Props with a leading : can contain JavaScript expressions that are evaluated on the client. You can also apply **Tailwind CSS utility classes** with the classes method.

Since the UI is very simple, I just had to apply some extra properties to the parent element:

    :::python
    container = ui.column().classes('w-full items-center')

That tells the UI to:

* occupy the full width ([Tailwind property](https://tailwind.build/classes/width/w-full))
* center all items below in the hierarchy ([Quasar property](https://quasar.dev/layout/grid/column#example--horizontal-alignment))

Result:

{% img [img] {static}/images/arewebro_centered.png 400 "" "" %}
