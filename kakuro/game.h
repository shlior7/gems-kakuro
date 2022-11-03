#include "board.h"

class Game
{
public:
	unique_ptr<Board> game_board;
	Game(int width, int height) : game_board(make_unique<Board>(width, height)) {}
	Game(std::vector<std::vector<int>> board) : game_board(make_unique<Board>(board)) {}
	bool solver();
	bool solve_down(shared_ptr<k_cell> &k);
	bool solve_right();
	bool possible(const shared_ptr<k_cell> &k_down, const shared_ptr<k_cell> &k_right, int n);
};
