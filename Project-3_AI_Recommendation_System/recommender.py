tech_roles = {
    "Data Scientist": [
        "python", "machine learning", "statistics",
        "sql", "data analysis"
    ],

    "AI Engineer": [
        "python", "machine learning",
        "deep learning", "tensorflow", "pytorch"
    ],

    "Backend Developer": [
        "java", "spring", "sql",
        "api", "database"
    ],

    "Web Developer": [
        "html", "css", "javascript",
        "react", "nodejs"
    ],

    "DevOps Engineer": [
        "aws", "docker", "kubernetes",
        "linux", "cloud"
    ],

    "Cloud Engineer": [
        "aws", "azure", "cloud",
        "docker", "linux"
    ],

    "Cybersecurity Analyst": [
        "networking", "linux",
        "security", "ethical hacking",
        "cybersecurity"
    ],

    "Data Analyst": [
        "excel", "sql",
        "python", "power bi",
        "data analysis"
    ]
}

print("=" * 50)
print("      AI TECH STACK RECOMMENDATION SYSTEM")
print("=" * 50)

while True:

    print("\nEnter your skills separated by commas")
    user_input = input("Skills: ").lower()

    user_skills = [skill.strip() for skill in user_input.split(",")]

    scores = {}

    for role, skills in tech_roles.items():

        matches = len(
            set(user_skills).intersection(set(skills))
        )

        percentage = (matches / len(skills)) * 100

        scores[role] = percentage

    recommendations = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTop Recommendations:\n")

    if recommendations[0][1] == 0:
        print("No matching roles found.")
        print("Try entering different skills.\n")

    else:
        for role, score in recommendations[:3]:
            print(f"{role} -> {score:.0f}% Match")

    choice = input("\nWould you like another recommendation? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using the AI Recommendation System!")
        break
