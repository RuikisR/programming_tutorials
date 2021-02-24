char[] board;
char player;
boolean gameOver = false;

void setup(){
  board = new char[9];
  player = 'X';
  size(300,300);
  for(int i = 0; i < 9; i++) board[i] = '_';
}

void draw(){
  //stop the game
  if(gameOver)return;
  
  //check if someone has won
  if(hasWinner(board)){
   println(switchPlayer(player)," has won!");
   gameOver = true;
  }
  
  //colour the lines and background
  background(255);
  fill(0);
  
  //draw our board
  drawBoard(board);
}

//change player
char switchPlayer(char input) {
   if (input == 'O') return 'X';
   else return 'O';
}

boolean hasWinner(char[] board) {
  // Row checks
  for(int i = 0; i < 9; i += 3){
     if(board[i] != '_' && board[i] == board[i + 1] && board[i] == board[1 + 2]) return true;
  }
  
  // Column checks
  for(int i = 0; i < 3; i ++){
     if(board[i] != '_' && board[i] == board[i + 3] && board[i] == board[i + 6]) return true;
  }
  
  // Diagonal checks
  if(board[0] != '_' && board[0] == board[4] && board[0] == board[8]) return true;
  if(board[2] != '_' && board[2] == board[4] && board[2] == board[6]) return true;
  
  return false;
}

void drawBoard(char[] board){
  //horizontal lines
  rect(20,100,260,5);
  rect(20,200,260,5);
  
  //vertical lines
  rect(100,20,5,260);
  rect(200,20,5,260);
  
  for(int column = 0; column < 3; column ++){
     for(int row = 0; row < 3; row ++){
       // draw X's and O's
       if(board[column*3 + row] == 'O'){
         ellipseMode(CORNER);
         ellipse(column * 100 + 30,row * 100 + 30,50,50);
       } else if(board[column*3 + row] == 'X'){
         line(column * 100 + 30,row * 100 + 30,column * 100 + 80,row * 100 + 80);
         line(column * 100 + 80,row * 100 + 30,column * 100 + 30,row * 100 + 80);
       }
     }
  }
}

void mousePressed() {
  boolean endLoop = false;
  
  for(int column = 0; column < 3; column ++){
     for(int row = 0; row < 3; row ++){
       if(mouseX < ((column * 100)+100)  && mouseY < ((row * 100)+100)){
         //set the square to the current player
         board[((column*3)+row)] = player;
         
         //change the player
         player = switchPlayer(player);
         
         //stop searching for winners
         endLoop = true;
       }
       if(endLoop)break;
     }
     if(endLoop)break;
  }
  
}
