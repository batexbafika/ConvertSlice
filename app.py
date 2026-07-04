import os
from flask import Flask, render_template, request, send_file, flash, redirect, url_for, session
from werkzeug.utils import secure_filename

import config

from utils.pdf_slicer import slice_pdf
from utils.pdf_converter import pdf_to_word
from utils.word_converter import word_to_pdf
from utils.file_validator import is_allowed_file

app = Flask(__name__)
app.secret_key = "convertslice_secret"

app.config["UPLOAD_FOLDER"] = config.UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = config.OUTPUT_FOLDER


# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# HELPER: HISTORY
# -------------------------
def add_to_history(filename, mode):
    if "history" not in session:
        session["history"] = []

    session["history"].append({
        "file": filename,
        "mode": mode
    })

    session.modified = True


# -------------------------
# PROCESS
# -------------------------
@app.route("/process", methods=["POST"])
def process_file():
    try:
        mode = request.form.get("mode")
        file = request.files.get("file")
        pages = request.form.get("pages")

        if not file:
            flash("No file uploaded ❌")
            return redirect(url_for("home"))

        if not is_allowed_file(file.filename):
            flash("Invalid file type ❌")
            return redirect(url_for("home"))

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)

        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(input_path)

        # -------------------------
        # SLICE PDF
        # -------------------------
        if mode == "slice":
            if not pages:
                flash("Enter page range ❌")
                return redirect(url_for("home"))

            output_name = f"sliced_{filename}"
            output_path = os.path.join(app.config["OUTPUT_FOLDER"], output_name)

            slice_pdf(input_path, output_path, pages)

            add_to_history(output_name, mode)

            return render_template(
                "result.html",
                filename=output_name,
            )

        # -------------------------
        # PDF → WORD
        # -------------------------
        elif mode == "pdf_to_word":
            output_name = f"{os.path.splitext(filename)[0]}.docx"
            output_path = os.path.join(app.config["OUTPUT_FOLDER"], output_name)

            pdf_to_word(input_path, output_path)

            add_to_history(output_name, mode)

            return render_template(
                "result.html",
                filename=output_name,
            )

        # -------------------------
        # WORD → PDF
        # -------------------------
        elif mode == "word_to_pdf":
            output_file = word_to_pdf(input_path, app.config["OUTPUT_FOLDER"])
            output_name = os.path.basename(output_file)

            add_to_history(output_name, mode)

            return render_template(
                "result.html",
                filename=output_name,
            )

        else:
            flash("Invalid mode selected ❌")
            return redirect(url_for("home"))

    except ValueError as ve:
        flash(str(ve))
        return redirect(url_for("home"))

    except Exception as e:
        flash(f"Error: {str(e)}")
        return redirect(url_for("home"))


# -------------------------
# DOWNLOAD
# -------------------------
@app.route("/download/<filename>")
def download(filename):
    file_path = os.path.join(app.config["OUTPUT_FOLDER"], filename)
    return send_file(file_path, as_attachment=True)


# -------------------------
# DASHBOARD
# -------------------------
@app.route("/dashboard")
def dashboard():
    history = session.get("history", [])
    return render_template("dashboard.html", history=history)


# -------------------------
# RUN APP
# -------------------------

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/delete/<filename>")
def delete_file(filename):

    file_path = os.path.join(app.config["OUTPUT_FOLDER"], filename)

    history = session.get("history", [])

    # Remove from history
    history = [item for item in history if item["file"] != filename]

    session["history"] = history

    # Delete physical file
    if os.path.exists(file_path):
        os.remove(file_path)

    flash("File deleted successfully.")

    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)