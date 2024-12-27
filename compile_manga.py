import os
import shutil

def compile_manga(manga_name, start_chapter, end_chapter):
    base_path = os.path.join(os.getcwd(), manga_name)
    volume_path = os.path.join(base_path, f'Volume_{start_chapter}_to_{end_chapter}')
    
    if not os.path.exists(volume_path):
        os.makedirs(volume_path)
    
    page_number = 1

    for chapter in range(start_chapter, end_chapter + 1):
        chapter_path = os.path.join(base_path, f'Chapter {chapter}')
        if not os.path.exists(chapter_path):
            print(f'Chapter {chapter} does not exist.')
            continue

        for image in sorted(os.listdir(chapter_path)):
            if image.endswith(('.jpg', '.png', '.jpeg')):
                image_path = os.path.join(chapter_path, image)
                shutil.copy(image_path, os.path.join(volume_path, f'{page_number:02d}.jpg'))
                page_number += 1

    print(f'Volume {start_chapter} to {end_chapter} created successfully at {volume_path}.')

if __name__ == "__main__":
    manga_name = input('Enter manga name: ')
    start_chapter = int(input('Enter start chapter: '))
    end_chapter = int(input('Enter end chapter: '))

    compile_manga(manga_name, start_chapter, end_chapter)