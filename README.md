## Project Summary: Review Summarization Tool 📝
This project uses the **OpenAI API** to summarize customer reviews from an Excel file within this repository. The main script, written in **Python 3.13.6**, runs on an **Ubuntu virtual machine** and is executed directly from the **GitHub UI**.

---

## How It Works ⚙️
1.  **Input:** The tool takes an Excel file (`Deeto References For Search.xlsx`) from the repository as its input.
2.  **Processing:** A Python script processes the reviews in the file.
3.  **API Call:** It sends the text of each review to the OpenAI API for summarization, requiring an **API key**.
4.  **Output:** The summarized reviews are generated and displayed directly in the **GitHub Actions run output**.

---

## Getting Started (for Developers) 🚀
### Prerequisites
* An **OpenAI API key**.
* Access to an **Ubuntu virtual machine** environment.
* **Python 3.13.6** installed.

### How to Run
This tool is designed to be run directly from the GitHub UI. A GitHub Action is configured to trigger the Python script, so there is no need to run it manually from the command line.

### File Structure
* `main.py`: The core Python script that handles the summarization process.
* `reviews.xlsx`: The input Excel file containing the raw customer reviews.
* `.github/workflows/main.yml`: The GitHub Actions workflow file that automates the execution of the script.

---

## The Output 📄
The final output is a concise, easy-to-read summary of all the reviews from the input Excel file. This summary is not saved as a separate file; instead, you will find it directly in the **log output of the GitHub Actions run**. This output provides valuable insights without the need to read every single review.

---

Google Gemini helped me write this README.md file
