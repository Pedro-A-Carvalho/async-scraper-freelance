import json
from scraper.config import OUTPUT_FILE
import csv


def export_to_csv(results: list, filename=OUTPUT_FILE +".csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["url", "title", "price", "rating"])

        for result in results:

            books = result.get("data", [])

            for book in books:
                writer.writerow([
                    result["url"],
                    book["title"],
                    book["price"],
                    book["rating"]
                ])


def export_to_json(data, filename=OUTPUT_FILE+".json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)