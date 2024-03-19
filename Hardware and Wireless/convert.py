import os

folder_path = "wireless/converted/Slide 04/"
markdown_file = "wireless/04.md"

with open(markdown_file, "w") as md:
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            slide_number = os.path.splitext(filename)[0].split("_")[-1]  # Assuming image files are named as slide_1.png, slide_2.png, etc.
            abs_slide_number = abs(int(slide_number))
            md.write(f"### {abs_slide_number}\n![[{folder_path}{slide_number}.png]]\n\n")
