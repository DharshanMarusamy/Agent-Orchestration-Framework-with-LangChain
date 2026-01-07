from config import generate_with_retry

class Researcher:
    def run(self, topic):
        print(f"   ⏳ Researcher is looking up '{topic}'...")
        prompt = f"Role: Researcher. Task: detailed technical facts about '{topic}'."
        return generate_with_retry(prompt)
