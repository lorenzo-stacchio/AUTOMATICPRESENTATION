import os 
from tts_module import generate_audio, SyntheticAudioTypes
from pydub import AudioSegment
from moviepy.editor import *
import json 
import tqdm 
from datetime import datetime, timedelta

path_slides_images = "slides/IEEEVR-2025-Slide-Template/"
speech_json_path = "data/speech.json"
vtt_path = "data/transcript.vtt"

if __name__=="__main__":
    audio_dir = "audio/"
    os.makedirs(audio_dir, exist_ok=True)
    video_clips = []
    audio_method = SyntheticAudioTypes.tts_coqui
    dict_Diapositivatext = json.load(open(speech_json_path, "r"))
    
    text_VTT = "WEBVTT + \n\n"
    actual_time = timedelta(hours=0, minutes=0, seconds=0, milliseconds=500)

    assert len(dict_Diapositivatext), print(f"Slides should have the same number as speeches in json, instead we have Json n° {len(dict_Diapositivatext)}")
    for k,v in tqdm.tqdm(dict_Diapositivatext.items(), desc = "Generating speech slides"):
        image_path = f"{path_slides_images}/{k}.PNG" 
        audio_path = f"audio/{k}"
        
        assert os.path.exists(image_path)
        audio_path = generate_audio(text=v, filename = audio_path, method = audio_method)

        # Load the audio file
        audio = AudioSegment.from_file(audio_path)
        # Get the duration in seconds
        duration_in_seconds = len(audio) / 1000
        
        print(f"Duration: {duration_in_seconds} seconds")
        
        ## CONSTRUCT VTT
        time_spent = timedelta(seconds=duration_in_seconds)

        # Sum the two timedelta objects
        total_time = actual_time + time_spent
        
        str_actual = str(actual_time)
        str_total = str(total_time)
        
        # Ensure it always has milliseconds (adds .000 if missing)
        for time_str in [str_actual,str_total]:
            if '.' not in time_str:
                time_str += '.000'
            
            
        text_VTT += f"{str_actual} --> {str_total}\n{v}\n\n"

        actual_time = total_time
        
        # print(text_VTT)
        # exit()
        ## CONSTRUCT VIDEO CLIP
        audio_clip = AudioFileClip(audio_path)
        image_clip = ImageClip(image_path).set_duration(duration_in_seconds)
        image_clip = image_clip.set_audio(audio_clip)

        # Create a list of ImageClips with each image shown for the calculated duration
        video_clips.append(image_clip)
        # break
    
    # Concatenate all the ImageClips into a single video
    video = concatenate_videoclips(video_clips, method="compose")


    # Write the result to a video file
    video.write_videofile('slides_video.mp4', fps=24)
    
    ## SAVE AND GENERATE VTT
    with open(vtt_path, "w") as f:
        f.write(text_VTT)