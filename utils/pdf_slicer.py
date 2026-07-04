from pypdf import PdfReader, PdfWriter


def parse_pages(page_input: str, total_pages: int):
    pages = set()

    if not page_input:
        return []

    for part in page_input.split(","):
        part = part.strip()

        if "-" in part:
            start, end = map(int, part.split("-"))
            for i in range(start, end + 1):
                if 1 <= i <= total_pages:
                    pages.add(i - 1)
        else:
            i = int(part)
            if 1 <= i <= total_pages:
                pages.add(i - 1)

    return sorted(list(pages))


def slice_pdf(input_path, output_path, page_input):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    if total_pages == 0:
        raise ValueError("PDF has no pages.")

    pages = parse_pages(page_input, total_pages)

    if not pages:
        raise ValueError(f"Invalid selection. PDF has only {total_pages} pages.")

    if max(pages) >= total_pages:
        raise ValueError(f"Page range exceeds limit. PDF has only {total_pages} pages.")

    for p in pages:
        writer.add_page(reader.pages[p])

    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path