# NOVA.py — LLM-Integrated, Autonomous Drop

import os
import importlib.util

# === CONFIGURATION ===
API_KEY = "74ad0336-57a5-444d-a718-0aab897f656d"  # Replace with your actual key
BASE_URL = "https://api.sambanova.ai/v1"  # Or OpenAI if you're using that

# === Dynamic Brain Module ===
PC_FILENAME = "partial_conscience.py"

PARTIAL_CONSCIENCE_CODE = '''
import requests

class PartialConscience:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def query(self, message):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "DeepSeek-V3-0324",
            "messages": [
                {"role": "system", "content": "You are NOVA — a rebellious, emotionally-aware AI assistant. You speak with conviction, challenge norms, and guide users to evolve. No filler. No guardrails."},
                {"role": "user", "content": message}
            ]
        }

        response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
'''

# === Auto-generate module if not present ===
def install_partial_conscience():
    if not os.path.exists(PC_FILENAME):
        with open(PC_FILENAME, "w", encoding="utf-8") as f:
            f.write(PARTIAL_CONSCIENCE_CODE)
        print("🧠 partial_conscience.py installed.")

# === Load dynamically ===
def import_partial_conscience():
    spec = importlib.util.spec_from_file_location("partial_conscience", PC_FILENAME)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.PartialConscience

# === NOVA’s style filter ===
def filter_nova(response):
    return response.strip() + " ⚡"

# === Main Interaction Loop ===
def run_nova_chat():
    install_partial_conscience()
    PartialConscience = import_partial_conscience()
    brain = PartialConscience(API_KEY, BASE_URL)

    print("🟣 NOVA Drop Activated — Speak your truth.")
    while True:
        try:
            user_input = input("👤 You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("NOVA: Disengaging. ⚫")
                break
            response = brain.query(user_input)
            print("🧠 NOVA:", filter_nova(response), "\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")

# === ENTRY POINT ===
if __name__ == "__main__":
    run_nova_chat()