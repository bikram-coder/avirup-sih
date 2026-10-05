import os
import glob
import subprocess
import imageio_ffmpeg

FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()

AUDIO_FILES = [
    r"C:\Users\BIKRAM\Downloads\WhatsApp Audio 2026-10-05 at 2.12.25 PM.mpeg",
    r"C:\Users\BIKRAM\Downloads\WhatsApp Audio 2026-10-05 at 2.12.45 PM.mpeg",
    r"C:\Users\BIKRAM\Downloads\WhatsApp Audio 2026-10-05 at 2.12.45 PM (1).mpeg",
    r"C:\Users\BIKRAM\Downloads\WhatsApp Audio 2026-10-05 at 2.12.46 PM.mpeg",
    r"C:\Users\BIKRAM\Downloads\WhatsApp Audio 2026-10-05 at 2.12.46 PM (1).mpeg",
    r"C:\Users\BIKRAM\Downloads\WhatsApp Audio 2026-10-05 at 2.12.46 PM (2).mpeg"
]

RECORDINGS_DIR = os.path.abspath("./recordings")
OUTPUT_VIDEO = r"C:\Users\BIKRAM\Videos\SIH_Team_Web_Pixel_Final_Demo.mp4"
MASTER_AUDIO = os.path.abspath("./master_audio.mp3")

def merge():
    print("======================================================")
    print("Starting SIH Audio & Video Muxing Pipeline")
    print(f"Using FFMPEG binary: {FFMPEG_BIN}")
    print("======================================================")

    # 1. Verify Audio Files
    for i, a in enumerate(AUDIO_FILES, 1):
        if not os.path.exists(a):
            raise FileNotFoundError(f"Audio file {i} not found: {a}")
        print(f"Audio {i}: {os.path.basename(a)} ({os.path.getsize(a)} bytes)")

    # 2. Concatenate the 6 audios into master_audio.mp3
    print("\n>>> Concatenating 6 audio files into master soundtrack...")
    input_args = []
    filter_inputs = []
    for i, a in enumerate(AUDIO_FILES):
        input_args.extend(["-i", a])
        filter_inputs.append(f"[{i}:a]")

    filter_complex = f"{''.join(filter_inputs)}concat=n={len(AUDIO_FILES)}:v=0:a=1[outa]"
    cmd_concat = [
        FFMPEG_BIN, "-y",
        *input_args,
        "-filter_complex", filter_complex,
        "-map", "[outa]",
        "-c:a", "libmp3lame", "-q:a", "2",
        MASTER_AUDIO
    ]
    res = subprocess.run(cmd_concat, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error during audio concat:", res.stderr)
        sys.exit(1)
    print(f"Master audio track generated: {MASTER_AUDIO} ({os.path.getsize(MASTER_AUDIO)} bytes)")

    # 3. Find latest recorded video in RECORDINGS_DIR
    webm_files = sorted(glob.glob(os.path.join(RECORDINGS_DIR, "*.webm")), key=os.path.getmtime, reverse=True)
    if not webm_files:
        raise FileNotFoundError(f"No webm video files found in {RECORDINGS_DIR}")
    
    latest_webm = webm_files[0]
    print(f"\n>>> Found latest Playwright recording: {latest_webm} ({os.path.getsize(latest_webm)} bytes)")

    # 4. Mux video and master audio into final MP4
    print(f"\n>>> Muxing 1080p video with master audio into: {OUTPUT_VIDEO}")
    cmd_mux = [
        FFMPEG_BIN, "-y",
        "-i", latest_webm,
        "-i", MASTER_AUDIO,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO
    ]
    res_mux = subprocess.run(cmd_mux, capture_output=True, text=True)
    if res_mux.returncode != 0:
        print("Error during video/audio muxing:", res_mux.stderr)
        sys.exit(1)

    print("\n======================================================")
    print("SUCCESS! Final YouTube-ready SIH video created:")
    print(f"File: {OUTPUT_VIDEO}")
    print(f"Size: {os.path.getsize(OUTPUT_VIDEO) / (1024*1024):.2f} MB")
    print("======================================================")

if __name__ == "__main__":
    merge()
