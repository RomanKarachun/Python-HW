import java.util.ArrayList;

public class Player {

	private String name;
	private ArrayList<Integer> al = new ArrayList<Integer>();
	private int score;
	public Player() {
		super();
	}
	public Player(String name, int score) {
		super();
		this.name = name;
		this.score = score;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	public ArrayList<Integer> getArr() {
		return al;
	}
	public int getScore() {
		return score;
	}
	public void setScore(int score) {
		this.score = score;
	}
}
