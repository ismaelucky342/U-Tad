/* 5.a As an example of any piece in a board game, chess or checkers, write the code for a class called GameShape, and its representation in UML, with a single behavior method, displayShape, whose implementation will print a message to the console "displaying shape".

5.b As a specialization of the previous class, GameShape, write the code for a new class GamePiece, and its representation in UML, adding a new method movePiece, whose implementation will print a message to the console 'moving game piece'.

5.c In the main method of the GameShape class, create an object called "figure" of type GameShape corresponding to an instance of the GamePiece class. */

class GameShape {
	public void displayShape() {
		System.out.println("displaying shape");
	}

	public static void main(String[] args) {
		GameShape figure = new GamePiece();
		figure.displayShape();
	}
}

class GamePiece extends GameShape {
	public void movePiece() {
		System.out.println("moving game piece");
	}
}

