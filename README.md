# Docker Flask And Locust
A docker + flask + locust demo project.

## Quick start
Prepare a Python environment and install the depedecies:

```bash
# Create a Python Environment 
python3 -m venv ~/.docker-flask-locust-env
# Activate the Environment 
source ~/.docker-flask-locust-env/bin/activate
# Change directory 
cd ~/environment/docker-flask-locust/ 
# Install dependencies
make install
```

Start the application
```bash
python app.py 
```
Start the Locust environment 
Open an new shell and activate the same Python enviromnet
```bash
source ~/.docker-flask-locust-env/bin/activate
```
Start locust
```bash
locust
```
Open your browser and visit http://localhost:8089

## Video Walkthrough
[Flask + Locust YouTube Walkthrough](https://www.youtube.com/watch?v=bUEYe6AqlXE)


![Screen Shot 2020-02-07 at 7 08 49 PM](https://user-images.githubusercontent.com/58792/74074716-65a2f580-49dd-11ea-943d-f91229a690ef.png)


![Screen Shot 2020-02-07 at 7 12 18 PM](https://user-images.githubusercontent.com/58792/74074801-c7635f80-49dd-11ea-9273-a04b587bbc05.png)


## This is one of my recipes in the upcoming book Cloud Computing for Data

### [Cloud Computing for Data Analysis Book](https://leanpub.com/cloud4data)
This book is being written "just in time", with a weekly release schedule.

![cloud4data books](https://d2sofvawe08yqg.cloudfront.net/cloud4data/hero2x?1578933644)
