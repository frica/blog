Title: Switching to European Digital Services
Date: 2026-02-14
Category: Tech
Tags: privacy, digital-sovereignty
Slug: switching-to-european-digital-services

The recent geopolitical changes have made me reflect on my dependence on US-based services. While most European companies are severely tied to MS, AWS and Google, I don't see why I couldn't migrate my personal data.

Requirements: all services must work on Linux and Windows, be based and hosted in Europe, and be ethical.

## Web Browser

User of Firefox [since it was called "Phoenix"](https://www.andrewturnbull.net/mozilla/historyfx.html), I've been concerned about Google Chrome's market dominance. The current problem is that Mozilla Foundation is also US-based. So I'm trying [Vivaldi](https://vivaldi.com/), a browser made in Iceland by one of Opera's co-founders. While this change may be less important than might appear (all modern browsers have the features I need), it's interesting to explore what Vivaldi offers.

## Email

As a longtime GMail user, I created a [Proton Mail](https://proton.me/mail) account a few months ago as a secondary mailbox. So far, no complaints, though I've received only a few emails there until now. I have no idea how the spam filter works.

I've also looked into [Mailo.com](https://www.mailo.com) (France), which is interesting in terms of inbox size and price:

- **Mailo Premium Mail**: €1/month - 20 GB + 5 GB Cloud 
- **Proton Mail Plus**: €3.99/month - 15 GB storage (+ calendar and Drive)

## Notes

Satisfied [Obsidian](https://obsidian.md/) user, I have no plans to switch. [Joplin](https://joplinapp.org/) is French and looks very similar, but Obsidian is based in Canada, so I'm good there. I pay annually for the Standard 1 Gb plan.

I still have to move away from Google Keep. As a simple todo and quick reminder app, it has the functionalities needed and it's snappy. I should explore whether I can adapt my habits and move this to Obsidian.

## Blog

I use GitHub to host my blog content in git and GitHub Pages to display my static site. I'm planning a migration to [Codeberg](https://codeberg.org), an open-source Git forge from Germany (free). Some friction is expected (GitHub makes everything so easy), but this migration makes sense because it's my content.

Resources:

- A good feedback about moving from [GitHub to Codeberg](https://itiquette.codeberg.page/posts/github-to-codeberg/)
- [Codeberg Missing Features](https://itiquette.codeberg.page/posts/codeberg-missing-features/)
- Another article about [Migrating from GitHub to Codeberg](https://www.andrlik.org/dispatches/migrating-from-github-to-codeberg/)
- Other notes about [Migrating from GitHub to Codeberg Notes](https://xrstf.de/notes/migrating-from-github-to-codeberg/)

## Git Forge

A few of my hobby projects rely on GitHub Actions, so I'm keeping those projects in GitHub. However, most projects could easily move to Codeberg. The annoying part is managing extra git credentials and switching between repositories locally across all my computers.

I'll also miss the `gh` CLI tool.

## Music Streaming

Spotify is Europe-based, but the company supports certain US political positions I disagree with, so I've switched end of last year to [Qobuz](https://www.qobuz.com/) (France). No major complaints so far.

## Video Streaming

I'm using Netflix and I have no plans to switch. Not that I'm 100% happy with it, but overall each family member finds something to watch here. It costs me 17,99€ per month.

## Storage

My dependency on Google Drive and Google One is a significant issue. It's critical for me to move away from it, and the scale of this migration is daunting. I'm a paying user for two Google One accounts, which I'll need to take into account in my migration costs.

I've looked into [Filen](https://filen.io) (Germany) for pure data storage, and the prices are attractive. However, it doesn't support photo albums: it's strictly file storage in folders. That's fine for Google Drive documents, but a bit more problematic for photos. I have 20 years of pictures that require safe backup and the possibility to organize by albums.

[pCloud](https://www.pcloud.com) (Switzerland) is very interesting with its interface that looks like Google Photos, its automatic import and lifetime plans.

Proton also offers Proton Drive, but I'm hesitant to switch everything to Proton due to their pricing and Linux support limitations. Proton Unlimited costs €9.99/month for 500 GB.

Infomaniak (Switzerland) also has an integrated solution, but I kind of dislike their branding. Still, their [prices are very attractive](https://www.infomaniak.com/en/ksuite/myksuite/prices).

I should also explore Nextcloud (Germany). I recently closed my CozyCloud/Twake account (France), because I wasn't using it. That shows how very accustomed to Google's ecosystem I am...

## Hosting

I wish to finally get some presence on the internet. I'm still investigating the best solution. The candidates are:

- **Hostinger** (Lithuania): web hosting
- **Hetzner** (Germany): cheap VPS

There are also self-hosted solutions like the **[Freedom Box and Yunohost](https://www.zdnet.com/article/personal-digital-sovereignty-choices-free-linux-servers/)**. It's attractive but I know I won't have the time and energy to maintain it.

## Domain Name

There are many European domain registrar alternatives. I still haven't decided on my domain name, so this is on hold.

## AI/LLM

I received a 6-month Mistral Pro subscription as a gift, and I really enjoy it as a daily AI chatbot. Mistral's Le Chat Pro costs nevertheless €18/month.

At work, I use many excellent US-based tools. I pay for my personal [warp.dev](https://www.warp.dev/) subscription ($180/year) but I'm not sure I will renew it.

I still need to find a good local open-source model for coding assistance, from Europe ideally (one can dream). I would like to avoid LLMs from China. They seem good but hey, you never know.

## Two Strategies

I see 2 strategies:

1. **All-in-one approach**: Proton / Infomaniak, Mistral
2. **Separate services approach**: Filen/pCloud, Proton/Mailo, Nextcloud, Mistral

## Efforts Required

- Download everything, upload everything
- Switch all contact email addresses from other subscriptions
- Get used to new applications
- Move family to the new services

## Financial Costs

### Scenario 1: single replacement for Google

| Service | Today | Tomorrow | Cost |
|---------|-------|---------|------|
| Cloud | Google | Proton | + €120 |
| Storage | Google One x2 | see above | - €44 |
| Notes | Obsidian<br>Notes | Obsidian | = ($48) |
| Git forge | GitHub | Codeberg | = |
| Web browser | Firefox | Vivaldi | = |
| Music | Qobuz | Qobuz | = (€210) |
| AI | Mistral (free)<br> Warp | Mistral | + €216 - $180 |
| Hosting | None | ? | ? |
| Domain | None | ? | ? |

### Scenario 2: several services (example)

| Service | Today | Tomorrow | Cost (yearly) |
|---------|-------|---------|------|
| Email | Google | Mailo | + 12€ |
| Storage | Google One x2 | Filen | + €20 - €44 |
| Notes | Obsidian<br>Notes | Obsidian | = ($48) |
| Git forge | GitHub | Codeberg | = |
| Web browser | Firefox | Vivaldi | = |
| Music | Qobuz | Qobuz | = (€210) |
| AI | Mistral (free)<br>Warp | Mistral | + €216 - $180 |
| Hosting | None | ? | ? |
| Domain | None | ? | ? |

## Conclusion

Technically, this is possible. Financially, I have to accept that these services linked to my "degooglisation" rightfully require payment, which can add up to a certain amount annually. I'm estimating the switch will cost 50-150€ per year (personal cloud + AI), **or** 100-200€ if I also choose a domain and hosting/VPS somewhere. I should also consider that I'll likely need to keep at least one GMail account, and I'll have to inform everyone about my email change and update all my service configurations to use the new email address.

Resources:

- [European Alternatives](https://european-alternatives.eu/blog)
- [Proton Europe Tech Watch](https://proton.me/fr/business/europe-tech-watch)
