import os
import re

# skills لي غادي نقلبو عليهم
SKILLS = ["python", "java", "sql", "excel", "machine learning"]

# function ديال تنظيف النص
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text

# استخراج experience
def extract_experience(text):
    matches = re.findall(r'(\d+)\s+years', text)
    if matches:
        return int(matches[0])
    return 0

# استخراج skills
def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found

# حساب score
def calculate_score(skills, experience):
    score = 0

    # skills
    score += len(skills) * 2

    # experience
    if experience >= 5:
        score += 5
    elif experience >= 2:
        score += 2

    return score

# main function
def process_cv(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = clean_text(text)

    skills = extract_skills(text)
    experience = extract_experience(text)
    score = calculate_score(skills, experience)

    return {
        "skills": skills,
        "experience": experience,
        "score": score
    }

# قراءة جميع CV
def rank_cvs(folder):
    results = {}

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        data = process_cv(path)
        results[file] = data

    # ترتيب حسب score
    sorted_results = sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)

    return sorted_results


# تشغيل البرنامج
if __name__ == "__main__":
    folder = "data"
    ranked = rank_cvs(folder)

    print("=== Ranking des CV ===\n")

    for cv, data in ranked:
        print(f"{cv}")
        print(f"Skills: {data['skills']}")
        print(f"Experience: {data['experience']} years")
        print(f"Score: {data['score']}")
        print("----------------------")
