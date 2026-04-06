import re

# 🎓 EDUCATION EXTRACTION (multi-language)
def extract_education(text):
    text = text.lower()

    education_levels = {
        "phd": ["phd", "doctorat"],
        "master": ["master", "bac+5", "msc"],
        "bachelor": ["bachelor", "licence", "bac+3"],
        "bac": ["bac", "high school"]
    }

    for level, keywords in education_levels.items():
        for word in keywords:
            if word in text:
                return level

    return "unknown"


# 💼 EXPERIENCE EXTRACTION (advanced)
def extract_experience(text):
    text = text.lower()

    patterns = [
        r'(\d+)\s+years',
        r'(\d+)\s+year',
        r'(\d+)\s+ans',
        r'expérience\s+de\s+(\d+)'
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))

    return 0


# 🧠 EXPERIENCE LEVEL
def experience_level(years):
    if years >= 7:
        return "expert"
    elif years >= 5:
        return "senior"
    elif years >= 2:
        return "mid"
    elif years > 0:
        return "junior"
    else:
        return "no experience"


# 📊 EDUCATION SCORE
def education_score(level):
    scores = {
        "phd": 5,
        "master": 4,
        "bachelor": 3,
        "bac": 1,
        "unknown": 0
    }
    return scores.get(level, 0)


# 📊 EXPERIENCE SCORE
def experience_score(years):
    if years >= 7:
        return 6
    elif years >= 5:
        return 5
    elif years >= 2:
        return 3
    elif years > 0:
        return 1
    else:
        return 0


# 🎯 FULL ANALYSIS
def analyze_education_experience(text):
    education = extract_education(text)
    experience = extract_experience(text)

    level = experience_level(experience)

    edu_score = education_score(education)
    exp_score = experience_score(experience)

    total = edu_score + exp_score

    return {
        "education": education,
        "experience_years": experience,
        "experience_level": level,
        "education_score": edu_score,
        "experience_score": exp_score,
        "total_score": total
    }
