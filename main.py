from flask import Flask, render_template,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():

    if request.method=="POST":
        tex= request.form.get("paragraph")
        sid= SentimentIntensityAnalyzer()
        score= sid.polarity_scores(tex)

        return render_template('Sentimental.html',msg=score['compound'])
    return render_template('Sentimental.html',msg="Fill the box")



if __name__=='__main__':
    app.run()