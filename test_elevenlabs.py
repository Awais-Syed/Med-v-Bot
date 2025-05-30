from dotenv import load_dotenv
import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform

load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
print(f"API Key present: {bool(ELEVENLABS_API_KEY)}")
print(f"API Key: {ELEVENLABS_API_KEY}")

def test_elevenlabs_tts():
    input_text = "This is a test of the ElevenLabs text to speech API."
    output_filepath = "test_elevenlabs.mp3"
    
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        
        print("Generating audio...")
        audio = client.generate(
            text=input_text,
            voice="Aria",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )
        
        print("Saving audio...")
        elevenlabs.save(audio, output_filepath)
        
        print(f"Audio saved to {output_filepath}")
        
        # Try to play the audio
        os_name = platform.system()
        print(f"Operating system: {os_name}")
        
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            print("Attempting to play audio on Windows...")
            subprocess.run(['start', output_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])
        else:
            print(f"Unsupported operating system: {os_name}")
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_elevenlabs_tts() 