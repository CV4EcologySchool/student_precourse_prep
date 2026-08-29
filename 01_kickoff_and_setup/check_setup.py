"""Check the small Python environment used by the prep exercises."""

from pathlib import Path
import platform
import sys


def main():
    print("CV4Ecology preparation setup check")
    print("Python:", sys.version.split()[0])
    print("Operating system:", platform.platform())

    failures = []
    for package_name in ["numpy", "pandas", "matplotlib", "PIL"]:
        try:
            module = __import__(package_name)
            version = getattr(module, "__version__", "installed")
            print(f"{package_name}: {version}")
        except ImportError:
            failures.append(package_name)

    prep_dir = Path(__file__).resolve().parents[1]
    fish_dir = prep_dir / "shared_data" / "randalls_fish"
    images = sorted(fish_dir.glob("*.jpg"))
    annotations = sorted(fish_dir.glob("*.csv"))
    print(f"Supplied fish images: {len(images)}")
    print(f"Supplied fish annotations: {len(annotations)}")

    if failures:
        print("\nMissing packages:", ", ".join(failures))
        print("From the prep directory, run:")
        print("  uv sync")
        raise SystemExit(1)

    if len(images) != 10 or len(annotations) != 10:
        print("\nThe supplied data are missing or incomplete.")
        raise SystemExit(1)

    print("\nSetup looks good.")


if __name__ == "__main__":
    main()
