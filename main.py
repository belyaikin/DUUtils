import os

from dotenv import load_dotenv
from fastapi import FastAPI

import scraper
from database import find_schedule

load_dotenv()

app = FastAPI()


def scrape():
    print("Starting scraping...")

    scraper.scrape_schedules()


if os.getenv("SCRAPE"):
    scrape()


@app.get("/schedules/{group}")
def get_schedule(group: str):
    return find_schedule(group)
