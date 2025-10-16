📥 YouTube Comment Scraper

A simple yet powerful Python script that retrieves all comments (including replies) from any YouTube video using the YouTube Data API v3 and exports them to an Excel file for analysis or archiving.

📚 Table of Contents

Introduction

Features

Requirements

Installation

Configuration

Usage

Output

Troubleshooting

Example

License

🧩 Introduction

This project provides a quick way to extract YouTube comments (including replies, likes, authors, and timestamps) for any public YouTube video.
The data is saved to an Excel (.xlsx) file, making it easy to perform sentiment analysis, keyword extraction, or other data processing tasks.

✨ Features

✅ Fetches all comments and replies from a given YouTube video.

✅ Exports data cleanly into an Excel spreadsheet.

✅ Automatically extracts the video ID from a YouTube URL.

✅ Includes detailed comment metadata (author, likes, timestamps).

✅ Simple, lightweight, and easy to use.

📦 Requirements

Make sure you have the following installed:

Python 3.8+

Google API Client for Python

Pandas

OpenPyXL (required for Excel export)

⚙️ Installation

Clone or download this repository:

git clone https://github.com/yourusername/youtube-comment-scraper.git
cd youtube-comment-scraper


Install dependencies:

pip install google-api-python-client pandas openpyxl

🔐 Configuration

Go to the Google Cloud Console
.

Create a new project (or use an existing one).

Enable the YouTube Data API v3.

Create an API key and copy it.

Open the Python script and paste your key:

API_KEY = "YOUR_API_KEY_HERE"

▶️ Usage

Open the script and replace the example YouTube URL:

VIDEO_URL = "https://www.youtube.com/watch?v=_DYRV1Asmjw"


Run the script:

python youtube_comment_scraper.py


Wait while comments are fetched (large videos may take several minutes).

📊 Output

After completion, the script will generate an Excel file named:

calikusu.xlsx


Each row includes:

Author	Comment	Like Count	Published At	Updated At
🧰 Troubleshooting
Issue	Possible Cause	Solution
HttpError: 403	Invalid or restricted API key	Re-enable YouTube Data API and ensure the key is unrestricted or properly scoped.
ValueError: Geçerli bir YouTube video URL'si girilmedi!	Invalid YouTube URL	Make sure you’re using a valid URL format like https://www.youtube.com/watch?v=VIDEO_ID.
No comments returned	Comments are disabled or video is private	Ensure the video is public and has visible comments.
🧪 Example

Input:

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


Output:

✅ Toplam 2563 yorum çekildi.
💾 Yorumlar 'calikusu.xlsx' dosyasına kaydedildi.


Excel Preview:

Author	Comment	Like Count	Published At	Updated At
John Doe	Great video!	12	2024-01-12T15:23:00Z	2024-01-12T15:23:00Z
Jane Smith	Thanks for the info!	3	2024-01-13T10:15:00Z	2024-01-13T10:15:00Z
🪪 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this script with proper attribution.
