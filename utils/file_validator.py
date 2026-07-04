ALLOWED_EXTENSIONS = {"pdf", "docx"}

def is_allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_file_extension(filename: str) -> str:
    return filename.rsplit(".", 1)[1].lower()


def secure_filename_custom(filename: str) -> str:
    keep_chars = ("_", "-", ".")
    return "".join(c for c in filename if c.isalnum() or c in keep_chars)
