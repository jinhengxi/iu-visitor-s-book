from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.f6qpo.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework2", methods=["POST"])
def homework2_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    homework2_list = list(db.homework2.find({}, {'_id': False}))
    count = len(homework2_list) + 1

    doc = {'name': name_receive,
           'comment': comment_receive,
           'num': count
           }
    db.homework2.insert_one(doc)

    return jsonify({'msg':'응원 완료!'})

@app.route("/homework2/delete", methods=["POST"])
def homework2_delete():
    num_receive = request.form['num_give']
    db.homework2.delete_one({'num': int(num_receive)})
    return jsonify({'msg':'삭제 완료!'})

@app.route("/homework2/edit", methods=["POST"])
def homework2_edit():

    name_receive = request.form['current_name_give']
    comment_receive = request.form['current_comment_give']
    edit_name_receive = request.form['edit_name_give']
    edit_comment_receive = request.form['edit_comment_give']

    db.homework2.update_one({'name': name_receive}, {'$set': {'name':edit_name_receive}})
    db.homework2.update_one({'comment': comment_receive}, {'$set': {'comment':edit_comment_receive}})
    return jsonify({'msg':'수정 완료!'})


@app.route("/homework2", methods=["GET"])
def homework2_get():
    comment_list = list(db.homework2.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)