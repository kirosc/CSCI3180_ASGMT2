from Monster import Monster


class Task4Monster(Monster):
    def __init__(self, monster_id, health_capacity):
        super().__init__(monster_id, health_capacity)

    def drop_items(self, soldier):
        super().drop_items(soldier)
        soldier.add_coin()
