from education_experience import analyze_education_experience

# 🎯 skills + synonyms
SKILLS_DB = {
    "python": ["python"],
    "java": ["java"],
    "sql": ["sql", "mysql", "postgres"],
    "excel": ["excel"],
    "machine learning": ["machine learning", "ml", "ai"],
    "data analysis": ["data analysis", "pandas", "numpy"]
}

# 🌍 languages
LANGUAGES = ["english", "french", "arabic", "spanish"]

# استخراج skills بطريقة ذكية
def extract_skills(text):
    text = text.lower()
    found = []

    for skill, keywords in SKILLS_DB.items():
        for word in keywords:
            if word in text:
                found.append(skill)
                break

    return list(set(found))


# استخراج اللغات
def extract_languages(text):
    text = text.lower()
    langs = []

    for lang in LANGUAGES:
        if lang in text:
            langs.append(lang)

    return langs


# عدد الشركات (approximation)
def extract_companies(text):
    # simple estimation: count "company" or "worked at"
    text = text.lower()
    count = text.count("company") + text.count("worked at")
    return count


# 🎯 FULL FEATURES EXTRACTION
def extract_features(text):
    text = text.lower()

    skills = extract_skills(text)
    languages = extract_languages(text)
    companies = extract_companies(text)

    edu_exp = analyze_education_experience(text)

    return {
        "skills": skills,
        "languages": languages,
        "companies_count": companies,
        "education": edu_exp["education"],
        "experience_years": edu_exp["experience_years"],
        "experience_level": edu_exp["experience_level"],
        "education_score": edu_exp["education_score"],
        "experience_score": edu_exp["experience_score"]
    }
