import mido, os


def string_to_midi(s, time_multiplier=140, velocity=70):
    mid = mido.MidiFile()
    mid.tracks.append(mido.midifiles.tracks.MidiTrack())  # create type 0 midi file
    t = 0
    for i in s.split():
        message_type = 'note_on'
        if i.startswith('wait'):
            t += int(i.lstrip('wait')) * time_multiplier
            continue
        # process note
        if i.startswith('end'):
            i = i.replace('end', '')
            message_type = 'note_off'
        instrument = i[0]
        note = int(''.join(i[1:])) + (3 * 12)  # bump the note up a few octaves
        # add the event to the midi file track
        mid.tracks[0].append(mido.Message(message_type, note=note, velocity=velocity, time=t))
        t = 0
    return mid


with open('result/sample.txt') as f:
    input = f.read()
    mid = string_to_midi(input)
    mid.save('sample-output.mid')
    # os.system('open {}'.format('sample-output.mid'))
