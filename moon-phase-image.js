/*
  انتخاب و نمایش عکس فاز ماه (بدون هیچ سرویس خارجی/NASA/CORS)
  ------------------------------------------------------------
  پیش‌نیاز: کتابخانه Astronomy Engine همان‌طور که در jupiter-moons.html
  و بخش طلوع/غروب ماه در moon.html استفاده شده، باید در صفحه لود شده باشد:
    <script src="https://cdn.jsdelivr.net/npm/astronomy-engine@2/astronomy.browser.min.js"></script>

  ۳۰ فایل تصویر (moon-phase-01.jpg تا moon-phase-30.jpg) باید در مسیر
  زیر روی سایت قرار بگیرند (مسیر را متناسب با ساختار ریپو تنظیم کنید):
    /assets/moon-phases/moon-phase-01.jpg ... moon-phase-30.jpg

  نگاشت فایل‌ها به فاز واقعی:
    فایل شماره d از p = (d-1)/30  استفاده کرده (p: 0 = ماه نو , 0.5 = ماه کامل)
    یعنی moon-phase-01.jpg نزدیک‌ترین به ماه نو و moon-phase-16.jpg
    دقیقاً همان عکس اصلی/کامل شماست (بدون هیچ سایه‌ای).
*/

const MOON_PHASE_IMG_BASE = "/assets/moon-phases/"; // مسیر را با ساختار واقعی ریپو تطبیق بدهید
const MOON_PHASE_FRAME_COUNT = 30;

function getMoonPhaseImagePath(date = new Date()) {
  // Astronomy.MoonPhase برمی‌گرداند: زاویه‌ی فاز ماه بر حسب درجه (0 تا 360)
  // 0 = ماه نو , 90 = تربیع اول , 180 = ماه کامل , 270 = تربیع آخر
  const phaseDeg = Astronomy.MoonPhase(date); // 0..360
  const p = phaseDeg / 360; // نرمال‌شده به 0..1 (0 = ماه نو , 0.5 = ماه کامل)

  let frame = Math.floor(p * MOON_PHASE_FRAME_COUNT) + 1;
  if (frame > MOON_PHASE_FRAME_COUNT) frame = MOON_PHASE_FRAME_COUNT; // احتیاط برای گرد کردن اعشاری
  if (frame < 1) frame = 1;

  const frameStr = String(frame).padStart(2, "0");
  return `${MOON_PHASE_IMG_BASE}moon-phase-${frameStr}.jpg`;
}

function updateMoonPhaseImage() {
  const imgEl = document.querySelector("#moon-phase-photo"); // آی‌دی تگ <img> در moon.html
  if (!imgEl) return;
  imgEl.src = getMoonPhaseImagePath();
}

// اجرای اولیه + به‌روزرسانی دوره‌ای (هر ۵ دقیقه، مثل بخش قبلی)
updateMoonPhaseImage();
setInterval(updateMoonPhaseImage, 5 * 60 * 1000);
