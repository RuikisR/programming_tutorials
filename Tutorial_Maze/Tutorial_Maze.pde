int screenWidth = 400,screenHeight = 400;

// declare variables 
int playerX,playerY;
boolean move;

void settings(){
 size(screenWidth,screenHeight); 
}

void setup(){
  // initialise variables
   playerX = 20;
   playerY = 20;
   move = true;
}

void draw(){
 // make background white 
 background(255);
 
 // make player rectangle black using greyscale notation
 fill(0);
 
 // rect( xposition, yposition, width, height)
 rect(playerX,playerY,20,20);
 
 // fill( Red, Green, Blue)
 fill(255,0,0);
 rect(380,20,5,5);
 
 // make a wall black using rgb notation
 fill(0,0,0);
 rect(200,0,5,360);
 fill(0,0,0);
 rect(100,40,5,360);
 
 // find out if the player is touching the cherry
 if (playerX + 20 > 380 
   && playerX <= 385
   && playerY <= 25
   && playerY + 20 > 20) {
     println("Cherry");
 }
 
 // find out if the player is touching the wall
 if (playerX + 20 > 200 
   && playerX <= 205
   && playerY <= 360
   && playerY + 20 > 0) {
     move = false;
     println("Wall");
 } 
 
 // find out if the player is touching the wall
 if (playerX + 20 > 100 
   && playerX <= 105
   && playerY <= 400
   && playerY + 20 > 40) {
     move = false;
     println("Wall");
 } 
}

void keyPressed(){
  // if the player  is able to move
  if(move){
    // move left
    if(key == 'a') playerX -= 5;
    
    // move right
    if(key == 'd') playerX += 5;
    
    //move up
    if(key == 'w') playerY -= 5;
    
    //move down
    if(key == 's') playerY += 5;
  }
}
