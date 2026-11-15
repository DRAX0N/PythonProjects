# Folder z plikami mp4

from pathlib import Path
import subprocess
import tempfile
import os

floder_paths = ["miaa-766-uncensored-leak", "nghj-055-uncensored-leak", "murikuri-007", "fsdss-671-uncensored-leak", "fsdss-769-uncensored-leak", "ipx-985-uncensored-leak", "ipx-850-uncensored-leak"]

for folder_name in floder_paths:
    folder = Path(r"F:\\Downloads\\xxx\\xxx-sxyprn com\\download\\" + folder_name)
    output_file = r"F:\\Downloads\\xxx\\xxx-sxyprn com\\download\\" + folder_name + ".mp4"


    mp4_files = sorted(folder.glob("*.mp4"))

    if not mp4_files:
        raise SystemExit("Brak plików MP4 w folderze.")

    ffmpeg_path = r"C:\\Users\\rafwz\\Downloads\\ffmpeg-2026-05-28-git-7b46c6a2a3-full_build\\bin\\ffmpeg.exe"   # <-- ustaw swoją ścieżkę

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt", encoding="utf-8") as f:
        list_file = f.name
        for file in mp4_files:
            f.write(f"file '{file.as_posix()}'\n")

    cmd = [
        ffmpeg_path,
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        str(output_file)
    ]

    subprocess.run(cmd, check=True)
    os.remove(list_file)

    print(f"Gotowe: {output_file}")