import re

# 🧹 حذف الرموز و characters غير مفيدة
def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', ' ', text)


# 🔡 تحويل النص لحروف صغيرة
def to_lowercase(text):
    return text.lower()


# 🧽 حذف spaces الزائدة
def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()


# 🔢 توحيد formats ديال experience
def normalize_experience(text):
    text = text.lower()

    # تحويل "5 ans" → "5 years"
    text = re.sub(r'(\d+)\s+ans', r'\1 years', text)

    # تحويل "years of experience" → "years"
    text = re.sub(r'years of experience', 'years', text)

    return text


# 🌍 توحيد اللغات
def normalize_languages(text):
    text = text.lower()

    replacements = {
        "anglais": "english",
        "français": "french",
        "arabe": "arabic",
        "espagnol": "spanish"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


# 🎯 CLEAN PIPELINE كامل
def preprocess_text(text):
    text = to_lowercase(text)
    text = normalize_experience(text)
    text = normalize_languages(text)
    text = remove_special_characters(text)
    text = remove_extra_spaces(text)

    return text
