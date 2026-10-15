#!/usr/bin/env python3
"""
Builds one static, crawlable HTML page per item in news.json (into /news/<id>.html),
plus sitemap.xml. Run this locally after editing news.json, then commit + push the
results — or let the GitHub Action in .github/workflows/build-news.yml do it for you
automatically on every push.

Usage:
python3 build_news.py
git add news/ sitemap.xml
git commit -m "apply new nav + light theme to all news articles"
git push
"""

{
  "id": "news-mcgetchin-26",
  "category": "نجوم",
  "date": "2026-10-15",
  "title": "شناسایی یک دهانه برخوردی تازه بر روی ماه",
  "excerpt": "تصور این که در دوران معاصر شاهد شکل‌گیری دهانه برخوردی جدید با ابعادی به نسبت  بزرگ باشیم بسیار دور از ذهن است اما دانشمندان اخیرا متوجه دهانه تازه ای بر روی ماه شده‌اند که می‌توانیم آن را دهانه قرن بنمایم",
  "body": [
    "نویسنده: پدرام محمدطاهری",
    "تقریبا کسی را سراغ نداریم که از دیدن ماه و دهانه‌های برخوردی آن از پشت تلسکوپ به شگفتی نیفتد. هنوز هم حتا با گذر سال‌ها رصد آسمان این دهانه‌های برخوردی برای‌مان جذاب‌اند و محلی هستند برای خیال‌پردازی. این دهانه‌های عظیم که وسعت آن‌ها گاهی به بزرگی یک شهر یا یک استان می‌رسد اکثرا از چند میلیون سال تا حدود 4 میلیارد سال قدمت دارند و یادگار دوران پربرخورد منظومه شمسی به شمار می‌روند و درست مانند یک فسیل ما را به گذشته‌های پر هرج و مرج سامانه‌ خورشیدی‌مان می‌برند. اما دانشمندان به تازگی موفق شده‌اند یک دهانه برخوردی را بر روی ماه شناسایی کنند که به تازگی شکل گرفته است و  می‌توانیم آن را بزرگترین دهانه برخوردی یک قرن اخیر بنامیم.",
    "واقعیت این است که سامانه خورشیدی کنونی ما نسبت به روزهای اولیه‌اش مکانی‌ست به مراتب آرام‌تر و کم‌برخوردتر. از این روی برخوردهای ویران‌گر در این روزها پدیده‌ای بسیار کم‌یاب است. بنابراین احتمال این که در دوران معاصر شاهد برخوردهایی چنین و به تبع آن شکل‌گیری دهانه‌های عظیمِ تازه بر روی ماه باشیم بسیار اندک است. اما دانشمندان به تازگی اعلام کرده‌اند که در بهار سال 2024 ماه به دنبال برخوردی با یک سیارک یا احتمالا دنباله‌دار ، صاحب یک دهانه برخوردی تازه شده که می‌توان آن را بزرگ‌ترین دهانه برخوردی تازه شکل‌گرفته در منظومه شمسی که توسط بشر معاصر ثبت شده به حساب آوریم. این دهانه 222 متر وسعت دارد و حاصل برخورد با جرمی در ابعاد یک ساختمان 3 تا 6 طبقه است. پیش از این بزرگ‌ترین دهانه برخوردی تازه و معاصر ثبت شده تنها 70 متر وسعت داشت.",
    "این دهانه برخوردی که در لبه شرقی ماه قرار دارد به نام «تام مک‌گچین» فقید نام‌گذاری شده است. تام مک‌گچین زمین‌شناس و دانشمند علوم سیاره‌ای یکی از تاثیرگذارترین چهره‌های زمین‌شناسی ماه است. مک‌گچین درک ما را از مکانیک برخوردها در سطح ماه و سایر اجرام مشابه و به علاوه آتشفشان‌های کهن ماه شکل داد و در انتخاب محل  فرود آپولو  17  نیز یاری رساند.",
    "شناسایی این دهانه برخوردی که در قالب دو مقاله در نشریه ساینس ادونسز و خلاصه‌ای از آن در نشریه آسترونومی به آن پرداخته شده توسط یکی از اعضای تیم مدارگرد شناسایی ماه (Lunar Reconnaissance Orbiter) به صورت تصادفی اتفاق می‌افتد. رابرت واگنر متخصص پردازش تصاویر در تیم اِل آر او اوایل پاییز سال 2025 مشغول مرور دستی آرشیو تصاویر دوربین میدان دیدِ باز این مدارگرد بود که ناگهان متوجه یک لکه روشن در عکس آرشیوی می‌شود که توسط حلقه‌ای تاریک احاطه شده است. این لکه به عنوان یک محل احتمالی برخورد در نظر گرفته می‌شود.",
    "مدارگرد شناسایی ماه یا به طور خلاصه ال آر او که از سال 2010 در حال فعالیت است قادر است هر سی روز یکبار از سراسر ماه تصویربرداری کند و این به معنی دسترسی به آرشیوی زمان‌بندی شده از ماه است. مقایسه عکس‌های جدید رسیده از ماه با عکس‌های قدیمی‌تر می‌تواند کوچک‌ترین تغییر جدیدی در سطح ماه را آشکار کند. تاکنون به همین روش بیش از 1000 دهانه برخوردی تازه به ثبت رسیده است. دهانه‌ای که واگنر شناسایی می‌کند درست به همین روش انجام می‌شود. یعنی مقایسه یک عکس جدید با عکس آرشیوی و جست‌وجو برای یافتن کوچک‌ترین تفاوت. این نقطه مرموز دانشمندان را ترغیب می‌کند که در گذرهای بعدی مدارگرد از فراز دهانه تازه شکل‌گرفته ، این‌بار از دوربین میدان دیدِ بسته مدارگرد استفاده کنند تا تصویری واضح‌تر با بزرگ‌نمایی بیشتر از محل برخورد به دست آید.",
    "در این تصویر که ابعاد 925 متر در 925 متر از سطح ماه را پوشش می‌دهد می‌توان به‌وضوح دهانه برخوردی جدید و تاثیرات پیرامونی آن را در سطح ماه مشاهده کرد.",
    "همان‌طور که گفته شد این اولین بار نیست که محققان متوجه یک دهانه برخوردی تازه بر روی ماه می‌شوند زیرا ماه اساسا فاقد جو است و کاملا بی‌دفاع. هر جرم فضایی سرگردان به‌سادگی می‌تواند با سطح ماه برخورد کند و هیچ عامل جوی سرعت آن را کاهش نمی‌دهد. از این روی ماه سالانه صاحب دهانه‌های برخوردی جدیدی می‌شود که بسیاری از آن‌ها به قدری کوچک هستند که حتا تجهیزات پیشرفته‌ای نظیر مدارگرد شناسایی ماه هم قادر به تشخیص آن‌ها نیست. تخمین زده شده که هرساله 140 دهانه برخوردی جدید در ماه توسط این مدارگرد شناسایی می‌شود که ابعاد آن‌ها چیزی حدود 9 متر است. اما دهانه مک‌گچین با قطر 222 متر یک مورد کاملا کم‌یاب است. مدل‌های ایجاد دهانه‌ها  پیش‌بینی می‌کند که برخوردهایی نظیر مک‌گچین هر 132 سال یکبار به وقوع می‌پیوندند.",
    "یک برخورد عظیم در مقابل چشمان جست‌وجوگر",
    "این برخوردهای تازه و شناسایی به موقع آن‌ها می‌تواند انباری از اطلاعات علمی را برای ما فراهم آورد. آن‌هم در دورانی که ما به ابزارهای بسیاری پیشرفته اندازه‌گیری مجهز هستیم. واقعیت این است که برخوردها با خود پدیده‌های زمین‌شناختی شگفت‌انگیزی را به همراه می‌آورند که درک آن‌ها برای ما مهم است. به عنوان مثال بین نوامبر 2025 تا فوریه 2026 محققان با کمک رادیومتر مدارگردِ ال آراو دمای منطقه برخورد را به طور متناوب اندازه‌گیری کردند و آن را با آرشیو دمایی همان نقطه پیش از برخورد به مقایسه گذاشتند و به نکته شگفتی پی بردند. محدوده‌ای در حدود 7 کیلومتر به مرکزیت دهانه مک‌گچین دمایی کمتر از محیط اطراف را از خود نشان می داد چیزی در حدود 8 الی 9 درجه سانتیگراد سردتر از نواحی دیگر ماه در زمان شب!",
    "حدود یک دهه است که با این پدیده آشنا هستیم پدیده‌ای که به «لکه سرد» موسوم است و راز آن به پوشش سطحی ماه برمی‌گردد. سطح رویی ماه و همچنین سطح سیاره خودمان زمین و حتا مریخ و بسیاری از سیارک‌ها از لایه‌ای ناهمگن ساخته شده که به رِگولیت مشهور است. رگولیت یک لایه ناهمگن از مواد مختلف مثل غبار، خاک ، خرده سنگ و موادی دیگر است که روی بستر سنگی جامد قرار می‌گیرد. رگولیت تقریبا تمام سطح ماه را پوشانده است و هرجا که قدم بگذارید رگولیتِ نسبتا متراکم را زیر پای خود احساس می‌کنید. زمانی که برخوردی با سطح ماه صورت می‌گیرد رگولیت موجود در مناطقِ پیرامونِ محلِ برخورد سست می‌شود و چگالی‌اش کاهش پیدا می‌کند. سست شدن رگولیت باعث می‌شود دیگر نتواند مانند قبل گرمایی که در زمان روزِ ماه در خود ذخیره کرده را به آرامی تخلیه کند بلکه خیلی زودتر از همیشه گرمای خود را در زمان شب از دست می‌دهد و برای همین نسبت به رگولیت‌های دورتر از محل برخورد خیلی سریع‌تر سرد می‌شود و به همین دلیل در نقشه‌های دمایی از سطح ماه ما شاهد لکه‌های سرد در سطح ماه هستیم.",
    "پدیده لکه سرد یک پدیده کوتاه‌مدت است یعنی قرار نیست تا ابد مناطق برخوردی تازه، دمای کمتری نسبت به سایر نقاط ماه در هنگام شب نشان دهند. خیلی زود محو می‌شوند و اثری ازشان باقی نمی‌ماند. بیشتر لکه‌های سردی که تاکنون کشف شده در زمانی بوده که لکه در حال محو شدن بوده است اما مک‌گچین  از این حیث متمایز است زیرا این بزرگ‌ترین لکه سردی است که درست در زمان شکل‌گیری‌اش توسط انسان معاصر مطالعه شده.",
    "در مقاله منتشر شده در مورد شناسایی مک‌گچین محققان به تخمین جالبی اشاره می‌کنند که اهمیت لکه‌های سرد را برای ما روشن می‌سازد. براساس این مقاله که با کمک مدل‌های رایانه‌ای انجام شده هر تکه از سطح ماه حدودا هر 10 میلیون سال وارد یک لکه سرد می‌شود و 2 تا 5 سانتیمتر از رگولیت رویی آن سست می‌گردد. این آهنگ تغییرات با آهنگ پدیده‌ای موسوم به «شخم‌خوردگی برخوردی» یعنی زیر و رو شدن خاک درون لبه دهانه‌ها ، هم‌ارز است و نشان می‌دهد که لکه‌های سرد عاملی مهم هستند برای شکل دادن به سطح ماه.",
    "خاکی که روزی بر آن قدم خواهیم زد",
    "احتمالا اگر برای ساختن یک سازه عظیم یا یک مدرسه بر روی زمین برنامه‌ای داشته باشیم اولین قدم آزمایش خاک و رگولیتی است که قرار است روی آن سازه بنا شود. شاید روزی آنچه که امروز از طریق مطالعه خاک ماه گردآوری می‌کنیم در آینده و برای آیندگانی که قرار است در ماه یا سیاره‌ای نظیر مریخ سکنی گزینند دارای اهمیت بسیاری باشد.",
    "ماه همچنان نزدیک‌ترین آزمایشگاه زمین‌شناسی سیاره‌ای به ماست که می‌توانیم آن را برای آیندگان کاوش کنیم و همچنان محل شگفتی و آگاهی ما در مورد منظومه شمسی و سیاره حیات‌بخش‌مان زمین. ",
    "مک‌گچین را نمی‌توانیم از پشت تلسکوپ از روی زمین تشخیص دهیم اما صدها دهانه عظیم‌تر منتظر شماست تا با ابتدایی‌ترین ابزار رصدی خود به سراغ آن بروید و به کاوش بصری ماه بپردازید. دستکم ماه خانه آینده ماست کسی چه می‌داند شاید دهانه‌ای که امشب رصدش می‌کنید روزی محل زندگی نسل‌های بعدی ما باشد.",
    "https://www.astronomy.com/science/scientists-spot-a-new-crater-on-the-moon/",  
    "https://www.science.org/doi/10.1126/sciadv.aeh7812"
  ],
  "image": "post-mcgetchin.jpg",
  "instagramLink": ""
}

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://kavoshspace.ir"
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

  <button class="nav-burger" id="navBurger" aria-label="منو" aria-expanded="false">
    <span></span>
    <span></span>
    <span></span>
  </button>

  <nav class="nav-links" id="navLinks">
    <a href="../index.html">خانه</a>
    <a href="../news.html" class="active">اخبار</a>
    <a href="../tools.html">ابزار رصد</a>
    <a href="../tours.html">گشت رصدی</a>

    <div class="nav-dropdown" id="navAboutDropdown">
      <button class="nav-dropdown-toggle" aria-expanded="false">درباره ما</button>
      <div class="nav-dropdown-menu">
        <a href="../about.html">درباره کاوش</a>
        <a href="../team.html">اعضا</a>
        <a href="../workshops.html">کارگاه‌ها</a>
      </div>
    </div>

    <a href="../contact.html">تماس با ما</a>

    <button class="nv-toggle" id="nvToggle" aria-pressed="false">
      <span class="nv-dot"></span>
      <span id="nvLabel">حالت رصد</span>
    </button>
  </nav>
