from config import generate_with_retry

class Writer:
    def run(self, topic, analysis):
        print(f"   ⏳ Writer is drafting email...")
        prompt = f"Role: Writer. Topic: {topic}. Data: {analysis}. Task: Write a professional email to stakeholders."
        return generate_with_retry(prompt)
