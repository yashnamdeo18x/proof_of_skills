from datetime import datetime

# ========== SCORING ENGINE ==========

def calculate_repo_score(data):
    core_score = 0
    advanced_score = 0

    # 1. Fork status
    core_score += 0 if data["fork"] else 10

    # 2. Commit ownership
    if data["commit_ownership_percent"] >= 90:
        core_score += 10
    elif data["commit_ownership_percent"] >= 75:
        core_score += 8
    elif data["commit_ownership_percent"] >= 50:
        core_score += 5
    else:
        core_score += 2

    # 3. Commit spread
    if data["commit_spread_days"] >= 14:
        core_score += 10
    elif data["commit_spread_days"] >= 7:
        core_score += 7
    elif data["commit_spread_days"] >= 3:
        core_score += 4
    else:
        core_score += 1

    # 4. Creation vs Push
    if data["repo_created"] and data["repo_pushed"]:
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        created = datetime.strptime(data["repo_created"], fmt)
        pushed = datetime.strptime(data["repo_pushed"], fmt)
        diff_days = (pushed - created).days

        if diff_days >= 30:
            core_score += 10
        elif diff_days >= 14:
            core_score += 7
        elif diff_days >= 7:
            core_score += 5
        else:
            core_score += 2
    else:
        core_score += 0

    # 5. README
    core_score += 10 if data["readme_exists"] else 2

    # Advanced checks
    advanced_score += 5 if data["commit_email_match"] else -5

    if data["stargazers_count"] > 100:
        advanced_score -= 5
    elif data["stargazers_count"] > 30:
        advanced_score -= 2
    else:
        advanced_score += 2

    advanced_score -= 5 if data["ai_comment_found"] else 2
    advanced_score -= 10 if data["single_commit_dump"] else 0
    advanced_score += 5 if data["top_contributor_is_user"] else -5

    # Total score
    total_score = core_score + advanced_score
    normalized_score = max(min(round((total_score / 80) * 100), 100), 0)

    if normalized_score >= 85:
        verdict = "✅ Trusted Original"
    elif normalized_score >= 60:
        verdict = "🟡 Likely Original"
    elif normalized_score >= 40:
        verdict = "🟠 Suspicious"
    else:
        verdict = "🔴 Likely Copied"

    return {
        "score": normalized_score,
        "verdict": verdict,
        "core_score": core_score,
        "advanced_score": advanced_score
    }

# ========== HELPER FUNCTIONS ==========

def is_forked(repo_data):
    return repo_data.get("fork", False)

def get_commit_ownership(commits, username):
    total = len(commits)
    authored_by_user = sum(1 for c in commits if c.get("author") and c["author"].get("login") == username)
    return (authored_by_user / total) * 100 if total > 0 else 0

def get_commit_spread(commits):
    if not commits:
        return 0
    dates = [datetime.strptime(c["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ") for c in commits]
    return (max(dates) - min(dates)).days

def is_single_commit_dump(commits, file_count):
    return len(commits) == 1 and file_count > 10

def has_readme(files):
    return any(f["name"].lower() == "readme.md" for f in files)

def is_email_match(commits, user_email):
    emails = [c["commit"]["author"]["email"].lower() for c in commits]
    match_count = emails.count(user_email.lower())
    return match_count >= (len(commits) // 2)

def is_top_contributor(contributors, username):
    if not contributors:
        return False
    top = contributors[0]
    return top.get("login") == username

def get_score_input(github_data, username, user_email):
    return {
        "fork": is_forked(github_data["repo"]),
        "commit_ownership_percent": get_commit_ownership(github_data["commits"], username),
        "commit_spread_days": get_commit_spread(github_data["commits"]),
        "readme_exists": has_readme(github_data["files"]),
        "repo_created": github_data["repo"]["created_at"],
        "repo_pushed": github_data["repo"]["pushed_at"],
        "commit_email_match": is_email_match(github_data["commits"], user_email),
        "stargazers_count": github_data["repo"]["stargazers_count"],
        "ai_comment_found": github_data.get("ai_comment_found", False),  # placeholder
        "single_commit_dump": is_single_commit_dump(github_data["commits"], github_data["file_count"]),
        "top_contributor_is_user": is_top_contributor(github_data["contributors"], username)
    }