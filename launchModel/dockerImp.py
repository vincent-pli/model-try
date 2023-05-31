import docker
from pydantic import BaseModel


class DockerLauncher(BaseModel):

    def launch(self, task: str, model: str):
        environments = {
            "task": task,
            "model": model,
            "GRADIO_SERVER_NAME": "0.0.0.0",
        }

        ports = {'8080': None}
        volumn = {'/Users/lipeng/workspaces/github.com/vincent-pli/model-try/pretrained': {'bind': '/app/pretrained', 'mode': 'rw'}}

        client = docker.from_env()
        container = client.containers.run(
            "docker.io/vincentpli/mode-base:v0.3", detach=True, environment=environments, ports=ports, volumes = volumn)
        container.reload()
        print(container.ports)
        return { "address": container.ports, "id": container.id }
    

    def remove(self, containerID: str):
        client = docker.from_env()
        containers = client.containers.list(filters={"id": containerID})
        
        if(len(containers) != 0):
            containers[0].remove(force=True)

        return None