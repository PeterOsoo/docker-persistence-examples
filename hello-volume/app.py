from flask import Flask
import os

app = Flask(__name__)
counter_file = "/data/visits.txt"

@app.route('/')
def hello():
    # read the current count
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            count = int(f.read().strip())
    else:
        count = 0

    # increment
    count += 1

    # save back
    with open(counter_file, "w") as f:
        f.write(str(count))

    return f"Hello — you are visitor #{count}!\nThe visit count is stored in persistent storage."
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
