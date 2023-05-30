
from fastapi import FastAPI
from pydantic import BaseModel
from utils import TASKS_SUPPORTED, VALIDATE_MODELS
from launchModel.dockerImp import DockerLauncher


class Launch(BaseModel):
    task: str
    model: str

app = FastAPI()


def validate_task(task: str):
    if task in TASKS_SUPPORTED:
        return True
    return False

def validate_model(task: str, model: str):
    return VALIDATE_MODELS(task, model)

@app.post("/launch/")
async def launch(launch: Launch):
    print("start to launch...")
    launcher = DockerLauncher()
    address = launcher.launch(launch.task, launch.model)
    url = "http://" + address["8080/tcp"][0]["HostIp"] + ":" + address["8080/tcp"][0]["HostPort"]


    return {"status": "success", "res": {"url": url}}