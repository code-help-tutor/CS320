WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import re, sys
from re import template
import pandas as pd
from flask import Flask, request, jsonify


application = Flask(__name__)


locationsTypes = {
    'id': 'object',
    'latitude': 'object',
    'longitude': 'object',
    'access_code': 'object',
    'description': 'object'
}
LOCATIONS_BFS = pd.read_csv('locations1.csv').astype(locationsTypes)
LOCATIONS_DFS = pd.read_csv('locations2.csv').astype(locationsTypes)

@application.route('/')
def home():
    with open("index.html") as f:
        html = f.read()
    return html

def node_link(node_index):
    return f'<th><a href="Node_{node_index}.html">Page {node_index}</a></th>'

def node(title, linkIndicies, bfs_pass, dfs_pass):
    result = None
    with open('Node_Template.html') as f:
        template = f.read()
        template = template.replace('&Title&', title)
        template = template.replace('&BFS_PASS&', bfs_pass)
        template = template.replace('&DFS_PASS&', dfs_pass)

        linkText = ""
        for linkIndex in linkIndicies:
            linkText += node_link(linkIndex)
        result = template.replace('&Links&', linkText)
    return result




@application.route('/Node_1.html')
def Node_1():
    return node("Maze Start", [2, 4], '1', '9')

@application.route("/Node_2.html")
def Node_2():
    return node("Page 2", [1, 3, 5], '2', '8')

@application.route("/Node_3.html")
def Node_3():
    return node("Page 3", [1, 6], '4', '7')

@application.route("/Node_4.html")
def Node_4():
    return node("Page 4", [3, 6, 7], '3', '6')

@application.route("/Node_5.html")
def Node_5():
    return node("Page 5", [6], '5', '5')

@application.route("/Node_6.html")
def Node_6():
    return node("Page 6", [3], '6', '4')

@application.route("/Node_7.html")
def Node_7():
    return node("Page 7", [6], '7', '3')

@application.route('/expandingTable.html')
def expandingTable():
    with open("expandingTable.html") as f:
        html = f.read()
    return html

@application.route('/waitingTable.html')
def waitingTable():
    with open("waitingTable.html") as f:
        html = f.read()
    return html

@application.route('/styles.css')
def styles():
    with open("styles.css") as f:
        html = f.read()
    return html

password_bfs = "1234567"
password_dfs = "9874563"

@application.route('/password', methods=["POST"])
def password():
    password = str(request.data, "utf-8")
    if "Password:" in password:
        password=password[9:]
        #if it contains the password precedor, remove it.
        
    if(password == password_bfs):
        return jsonify('expandingTable.html')
    if(password == password_dfs):
        #return jsonify('waitingTable.html')
        return jsonify('expandingTable.html')
    return jsonify('NO')

@application.route('/locations_bfs', methods=["GET"])
def locations_bfs():
    numRowsRequested = int(request.args.get("num"))

    result = []
    for i in range(min(len(LOCATIONS_BFS), numRowsRequested)):
        rowAsDict = LOCATIONS_BFS.iloc[i].to_dict()
        result.append(rowAsDict)

    return jsonify(result)

@application.route('/locations_dfs', methods=["GET"])
def locations_dfs():
    numRowsRequested = int(request.args.get("num"))

    result = []
    for i in range(min(len(LOCATIONS_DFS), numRowsRequested)):
        rowAsDict = LOCATIONS_DFS.iloc[i].to_dict()
        result.append(rowAsDict)

    return jsonify(result)


@application.route('/robots.txt')
def broken():
    with open('robots.txt') as f:
        txt = f.read()
        return txt


if __name__ == '__main__':
    port = None if len(sys.argv) == 1 else int(sys.argv[1])
    application.run("0.0.0.0", port)
