import java.util.Scanner;

public class Merchant {

  private int elixirPrice;
  private int shieldPrice;
  private Pos pos;

  public Merchant() {
    this.elixirPrice = 1;
    this.shieldPrice = 2;
    this.pos = new Pos();
  }

  public void actionOnSoldier(Task4Soldier soldier) {
    this.talk("Do you want to buy something? (1. Elixir, 2. Shield, 3. Leave.) Input: ");

    boolean buyEnabled = true;
    Scanner sc = new Scanner(System.in);

    while (buyEnabled) {
      String choice = sc.nextLine();

      if (choice.equalsIgnoreCase("1")) {
        if (soldier.getCoin() >= elixirPrice) {
          soldier.useCoin(elixirPrice);
          soldier.addElixir();
          System.out.printf("You have bought an Elixir.%n%n");
        } else {
          System.out.printf("You don't have enough coins.%n%n");
        }
        buyEnabled = false;
      } else if (choice.equalsIgnoreCase("2")) {
        if (soldier.getCoin() >= shieldPrice) {
          soldier.useCoin(shieldPrice);
          soldier.addElixir();
          System.out.printf("You have bought a Shield.%n%n");
        } else {
          System.out.printf("You don't have enough coins.%n%n");
        }
        buyEnabled = false;
      } else if (choice.equalsIgnoreCase("3")) {
        buyEnabled = false;
      } else {
        System.out.printf("=> Illegal choice!%n%n");
      }
    }
  }

  public void talk(String text) {
    System.out.printf("Merchant$: " + text);
  }
}