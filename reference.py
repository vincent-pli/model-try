from transformers import pipeline, set_seed


import os

is_local = os.environ.get('local')
task = os.environ.get('task')
model = os.environ.get('model')

if os.path.isdir("./pretrained/text-generation/gpt2"):
    generator = pipeline('text-generation', model='./pretrained/text-generation/gpt2')
else:
    generator = pipeline('text-generation', model='gpt2')
    os.makedirs("./pretrained/text-generation/gpt2")
    generator.save_pretrained("./pretrained/text-generation/gpt2")


set_seed(42)



def generate(input):
    txt = generator(input, max_length=30, num_return_sequences=1)
    return txt[0]["generated_text"]


import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=generate, inputs=gr.Textbox(lines=2, placeholder="Name Here..."), outputs="text", title="AI Chatbot", description="Ask anything you want", theme="compact")

demo.launch(server_port=8080) 


