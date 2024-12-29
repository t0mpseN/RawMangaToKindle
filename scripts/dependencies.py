import subprocess
import sys
import shutil

def install_python_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_ruby_gem(gem):
    gem_executable = shutil.which("gem")
    if gem_executable:
        subprocess.check_call([gem_executable, "install", gem])
    else:
        print("RubyGems executable not found. Please ensure Ruby is installed and in your PATH.")
        sys.exit(1)

def install_image_magick():
    print("Please install ImageMagick manually by following these steps:")
    print("1. Visit https://imagemagick.org/script/download.php")
    print("2. Download the appropriate version for your operating system.")
    print("3. Follow the installation instructions.")
    print("4. Ensure ImageMagick is added to your system's PATH.")
    input("Press Enter to exit. . .")

def main():
    # Install Python packages
    python_packages = ["pip", "mokuro", "pypdf"]
    for package in python_packages:
        install_python_package(package)
    
    # Install Ruby gems
    ruby_gems = ["prawn", "mini_magick"]
    for gem in ruby_gems:
        install_ruby_gem(gem)
    
    # Prompt user to install ImageMagick manually
    install_image_magick()
    
    print("All dependencies installed successfully.")

if __name__ == "__main__":
    main()