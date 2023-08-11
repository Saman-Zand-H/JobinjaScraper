import scrapy
from urllib.parse import parse_qs


class JobinjaspiderSpider(scrapy.Spider):
    name = "jobinjaspider"
    allowed_domains = ["jobinja.ir"]
    # this is a custom attr that let's us choose number of paginated pages we want to scrape
    number_of_pages = 100
    start_urls = ["https://jobinja.ir/jobs/category/it-software-web-development-jobs/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D9%88%D8%A8-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-%D9%86%D8%B1%D9%85-%D8%A7%D9%81%D8%B2%D8%A7%D8%B1?preferred_before=1691671654&sort_by=relevance_desc"]

    def parse(self, response):
        JOB_CARDS_XPATH = '//*[@id="js-jobSeekerSearchResult"]/div/div[3]/section/div/ul/li/div/div[2]/a/@href'
        job_links = response.xpath(JOB_CARDS_XPATH).getall()
        for job_link in job_links:
            yield scrapy.Request(
                job_link,
                callback=self.parse_job_link
            )
        
        next_page = response.css('a[rel="next"] ::attr(href)').get()
        page_num: list = parse_qs(next_page).get("page", [])
        if len(page_num) <= 0:
            return
        page_num: int = int(page_num[0])
        
        if next_page is not None and page_num <= self.number_of_pages:
            yield response.follow(
                next_page,
                callback=self.parse
            )

    def parse_job_link(self, response):
        TECH_TAGS_XPATH = '//*[contains(@class, "c-infoBox") and contains(@class, "u-mB0")]//li[contains(@class, "c-infoBox__item")][1]/div[contains(@class, "tags")]/span/text()'
        techs = response.xpath(TECH_TAGS_XPATH).getall()
        for tech in techs:
            yield {"name": tech.strip().title()}