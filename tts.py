# import all the modules that we will need to use
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = 'venv/Lib/site-packages/TTS/.models.json'

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")

voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

syn = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    vocoder_checkpoint=voc_path,
    vocoder_config=voc_config_path
)

text = 'I went through Mrs Shears gate, closing it behind me. I walked onto her lawn and knelt beside the dog. I put my hand on the muzzle of the dog. It was still warm.The dog was called Wellington. It belonged to Mrs Shears who was our friend. She lived on the opposite side of the road, two houses to the left.Wellington was a poodle. Not one of the small poodles that have hairstyles but a big poodle. It had curly black fur, but when you got close you could see that the skin underneath the fur was a very pale yellow, like chicken.I stroked Wellington and wondered who had killed him, and why.'

outputs = syn.tts(text)
syn.save_wav(outputs, "audio-1.wav")