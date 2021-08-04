/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: Basic.java StdDraw.java
 *
 *  Creates a Basic ball and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;

public class BallGame { 

    public static void main(String[] args) {
        
    	// number of bouncing balls
        int numBalls =0 ;  
    	try {
            numBalls = Integer.parseInt(args[0]);
        } catch (Exception e) {
            System.out.print("Invalid program argument! - java <num> <type> <radius>\n");

        }
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
    	
        try {
            //retrieve ball types
            int index =1;
            for (int i=0; i<numBalls; i++) {
                ballTypes[i] = args[index];
                index = index+2;
    	}
        } catch (Exception e) {
            System.out.print("Invalid program argument! - java <num> <type> <radius>\n");
        }

        try {
            //retrieve ball sizes
            int index = 2;
            for (int i=0; i<numBalls; i++) {
                ballSizes[i] = Double.parseDouble(args[index]);
                index = index+2;
    	    }   
        } catch (Exception e) {
            System.out.print("Invalid program argument! - java <num> <type> <radius>\n");
        }
     
    	//TO DO: create a Player object and initialize the player game stats.  
    	
    	
    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
   		Basic ball = new Basic(ballSizes[0],Color.RED);
   		//TO DO: initialize the numBallsinGame
   		numBallsinGame++;
        
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

        	// TODO: move all balls
            ball.move();

            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.  
                if (ball.isHit(x,y)) {
                    	ball.reset();
                    	//TO DO: Update player statistics
                }
            }
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game.  
            if (ball.isOut == false) { 
                ball.draw();
                numBallsinGame++;
            }
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            //TO DO: print the rest of the player statistics

            StdDraw.show();
            StdDraw.pause(20);
        }
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
