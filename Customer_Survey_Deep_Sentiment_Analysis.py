# Define pipeline

def deep_emotion_analysis_survey_notes():
    
    """
    Perform deep sentiment analysis on a collection of survey notes.

    Parameters:
    - text_data (list of str): A list of survey notes or comments to analyze for sentiment.

    Returns:
    - sentiment_scores (list of float): A list of sentiment scores corresponding to each input survey note.
      These scores typically range from -1.0 (negative sentiment) to 1.0 (positive sentiment).
    
    - sentiment_labels (list of str): A list of sentiment labels corresponding to each input survey note.
      These labels can be "positive," "negative," or "neutral," indicating the sentiment of each note.
    
    - emotion_labels (list of str): A list of emotion labels corresponding to each input survey note.
      These labels represent more fine-grained emotional states, such as "joy," "anger," "sadness," or "surprise."

    Description:
    
    This function takes a list of survey notes or comments as input and performs deep sentiment analysis
    using pre-trained deep learning models. It returns sentiment scores, sentiment labels, and emotion labels
    for each input note, providing insights into the emotional tone and sentiment expressed in the text data.

    """
    
    Customer_Survey_Notes_batch_size = 40
    
    classifier = pipeline(task="zero-shot-classification",model="facebook/bart-large-mnli",device=0)

    Customer_Survey_Notes_list = cn_data['Customer_Survey_Notes'].to_list()

    Customer_Survey_Notes_candidate_labels = ['Satisfied', 'Happy', 'Impressed', 'Relieved', 'Understanding', 'Frustrated', 'Anxious', 
                                      'Indifferent', 'Confused', 
                                      'Appreciative', 'Dissatisfied', 'Reluctant', 'Supportive', 'Collaborative', 'Hopeful']

    Customer_Survey_Notes_template_hypothesis = "The sentimente of this customer survey notes is {}."

    single_topic_prediction = classifier(Customer_Survey_Notes_list, 
                                         Customer_Survey_Notes_candidate_labels, 
                                         hypothesis_template=Customer_Survey_Notes_template_hypothesis)
    # Save the output as a dataframe
    
    single_topic_prediction = pd.DataFrame(single_topic_prediction)



    # The column for the predicted topic
    
    single_topic_prediction['predicted_topic'] = single_topic_prediction['labels'].apply(lambda x: x[0])

    # The column for the score of predi ted topic
    
    single_topic_prediction['predicted_topic_score'] = single_topic_prediction['scores'].apply(lambda x: x[0])

    # Take a look at the data



    return single_topic_prediction
