Title: Glow, a command-line Markdown viewer
Date: 2026-02-18
Category: Tech
Tags: markdown, cli, go
Slug: glow-markdown-viewer
Summary: Reading markdown files in the terminal

[Glow](https://github.com/charmbracelet/glow) is a command-line markdown viewer created by [charmbracelet](https://charm.land), whose mission is simply to "make the command line glamorous" 🦄.

It renders markdown files in your terminal with proper formatting, syntax highlighting, and a clean reading experience. The difference with editing with a pure (decent) cli text editor like `micro` (see this previous [article]({filename}/articles/terminal-setup.md)) is subtle but I like it.

## Installation

Install Glow using snap:

```bash
sudo snap install glow
```

Alternatively, you can install it via other package managers depending on your system (including `.deb`).

## Basic Usage

### View a file

Simply pass the markdown file path to glow:

```bash
glow your-file.md
```

### Set a maximum width

You can use the `-w` flag to set the maximum width (useful for wrapping long lines):

```bash
glow python-tips.md -w 60
```

### Browse files

To list and browse available markdown files in the current directory, simply type:

```bash
glow
```

### Display line numbers

You can show line numbers with the `-l` flag:

```bash
glow -l
```

## Why use Glow?

If you frequently work with markdown documentation in the terminal, Glow improves the experience from reading plain text to viewing more beautifully formatted content. It's nice for:

- Reading documentation directly from the command line
- Browsing project README files
- Reviewing markdown notes created by agents
- Reviewing markdown files with tables
- Previewing blog content 🙂
