#!/usr/bin/env python3
"""
Builds one static, crawlable HTML page per item in news.json (into /news/<id>.html),
plus sitemap.xml. Run this locally after editing news.json, then commit + push the
results — or let the GitHub Action in .github/workflows/build-news.yml do it for you
automatically on every push.

Usage:
    python3 build_news.py
"""
import json
import os
import html
from datetime import datetime, date

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://kavosh-space.github.io"
SITE_NAME = "گروه نجوم کاوش"

FA_MONTHS = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور",
             "مهر","آبان","آذر","دی","بهمن","اسفند"]

def gregorian_to_jalali(g_y, g_m, g_d):
    g_days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    j_days_in_month = [31,31,31,31,31,31,30,30,30,30,30,29]
    gy = g_y - 1600
    gm = g_m - 1
    gd = g_d - 1
    g_day_no = 365*gy + (gy+3)//4 - (gy+99)//100 + (gy+399)//400
    for i in range(gm):
        g_day_no += g_days_in_month[i]
    if gm > 1 and ((g_y % 4 == 0 and g_y % 100 != 0) or (g_y % 400 == 0)):
        g_day_no += 1
    g_day_no += gd
    j_day_no = g_day_no - 79
    j_np = j_day_no // 12053
    j_day_no %= 12053
    jy = 979 + 33*j_np + 4*(j_day_no//1461)
    j_day_no %= 1461
    if j_day_no >= 366:
        jy += (j_day_no-1)//365
        j_day_no = (j_day_no-1) % 365
    for i in range(11):
        if j_day_no < j_days_in_month[i]:
            jm = i+1
            jd = j_day_no+1
            break
        j_day_no -= j_days_in_month[i]
    else:
        jm = 12
        jd = j_day_no+1
    return jy, jm, jd

def fa_date(iso):
    d = datetime.strptime(iso, "%Y-%m-%d")
    jy, jm, jd = gregorian_to_jalali(d.year, d.month, d.day)
    return f"{jd} {FA_MONTHS[jm-1]} {jy}"

def esc(s):
    return html.escape(s, quote=True)

PAGE_TMPL = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | گروه نجوم کاوش</title>
<meta name="description" content="{excerpt}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{excerpt}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="گروه نجوم کاوش">
<meta property="og:locale" content="fa_IR">
<meta property="og:image" content="{site_url}/logo.png">
<meta name="twitter:card" content="summary">
<link rel="icon" href="../logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;700;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>

<header class="site-nav">
  <a href="../index.html" class="nav-brand">
    <img src="../logo.png" alt="لوگوی گروه نجوم کاوش" class="nav-logo">
    <span>گروه نجوم کاوش</span>
  </a>
  <nav class="nav-links">
    <a href="../index.html">خانه</a>
    <a href="../news.html" class="active">اخبار</a>
    <a href="../team.html">اعضا</a>
    <a href="https://instagram.com/kavosh.space" target="_blank" rel="noopener">اینستاگرام</a>
    <button class="nv-toggle" id="nvToggle" aria-pressed="false">
      <span class="nv-dot"></span>
      <span id="nvLabel">حالت شب</span>
    </button>
  </nav>
</header>

<article>
  <div class="wrap" style="padding-top:64px; max-width:720px;">
    <nav style="font-family:var(--font-data); font-size:12px; color:var(--star-500); margin-bottom:28px;">
      <a href="../index.html" style="color:var(--star-500);">خانه</a> ›
      <a href="../news.html" style="color:var(--star-500);"> اخبار</a> ›
      <span style="color:var(--star-300);"> {title}</span>
    </nav>
    <div class="kicker">{category} · {fa_date}</div>
    <h1 style="font-size:clamp(28px,4vw,42px); margin-bottom:28px;">{title}</h1>
    <div style="color:var(--star-300); font-size:16px; line-height:2;">
      {body_html}
    </div>
    {ig_block}
  </div>
</article>

<footer style="margin-top:80px;">
  گروه نجوم کاوش &nbsp;·&nbsp; تهران و دماوند
</footer>

<script src="../kavosh.js"></script>

</body>
</html>
"""

def build():
    with open(os.path.join(ROOT, "news.json"), encoding="utf-8") as f:
        items = json.load(f)

    news_dir = os.path.join(ROOT, "news")
    os.makedirs(news_dir, exist_ok=True)

    urls = [f"{SITE_URL}/", f"{SITE_URL}/news.html", f"{SITE_URL}/team.html"]

    for item in items:
        url = f"{SITE_URL}/news/{item['id']}.html"
        urls.append(url)
        body_html = "\n      ".join(f"<p style='margin-bottom:20px;'>{esc(p)}</p>" for p in item.get("body", [item.get("excerpt","")]))

        jsonld = {
            "@context": "https://schema.org",
            "@type": "Event" if item["category"] == "رویداد آسمانی" else "NewsArticle",
            "name": item["title"],
            "headline": item["title"],
            "description": item["excerpt"],
            "datePublished": item["date"],
            "url": url,
            "publisher": {
                "@type": "Organization",
                "name": SITE_NAME,
                "url": SITE_URL,
                "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/logo.png"}
            }
        }
        if item["category"] == "رویداد آسمانی":
            jsonld["startDate"] = item["date"]
            jsonld["eventAttendanceMode"] = "https://schema.org/OfflineEventAttendanceMode"
            jsonld["location"] = {"@type": "Place", "name": "دماوند / تهران، ایران"}
            jsonld["organizer"] = {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL}

        ig_block = ""
        if item.get("instagramLink"):
            ig_block = f'<p style="margin-top:32px;"><a class="btn btn-ghost btn-sm" href="{esc(item["instagramLink"])}" target="_blank" rel="noopener">دنبال کردن در اینستاگرام ↗</a></p>'

        page = PAGE_TMPL.format(
            title=esc(item["title"]),
            excerpt=esc(item["excerpt"]),
            url=url,
            site_url=SITE_URL,
            category=esc(item["category"]),
            fa_date=fa_date(item["date"]),
            body_html=body_html,
            ig_block=ig_block,
            jsonld=json.dumps(jsonld, ensure_ascii=False, indent=2),
        )
        out_path = os.path.join(news_dir, f"{item['id']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"wrote {out_path}")

    # sitemap.xml
    today = date.today().isoformat()
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>")
    sitemap.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap))
    print("wrote sitemap.xml")

if __name__ == "__main__":
    build()
