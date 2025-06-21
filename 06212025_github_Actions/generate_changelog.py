import os
from openai import OpenAI

with open(os.path.join(os.path.dirname(__file__), "commits.txt"), "r") as f:
    commits = f.read()

prompt = f"""
You are a helpful release assistant.
Summarize the following commit messages into a professional changelog with section titles and short bullets.

Commits:
{commits}
"""

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

    result = response.choices[0].message.content

    changelog_path = os.path.join(os.path.dirname(__file__), "changelog.md")
    print(f"🧭 Writing to: {changelog_path}")

    with open(changelog_path, "w") as f:
        f.write(result)

    print("✅ Changelog generated.")
except Exception as e:
    print(f"❌ Failed to generate changelog: {e}")