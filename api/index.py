from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

# Define your API key
API_KEY = "tpAaGvmfV1ApYUYr5ACM0quozSfweG0Y"

@app.route('/transcript', methods=['POST'])
def get_transcript():
    # Check for the Authorization header
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != f"Apikey {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    # Get video_id from the request body
    data = request.get_json()
    video_id = data.get('video_id')
    
    if not video_id:
        return jsonify({"error": "video_id is required"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcript)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
