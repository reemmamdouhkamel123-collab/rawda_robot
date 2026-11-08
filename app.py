from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%H:%M")
    return f"""
    <html dir="rtl" style="font-family:system-ui;text-align:center;padding:20px">
    <h1 style="color:#0B6B4A">روضة ترافيل - الروبوت شغال ✅</h1>
    <p>المعتمر: A4042**** - اليوم: 8/11/2026</p>
    <p>مسار فوري - نساء - الفجر</p>
    <p>الوقت دلوقتي على السيرفر: {now}</p>
    <p>الروبوت هيدخل 5:59 ص ويحجز أول ساعة خضراء</p>
    <div style="background:#eee;padding:15px;border-radius:12px">
    5:00 - مقفولة<br>6:00 - مقفولة<br>7:00 - مقفولة<br>8:00 - مقفولة<br>
    <b style="color:green">9:00 - خضراء - جاهزة للحجز</b>
    </div>
    <p>لو شايفة الصفحة دي، يبقى السيرفر شغال صح</p>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
