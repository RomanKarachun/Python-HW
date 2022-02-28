import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;
public class Rules {
	public void GameStart(){
		ArrayList<Integer> allBrand = new ArrayList<Integer>();
		for(int i=1;i<=36;i++){
			allBrand.add(i);
		}
		Player player1=new Player();
		Player player2=new Player();
		Scanner sc=new Scanner(System.in);
		Licensing(allBrand,player1,player2);
		showBrand(player1,player2);
		Calculation( player1, player2);
		needBrand(allBrand,player1,player2);
		compare(player1, player2);
	}
	public void compare(Player player1,Player player2){
		if(player1.getScore()>player2.getScore()&&player1.getScore()<=21 ){
			System.out.println("Player 1, u win!");
		}else if(player1.getScore()<player2.getScore()&&player2.getScore()<=21){
			System.out.println("Player 2, u win!");
		}else if(player1.getScore() > 21 || player2.getScore() <= 21){
			System.out.println("Player 2, u win!");
		}else if(player2.getScore() > 21 || player1.getScore() <= 21){
			System.out.println("Player 1, u win!");
		}
	}
	public void needBrand(ArrayList<Integer> allBrand,Player player1,Player player2){
		Random rd=new Random();
		int choice;
		int choice1;
		do{
		System.out.println("Player 1, do u need another card?");
		System.out.println("1=Y | 2=N");
		Scanner sc=new Scanner(System.in);
		choice=sc.nextInt();
		switch (choice) {
		case 1:
			int a=rd.nextInt(allBrand.size());
			player1.getArr().add(allBrand.get(a));
			allBrand.remove(a);
			showBrand(player1,player2);
			Calculation( player1, player2);
			break;
		case 2:
			break;
		default:
			System.out.println("Incorrect!");
			break;
		}
		System.out.println("Player 2, do u need another card?");
		System.out.println("1=Y | 2=N");
		choice1=sc.nextInt();
		switch (choice1) {
		case 1:
			int b=rd.nextInt(allBrand.size());
			player2.getArr().add(allBrand.get(b));
			allBrand.remove(b);
			showBrand(player1,player2);
			Calculation( player1, player2);
			break;
		case 2:
			break;
		default:
			System.out.println("Incorrect!");
			break;
		}
		}while(choice==1||choice1==1);
	}
	public void Calculation(Player player1,Player player2){
		System.out.println();
		int temp=0;
		for(int i=0;i<player1.getArr().size();i++){
			temp+=brandNumber(player1.getArr().get(i));
			player1.setScore(temp);
		}
		temp=0;
		System.out.println("Player 1 score = "+player1.getScore());
		for(int i=0;i<player2.getArr().size();i++){
			temp+=brandNumber(player2.getArr().get(i));
			player2.setScore(temp);
		}
		System.out.println("Player 2 score = "+player2.getScore());
	}
	public int brandNumber(int i){
		if(i<=4 &&i>0){
			return 11;
		}else if(i<=8 && i>4){
			return 6;
		}else if(i<=12 && i>8){
			return 7;
		}else if(i<=16 && i>12){
			return 8;
		}else if(i<=20 && i>16){
			return 9;
		}else if(i<=24 && i>20){
			return 10;
		}else if(i<=28 && i>24){
			return 2;
		}else if(i<=32 && i>28){
			return 3;
		}else if(i<=36 && i>32){
			return 4;
		}return 0;
	}
	public void showBrand(Player player1,Player player2){
		System.out.print("Player's 1 current cards: ");
		for(int i=0;i<player1.getArr().size();i++){
			BrandFace(player1.getArr().get(i), player1, player2);
			System.out.print(" ");
		}
		System.out.println();
		System.out.print("Player's 2 current cards: ");
		for(int i=0;i<player2.getArr().size();i++){
			BrandFace(player2.getArr().get(i), player1, player2);
			System.out.print(" ");
		}
	}
	public void BrandFace(int i,Player player1,Player player2){
		if(i<=4 &&i>0){
			System.out.print("A");
		}else if(i<=8 && i>4){
			System.out.print("6");
		}else if(i<=12 && i>8){
			System.out.print("7");
		}else if(i<=16 && i>12){
			System.out.print("8");
		}else if(i<=20 && i>16){
			System.out.print("9");
		}else if(i<=24 && i>20){
			System.out.print("10");
		}else if(i<=28 && i>24){
			System.out.print("J");
		}else if(i<=32 && i>28){
			System.out.print("Q");
		}else if(i<=36 && i>32){
			System.out.print("K");
		}
	}
	public void Licensing(ArrayList<Integer> allBrand,Player player1,Player player2){
		Random rd=new Random();
		int first=rd.nextInt(allBrand.size());
		player1.getArr().add(allBrand.get(first));
		allBrand.remove(first);
		int second=rd.nextInt(allBrand.size());
		player1.getArr().add(allBrand.get(second));
		allBrand.remove(second);
		int third=rd.nextInt(allBrand.size());
		player2.getArr().add(allBrand.get(third));
		allBrand.remove(third);
		int fourth=rd.nextInt(allBrand.size());
		player2.getArr().add(allBrand.get(fourth));
		allBrand.remove(fourth);
	}
}