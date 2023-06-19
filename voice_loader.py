import pyaudio
import wave
from pydub import AudioSegment

def record_audio(output_filename, duration=5, sample_rate=44100, channels=2):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=1024)

    print("Recording started...")

    frames = []
    for _ in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the audio recording as a WAV file
    wave_file = wave.open(output_filename, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    print(f"Audio saved as {output_filename}")




# file_new = AudioSegment.from_wav("recorded_audio.wav")
# file_new.export("recorded_audio.flac",format = "flac")