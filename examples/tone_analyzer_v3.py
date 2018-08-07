from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput

tone_analyzer = ToneAnalyzerV3(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/tone-analyzer/api',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2017-09-26')

## If service instance provides API key authentication
# tone_analyzer = ToneAnalyzerV3(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/tone-analyzer/api',
#     version='2017-09-26',
#     iam_api_key='your_api_key')

print("\ntone_chat() example 1:\n")
utterances = [{'text': 'I am very happy.', 'user': 'glenn'},
              {'text': 'It is a good day.', 'user': 'glenn'}]
print(json.dumps(tone_analyzer.tone_chat(utterances), indent=2))

print("\ntone() example 1:\n")
print(json.dumps(tone_analyzer.tone(tone_input='I am very happy. It is a good day.',
                                    content_type="text/plain"), indent=2))

print("\ntone() example 2:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = tone_analyzer.tone(json.load(tone_json)['text'], "text/plain")
print(json.dumps(tone, indent=2))

print("\ntone() example 3:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = tone_analyzer.tone(tone_input=json.load(tone_json)['text'],
                              content_type='text/plain', sentences=True)
print(json.dumps(tone, indent=2))

print("\ntone() example 4:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = tone_analyzer.tone(tone_input=json.load(tone_json),
                              content_type='application/json')
print(json.dumps(tone, indent=2))

print("\ntone() example 5:\n")
with open(join(dirname(__file__),
               '../resources/tone-example-html.json')) as tone_html:
    tone = tone_analyzer.tone(json.load(tone_html)['text'],
                              content_type='text/html')
print(json.dumps(tone, indent=2))

print("\ntone() example 6 with GDPR support:\n")
tone_analyzer.set_detailed_response(True)
with open(join(dirname(__file__),
               '../resources/tone-example-html.json')) as tone_html:
    tone = tone_analyzer.tone(json.load(tone_html)['text'],
                              content_type='text/html',
                              headers={'Custom-Header': 'custom_value'})

print(tone)
print(tone.get_headers())
print(tone.get_result())
tone_analyzer.set_detailed_response(False)

print("\ntone() example 7:\n")
tone_input = ToneInput('I am very happy. It is a good day.')
tone = tone_analyzer.tone(
    tone_input=tone_input,
    content_type="application/json")
print(json.dumps(tone, indent=2))
