"""Human-readable study logs for training and inference observations."""


def log_info(component: str, message: str) -> None:
    print(f"[INFO] {component}: {message}")


def log_error(component: str, message: str) -> None:
    print(f"[ERROR] {component}: {message}")
