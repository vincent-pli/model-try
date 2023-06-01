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
    print("loading from local, since the model is already there...")
    generator = pipeline(task, model=model_path)
else:
    generator = pipeline(task, model=model)
    os.makedirs(model_path)
    generator.save_pretrained(model_path)


set_seed(42)



import gradio as gr

instance = gr.Interface.from_pipeline(generator)
instance.title = "测试：" + model
instance.launch(server_port=8080)


