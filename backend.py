from flask import Flask, request, render_template,jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def input_form():
    return render_template('input.html')

#@app.route('/', methods=['POST'])
#def text_input():
    #text = request.form['text']
    #return text

@app.route("/", methods=['POST'])
def sentiment_analysis():
	sentence=request.form['text']
	polarity = TextBlob(sentence).sentences[0].polarity
	return jsonify(
        sentence=sentence,
        polarity=polarity
    )

app.run(debug=True ,host="0.0.0.0", port=8080)
