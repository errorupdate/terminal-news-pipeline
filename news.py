import urllib.parse
import feedparser
import json
import os
import sys
import webbrowser
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

console = Console()

rprint(Panel.fit("[bold cyan]Terminal News Data Pipeline[/bold cyan]", border_style="cyan"))

while True:
    console.print("\n" + "="*80)
    query = input("Enter target entity/topic (or 'q' to quit): ")
    
    if query.lower() in ['q', 'quit', 'exit']:
        sys.exit(0)

    # 1. DATA EXTRACTION
    with console.status(f"[bold yellow]Scraping real-time data for '{query}'...", spinner="dots"):
        safe_query = urllib.parse.quote(query)
        url = f"https://news.google.com/rss/search?q={safe_query}&hl=en-IN&gl=IN&ceid=IN:en"
        feed = feedparser.parse(url)

    if not feed.entries:
        console.print("[bold red]No data feeds found. Try another entity.[/bold red]")
        continue
    
    top_articles = feed.entries[:15]
    
    # 2. DATA VISUALIZATION
    overview_text = (
        f"[bold]Target Entity:[/bold] {query}\n"
        f"[bold]Articles Retrieved:[/bold] {len(top_articles)} (Top sources)\n"
        f"[bold]Latest Update:[/bold] {top_articles[0].published if top_articles else 'N/A'}"
    )
    
    summary_panel = Panel(
        overview_text,
        title="[bold green]Live Feed Overview[/bold green]",
        border_style="green",
        expand=False
    )
    console.print("\n")
    console.print(summary_panel)
    
    table = Table(title=f"Source Intelligence: {query}", show_header=True, header_style="bold cyan")
    table.add_column("No.", style="dim", width=4)
    table.add_column("Headline", width=60)
    table.add_column("Publication Date", style="dim")
    
    for i, article in enumerate(top_articles, start=1):
        table.add_row(str(i), article.title, article.published[5:16])
        
    console.print(table)

    # 3. DATA EXPORT
    export_data = {
        "timestamp": datetime.now().isoformat(),
        "topic": query,
        "total_extracted": len(top_articles),
        "sources": [{"title": a.title, "link": a.link} for a in top_articles]
    }
    
    os.makedirs("exports", exist_ok=True)
    filename = f"exports/{query.replace(' ', '_').lower()}_report.json"
    with open(filename, "w") as f:
        json.dump(export_data, f, indent=4)
    
    console.print(f"[bold green]✔ Report successfully exported to {filename}[/bold green]\n")

    # 4. INTERACTIVE READER
    while True:
        choice = input(f"Enter article number (1-{len(top_articles)}) to read, 'n' for new search, or 'q' to quit: ")
        
        if choice.lower() in ['q', 'quit', 'exit']:
            sys.exit(0)
        elif choice.lower() in ['n', 'new']:
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(top_articles):
            idx = int(choice) - 1
            webbrowser.open(top_articles[idx].link)
        else:
            print("Invalid input.")