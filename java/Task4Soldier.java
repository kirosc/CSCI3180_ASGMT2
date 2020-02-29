public class Task4Soldier extends Soldier {

  private int numCoins = 0;
  private int defenseValue = 0;

  public void addShield() {
    this.defenseValue += 5;
  }

  public int getCoin() {
    return this.numCoins;
  }

  public void addCoin() {
    this.numCoins++;
  }

  public void useCoin(int number) {
    this.numCoins -= number;
  }

  @Override
  public boolean loseHealth() {
    this.health += this.defenseValue;
    return super.loseHealth();
  }
}
