
from fastapi import FastAPI
from pydantic import BaseModel
from utils import TASKS_SUPPORTED, VALIDATE_MODELS
from launchModel.dockerImp import DockerLauncher
from fastapi.middleware.cors import CORSMiddleware


class Launch(BaseModel):
    name: str
    task: str
    model: str

class Remove(BaseModel):
    id: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
launcher = DockerLauncher()

def validate_task(task: str):
    if task in TASKS_SUPPORTED:
        return True
    return False

def validate_model(task: str, model: str):
    return VALIDATE_MODELS(task, model)

@app.post("/launch/")
async def launch(launch: Launch):
    print("start to launch...")
    if not validate_task(launch.task) or not validate_model(launch.task, launch.model):
        return {"status": "failed", "res": {"message": "'task' or 'model' is invalidated or not support, check it again..."}}
    
    
    info = launcher.launch(launch.name, launch.task, launch.model)
    print(info)
    url = "http://" + info["address"]["8080/tcp"][0]["HostIp"] + ":" + info["address"]["8080/tcp"][0]["HostPort"]


    return {"status": "success", "res": {"url": url, "id": info["id"]}}


@app.post("/remove/")
async def remove(remover: Remove):
    print("start to remove...")
    launcher.remove(remover.id)

    return {"status": "success"}

@app.get("/list/")
async def list():
    res = launcher.list()

    return {"status": "success", "res": res}