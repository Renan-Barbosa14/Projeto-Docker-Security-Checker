import argparse
from docker_checker import get_container_info, get_container_user
from security_checks import (
    check_running,
    check_root_user,
    check_privileged,
    check_readonly,
    check_host_network
)


def main():
    parser = argparse.ArgumentParser(description="Auditoria de Segurança de Containers Docker")
    parser.add_argument("container", help="Nome do container para analisar")
    args = parser.parse_args()

    try:
        container = get_container_info(args.container)
        user = get_container_user(container)

    except RuntimeError as error:
        print(f"[ERROR] {error}")
        return

    name = container["Name"].lstrip("/")
    image = container["Config"]["Image"]
    status = container["State"]["Status"]
    privileged = container["HostConfig"]["Privileged"]
    readonly = container["HostConfig"]["ReadonlyRootfs"]
    network_mode = container["HostConfig"]["NetworkMode"]

    print("DOCKER SECURITY CHECKER")

    print(f"\nContainer: {name}")
    print(f"Image:     {image}")
    print(f"Status:    {status}")
    print(f"User:      {user}")

    print("\nSecurity Checks")

    checks = [
        check_running(status),
        check_root_user(user),
        check_privileged(privileged),
        check_readonly(readonly),
        check_host_network(network_mode)
    ]

    passed = 0

    for result, message in checks:
        if result:
            print(f"[PASS] {message}")
            passed += 1
        else:
            print(f"[WARN] {message}")

    score = int((passed / len(checks)) * 100)

    print(f"\nSecurity Score: {score}/100")

if __name__ == "__main__":
    main()