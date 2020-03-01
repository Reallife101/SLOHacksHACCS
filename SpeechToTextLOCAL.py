# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "speech_transcribe_sync")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-speech

# sample-metadata
#   title: Transcribe Audio File (Local File)
#   description: Transcribe a short audio file using synchronous speech recognition
#   usage: python3 samples/v1/speech_transcribe_sync.py [--local_file_path "resources/brooklyn_bridge.raw"]

# [START speech_transcribe_sync]

from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
import io

import GlobalVariables


def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition
    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech_v1p1beta1.SpeechClient()

    # local_file_path = 'resources/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    # LINEAR16
    encoding = enums.RecognitionConfig.AudioEncoding.MP3

    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)

    # print("response: {}".format(response))

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        GlobalVariables.command=alternative.transcript
        print(u"Transcript: {}".format(alternative.transcript))


# [END speech_transcribe_sync]


def main():
    import argparse

    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--local_file_path", type=str, default="recording.mp3"
    # )
    # args = parser.parse_args()

    sample_recognize("recording.mp3")


if __name__ == "__main__":
    main()