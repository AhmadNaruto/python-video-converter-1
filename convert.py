from converter import Converter
conv = Converter()

info = conv.probe('monfichier.ogv')

convert = conv.convert('monfichier.ogv', 'monfichier.mp4', {
    'format': 'mp4',
    'audio': {
        'codec': 'aac',
        'samplerate': 11025,
        'channels': 2
    },
    'video': {
        'codec': 'h264',
        'width': 720,
        'fps': 25
    }})

for timecode in convert:
    print(f'\rConverting ({timecode:.2f}) ...')
