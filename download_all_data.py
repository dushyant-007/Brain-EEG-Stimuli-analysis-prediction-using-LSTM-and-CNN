'''

IF THE CODE DOES NOT RUN , DO THIS - 

1. Download the dataset.
location of the emotions.csv file on my google drive. 
https://drive.google.com/file/d/19UcPRIWuBisoh2Od0zokkonsJcc5tWos/view?usp=sharing

location of the brain_EEG_MNist dataset on my drive - edited data to just keep the important part. 
File name - MindBigDataVisualMnist2021-Muse2v0.16Cut2.csv
https://drive.google.com/file/d/1OTJ9He31XIYaHjPF1EO7cCNVmxTGG5TD/view?usp=sharing

2. Save the dataset in the right location as follows
Data/emotions.csv
Data/MindBigDataVisualMnist2021-Muse2v0.16Cut2.csv

3. You are good to start the work on the files. 
'''

!wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=19UcPRIWuBisoh2Od0zokkonsJcc5tWos' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=19UcPRIWuBisoh2Od0zokkonsJcc5tWos" -O Data/'emotions.csv' && rm -rf /tmp/cookies.txt

!wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1OTJ9He31XIYaHjPF1EO7cCNVmxTGG5TD' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1OTJ9He31XIYaHjPF1EO7cCNVmxTGG5TD" -O Data/'MindBigDataVisualMnist2021-Muse2v0.16Cut2.csv' && rm -rf /tmp/cookies.txt