</header>

<nav class="story-sticky-nav" id="storyStickyNav" aria-label="فهرست کوتاه صفحه">
  <a href="../index.html" class="story-sticky-brand">
    <img src="../logo.png" alt="" class="story-sticky-logo">
    <span>گروه نجوم کاوش</span>
  </a>
  <div class="story-sticky-links">
    <a href="../index.html">خانه</a>
    <a href="../news.html">اخبار</a>
  </div>
</nav>

<div class="light-scope">
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
</div>

<footer style="margin-top:80px;">
  گروه نجوم کاوش &nbsp;·&nbsp; تهران و دماوند
</footer>

<script src="../kavosh.js"></script>
<script>
  // Swap the main dark nav for the slim sticky nav shortly after the reader
  // starts scrolling through the article body (there's no hero photo on
  // article pages to use as a scroll trigger, so a fixed offset is used).
  (function(){{
    var mainNav = document.querySelector('header.site-nav');
    var miniNav = document.getElementById('storyStickyNav');
    if(!mainNav || !miniNav) return;
    var THRESHOLD = 180;
    function onScroll(){{
      var past = window.scrollY > THRESHOLD;
      mainNav.classList.toggle('story-nav-hidden', past);
      miniNav.classList.toggle('is-visible', past);
    }}
    document.addEventListener('scroll', onScroll, {{ passive: true }});
    onScroll();
  }})();
