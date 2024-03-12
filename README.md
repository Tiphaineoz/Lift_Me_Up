# Welcome to Lift Me Up

![Lift Me Up Logo](https://github.com/tiphaineoz/Lift_Me_Up/'liftmeup_app/images/Logo_Lift_Me_Up.jpg' )
Bringing positivity to your fingertips

## The context

As part of a 9 weeks Bootcamp at Le Wagon Madrid we have to work on a real case project for the two last weeks. 

🤖 The ambitious project is to create a motivational bot which would provide a personalised pep talk. This pep talk would be inspired from reknowned speakers like Simon Sinek, Tonny Robbins, Oprah etc. 🎉

🌟A bot ready to uplift and inspire people whenever they need it most.

## The Data

🧮 The main database we'll use to train our model is from Hugging Face: https://huggingface.co/datasets/jkhedri/psychology-dataset?row=74

We will then use youtube-transcript-api to :
- download motivational speech from expert in the fields (the likes of Simon sinek, Oprah, Tony Robbins, Eckhart Tolle )
- leverage on experts on particular topics (ie eating disorder, anger management etc) to custommise the pep talk in a more professional/specific way. 

## The Models

-  Clustering
At first glance we wanted to leverage on pretrained ayoubkirouane/BERT-Emotions-Classifier but this model was only able to classify in 10 topics (and half of them were positive sentiments which were not useful to our case)

🛠 We've tried to do a semantic clusterring to define the optimal numnber of clusters for our database questions. We've used the AgglomerativeClustering model and the silhouette score from sklearn. That way we figured that about 40 topics was the optimal number of labels. 

- Labelling
We've tried to use Machine Learning model like LDA to cluster our database question into 40 topics but the results were sub-par. 
As a result we've decided to manually label a thousand rows of our dataset to train a RNN model.

🧠 We then use that RNN model to attach a label to each additional statement.

- Generative AI
💬 We used transformers from Hugging Face (ie "t5-small") to generate a basic answer to a user feeling.

## The back up/presentation plan

- Langchain 
we are leveraging from langchain model to customise the answer to the user. 
💬Langchain will be using relevant summaries from expert advice and copy the style of motivational speakers. 

## The Front end 

we are using streamlit to showcase our project on Demo day.

