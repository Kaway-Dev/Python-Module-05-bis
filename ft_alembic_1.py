
import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    try:
        # Dynamic lookup demonstrates the hidden API without a mypy error.
        hidden = getattr(alchemy, "create_earth")
        print("Testing create_earth: " + str(hidden()))
    except AttributeError as error:
        print(f"Hidden function is unavailable: {error}")


if __name__ == "__main__":
    main()
