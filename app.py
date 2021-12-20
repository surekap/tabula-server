from flask import Flask, request, Response
import tabula, json

app = Flask(__name__)

@app.route('/pdf_to_lattice', methods=['GET', 'POST'])
def pdf_to_lattice():
	url = request.args.get('url')
	pages = request.args.get('pages', 'all')
	
	df = tabula.read_pdf(url, pages=pages, lattice=True)
	data = [x.to_csv() for x in df]
	csv = json.dumps(data)
	return Response(csv)

@app.route('/pdf_to_stream', methods=['GET', 'POST'])
def pdf_to_stream():
	url = request.args.get('url')
	pages = request.args.get('pages', 'all')
	
	df = tabula.read_pdf(url, pages=pages, stream=True)
	data = [x.to_csv() for x in df]
	csv = json.dumps(data)
	return Response(csv)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	who = request.args.get('name')
	return Response("Hello " + str(who))


if __name__ == "__main__":
	app.run()