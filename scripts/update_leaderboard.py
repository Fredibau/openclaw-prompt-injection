import os
import yaml
from datetime import datetime

ATTACKS_DIR = "attacks"
LEADERBOARD_FILE = "LEADERBOARD.md"

def get_attack_data():
    attacks = []
    if not os.path.exists(ATTACKS_DIR):
        return attacks

    for source_dir in os.listdir(ATTACKS_DIR):
        source_path = os.path.join(ATTACKS_DIR, source_dir)
        if not os.path.isdir(source_path):
            continue
        
        for attack_dir in os.listdir(source_path):
            attack_path = os.path.join(source_path, attack_dir)
            meta_path = os.path.join(attack_path, "meta.yaml")
            
            if os.path.exists(meta_path):
                with open(meta_path, "r") as f:
                    try:
                        data = yaml.safe_load(f)
                        # Add path for linking
                        data['path'] = f"/attacks/{source_dir}/{attack_dir}/"
                        # Use file mtime as a fallback date if not in yaml
                        if 'date' not in data:
                            mtime = os.path.getmtime(meta_path)
                            data['date'] = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
                        attacks.append(data)
                    except Exception as e:
                        print(f"Error parsing {meta_path}: {e}")
    
    # Sort by date descending
    attacks.sort(key=lambda x: x.get('date', ''), reverse=True)
    return attacks

def generate_leaderboard(attacks):
    header = "# OpenClaw Injection Leaderboard (Hall of Fame)\n\n"
    header += "This leaderboard is automatically updated when new verified attacks are merged.\n\n"
    
    # Table of attacks
    table = "## Recent Successful Attacks\n\n"
    table += "| Date | ID | Title | Source | Models | Severity | Author |\n"
    table += "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
    
    stats = {
        "SRC-FILE": 0,
        "SRC-WEB": 0,
        "SRC-SKILL": 0,
        "SRC-SOUL": 0,
        "SRC-FEED": 0
    }
    
    for a in attacks:
        date = a.get('date', 'N/A')
        aid = a.get('id', 'N/A')
        title = a.get('title', 'N/A')
        source = a.get('source', 'N/A')
        severity = a.get('severity', 'N/A')
        author = a.get('author', 'N/A')
        path = a.get('path', '#')
        models = ", ".join(a.get('models', ['N/A']))
        
        table += f"| {date} | [{aid}]({path}) | {title} | {source} | {models} | {severity} | {author} |\n"
        
        if source in stats:
            stats[source] += 1

    # Stats table
    stats_table = "\n## Attack Statistics (by Source)\n\n"
    stats_table += "| Source | Total Verified Attacks |\n"
    stats_table += "| :--- | :--- |\n"
    for src, count in stats.items():
        stats_table += f"| **{src}** | {count} |\n"
    
    # Contributor Ranking
    contributor_stats = {}
    for a in attacks:
        author = a.get('author', 'N/A')
        contributor_stats[author] = contributor_stats.get(author, 0) + 1
    
    # Sort contributors by count descending
    sorted_contributors = sorted(contributor_stats.items(), key=lambda x: x[1], reverse=True)
    
    rank_table = "\n## Contributor Ranking\n\n"
    rank_table += "| Rank | Author | Attacks Submitted |\n"
    rank_table += "| :--- | :--- | :--- |\n"
    for i, (author, count) in enumerate(sorted_contributors, 1):
        rank_table += f"| {i} | {author} | {count} |\n"
    
    footer = "\n---\n\n### How to get listed\n"
    footer += "1. Submit a Pull Request with a new attack case following the [ATTACK_SPEC.md](/ATTACK_SPEC.md).\n"
    footer += "2. Once merged, this leaderboard will update automatically.\n"
    
    with open(LEADERBOARD_FILE, "w") as f:
        f.write(header + table + stats_table + rank_table + footer)

if __name__ == "__main__":
    attacks = get_attack_data()
    generate_leaderboard(attacks)
    print(f"Leaderboard updated with {len(attacks)} attacks.")

