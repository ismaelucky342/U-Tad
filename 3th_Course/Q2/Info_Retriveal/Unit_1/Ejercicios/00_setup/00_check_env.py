import platform
import site
import sys


def main() -> None:
    print("=== Python Environment Check ===")
    print(f"Python version: {sys.version}")
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print(f"Prefix: {sys.prefix}")
    print(f"Base prefix: {getattr(sys, 'base_prefix', 'N/A')}")
    print("\n--- site ---")
    print("site.getsitepackages:")
    for p in getattr(site, "getsitepackages", lambda: [])():
        print(" -", p)
    print("site.getusersitepackages:")
    print(" -", site.getusersitepackages())


if __name__ == "__main__":
    main()
