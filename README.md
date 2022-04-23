musicinformationretrieval.com
=============================


Introduction
------------

1.  [About This Site](https://colab.research.google.com/github/stevetjoa/musicinformationretrieval.com/blob/gh-pages/about.ipynb) (Start here!)
2.  [About the book <em>Fundamentals of Music Processing</em>](https://musicinformationretrieval.com/about_fmp.html)
3.  [About the CCRMA Workshop on Music Information Retrieval](about_ccrma_workshop.ipynb)
4.  [What is MIR?](why_mir.ipynb)
5.  [Python Basics and Dependencies](python_basics.ipynb)
6.  [Jupyter Basics](get_good_at_ipython.ipynb)
7.  [Jupyter Audio Basics](ipython_audio.ipynb)
8.  [SoX and ffmpeg](sox_and_ffmpeg.ipynb)
9.  [NumPy and SciPy Basics](numpy_basics.ipynb)


Music Representations
---------------------

1.  [Sheet Music Representations](sheet_music_representations.ipynb)
2.  [Symbolic Representations](symbolic_representations.ipynb)
3.  [Audio Representation](audio_representation.ipynb)
4.  [Tuning Systems](tuning_systems.ipynb)
5.  [MIDI Note to Frequency Conversion Table](midi_conversion_table.ipynb)
6.  [Understanding Audio Features through Sonification](feature_sonification.ipynb)


Signal Analysis and Feature Extraction
--------------------------------------

1.  [Basic Feature Extraction](basic_feature_extraction.ipynb)
2.  [Segmentation](segmentation.ipynb)
3.  [Energy and RMSE](energy.ipynb)
4.  [Zero Crossing Rate](zcr.ipynb)
5.  [Fourier Transform](fourier_transform.ipynb)
6.  [Short-time Fourier Transform and Spectrogram](stft.ipynb)
7.  [Constant-Q Transform and Chroma](chroma.ipynb)
8.  [Video: Chroma Features](video_chroma.ipynb)
9.  [Magnitude Scaling](magnitude_scaling.ipynb)
10. [Spectral Features](spectral_features.ipynb)
11. [Autocorrelation](autocorrelation.ipynb)
12. [Pitch Transcription Exercise](pitch_transcription_exercise.ipynb)


Rhythm, Tempo, and Beat Tracking
--------------------------------

1. [Novelty Functions](novelty_functions.ipynb)
2. [Peak Picking](peak_picking.ipynb)
3. [Onset Detection](onset_detection.ipynb)
4. [Onset-based Segmentation with Backtracking](onset_segmentation.ipynb)
5. [Tempo Estimation](tempo_estimation.ipynb)
6. [Beat Tracking](beat_tracking.ipynb)
7. [Video: Tempo and Beat Tracking](video_tempo_beat_tracking.ipynb)
8. [Drum Transcription using ADTLib](adtlib.ipynb)


Machine Learning
----------------

1. [K-Means Clustering](kmeans.ipynb)
2. [Exercise: Unsupervised Instrument Classification using K-Means](kmeans_instrument_classification.ipynb)
3. [Neural Networks](neural_networks.ipynb)
4. [Genre Recognition](genre_recognition.ipynb)
5. [Exercise: Genre Recognition](exercise_genre_recognition.ipynb)


Evaluation
----------

1. [Introduction to <code>mir_eval</code>](intro_mir_eval.ipynb)
2. [Onset Detection](evaluation_onset.ipynb)
3. [Beat Tracking](evaluation_beat.ipynb)
4. [Chord Estimation](evaluation_chord.ipynb)


Music Synchronization
---------------------

1. [Dynamic Programming](dp.ipynb)
2. [Longest Common Subsequence](lcs.ipynb)
3. [Dynamic Time Warping](dtw.ipynb)
4. [Dynamic Time Warping Example](dtw_example.ipynb)


Music Structure Analysis
------------------------

1. [Mel-Frequency Cepstral Coefficients](mfcc.ipynb)


Content-Based Audio Retrieval
-----------------------------

1. [Locality Sensitive Hashing](lsh_fingerprinting.ipynb)


Musically Informed Audio Decomposition
--------------------------------------

1. [Principal Component Analysis](pca.ipynb)
2. [Nonnegative Matrix Factorization](nmf.ipynb)
3. [NMF Audio Mosaicing](nmf_audio_mosaic.ipynb)
4. [Harmonic-Percussive Source Separation](hpss.ipynb)


Just For Fun
------------

1. [Real-time Spectrogram](realtime_spectrogram.ipynb)
2. [THX Logo Theme](thx_logo_theme.ipynb)


---

This repository contains instructional Jupyter notebooks related to music information retrieval (MIR). Inside these notebooks are Python code snippets that illustrate basic MIR systems.

The simplest way to use this repository is to (1) browse a read-only version of this repo at [musicinformationretrieval.com](https://musicinformationretrieval.com), and (2) follow along using a blank Jupyter notebook of your own.


Updates
-------

2022 April 22: It's 2022, and Colab seems to be much more popular and usable than it was a few years ago. Therefore, I'm going to try migrating some notebooks to Colab. In the process, I will probably delete some of the static HTML files, since the roundabout process of editing a IPYNB and converting it to static HTML is unnecessary and annoying.

2021 June 2: I'm sorry that I haven't updated this repository lately. My career focus has drifted away from MIR, sadly. Therefore, please understand that I might not be checking this repo very frequently. However, I'm grateful that many of you still find this repo helpful. I encourage you to raise GitHub issues and participate in community discussions through the issue forums. If you want to submit a pull request, you can email steve at musicinformationretrieval dot com to let me know to check GitHub. 


Installation
------------

1.  Download and install [Anaconda for Python 3.x](https://www.anaconda.com/download).
    
2.  Install [librosa](https://librosa.github.io/librosa/install.html) and [ffmpeg](https://librosa.github.io/librosa/install.html#ffmpeg):

        conda install -c conda-forge librosa ffmpeg

    To upgrade:

        conda upgrade -c conda-forge librosa ffmpeg

[2018 June 24] These notebooks reflect the following package versions:

-   ipython 6.2.1
-   joblib 0.11
-   jupyter 1.0.0
-   librosa 0.6.1
-   matplotlib 2.2.0
-   numpy 1.14.2
-   pandas 0.22.0
-   scikit-learn 0.19.1
-   scipy 1.0.0

Usage
-----

1.  Start the [Jupyter notebook](https://jupyter.org/) server on your local machine. For Mac users, at the Terminal:

        your-local-machine:~$ jupyter notebook

    For Windows users, open the application "Jupyter Notebook". Alternatively for Windows: open the application "Anaconda Prompt" and type in `jupyter notebook`.

    Jupyter should automatically open a new window in your web browser that resembles a directory tree.

2.  To open a new notebook, in the new window of your web browser, click on *New* near the top right to open a new notebook.

    -   To rename the notebook, click on "Untitled" in the top left, and choose a different name.
    -   Inside a cell, run `1+2`. Press `<Shift-Enter>` on a cell to run that cell. Hopefully you get the output `3`.
    -   Inside a cell, run `import scipy, sklearn, pandas, librosa`. Press `<Shift-Enter>` to run the cell. If that runs without error, congratulations, you have the necessary libraries installed properly.
    -   Try executing the content from <https://musicinformationretrieval.com> inside this blank notebook.

3.  To close the Jupyter notebook,

    -   Save the notebook. (Either use keyboard shortcut `s`, or "File | Save" in the top menu.)
    -   Close the browser window.
    -   If you opened the notebook from a prompt/shell as indicated in Step 1 above, from that shell, press `<Ctrl-C>` twice to return to the prompt.

Congratulations, you are now running a Jupyter notebook, and you can get started with the notebooks in this repository.

After installing, if something doesn’t work, try closing the terminal or restarting the OS. Sometimes that can reset the necessary configurations.


Troubleshooting
---------------

[Issue #729](https://github.com/librosa/librosa/issues/729): `import librosa` causes `TypeError: expected string or buffer` 

-   Workaround: downgrade `joblib` to v0.11:

        pip install joblib==0.11


Contributions
-------------

Your contributions are welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/musicinformationretrieval.com/issues)" in the right navigation bar, then "New Issue".  Issues can include Python bugs, spelling mistakes, broken links, requests for new content, and more.

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).

This repo is statically hosted using [GitHub Pages](https://pages.github.com/). Any changes to HTML files in the `gh-pages` branch will be seen on [musicinformationretrieval.com](https://musicinformationretrieval.com).

To edit musicinformationretrieval.com:

1.  Edit a notebook, e.g.:

        $ jupyter notebook kmeans.ipynb

2.  Convert notebook to HTML:

        $ jupyter nbconvert kmeans.ipynb

3.  Commit the notebook and the HTML:

        $ git add kmeans.ipynb kmeans.html
        $ git commit
        $ git push

    You may need to wait 1-2 minutes before the changes are live on GitHub Pages.

