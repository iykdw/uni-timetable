import os
import sys

from pdf2image import convert_from_path
from pypdf import PdfReader, PdfWriter, Transformation

file = sys.argv[1]

reader = PdfReader(file)
writer = PdfWriter()
scale = Transformation().scale(sx=0.9, sy=0.9)
for i in range(len(reader.pages)):
    page = reader.pages[i]
    move = Transformation().translate(0, page.mediabox.height / 10)
    page.add_transformation(scale)
    page.add_transformation(move)
    writer.add_page(page)

writer.write("compiled.pdf")

reader = PdfReader(sys.argv[1])
writer = PdfWriter()

days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    cropped_x = page.mediabox.right / 2
    cropped_y = (cropped_x / 9) * 19.5
    buffer_x = (page.mediabox.right - cropped_x) / 2
    buffer_y = (page.mediabox.top - cropped_y) / 2
    page.mediabox.upper_right = (
        (page.mediabox.right - buffer_x),
        (page.mediabox.top - buffer_y),
    )
    page.mediabox.lower_left = (
        (page.mediabox.left + buffer_x),
        (page.mediabox.bottom + buffer_y),
    )

    writer.add_page(page)
    filename = f"{days[i]}.pdf"
    with open(filename, "wb") as fp:
        writer.write(fp)

    page = convert_from_path(filename, 500)[0]

    page.save(f"{days[i]}.jpg", "JPEG")

os.system("rm *.pdf *.aux *.fdb_latexmk *.fls *.log *.synctex.gz")
