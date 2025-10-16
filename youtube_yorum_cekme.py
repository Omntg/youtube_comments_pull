from googleapiclient.discovery import build
import pandas as pd
import re

# ===============================
# 🔑 1. API Anahtarını Buraya Gir
# ===============================
API_KEY = ""  # ← Buraya kendi API anahtarını gir

# ===============================
# 🎥 2. YouTube Video URL'sini Gir
# ===============================
VIDEO_URL = "https://www.youtube.com/watch?v=_DYRV1Asmjw"  # ← Örnek URL

# ===========================================
# 🔍 3. URL'den video ID'sini otomatik çıkar
# ===========================================
def extract_video_id(url):
    """
    YouTube video URL'sinden video ID'sini çıkarır.
    Örn: https://www.youtube.com/watch?v=abcd1234 → abcd1234
    """
    pattern = r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Geçerli bir YouTube video URL'si girilmedi!")
    return match.group(1)

video_id = extract_video_id(VIDEO_URL)

# ===============================
# ⚙️ 4. YouTube API Servisini Kur
# ===============================
youtube = build("youtube", "v3", developerKey=API_KEY)

# ===============================================
# 💬 5. Yorumları Sayfa Sayfa Toplayan Fonksiyon
# ===============================================
def get_all_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        # YouTube Data API'ye istek
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,  # her sayfada max 100 yorum
            pageToken=next_page_token,
            textFormat="plainText"
        ).execute()

        for item in response["items"]:
            top_comment = item["snippet"]["topLevelComment"]["snippet"]
            comment_data = {
                "Author": top_comment["authorDisplayName"],
                "Comment": top_comment["textDisplay"],
                "Like Count": top_comment["likeCount"],
                "Published At": top_comment["publishedAt"],
                "Updated At": top_comment["updatedAt"],
            }
            comments.append(comment_data)

            # Yanıtlar varsa ekle
            reply_count = item["snippet"]["totalReplyCount"]
            if reply_count > 0:
                replies_response = youtube.comments().list(
                    part="snippet",
                    parentId=item["id"],
                    maxResults=100
                ).execute()

                for reply in replies_response["items"]:
                    reply_snippet = reply["snippet"]
                    reply_data = {
                        "Author": reply_snippet["authorDisplayName"],
                        "Comment": reply_snippet["textDisplay"],
                        "Like Count": reply_snippet["likeCount"],
                        "Published At": reply_snippet["publishedAt"],
                        "Updated At": reply_snippet["updatedAt"],
                    }
                    comments.append(reply_data)

        # Sonraki sayfa varsa devam et
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments

# ===============================
# 📦 6. Tüm Yorumları Çek
# ===============================
print("⏳ Yorumlar çekiliyor... Bu işlem birkaç dakika sürebilir.")
all_comments = get_all_comments(video_id)
print(f"✅ Toplam {len(all_comments)} yorum çekildi.")

# ===============================
# 📊 7. Excel Olarak Kaydet
# ===============================
df = pd.DataFrame(all_comments)
output_filename = "video_yorumlari.xlsx"
df.to_excel(output_filename, index=False)
print(f"💾 Yorumlar '{output_filename}' dosyasına kaydedildi.")

