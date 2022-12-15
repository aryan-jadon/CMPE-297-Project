# Project - Summarized Video Transcript Classification using Few Shot Learning and Zero Shot Learning

### Team Members
1. ARYAN JADON ( 015260609 ) 
2. HARIKA NALAM ( 015939963 ) 
3. SHREYA NIMBHORKAR ( 015226315 ) 
4. SWATHI ANANDRAM ( 015923804)


### Project Abstract
On the Internet, a massive volume of video recordings
is made and shared daily. It has become very challenging
in today’s daily life to watch videos that may last longer than
anticipated. Sometimes our efforts may be in vain if we cannot
discern helpful information from them. Automatically creating
summaries of these videos material enables us to rapidly scan
for critical themes and saves us time and effort from having to
watch the entire thing again. Our system aims to provide the
user to upload a video and get the transcription of the video,
which converts speech to text and classifies the video as per the
categories. It is helpful to determine the tags of the videos that are
being uploaded. The work of classifying videos has become very
successful recently. Remarkably, the subject has drawn increased
interest since deep learning models became an effective tool for
identifying videos.

### Project Flow Diagram

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Diagram.png)

### MLOps Project Flow Diagram

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/MLOpsWorkflow.png)


### Project Files

#### MLOps Slides Link - https://drive.google.com/drive/folders/1L5IyrtueociFmLNkt7dkEuph3GdNj33g?usp=share_link

#### Presentation Slides Link - https://drive.google.com/drive/folders/1BiF2mIcIeJoaQq29q3e0iXnS3LK1NCu3?usp=share_link

#### Dataset Link - https://drive.google.com/drive/folders/1jG7f-U7QlH0Tf0Es9fp0AMcyZ1I5Mzmh?usp=share_link

#### Project Report Link - https://drive.google.com/drive/folders/10s2rOf6i0t2ET28-Rap1JhtPgbtrPHlZ?usp=share_link

#### Project Demo Video Link - https://drive.google.com/drive/folders/1n1RgTIgcNA765vJOndch1i73v7ViAvwh?usp=share_link


## Team Members Responsibility
1. Aryan Jadon
2. Swathi Anandram
3. Shreya Nimbhorkar
4. Harika Nalam


## Project Screenshots

### StreamLit App

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/streamlit-run-1.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Streamlit-1.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Streamlit-2.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Streamlit-3.png)

### Project API's

#### Transcription API

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Transcription-API.png)

#### Summarizer API

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/XLNET-Summarizer-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Zero-Short-Summarizer-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/GPT-Summarizer-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/BERT-Summarizer-API.png)


#### Classification API

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Classification-API.png)



### Steps To Run Project

1. create conda environment using command 
```bash
conda create -n myenv python=3.9
```

2. install project dependencies 
```bash
pip install -r complete_requirements.txt
```

3. run video_transcription_api form it's parent folder
```bash
python manage.py runserver 8001
```

4. run video_transcript_classification_api form it's parent folder
```bash
python manage.py runserver 8002
```

5. run summarizer_api form it's parent folder
```bash
python manage.py runserver 8000
```

6. run Streamlit App form it's parent folder
```bash
streamlit run project_app.py
```
