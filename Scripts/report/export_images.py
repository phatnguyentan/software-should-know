import os
import csv
from PIL import Image

def list_images_to_csv(input_dir, output_csv):
    # Supported image extensions
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    rows = []
    counter = 1

    for root, _, files in os.walk(input_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()

            if ext in image_extensions:
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        rel_path = os.path.relpath(root, input_dir)  # relative path
                        rows.append([
                            counter,
                            file,
                            ext.replace(".", ""),
                            f"{width} x {height}",
                            rel_path if rel_path != "." else ""
                        ])
                        counter += 1
                except Exception as e:
                    print(f"Skipping {file} (error: {e})")

    # Write CSV without header
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"CSV exported successfully: {output_csv}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Export image info from directory (with subfolders) to CSV.")
    parser.add_argument("input_dir", help="Path to the input directory containing images")
    parser.add_argument("output_csv", help="Path to the output CSV file")
    args = parser.parse_args()

    list_images_to_csv(args.input_dir, args.output_csv)
