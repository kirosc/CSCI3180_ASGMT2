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
    boolean buyEnabled = true;
    Scanner sc = new Scanner(System.in);

    while (buyEnabled) {
      this.talk("Do you want to buy something? (1. Elixir, 2. Shield, 3. Leave.) Input: ");

      String choice = sc.nextLine();

      if (choice.equalsIgnoreCase("1")) {
        if (soldier.getCoin() >= elixirPrice) {
          soldier.useCoin(elixirPrice);
          soldier.addElixir();
          System.out.printf("You have bought an Elixir.%n%n");
        } else {
          this.talk("You don't have enough coins.%n%n");
        }
        buyEnabled = false;
      } else if (choice.equalsIgnoreCase("2")) {
        if (soldier.getCoin() >= shieldPrice) {
          soldier.useCoin(shieldPrice);
          soldier.addShield();
          System.out.printf("You have bought a Shield.%n%n");
        } else {
          this.talk("You don't have enough coins.%n%n");
        }
        buyEnabled = false;
      } else if (choice.equalsIgnoreCase("3")) {
        buyEnabled = false;
      } else {
        System.out.printf("=> Illegal choice!%n%n");
      }
    }
  }

  public Pos getPos() {
    return this.pos;
  }

  public void setPos(int row, int column) {
    this.pos.setPos(row, column);
  }

  public void talk(String text) {
    System.out.printf("Merchant$: " + text);
  }

  public void displaySymbol() {
    System.out.printf("$");
  }
}