import scrapy
from scrapy.http import Response


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["work.ua"]
    start_urls = ["https://www.work.ua/jobs-python/"]

    def parse(self, response: Response, **kwargs) -> None:
        vacancies = response.css(
            "div.card.card-hover.card-search > div > h2 > a::attr(href)"
        ).getall()
        for vacancy in vacancies:
            yield response.follow(vacancy, callback=self._parse_vacancy)

        next_page = response.css(
            "ul.pagination > li.circle-style:last-child > a::attr(href)"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    @staticmethod
    def _get_requirements(response: Response) -> list:
        requirements = response.css("div.flex.toggle-block.toggle-block>span")
        return [
            technology.css(".ellipsis::text").get()
            for technology in requirements
        ]

    def _parse_vacancy(self, response: Response) -> None:

        title = response.css("#h1-name::text").get()
        requirements = self._get_requirements(response)

        yield {
            "title": title,
            "requirements": requirements,
        }
