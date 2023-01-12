# Article Category Classifier

This notebook can be used to create a classification model for classifying whether a sentence is the Aim (AIMX), Own (OWNX), Contrast (CONT), Basis (BASIS), or Misc (MISC). There are two approaches for this project, a classic approach using TF-IDF which uses a LightGBM classification model and a more modern approach using BERT. Because of the short time, no hyperparameter tuning or experiments using various models is done.

## Model Training

The first approach is the [TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) as the vectorizer of each sentences, and a [LightGBM](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html) for the classification of the sentence vector. Before the sentences are vectorized, a data cleaning is used by lowering, removing punctuations, stripping, tokenizing, removing stopwords, and lemmatization using the help of [NLTK](https://www.nltk.org/) library. [Chi-squared test](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html) is used to reduce the dimension of our matrix by selecting important features (words). Each word will be tested to each category and using the p-value limit of 0.95, a reduction of features from __ to __ is done (idea by [Mauro Di Pietro](https://towardsdatascience.com/text-classification-with-nlp-tf-idf-vs-word2vec-vs-bert-41ff868d1794)). Then, each sentences are vectorized using TF-IDF vectorizer. Then, a LightGBM is trained using a 80:10:10 split using the default parameters. 

The second approach uses a pre-trained BERT model ([bert-base-cased](https://huggingface.co/bert-base-cased)) and a simple classification layer using Dropout and Single Linear layer. A dropout value of 0.5 is used to avoid overfitting. The loss function used is Cross Entropy Loss with Adam Optimizer using 5e-6 learning rate and batch size of 32 using 10 epochs. Each training epoch takes about 48 seconds on a free google colab session using the GPU.

The third approach is almost the same as the second approach, but to overcome the imbalanced dataset problem, I used a class weighting.

## Model Performance

The first model achieves 0.70 accuracy, with 0.66 weighed average F1-Score with 3 categories has very bad classification (<0.4 F1-Score). 

![Classification Report First Method](readme/m1_res.png?raw=true)

The second method improves significantly based on the accuracy, with 0.83 accuracy but has very bad performance on the OWNX category.

![Classification Report Second Method](readme/m2_res.png?raw=true)
![Loss Second Method](readme/loss1.png?raw=true)
![Acc Report Second Method](readme/acc1.png?raw=true)

The third method can increase the F1-score of the BASE category (previously has 0.00 F1-Score) to __. This shows that the class weighting can overcome the imbalanced dataset problem.

![Classification Report Third Method](readme/m3_res.png?raw=true)
![Loss Second Method](readme/loss2.png?raw=true)
![Acc Report Second Method](readme/acc2.png?raw=true) 

## How to train yourself

Create a directory called `./dataset/` with the .txt files in the folder, and run the notebook.

## Suggestions

Try to plot the ROC Curves of each model to know more about the performance of the model. Also try another model and preprocessing methods. 