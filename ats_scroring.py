import re

# skills المطلوبة فالشركة (تقدر تبدلهم)
REQUIRED_SKILLS = {
    "python": 3,
    "sql": 2,
    "machine learning": 4,
    "excel": 1,
    "java": 2
}

# تنظيف النص
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text

# استخراج skills
def extract_skills(text):
    found_skills = []

    for skill in REQUIRED_SKILLS.keys():
        if skill in text:
            found_skills.append(skill)

    return found_skills

# استخراج experience
def extract_experience(text):
    matches = re.findall(r'(\d+)\s+years', text)
    if matches:
        return int(matches[0])
    return 0

# استخراج niveau d'étude
def extract_education(text):
    if "master" in text:
        return "master"
    elif "bachelor" in text or "bac+3" in text:
        return "bachelor"
    else:
        return "unknown"

# scoring system (ATS)
def calculate_ats_score(text):
    text = clean_text(text)

    skills = extract_skills(text)
    experience = extract_experience(text)
    education = extract_education(text)

    score = 0

    # 🎯 skills scoring (important)
    for skill in skills:
        score += REQUIRED_SKILLS[skill]

    # 🎯 experience scoring
    if experience >= 5:
        score += 5
    elif experience >= 2:
        score += 3
    else:
        score += 1

    # 🎯 education scoring
    if education == "master":
        score += 4
    elif education == "bachelor":
        score += 2

    return {
        "skills": skills,
        "experience": experience,
        "education": education,
        "score": score
    }