</script>

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
    title = esc(item["title"])
    excerpt = esc(item["excerpt"])
    return f"""    <article class="news-card" data-cat="{category}">
      <img src="{image}" alt="{title}" class="news-card-img" loading="lazy">
      <div class="news-card-body">
        <div class="news-meta">
          <span class="news-tag">{category}</span>
          <span>{fa_date(item["date"])}</span>
        </div>
        <h3>{title}</h3>
        <p>{excerpt}</p>
        <a class="news-link" href="news/{esc(item['id'])}.html">جزئیات بیشتر ↗</a>
      </div>
    </article>"""

def news_mini_card_html(item):
    """Static HTML for one homepage teaser card — image + title only, no excerpt.
    Used inside the horizontal-scrolling #newsTeaser strip on index.html."""
    image = esc(item.get("image") or NEWS_DEFAULT_IMG)
    category = esc(item["category"])
    title = esc(item["title"])
    return f"""    <a class="news-mini-card" href="news/{esc(item['id'])}.html" data-cat="{category}">
      <img src="{image}" alt="{title}" loading="lazy">
      <span class="news-mini-tag">{category}</span>
      <span class="news-mini-title">{title}</span>
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

    # --- index.html: teaser (latest 3 items as image+title cards, scrollable,
    # with a 4th "خبرهای بیشتر" card reached by scrolling further) ---
    index_html_path = os.path.join(ROOT, "index.html")
    with open(index_html_path, encoding="utf-8") as f:
        index_html = f.read()

    if items_sorted:
        latest_three = items_sorted[:3]
        cards = "\n".join(news_mini_card_html(i) for i in latest_three)
        teaser_html = f'  <div class="news-scroll">\n{cards}\n  </div>'
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

    STATIC_PAGES = [
        "news.html", "team.html", "about.html", "contact.html", "tours.html",
        "workshops.html", "observatory.html", "gallery.html", "sky-map.html",
        "tools.html", "sky-map-live.html", "comets.html", "moon.html",
        "jupiter-moons.html", "seeing.html", "iss-passes.html",
        "seeing-transparency-story.html",
    ]
    today = date.today().isoformat()

    # (url, lastmod) pairs. Static pages get today's date; each news article
    # gets its own publication date, so Google sees an honest lastmod.
    urls = [(f"{SITE_URL}/", today)] + [(f"{SITE_URL}/{p}", today) for p in STATIC_PAGES]

    for item in items:
        url = f"{SITE_URL}/news/{item['id']}.html"
        urls.append((url, item["date"]))
        body_html = "\n      ".join(
            render_body_block(p) for p in item.get("body", [item.get("excerpt","")])
        )

        og_image = f"{SITE_URL}/{item['image']}" if item.get("image") else f"{SITE_URL}/logo.png"
        twitter_card = "summary_large_image" if item.get("image") else "summary"

        # Every news item is a NewsArticle. (Astronomical phenomena are not
        # attendable events, so no Event markup is generated here; real
        # attendable events live as Event JSON-LD on workshops.html.)
        jsonld = {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": item["title"],
            "description": item["excerpt"],
            "image": og_image,
            "datePublished": item["date"],
            "dateModified": item["date"],
            "mainEntityOfPage": url,
            "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL},
            "publisher": {
                "@type": "Organization",
                "name": SITE_NAME,
                "url": SITE_URL,
                "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/logo.png"}
            }
        }

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
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lastmod in urls:
        sitemap.append(f"  <url><loc>{u}</loc><lastmod>{lastmod}</lastmod></url>")
    sitemap.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap))
    print("wrote sitemap.xml")

    items_sorted = sorted(items, key=lambda i: i["date"], reverse=True)
    build_news_listing_and_teaser(items_sorted)

if __name__ == "__main__":
    build()
