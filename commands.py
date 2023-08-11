import click

# Ajoute une dépense
@click.command()
@click.option("--amount", prompt="Montant de la dépense", type=float)
@click.option("--category", prompt="Catégorie de la dépense")
@click.pass_context
def add(ctx, amount, category):
    """Ajoute une dépense."""
    budget_manager = ctx.obj["budget_manager"]
    budget_manager.add_expense(amount, category)
    click.echo("Dépense ajoutée avec succès !")

# Affiche la liste des dépenses
@click.command()
@click.pass_context
def list_expenses(ctx):
    """Affiche la liste des dépenses."""
    budget_manager = ctx.obj["budget_manager"]
    click.echo("\nListe des dépenses :")
    for expense in budget_manager.expenses:
        click.echo(f"{expense['category']}: {expense['amount']}")

# Affiche le budget restant
@click.command()
@click.pass_context
def remaining(ctx):
    """Affiche le budget restant."""
    budget_manager = ctx.obj["budget_manager"]
    click.echo(f"Budget restant : {budget_manager.get_remaining_budget()}")
