from pip._internal.models import candidate

candidates = [
{"name": "Олексій", "skills": {"Python", "Django", "Git", "SQL", "English"}},
{"name": "Марія", "skills": {"Java", "Spring", "SQL", "English", "Docker"}},
{"name": "Іван", "skills": {"Python", "Git", "Linux"}},
{"name": "Оксана", "skills": {"Python", "FastAPI", "PostgreSQL", "Git", "English",
"Docker"}}
    ]

vacancy_requirements = {"Python", "Django", "Git", "SQL", "Docker"}


def calculate_match(candidate_skills, required_skills):
    is_perfect = False

    skills_req_count = len(required_skills)
    matching_count = len(candidate_skills.intersection(required_skills))
    match_percent = (matching_count/skills_req_count)*100

    missing_skills = required_skills.difference(candidate_skills)

    if match_percent > 50: is_perfect = True

    dictionary = [
        {"match_percent" : match_percent} ,
        {"missing_skills" : missing_skills},
        {"is_perfect" : is_perfect}]
    return dictionary


def find_best_candidates(candidates_db, vacancy):
    result_db = []
    for candidate in candidates_db:
        candidate["results"] = calculate_match(candidate["skills"], vacancy)
        result_db.append(candidate)
    return result_db


def print_report(results):

    for candidate in results:
        print(f"Кандидат: {candidate['name']}")
        print(f"- Відповідність: {candidate['results'][0]['match_percent']} %")
        print(f"- Не вистачає: {candidate['results'][1]['missing_skills']}")



report = find_best_candidates(candidates, vacancy_requirements)
print_report(report)