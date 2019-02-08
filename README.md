# Song Recommender
**For a less-accurate (due to Heroku's size limits) deployed app, 
head to https://song-recommender.herokuapp.com/**

**Please refer to the analysis report titled 'Report_song_recommender'. 
Note that there are three formats available: Jupyter Notebook (.ipynb), 
PDF (.pdf), and HTML (.html). The .ipynb file is best since it is
nicely formatted and includes interactive cells.**

This is a personal project to analyze song playlist data to build a song 
recommender.

## Data
There is not a lot of widely available and open song/playlist data. 
Spotify's Million Song Playlist competition data is not yet available
for non-competitors. Kaggle had a very large 90+ million row set, but
it was primarily Russian and I do not have the computer resources to
translate such a large dataset (although Google's translator package
worked admirably during my brief testing).

I settled on a moderately large (~11000 playlists consisting of ~1.88 
million songs) dataset that was created in late 2010/early 2011. The raw 
data was collected by Shuo Chen from Cornell University's Department of 
Computer Science. Specifically, playlist and tag data was scraped from 
Yes.com and Last.fm, respectively; Yes.com and Last.fm thus owns the 
data.

### References
[1] Shuo Chen, Joshua L. Moore, Douglas Turnbull, Thorsten Joachims, 
Playlist Prediction via Metric Embedding, ACM Conference on Knowledge 
Discovery and Data Mining (KDD), 2012.

[2] Joshua L. Moore, Shuo Chen, Thorsten Joachims, Douglas Turnbull, 
Learning to Embed Songs and Tags for Playlists Prediction, International 
Society for Music Information Retrieval (ISMIR), 2012.

[3] Shuo Chen, Jiexun Xu, Thorsten Joachims, Multi-space Probabilistic 
Sequence Modeling, ACM Conference on Knowledge Discovery and Data Mining 
(KDD), 2013.

## Goal
The goal of this project is to create a recommender system that takes 
one song and suggests others.

## Instructions
1. Install Python3.
2. Save the following files in the same directory:
	* playlist_song_mat_train.pkl
	* song_recommender.py
3. Open the command prompt.
4. In the command prompt, navigate to the working directory where the
files from step 2 are located.
5. Type 'python song_recommender.py'
6. Follow the prompts.