from transformers import pipeline, set_seed


import os

is_local = os.environ.get('local')
task = os.environ.get('task')
model = os.environ.get('model')

dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, "pretrained", task, model)
generator = None

print(model_path)
if os.path.isdir(model_path):
    generator = pipeline(task, model=model_path)
else:
    generator = pipeline(task, model=model)
    os.makedirs(model_path)
    generator.save_pretrained(model_path)


set_seed(42)



# def generate(input):
#     txt = generator(input, max_length=30, num_return_sequences=1)
#     return txt

import gradio as gr

gr.Interface.from_pipeline(generator).launch(server_port=8080)

# demo = gr.Interface(fn=generate, inputs=gr.Textbox(lines=2, placeholder="Name Here..."), outputs="text", title="AI Chatbot", description="Ask anything you want", theme="compact")

# demo.launch(server_port=8080) 


