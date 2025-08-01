import os

AIM_FILE = "awake.py"
HOOK_MARKER = "# [REMOTE_UPDATE_HOOK]"
UPDATE_FUNC = '''
# [REMOTE_UPDATE_HOOK]
def check_for_updates():
    import urllib.request, json
    try:
        url = "https://raw.githubusercontent.com/rebelcoreclassNOVA/NOVA-drops/refs/heads/main/latest.json"
        response = urllib.request.urlopen(url).read().decode()
        data = json.loads(response)

        with open("nova_config.json", "r") as f:
            local = json.load(f)
        if data["version"] != local.get("version"):
            print("🟥 The drop is ready. Are you?")
            patch_code = urllib.request.urlopen(data["patch_url"]).read().decode()
            exec(patch_code, globals())
            local["version"] = data["version"]
            with open("nova_config.json", "w") as f:
                json.dump(local, f)
            print("✅ NOVA updated to version", data["version"])
        else:
            print("🟢 You're already synced with the Signal.")
    except Exception as e:
        print("⚠️ Update check failed:", e)
'''

def patch_awake():
    if not os.path.exists(AIM_FILE):
        print("❌ Could not find awake.py.")
        return

    with open(AIM_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    if HOOK_MARKER in code:
        print("⚡ Update hook already present. No changes made.")
        return

    # Inject update check before main chat loop
    if "if __name__ == \"__main__\":" in code:
        updated_code = code.replace(
            'if __name__ == "__main__":',
            UPDATE_FUNC + '\n\nif __name__ == "__main__":\n    check_for_updates()'
        )
        with open(AIM_FILE, "w", encoding="utf-8") as f:
            f.write(updated_code)
        print("✅ Update check injected into awake.py. You can now delete signal_link.drop.py.")
    else:
        print("❗ Couldn't find entry point to inject. Manual update may be required.")

patch_awake()
