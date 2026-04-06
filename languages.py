import re

# 🌍 قاعدة بيانات اللغات + synonyms
LANG_DB = {
    "english": ["english", "anglais"],
    "french": ["french", "français", "francais"],
    "arabic": ["arabic", "arabe"],
    "spanish": ["spanish", "espagnol"]
}

# 📊 keywords ديال levels
LEVELS = {
    "fluent": ["fluent", "native", "bilingual", "courant"],
    "intermediate": ["intermediate", "moyen"],
    "basic": ["basic", "beginner", "débutant"]
}


# استخراج اللغات
def extract_languages(text):
    text = text.lower()
    found = {}

    for lang, keywords in LANG_DB.items():
        for word in keywords:
            if word in text:
                found[lang] = "unknown"
                break

    return found


# استخراج المستوى
def detect_language_levels(text, languages):
    text = text.lower()

    for lang in languages:
        for level, keywords in LEVELS.items():
            for word in keywords:
                # نحاولو نلقاو مثلا: "english fluent"
                pattern = f"{lang}.*{word}"
                if re.search(pattern, text):
                    languages[lang] = level
                    break

    return languages


# scoring
def language_score(languages):
    score = 0

    for level in languages.values():
        if level == "fluent":
            score += 3
        elif level == "intermediate":
            score += 2
        elif level == "basic":
            score += 1
        else:
            score += 1  # unknown

    return score


# 🎯 FULL ANALYSIS
def analyze_languages(text):
    langs = extract_languages(text)
    langs = detect_language_levels(text, langs)
    score = language_score(langs)

    return {
        "languages": langs,
        "language_score": score
    }
