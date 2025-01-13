import asyncio
import datetime

from flask import Flask, render_template, request
from shared import DEMO_OPTIONS, WorkflowInput
from temporalio.client import Client
from workflow import GetAddressFromIP

app = Flask(__name__)


async def connect_temporal(app):
    client = await Client.connect("localhost:7233")
    app.temporal_client = client


@app.route("/")
async def index():
    return render_template("index.html")


@app.route("/demo-options")
async def demo_options():
    return DEMO_OPTIONS


@app.route("/greet", methods=["POST"])
async def greet():
    name = request.form.get("name")
    seconds = request.form.get("sleep_duration")

    if seconds is None or seconds == "":
        input = WorkflowInput(name=name)
    else:
        input = WorkflowInput(name=name, seconds=int(seconds))

    # Create a pseudo id for our Workflow using current time
    timestamp = datetime.datetime.now().strftime("%H%M")

    # Execute a workflow
    result = await app.temporal_client.execute_workflow(
        GetAddressFromIP.run,
        input,
        id=f"greeting-workflow-{timestamp}",
        task_queue="greeting-tasks",
    )

    greeting = f"Hello, {name}!<br> Your IP Address is <code>{result.ip_addr}</code>.<br> You are in {result.location}"
    return greeting


if __name__ == "__main__":
    # Create Temporal connection.
    asyncio.run(connect_temporal(app))

    app.run(debug=True, port=8000)
