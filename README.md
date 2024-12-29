# **単行本職人 & RM2OCR-PDF**

RawMangaToOCR-PDF is a Python script designed to compile Japanese manga chapters into volumes (単行本), convert raw manga pages into a single OCR-processed PDF using Mokuro and Mokuro2PDF, and compress the resulting file with PyPDF for efficient storage (e.g., for Kindle).

For example, if users obtain their raw manga chapters using [Hakuneko](https://github.com/manga-download/hakuneko), they should **organize their files with the following folder structure and file name (mainly "Chapter X" and pages "01", "02", etc...)**:

```
RawMangaToOCR-PDF/  # Root directory of the project (Git repo)
├── Mangas/  # Place your raw manga chapters here
│   └── manga_name/  # (e.g., One Piece)
│       ├── Chapter 1/  # All pages from Chapter 1 as image files name with zero-padded format (e.g., 05.jpg)
│       │   ├── 01.jpg
│       │   ├── 02.jpg
│       │   └── ...
│       ├── Chapter 2/
│       │   ├── 01.jpg
│       │   ├── 02.jpg
│       │   └── ...
│       └── ...
├── Results/  # Final output folder for compiled manga volumes
│   └── manga_volume.pdf  # Your OCR-processed (and compressed PDF, if you opted for compression when running the script)
├── scripts/  # Utility scripts (ignore this unless you know what you're doing)
├── install_dependencies.bat  # Batch file to install required dependencies (please read DEPENDENCIES)
└── start.bat  # Main script to run the program
```

## USAGE

The main scope of this script is to make **Japanese text selectable through .pdf files**, being able to open them on browsers while using extensions like [Yomitan](https://github.com/yomidevs/yomitan), or even sending manga directly to Kindle and using the digital dictionaries, turning Japanese reading more *enjoyable* and *accessible*.

### RESULT EXAMPLE

- Click on the image to view the OCR-processed PDF.
  
[![EXAMPLE](https://github.com/user-attachments/assets/e54a82ff-fc3e-439b-8ad1-ea420aba9e2b)](https://github.com/user-attachments/files/18268420/Example.-.Vol1to1.pdf)

*Images from **Astro Boy by Tezuka Osamu. 鉄腕アトム - 手塚 治虫***

## INSTRUCTIONS

### (A) COMPILING CHAPTERS INTO VOLUMES
1. Install all the [requirements as written below](#requirements).
2. Create or insert a folder with the name of your chosen manga inside the `Mangas/` folder located on the main folder (*check the folder structure above*).
3. Inside your chosen manga folder, you must have your chapters folders named like "Chapter `insert chapter number`", for example, "Chapter 1", or "Chapter 15" (*check the folder structure above*).
4. Inside the chapters folders there must be an image for each page, named with zero-padded format like "01.jpg", "02.jpg", "15.jpg", etc... (*check the folder structure above*)
5. After everything is in place and correctly named, run start.bat if using Windows (*for other distros run main.py inside* `scripts/`).
6. Follow the terminal prompt instructions. **OBSERVATION: *Don't use `"` when typing manga name, chapter number, etc***.
### (B) OCR-PDF
1. Do the same as in (A). **If you already have a Volume or Chapter folder ready to OCR, you can skip the Chapter to Volume compilation (just type `n` when asked `Do you want to convert chapters to a volume? (y/n):`).**
2. If you want to adjust the .pdf compression, you can edit the line `img.replace(img.image, quality=20) #Change quality from 1 to 100, HIGHER = BETTER QUALITY, LOWER = LOWER SIZE` inside `scripts/pdf_compressor.py`.

## REQUIREMENTS

The script `install_dependencies.bat` should install all the dependencies needed to run the script, **except** [ImageMagick](https://imagemagick.org/script/download.php). In case one or more of the dependencies fail to install, please do manually install them through the links/commands written below **(be sure to add the signaled ones to PATH)**:

**Notice that if you are using an *Unix distro* or any OS other than *Windows*, you should manually install the dependencies below, and then run the `main.py` script inside `/scripts`. There is no guarantee they will work.**

- [Python](https://www.python.org/downloads/)

- [pip](https://pypi.org/project/pip/) `pip install pip`

- [Mokuro](https://github.com/kha-white/mokuro) `pip install mokuro`

- [Mokuro2Pdf](https://github.com/Kartoffel0/Mokuro2Pdf) *(already included inside scripts, needing only the dependencies listed below)*

  - [Ruby](https://rubyinstaller.org/downloads/) **(needs to be on PATH)**

  - Prawn `gem install prawn`

  - MiniMagick `gem install mini_magick`

- [ImageMagick](https://imagemagick.org/script/download.php) **(needs to be on PATH)**

- [PDF Compression (optional)](https://pypdf.readthedocs.io/en/stable/user/file-size.html) - `pip install pypdf`

## CREDITS

All credits go to the creators of [Mokuro](https://github.com/kha-white/mokuro), [Mokuro2Pdf](https://github.com/Kartoffel0/Mokuro2Pdf) and all other dependencies used on this project. *This is a simple program that tries to simplify the process while adding some basic features like **chapter compiling** and **pdf compression**.*
