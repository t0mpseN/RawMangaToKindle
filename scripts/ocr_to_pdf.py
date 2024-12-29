import os
import subprocess
import shutil

def find_ruby_path():
    ruby_executable = shutil.which("ruby")
    if ruby_executable:
        print(f"Ruby executable found at: {ruby_executable}")
        return ruby_executable
    else:
        print("Ruby executable not found in PATH.")
        return None

def ocr_to_pdf(manga_name, vol_name):
    base_path = "./Mangas"
    manga_path = f"{base_path}/{manga_name}/{vol_name}"

    mokuro_command = [
        "mokuro", manga_path,
        "--force_cpu", "--disable_confirmation", "--ignore_errors"
    ]
    print("Running mokuro. . . This can take a while (check progress on Mangas/_ocr/[vol]. When all pages are done the script will resume.) ")
    ocr = subprocess.run(mokuro_command, shell=True, capture_output=True, text=True)
    print(ocr.stdout)
    print(ocr.stderr)

    ruby_path = find_ruby_path() #CHANGE THIS DEPENDING ON YOUR RUBY VERSION (or if its not on PATH)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mokuro2pdf_script = os.path.join(script_dir, "Mokuro2Pdf-master", "Mokuro2Pdf.rb")
    base_path2 = "../Mangas"
    manga_path2 = f"{base_path2}/{manga_name}/{vol_name}"
    ocr_path = f"../Mangas/{manga_name}/_ocr/{vol_name}"

    mokuro2pdf = [
        ruby_path, mokuro2pdf_script,
        "-i", manga_path2,
        "-o", ocr_path,
        "-n", f"{manga_name} - {vol_name}",
        "-f", "0.1",
        "-g", "0.5",
        "-u"
    ]

    env = os.environ.copy()

    print("Running mokuro2pdf. . . Please wait.")
    ocrtopdf = subprocess.run(mokuro2pdf, capture_output=True, text=True, cwd=script_dir, env=env)

    print(ocrtopdf.stdout)
    print(ocrtopdf.stderr)
    
if __name__ == "__main__":
    manga_name = input("Input the name of the manga (folder name): ")
    vol_name = input("Input the volume (folder name): ")
    ocr_to_pdf(manga_name, vol_name)