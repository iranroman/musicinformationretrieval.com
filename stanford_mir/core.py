import errno
import os
import os.path
import urllib

def download_drum_samples(path='drum_samples'):
    """Download ten kick drum samples and ten snare drum samples.

        `path`: output directory containing the twenty drum samples

    Returns:

        `kick_filepaths`: list of kick drum filepaths

        `snare_filepaths`: list of snare drum filepaths
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print "Directory %s already exists." % path
    for drum_type in ['kick', 'snare']:
        for i in range(1, 11):
            filename = '%s_%02d.wav' % (drum_type, i)
            urllib.urlretrieve('http://audio.musicinformationretrieval.com/drum_samples/%s' % filename,
                               filename=os.path.join(path, filename))
    kick_filepaths = [os.path.join(path, 'kick_%02d.wav' % i) for i in range(1, 11)]
    snare_filepaths = [os.path.join(path, 'snare_%02d.wav' % i) for i in range(1, 11)]
    return kick_filepaths, snare_filepaths
