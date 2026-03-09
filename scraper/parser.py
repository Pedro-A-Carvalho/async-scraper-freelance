from bs4 import BeautifulSoup


def parse_title(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("title")

    if title_tag and title_tag.text:
        return {"title": title_tag.text.strip()}

    return {"title": None}

def parse_books(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    books = []

    articles = soup.select("article.product_pod")

    for book in articles:
        title = book.h3.a["title"]

        price = book.select_one(".price_color").text

        rating_class = book.select_one(".star-rating")["class"]
        rating = rating_class[1]  # exemplo: "Three"

        books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    return books