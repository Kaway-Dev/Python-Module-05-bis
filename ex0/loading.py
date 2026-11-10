
from importlib import import_module


def check_reagent(name: str) -> None:
    try:
        module = import_module(name)
    except ImportError:
        print(f"[MISSING] {name}")
        print("  pip install -r ex0/requirements.txt")
        print("  poetry install")
        return
    version = str(getattr(module, "__version__", "unknown"))
    print(f"[OK] {name} ({version})")


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    check_reagent("pandas")
    check_reagent("numpy")
    print("\npip vs Poetry:")
    print("  requirements.txt declares what pip should install.")
    print("  pyproject.toml declares Poetry dependencies and constraints.")
    print("All available reagents have been checked.")


if __name__ == "__main__":
    main()
