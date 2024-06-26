import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("vacancies.csv")
df = data.dropna()

python_df = df[df["requirements"].str.contains("Python")]
count_python = len(python_df)

postgresql_df = df[df["requirements"].str.contains("PostgreSQL")]
count_postgresql = len(postgresql_df)

git_df = df[df["requirements"].str.contains("Git")]
count_git = len(git_df)

django_df = df[df["requirements"].str.contains("Django")]
count_django = len(django_df)

selenium_df = df[df["requirements"].str.contains("Selenium")]
count_selenium = len(selenium_df)

flask_df = df[df["requirements"].str.contains("Flask")]
count_flask = len(flask_df)

fast_df = df[df["requirements"].str.contains("Fast")]
count_fast = len(fast_df)

docker_df = df[df["requirements"].str.contains("Docker")]
count_docker = len(docker_df)

drf_df = df[df["requirements"].str.contains("Django Rest Framework")]
count_drf = len(drf_df)

ml_df = df[df["requirements"].str.contains("Machine")]
count_ml = len(ml_df)

keywords = [
    "Python",
    "PostgreSQL",
    "Git",
    "Django",
    "Selenium",
    "Flask",
    "Fast",
    "Docker",
    "Django Rest Framework",
    "Machine Learning",
]
counts = [
    count_python,
    count_postgresql,
    count_git,
    count_django,
    count_selenium,
    count_flask,
    count_fast,
    count_docker,
    count_drf,
    count_ml,
]

plt.figure(figsize=(10, 6))

plt.bar(keywords, counts, color="skyblue", edgecolor="black")
plt.xlabel("Keywords")
plt.ylabel("Count")
plt.title("The demand for skills for Python developers")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
