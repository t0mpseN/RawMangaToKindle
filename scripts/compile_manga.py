import os
import shutil

def compile_manga(manga_name, start_chapter, end_chapter, delete_chapters):
    base_path = f"./Mangas/{manga_name}"
    volume_path = os.path.join(base_path, f'Vol{start_chapter}to{end_chapter}')
    
    if not os.path.exists(volume_path):
        os.makedirs(volume_path)
    
    page_number = 1

    for chapter in range(int(start_chapter), int(end_chapter) + 1):
        chapter_path = os.path.join(base_path, f'Chapter {chapter}')
        if not os.path.exists(chapter_path):
            print(f'Chapter {chapter} does not exist.')
            continue

        for image in sorted(os.listdir(chapter_path)):
            if image.endswith(('.jpg', '.png', '.jpeg')):
                image_path = os.path.join(chapter_path, image)
                shutil.copy(image_path, os.path.join(volume_path, f'{page_number:03d}.jpg'))
                page_number += 1

    print(f'Volume {start_chapter} to {end_chapter} created successfully at {volume_path}.')
    
    if delete_chapters:
        for chapter in range(int(start_chapter), int(end_chapter) + 1):
            chapter_path = os.path.join(base_path, f'Chapter {chapter}')
            if os.path.exists(chapter_path):
                shutil.rmtree(chapter_path)
                print(f'Deleted {chapter_path}')

    return volume_path

if __name__ == "__main__":
    volumer = input("Do you want to convert chapters to a volume? (y/n): ")
    if volumer.lower() == "y":
        manga_name = input("Insert Manga Name (folder name, i.e: 'One Piece'): ")
        start_chapter = input("Insert start chapter number (i.e: if the first chapter of the volume should be Chapter 8, type '8'): ")
        end_chapter = input("Insert last chapter number (i.e: if the last chapter of the volume should be Chapter 16, type '16'): ")
        delete_chapters = input("Do you want to delete the chapter folders after creating the volume? (y/n): ").lower() == 'y'
        volume_path = compile_manga(manga_name, start_chapter, end_chapter, delete_chapters)