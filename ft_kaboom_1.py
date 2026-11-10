

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Forbidden", "bats and arsenic"))


if __name__ == "__main__":
    main()
