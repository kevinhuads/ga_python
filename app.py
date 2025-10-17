import argparse

def main(name: str) -> str:
    """Return the greeting message (so it can be tested)."""
    return f"Hello from Python app, {name}!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Small demo app")
    parser.add_argument("--name", default="world", help="Name to greet")
    args = parser.parse_args()
    print(main(args.name))