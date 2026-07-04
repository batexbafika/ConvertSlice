import subprocess
import os

def word_to_pdf(input_path: str, output_folder: str):
    command = [
        "soffice",
        "--headless",
        "--convert-to",
        "pdf",
        input_path,
        "--outdir",
        output_folder
    ]

    subprocess.run(command, check=True)

    output_file = os.path.join(
        output_folder,
        os.path.splitext(os.path.basename(input_path))[0] + ".pdf"
    )

    return output_file