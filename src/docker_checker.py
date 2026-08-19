import subprocess
import json

def get_container_info(container_name: str) -> dict:
    result = subprocess.run(
        ["docker", "inspect", "--format", "{{json .}}", container_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return json.loads(result.stdout)

def get_container_user(container_info: dict) -> str:
    user = container_info["Config"]["User"]
    
    if not user:
        return "root"
    return user