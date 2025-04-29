import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import os
from dotenv import load_dotenv

load_dotenv()

# Set your Gemini API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Prompt templates
PROMPTS = {
    "thread": (
        "You are a social media strategist tasked with creating a compelling Twitter thread. "
        "Summarize the main ideas of the video in a series of tweets that engage and inform your audience. "
        "Ensure each tweet is concise, impactful, and encourages interaction. "
        "Include relevant hashtags and mentions where appropriate.\n\nTranscript:\n{transcript}"
    ),
    "newsletter": (
        "Craft a comprehensive newsletter that includes a captivating title, a concise summary, "
        "and key takeaways from the video. The newsletter should be engaging and informative, "
        "providing value to the reader. Consider including sections such as 'Highlights', 'Insights', "
        "and 'Actionable Tips'. Ensure the tone is consistent with a professional newsletter format.\n\nTranscript:\n{transcript}"
    ),
    "tweets": (
        "Generate 3 high-impact tweets that capture the essence of the video. Each tweet should be "
        "designed to maximize engagement, using attention-grabbing language and relevant hashtags. "
        "Focus on delivering the core message succinctly while encouraging retweets and likes.\n\nTranscript:\n{transcript}"
    ),
    "article": (
        "Write a well-structured article that includes a compelling title, an engaging introduction, "
        "and clearly defined sections. The article should provide a thorough analysis of the video's content, "
        "offering insights and detailed explanations. Use subheadings to organize the content and ensure "
        "a logical flow. Conclude with a summary that reinforces the main points.\n\nTranscript:\n{transcript}"
    ),
}

# Get transcript from YouTube
def get_transcript(video_id: str) -> str:
    result = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([snippet['text'] for snippet in result])

# Generate content with Gemini
def generate_outputs(transcript: str) -> dict:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response_dict = {}

    for key, prompt in PROMPTS.items():
        full_prompt = prompt.format(transcript=transcript)
        response = model.generate_content(full_prompt)
        response_dict[key] = response.text.strip()

    return response_dict

# Main function to handle everything
def generate_from_youtube(video_id: str) -> dict:
    transcript = get_transcript(video_id)
    return generate_outputs(transcript)
