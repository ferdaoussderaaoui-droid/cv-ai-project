import os

# 📄 قراءة TXT
def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# 📄 قراءة PDF (خاصك تثبت pdfminer)
def read_pdf(file_path):
    try:
        from pdfminer.high_level import extract_text
        return extract_text(file_path)
    except:
        print("⚠️ pdfminer غير مثبت")
        return ""


# 🎯 اختيار الطريقة حسب نوع الملف
def read_cv(file_path):
    _, ext = os.path.splitext(file_path)

    if ext == ".txt":
        return read_txt(file_path)

    elif ext == ".pdf":
        return read_pdf(file_path)

    else:
        print(f"❌ Format غير مدعوم: {ext}")
        return ""
