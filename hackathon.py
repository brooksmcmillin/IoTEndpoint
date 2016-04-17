import requests

def dostuff(value):

    print "Pass Through: ", value


    # Send data to server
    req = requests.post("http://hackdfw.brooksmcmillin.com/api/savedata.php", data={"data": "1,2,3,4"})
    print req.status_code, " + ", req.reason


