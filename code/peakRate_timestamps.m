%% RWE-EEG: Identifying peakRate time points for syllable onsets
% Author: Jessica M. Alexander, George A. Buzzell
% Last updated: 2022-05-21
% This script imports an audio file and extracts the broad amplitude envelope, then calculates the second derivative
% (the rate of change of the loudness contours) and identifies local maxima.  These local maxima represent the syllabic
% onsets as detailed in:
% Oganian, Y., & Chang, E. F. (2019). A speech envelope landmark for syllable encoding in human superior temporal gyrus. Science Advances.


% Notes
text = 'The first expedition to the South Pole was led by an explorer from the newly independent country of Norway.';
noSyll = 30;

% File Locations
main_dir = '/Users/jalexand/Downloads/readAloud-valence/';

% Read in audio file
input_audio = 'short-sample.wav'; % .wav format
[y,Fs] = audioread([main_dir filesep input_audio]); % load audio file, y=sampled data, Fs=sampling rate

% Create array containing Bark scale cut-off frequencies
bark_bands = [1, 20, 100; 2, 100, 200; 3, 200, 300; 4, 300, 400; 5, 400, 510; 6, 510, 630; ...
    7, 630, 770; 8, 770, 920; 9, 920, 1080; 10, 1080, 1270; 11, 1270, 1480; 12, 1480, 1720; ...
    13, 1720, 2000; 14, 2000, 2320; 15, 2320, 2700; 16, 2700, 3150; 17, 3150, 3700; 18, 3700, 4400; ...
    19, 4400, 5300; 20, 5300, 6400; 21, 6400, 7700; 22, 7700, 9500; 23, 9500, 12000; 24, 12000, 15500];

% Filter audio data across 24 Bark bandpass filters, half-rectify, average across bands, re-filter (low=1 Hz, high=10 Hz)
audioDat = zeros(size(y,1), size(bark_bands,1));

for band=1:size(bark_bands,1)
    a = bandpass(y, [bark_bands(band,2) bark_bands(band,3)], Fs);
        for i=1:length(a)
            if a(i) < 0
                a(i) = 0;
            end
        end
    audioDat(:,band) = a;
end

% Plot bark bands for visual check
bands = [1:24];
t = tiledlayout(8, 3, 'TileSpacing', 'Compact');
for i = bands
    nexttile
    plot(audioDat(:,i))
    hold on
    title(strcat('Band ', num2str(bands(i))))
    hold off
end

barkDat = mean(audioDat,2);

% THIS IS WHERE THINGS GO AWRY
filteredDat = bandpass(barkDat, [1 10], Fs);

% DOWNSAMPLING MADE THINGS EVEN CRAZIER - if downsample, must adjust MinSeparation accordingly
%Fs_downsampled = 1000
%downsampleDat = resample(filteredDat, 1, (Fs/Fs_downsampled);


% Take the second derivative and compute local maxima
secondDeriv = diff(downsampleDat, 2);
peakRate = islocalmax(secondDeriv, 'MinSeparation', 3000); %3000 was just a test that seemed to work

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