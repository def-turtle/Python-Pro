from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'
@app.route("/123")
def hello_world_123():
    return '<p>Hello, World 123!</p>'
def hello_world_456():
    return '<p>Hello, World 456!</p>'
app.route("/456")(hello_world_456)
@app.route("/example-simple/hi/<name>/<int:age>")
@app.route("/example-simple/hello/<name>")
@app.route("/example-simple/greet")
def example_simple(name="Guest", age=None): 
    if age is not None:
        return f'<p>Hello, {name}! You are {age} years old.</p>'
        
    else:
        return f'<p>Hello, {name}!</p>'
    
if __name__ == '__main__':
    app.run()