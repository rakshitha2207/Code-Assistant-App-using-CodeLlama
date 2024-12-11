import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "CodeEasy",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    else:
        return f"Error: {response.text}"

with gr.Blocks() as app:
    gr.Markdown("## Code Assistant App Using Code Llama")
    with gr.Row():
        input_box = gr.Textbox(lines=4, placeholder="Enter your Prompt", label="Prompt")
        output_box = gr.Textbox(label="Response")
    submit_btn = gr.Button("Submit")
    submit_btn.click(generate_response, inputs=input_box, outputs=output_box)

# Launch the app
if __name__ == "__main__":
    app.launch()
