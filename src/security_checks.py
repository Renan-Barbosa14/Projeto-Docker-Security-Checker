def check_running(status):
    if status == "running":
        return True, "Container is running"

    return False, "Container is not running"


def check_root_user(user):
    if user == "root":
        return False, "Container is running as root"

    return True, "Container is running as non-root"


def check_privileged(privileged):
    if privileged:
        return False, "Container is running in privileged mode"

    return True, "Privileged mode disabled"


def check_readonly(readonly):
    if readonly:
        return True, "Root filesystem is read-only"

    return False, "Root filesystem is writable"


def check_host_network(network_mode):
    if network_mode == "host":
        return False, "Container is using host network"

    return True, "Host network disabled"