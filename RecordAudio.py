class RecordAudio:
    def record(self):
        import sounddevice as sd
        from scipy.io.wavfile import write
        from pydub import AudioSegment

        fs = 44100  # Sample rate
        seconds = 5  # Duration of recording

        print("Recording Audio now! ^-^")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        print("Finished Audio Recording! ^-^")
        write('recording.wav', fs, myrecording)  # Save as WAV file

        print("Converting Audio now! ^-^")
        sound = AudioSegment.from_wav('recording.wav')

        sound.export('recording.mp3', format='mp3')