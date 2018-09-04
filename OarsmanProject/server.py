# server.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

	s = "abc"
	lis = ["a1", "a2", "a3"]
	dic ={"name":"john", "age":24}
	bl =True


	return render_template('index.html', s=s, lis=lis, dic=dic, bl=bl)

@app.route('/test', methods=['GET', 'POST'])
def test():
	if request.method == 'GET':
		res = request.args.get('get_value')
	elif request.method == 'POST':
		res = request.form['post_value']
	
	return res

@app.route('/search', methods=['GET', 'POST'])
def to_search():
	if request.method == 'GET':
		res = request.args.get('to_search')
	elif request.method == 'GET':
		res = request.form['to_registration']
	
	return res

if __name__=='__main__':
	app.run(debug=True)
