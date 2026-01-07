from config import generate_with_retry

class Analyst:
    def run(self, data):
        print(f"   ⏳ Analyst is processing data...")
        prompt = f"Role: Analyst. Context: {data}. Task: 3 bullet points & 1 summary sentence."
        return generate_with_retry(prompt)
