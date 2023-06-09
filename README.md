# YouTube Transcript Summarizer

This project aims to create a Chrome Extension that leverages a backend REST API to perform Natural Language Processing (NLP) and provide a summarized version of a YouTube transcript.

## Project Context

With the enormous number of video recordings being created and shared on the internet every day, it has become increasingly challenging to find relevant information efficiently. Videos with longer durations can be time-consuming to watch, and it can be frustrating when we cannot extract the key points or important patterns from them. Automatic summarization of video transcripts enables us to quickly identify essential information, saving time and effort by avoiding the need to go through the entire video content. This project offers an opportunity to gain hands-on experience with state-of-the-art NLP techniques for abstractive text summarization and implement an intriguing idea suitable for intermediate developers or a refreshing hobby project for professionals.

## High-Level Approach

The project follows these key steps:

1. Obtain transcripts/subtitles for a given YouTube video ID using a Python API.
2. Perform text summarization on the obtained transcripts using HuggingFace transformers or similar NLP models.
3. Build a Flask backend REST API to expose the summarization service to the client.
4. Develop a Chrome extension that utilizes the backend API to display the summarized text to the user.

## Applications

The YouTube Transcript Summarizer has various potential applications, including:

- Meetings and video-conferencing: A system that can convert voice to text and generate summaries from team meetings, making it easier to review discussions and action items.
- Patent research: A summarizer capable of extracting the most salient claims across patents, facilitating efficient analysis and comparison of intellectual property.

## Prerequisites

Before using this project, ensure you have the following:

- Python installed (version X.X.X)
- Chrome browser installed (version X.X.X)

## Installation and Usage

To use the YouTube Transcript Summarizer, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python dependencies by running `pip install -r requirements.txt`.
3. Start the Flask backend API by running `python api.py`.
4. Open the Chrome browser and navigate to `chrome://extensions`.
5. Enable Developer Mode by toggling the switch in the top-right corner.
6. Click on "Load unpacked" and select the folder where you cloned the repository.
7. The YouTube Transcript Summarizer extension should now appear in your Chrome browser toolbar.
8. Visit any YouTube video page and click on the extension icon to generate a summarized version of the transcript.

## Contribution

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request.
