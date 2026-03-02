from bs4 import BeautifulSoup


def parse_title(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("title")

    if title_tag and title_tag.text:
        return {"title": title_tag.text.strip()}

    return {"title": None}