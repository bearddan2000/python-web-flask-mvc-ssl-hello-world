from flask import Flask, render_template

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

@app.route('/')
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True, ssl_context='adhoc')
