from flask import Flask, request, Response
import tabula, json

app = Flask(__name__)

@app.route('/pdf_to_lattice', methods=['GET', 'POST'])
def pdf_to_lattice():
	url = request.args.get('url')
	pages = request.args.get('pages', 'all')
	stream = bool(request.args.get('stream', True))
	lattice = bool(request.args.get('lattice', False))
	
	stream = False if lattice else True
	
	df = tabula.read_pdf(url, pages=pages, stream=stream, lattice=lattice)
	data = [x.to_csv() for x in df]
	csv = json.dumps(data)
	return Response(csv)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	who = request.args.get('name')
	return Response("Hello " + who)


if __name__ == "__main__":
	app.run()