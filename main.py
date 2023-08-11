import click
from budget_manager import BudgetManager
from commands import add, list_expenses, remaining

@click.group()
@click.option("--initial-budget", prompt="Budget mensuel initial", type=float)
@click.pass_context
def cli(ctx, initial_budget):
    """Application de gestion de budget."""
    ctx.obj = {"budget_manager": BudgetManager(initial_budget)}

cli.add_command(add)
cli.add_command(list_expenses, name="list")
cli.add_command(remaining)

if __name__ == "__main__":
    cli()
