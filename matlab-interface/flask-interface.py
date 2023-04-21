from flask import Flask, request, Response

import os
import time
import logging

import matlab.engine

ALLOWED_EXTENSIONS = {"xlsx", "xls"}
FILE_HOLDING = os.path.expanduser("~/tmp/")
MATLAB_FUNCTION_PATH = os.path.expanduser("~/gwu-src/predictmod-project/PredictMod/predictmod/")

class MatlabRunner:
    def __init__(self, path):
        eng = matlab.engine.start_matlab()
        eng.cd(MATLAB_FUNCTION_PATH, nargout=0)
        # eng.load("Synth_data_trained_net.mat")
        eng.addpath(MATLAB_FUNCTION_PATH)
        eng.cd(path, nargout=0)
        # self.nets = [eng.workspace['net1'], eng.workspace['net2'], eng.workspace['net3']]
        self.engine = eng

    def make_prediction(self, filename):
        return self.engine.single_predict(filename)

runner = MatlabRunner(FILE_HOLDING)        

def allowed_filename(filename):
    return filename.split(".")[-1] in ALLOWED_EXTENSIONS

def restarting_the_engine_is_slow(path, file_name):

        eng = matlab.engine.start_matlab()
        eng.cd(MATLAB_FUNCTION_PATH, nargout=0)
        # eng.load("Synth_data_trained_net.mat")
        eng.addpath(MATLAB_FUNCTION_PATH)
        eng.cd(path, nargout=0)
        # nets = [eng.workspace['net1'], eng.workspace['net2'], eng.workspace['net3']]
        return eng.single_predict(file_name)

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


@app.route("/", methods=["POST"])
def request_received():
    try:
        if "files" not in request.files:
            keys_list = ",".join([fk for fk in request.files.keys()])
            return Response(
                f"<b>No file received!</b><br>Files was {keys_list}", status=400
            )
        file = request.files["files"]
        if not file.filename or not allowed_filename(file.filename):
            return Response(f"<b>Illegal filename {file.filename}!</b>")
        file.save(os.path.join(FILE_HOLDING, file.filename))

        obj_start = time.time()
        prediction = runner.make_prediction(file.filename)
        obj_elapsed = f"{time.time() - obj_start:.2f}s"
        obj_pred = f"{prediction} - {obj_elapsed}"
        func_start = time.time()
        # prediction = restarting_the_engine_is_slow(FILE_HOLDING, file.filename)
        func_elapsed = f"{time.time() - func_start:.2f}s"
        func_pred = f"{prediction} - {func_elapsed}"
        
        # app.logger.debug("-" * 80)
        # app.logger.debug(f"---> Runner output: {prediction}")
        # app.logger.debug("-" * 80)
        outstr = f"""
<b>Received response:</b>
<br>
Object-oriented result:
    {obj_pred}
<br>
Function-based result:
    {func_pred}
"""
        return Response(outstr)

    except Exception as e:
        return Response(f"Got an error!\n\t{e}")
