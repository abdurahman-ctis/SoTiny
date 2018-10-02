from flask import Flask, render_template, request

app = Flask(__name__)

# storing shortened urls
urls = {}
def loadurls():
    with open("urls.txt") as f:
        for line in f:
            (key, val) = line.split()
            urls[key] = val

# hash function for urls
def furyoku(url):
    pass

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = request.form('url')
        if urls.get(furyoku(url)):
            print('exists')
        else:
            urls[furyoku(url)] = url
        return render_template('index.html', url = urls.get(furyoku(url)))

if __name__ == '__main__':
    loadurls()
    app.run(debug=True)