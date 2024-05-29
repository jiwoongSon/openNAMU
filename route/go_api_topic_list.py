from .tool.func import *

def api_topic_list(name = 'Test', set_type = 'normal', num = 1):
    other_set = {}
    other_set["name"] = str(name)
    other_set["set_type"] = set_type
    other_set["num"] = str(num)
    other_set = json.dumps(other_set)

    if platform.system() == 'Linux':
        if platform.machine() in ["AMD64", "x86_64"]:
            data = subprocess.Popen([os.path.join(".", "route_go", "bin", "main.amd64.bin"), sys._getframe().f_code.co_name, other_set], stdout = subprocess.PIPE).communicate()[0]
        else:
            data = subprocess.Popen([os.path.join(".", "route_go", "bin", "main.arm64.bin"), sys._getframe().f_code.co_name, other_set], stdout = subprocess.PIPE).communicate()[0]
    else:
        if platform.machine() in ["AMD64", "x86_64"]:
            data = subprocess.Popen([os.path.join(".", "route_go", "bin", "main.amd64.exe"), sys._getframe().f_code.co_name, other_set], stdout = subprocess.PIPE).communicate()[0]
        else:
            data = subprocess.Popen([os.path.join(".", "route_go", "bin", "main.arm64.exe"), sys._getframe().f_code.co_name, other_set], stdout = subprocess.PIPE).communicate()[0]

    data = data.decode('utf8')

    return flask.Response(response = data, status = 200, mimetype = 'application/json')