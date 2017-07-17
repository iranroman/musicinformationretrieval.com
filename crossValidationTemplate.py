#
# CCRMA MIR workshop 2014 code examples and useful functions
#
# Ported to SKLearn Python by Steve Tjoa & Leigh M. Smith
#

import numpy as np
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
import urllib2  # the lib that handles the url stuff
import urllib
from essentia.standard import MonoLoader
from essentia.standard import ZeroCrossingRate, CentralMoments, Spectrum, Windowing, Centroid, DistributionShape

# Here are examples of how scaling functions would be written, however nowdays SciKit
# Learn will do it for you with the MinMaxScaler!

def scale(x):
    """
    Linearly scale data, to a range of -1 to +1.
    Return the scaled data, the gradient and offset factors.
    """
    if x.shape[0] != 1:                   # Make sure that data is matrix and not a vector
        dataMax = x.max(0)
        dataRange = dataMax - x.min(0)         # First, find out the ranges of the data
        multfactor = 2 / dataRange        # Scaling to be {-1 to +1}.  This is a range of "2" 
        newMaxval = multfactor * dataMax
        subfactor = newMaxval - 1      # Center around 0, which means subtract 1
        data = np.empty(x.shape)
        for featureIndex in range(x.shape[1]):
            data[:, featureIndex] = x[:, featureIndex] * multfactor[featureIndex] - subfactor[featureIndex]
    else:                                 # If data is a vector, just return vector and multiplication = 1, subtraction = 0
        data = x 
        multfactor = 1
        subfactor  = 0 
    return data, multfactor, subfactor

def rescale(featureVector, mf, sf):
    """
    featureVector = the unscaled feature vector
    mf = the multiplication factor used for linear scaling 
    sf = the subtraction factor used for linear scaling
    """
    featureVector_scaled = np.empty(featureVector.shape)
    for featureIndex in range(featureVector.shape[1]):
        # linear scale
        featureVector_scaled[:, featureIndex] = featureVector[:, featureIndex] * mf[featureIndex] - sf[featureIndex]
    return featureVector_scaled

def crossValidateKNN(features, labels):
    """
    This code is provided as a template for cross-validation of KNN classification.
    Pass into the variables "features", "labels" your own data. 

    As well, you can replace the code in the "BUILD" and "EVALUATE" sections
    to be useful with other types of Classifiers.
    """
    #
    # CROSS VALIDATION 
    # The features array is arranged as rows of instances, columns of features in our training set.
    numInstances, numFeatures = features.shape
    numFolds = min(10, numInstances) # how many cross-validation folds do you want - (default=10)
    # divide test set into 10 random subsets
    indices = cross_validation.KFold(numInstances, n_folds = numFolds)

    errors = np.empty(numFolds)
    for foldIndex, (train_index, test_index) in enumerate(indices):
        # SEGMENT DATA INTO FOLDS
        print('Fold: %d' % foldIndex) 
        print("TRAIN: %s" % train_index)
        print("TEST: %s" % test_index)
    
        # SCALE
        scaler = preprocessing.MinMaxScaler(feature_range = (-1, 1))
        trainingFeatures = scaler.fit_transform(features.take(train_index, 0))
        # BUILD NEW MODEL - ADD YOUR MODEL BUILDING CODE HERE...
        model = KNeighborsClassifier(n_neighbors = 3)
        model.fit(trainingFeatures, labels.take(train_index, 0))
        # RESCALE TEST DATA TO TRAINING SCALE SPACE
        testingFeatures = scaler.transform(features.take(test_index, 0))
        # EVALUATE WITH TEST DATA - ADD YOUR MODEL EVALUATION CODE HERE
        model_output = model.predict(testingFeatures)
        print("KNN prediction %s" % model_output) # Debugging.
        # CONVERT labels(test,:) LABELS TO SAME FORMAT TO COMPUTE ERROR 
        labels_test = labels.take(test_index, 0)
        # COUNT ERRORS. matches is a boolean array, taking the mean does the right thing.
        matches = model_output != labels_test
        errors[foldIndex] = matches.mean()
    print('cross validation error: %f' % errors.mean())
    print('cross validation accuracy: %f' % (1.0 - errors.mean()))
    return errors


def process_corpus(corpusURL):
    """Read a list of files to process from the text file at corpusURL. Return a list of URLs""" 
    # Open and read each line
    urlListTextData = urllib2.urlopen(corpusURL) # it's a file like object and works just like a file
    for fileURL in urlListTextData: # files are iterable
        yield fileURL.rstrip()
    # return [fileURL.rstrip() for fileURL in urlListTextData]

# audioFileURLs = process_corpus("https://ccrma.stanford.edu/workshops/mir2014/SmallCorpus.txt")
# for audioFileURL in process_corpus("https://ccrma.stanford.edu/workshops/mir2014/SmallCorpus.txt"):
# print audioFileURL

def spectral_features(filelist):
    """
    Given a list of files, retrieve them, analyse the first 100mS of each file and return
    a feature table.
    """
    number_of_files = len(filelist)
    number_of_features = 5
    features = np.zeros([number_of_files, number_of_features])
    sample_rate = 44100

    for file_index, url in enumerate(filelist):
        print url
        urllib.urlretrieve(url, filename='/tmp/localfile.wav')
        audio = MonoLoader(filename = '/tmp/localfile.wav', sampleRate = sample_rate)()
        zcr = ZeroCrossingRate()
        hamming_window = Windowing(type = 'hamming') # we need to window the frame to avoid FFT artifacts.
        spectrum = Spectrum()
        central_moments = CentralMoments()
        distributionshape = DistributionShape()
        spectral_centroid = Centroid()

        frame_size = int(round(0.100 * sample_rate))   # 100ms
        # Only do the first frame for now.
        # TODO we should generate values for the entire file, probably by averaging the features.
        current_frame = audio[0 : frame_size]
        features[file_index, 0] = zcr(current_frame)
        spectral_magnitude = spectrum(hamming_window(current_frame))
        centroid = spectral_centroid(spectral_magnitude)
        spectral_moments = distributionshape(central_moments(spectral_magnitude))
        features[file_index, 1] = centroid
        features[file_index, 2:5] = spectral_moments
    return features

