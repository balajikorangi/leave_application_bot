from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
vectorizer = TfidfVectorizer(analyzer='word',lowercase=True,sublinear_tf=True)


data={
	"global_no": {
	"examples" : ["nope","no never","nah!","never","a big no","always a no","reject"]
	
  },
	"global_yes": {
	"examples" : ["yes","yaa","go ahead","yup","yeah","ya"]
	
  },
  "greet": {
	"examples" : ["hello","hey there","howdy","hello","hi","hey","hey ho"]
	
  },
  "beverage": {
	"examples" : [
	  "i would like to have coffee",
	  "i would like to have coffee with soy milk",
	  "can you please get me a coffee with almond milk",
	  "can you please get me a coffee",
	  "i need a coffee with soy milk",
	  "maybe coffee",
	  "coffee it is!!!!",
	  "i want coffee",
	  "can you please get me a coffee",
	  "i love to have coffee",
	  "i will go with coffee this time",
	  "coffee",
	  "need a coffee",
	  "need to order a cup coffee",
	  "can i get a coffee",
	  "get me a coffee",
	  "get me a coffee please",
	  "i would like to have cappuccino with soy milk",
	  "i will go with cappuccino this time",
	  "i like to go with cappuccino and soy milk",
	  "i want cappuccino with almond milk",
	  "i need a cappuccino with almond milk",
	  "can you please get me a cappuucino with soy milk",
	  "can you get me a cappuccino",
	  "nothing can beat cappuccino",
	  "i love to have cappuccino"
	  "cappuccino",
	  "can you get me a cappuccino",
	  "please get me a cappuccino",
	  "can you please get me a cappuccino",
	  "i like to have cappuccino",
	  "need to order a cappuccino",
	  "please can i have cappuccino",
	  "i like to have cappuccino",
	  "i want to have cappuccino"
	]
  },
  "update": {
	"examples": [
	   "actually go with soy milk",
	   "can you change it to coffee",
	   "can you change it to cappuccino",
	   "no i changed my mind.please go with coffee",
	   "no i changed my mind.please go with cappuccino",
	   "update it with almond milk",
	   "change it to almond milk",
	   "change it to soy milk",
	   "i want to update",
	   "can you please update my order",
	   "i want to change my order",
	   "updte with coffee",
	   "i want to update my order",
	   "i want to change it",
	   "update it with soy milk"
	]

  }
}

training_text = []
training_class = []

for label in data.keys():
	for text in data[label]["examples"]:
		training_class.append(label)
		training_text.append(text)



X_vector = vectorizer.fit_transform(training_text)

clf = PassiveAggressiveClassifier(n_iter=50)
clf.fit(X_vector,training_class)


file_Name = "classif_test.p"
fileObject = open(file_Name,'wb') 
pickle.dump(clf, fileObject)
fileObject.close()




while(1):
	out_put = []
	out_put.append(raw_input('Enter: ').lower())
	out_put_vector = vectorizer.transform(out_put)
	out_put_class = clf.predict(out_put_vector)
	print out_put_class
	print clf.decision_function(out_put_vector)
	# print clf.predict_proba(out_put_vector)








