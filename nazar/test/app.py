from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>Hello, World!!</h1>
    <i>italic stuff</i>
    <button id="btn">Click</button>
    <script>
        document.getElementById('btn').addEventListener('click', function() {
            alert('clicked');
        })
    </script>
    """\
    
@app.route("/<name>")
def helloName(name):
    return f"Hello, {name}!!"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
