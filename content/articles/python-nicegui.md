Title: Python modern UI toolkit: NiceGUI
Date: 2024-03-01 23:00
Category: Tech
Tags: python, nicegui
Lang: en

Yesterday I discovered a modern-looking UI toolkit for Python called [NiceGUI](https://nicegui.io/) and I played around a bit.

Installation:

    pip install nicegui

Hello world application

    :::python
    from nicegui import ui
    ui.label('Hello world!')
    ui.run()

To go a bit further, I decided to use the [2024 Olympic Games open data](https://data.paris2024.org/) to load a list of all Olympic sites. First I downloaded locally the json file containing all sites for the Olympics and Paralympics Games.

    :::python
    import json
    from nicegui import ui

    columns = [
    {'name': 'site', 'label': 'Site', 'field': 'site', 'required': True, 'align': 'left'},
    {'name': 'sports', 'label': 'Sport(s)', 'field': 'sports', 'sortable': True, 'align': 'left'},
    ]

    link = 'paris-2024-sites-de-competition.json'
    # read file
    with open(link, 'r') as myfile:
        data = myfile.read()

    # parse file
    sites = json.loads(data)
    rows = []

    for site in sites:
    if site["category_id"] == "venue-olympic":
        rows.append({'site': site["nom_du_site"], 
                      'sports' : site["sports"]})
    
    ui.table(title="Olympic sites list", columns=columns, rows=rows, pagination=10)

    ui.run(title='JO Paris 2024')

And voilà! It will show in your web browser by default.

{% img {static}/images/nicegui_list.png 600 "My Sample NiceGUI application" "" %}

**Note:** extra header and footer are not in the sample code.
