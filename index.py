from flask import Flask
from kakuro import solve_kakuro

app = Flask(__name__)


@app.route('/')
def hello():
    kakuro_board = [
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
    result = solve_kakuro(kakuro_board)
    return {'result': result}


@app.route('/solve')
def hello(board: list[list[int]]):
    result = solve_kakuro(board)
    return {'result': result}


if __name__ == "__main__":
    app.run()
