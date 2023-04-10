
from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon name", ["pika", "squirle","charmander"])
table.align="l"
print(table)
