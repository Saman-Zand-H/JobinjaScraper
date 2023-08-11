# Jobinja Crawler

This is a project using Scrapy and Django for crawling, possibly analyzing, and storing scraped data.

The purpose of this project (right now) is for analyzing what technologies have a higher demands in job advertisments.

## Project Stracture

```schema
.
├── apps   # apps live here
│   ├── crawler    # this is the scrapy crawler and all the other folders are django apps
│   │   └── spiders
│   ├── demand
│   │   ├── management
│   │   │   └── commands
│   │   └── migrations
│   └── users
│       └── migrations
└── conf   # this is django's root project dir
```

## Running The Project

To initialize the project, run this command first:

```bash
    python manage.py migrate
```

And then to crawl and scrape the data to populate the database run this command:

```bash
    python manage.py crawl
```
