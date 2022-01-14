from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def three_blue_boxes():
    return render_template("index.html", num=3, color="dodgerblue")

@app.route('/play/<int:num>')
def number_of_boxes(num):
    return render_template("index.html", num=num, color="royalblue")

@app.route('/play/<int:num>/<color>')
def color_of_boxes(num, color):
    return render_template("index.html", num=num, color=color)



if __name__=="__main__":
    app.run(debug=True)
