"""Small path/loading examples for students working with WAV audio or video."""

from pathlib import Path
import wave


def inspect_wav(path):
    """Print basic properties of an uncompressed WAV file."""
    path = Path(path)
    with wave.open(str(path), "rb") as recording:
        frame_rate = recording.getframerate()
        frame_count = recording.getnframes()
        print("File:", path.name)
        print("Channels:", recording.getnchannels())
        print("Sample rate:", frame_rate)
        print("Duration (seconds):", frame_count / frame_rate)


def inspect_video(path):
    """Print basic video properties if OpenCV is installed."""
    try:
        import cv2
    except ImportError:
        print("Video example requires OpenCV: uv pip install opencv-python")
        return

    path = Path(path)
    video = cv2.VideoCapture(str(path))
    if not video.isOpened():
        raise ValueError(f"Could not open video: {path}")

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video.release()

    print("File:", path.name)
    print("Frames:", frame_count)
    print("Frame rate:", frame_rate)
    print("Frame size:", (width, height))
    if frame_rate:
        print("Duration (seconds):", frame_count / frame_rate)


if __name__ == "__main__":
    print("Set a path to one of your own small files, then call:")
    print("  inspect_wav('/path/to/example.wav')")
    print("or:")
    print("  inspect_video('/path/to/example.mp4')")
