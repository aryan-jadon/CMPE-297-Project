# Summarized Video Transcript Classification using Zero Shot Learning

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Diagram.png)

### Team Members
1. ARYAN JADON ( 015260609 ) 
2. HARIKA NALAM ( 015939963 ) 
3. SHREYA NIMBHORKAR ( 015226315 ) 
4. SWATHI ANANDRAM ( 015923804)


### Project Files

#### Dataset Link - https://drive.google.com/drive/folders/1jG7f-U7QlH0Tf0Es9fp0AMcyZ1I5Mzmh?usp=sharing

#### Slides Link - https://drive.google.com/drive/folders/1BiF2mIcIeJoaQq29q3e0iXnS3LK1NCu3?usp=sharing

#### Project Demo Video Link - https://drive.google.com/drive/folders/1n1RgTIgcNA765vJOndch1i73v7ViAvwh?usp=sharing


## Project Screenshots

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Streamlit-1.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Streamlit-2.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Streamlit-3.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Diagram.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Transcription-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/XLNET-Summarizer-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Zero-Short-Summarizer-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/GPT-Summarizer-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/BERT-Summarizer-API.png)

![Diagram](https://github.com/aryan-jadon/CMPE-297-Project/blob/main/screenshots/Classification-API.png)

### How To Run
1. create conda environment using command 
```bash
conda create -n myenv python=3.9
```
2. install project dependencies 
```bash
pip install -r requirements.txt
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
streamlit run app.py
```
