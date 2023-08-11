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

This Project makes use of Celery and Celery Beat, to crawl and scrape Jobinja every 6 hours (configurable). Run the project with this command:

```bash
    docker-compose up --build
```
