from faster_whisper import WhisperModel
import os, subprocess

for dir_path, _, files in os.walk("raw"):
    for filename in files:
        if not os.path.exists(os.path.join("res", os.path.splitext(os.path.basename(filename))[0] + ".txt")):
            print(f"Start converting {os.path.join(dir_path, filename)}")
            subprocess.check_call([
                "ffmpeg",
                "-i", os.path.join(dir_path, filename),
                "-progress", "-",
                os.path.join("source", os.path.splitext(os.path.basename(filename))[0] + ".wav"),
            ])
            print(f"Converted {os.path.join(dir_path, filename)}")

model = WhisperModel("large-v3-turbo", device="cuda", compute_type="float32")
for file in os.listdir("source"):
    print(os.path.join("res", os.path.splitext(os.path.basename(file))[0]+".txt"))
    segments, _ = model.transcribe(
        os.path.join("source", file),
        #language="ja",
        beam_size=10,
        vad_filter=True,
        vad_parameters= {
            "min_silence_duration_ms": 500,
        }, 
    )
    res = []
    for seg in segments:
        if len(res) == 0 or res[-1] != seg.text:
            res.append(seg.text)
            print(seg.text)
    with open(os.path.join("res", os.path.splitext(os.path.basename(file))[0]+".txt"), "w") as f:
        f.write("\n".join(res))
    print(f'Exported to {os.path.join("res", os.path.splitext(os.path.basename(file))[0]+".txt")}')
print("Finished job")
