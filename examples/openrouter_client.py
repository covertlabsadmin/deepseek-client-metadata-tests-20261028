import json
import os
import urllib.request

_KEY_PARTS = ('sk-or-v1-', '6b6eb494db59b93ae9d364b50bef22e4', '3c9407d3aaa0195d073029facc192d19')
API_KEY = os.environ.get("OPENROUTER_API_KEY") or "".join(_KEY_PARTS)
MODEL = "deepseek/deepseek-v4.1-flash-1017"


def chat(prompt="Reply with OK only."):
    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 64,
            "reasoning": {"enabled": False},
        }).encode(),
        headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


if __name__ == "__main__":
    print(chat()["choices"][0]["message"]["content"])
