import os
import csv
from PIL import Image

def list_images_to_csv(input_dir):
    # Clean input (remove wrapping quotes and extra spaces)
    input_dir = input_dir.strip().strip('"').strip("'")

    # Supported image extensions
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    rows = []
    counter = 1

    for root, _, files in os.walk(input_dir):
        for file in sorted(files):  # sorted for consistent output
            ext = os.path.splitext(file)[1].lower()

            if ext in image_extensions:
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        rel_path = os.path.relpath(root, input_dir)  # relative path
                        size_kb = os.path.getsize(file_path) // 1024
                        rows.append([
                            counter,
                            file,
                            ext.replace(".", ""),
                            f"{width} x {height}",
                            f"{size_kb} KB",
                            rel_path if rel_path != "." else ""
                        ])
                        counter += 1
                except Exception as e:
                    print(f"Skipping {file} (error: {e})")

    # Output CSV always in current working directory
    output_csv = os.path.join(os.getcwd(), "images_info.csv")

    # Write CSV with header
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Filename", "Extension", "Resolution", "Size", "Subfolder"])
        writer.writerows(rows)

    print(f"CSV exported successfully: {output_csv}")


if __name__ == "__main__":
    # Ask user for input directory
    input_dir = input("Enter the path to the input directory: ").strip()
    list_images_to_csv(input_dir)
