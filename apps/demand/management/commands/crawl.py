from scrapy.crawler import CrawlerRunner, CrawlerProcess
from django.core.management.base import BaseCommand
from scrapy.utils.project import get_project_settings
from crawler.spiders.jobinjaspider import JobinjaspiderSpider


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        try:
            process = CrawlerProcess(get_project_settings())
        except:
            # when using celery, this will run but CrawlerProcess won't
            process = CrawlerRunner(get_project_settings())

        process.crawl(JobinjaspiderSpider)
        process.start()
