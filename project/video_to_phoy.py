import os
import cv2

# Folder źródłowy z filmami
source_dir = "C:\\Users\\julia\\Desktop\\1_DATASET_TENIS"

# Folder docelowy na zdjęcia
target_dir = "C:\\Users\\julia\\Desktop\\tenis_photos"

# Mapowanie nazw folderów
folder_map = {
    "backhand": "backhand",
    "forehand": "forehand",
    "serwis": "serve",
    "waiting": "ready"
}

for src_folder, dst_folder in folder_map.items():
    src_path = os.path.join(source_dir, src_folder)
    dst_path = os.path.join(target_dir, dst_folder)

    # Pobieramy wszystkie filmy w folderze
    videos = [f for f in os.listdir(src_path) if f.endswith(".mp4")]

    # Numeracja plików w folderze docelowym
    counter = 1

    for video_file in videos:
        video_path = os.path.join(src_path, video_file)
        cap = cv2.VideoCapture(video_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Tworzymy nazwę pliku z numerem
            out_name = f"{counter:04d}.jpg"
            out_path = os.path.join(dst_path, out_name)

            cv2.imwrite(out_path, frame)
            counter += 1

        cap.release()
        print(f"Przetworzono wideo: {video_file} -> {dst_folder}")
