import os

from dotenv import load_dotenv
from fastapi import FastAPI

import scraper
from controller import schedule_controller

load_dotenv()

app = FastAPI()

app.include_router(schedule_controller.router)


def scrape():
    print("Starting scraping...")

    scraper.scrape_schedules()


if os.getenv("SCRAPE"):
    scrape()
