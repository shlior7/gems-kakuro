from flask import Flask, render_template
# from kakuro.main import solve_kakuro

app = Flask(__name__)


@app.route('/')
def hello():
    kakuro = [
            [
                -1,
                -1,
                -1,
                -1,
                4,
                0,
                10,
                0,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
            ],
            [
                -1,
                -1,
                0,
                4,
                0,
                0,
                0,
                0,
                -1,
                -1,
                3,
                0,
                4,
                0,
            ],
            [
                -1,
                -1,
                0,
                3,
                0,
                0,
                0,
                0,
                11,
                4,
                0,
                0,
                0,
                0,
            ],
            [
                -1,
                -1,
                3,
                0,
                4,
                10,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                11,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                4,
                0,
                -1,
                -1,
            ],
            [
                0,
                4,
                0,
                0,
                0,
                0,
                0,
                4,
                0,
                0,
                0,
                0,
                -1,
                -1,
            ],
            [
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                0,
                3,
                0,
                0,
                0,
                0,
                -1,
                -1,
            ],
        ]
    result = kakuro
    return result
