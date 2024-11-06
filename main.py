from src.world.world import World
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout


def display_world(console, chunksize: int):
    table = Table(box=None, show_header=False, show_edge=False)
    for row in chunksize:
        table.add_row(" ".join(row))
    console.print(Panel(table, title="2D CLI World", border_style="blue"))

def main():
    console = Console()
    world = World()
    display_world(console, world.get_chunks())
    

if __name__ == "__main__":
    main()