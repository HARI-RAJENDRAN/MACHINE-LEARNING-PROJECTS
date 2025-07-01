import gradio as gr
import requests

OPENROUTER_API_KEY = "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"

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
            "HTTP-Referer": "https://your-app.com",  # any domain
            "X-Title": "GradioChatbot"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": messages
        }
    )

    try:
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        return reply  # ✅ only return the reply, not (reply, history)
    except Exception as e:
        return f"[Error] {e}"

gr.ChatInterface(fn=chat_openrouter, title="🤖 Chatbot using OpenRouter API").launch()
