## How ConvertSlice Works

ConvertSlice is a web-based document processing tool built with Python and Flask. It allows users to upload PDF or Word documents and perform simple document operations through a browser.

The application currently supports three main functions:

1. **Slice PDF**
   - Users can upload a PDF file.
   - They enter specific pages or page ranges.
   - The system extracts only those pages and creates a new PDF.

2. **PDF to Word**
   - Users upload a PDF file.
   - The system converts it into a Microsoft Word document using `pdf2docx`.

3. **Word to PDF**
   - Users upload a Word document.
   - The system converts it into PDF format using LibreOffice in headless mode.

Processed files are saved temporarily and shown in the dashboard, where users can download them again.

---

## How to Use ConvertSlice

### 1. Open the Application

Visit the ConvertSlice web app in your browser.

### 2. Select a Tool

Choose one of the available tools from the dropdown menu:

- **Slice PDF**
- **PDF → Word**
- **Word → PDF**

### 3. Upload a File

Click **Choose File** and select the document you want to process.

Supported file types:

- `.pdf`
- `.docx`

### 4. Enter Pages for PDF Slicing

If you choose **Slice PDF**, enter the pages you want to extract.

Examples:

```text
1
Extracts page 1.

1,3,5
Extracts pages 1, 3, and 5.

2-6
Extracts pages 2 through 6.

1,3,7-10
Extracts pages 1, 3, and pages 7 to 10.

5. Process the Document
Click Process Document.

The system will upload, process, and generate a new file.

6. Download the Result
After processing, you will be taken to a result page.

Click Download File to save the processed document.

7. View Previous Files
Open the Dashboard page to view recently processed files.

From the dashboard, you can download previous outputs again.

Example Use Cases
Extract only selected pages from a long PDF.

Convert a PDF report into an editable Word document.

Convert a Word assignment or letter into PDF format.

Help users process documents without needing advanced knowledge of Microsoft Word or paid PDF tools.

Intended Users
ConvertSlice is designed for:

Students

Office workers

Non-technical users

People without access to paid document tools

Users who need quick document conversion or page extraction

Author
ConvertSlice was developed by Batex Bafika, a B.Tech Software Engineering student at EHIST University, Bamenda.

This project is free for non-commercial use.

