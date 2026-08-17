import subprocess
import json


def get_container_info(container_name):
    result = subprocess.run(
        ["docker", "inspect", "--format", "{{json .}}", container_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return json.loads(result.stdout)


def get_container_user(container_name):
    result = subprocess.run(
        ["docker", "exec", container_name, "whoami"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return result.stdout.strip()