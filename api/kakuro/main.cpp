#include <pybind11/pybind11.h>
#include <iostream>
#include <pybind11/stl.h>
#include "stdio.h"
#include "game.h"

std::vector<std::vector<int>> solve_kakuro(std::vector<std::vector<int>> board)
{
    Game kakuro(board);
    kakuro.solver();
    kakuro.game_board->print();
    return kakuro.game_board->toVector();
}

namespace py = pybind11;

PYBIND11_MODULE(main, m)
{
    // optional module docstring
    m.doc() = "pybind11 main plugin";

    m.def(
        "solve_kakuro", &solve_kakuro, "A function which solves kakuro");
}
