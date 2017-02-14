# CSCI561 Assignment 2

Once upon a time, Los Angeles was a Never Never Land.		People were blissfully happy, Conan O'Brien was still on late-night, and no one knew who “the Real Housewives of New Jersey” were.	 	 Until the day that two violent, money-thirsty gangs decided to put their dirty hands onto Los Angeles.		

One gang was from the north, and the other gang was from the south.		Both wanted to take over the entire city.		Therefore, war was unavoidable.		To win the war, the leader of the south gang knew that he needed not mere foot troops, but admirals.		Therefore, he built an institute to train his future admirals.		He named his training institute CSCI-561, and asked his recruits to create artificial agents to engage in a combat simulation, which he called a 'game', meant to imitate the upcoming gang war.  

(Once the members are finished, the leader will classify their research and pull them from the institute, leaving them fractured and bitter human beings.	 	However, as they do not know this yet, they are full of excitement and zeal for the project.)  

The game is a simulation of ground warfare and has the following rules:  
1. The game board is an NxN grid representing the territory your forces will trample (N=5 in the figures below). Columns are named A, B, C, … starting from the left, and rows are named 1, 2, 3, … from top.
2. Each player takes turns as in chess or tic-tac-toe. That is, player X takes a move, then player O, then back to player X, and so forth.  
3. Each square has a fixed point value between 1 and 99, based upon its computed strategic and resource value.  
4. The object of the game for each player is to score the most points, where score is the sum of all point values of all his or her occupied squares minus the sum of all points in the squares occupied by the other player. Thus, one wants to capture the squares worth the most points while preventing the other player to do so.  
5. The game ends when all the squares are occupied by the players since no more moves are left.  
6. Players cannot pass their move, i.e., they must make a valid move if one exists (game is not over).  
7. Movement and adjacency relations are always vertical and horizontal but never diagonal.  
8. The values of the squares can be changed for each game, but remain constant within a game.  
9. Game score is computed as the difference between (a) the sum of the values of all squares occupied by your player and (b) the sum of the values of all squares occupied by the other player. This applies both to terminal (game over, terminal utility function) and non-terminal states (evaluation function). This is required to ensure that your program produces the same results as the grading script.  
10. On each turn, a player can make one of two moves:  

Stake – You can take any open space on the board.		This will create a new piece on the board. This move can be made as many times as one wants to during the game, but only once per turn. However, a Stake cannot conquer any pieces.		It simply allows one to arbitrarily place a piece anywhere unoccupied on the board. Once you have done a Stake, your turn is complete.  

Raid – From any space you occupy on the board, you can take the one next to it (up, down, left, right, but not diagonally) if it is unoccupied.		The space you originally held is still occupied. Thus, you get to create a new piece in the raided square. Any enemy touching the square you have taken is conquered and that square is turned to your side (you turn its piece to your side). A Raid can be done even if it will not conquer another piece. Once you have made this move, your turn is over.    

Your assignment is:
Base homework (required): Create a program to play the game, using, depending on specification in the input file, either the plain Minimax algorithm with depth limit, or Alpha-Beta Pruning.
