def load_urls(file_path: str) -> list[str]:
    urls = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            url = line.strip()

            if url:
                urls.append(url)

    return urls