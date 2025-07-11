import typer
from .summarize import summarizing

app = typer.Typer()
app.command()(summarizing)

if __name__ == "__main__":
    app()