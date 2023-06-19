from voice_loader import record_audio
from voice_transformer import *

def main():
    # Usage example
    output_filename = 'recorded_audio.flac'  # Provide the desired output filename
    duration = 10  # Specify the duration of the recording in seconds
    record_audio(output_filename, duration)

    data = query(output_filename)
    print(data)

if __name__ == "__main__":
    main()
