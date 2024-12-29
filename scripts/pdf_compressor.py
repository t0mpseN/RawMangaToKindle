import os
import shutil
from pypdf import PdfWriter

def compress_pdf(source_file_path):
    writer = PdfWriter(clone_from=source_file_path)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=20) #Change this from 1 to 100, HIGHER = BETTER QUALITY, LOWER = LOWER SIZE

    with open(os.path.basename(source_file_path), "wb") as f:
        writer.write(f)
    
    os.remove(source_file_path)
    
    src = os.path.basename(source_file_path)
    dest = f"Results/{src}"
    
    shutil.move(src, dest)
        
    print(f"{os.path.basename(source_file_path)} is ready at 'Results' folder.")

