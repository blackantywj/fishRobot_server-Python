from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
import requests

app = Flask(__name__)
api = Api(app)

value1 = 'welcome'
value2 = 'welcome'
value3 = 'welcome'

TODOS = {
    'todo1': {'task': value1},
    'todo2': {'task': value2},
    'todo3': {'task': value3},
}

parser = reqparse.RequestParser()
parser.add_argument('task')

# Todo
# 增删改查
class Todo(Resource):
    def get(self, todo_id):
        return TODOS[todo_id]
    def delete(self, todo_id):
        del TODOS[todo_id]
        return '', 204
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
    def post(self,todo_id):
        args = parser.parse_args()
        a = request.form.get('d')
        #print(a)
        task = {'task':a}
        TODOS[todo_id] = task
        return task, 201	

api.add_resource(Todo, '/todos/<todo_id>')  #添加资源


if __name__ == '__main__':
    app.run(debug=True)