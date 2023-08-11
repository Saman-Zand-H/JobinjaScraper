from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)


@shared_task
def crawl_jobinja_demands():
    logger.info("Jobinja Jobs Crawling is Starting...")
    call_command("crawl")
    logger.info("Crawling Finished and Saved to Database.")
