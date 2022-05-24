%% RWE-EEG: Identifying peakRate time points for syllable onsets
% Author: Jessica M. Alexander, George A. Buzzell
% Last updated: 2022-05-24
% This script imports an audio file and extracts the broad amplitude envelope, then calculates the second derivative
% (the rate of change of the loudness contours) and identifies local maxima.  These local maxima represent the syllabic
% onsets as detailed in:
% Oganian, Y., & Chang, E. F. (2019). A speech envelope landmark for syllable encoding in human superior temporal gyrus. Science Advances.

% File Locations
main_dir = '/Users/jalexand/Downloads/rwe-eeg-pilot';

% Read in audio file
input_audio = 'sub-210001_rwe_darwin_s1_r1_e1_2-on-several.wav'; % .wav format
[stereo,Fs] = audioread([main_dir filesep input_audio]); % load audio file, y=sampled data, Fs=sampling rate
y = stereo(:,1);
pulse = stereo(:,2);

% Pad audio file
pad = zeros((Fs*10)',1);
y_padded = [pad; y; pad];

% Create array containing Bark scale cut-off frequencies
bark_bands = [1, 20, 100; 2, 100, 200; 3, 200, 300; 4, 300, 400; 5, 400, 510; 6, 510, 630; ...
    7, 630, 770; 8, 770, 920; 9, 920, 1080; 10, 1080, 1270; 11, 1270, 1480; 12, 1480, 1720; ...
    13, 1720, 2000; 14, 2000, 2320; 15, 2320, 2700; 16, 2700, 3150; 17, 3150, 3700; 18, 3700, 4400; ...
    19, 4400, 5300; 20, 5300, 6400; 21, 6400, 7700; 22, 7700, 9500; 23, 9500, 12000; 24, 12000, 15500];

% Filter audio data across 24 Bark bandpass filters, square-rectify, average across bands, re-filter (low=1 Hz, high=10 Hz) to smooth the waveform
audioDat = zeros(size(y_padded,1), 21);

for band=1:21
    a = bandpass(y_padded, [bark_bands(band,2) bark_bands(band,3)], Fs);
    audioDat(:,band) = a.^2;
end

barkDat = mean(audioDat,2);
%barkDat = downsample(barkDat, 100);

filteredDat = bandpass(barkDat, [1 10], Fs);

% Remove padding
smoothDat = filteredDat((size(pad,1)+1):(length(filteredDat)-size(pad,1)),:);

% Take the second derivative and compute local maxima based on a faster 10 Hz speaking rate
secondDeriv = diff(smoothDat, 2);
peakRate = islocalmax(secondDeriv, 'MinSeparation', 4410);

% Add time points
samplePoints = 2:1:(length(y)-1);
peakRateSamplePts = [peakRate, samplePoints']

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Another method using envelope() function, seemed similar but less transparency in method
[yupper, ylower] = envelope(y);
upperEnv = yupper;
secondDeriv2 = diff(upperEnv, 2);
peakRate2 = islocalmax(secondDeriv2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Another method using audioFeatureExtractor, but still troubleshooting
% https://www.mathworks.com/help/audio/ref/audiofeatureextractor.html
aFE = audioFeatureExtractor( ...
    SampleRate=Fs, ...
    barkSpectrum=true);

setExtractorParameters(aFE,"barkSpectrum",NumBands=24);

bark = extract(aFE, y);