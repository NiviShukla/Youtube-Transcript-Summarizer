from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline, PegasusForConditionalGeneration, PegasusTokenizer

app = Flask(__name__)

def jls_extract_def():
    return get_transcript

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    summary = get_summary(jls_extract_def()(video_id))
    return summary, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript):
    model_name = 'google/pegasus-large'
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)
    summary = summarizer(transcript, max_length=300, min_length=50, do_sample=False)[0]['summary_text']
    return summary
    
if __name__ == '__main__':
    app.run()