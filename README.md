# Text-to-Speech Conversion Tool

This Python script utilizes the ElevenLabs API to convert text files into speech. It reads text from files within a specified directory, sends the text to the ElevenLabs API, and receives audio files in return. The script then concatenates these audio files into a single MP3 file.

## Features

- Reads text files from a given directory.
- Converts text to speech using the ElevenLabs API with customizable voice settings.
- Concatenates individual speech audio files into one final audio file.
- Tracks and reports the number of credits used based on the amount of text processed.

## Requirements

- An API key from ElevenLabs stored in an environment variable.
- The `pydub` library for audio file manipulation.
- Internet access to reach the ElevenLabs API endpoint.

## Usage

1. Store your ElevenLabs API key in an environment variable named `ELEVEN_API_KEY`.
2. Place your text files in the `txt_files` directory.
3. Replace the `voice_id` with the voice of your choosing.
4. Run the script to convert all text files in the directory to speech and combine them into a single MP3 file named `combined.mp3`.

The script is designed to handle errors gracefully, informing the user if the API request fails or if the expected audio content is not received.