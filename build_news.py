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
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="{twitter_card}">
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

def render_body_block(p):
    """Render one item of a news 'body' array.
    - plain string -> a paragraph, exactly as before (old articles are unaffected).
    - {"type": "image", "src": "...", "alt": "...", "caption": "..."} -> an inline figure.
    """
    if isinstance(p, dict) and p.get("type") == "image":
        src = esc(p["src"])
        alt = esc(p.get("alt", ""))
        figcaption = ""
        if p.get("caption"):
            figcaption = (
                f"<figcaption style='margin-top:10px; font-size:13px; "
                f"color:var(--star-500); text-align:center;'>{esc(p['caption'])}</figcaption>"
            )
        return (
            f"<figure style='margin:32px 0;'>"
            f"<img src='../{src}' alt='{alt}' loading='lazy' "
            f"style='width:100%; border-radius:12px; display:block;'>"
            f"{figcaption}</figure>"
        )
    return f"<p style='margin-bottom:20px;'>{esc(p)}</p>"

NEWS_DEFAULT_IMG = "perseids.jpg"

def news_card_html(item):
    """Static HTML for one card in the news.html full grid — mirrors kavosh.js'
    newsCardHtml() exactly, plus a data-cat attribute so the (now optional)
    client-side filter can show/hide pre-rendered cards without re-fetching JSON."""
    image = esc(item.get("image") or NEWS_DEFAULT_IMG)
    category = esc(item["category"])
    return f"""    <article class="news-card" data-cat="{category}">
      <img src="{image}" alt="" class="news-card-img" loading="lazy">
      <div class="news-card-body">
        <div class="news-meta">
          <span class="news-tag">{category}</span>
          <span>{fa_date(item["date"])}</span>
        </div>
        <h3>{esc(item["title"])}</h3>
        <p>{esc(item["excerpt"])}</p>
        <a class="news-link" href="news/{esc(item['id'])}.html">جزئیات بیشتر ↗</a>
      </div>
    </article>"""

def news_featured_html(item):
    """Static HTML for the single featured/latest item — mirrors kavosh.js' newsFeaturedHtml()."""
    image = esc(item.get("image") or NEWS_DEFAULT_IMG)
    category = esc(item["category"])
    return f"""  <a class="news-featured" href="news/{esc(item['id'])}.html" data-cat="{category}">
    <img src="{image}" alt="" class="news-featured-img" loading="lazy">
    <div class="news-featured-body">
      <div class="news-meta">
        <span class="news-tag">{category}</span>
        <span>{fa_date(item["date"])}</span>
      </div>
      <h3>{esc(item["title"])}</h3>
      <p>{esc(item["excerpt"])}</p>
      <span class="news-link">بیشتر بخوانید ↗</span>
    </div>
  </a>"""

def news_filters_html(items):
    categories = ["همه"]
    for i in items:
        if i["category"] not in categories:
            categories.append(i["category"])
    chips = []
    for idx, c in enumerate(categories):
        active = " active" if idx == 0 else ""
        chips.append(f'<button class="filter-chip{active}" data-cat="{esc(c)}">{esc(c)}</button>')
    return "\n    ".join(chips)

def inject_between_markers(html_text, start_marker, end_marker, new_inner_html):
    """Replace everything between two HTML comment markers, keeping the markers."""
    start_idx = html_text.find(start_marker)
    end_idx = html_text.find(end_marker)
    if start_idx == -1 or end_idx == -1:
        raise ValueError(f"markers {start_marker!r}/{end_marker!r} not found — is the template out of date?")
    before = html_text[:start_idx + len(start_marker)]
    after = html_text[end_idx:]
    return f"{before}\n{new_inner_html}\n{after}"

def build_news_listing_and_teaser(items_sorted):
    """Pre-render the news.html full grid + filter chips, and the index.html
    teaser (featured item + 3 more), so search engines and non-JS clients see
    real content in the initial HTML instead of a JS-injected 'loading' state."""

    # --- news.html: filter chips + full grid ---
    news_html_path = os.path.join(ROOT, "news.html")
    with open(news_html_path, encoding="utf-8") as f:
        news_html = f.read()

    news_html = inject_between_markers(
        news_html, "<!--NEWS_FILTERS_START-->", "<!--NEWS_FILTERS_END-->",
        "    " + news_filters_html(items_sorted)
    )
    full_grid = "\n".join(news_card_html(i) for i in items_sorted)
    news_html = inject_between_markers(
        news_html, "<!--NEWS_CARDS_START-->", "<!--NEWS_CARDS_END-->", full_grid
    )

    with open(news_html_path, "w", encoding="utf-8") as f:
        f.write(news_html)
    print("updated news.html (static filter chips + full grid)")

    # --- index.html: teaser (latest item featured + next 3 as small cards) ---
    index_html_path = os.path.join(ROOT, "index.html")
    with open(index_html_path, encoding="utf-8") as f:
        index_html = f.read()

    if items_sorted:
        latest, *rest = items_sorted[:4]
        teaser_html = news_featured_html(latest)
        if rest:
            rest_cards = "\n".join(news_card_html(i) for i in rest)
            teaser_html += f'\n  <div class="news-grid">\n{rest_cards}\n  </div>'
    else:
        teaser_html = '<p class="news-empty">فعلاً خبری ثبت نشده — تازه‌ترین رویدادها را در <a href="https://instagram.com/kavosh.space" target="_blank" rel="noopener">اینستاگرام کاوش</a> دنبال کنید.</p>'

    index_html = inject_between_markers(
        index_html, "<!--NEWS_TEASER_START-->", "<!--NEWS_TEASER_END-->", teaser_html
    )

    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("updated index.html (static news teaser)")

def build():
    with open(os.path.join(ROOT, "news.json"), encoding="utf-8") as f:
        items = json.load(f)

    news_dir = os.path.join(ROOT, "news")
    os.makedirs(news_dir, exist_ok=True)

    # Static site pages that are properly nav-linked from every page (and so
    # already have internal links pointing at them) but were previously
    # missing from the sitemap entirely — this was leaving Google to discover
    # them only by chance rather than being told about them directly.
    STATIC_PAGES = [
        "news.html", "team.html", "about.html", "contact.html", "tours.html",
        "offerings.html", "observatory.html",
        "tools.html", "sky-map-live.html", "comets.html", "moon.html",
        "jupiter-moons.html", "seeing.html", "iss-passes.html",
        "seeing-transparency-story.html",
    ]
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{p}" for p in STATIC_PAGES]

    for item in items:
        url = f"{SITE_URL}/news/{item['id']}.html"
        urls.append(url)
        body_html = "\n      ".join(
            render_body_block(p) for p in item.get("body", [item.get("excerpt","")])
        )

        og_image = f"{SITE_URL}/{item['image']}" if item.get("image") else f"{SITE_URL}/logo.png"
        twitter_card = "summary_large_image" if item.get("image") else "summary"

        jsonld = {
            "@context": "https://schema.org",
            "@type": "Event" if item["category"] == "رویداد آسمانی" else "NewsArticle",
            "name": item["title"],
            "headline": item["title"],
            "description": item["excerpt"],
            "image": og_image,
            "datePublished": item["date"],
            "url": url,
            "author": {"@type": "Organization", "name": SITE_NAME},
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
            og_image=esc(og_image),
            twitter_card=twitter_card,
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

    items_sorted = sorted(items, key=lambda i: i["date"], reverse=True)
    build_news_listing_and_teaser(items_sorted)

if __name__ == "__main__":
    build()
