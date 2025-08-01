from datetime import datetime

def generate_markdown(sector: str, ai_output: str) -> str:
    date = datetime.now().strftime("%Y-%m-%d")
    return f"# Market Analysis: {sector.title()} Sector (India)\n\n{ai_output}\n\n*Last Updated: {date}*"
