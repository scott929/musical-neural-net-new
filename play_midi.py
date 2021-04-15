import pygame as pg


def play_music(music_file):
    clock = pg.time.Clock()
    pg.mixer.music.load(music_file)
    print("Music file {} loaded!".format(music_file))

    pg.mixer.music.play()
    # check if playback has finished
    while pg.mixer.music.get_busy():
        clock.tick(30)


music_file = "sample-output.mid"
freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 2048  # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pg.mixer.music.set_volume(0.8)
try:
    play_music(music_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pg.mixer.music.fadeout(1000)
    pg.mixer.music.stop()
    raise SystemExit
