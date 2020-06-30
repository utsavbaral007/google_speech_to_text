from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
import io

def recognize(local_file_path):
	client = speech_v1p1beta1.SpeechClient.from_service_account_json("learngaroo.json")

	local_file_path = 'Recording.flac'

	language_code = 'en-US'

	sample_rate_hertz = 44100

	config = {
		'language_code' : language_code,
		'sample_rate_hertz' : sample_rate_hertz,
	}
	with io.open(local_file_path, 'rb') as f:
		content = f.read()

	audio = {'content' : content}

	operation = client.long_running_recognize(config, audio)

	print("Waiting for operation to complete...")
	response = operation.result()

	for result in response.results:
		alternative = result.alternatives[0]
		print(u"Transcript: {}".format(alternative.transcript))

def main():
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--local_file_path",
		type=str,
		default="Recording.flac"
	)
	args = parser.parse_args()

	recognize(args.local_file_path)

if __name__ == '__main__':
	main()