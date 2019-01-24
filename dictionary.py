from flask import Flask, render_template
import random
app = Flask(__name__)




@app.route("/dictionary/<string:word>")
def dictionary(word):
    dict = {'apple':'사과','kid':'아이','cloth':'천','book':'책'}
    
    result = dict.get(word)
    if result:
        result = f"{word}는 {result}입니다."
    else:
        result = f"{word}는 단어장에 없는 단어입니다."
        
    return render_template("dictionary.html",result=result)
    
    # if word in dict.keys():
    #     mean = dict[word]
    # else:
    #     mean = "나만의 단어장에 없음"

    # return render_template("dictionary.html", word=word, mean=mean)
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)