import os
import time
import shutil
import compile_manga
import ocr_to_pdf
from pdf_compressor import compress_pdf

volumer = ""
ocr_option = ""
ch_deletion = ""
delete_chapters = False
compress = ""

while volumer.lower() != "y" and volumer.lower() != "n":
    volumer = input("Do you want to convert chapters to a volume? (y/n): ")
    if volumer.lower() == "y":
        manga_name = input("Insert Manga Name (folder name, i.e: 'One Piece'): ")
        start_chapter = input("Insert start chapter number (i.e: if the first chapter of the volume should be Chapter 8, type '8'): ")
        end_chapter = input("Insert last chapter number (i.e: if the last chapter of the volume should be Chapter 16, type '16'): ")
        while ch_deletion.lower() != "y" and ch_deletion.lower() != "n":
            ch_deletion = input("Do you want to delete the chapter folders after creating the volume? (y/n): ")
            if ch_deletion.lower() == "y":
                delete_chapters = True
            elif ch_deletion.lower() == "n":
                delete_chapters = False
                pass
            else:
                print("Please insert a valid answer. (y/n)")
        vol_name = compile_manga.compile_manga(manga_name, start_chapter, end_chapter, delete_chapters)
        while ocr_option.lower() != "y" and ocr_option.lower() != "n":
            ocr_option = input("Do you want to get a single Volume OCR (.pdf)? (y/n): ")
            if ocr_option.lower() == "y":
                vol_name = os.path.basename(vol_name)
                ocr_to_pdf.ocr_to_pdf(manga_name, vol_name)
            elif ocr_option.lower() == "n":
                break
            else:
                print("Please insert a valid answer. (y/n)")
        break
    elif volumer.lower() == "n":
        manga_name = input("Input the name of the manga (folder name): ")
        vol_name = input("Input the volume (folder name): ")
        ocr_to_pdf.ocr_to_pdf(manga_name, vol_name)
        break
    else:
        print("Please insert a valid answer. (y/n)")

while compress.lower() != "y" and compress.lower() != "n":
    compress = input("Do you want to compress the .pdf (recommended for kindle transfer)? (y/n): ")
    if compress.lower() == "y":
         compress_pdf(f"scripts/{manga_name} - {vol_name}.pdf")
    elif compress.lower() == "n":
        src = f"scripts/{manga_name} - {vol_name}.pdf"
        dest = f"Results/{manga_name} - {vol_name}.pdf"
        if os.path.exists(dest):
            os.remove(dest)
        shutil.move(src, dest)
    else:
        print("Please insert a valid answer. (y/n)")

seconds = 10

while seconds > 0:
    mins, secs = divmod(seconds, 60)
    timer = '{:02d}'.format(secs)
    print(f"Closing in {timer}", end="\r")
    time.sleep(1)
    seconds -= 1
   
