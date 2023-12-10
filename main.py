import requests
import os
from pydub import AudioSegment

# ElevenLabs API key from environment variable
api_key = os.environ['ELEVEN_API_KEY']

# Define Voice ID and Model ID
voice_id = "PLMnTJxBV1iLqZlVV9Uv"
model_id = "eleven_multilingual_v2"

# Function to convert text to speech using ElevenLabs API
def text_to_speech(text, filename, voice_id, model_id):
    # API endpoint
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    # Payload for the API request with default voice settings
    payload = {
        "model_id": model_id,
        "text": text,
        "voice_settings": {
            "similarity_boost": .75,  # Default values
            "stability": .85,
            "style": .1,
            "use_speaker_boost": False
        }
    }
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    # API request
    print(f"Sending request to synthesize text: {text[:30]}...")
    response = requests.post(url, json=payload, headers=headers)

    # Check for successful response and download file
    if response.status_code == 200:
        if response.headers.get('Content-Type') == 'audio/mpeg':
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Audio file {filename} created successfully.")
            return filename
        else:
            print("Received non-audio response. Headers:", response.headers)
            return None
    else:
        print("Error on API request:", response.status_code, response.text)
        return None

# Directory containing text files
txt_dir = 'txt_files'

# Verify if txt_dir exists
if not os.path.exists(txt_dir):
    print(f"Directory {txt_dir} does not exist. Please check the directory path.")
else:
    # Read text files and convert each section to speech
    filenames = []
    credits_used = 0
    for file in sorted(os.listdir(txt_dir)):  # Sort the file list for sequential order
        if file.endswith('.txt'):
            file_path = os.path.join(txt_dir, file)
            with open(file_path, 'r') as f:
                text = f.read()

            audio_filename = file.replace('.txt', '.mp3')
            result = text_to_speech(text, audio_filename, voice_id, model_id)
            if result:
                filenames.append(result)
                credits_used += len(text) / 1000  # Assuming 1 credit per 1000 characters

    # Concatenate audio files in sorted order
    combined = AudioSegment.empty()
    for filename in sorted(filenames):  # Ensure files are added in sorted order
        audio = AudioSegment.from_mp3(filename)
        combined += audio
        print(f"Added {filename} to the combined audio.")

# Export the final combined file
if filenames:
    combined.export("combined.mp3", format="mp3")
    print("Audio file combined.mp3 created.")
    print(f"Total credits used: {credits_used}")
else:
    print("No MP3 files were created. Please check for errors.")
