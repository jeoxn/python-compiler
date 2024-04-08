import hashlib
import os
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        code = request.form.get("code")
        # Generate a unique filename based on the code content
        filename = hashlib.sha256(code.encode()).hexdigest() + ".py"
        filepath = os.path.join("codes", filename)
        
        # Check if the file already exists
        if not os.path.exists(filepath):
            # Write the code to the generated file
            with open(filepath, "w") as f:
                f.write(code)
        else:
            # If the file already exists, execute it and return the output
            output = subprocess.run(["python", filepath], capture_output=True, text=True)
            return render_template("index.html", output=output.stdout, code=code)
            
        # Execute exec.py
        output = subprocess.run(["python", "exec.py", filepath], capture_output=True, text=True)
        return render_template("index.html", output=output.stdout, code=code)
            
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
