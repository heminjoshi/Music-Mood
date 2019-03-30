import requests
import json
from watson_developer_cloud import ToneAnalyzerV3

class ToneAnalyzer(object) :
    def __init__(self, key = "my_key") :
        self.key = key;

    def analyze(self, track) :
        tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            iam_apikey=self.key,
            url='https://gateway.watsonplatform.net/tone-analyzer/api'
        )
        tone_analysis = tone_analyzer.tone( {'text': track.lyrics}, 'application/json').get_result()
        
        return [k['tone_name'] for k in tone_analysis["document_tone"]["tones"]];


