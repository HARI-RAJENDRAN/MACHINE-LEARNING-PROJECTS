import gradio as gr
import requests

OPENROUTER_API_KEY = "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"  # ← replace with your real key

def chat_openrouter(user_input, history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": user_input})

    response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://chatbot.local",  # Required domain (can be anything)
        "X-Title": "LLaMAChatBot"
    },
    json={
        "model": "meta-llama/llama-3-8b-instruct",  # ✅ Correct OpenRouter model ID
        "messages": messages
    }
)


    try:
        result = response.json()
        if "choices" not in result:
            print(result)  # Debug error response
            return f"[Error] {result}"
        reply = result["choices"][0]["message"]["content"]
        return reply
    except Exception as e:
        return f"[Exception] {e}"

gr.ChatInterface(fn=chat_openrouter, title="🦙 Meta LLaMA 3.1 8B Chatbot").launch()
