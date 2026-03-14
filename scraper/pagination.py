from bs4 import BeautifulSoup


def get_total_pages(html: str) -> int:
    soup = BeautifulSoup(html, "html.parser")

    current = soup.select_one("li.current")

    if not current:
        return 1

    text = current.text.strip()

    # exemplo: "Page 1 of 50"
    parts = text.split()

    total_pages = int(parts[-1])

    return total_pages