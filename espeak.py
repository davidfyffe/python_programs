import subprocess

def say(words):
	#speaks words via espeak text to speech engine.
	devnull = open("/dev/null", "w")

	subprocess.call([
		"espeak",
		"-v", "en-rp+f4", # english received pronunciation
		 words],
		stderr=devnull)
