from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

page1 = '''
    <title>Webpage 2</title>
    <div class="container">
        <h1>Webpage 2</h1>
        <div class="content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla at sem in tortor bibendum consectetur. Nam porttitor tellus vel dapibus convallis. Vivamus condimentum ligula arcu, ut consectetur lacus iaculis at. Etiam euismod tellus augue, eget rhoncus metus efficitur vitae. Praesent iaculis ligula id orci aliquam, eu aliquet justo dapibus. Morbi vel eleifend lectus, a lacinia erat.</p>
            <p>Sed ultricies massa in turpis iaculis, sit amet dictum tellus lobortis. Integer consequat urna sed ultrices rutrum. Fusce vitae consectetur enim. Suspendisse id neque urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nunc ac feugiat enim. In hac habitasse platea dictumst. Sed eu dui id erat elementum aliquet vel in purus. Donec convallis justo quis tincidunt posuere.</p>
            <p>Mauris vestibulum eleifend justo id finibus. Sed congue condimentum dolor vitae ullamcorper. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec vitae dolor nibh. Pellentesque et justo lectus. Phasellus ac purus sem. Duis blandit ante et lacus efficitur, eget rhoncus ligula faucibus. Sed at turpis sed metus blandit laoreet.</p>
            <p>Donec et pulvinar mauris. Donec pretium arcu vel urna blandit, nec varius arcu semper. Vivamus tincidunt consequat tellus, sed semper lorem pellentesque ut. Curabitur dignissim odio eu leo egestas ultricies. Integer vitae mi lorem. Cras hendrerit, turpis et euismod bibendum, orci mauris facilisis nunc, nec pellentesque purus purus sit amet dui.</p>
        </div>
        <button type="submit" class="button" onclick="one()">Click Me</button>
    </div>
'''
page2 = '''
    <title>Webpage 1</title>
    <div class="container">
        <h1>Webpage 1</h1>
        <div class="content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper euismod libero, id convallis elit fringilla at. Morbi vel malesuada metus. Mauris quis mauris consectetur, sagittis quam vitae, consequat felis. Vivamus vitae ultricies lectus. Mauris efficitur sapien in dignissim fringilla.</p>
            <p>Suspendisse varius tempor nibh, vitae faucibus arcu rutrum in. Phasellus nec consectetur odio. Nam id tortor arcu. Quisque consectetur tortor sed risus posuere, vitae dignissim lacus congue. Sed consequat finibus mauris, sed rhoncus turpis varius a. Aenean accumsan sem ut ultrices iaculis.</p>
            <p>Proin mattis nunc risus, a placerat sem vestibulum id. Ut vulputate, turpis ac tempus tristique, nibh tortor eleifend lacus, et hendrerit felis enim et dui. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aliquam volutpat lobortis est id tincidunt. Mauris lacinia nisi vel lectus lobortis, in posuere neque fringilla.</p>
        </div>
        <button type="submit" class="button" onclick="two()">Click Me</button>
    </div>
'''


@app.route('/')
def index():
    return redirect(url_for('static', filename='magic.js'))

@app.route('/api', methods=["GET"])
def get_request():
    return redirect('/')

@app.route('/api', methods=['POST', 'OPTIONS'])
def post_request():
    if request.method == 'OPTIONS':
        response = app.response_class()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    data = request.get_json()
    if data.get("value") == "two":
        return jsonify({"page": page1})
    else:
        return jsonify({"page": page2})


if __name__ == "__main__":
    app.run(debug=True)
