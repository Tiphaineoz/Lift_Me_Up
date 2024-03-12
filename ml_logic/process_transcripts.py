# This is to get transcript and process them into a motivational text

from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5Tokenizer, T5ForConditionalGeneration

example_video_id = 'tF7YLGpOoz8'

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join([dict['text'] for dict in transcript])
    return transcript_text


def summarize_transcript(video_id):
    transcript = get_transcript(video_id)
    input_prompt = f"summarize: {transcript}"
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    input_ids = tokenizer(input_prompt, return_tensors="pt")['input_ids']
    generated_output = model.generate(input_ids, max_length=300, num_beams=4, early_stopping=True)
    decoded_output = tokenizer.decode(generated_output[0], skip_special_tokens=True)
    return decoded_output
    
    