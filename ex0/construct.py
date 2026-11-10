
import os
import site
import sys


def main() -> None:
    prefix = sys.prefix
    base_prefix = sys.base_prefix
    in_venv = prefix != base_prefix
    env_name = os.path.basename(prefix) if in_venv else "None detected"

    if in_venv:
        print("LABORATORY STATUS: The laboratory is sealed")
    else:
        print("LABORATORY STATUS: You are working in the open")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    if in_venv:
        print(f"Environment Path: {prefix}")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.")
        paths = site.getsitepackages()
        if paths:
            print(f"\nReagent installation path:\n{paths[0]}")
    else:
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")
        print("\nGlobal package locations:")
        for path in site.getsitepackages():
            print(path)


if __name__ == "__main__":
    main()
