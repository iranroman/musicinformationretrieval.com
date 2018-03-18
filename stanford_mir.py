import errno
import librosa
import matplotlib, matplotlib.pyplot as plt
import numpy
import os
import os.path
import sklearn
import urllib.request

def init():
    plt.style.use('seaborn-muted')
    #plt.rcParams['figure.figsize'] = (14, 5)
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.bottom'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.xmargin'] = 0
    plt.rcParams['axes.ymargin'] = 0
    plt.rcParams['image.cmap'] = 'gray'
    plt.rcParams['image.interpolation'] = None


def extract_features(signal, features):
    fvs = list()
    for feature_name in features:
        if feature_name == 'zero_crossing_rate':
            fvs.append( librosa.feature.zero_crossing_rate(signal)[0, 0] )
        elif feature_name == 'spectral_centroid':
            fvs.append( librosa.feature.spectral_centroid(signal)[0, 0] )
    return fvs


def get_features(collection='drum_samples_train',
                 features=('zero_crossing_rate', 'spectral_centroid'),
                 scaler=None,
                 download=True):

    if collection == 'drum_samples_train':
        kick_filepaths, snare_filepaths = download_samples('drum_samples_train', download=download)
        kick_signals = [
            librosa.load(p)[0] for p in kick_filepaths
        ]
        snare_signals = [
            librosa.load(p)[0] for p in snare_filepaths
        ]

        kick_features = numpy.array([extract_features(x, features) for x in kick_signals])
        snare_features = numpy.array([extract_features(x, features) for x in snare_signals])
        feature_table = numpy.vstack((kick_features, snare_features))
        if scaler is None:
            scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
            scaler.fit(feature_table)
        training_features = scaler.transform(feature_table)

        kick_labels = numpy.zeros(10)
        snare_labels = numpy.ones(10)
        training_labels = numpy.concatenate((kick_labels, snare_labels))

        return training_features, training_labels, scaler

    elif collection == 'drum_samples_test':
        kick_filepaths, snare_filepaths = download_samples('drum_samples_test', download=download)
        kick_signals = [
            librosa.load(p)[0] for p in kick_filepaths
        ]
        snare_signals = [
            librosa.load(p)[0] for p in snare_filepaths
        ]

        kick_features = numpy.array([extract_features(x, features) for x in kick_signals])
        snare_features = numpy.array([extract_features(x, features) for x in snare_signals])
        feature_table = numpy.vstack((kick_features, snare_features))
        if scaler is None:
            scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
            scaler.fit(feature_table)
        test_features = scaler.transform(feature_table)

        kick_labels = numpy.zeros(30)
        snare_labels = numpy.ones(30)
        labels = numpy.concatenate((kick_labels, snare_labels))

        return test_features, labels, scaler

def download_samples(collection='drum_samples_train', download=True):
    """Download ten kick drum samples and ten snare drum samples.

        `collection`: output directory containing the twenty drum samples

    Returns:

        `kick_filepaths`: list of kick drum filepaths

        `snare_filepaths`: list of snare drum filepaths
    """
    try:
        os.makedirs(collection)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    if collection == 'drum_samples_train':
        if download:
            for drum_type in ['kick', 'snare']:
                for i in range(1, 11):
                    filename = '%s_%02d.wav' % (drum_type, i)
                    urllib.request.urlretrieve('http://audio.musicinformationretrieval.com/drum_samples/%s' % filename,
                                       filename=os.path.join(collection, filename))
        kick_filepaths = [os.path.join(collection, 'kick_%02d.wav' % i) for i in range(1, 11)]
        snare_filepaths = [os.path.join(collection, 'snare_%02d.wav' % i) for i in range(1, 11)]
        return kick_filepaths, snare_filepaths

    elif collection == 'drum_samples_test':
        if download:
            for drum_type in ['kick', 'snare']:
                for i in range(30):
                    filename = '%s_%02d.wav' % (drum_type, i)
                    urllib.request.urlretrieve('http://audio.musicinformationretrieval.com/drum_samples/test/%s' % filename,
                                       filename=os.path.join(collection, filename))
        kick_filepaths = [os.path.join(collection, 'kick_%02d.wav' % i) for i in range(30)]
        snare_filepaths = [os.path.join(collection, 'snare_%02d.wav' % i) for i in range(30)]
        return kick_filepaths, snare_filepaths

    elif collection == 'violin_samples_train':
        urllib.request.urlretrieve('http://audio.musicinformationretrieval.com/violin_samples_train/list.txt',
                           filename=os.path.join(collection, 'list.txt'))
        for line in open(os.path.join(collection, 'list.txt'), 'r'):
            filename = line.strip()
            print(filename)
            if filename.endswith('.wav'):
                urllib.request.urlretrieve('http://audio.musicinformationretrieval.com/' + filename,
                                   filename=filename)
        return [os.path.join(collection, f) for f in os.listdir(collection)]
