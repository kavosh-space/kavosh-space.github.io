/* ---------- Night vision toggle (shared) ---------- */
function initNightVision(){
  const toggle = document.getElementById('nvToggle');
  const label = document.getElementById('nvLabel');
  if(!toggle) return;
  toggle.addEventListener('click', () => {
    const on = document.body.classList.toggle('night-vision');
    toggle.classList.toggle('on', on);
    toggle.setAttribute('aria-pressed', on);
    label.textContent = on ? 'خروج' : 'حالت شب';
  });
}

/* ---------- Mobile hamburger menu ---------- */
function initNavBurger(){
  const burger = document.getElementById('navBurger');
  const navLinks = document.getElementById('navLinks');
  if(!burger || !navLinks) return;

  burger.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    burger.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open);
    
    // Prevent body scroll when menu is open
    document.body.style.overflow = open ? 'hidden' : '';
  });

  // Close menu when a link is clicked
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      burger.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });
}

/* ---------- Moon phase (pure client-side, no API) ---------- */
function getMoonPhase(date){
  const synodic = 29.53058867;
  const knownNewMoon = Date.UTC(2000, 0, 6, 18, 14, 0);
  const diffDays = (date.getTime() - knownNewMoon) / 86400000;
  const phaseDays = ((diffDays % synodic) + synodic) % synodic;
  const t = phaseDays / synodic;
  const illumination = Math.round((1 - Math.cos(2 * Math.PI * t)) / 2 * 100);

  let name, icon;
  if (t < 0.02 || t > 0.98)      { name = 'ماه نو';                  icon = '🌑'; }
  else if (t < 0.24)             { name = 'هلال رو به افزایش';        icon = '🌒'; }
  else if (t < 0.27)             { name = 'تربیع اول';                icon = '🌓'; }
  else if (t < 0.48)             { name = 'بیش از نیمه، رو به افزایش'; icon = '🌔'; }
  else if (t < 0.52)             { name = 'ماه کامل';                 icon = '🌕'; }
  else if (t < 0.73)             { name = 'بیش از نیمه، رو به کاهش';   icon = '🌖'; }
  else if (t < 0.76)             { name = 'تربیع آخر';                icon = '🌗'; }
  else                            { name = 'هلال رو به کاهش';          icon = '🌘'; }

  return { name, icon, illumination };
}

function initMoonBadge(){
  const el = document.getElementById('moonText');
  const icon = document.getElementById('moonIcon');
  if(!el) return;
  const { name, icon: moonIcon, illumination } = getMoonPhase(new Date());
  icon.textContent = moonIcon;
  el.textContent = `امشب: ${name} · ${illumination}٪ روشنایی`;
}

/* ---------- News rendering ---------- */
function formatFaDate(iso){
  try{
    return new Intl.DateTimeFormat('fa-IR', { year:'numeric', month:'long', day:'numeric' }).format(new Date(iso));
  }catch(e){
    return iso;
  }
}

const NEWS_DEFAULT_IMG = 'perseids.jpg';

function newsCardHtml(item){
  const href = `news/${item.id}.html`;
  return `
    <article class="news-card">
      <img src="${item.image || NEWS_DEFAULT_IMG}" alt="" class="news-card-img" loading="lazy">
      <div class="news-card-body">
        <div class="news-meta">
          <span class="news-tag">${item.category}</span>
          <span>${formatFaDate(item.date)}</span>
        </div>
        <h3>${item.title}</h3>
        <p>${item.excerpt}</p>
        <a class="news-link" href="${href}">جزئیات بیشتر ↗</a>
      </div>
    </article>
  `;
}

function newsFeaturedHtml(item){
  const href = `news/${item.id}.html`;
  return `
    <a class="news-featured" href="${href}">
      <img src="${item.image || NEWS_DEFAULT_IMG}" alt="" class="news-featured-img" loading="lazy">
      <div class="news-featured-body">
        <div class="news-meta">
          <span class="news-tag">${item.category}</span>
          <span>${formatFaDate(item.date)}</span>
        </div>
        <h3>${item.title}</h3>
        <p>${item.excerpt}</p>
        <span class="news-link">بیشتر بخوانید ↗</span>
      </div>
    </a>
  `;
}

async function loadNews(){
  const res = await fetch('news.json');
  if(!res.ok) throw new Error('news.json not found');
  const items = await res.json();
  return items.sort((a,b) => new Date(b.date) - new Date(a.date));
}

async function initNewsTeaser(limit = 4){
  const mount = document.getElementById('newsTeaser');
  if(!mount) return;
  try{
    const items = await loadNews();
    const shown = items.slice(0, limit);
    if(shown.length === 0) throw new Error('no items');
    const [latest, ...rest] = shown;
    mount.innerHTML = newsFeaturedHtml(latest) + `<div class="news-grid">${rest.map(newsCardHtml).join('')}</div>`;
  }catch(e){
    mount.innerHTML = `<p class="news-empty">فعلاً خبری ثبت نشده — تازه‌ترین رویدادها را در <a href="https://instagram.com/kavosh.space" target="_blank" rel="noopener">اینستاگرام کاوش</a> دنبال کنید.</p>`;
  }
}

async function initNewsFull(){
  const mount = document.getElementById('newsFull');
  if(!mount) return;
  try{
    const items = await loadNews();
    const categories = ['همه', ...new Set(items.map(i => i.category))];

    const filterRow = document.getElementById('newsFilters');
    if(filterRow){
      filterRow.innerHTML = categories.map((c,i) =>
        `<button class="filter-chip${i===0 ? ' active' : ''}" data-cat="${c}">${c}</button>`
      ).join('');
      filterRow.addEventListener('click', (e) => {
        const btn = e.target.closest('.filter-chip');
        if(!btn) return;
        filterRow.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const cat = btn.dataset.cat;
        const filtered = cat === 'همه' ? items : items.filter(i => i.category === cat);
        mount.innerHTML = filtered.map(newsCardHtml).join('');
      });
    }

    mount.innerHTML = items.map(newsCardHtml).join('');
  }catch(e){
    mount.innerHTML = `<p class="news-empty">فعلاً خبری ثبت نشده — تازه‌ترین رویدادها را در <a href="https://instagram.com/kavosh.space" target="_blank" rel="noopener">اینستاگرام کاوش</a> دنبال کنید.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initNightVision();
  initMoonBadge();
  initNavBurger();
  initNewsTeaser(4);
  initNewsFull();
});
