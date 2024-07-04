from flask import Flask, render_template_string
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
import io
import base64
import random
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hi, the time is {current_time}"

@app.route('/graph')
def graph():
    # Generate random data
    times = [datetime.now() + timedelta(seconds=i) for i in range(10)]
    values = [random.randint(0, 100) for _ in range(10)]

    # Create a plot
    plt.figure()
    plt.plot(times, values)
    plt.title("Dynamic Line Chart")
    plt.xlabel("Time")
    plt.ylabel("Value")

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.getvalue()).decode()

    # Render the image in the HTML template
    html = f"""
    <h1>Dynamic Line Chart</h1>
    <img src="data:image/png;base64,{img}" />
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
