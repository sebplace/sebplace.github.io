from __future__ import annotations

import json
import os
import re
import unicodedata
import urllib.parse

CONTACT_EMAILS = ["splace@microsoft.com", "Jochem.Claes@microsoft.com"]


def mailto_href(subject, body):
    to = ",".join(CONTACT_EMAILS)
    query = urllib.parse.urlencode({"subject": subject, "body": body}, quote_via=urllib.parse.quote)
    return f"mailto:{to}?{query}"


def minify_css(source):
    """Conservative, safe CSS minifier: strips comments and collapses whitespace.
    Deliberately does not attempt anything risky (no property reordering, no
    unit shortening) — CSS syntax is simple enough that this is safe, unlike a
    hand-rolled JS minifier would be."""
    text = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*([{}:;,>])\s*", r"\1", text)
    text = re.sub(r";}", "}", text)
    return text.strip()


def q(question, options, answer, explanation):
    return {
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation,
    }


def quiz(title, intro, questions, pass_score=4):
    return {
        "title": title,
        "intro": intro,
        "pass_score": pass_score,
        "questions": questions,
    }


def scenario_item(id, icon, role, hook, problem, features, prompt, output, steps, deliverables, impact):
    return {
        "id": id,
        "icon": icon,
        "role": role,
        "hook": hook,
        "problem": problem,
        "features": features,
        "prompt": prompt,
        "output": output,
        "steps": steps,
        "deliverables": deliverables,
        "impact": impact,
    }


def plan_row(plan, price, audience, free_note, facts, badge=None):
    return {
        "plan": plan,
        "price": price,
        "audience": audience,
        "free_note": free_note,
        "facts": facts,
        "badge": badge,
    }


def explorer_usecase(persona, title, features, situation, steps, result, further):
    return {
        "persona": persona,
        "title": title,
        "features": features,
        "situation": situation,
        "steps": steps,
        "result": result,
        "further": further,
    }


ROUTE_FILENAMES = {
    "home": "index.html",
    "explorer": "cas-usage.html",
    "plans": "plans.html",
    "scenarios": "scenarios.html",
    "best_practices": "best-practices.html",
    "toolkit": "toolkit.html",
    "about": "about.html",
    "first_commit": "first-commit.html",
    "build_vs_buy": "build-vs-buy.html",
    "glossary": "glossary.html",
    "workshop": "workshop.html",
    "certificate": "certificate.html",
    "quick_reference": "quick-reference.html",
    "sitemap": "sitemap.html",
    "maturity": "maturity.html",
    "changelog": "changelog.html",
}

FEATURE_KEY_REMAP = {
    "inline": "inline",
    "chat": "chat",
    "agent": "agent",
    "cli": "cli",
    "pr": "review",
    "codingagent": "cloudagent",
    "vision": "spaces",
    "mcp": "mcp",
}

CURRENT_YEAR = 2026
PLACEHOLDER_SITE_BASE = "https://sebplace.github.io/vibe-coding-copilot/"

# Privacy-friendly analytics (GoatCounter — https://www.goatcounter.com). No cookies, no
# personal data, EU-hosted option available. Sign up for free at goatcounter.com, then
# replace this placeholder with your real site code (e.g. "vibecodingcopilot" if your
# dashboard URL is https://vibecodingcopilot.goatcounter.com). Leave as-is to ship the site
# with the feedback widget working purely visually but with no analytics call sent
# (the script tag is simply omitted and the click handler no-ops safely).
GOATCOUNTER_CODE = "vibecodingcopilot"

DOC_URLS = {
    "plans": "https://docs.github.com/en/copilot/get-started/plans",
    "students": "https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students",
    "teachers": "https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers",
    "what_is": "https://docs.github.com/en/copilot/get-started/what-is-github-copilot",
    "features": "https://docs.github.com/en/copilot/get-started/features",
    "spaces": "https://docs.github.com/en/copilot/concepts/context/spaces",
    "copilot_app": "https://docs.github.com/en/copilot/concepts/agents/github-copilot-app",
    "cloud_agent": "https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent",
    "mcp": "https://docs.github.com/en/copilot/concepts/context/mcp",
    "agent_skills": "https://docs.github.com/en/copilot/concepts/agents/about-agent-skills",
    "memory": "https://docs.github.com/en/copilot/concepts/agents/copilot-memory",
    "customization": "https://docs.github.com/en/copilot/reference/customization-cheat-sheet",
    "policies": "https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies",
    "billing": "https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises",
    "plan_getting_started": "https://docs.github.com/en/copilot/how-tos/manage-your-account/get-started-with-a-copilot-plan",
    "campus_program": "https://docs.github.com/en/education/about-github-education/use-github-at-your-educational-institution/about-github-campus-program",
    "create_account": "https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github",
    "repo_quickstart": "https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories",
    "pages_quickstart": "https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site",
    "cli_about": "https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli",
    "cli_getting_started": "https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-getting-started",
    "cli_install": "https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli",
    "desktop": "https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop",
    "agents_overview": "https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/overview",
    "impact_dashboard": "https://docs.github.com/en/copilot/how-tos/administer-copilot/view-impact-dashboard",
    "research_2022": "https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/",
}

FACT_BANNERS = {
    "fr": "Faits vérifiés en août 2026 sur docs.github.com — GitHub Copilot évolue vite, donc revérifie les chiffres précis avant une décision d’achat.",
    "en": "Facts checked in August 2026 against docs.github.com — GitHub Copilot changes quickly, so re-check precise numbers before a buying decision.",
    "nl": "Feiten gecontroleerd in augustus 2026 op docs.github.com — GitHub Copilot evolueert snel, dus controleer exacte cijfers opnieuw vóór een aankoopbeslissing.",
}

SOURCE_LABEL = {"fr": "↗ source", "en": "↗ source", "nl": "↗ bron"}
SKIP_LINK_LABEL = {"fr": "Aller au contenu", "en": "Skip to content", "nl": "Naar de inhoud gaan"}
BACK_TO_TOP_LABEL = {"fr": "Retour en haut de page", "en": "Back to top", "nl": "Terug naar boven"}
OG_LOCALE = {"fr": "fr_FR", "en": "en_US", "nl": "nl_NL"}

# Pages where the "was this helpful?" feedback widget is shown — the meaty, self-serve
# content pages, not listing/utility pages (home, about, glossary, sitemap, changelog,
# certificate, workshop already has its own dedicated CTA).
FEEDBACK_WIDGET_PAGES = {
    "explorer", "scenarios", "first_commit", "build_vs_buy", "plans", "toolkit",
    "best_practices", "quick_reference", "maturity", "basics", "advanced", "expert",
}
FEEDBACK_WIDGET_TEXT = {
    "fr": {
        "question": "Cette page t'a-t-elle aidé\u00b7e ?",
        "yes": "Oui \U0001F44D",
        "no": "Pas vraiment \U0001F44E",
        "thanks": "Merci pour ton retour \u2014 il aide \u00e0 am\u00e9liorer le site.",
    },
    "en": {
        "question": "Was this page helpful?",
        "yes": "Yes \U0001F44D",
        "no": "Not really \U0001F44E",
        "thanks": "Thanks for the feedback \u2014 it helps improve the site.",
    },
    "nl": {
        "question": "Heeft deze pagina je geholpen?",
        "yes": "Ja \U0001F44D",
        "no": "Niet echt \U0001F44E",
        "thanks": "Bedankt voor je feedback \u2014 het helpt de site te verbeteren.",
    },
}

FEATURE_DOCS = {
    "Copilot Chat": DOC_URLS["features"],
    "GitHub Pages": DOC_URLS["pages_quickstart"],
    "Copilot Spaces": DOC_URLS["spaces"],
    "Copilot Student": DOC_URLS["students"],
    "Agent mode": DOC_URLS["features"],
    "Mode Agent": DOC_URLS["features"],
    "Copilot code review": DOC_URLS["features"],
    "GitHub Copilot app": DOC_URLS["copilot_app"],
    "Copilot cloud agent": DOC_URLS["cloud_agent"],
    "Prompt files": DOC_URLS["customization"],
    "AI credits": DOC_URLS["billing"],
    "MCP servers": DOC_URLS["mcp"],
    "GitHub Campus Program": DOC_URLS["campus_program"],
}

GLOSSARY_GROUPS = {
    "fr": [
        {
            "title": "Copilot : fonctionnalités, contexte et agents",
            "items": [
                {"id": "copilot-chat", "term": "Copilot Chat", "desc": "Interface de conversation pour demander, reformuler ou expliquer du code et des tâches dans l’écosystème Copilot.", "source": DOC_URLS["features"]},
                {"id": "agent-mode", "term": "Mode Agent", "desc": "Mode où Copilot peut planifier puis exécuter plusieurs étapes d’un travail au lieu de ne répondre qu’avec du texte.", "source": DOC_URLS["features"]},
                {"id": "copilot-cloud-agent", "term": "Copilot cloud agent", "desc": "Agent exécuté côté GitHub pour prendre en charge des tâches à partir d’une issue ou d’une demande assignée à Copilot.", "source": DOC_URLS["cloud_agent"]},
                {"id": "copilot-cli", "term": "Copilot CLI", "desc": "Interface en ligne de commande pour piloter Copilot depuis un terminal, en mode interactif ou non interactif.", "source": DOC_URLS["cli_about"]},
                {"id": "copilot-app", "term": "GitHub Copilot app", "desc": "Application GitHub qui centralise les interactions agentiques, les tâches et certains flux de travail sur GitHub.", "source": DOC_URLS["copilot_app"]},
                {"id": "copilot-spaces", "term": "Copilot Spaces", "desc": "Espaces de contexte où tu rassembles fichiers, consignes et références afin de mieux ancrer les réponses de Copilot.", "source": DOC_URLS["spaces"]},
                {"id": "copilot-memory", "term": "Copilot Memory", "desc": "Fonction qui permet à Copilot de réutiliser certains faits, préférences ou décisions déjà établis dans un contexte donné.", "source": DOC_URLS["memory"]},
                {"id": "mcp-servers", "term": "MCP servers", "desc": "Serveurs Model Context Protocol qui exposent outils, données ou systèmes pour donner à Copilot un contexte opérationnel vérifiable.", "source": DOC_URLS["mcp"]},
                {"id": "prompt-files", "term": "Prompt files", "desc": "Fichiers de consignes réutilisables pour guider Copilot avec un cadre, une structure ou des attentes précises.", "source": DOC_URLS["customization"]},
                {"id": "custom-agents", "term": "Custom agents", "desc": "Agents configurés pour un rôle ou un flux précis, avec des instructions et parfois des outils ou contextes dédiés.", "source": DOC_URLS["copilot_app"]},
                {"id": "agent-skills", "term": "Agent skills", "desc": "Compétences réutilisables qu’un agent peut invoquer pour accomplir plus vite un type d’action cadré.", "source": DOC_URLS["agent_skills"]},
                {"id": "ai-credits", "term": "AI credits", "desc": "Unité de consommation utilisée pour certains modèles, tâches ou usages avancés selon le plan Copilot choisi.", "source": DOC_URLS["billing"]},
            ],
        },
        {
            "title": "GitHub de base pour démarrer",
            "items": [
                {"id": "repository", "term": "Dépôt (repository)", "desc": "Espace GitHub où vivent les fichiers, l’historique et les réglages d’un projet.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "commit", "term": "Commit", "desc": "Enregistrement daté d’un changement dans l’historique du dépôt.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "branch", "term": "Branch", "desc": "Branche de travail parallèle pour tester un changement sans toucher immédiatement à la version principale.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "pull-request", "term": "Pull Request", "desc": "Demande de relecture et de fusion d’une branche vers une autre, souvent vers la branche principale.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "issue", "term": "Issue", "desc": "Ticket GitHub servant à décrire un besoin, un bug, une idée ou une tâche à suivre.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "github-pages", "term": "GitHub Pages", "desc": "Service d’hébergement statique pour publier rapidement un site ou un prototype depuis un dépôt GitHub.", "source": DOC_URLS["pages_quickstart"]},
            ],
        },
        {
            "title": "Éducation et déploiement",
            "items": [
                {"id": "campus-program", "term": "GitHub Campus Program", "desc": "Programme destiné aux établissements éligibles pour obtenir une capacité plateforme GitHub à l’échelle institutionnelle.", "source": DOC_URLS["campus_program"]},
            ],
        },
    ],
    "en": [
        {
            "title": "Copilot features, context, and agents",
            "items": [
                {"id": "copilot-chat", "term": "Copilot Chat", "desc": "Conversation interface for asking Copilot to explain, draft, refine, or generate work inside the GitHub Copilot experience.", "source": DOC_URLS["features"]},
                {"id": "agent-mode", "term": "Agent mode", "desc": "A mode where Copilot can plan and execute multiple steps instead of only returning a single text answer.", "source": DOC_URLS["features"]},
                {"id": "copilot-cloud-agent", "term": "Copilot cloud agent", "desc": "A GitHub-hosted agent that can pick up assigned tasks and work from issues or natural-language requests.", "source": DOC_URLS["cloud_agent"]},
                {"id": "copilot-cli", "term": "Copilot CLI", "desc": "The command-line interface for using Copilot from a terminal in interactive or scripted workflows.", "source": DOC_URLS["cli_about"]},
                {"id": "copilot-app", "term": "GitHub Copilot app", "desc": "The GitHub app surface that brings together Copilot tasks, agentic flows, and GitHub-native work.", "source": DOC_URLS["copilot_app"]},
                {"id": "copilot-spaces", "term": "Copilot Spaces", "desc": "Context spaces where you gather files, references, and instructions so Copilot answers with better grounding.", "source": DOC_URLS["spaces"]},
                {"id": "copilot-memory", "term": "Copilot Memory", "desc": "A capability that lets Copilot reuse selected facts, preferences, or decisions in the right context.", "source": DOC_URLS["memory"]},
                {"id": "mcp-servers", "term": "MCP servers", "desc": "Model Context Protocol servers that expose tools and trusted data so Copilot can work with real systems.", "source": DOC_URLS["mcp"]},
                {"id": "prompt-files", "term": "Prompt files", "desc": "Reusable instruction files that keep prompts, output structures, or role guidance consistent.", "source": DOC_URLS["customization"]},
                {"id": "custom-agents", "term": "Custom agents", "desc": "Agents tailored to a role or workflow with dedicated instructions and sometimes dedicated tooling.", "source": DOC_URLS["copilot_app"]},
                {"id": "agent-skills", "term": "Agent skills", "desc": "Reusable capabilities that agents can call for well-bounded tasks or repeatable actions.", "source": DOC_URLS["agent_skills"]},
                {"id": "ai-credits", "term": "AI credits", "desc": "Consumption units used for some advanced models or agentic workloads, depending on the Copilot plan.", "source": DOC_URLS["billing"]},
            ],
        },
        {
            "title": "GitHub basics for starters",
            "items": [
                {"id": "repository", "term": "Repository", "desc": "A GitHub project space that stores files, history, settings, and collaboration flows.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "commit", "term": "Commit", "desc": "A recorded snapshot of a change in the project history.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "branch", "term": "Branch", "desc": "A parallel line of work for testing or preparing changes before merging them into the main branch.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "pull-request", "term": "Pull Request", "desc": "A request to review and merge changes from one branch into another.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "issue", "term": "Issue", "desc": "A GitHub ticket used to capture ideas, bugs, tasks, or requests for work.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "github-pages", "term": "GitHub Pages", "desc": "GitHub’s static hosting service for quickly publishing a site or prototype from a repository.", "source": DOC_URLS["pages_quickstart"]},
            ],
        },
        {
            "title": "Education and rollout",
            "items": [
                {"id": "campus-program", "term": "GitHub Campus Program", "desc": "A programme for eligible institutions that want institution-wide GitHub platform capacity.", "source": DOC_URLS["campus_program"]},
            ],
        },
    ],
    "nl": [
        {
            "title": "Copilot-features, context en agents",
            "items": [
                {"id": "copilot-chat", "term": "Copilot Chat", "desc": "Gespreksinterface om Copilot te vragen iets uit te leggen, te herschrijven of mee op te bouwen.", "source": DOC_URLS["features"]},
                {"id": "agent-mode", "term": "Agent mode", "desc": "Modus waarin Copilot meerdere stappen kan plannen en uitvoeren in plaats van alleen tekst terug te geven.", "source": DOC_URLS["features"]},
                {"id": "copilot-cloud-agent", "term": "Copilot cloud agent", "desc": "Een door GitHub gehoste agent die toegewezen taken kan opnemen vanuit issues of natuurlijke taal.", "source": DOC_URLS["cloud_agent"]},
                {"id": "copilot-cli", "term": "Copilot CLI", "desc": "De command-line-interface om Copilot vanuit een terminal te gebruiken, interactief of in scripts.", "source": DOC_URLS["cli_about"]},
                {"id": "copilot-app", "term": "GitHub Copilot app", "desc": "De GitHub-appomgeving die agentische taken en GitHub-native workflows samenbrengt.", "source": DOC_URLS["copilot_app"]},
                {"id": "copilot-spaces", "term": "Copilot Spaces", "desc": "Contextspaces waarin je bestanden, referenties en instructies bundelt voor beter gegronde antwoorden.", "source": DOC_URLS["spaces"]},
                {"id": "copilot-memory", "term": "Copilot Memory", "desc": "Mogelijkheid waarbij Copilot bepaalde voorkeuren, feiten of beslissingen kan hergebruiken in de juiste context.", "source": DOC_URLS["memory"]},
                {"id": "mcp-servers", "term": "MCP-servers", "desc": "Model Context Protocol-servers die tools of betrouwbare data aanbieden zodat Copilot met echte systemen kan werken.", "source": DOC_URLS["mcp"]},
                {"id": "prompt-files", "term": "Prompt files", "desc": "Herbruikbare instructiebestanden om prompts en verwachte output consistenter te maken.", "source": DOC_URLS["customization"]},
                {"id": "custom-agents", "term": "Custom agents", "desc": "Agents die op maat gemaakt zijn voor een rol of workflow, met gerichte instructies en soms extra tooling.", "source": DOC_URLS["copilot_app"]},
                {"id": "agent-skills", "term": "Agent skills", "desc": "Herbruikbare vaardigheden die een agent kan oproepen voor afgebakende of terugkerende taken.", "source": DOC_URLS["agent_skills"]},
                {"id": "ai-credits", "term": "AI credits", "desc": "Verbruikseenheden voor sommige geavanceerde modellen of agentische workloads, afhankelijk van het Copilot-plan.", "source": DOC_URLS["billing"]},
            ],
        },
        {
            "title": "GitHub-basis om te starten",
            "items": [
                {"id": "repository", "term": "Repository", "desc": "De GitHub-projectruimte waar bestanden, geschiedenis en instellingen samenkomen.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "commit", "term": "Commit", "desc": "Een vastgelegde wijziging in de projectgeschiedenis.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "branch", "term": "Branch", "desc": "Een parallelle werkstroom om wijzigingen te testen voordat je ze in de hoofdbranch samenbrengt.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "pull-request", "term": "Pull Request", "desc": "Een verzoek om wijzigingen uit één branch te laten nalezen en samen te voegen in een andere.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "issue", "term": "Issue", "desc": "Een GitHub-ticket voor ideeën, bugs, taken of werkverzoeken.", "source": DOC_URLS["repo_quickstart"]},
                {"id": "github-pages", "term": "GitHub Pages", "desc": "De statische hostingdienst van GitHub om snel een site of prototype vanuit een repository te publiceren.", "source": DOC_URLS["pages_quickstart"]},
            ],
        },
        {
            "title": "Onderwijs en uitrol",
            "items": [
                {"id": "campus-program", "term": "GitHub Campus Program", "desc": "Een programma voor in aanmerking komende instellingen die GitHub-platformcapaciteit op instellingsniveau willen.", "source": DOC_URLS["campus_program"]},
            ],
        },
    ],
}

PAGE_UI = {
    "fr": {
        "glossary_title": "Glossaire",
        "glossary_sub": "Les mots qui reviennent partout sur ce site, expliqués brièvement avec une source fiable quand elle existe.",
        "sitemap_title": "Plan du site",
        "sitemap_sub": "Toutes les pages et tous les parcours de Vibe Coding Copilot, regroupés pour retrouver rapidement le bon point d’entrée.",
        "workshop_title": "Kit d’atelier « Vibe Coding Challenge »",
        "workshop_sub": "Un atelier interne de 90 à 120 minutes, prêt à animer, pour faire passer une équipe d’une idée campus à un prototype publié.",
        "certificate_title": "Certificat de parcours Vibe Coding Copilot",
        "certificate_sub": "Quand les 25 leçons sont cochées et les 3 quiz réussis, ce certificat devient imprimable en PDF ou sur papier.",
        "verified_tag": "Faits vérifiés",
        "progress_label": "Progression",
        "progress_button": "Marquer comme terminé",
        "progress_done": "Terminé",
        "quiz_status": "Quiz mémorisé dans ce navigateur",
        "certificate_cta": "Voir mon certificat",
        "certificate_name": "Ton nom",
        "certificate_name_placeholder": "Prénom Nom",
        "certificate_print": "Imprimer / Enregistrer en PDF",
        "certificate_ready": "Bravo — tous les parcours et les quiz requis sont validés dans cette langue.",
        "certificate_locked": "Termine les 25 leçons et réussis les 3 quiz de ce parcours linguistique pour déverrouiller le certificat.",
        "certificate_tracks": "Parcours validés",
        "certificate_date": "Date",
        "certificate_footer": "Certificat généré localement depuis le navigateur, sans serveur ni suivi externe.",
        "search_open": "Ouvrir la recherche",
        "search_title": "Rechercher dans le site",
        "search_placeholder": "Chercher une leçon, un cas d’usage, un terme du glossaire…",
        "search_close": "Fermer",
        "search_empty": "Aucun résultat pour cette recherche.",
        "search_hint": "Commence à taper pour filtrer les pages, leçons, scénarios, cas d’usage et termes du glossaire.",
        "workshop_print": "Imprimer ce kit d’atelier",
        "workshop_qr_label": "QR code vers la page d’accueil publiée",
        "workshop_qr_note": "Pointe vers la version publiée en ligne du site. Si tu adaptes ce kit pour une autre institution, remplace l’URL par la vôtre avant impression.",
        "workshop_qr_url": "https://sebplace.github.io/vibe-coding-copilot/fr/index.html",
        "workshop_intro": "Utilise ce déroulé pour lancer un atelier simple, concret et rassurant : montrer, faire avec, puis laisser les équipes adapter à leur rôle.",
        "workshop_sections": [
            ("10 min", "Accroche + démonstration courte", "Projette la démo Quick Poll, puis montre qu’un micro-outil utile peut naître d’un simple prompt. L’objectif est de casser l’idée qu’il faut d’abord un “grand projet”."),
            ("15 min", "Boucle conceptuelle", "Explique la boucle Idée → Construire → Publier → Améliorer en t’appuyant sur le parcours d’accueil et sur GitHub Pages comme sortie visible."),
            ("35 min", "Construction guidée en direct", "Fais construire à tout le groupe un petit outil en suivant la route navigateur de la page Ton premier commit : compte, dépôt, issue, Copilot, pull request, publication."),
            ("30 min", "Temps de fabrication par rôle ou table", "Chaque table choisit un persona ou un cas d’usage de l’Explorer / des Scénarios et tente une première version utile pour son métier."),
            ("15 min", "Partage croisé", "Chaque groupe montre ce qui fonctionne déjà, ce qui bloque encore, et la prochaine itération la plus réaliste."),
            ("10 min", "Clôture + prochaines étapes", "Renvoie vers les 3 parcours guidés, la Boîte à outils et les bonnes pratiques pour prolonger sans tout recommencer en réunion."),
        ],
        "workshop_prep_title": "Préparation facilitatrice / facilitateur",
        "workshop_prep": [
            "Ouvrir la démo Quick Poll et vérifier l’affichage sur le projecteur.",
            "Préparer un dépôt simple pour la construction guidée.",
            "Choisir 3 à 4 cas d’usage de secours depuis l’Explorer si une table bloque.",
            "Décider dès le départ si le groupe publie en public ou en privé.",
        ],
        "workshop_resources_title": "Liens à projeter ou à partager ensuite",
        "workshop_demo_title": "Démo d’ouverture réutilisable",
        "workshop_agenda_title": "Agenda prêt à imprimer",
        "sitemap_groups": [("Pages principales", "main"), ("Parcours guidés", "tracks"), ("Ressources supplémentaires", "resources")],
        "glossary_shortcuts_title": "Mots utiles pour cette page",
        "mobile_search": "Recherche",
    },
    "en": {
        "glossary_title": "Glossary",
        "glossary_sub": "Short explanations for the terms that keep appearing across the site, with a source link when one exists.",
        "sitemap_title": "Sitemap",
        "sitemap_sub": "Every page and learning path in Vibe Coding Copilot, grouped so people can find the right starting point fast.",
        "workshop_title": "“Vibe Coding Challenge” workshop kit",
        "workshop_sub": "A ready-to-run 90–120 minute internal workshop that helps a team move from a campus idea to a published prototype.",
        "certificate_title": "Vibe Coding Copilot learning certificate",
        "certificate_sub": "Once all 25 lessons are checked and all 3 quizzes are passed, this certificate becomes ready to print or save as PDF.",
        "verified_tag": "Facts checked",
        "progress_label": "Progress",
        "progress_button": "Mark as completed",
        "progress_done": "Completed",
        "quiz_status": "Quiz state is saved in this browser",
        "certificate_cta": "View my certificate",
        "certificate_name": "Your name",
        "certificate_name_placeholder": "First Last",
        "certificate_print": "Print / Save as PDF",
        "certificate_ready": "Well done — every track and required quiz is complete in this language.",
        "certificate_locked": "Complete all 25 lessons and pass the 3 quizzes in this language to unlock the certificate.",
        "certificate_tracks": "Completed tracks",
        "certificate_date": "Date",
        "certificate_footer": "Certificate generated locally in the browser, with no server-side tracking.",
        "search_open": "Open search",
        "search_title": "Search the site",
        "search_placeholder": "Search for a lesson, use case, glossary term…",
        "search_close": "Close",
        "search_empty": "No results for that search.",
        "search_hint": "Start typing to filter pages, lessons, scenarios, use cases, and glossary terms.",
        "workshop_print": "Print this workshop kit",
        "workshop_qr_label": "QR code to the published homepage",
        "workshop_qr_note": "Points to the published live site. If you adapt this kit for another institution, swap in your own URL before printing.",
        "workshop_qr_url": "https://sebplace.github.io/vibe-coding-copilot/en/index.html",
        "workshop_intro": "Use this agenda for a practical, low-drama session: show something real, build together, then let teams adapt the idea to their role.",
        "workshop_sections": [
            ("10 min", "Hook + short demo", "Project the Quick Poll demo, then show that a useful micro-tool can start from a single prompt. The goal is to lower the psychological barrier immediately."),
            ("15 min", "Concept walkthrough", "Explain the Idea → Build → Publish → Improve loop using the homepage journey and GitHub Pages as the visible destination."),
            ("35 min", "Guided build-together", "Build a tiny tool live with the whole room by following the browser-first path on the First commit page: account, repository, issue, Copilot, pull request, publish."),
            ("30 min", "Breakout build time by role/table", "Each table picks a role or scenario from the Explorer / Scenarios pages and attempts a first useful version for its own work."),
            ("15 min", "Share-out", "Each group shows what already works, what still feels fragile, and what the next realistic iteration should be."),
            ("10 min", "Wrap-up + next steps", "Point people to the three guided tracks, the Toolkit, and the Best practices page so momentum does not vanish after the workshop."),
        ],
        "workshop_prep_title": "Facilitator prep",
        "workshop_prep": [
            "Open the Quick Poll demo and verify it looks good on the projector.",
            "Prepare one simple repository for the guided build-together segment.",
            "Pick 3–4 backup use cases from the Explorer in case one table gets stuck.",
            "Decide upfront whether the group will publish publicly or privately.",
        ],
        "workshop_resources_title": "Links to project or share afterwards",
        "workshop_demo_title": "Reusable opening demo",
        "workshop_agenda_title": "Printable agenda",
        "sitemap_groups": [("Core pages", "main"), ("Learning tracks", "tracks"), ("Extra resources", "resources")],
        "glossary_shortcuts_title": "Helpful terms on this page",
        "mobile_search": "Search",
    },
    "nl": {
        "glossary_title": "Glossarium",
        "glossary_sub": "Korte definities van termen die overal op de site terugkomen, met een bronlink wanneer die bestaat.",
        "sitemap_title": "Sitemap",
        "sitemap_sub": "Alle pagina’s en leertrajecten van Vibe Coding Copilot, logisch gegroepeerd zodat je snel het juiste startpunt vindt.",
        "workshop_title": "Workshopkit “Vibe Coding Challenge”",
        "workshop_sub": "Een kant-en-klare interne workshop van 90 tot 120 minuten waarmee een team van een campusidee naar een gepubliceerd prototype gaat.",
        "certificate_title": "Vibe Coding Copilot-certificaat",
        "certificate_sub": "Zodra alle 25 lessen aangevinkt zijn en de 3 quizzen gehaald zijn, kun je dit certificaat afdrukken of als PDF bewaren.",
        "verified_tag": "Feiten gecontroleerd",
        "progress_label": "Voortgang",
        "progress_button": "Markeer als voltooid",
        "progress_done": "Voltooid",
        "quiz_status": "Quizstatus wordt in deze browser bewaard",
        "certificate_cta": "Bekijk mijn certificaat",
        "certificate_name": "Je naam",
        "certificate_name_placeholder": "Voornaam Naam",
        "certificate_print": "Afdrukken / Opslaan als PDF",
        "certificate_ready": "Goed gedaan — alle trajecten en vereiste quizzen zijn in deze taal afgerond.",
        "certificate_locked": "Werk alle 25 lessen af en slaag voor de 3 quizzen in deze taal om het certificaat te ontgrendelen.",
        "certificate_tracks": "Afgeronde trajecten",
        "certificate_date": "Datum",
        "certificate_footer": "Certificaat lokaal in de browser gegenereerd, zonder servertracking.",
        "search_open": "Zoeken openen",
        "search_title": "Zoek in de site",
        "search_placeholder": "Zoek een les, use case, term uit het glossarium…",
        "search_close": "Sluiten",
        "search_empty": "Geen resultaten voor deze zoekopdracht.",
        "search_hint": "Begin te typen om pagina’s, lessen, scenario’s, use cases en termen uit het glossarium te filteren.",
        "workshop_print": "Druk deze workshopkit af",
        "workshop_qr_label": "QR-code naar de gepubliceerde homepage",
        "workshop_qr_note": "Verwijst naar de gepubliceerde live site. Pas je dit kit aan voor een andere instelling, vervang dan de URL door jullie eigen URL vóór het afdrukken.",
        "workshop_qr_url": "https://sebplace.github.io/vibe-coding-copilot/nl/index.html",
        "workshop_intro": "Gebruik dit draaiboek voor een praktische sessie met weinig frictie: toon iets echts, bouw samen, en laat teams het daarna op hun eigen rol toepassen.",
        "workshop_sections": [
            ("10 min", "Hook + korte demo", "Projecteer de Quick Poll-demo en toon dat een bruikbare microtool uit één goede prompt kan ontstaan. Zo verlaag je meteen de drempel."),
            ("15 min", "Conceptuele walkthrough", "Leg de lus Idee → Bouwen → Publiceren → Verbeteren uit aan de hand van de journey op de homepage en GitHub Pages als zichtbare eindstap."),
            ("35 min", "Begeleid samen bouwen", "Bouw live met de hele groep een kleine tool via de browser-first route op Jouw eerste commit: account, repository, issue, Copilot, pull request, publiceren."),
            ("30 min", "Breakout-bouwtijd per rol of tafel", "Elke tafel kiest een persona of scenario uit de Explorer / Scenariopagina’s en probeert een eerste nuttige versie voor het eigen werk te maken."),
            ("15 min", "Terugkoppeling", "Elke groep deelt wat al werkt, wat nog broos is en wat de volgende realistische iteratie moet zijn."),
            ("10 min", "Afronden + volgende stappen", "Verwijs naar de drie begeleide trajecten, de Toolkit en de Best practices-pagina zodat de energie niet na de workshop verdwijnt."),
        ],
        "workshop_prep_title": "Voorbereiding voor de facilitator",
        "workshop_prep": [
            "Open de Quick Poll-demo en controleer de projectieweergave.",
            "Voorzie één eenvoudige repository voor het begeleide bouwmoment.",
            "Kies 3 à 4 reserve-use-cases uit de Explorer voor het geval een tafel vastloopt.",
            "Beslis vooraf of de groep publiek of privé publiceert.",
        ],
        "workshop_resources_title": "Links om te projecteren of nadien te delen",
        "workshop_demo_title": "Herbruikbare openingsdemo",
        "workshop_agenda_title": "Afdrukbare agenda",
        "sitemap_groups": [("Hoofdpagina’s", "main"), ("Leertrajecten", "tracks"), ("Extra bronnen", "resources")],
        "glossary_shortcuts_title": "Handige termen op deze pagina",
        "mobile_search": "Zoeken",
    },
}

LANGUAGE_NAMES = {"fr": "Français", "en": "English", "nl": "Nederlands"}

LANGUAGE_BANNER_UI = {
    "fr": {
        "prefix": "Il semble que ton navigateur préfère ",
        "cta": "Passer à cette langue",
        "dismiss": "Masquer cette suggestion",
    },
    "en": {
        "prefix": "Your browser seems to prefer ",
        "cta": "Switch to this language",
        "dismiss": "Dismiss this suggestion",
    },
    "nl": {
        "prefix": "Je browser lijkt voorkeur te hebben voor ",
        "cta": "Schakel naar deze taal",
        "dismiss": "Verberg deze suggestie",
    },
}

PROMPT_CONFIGURATOR_UI = {
    "fr": {
        "title": "Configurateur de prompt personnalisé",
        "sub": "Choisis un rôle, précise le besoin du moment, ajoute quelques contraintes, puis copie un prompt prêt à coller dans Copilot Chat.",
        "role_label": "Rôle / persona",
        "default_option": "Choisir…",
        "preset_label": "Besoin fréquent",
        "preset_default": "Choisir un besoin fréquent",
        "goal_label": "Besoin précis",
        "goal_placeholder": "Ex. préparer un quiz de révision, résumer un document, prototyper un tableau de bord…",
        "constraints_label": "Contraintes à garder en tête",
        "output_label": "Prompt prêt à coller",
        "empty": "Choisis un rôle puis précise le besoin que tu veux faire avancer.",
        "copy": "Copier le prompt",
        "copied": "Prompt copié",
        "fallback": "Prompt sélectionné — copie-le manuellement",
        "constraints": [
            "Le prototype doit rester dans le navigateur et sans backend.",
            "La réponse doit s’appuyer sur un document ou un cours existant.",
            "La proposition doit rester simple à publier sur GitHub Pages.",
            "Je veux un plan étape par étape avant toute génération de code.",
        ],
        "personas": {
            "teaching": {
                "presets": ["un quiz de révision", "une page de syllabus vivante", "un exercice interactif"],
                "surface": "Copilot Chat, GitHub Pages et Copilot Spaces",
                "instruction": "Aide-moi à construire un prototype pédagogique clair, léger et réutilisable.",
            },
            "students": {
                "presets": ["un portfolio de projet", "une appli de flashcards", "un mini MVP pour un travail de fin d’études"],
                "surface": "Copilot Chat, Mode Agent et revue de code",
                "instruction": "Aide-moi à garder le projet compréhensible, livrable et bien découpé par étapes.",
            },
            "it": {
                "presets": ["un outil interne simple", "une automatisation de ticket récurrent", "un prototype de service campus"],
                "surface": "Mode Plan, GitHub Copilot app et pull requests",
                "instruction": "Propose un flux qui garde les diffs relisibles, testables et faciles à approuver.",
            },
            "hr": {
                "presets": ["une check-list d’onboarding", "un formulaire de feedback", "une FAQ de procédures internes"],
                "surface": "Copilot Chat, Copilot Spaces et instructions de contexte",
                "instruction": "Garde les formulations alignées sur des politiques internes et sur une expérience simple pour le personnel.",
            },
            "leadership": {
                "presets": ["un tableau de bord simple", "une synthèse de KPI", "un sondage de réunion"],
                "surface": "Copilot Chat, agents personnalisés et synthèses prêtes à relire",
                "instruction": "Cherche un résultat visible rapidement, avec une lecture claire des risques et des prochaines étapes.",
            },
            "finance": {
                "presets": ["un calculateur budgétaire", "un suivi de dépenses récurrentes", "un tableau triable depuis un export"],
                "surface": "Copilot Chat, tableaux HTML et publication légère",
                "instruction": "Privilégie les calculs transparents, les hypothèses explicites et une interface sobre.",
            },
            "research": {
                "presets": ["une exploration de données de confiance", "un assistant de requêtes dataset", "un mini tableau de bord de laboratoire"],
                "surface": "Copilot Chat, MCP servers et scripts inspectables",
                "instruction": "Fais ressortir les sources, les hypothèses et les scripts que l’équipe pourra relire et rejouer.",
            },
            "campus": {
                "presets": ["une réservation de salle", "une FAQ bibliothèque", "un mini agenda d’événements"],
                "surface": "Copilot Chat, GitHub Pages et formulaires simples",
                "instruction": "Cherche un service utile tout de suite, léger à maintenir et facile à partager sur le campus.",
            },
        },
    },
    "en": {
        "title": "Personalised prompt configurator",
        "sub": "Pick a role, describe the need in front of you, add a few constraints, then copy a prompt that is ready for Copilot Chat.",
        "role_label": "Role / persona",
        "default_option": "Choose…",
        "preset_label": "Common need",
        "preset_default": "Choose a common need",
        "goal_label": "Specific need",
        "goal_placeholder": "E.g. build a revision quiz, summarise a policy document, prototype a dashboard…",
        "constraints_label": "Constraints to keep in view",
        "output_label": "Prompt ready to paste",
        "empty": "Choose a role, then describe the need you want to move forward.",
        "copy": "Copy the prompt",
        "copied": "Prompt copied",
        "fallback": "Prompt selected — copy it manually",
        "constraints": [
            "The prototype must stay browser-only, with no backend.",
            "The answer should stay grounded in an existing course or document.",
            "The result should stay easy to publish on GitHub Pages.",
            "I want a step-by-step plan before any code is generated.",
        ],
        "personas": {
            "teaching": {
                "presets": ["a revision quiz", "a live syllabus page", "an interactive practice exercise"],
                "surface": "Copilot Chat, GitHub Pages, and Copilot Spaces",
                "instruction": "Help me build a clear, lightweight, reusable teaching prototype.",
            },
            "students": {
                "presets": ["a project portfolio", "a flashcard app", "a final-project MVP"],
                "surface": "Copilot Chat, Agent mode, and code review",
                "instruction": "Help me keep the project understandable, shippable, and broken into clear steps.",
            },
            "it": {
                "presets": ["a simple internal tool", "a repeatable ticket automation", "a campus service prototype"],
                "surface": "Plan mode, the GitHub Copilot app, and pull requests",
                "instruction": "Propose a workflow that keeps diffs reviewable, testable, and safe to approve.",
            },
            "hr": {
                "presets": ["an onboarding checklist", "a training feedback form", "an internal policy FAQ"],
                "surface": "Copilot Chat, Copilot Spaces, and context instructions",
                "instruction": "Keep the wording aligned with internal policy and simple for staff to use.",
            },
            "leadership": {
                "presets": ["a lightweight dashboard", "a KPI summary", "a meeting poll"],
                "surface": "Copilot Chat, custom agents, and review-ready summaries",
                "instruction": "Aim for a visible result quickly, with a crisp read-out of risk and next steps.",
            },
            "finance": {
                "presets": ["a budget calculator", "a recurring-expense tracker", "a sortable table from an export"],
                "surface": "Copilot Chat, HTML tables, and lightweight publishing",
                "instruction": "Prefer transparent calculations, explicit assumptions, and a restrained interface.",
            },
            "research": {
                "presets": ["a trusted-data exploration", "a dataset query helper", "a lightweight lab dashboard"],
                "surface": "Copilot Chat, MCP servers, and inspectable scripts",
                "instruction": "Surface the sources, assumptions, and scripts that the team can inspect and rerun.",
            },
            "campus": {
                "presets": ["a room-booking flow", "a library FAQ", "a compact events page"],
                "surface": "Copilot Chat, GitHub Pages, and simple forms",
                "instruction": "Aim for a useful service quickly, light to maintain, and easy to share across campus.",
            },
        },
    },
    "nl": {
        "title": "Persoonlijke promptconfigurator",
        "sub": "Kies een rol, beschrijf de behoefte van dit moment, voeg enkele randvoorwaarden toe en kopieer daarna een prompt die klaarstaat voor Copilot Chat.",
        "role_label": "Rol / persona",
        "default_option": "Kies…",
        "preset_label": "Veelvoorkomende behoefte",
        "preset_default": "Kies een veelvoorkomende behoefte",
        "goal_label": "Concrete behoefte",
        "goal_placeholder": "Bijv. een herhalingsquiz bouwen, een beleidsdocument samenvatten, een dashboard prototypen…",
        "constraints_label": "Randvoorwaarden om mee te nemen",
        "output_label": "Prompt klaar om te plakken",
        "empty": "Kies een rol en beschrijf daarna de behoefte die je vooruit wilt helpen.",
        "copy": "Kopieer de prompt",
        "copied": "Prompt gekopieerd",
        "fallback": "Prompt geselecteerd — kopieer hem handmatig",
        "constraints": [
            "Het prototype moet volledig in de browser blijven, zonder backend.",
            "Het antwoord moet steunen op een bestaand document of cursusmateriaal.",
            "Het resultaat moet eenvoudig op GitHub Pages te publiceren blijven.",
            "Ik wil eerst een stappenplan zien vóór er code wordt gegenereerd.",
        ],
        "personas": {
            "teaching": {
                "presets": ["een herhalingsquiz", "een levende syllabuspagina", "een interactieve oefening"],
                "surface": "Copilot Chat, GitHub Pages en Copilot Spaces",
                "instruction": "Help me een duidelijk, licht en herbruikbaar onderwijsprototype te bouwen.",
            },
            "students": {
                "presets": ["een projectportfolio", "een flashcard-app", "een MVP voor een eindproject"],
                "surface": "Copilot Chat, Agent mode en codereview",
                "instruction": "Help me het project begrijpelijk, leverbaar en netjes in stappen op te bouwen.",
            },
            "it": {
                "presets": ["een eenvoudige interne tool", "een terugkerende ticketautomatisering", "een campusservice-prototype"],
                "surface": "Plan mode, de GitHub Copilot-app en pull requests",
                "instruction": "Stel een workflow voor die diffs reviewbaar, testbaar en veilig goed te keuren houdt.",
            },
            "hr": {
                "presets": ["een onboardingchecklist", "een feedbackformulier voor training", "een interne beleids-FAQ"],
                "surface": "Copilot Chat, Copilot Spaces en contextinstructies",
                "instruction": "Houd de formuleringen afgestemd op interne procedures en eenvoudig voor medewerkers.",
            },
            "leadership": {
                "presets": ["een licht dashboard", "een KPI-samenvatting", "een poll voor een vergadering"],
                "surface": "Copilot Chat, custom agents en samenvattingen klaar voor review",
                "instruction": "Stuur op een snel zichtbaar resultaat, met een heldere lezing van risico en volgende stap.",
            },
            "finance": {
                "presets": ["een budgetcalculator", "een tracker voor terugkerende uitgaven", "een sorteerbare tabel uit een export"],
                "surface": "Copilot Chat, HTML-tabellen en lichte publicatie",
                "instruction": "Geef voorrang aan transparante berekeningen, expliciete aannames en een sobere interface.",
            },
            "research": {
                "presets": ["een verkenning van vertrouwde data", "een dataset-queryhulp", "een compact labdashboard"],
                "surface": "Copilot Chat, MCP-servers en inspecteerbare scripts",
                "instruction": "Laat de bronnen, aannames en scripts zien die het team kan nakijken en opnieuw draaien.",
            },
            "campus": {
                "presets": ["een reservatiestroom voor ruimtes", "een bibliotheek-FAQ", "een compacte eventpagina"],
                "surface": "Copilot Chat, GitHub Pages en eenvoudige formulieren",
                "instruction": "Zoek een dienst die snel nuttig is, licht blijft in beheer en eenvoudig campusbreed te delen is.",
            },
        },
    },
}

SCENARIO_ONEPAGER_UI = {
    "fr": {
        "title": "Générer ma fiche personnalisée",
        "sub": "Choisis un rôle et un cas d’usage déjà présent sur le site. La fiche réutilise les données existantes pour fabriquer un bref imprimable en une page.",
        "persona_label": "Rôle",
        "usecase_label": "Cas d’usage",
        "default_option": "Choisir…",
        "brief_title": "Fiche prête à partager",
        "pitch_label": "Pourquoi ce rôle s’y retrouve",
        "context_label": "Situation de départ",
        "steps_label": "Étapes clés",
        "outcome_label": "Résultat attendu",
        "further_label": "Pour aller plus loin",
        "start_label": "Point de départ conseillé",
        "print": "Imprimer cette fiche",
    },
    "en": {
        "title": "Generate my one-page brief",
        "sub": "Choose a role and one existing use case from the site. The brief reuses the live site data to produce a compact printable handout.",
        "persona_label": "Role",
        "usecase_label": "Use case",
        "default_option": "Choose…",
        "brief_title": "Brief ready to share",
        "pitch_label": "Why this role cares",
        "context_label": "Starting situation",
        "steps_label": "Key steps",
        "outcome_label": "Expected outcome",
        "further_label": "Go further",
        "start_label": "Suggested starting point",
        "print": "Print this brief",
    },
    "nl": {
        "title": "Genereer mijn persoonlijke fiche",
        "sub": "Kies een rol en een bestaande use case van de site. De fiche hergebruikt de live data van de site voor een compacte afdrukbare hand-out.",
        "persona_label": "Rol",
        "usecase_label": "Use case",
        "default_option": "Kies…",
        "brief_title": "Fiche klaar om te delen",
        "pitch_label": "Waarom deze rol dit wil",
        "context_label": "Startsituatie",
        "steps_label": "Kernstappen",
        "outcome_label": "Verwachte uitkomst",
        "further_label": "Verder bouwen",
        "start_label": "Aangeraden startpunt",
        "print": "Druk deze fiche af",
    },
}

EXTRA_PAGE_CONTENT = {
    "fr": {
        "maturity": {
            "title": "Diagnostic de maturité institutionnelle",
            "sub": "Un auto-positionnement court et honnête pour choisir la prochaine page utile — sans prétendre te donner un score certifié.",
            "banner_label": "À quoi sert ce diagnostic ?",
            "banner_text": "Il aide à choisir une prochaine étape réaliste selon votre point de départ GitHub, vos premiers usages Copilot et votre niveau de cadrage interne.",
            "intro": "Répondez aux six questions ci-dessous. La recommandation finale vous orientera vers Ton premier commit, les Scénarios ou Plans & réalité selon votre contexte du moment.",
            "submit": "Voir la suggestion",
            "reset": "Recommencer le diagnostic",
            "result_title": "Suggestion de prochaine étape",
            "result_empty": "Répondez à toutes les questions pour obtenir une suggestion personnalisée.",
            "questions": [
                {
                    "id": "github",
                    "question": "Où en êtes-vous côté GitHub dans l’établissement ?",
                    "options": [
                        {"label": "Pas encore de compte ou de dépôt utilisé pour ce sujet", "value": 0},
                        {"label": "Quelques comptes individuels et un ou deux dépôts d’essai", "value": 1},
                        {"label": "Des dépôts et une organisation GitHub existent déjà pour de vrais besoins", "value": 2},
                    ],
                },
                {
                    "id": "copilot",
                    "question": "Combien de personnes utilisent déjà Copilot, même à petite échelle ?",
                    "options": [
                        {"label": "Personne ou presque", "value": 0},
                        {"label": "Une poignée de personnes pionnières", "value": 1},
                        {"label": "Une équipe ou plusieurs métiers l’utilisent déjà", "value": 2},
                    ],
                },
                {
                    "id": "budget",
                    "question": "Le sujet a-t-il déjà une ligne budgétaire ou un mandat explicite ?",
                    "options": [
                        {"label": "Non, on explore encore", "value": 0},
                        {"label": "Une enveloppe ou un sponsor est en discussion", "value": 1},
                        {"label": "Oui, le budget ou le mandat est identifié", "value": 2},
                    ],
                },
                {
                    "id": "need",
                    "question": "Le besoin principal aujourd’hui est plutôt…",
                    "options": [
                        {"label": "Pédagogique / lié à l’apprentissage", "value": 0},
                        {"label": "Opérationnel / IT / support", "value": 1},
                        {"label": "Les deux à la fois", "value": 2},
                    ],
                },
                {
                    "id": "buyin",
                    "question": "Avez-vous encore besoin de convaincre en interne avec des exemples très concrets ?",
                    "options": [
                        {"label": "Oui, il faut d’abord montrer des cas parlants", "value": 2},
                        {"label": "Un peu, mais un petit pilote existe déjà", "value": 1},
                        {"label": "Non, le sujet est déjà pris au sérieux", "value": 0},
                    ],
                },
                {
                    "id": "governance",
                    "question": "Vos contenus, procédures ou données sont-ils déjà assez cadrés pour guider Copilot ?",
                    "options": [
                        {"label": "Pas encore, tout est dispersé", "value": 0},
                        {"label": "Partiellement : quelques documents et règles existent", "value": 1},
                        {"label": "Oui : documents, politiques ou sources de vérité sont identifiés", "value": 2},
                    ],
                },
            ],
            "outcomes": {
                "first_commit": {
                    "title": "Commence par Ton premier commit",
                    "body": "Votre meilleure prochaine étape est de faire vivre un premier petit flux complet : compte GitHub, dépôt, Copilot, pull request et publication simple.",
                    "bullets": [
                        "Utile si les bases GitHub ne sont pas encore partagées.",
                        "Rassure très vite les personnes non techniques.",
                        "Donne un langage commun avant de parler plan ou gouvernance.",
                    ],
                    "page": "first_commit",
                    "cta": "Ouvrir Ton premier commit",
                },
                "scenarios": {
                    "title": "Explore d’abord les scénarios",
                    "body": "Vous avez surtout besoin d’exemples crédibles pour créer l’adhésion. La page Scénarios vous donne des démonstrateurs déjà racontés par rôle.",
                    "bullets": [
                        "Pratique pour un comité, un atelier ou une réunion de cadrage.",
                        "Aide à choisir un premier pilote qui parle aux métiers.",
                        "Évite de bloquer trop tôt sur les questions d’outillage.",
                    ],
                    "page": "scenarios",
                    "cta": "Voir les scénarios",
                },
                "plans": {
                    "title": "Passe à Plans & réalité",
                    "body": "Votre contexte ressemble déjà à une conversation de déploiement : budgets, gouvernance, usages existants et arbitrages institutionnels comptent maintenant plus qu’une simple démo.",
                    "bullets": [
                        "Utile si plusieurs métiers sont déjà concernés.",
                        "Aide à cadrer Business / Enterprise, AI credits et routes gratuites.",
                        "Donne une base plus honnête pour parler achat, sécurité et pilotage.",
                    ],
                    "page": "plans",
                    "cta": "Voir Plans & réalité",
                },
            },
        },
        "quick_reference": {
            "title": "Repère en 2 minutes",
            "sub": "La page courte et orientée pour comprendre ce que contient ce site et choisir le prochain clic utile.",
            "intro": "Vibe Coding Copilot est un site statique trilingue pour les personnes qui enseignent, étudient, soutiennent ou pilotent l’enseignement supérieur et qui veulent utiliser GitHub Copilot sans jargon inutile. Si tu viens d’arriver, cette page te montre ce que le site offre déjà et quel premier détour vaut vraiment ton temps.",
            "situations_title": "Choisis ta situation",
            "situations_sub": "Un besoin, un meilleur prochain clic.",
            "situations": [
                {"icon": "⚡", "title": "Je veux essayer Copilot tout de suite", "desc": "Pas d’installation, pas de dépôt local : teste un vrai prompt dans le navigateur.", "href": "https://github.com/copilot", "cta": "Ouvrir github.com/copilot"},
                {"icon": "🧭", "title": "Je ne sais pas encore par où commencer", "desc": "Le diagnostic de maturité te renvoie vers la page la plus utile selon ton contexte du moment.", "page": "maturity", "cta": "Faire le diagnostic"},
                {"icon": "🪜", "title": "Je veux apprendre pas à pas", "desc": "Le parcours Basics part du premier prompt et va jusqu’à la publication d’une première application.", "page": "basics", "cta": "Ouvrir le parcours Débutant"},
                {"icon": "🎭", "title": "Je veux des exemples crédibles à montrer", "desc": "Les huit scénarios servent bien en démo, en atelier ou pour amorcer une discussion interne.", "page": "scenarios", "cta": "Voir les scénarios"},
                {"icon": "🧑‍🏫", "title": "Je veux animer un atelier interne", "desc": "Le kit d’atelier donne l’agenda, la démo d’ouverture et les ressources à projeter.", "page": "workshop", "cta": "Ouvrir le kit d’atelier"},
            ],
            "search_label": "Mot précis ?",
            "search_before": "Ouvre le",
            "search_after": "ou utilise l’icône de recherche dans l’en-tête pour retrouver une fonctionnalité ou une page.",
            "overview_title": "Tout ce que contient déjà le site en un coup d’œil",
            "overview_sub": "Ces repères viennent directement de la page d’accueil actuelle.",
            "sitemap_label": "Tout voir ?",
            "sitemap_before": "Pour la liste exhaustive de toutes les pages, leçons et ressources, ouvre le",
            "sitemap_after": ".",
        },
        "changelog": {
            "title": "Historique du site",
            "sub": "Les principales vagues d’évolution de ce site lui-même, regroupées par phase d’août 2026 pour éviter une fausse précision au jour près.",
            "banner_label": "À propos de cette page",
            "banner_text": "Elle documente l’évolution du contenu du site, en complément des bandeaux “Faits vérifiés” qui concernent les réalités GitHub Copilot sous-jacentes.",
            "entries": [
                {
                    "date": "Fin août 2026",
                    "title": "SEO technique, impressions et outils personnalisés",
                    "summary": "Ajout de sitemap.xml, robots.txt, hreflang, d’un configurateur de prompt, d’un diagnostic de maturité, d’une fiche personnalisée générée depuis les cas d’usage, d’une bannière de suggestion de langue et de cette page d’historique.",
                    "links": [("toolkit", "Boîte à outils"), ("maturity", "Diagnostic"), ("scenarios", "Fiche personnalisée"), ("changelog", "Historique")],
                },
                {
                    "date": "Mi-août 2026",
                    "title": "Glossaire, plan du site, certificat, kit d’atelier et recherche globale",
                    "summary": "Le site a reçu un glossaire sourcé, un plan du site, un certificat imprimable, un kit d’atelier, une recherche transversale, un favicon, des métadonnées OG/Twitter et un skip-link accessible.",
                    "links": [("glossary", "Glossaire"), ("sitemap", "Plan du site"), ("certificate", "Certificat"), ("workshop", "Kit d’atelier")],
                },
                {
                    "date": "Mi-août 2026",
                    "title": "Approfondissement des contenus d’aide à la décision",
                    "summary": "Ajout du guide Ton premier commit, de Construire ou acheter, du comparatif Plans & réalité et de l’Explorer étendu à 36 cas d’usage filtrables.",
                    "links": [("first_commit", "Ton premier commit"), ("build_vs_buy", "Construire ou acheter"), ("plans", "Plans & réalité"), ("explorer", "Explorer")],
                },
                {
                    "date": "Début août 2026",
                    "title": "Lancement structurant du site",
                    "summary": "Publication initiale de la page d’accueil, des trois parcours avec quiz, des huit scénarios, des bonnes pratiques et de la page À propos pour ancrer le projet.",
                    "links": [("home", "Accueil"), ("basics", "Parcours"), ("scenarios", "Scénarios"), ("best_practices", "Bonnes pratiques"), ("about", "À propos")],
                },
            ],
        },
    },
    "en": {
        "maturity": {
            "title": "Institutional maturity diagnostic",
            "sub": "A short, honest self-check that points you to the next useful page — not a fake certified score.",
            "banner_label": "What this diagnostic does",
            "banner_text": "It helps you choose a realistic next step based on your GitHub starting point, your first Copilot usage, and your current level of internal alignment.",
            "intro": "Answer the six questions below. The final recommendation will point you to First commit, Scenarios, or Plans & reality depending on your current context.",
            "submit": "See the recommendation",
            "reset": "Restart the diagnostic",
            "result_title": "Suggested next step",
            "result_empty": "Answer all six questions to get a personalised suggestion.",
            "questions": [
                {
                    "id": "github",
                    "question": "Where are you today on the GitHub side?",
                    "options": [
                        {"label": "No account or repository is in active use for this work yet", "value": 0},
                        {"label": "A few individual accounts and one or two trial repositories exist", "value": 1},
                        {"label": "Real repositories and a GitHub organisation already support live work", "value": 2},
                    ],
                },
                {
                    "id": "copilot",
                    "question": "How many people already use Copilot, even informally?",
                    "options": [
                        {"label": "Nobody or almost nobody yet", "value": 0},
                        {"label": "A handful of pioneers", "value": 1},
                        {"label": "A team or several roles already use it", "value": 2},
                    ],
                },
                {
                    "id": "budget",
                    "question": "Is there already a budget line or explicit mandate behind this topic?",
                    "options": [
                        {"label": "No, we are still exploring", "value": 0},
                        {"label": "A sponsor or budget line is being discussed", "value": 1},
                        {"label": "Yes, budget or mandate is identified", "value": 2},
                    ],
                },
                {
                    "id": "need",
                    "question": "Your main need today is mostly…",
                    "options": [
                        {"label": "Teaching / learning", "value": 0},
                        {"label": "Operations / IT / support", "value": 1},
                        {"label": "Both at once", "value": 2},
                    ],
                },
                {
                    "id": "buyin",
                    "question": "Do you still need concrete examples to build internal buy-in?",
                    "options": [
                        {"label": "Yes, visible examples come first", "value": 2},
                        {"label": "Somewhat, but a small pilot already exists", "value": 1},
                        {"label": "No, the topic is already taken seriously", "value": 0},
                    ],
                },
                {
                    "id": "governance",
                    "question": "Are your documents, procedures, or trusted data already structured enough to guide Copilot?",
                    "options": [
                        {"label": "Not yet, the material is still scattered", "value": 0},
                        {"label": "Partly: a few documents and rules already exist", "value": 1},
                        {"label": "Yes: policies, documents, or source-of-truth systems are identified", "value": 2},
                    ],
                },
            ],
            "outcomes": {
                "first_commit": {
                    "title": "Start with First commit",
                    "body": "Your strongest next move is to experience one small complete loop: GitHub account, repository, Copilot, pull request, and a lightweight publish step.",
                    "bullets": [
                        "Best when GitHub basics are not yet shared knowledge.",
                        "Reassures non-technical colleagues quickly.",
                        "Creates a common language before plan, policy, or rollout conversations.",
                    ],
                    "page": "first_commit",
                    "cta": "Open First commit",
                },
                "scenarios": {
                    "title": "Explore the scenarios first",
                    "body": "You mainly need believable examples to create momentum. The scenarios page gives you role-based demo stories that already sound like real work.",
                    "bullets": [
                        "Useful for committees, workshops, and framing meetings.",
                        "Helps you pick a first pilot that resonates with the business side.",
                        "Stops the conversation from getting stuck too early in tooling details.",
                    ],
                    "page": "scenarios",
                    "cta": "View the scenarios",
                },
                "plans": {
                    "title": "Move to Plans & reality",
                    "body": "Your context already looks like a rollout conversation: budgets, governance, existing usage, and institutional trade-offs matter more now than a first demo alone.",
                    "bullets": [
                        "Useful when several roles are already involved.",
                        "Helps frame Business / Enterprise, AI credits, and education free routes.",
                        "Gives a more honest base for security, purchasing, and governance discussions.",
                    ],
                    "page": "plans",
                    "cta": "Open Plans & reality",
                },
            },
        },
        "quick_reference": {
            "title": "2-minute guide",
            "sub": "The short, opinionated page for understanding what this site offers and choosing the next useful click.",
            "intro": "Vibe Coding Copilot is a trilingual static site for people who teach, study, support, or lead in higher education and want to use GitHub Copilot without unnecessary jargon. If you just landed here, this page shows what the site already contains and where your time is best spent first.",
            "situations_title": "Pick your situation",
            "situations_sub": "One need, one best next click.",
            "situations": [
                {"icon": "⚡", "title": "I want to try Copilot right now", "desc": "No install and no local repository yet: test a real prompt in the browser first.", "href": "https://github.com/copilot", "cta": "Open github.com/copilot"},
                {"icon": "🧭", "title": "I am not sure where we should start", "desc": "The maturity diagnostic points you to the most useful next page for your current context.", "page": "maturity", "cta": "Take the diagnostic"},
                {"icon": "🪜", "title": "I want to learn step by step", "desc": "The Basics track starts with the first prompt and ends with publishing a first working app.", "page": "basics", "cta": "Open the Beginner track"},
                {"icon": "🎭", "title": "I need credible examples to show others", "desc": "The eight scenarios work well for demos, workshops, and early internal conversations.", "page": "scenarios", "cta": "See the scenarios"},
                {"icon": "🧑‍🏫", "title": "I want to run an internal workshop", "desc": "The workshop kit gives you the agenda, opening demo, and projector-ready follow-up links.", "page": "workshop", "cta": "Open the workshop kit"},
            ],
            "search_label": "Need one precise term?",
            "search_before": "Open the",
            "search_after": "or use the search icon in the header to jump to a feature or page fast.",
            "overview_title": "Everything already on the site at a glance",
            "overview_sub": "These reference points come directly from the live homepage.",
            "sitemap_label": "Want the full list?",
            "sitemap_before": "For the exhaustive list of every page, lesson, and extra resource, open the",
            "sitemap_after": ".",
        },
        "changelog": {
            "title": "Site changelog",
            "sub": "The main waves of change in this site itself, grouped into August 2026 phases rather than pretending to be exact to the day.",
            "banner_label": "About this page",
            "banner_text": "It tracks how the site content evolved, complementing the separate “Facts checked” banners that cover GitHub Copilot realities underneath.",
            "entries": [
                {
                    "date": "Late August 2026",
                    "title": "Technical SEO, print views, and personalised tools",
                    "summary": "Added sitemap.xml, robots.txt, hreflang, a prompt configurator, a maturity diagnostic, a generated one-page brief, a browser-language suggestion banner, and this changelog page.",
                    "links": [("toolkit", "Toolkit"), ("maturity", "Diagnostic"), ("scenarios", "One-page brief"), ("changelog", "Changelog")],
                },
                {
                    "date": "Mid August 2026",
                    "title": "Glossary, sitemap, certificate, workshop kit, and global search",
                    "summary": "The site gained a sourced glossary, a sitemap page, a printable certificate, a workshop kit, full-site search, a favicon, OG/Twitter tags, and an accessible skip link.",
                    "links": [("glossary", "Glossary"), ("sitemap", "Sitemap"), ("certificate", "Certificate"), ("workshop", "Workshop kit")],
                },
                {
                    "date": "Mid August 2026",
                    "title": "Decision-support content expansion",
                    "summary": "Added the First commit guide, Build vs buy, the Plans & reality comparison, and the Explorer expanded to 36 filterable use cases.",
                    "links": [("first_commit", "First commit"), ("build_vs_buy", "Build vs buy"), ("plans", "Plans & reality"), ("explorer", "Explorer")],
                },
                {
                    "date": "Early August 2026",
                    "title": "Initial structured launch",
                    "summary": "Published the home page, the three learning tracks with quizzes, the eight scenarios, the best-practices page, and the About page as the core teaching spine.",
                    "links": [("home", "Home"), ("basics", "Tracks"), ("scenarios", "Scenarios"), ("best_practices", "Best practices"), ("about", "About")],
                },
            ],
        },
    },
    "nl": {
        "maturity": {
            "title": "Diagnose van institutionele maturiteit",
            "sub": "Een korte, eerlijke zelfscan die je naar de nuttigste volgende pagina stuurt — niet naar een kunstmatige certificeerbare score.",
            "banner_label": "Waarvoor dient deze diagnose?",
            "banner_text": "Ze helpt je een realistische volgende stap te kiezen op basis van je GitHub-startpunt, je eerste Copilot-gebruik en je huidige interne afstemming.",
            "intro": "Beantwoord de zes vragen hieronder. De eindaanbeveling verwijst je naar Jouw eerste commit, Scenarios of Plannen & realiteit, afhankelijk van je situatie van vandaag.",
            "submit": "Bekijk de aanbeveling",
            "reset": "Herstart de diagnose",
            "result_title": "Aangeraden volgende stap",
            "result_empty": "Beantwoord alle zes vragen om een persoonlijke suggestie te krijgen.",
            "questions": [
                {
                    "id": "github",
                    "question": "Waar sta je vandaag aan de GitHub-kant?",
                    "options": [
                        {"label": "Nog geen account of repository in actief gebruik voor dit werk", "value": 0},
                        {"label": "Een paar individuele accounts en één of twee proefrepositories", "value": 1},
                        {"label": "Er zijn al echte repositories en een GitHub-organisatie voor live werk", "value": 2},
                    ],
                },
                {
                    "id": "copilot",
                    "question": "Hoeveel mensen gebruiken Copilot al, al is het informeel?",
                    "options": [
                        {"label": "Niemand of bijna niemand nog", "value": 0},
                        {"label": "Een handvol pioniers", "value": 1},
                        {"label": "Een team of meerdere rollen gebruiken het al", "value": 2},
                    ],
                },
                {
                    "id": "budget",
                    "question": "Is er al een budgetlijn of expliciet mandaat voor dit onderwerp?",
                    "options": [
                        {"label": "Nee, we verkennen nog", "value": 0},
                        {"label": "Een sponsor of budgetlijn wordt besproken", "value": 1},
                        {"label": "Ja, budget of mandaat is geïdentificeerd", "value": 2},
                    ],
                },
                {
                    "id": "need",
                    "question": "Je belangrijkste behoefte vandaag is vooral…",
                    "options": [
                        {"label": "Onderwijs / leren", "value": 0},
                        {"label": "Operaties / IT / support", "value": 1},
                        {"label": "Beide tegelijk", "value": 2},
                    ],
                },
                {
                    "id": "buyin",
                    "question": "Heb je nog concrete voorbeelden nodig om intern draagvlak op te bouwen?",
                    "options": [
                        {"label": "Ja, eerst zichtbare voorbeelden", "value": 2},
                        {"label": "Gedeeltelijk, maar er bestaat al een kleine pilot", "value": 1},
                        {"label": "Nee, het onderwerp wordt al ernstig genomen", "value": 0},
                    ],
                },
                {
                    "id": "governance",
                    "question": "Zijn je documenten, procedures of vertrouwde data al voldoende gestructureerd om Copilot te sturen?",
                    "options": [
                        {"label": "Nog niet, alles zit nog verspreid", "value": 0},
                        {"label": "Gedeeltelijk: enkele documenten en regels bestaan al", "value": 1},
                        {"label": "Ja: beleid, documenten of bronsystemen zijn aangeduid", "value": 2},
                    ],
                },
            ],
            "outcomes": {
                "first_commit": {
                    "title": "Start met Jouw eerste commit",
                    "body": "Je sterkste volgende stap is één kleine volledige lus beleven: GitHub-account, repository, Copilot, pull request en lichte publicatie.",
                    "bullets": [
                        "Best wanneer GitHub-basiskennis nog niet gedeeld is.",
                        "Stelt niet-technische collega’s snel gerust.",
                        "Creëert een gemeenschappelijke taal vóór plan-, beleid- of uitrolgesprekken.",
                    ],
                    "page": "first_commit",
                    "cta": "Open Jouw eerste commit",
                },
                "scenarios": {
                    "title": "Verken eerst de scenario’s",
                    "body": "Je hebt vooral geloofwaardige voorbeelden nodig om beweging te creëren. De scenariopagina geeft je rolgerichte demoverhalen die al als echt werk klinken.",
                    "bullets": [
                        "Handig voor commissies, workshops en kadergesprekken.",
                        "Helpt een eerste pilot te kiezen die voor de businesszijde herkenbaar is.",
                        "Voorkomt dat het gesprek te vroeg vastloopt op tooldetails.",
                    ],
                    "page": "scenarios",
                    "cta": "Bekijk de scenario’s",
                },
                "plans": {
                    "title": "Ga naar Plannen & realiteit",
                    "body": "Je context lijkt al op een uitrolgesprek: budget, governance, bestaand gebruik en institutionele afwegingen wegen nu zwaarder dan alleen een eerste demo.",
                    "bullets": [
                        "Nuttig wanneer al meerdere rollen betrokken zijn.",
                        "Helpt Business / Enterprise, AI credits en onderwijsroutes te kaderen.",
                        "Geeft een eerlijkere basis voor beveiliging, aankoop en governance.",
                    ],
                    "page": "plans",
                    "cta": "Open Plannen & realiteit",
                },
            },
        },
        "quick_reference": {
            "title": "Wegwijzer in 2 minuten",
            "sub": "De korte, sturende pagina om te begrijpen wat deze site bevat en welke volgende klik het nuttigst is.",
            "intro": "Vibe Coding Copilot is een drietalige statische site voor mensen die lesgeven, studeren, ondersteunen of leiding geven in het hoger onderwijs en GitHub Copilot zonder overbodig jargon willen gebruiken. Als je hier net bent aangekomen, toont deze pagina wat de site al biedt en waar je best eerst naartoe gaat.",
            "situations_title": "Kies je situatie",
            "situations_sub": "Eén nood, één beste volgende klik.",
            "situations": [
                {"icon": "⚡", "title": "Ik wil Copilot meteen proberen", "desc": "Geen installatie en nog geen lokale repository nodig: test eerst een echte prompt in de browser.", "href": "https://github.com/copilot", "cta": "Open github.com/copilot"},
                {"icon": "🧭", "title": "Ik weet nog niet waar we moeten starten", "desc": "De maturiteitsdiagnose stuurt je naar de nuttigste volgende pagina voor jullie huidige context.", "page": "maturity", "cta": "Doe de diagnose"},
                {"icon": "🪜", "title": "Ik wil stap voor stap leren", "desc": "Het Basics-traject begint bij de eerste prompt en eindigt bij het publiceren van een eerste werkende app.", "page": "basics", "cta": "Open het Beginnerstraject"},
                {"icon": "🎭", "title": "Ik heb geloofwaardige voorbeelden nodig", "desc": "De acht scenario’s werken goed voor demo’s, workshops en eerste interne gesprekken.", "page": "scenarios", "cta": "Bekijk de scenario’s"},
                {"icon": "🧑‍🏫", "title": "Ik wil een interne workshop begeleiden", "desc": "De workshopkit geeft je het agendaformat, de openingsdemo en de links om te projecteren.", "page": "workshop", "cta": "Open de workshopkit"},
            ],
            "search_label": "Eén precies begrip nodig?",
            "search_before": "Open het",
            "search_after": "of gebruik het zoekicoon in de header om snel naar een feature of pagina te springen.",
            "overview_title": "Alles wat al op de site staat in één oogopslag",
            "overview_sub": "Deze referentiepunten komen rechtstreeks van de huidige homepage.",
            "sitemap_label": "Alles zien?",
            "sitemap_before": "Open voor de volledige lijst van alle pagina’s, lessen en extra bronnen de",
            "sitemap_after": ".",
        },
        "changelog": {
            "title": "Sitechangelog",
            "sub": "De belangrijkste evolutiegolven van deze site zelf, gegroepeerd in fases van augustus 2026 in plaats van kunstmatig exact per dag te doen.",
            "banner_label": "Over deze pagina",
            "banner_text": "Ze volgt hoe de site-inhoud evolueerde, als aanvulling op de aparte “Feiten gecontroleerd”-banners over de onderliggende GitHub Copilot-realiteit.",
            "entries": [
                {
                    "date": "Eind augustus 2026",
                    "title": "Technische SEO, printweergaven en persoonlijke tools",
                    "summary": "Toegevoegd: sitemap.xml, robots.txt, hreflang, een promptconfigurator, een maturiteitsdiagnose, een gegenereerde one-pager, een browsertaalsuggestie en deze changelogpagina.",
                    "links": [("toolkit", "Toolkit"), ("maturity", "Diagnose"), ("scenarios", "One-pager"), ("changelog", "Changelog")],
                },
                {
                    "date": "Midden augustus 2026",
                    "title": "Glossarium, sitemap, certificaat, workshopkit en globale zoekfunctie",
                    "summary": "De site kreeg een onderbouwd glossarium, een sitemap-pagina, een afdrukbaar certificaat, een workshopkit, sitebrede zoekfunctie, een favicon, OG/Twitter-tags en een toegankelijke skip-link.",
                    "links": [("glossary", "Glossarium"), ("sitemap", "Sitemap"), ("certificate", "Certificaat"), ("workshop", "Workshopkit")],
                },
                {
                    "date": "Midden augustus 2026",
                    "title": "Uitbreiding van beslissingsondersteunende inhoud",
                    "summary": "Toegevoegd: de gids Jouw eerste commit, Bouwen of kopen, de vergelijking Plannen & realiteit en de Explorer met 36 filterbare use cases.",
                    "links": [("first_commit", "Jouw eerste commit"), ("build_vs_buy", "Bouwen of kopen"), ("plans", "Plannen & realiteit"), ("explorer", "Explorer")],
                },
                {
                    "date": "Begin augustus 2026",
                    "title": "Eerste gestructureerde lancering",
                    "summary": "Publicatie van de homepage, de drie leertrajecten met quizzen, de acht scenario’s, de Best practices-pagina en de Over-pagina als kern van het leerpad.",
                    "links": [("home", "Home"), ("basics", "Trajecten"), ("scenarios", "Scenario’s"), ("best_practices", "Best practices"), ("about", "Over")],
                },
            ],
        },
    },
}

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Vibe Coding Copilot">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a371f7"/>
      <stop offset="100%" stop-color="#58a6ff"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="18" fill="#0d1117"/>
  <rect x="5" y="5" width="54" height="54" rx="16" fill="url(#g)" opacity=".18"/>
  <path fill="#e6edf3" d="M32 8a24 24 0 0 0-7.59 46.77c1.2.21 1.65-.51 1.65-1.14l-.03-4.47c-6.03 1.32-7.29-2.91-7.29-2.91-.98-2.49-2.4-3.15-2.4-3.15-1.98-1.35.15-1.32.15-1.32 2.16.15 3.3 2.22 3.3 2.22 1.92 3.3 5.04 2.34 6.27 1.8.21-1.38.75-2.34 1.38-2.88-4.8-.54-9.87-2.4-9.87-10.71 0-2.37.84-4.29 2.22-5.79-.21-.54-.96-2.76.21-5.76 0 0 1.83-.57 5.97 2.22a20.7 20.7 0 0 1 10.89 0c4.14-2.79 5.97-2.22 5.97-2.22 1.17 3 .42 5.22.21 5.76 1.38 1.5 2.22 3.42 2.22 5.79 0 8.34-5.07 10.17-9.9 10.68.78.66 1.47 1.98 1.47 3.99l-.03 5.91c0 .63.42 1.35 1.65 1.14A24 24 0 0 0 32 8Z"/>
</svg>
"""


CONTENT_UPDATES = {
    "en": {
        "nav": {
            "plans": "Plans & reality",
            "scenarios": "8 real scenarios",
            "courses_menu": "Learning tracks",
            "mobile_group_learn": "Learn",
            "mobile_group_resources": "Resources",
            "mobile_group_tools": "Tools",
        },
        "home": {
            "cta_primary": "Browse 8 real scenarios",
            "cta_primary_page": "scenarios",
            "cta_secondary": "Compare plans & free entry points",
            "cta_secondary_page": "plans",
            "cta_tertiary": "Start the guided track",
            "cta_tertiary_page": "basics",
            "hero_note": "Start today on github.com/copilot, then choose the path that fits your role: student, teaching staff, IT, HR, leadership, finance, research, or library/campus teams.",
            "journey_title": "From a real campus problem to a published app",
            "journey_sub": "The same practical loop works across teaching, operations, support, and research.",
            "courses_sub": "Use the guided tracks to build the habit, then adapt the workflow to your own faculty, service, lab, library, or programme.",
            "scenario_section_title": "A few scenarios to make it concrete",
            "scenario_section_sub": "The scenarios page expands into eight detailed walkthroughs. Start here with four quick role-based glimpses, then open the full playbook for the step-by-step version.",
            "scenario_section_cta": "See all 8 complete scenarios",
            "start_free_title": "How to start today",
            "start_free_sub": "Pick the doorway that removes your current blocker: setup, first practice, or understanding who still qualifies for a free route.",
            "impact_stats": [
                {"value": 26, "label": "filterable use cases", "desc": "Across eight higher-education roles"},
                {"value": 25, "label": "guided lessons", "desc": "From first prompt to published app"},
                {"value": 8, "label": "flagship scenarios", "desc": "Teacher to library, all grounded in real features"},
                {"value": 5, "label": "individual plans", "desc": "Free, Student, Pro, Pro+, and Max"},
            ],
            "hero_visual": {
                "title": "From prompt to prototype",
                "badges": ["Chat", "Spaces", "Agent mode", "GitHub Pages"],
                "lines": [
                    "Open github.com/copilot",
                    "Describe a real campus problem",
                    "Let Copilot scaffold the first version",
                    "Publish the result on GitHub Pages",
                ],
            },
            "start_free_cards": [
                {
                    "icon": "🧪",
                    "title": "Start with your first commit",
                    "desc": "The guided beginner page takes you from GitHub account to first repository and explains the browser, CLI, and Desktop paths — plus where the student and teacher free routes fit.",
                    "cta": "Follow the guided page",
                    "page": "first_commit",
                    "badge": "Start here",
                    "featured": True,
                },
                {
                    "icon": "⚡",
                    "title": "Try Copilot in the browser",
                    "desc": "Need a zero-install first look? Open Copilot Chat on github.com/copilot and test a real prompt before touching any local setup.",
                    "cta": "Open github.com/copilot",
                    "href": "https://github.com/copilot",
                },
                {
                    "icon": "🎓",
                    "title": "Check the free routes",
                    "desc": "See who still starts free in 2026: Copilot Student for verified students, free Copilot Pro for verified teachers, and where paid rollout begins for everyone else.",
                    "cta": "See plans & reality",
                    "page": "plans",
                },
            ],
            "start_free_links_label": "Then keep going with",
            "start_free_links": [
                {"label": "36 concrete use cases", "page": "explorer"},
                {"label": "Build vs buy", "page": "build_vs_buy"},
            ],
            "scenario_teaser_ids": ["teacher", "student", "it", "leadership"],
            "scenario_examples_label": "Four more ideas from other roles",
        },
        "home_personas": [
            ("🎓", "Teaching staff", "Build the course companion, quiz, revision page, or grading helper you have wanted for years.", "Example:", "A chemistry lecturer ships a grounded revision microsite before next week’s lab."),
            ("🧑‍🎓", "Students", "Turn a final-year idea into a working prototype branch by branch, with Copilot reviewing the code before hand-in.", "Example:", "A student team builds a lab-booking prototype instead of handing in a static mock-up."),
            ("🖥️", "IT & digital services", "Run multiple agent sessions in parallel, keep control in Plan mode, and review diffs before anything ships.", "Example:", "IT clears three backlog tickets in parallel with the GitHub Copilot app."),
            ("🤝", "HR & people operations", "Ground Copilot on real procedures, templates, and onboarding material so the answers stay policy-aware.", "Example:", "HR turns policy PDFs into a searchable onboarding assistant without hand-coding a backend."),
            ("🧭", "Leadership & management", "Automate weekly synthesis work with custom agents and scheduled cloud-agent runs.", "Example:", "A dean receives one PR-ready KPI summary every Friday instead of chasing updates all morning."),
            ("💶", "Finance & administration", "Turn exports into dashboards fast, while keeping cost visibility honest through pooled AI credits.", "Example:", "Finance converts a monthly budget export into a one-page variance dashboard in minutes."),
            ("🔬", "Research", "Connect trusted data through MCP and let Copilot draft the Python or R analysis you can inspect and rerun.", "Example:", "A research team queries retention data in plain language, then receives the notebook behind the chart."),
            ("📚", "Library, campus & student services", "Build lightweight room-booking, inventory, FAQ, or events tools without waiting for a full custom project.", "Example:", "Library staff publish a small room-booking app on GitHub Pages for the semester launch."),
        ],
        "home_examples": [
            ("Onboarding question hub", "A policy-grounded assistant for recurring staff questions.", "HR"),
            ("Budget variance dashboard", "A one-page dashboard from an Excel or CSV export.", "Finance"),
            ("Dataset query assistant", "Plain-language questions over trusted data, with the script behind the answer.", "Research"),
            ("Library room-booking prototype", "A lightweight GitHub Pages service page for rooms, slots, and accessibility notes.", "Library & campus services"),
        ],
        "best_practices": {
            "title": "Best practices",
            "sub": "A one-page checklist to start strong, stay factual, and keep your rollout realistic from first prompt to institutional adoption.",
            "items": [
                ("Start from a real campus problem", "The best app ideas come from repetitive work, bottlenecks, or missed opportunities that staff or students feel every week."),
                ("Start tiny, then iterate", "A small page that works and ships beats a grand concept that never reaches users."),
                ("One change, one test, one commit", "Small steps make it obvious what changed, what broke, and what to roll back."),
                ("Save everything on GitHub from day one", "Even a tiny prototype deserves version history, backup, and a straightforward publishing path."),
                ("Check your actual entitlement early", "Students can apply for Copilot Student, verified teachers can apply for free Copilot Pro, and broader staff rollout means paid Business or Enterprise."),
                ("Ground Copilot before trusting the answer", "Spaces, custom instructions, prompt files, or MCP servers help Copilot stay close to your institution’s real documents and data."),
                ("Use .github/copilot-instructions.md", "Write the conventions, build steps, and style rules you repeat every session so Copilot stops guessing."),
                ("Keep secrets and personal data out of the browser", "API keys belong in protected secrets, and student or staff data needs privacy-aware design from the start."),
                ("Review every suggestion before accepting it", "Copilot proposes. You approve, reject, or reshape the change."),
                ("Keep custom instructions short and concrete", "A few precise rules Copilot actually follows beat a long document it skims. State conventions, not philosophy."),
                ("Keep a short trace of what an agent changed", "A one-line note per agent session — what changed, why, what to check — saves real time when several people share the same repository."),
            ],
        },
        "about": {
            "title": "About this track",
            "paragraphs": [
                "Vibe Coding Copilot is an independent, free learning resource for higher education: teaching staff, students, IT and digital services, HR, leadership, finance, researchers, and campus or library teams who want to build practical tools with GitHub Copilot and GitHub.",
                "This site is not affiliated with, endorsed by, or sponsored by GitHub or Microsoft. Its job is to help institutions make realistic, evidence-based adoption decisions — including where the free routes end and paid organisational rollout begins.",
            ],
            "sections": [
                ("Why this track exists", [
                    "Too many good ideas stay trapped behind a queue, a budget line, or the phrase “we need a full project for that”. Vibe coding lowers that barrier by turning domain expertise into working prototypes and small apps."
                ]),
                ("Why GitHub specifically", [
                    "GitHub gives the second half of the story: repositories, branches, pull requests, GitHub Pages, and a native home for Copilot. The GitHub Campus Program can even provide GitHub Enterprise Cloud or Server to the institution, but that platform access is not the same thing as free Copilot seats for every staff role."
                ]),
                ("The honest rollout reality in 2026", [
                    "Students can still get Copilot Student for free. Verified teachers can still get Copilot Pro for free individually. But institution-wide rollout for IT, HR, finance, leadership, administration, research support, and other staff roles now means planning for Copilot Business or Copilot Enterprise, often through a Sales conversation rather than one-click self-serve."
                ]),
                ("Feedback", [
                    "Treat this site like living course material. If a scenario, lesson, or factual note needs sharpening, improve it the same way you would improve a syllabus: with evidence and real examples."
                ]),
            ],
        },
        "quiz_ui": {
            "eyebrow": "Track quiz",
            "score_label": "Score",
            "answered_label": "Answered",
            "correct_label": "Correct",
            "wrong_label": "Not quite",
            "reset_label": "Retry quiz",
            "success_message": "Strong finish — you are ready to move to the next step.",
            "retry_message": "Good start — reread the explanations, then try again.",
            "why_label": "Why this matters",
        },
        "plans": {
            "title": "Plans & reality",
            "sub": "The honest map for 2026: some individual education routes are still free, but institution-wide adoption for every staff role now requires a paid organisational plan.",
            "stat_cards": [
                {"value": 5, "label": "individual plans", "desc": "From Copilot Free to Max"},
                {"value": 2, "label": "organisation plans", "desc": "Business and Enterprise"},
                {"value": 50000, "label": "Campus Program Actions minutes", "desc": "Per institution, per year, with 50 GB Packages"},
                {"value": 0, "label": "extra cost for completions", "desc": "Code completions and next edit suggestions stay unlimited on paid plans"},
            ],
            "individual_title": "Individual plans",
            "individual_intro": "Every individual plan includes Copilot CLI and the GitHub Copilot app. The real differences are access limits, premium models, and who can get a plan for free through education or open source eligibility.",
            "individual_columns": ["Plan", "Price", "Best for", "Free route", "Reality check"],
            "individual_rows": [
                plan_row("Copilot Free", "$0", "Anyone with a GitHub account", "No application needed", ["2,000 completions per month", "Automatic model selection only", "No premium models", "Limited Chat"]),
                plan_row("Copilot Student", "$0", "Verified students", "Apply via GitHub Education", ["Full student plan", "Excludes third-party coding agents", "Re-verified monthly", "Cannot be self-cancelled once granted"], "Students"),
                plan_row("Copilot Pro", "$10 / month", "Individual staff or developers", "Free for verified teachers and popular open-source maintainers", ["This is the specific free teacher entitlement", "Good default individual paid plan", "Includes CLI and GitHub Copilot app"], "Teachers"),
                plan_row("Copilot Pro+", "$39 / month", "Heavier individual use", "No standing free route", ["More AI credits", "Premium models", "Higher ceiling than Pro"]),
                plan_row("Copilot Max", "$100 / month", "Maximum individual capacity", "No standing free route", ["Top individual tier", "More AI credits", "Premium models"]),
            ],
            "org_title": "Organisation and enterprise plans",
            "org_intro": "This is the route for institution-wide rollout across roles that are not individually covered by student or teacher benefits.",
            "org_cards": [
                {
                    "icon": "🏫",
                    "title": "Copilot Business",
                    "price": "$19 / seat / month",
                    "credits": "1,900 AI credits per user / month included (promotional 3,000 through 1 Sept 2026)",
                    "note": "Starting 22 April 2026, new self-serve sign-ups for organisations on GitHub Free and GitHub Team are temporarily paused.",
                    "bullets": ["Good for staff-wide rollout with policy controls", "Code completions and next edit suggestions remain unlimited", "Chat, CLI, Spaces, cloud agent, and similar model features draw from pooled AI credits"],
                },
                {
                    "icon": "🛡️",
                    "title": "Copilot Enterprise",
                    "price": "$39 / seat / month",
                    "credits": "3,900 AI credits per user / month included (promotional 7,000 through 1 Sept 2026)",
                    "note": "Requires GitHub Enterprise Cloud and is set up through GitHub Sales.",
                    "bullets": ["Enterprise governance and admin controls", "More included credits than Business", "Designed for large-scale rollout and policy-managed environments"],
                },
            ],
            "ocre_title": "What about the OCRE framework?",
            "ocre_text": "GitHub Copilot does not appear as its own product in the OCRE catalogue. However, if your institution already has an Azure contract through an OCRE-affiliated procurement route, Copilot Business or Enterprise can typically be activated as usage-based billing on that same Azure subscription — a real but indirect path, to confirm with your Azure reseller.",
            "ocre_cta_label": "My institution wants to explore the OCRE route",
            "ocre_mailto_subject": "Our institution's interest in the OCRE route for GitHub Copilot",
            "ocre_mailto_body": "Hello Sebastien and Jochem,\n\nOur institution would like to explore the OCRE route to activate GitHub Copilot Business/Enterprise through our existing Azure contract.\n\nInstitution name:\nIT/procurement contact:\nCurrent Azure context (reseller, procurement vehicle):\n\nPlease get back to us to discuss.\n\nBest regards,",
            "pool_title": "AI credits are pooled, not trapped per person",
            "pool_intro": "That makes the finance conversation far more honest: heavy and light users balance out, while routine autocomplete keeps flowing without consuming credits.",
            "pool_total_label": "Illustrative Business pool",
            "pool_total": 5700,
            "pool_total_suffix": "credits shared across 3 seats",
            "pool_users": [
                {"name": "Light user", "used": 250, "note": "Checks Chat twice a day"},
                {"name": "Project lead", "used": 1200, "note": "Uses Chat, CLI, and one Space"},
                {"name": "Heavy builder", "used": 3200, "note": "Runs agentic features all week"},
            ],
            "pool_bullets": [
                "1 credit = $0.01.",
                "Business seats include 1,900 credits each per month; Enterprise seats include 3,900 each.",
                "Code completions and next edit suggestions are not billed in credits on paid plans.",
            ],
            "campus_title": "GitHub Campus Program: powerful platform, separate Copilot reality",
            "campus_intro": "The Campus Program is still a major strategic asset — just not a blanket free Copilot licence for everybody.",
            "campus_cards": [
                {"icon": "🏛️", "title": "Institution-wide GitHub platform", "desc": "Accredited degree-, diploma-, and certificate-granting schools can get GitHub Enterprise Cloud or Server for the whole institution, across academic and technical departments."},
                {"icon": "⚙️", "title": "Included platform capacity", "desc": "50,000 GitHub Actions minutes and 50 GB of Packages storage are included, renewed yearly if the programme terms are still met."},
                {"icon": "🧾", "title": "What it does not include", "desc": "It does not automatically include free Copilot seats for every staff member. Students and verified teachers still use their own individual education routes; everyone else needs a paid organisational plan."},
            ],
            "cta_title": "Start with the right doorway",
            "cta_cards": [
                {"title": "Instant browser demo", "desc": "Open Copilot Chat with zero install and try your first prompt in the browser.", "label": "github.com/copilot", "href": "https://github.com/copilot"},
                {"title": "Student or teacher route", "desc": "Check GitHub Education for Copilot Student or free Copilot Pro eligibility.", "label": "github.com/education", "href": "https://github.com/education"},
                {"title": "Campus Program application", "desc": "Institutional leaders can apply for the GitHub Campus Program.", "label": "education.github.com/schools", "href": "https://education.github.com/schools"},
                {"title": "Institution-wide rollout", "desc": "When you are beyond individually eligible users, plan for a Sales conversation about Business or Enterprise.", "label": "Talk to GitHub Sales", "href": "https://github.com/customer-stories?type=sales"},
            ],
        },
        "scenarios": {
            "title": "Eight real scenarios by role",
            "sub": "Use these as demos, workshop scripts, or internal adoption stories. Every scenario below is anchored in a real GitHub Copilot feature named in the official documentation.",
            "jump_label": "Jump to a role",
            "steps_label": "What happens",
            "deliverables_label": "Concrete outcome",
            "impact_label": "Why it lands",
            "items": [
                scenario_item("teacher", "🎓", "Teacher", "Live in class, zero install, and build something visible before the session ends.", "A teacher has a course outline, wants a revision quiz and one practical exercise page, and does not want to install a full toolchain just to test the idea.", ["Copilot Chat", "GitHub Pages", "Copilot Spaces"], "I teach first-year microbiology. Build a GitHub Pages-friendly mini-site with one index.html, one style.css, and one script.js. Include 6 multiple-choice revision questions, one short case exercise, instant feedback, and a reset button. Keep the language student-friendly.", "Here is a starter version with the three files, a clean layout, and the first six questions scaffolded. I also added comments so you can swap in your own course topics before publishing.", ["Open github.com/copilot in the browser and paste the outline.", "Ask Copilot Chat for a first static version you can publish on GitHub Pages.", "Once it works, create a Copilot Space called “My syllabus” with the slides, readings, and glossary so future answers stay grounded in that course."], ["A working revision page in a repository", "A GitHub Pages URL you can share the same day", "A reusable Space for the next assignment or FAQ"], "The teacher feels the shift immediately: Copilot is not “talking about AI”; it is shipping a real teaching artefact in public view."),
                scenario_item("student", "🧑‍🎓", "Student", "Turn a final-year project idea into a branch-by-branch working app instead of a vague concept note.", "A student team has a project brief, limited time, and wants to move from idea to MVP while still learning what the code does.", ["Copilot Student", "Agent mode", "Copilot code review"], "Agent mode: build a minimum viable lab-equipment booking app for a final-year project. Start with a landing page, request form, admin list, README, and one feature branch at a time. Explain each major change before applying it.", "I can start with a repository plan, scaffold the first branch, and then open reviewable changes for the booking form and admin view separately so you keep the project understandable.", ["Use the free Copilot Student entitlement in VS Code.", "Ask Agent mode to scaffold the MVP one branch at a time instead of making a giant opaque jump.", "Before submission, run Copilot code review on the pull requests so the team gets specific improvement notes."], ["A working MVP rather than a slide deck only", "A clearer commit and branch history for supervisors", "Review comments that strengthen code quality before hand-in"], "The student experience stays hands-on: Copilot accelerates the build, but the branch structure and review cycle keep the learning visible."),
                scenario_item("it", "🖥️", "IT & digital services", "Clear several internal tickets in parallel without losing control of what changes where.", "An IT team has a pile of small tickets — restyling a service page, migrating a script, improving a form — and wants speed without chaos.", ["GitHub Copilot app", "Parallel agents", "Plan mode"], "Create three Plan-mode sessions: 1) migrate this CSV cleanup script to Python, 2) refresh the staff directory front page, 3) add structured logging to the room-booking service. Keep each task in its own worktree and show the plan before any edits.", "I created separate plans for the three tickets, each isolated in its own session and branch. Review the diffs and approve only the pieces you want to ship this week.", ["Launch the GitHub Copilot app and open several agent sessions in parallel.", "Keep the sessions in Plan mode so the team reviews the plan and the diffs before execution.", "Use the native GitHub integration to move each accepted change into the usual branch / PR / CI flow."], ["Three parallel workstreams instead of one blocked queue", "Reviewable diffs per ticket", "A faster backlog rhythm with human approval still in the loop"], "This is where agent-driven development feels operationally useful rather than theatrical: parallel, isolated, and reviewable."),
                scenario_item("hr", "🤝", "HR", "Build a grounded internal assistant without hand-coding a backend.", "HR keeps answering the same onboarding, leave, and contract-template questions, but wants answers tied to the real policy documents.", ["Copilot Spaces", "Copilot Chat"], "Create a Space called HR policies using these onboarding guides, leave procedures, contract templates, and FAQ notes. Draft a staff-facing question page that answers the top 12 recurring questions and clearly cites the policy source for each answer.", "I grouped the source material, drafted answer patterns grounded in the uploaded documents, and produced a clean FAQ-style page that HR can review before publishing internally.", ["Create one Space that contains the canonical HR material.", "Use Copilot Chat against that Space to draft answers and a simple FAQ page.", "Review, adjust tone, then publish the approved version as an internal reference page."], ["A grounded FAQ instead of another overflowing mailbox", "Faster onboarding answers for staff", "A reusable Space that improves future HR prompts"], "The key win is trust: people get answers from the institution’s own documents, not generic web prose."),
                scenario_item("leadership", "🧭", "Leadership", "Turn weekly KPI chasing into a scheduled, reviewable synthesis flow.", "A dean or department head wants one concise weekly picture across several teams without manually collating every update.", ["Custom agents", "Copilot cloud agent", "Automations"], "In .github/agents/reporting.md, define an agent that reads the KPI files in /finance, /student-success, /research, and /operations, then writes a weekly-summary.md draft with wins, risks, and open questions. Schedule it every Friday afternoon and open a PR instead of editing main directly.", "I can use the custom agent instructions, pull the source files together, and raise a reviewable PR with the proposed weekly summary so leadership approves the narrative before it is shared.", ["Create a custom agent persona for the reporting style you want.", "Schedule a Copilot cloud agent automation to run every week.", "Review the PR, not a mystery email attachment, before the summary is circulated."], ["A repeatable weekly reporting ritual", "One PR that leadership can comment on", "Less coordinator time spent copy-pasting status updates"], "Leadership gets the speed of automation while keeping the institutional review checkpoint where it belongs: before publication."),
                scenario_item("finance", "💶", "Finance", "Turn a monthly export into a dashboard in minutes and keep the AI-cost story measurable.", "Finance receives a recurring Excel or CSV export and wants a lightweight dashboard instead of rebuilding the same spreadsheet views every month.", ["Prompt files", "Copilot Chat", "AI credits"], "Use .github/prompts/budget-dashboard.prompt.md with inputs [export_file] and [month]. Transform the attached budget export into a static dashboard with variance cards, a sortable table, and overspend flags. Keep calculations visible in code and explain the estimated AI-credit usage for this run.", "I drafted the prompt-file template, converted the export into a one-page dashboard, and kept the formulas visible so the team can audit both the numbers and the build process.", ["Create one shared prompt file for the recurring finance workflow.", "Feed the current export into the template instead of re-explaining the task every month.", "Track the run inside your normal organisational AI-credit pool rather than guessing at a flat mystery cost."], ["A reusable dashboard workflow", "Visible calculations in code", "A concrete finance story for why pooled AI credits are easier to govern than guesswork"], "Finance does not have to love hype to see the value: the result is faster reporting with a clearer cost model."),
                scenario_item("research", "🔬", "Research", "Ask a dataset a plain-language question and still receive the script behind the answer.", "Researchers want faster access to trusted data, but they also need reproducibility and an inspectable analysis path.", ["MCP servers", "Copilot Chat", "Python / R script generation"], "Using the approved retention-data MCP server, compare retention for cohorts 2022 to 2025 by faculty. Then generate the Python notebook that reproduces the chart and add comments explaining every transformation step.", "I can query the connected dataset, summarise the comparison in plain language, and generate the notebook so the research team can rerun or adapt the method.", ["Connect an approved MCP server to the relevant dataset.", "Ask the question in Copilot Chat instead of manually stitching together the first query.", "Take the generated Python or R script as the reproducible artefact for review, reuse, or publication support."], ["A faster path from question to first analysis", "A script the team can inspect and rerun", "A grounded workflow that respects research traceability"], "This keeps the convenience of natural language without giving up the reproducibility researchers need."),
                scenario_item("campus", "📚", "Library / campus services", "Let a non-developer service team ship a useful mini-app instead of waiting for a full system replacement.", "Library or campus staff need a simple room-booking or inventory-tracking tool for one service point and want something practical this semester.", ["Agent mode", "GitHub Pages", "GitHub Campus Program"], "Build a static room-booking prototype for the library: date selector, room cards, booked/free status using mock data, accessibility notes, and a GitHub Pages deployment workflow. Keep the structure easy for non-developers to edit later.", "I scaffolded a small static app, added accessible room cards and a deploy workflow, and kept the content files simple so the service team can maintain the page after the first launch.", ["Use Agent mode to scaffold the first version quickly.", "Host the app on GitHub Pages using the institution’s GitHub platform footprint.", "Keep the content editable enough that library or campus staff can own the page after launch."], ["A working service prototype instead of a long waiting list", "Free static hosting on GitHub Pages", "A concrete demonstration of what the Campus Program platform can enable"], "The library team sees immediate value because the result is a usable service page, not an abstract AI pilot."),
            ],
        },
        "tracks": {
            "basics": {
                "subtitle": "Your first steps in vibe coding: turn a real campus problem into a real app with GitHub Copilot.",
                "card_desc": "Discover vibe coding, build your first useful web app with Copilot, and publish it online.",
                "lesson_updates": {
                    1: {
                        "title": "From a real campus problem to an app idea",
                        "paragraphs": [
                            "The best starting point is never a technology, it is a real campus problem: students have no easy way to revise, a service keeps answering the same question by email, a team tracks a budget line in ten spreadsheets, a lab needs a lightweight booking page. Start from lived friction.",
                            "Describe the problem in one sentence, then imagine the smallest possible app that would reduce that friction. A quiz, a page, a calculator, a tracker, a searchable FAQ: keep it simple first, then grow it once people are actually using it.",
                        ],
                    },
                    2: {
                        "paragraphs": [
                            "This is the lesson where you actually build something. Install the GitHub Copilot extension in Visual Studio Code, or open Copilot Chat directly on github.com/copilot with your GitHub account, then create a new file called index.html.",
                            "Below, we build a real, working example together — a “Quick Poll” you could use in a class, a training session, a team meeting, or a town hall. Follow the steps with your own copy of Copilot, then try the finished result live at the end.",
                        ],
                    },
                    5: {
                        "paragraphs": [
                            "Once your app works, ask Copilot to improve the presentation: your institution’s colours, clearer spacing, more readable text, stronger accessibility. You can also create a small Copilot Space with example copy, slides, or a style guide so the suggestions stay grounded in your own material.",
                            "Think about accessibility too: enough contrast, readable text, clear labels, and buttons that are easy to hit. Ask Copilot to check those points explicitly before you publish.",
                        ],
                    },
                },
                "quiz": quiz("Basics quiz — can you launch a first app safely?", "Five quick checks before you move on. Answer each question and read the explanation straight away.", [
                    q("Where can you try Copilot Chat with zero install from any GitHub account?", ["Only inside VS Code", "On github.com/copilot", "Only in GitHub Desktop", "Only in the mobile app"], 1, "github.com/copilot is the zero-install browser entry point and a powerful first demo for workshops."),
                    q("What is the best first shape for a vibe-coding project?", ["A tiny version that already works", "A full platform with every planned feature", "A database-first architecture document", "A perfect visual identity before any code"], 0, "A small working version gives you something to test, publish, and improve without getting lost."),
                    q("Why put even a tiny project on GitHub early?", ["Only to impress colleagues", "Because GitHub automatically makes it private forever", "For backup, version history, and easy publishing", "Because Copilot refuses to work without it"], 2, "GitHub gives you backup, branches, commits, and a straightforward path to GitHub Pages."),
                    q("What is the safer way to improve an app with Copilot?", ["Ask for ten changes at once", "One change, one test, one commit", "Never test until the end", "Rewrite everything from scratch each time"], 1, "Small, testable increments make the process understandable and reversible."),
                    q("Who stays in charge when Copilot proposes code?", ["Copilot alone", "The browser cache", "You do: read, adjust, approve", "Whoever published the repository first"], 2, "Copilot is a proposing system. Human review remains the control point."),
                ]),
            },
            "advanced": {
                "subtitle": "Connect a database, give your project durable instructions, and manage your code like a project that is meant to last.",
                "lesson_updates": {
                    6: {
                        "paragraphs": [
                            "Without specific instructions, Copilot will not automatically keep every project convention in mind. Put a .github/copilot-instructions.md file in the repository and write the rules you repeat every session: naming, tone, build steps, accessibility constraints, or visual conventions.",
                            "You can complement that with prompt files, path-specific instruction files, AGENTS.md, or specialised agent files later. Start with the single always-on instruction file first so the project stops resetting to “generic mode”.",
                        ],
                        "exercise": "Create your first .github/copilot-instructions.md file with at least three rules that matter in your own context: style, build steps, and one institutional constraint.",
                    },
                    8: {
                        "paragraphs": [
                            "A project that lasts needs real organisation: clear commits, small branches, pull requests, and a review habit. If your institution wants the GitHub platform at scale, the GitHub Campus Program can provide GitHub Enterprise Cloud or Server to the whole school — but that is the platform layer, not a blanket free Copilot licence for every staff role.",
                            "For Copilot itself, students can still use Copilot Student individually and verified teachers can still use free Copilot Pro individually. Wider staff rollout across IT, HR, finance, leadership, and administration means planning for Copilot Business or Copilot Enterprise with the right governance and budget model.",
                        ],
                    },
                },
                "quiz": quiz("Advanced quiz — can you scale without losing control?", "These questions check the habits that make a prototype sustainable inside a real institution.", [
                    q("When is Agent mode most useful?", ["When you want multi-step changes planned and applied with approval checkpoints", "Only for renaming one variable", "Only on mobile", "Only after a project is finished"], 0, "Agent mode shines on bigger tasks that touch several files or steps."),
                    q("When do you need a database?", ["Whenever you want dark mode", "When the app must remember information between sessions", "Only after you have 10,000 users", "Never in education"], 1, "If the app must store scores, sign-ups, bookings, or any ongoing record, you need persistence."),
                    q("What is the correct always-on custom-instructions file path for a repository?", ["instructions.txt", ".github/copilot-instructions.md", "README.instructions", "copilot.json"], 1, "That exact file path is the official repository-level custom instructions entry point."),
                    q("What is the honest 2026 message about Campus Program versus Copilot seats?", ["Campus Program automatically gives every staff member free Copilot", "Campus Program provides the GitHub platform, while wider staff Copilot access is still a separate plan decision", "Campus Program only works for students", "Campus Program removes the need for pull requests"], 1, "The platform and the Copilot seat entitlement are related, but not the same thing."),
                    q("Why keep work in branches and pull requests?", ["To make the project harder to understand", "To avoid ever talking to colleagues", "To isolate changes, review them, and merge safely", "Because GitHub Pages demands it"], 2, "Branch / PR flow is what lets a project grow without turning every experiment into production immediately."),
                ]),
            },
            "expert": {
                "lesson_updates": {
                    5: {
                        "paragraphs": [
                            "An AI model costs something for every question asked. On paid organisational Copilot plans, model-heavy features such as Chat, CLI, Spaces, the cloud agent, and similar agentic tools use AI credits — but code completions and next edit suggestions stay unlimited and are not billed in credits.",
                            "Business includes 1,900 AI credits per user per month and Enterprise includes 3,900, with higher promotional allocations through 1 September 2026. Those credits are pooled across the whole billing entity, so heavy and light users balance out instead of every person being trapped inside a silo.",
                        ],
                        "exercise": "Write down which part of your workflow needs unlimited autocomplete and which part truly needs model-heavy agentic work. That distinction is the basis of honest cost control.",
                    },
                },
                "quiz": quiz("Expert quiz — do you understand the real AI rollout economics?", "These questions check the feature, security, and plan realities behind a serious Copilot deployment.", [
                    q("What should never appear in browser-visible code?", ["A CSS variable", "An API key for your AI service", "A heading tag", "A README link"], 1, "Secrets belong in protected environment variables or GitHub secrets, not in client-side source."),
                    q("Which Copilot activities are billed in AI credits on paid organisational plans?", ["Code completions only", "Chat, CLI, Spaces, and agentic model features", "Git commits", "GitHub Pages deploys"], 1, "Model-driven features consume credits; routine autocomplete does not."),
                    q("What remains unlimited on all paid Copilot plans?", ["Pull requests", "Repository size", "Code completions and next edit suggestions", "Cloud-agent PRs"], 2, "That is the key “cost control” fact: autocomplete stays unlimited."),
                    q("How are included AI credits handled on Business and Enterprise?", ["They are pooled across the billing entity", "They are trapped forever per person", "They reset every hour", "They only exist on Copilot Free"], 0, "Pooling lets heavy and light users balance each other instead of forcing flat, per-head fear."),
                    q("What does the Campus Program not automatically include?", ["GitHub Enterprise Cloud or Server access", "GitHub Actions minutes and Packages storage", "Free Copilot seats for every staff role", "Institutional eligibility for GitHub"], 2, "Campus Program is a strong GitHub platform story, but it is not a blanket free Copilot-seat story."),
                ]),
            },
        },
        "explorer": {
            "sub": "26 concrete, ready-to-follow use cases across every part of higher education. Filter by role or by real GitHub Copilot feature families, then open a card for the exact steps.",
            "features": [
                ("inline", "Inline suggestions", "Autocomplete-style code suggestions in your IDE, plus next edit suggestions in supported editors."),
                ("chat", "Copilot Chat", "Ask, refine, explain, and build in plain language on github.com/copilot, mobile, IDEs, or Windows Terminal."),
                ("agent", "Agent mode", "Copilot works more autonomously in your IDE, planning and applying multi-file changes with approval checkpoints."),
                ("cli", "Copilot CLI", "Describe terminal work in natural language and keep the flow moving in the command line."),
                ("review", "Copilot code review", "AI review suggestions and reviewer focus areas before or during human review."),
                ("cloudagent", "Copilot cloud agent", "Assign a task or issue, let Copilot work on a branch, then review the pull request."),
                ("spaces", "Copilot Spaces", "Ground Copilot with repos, files, free text, transcripts, and images in a shareable space."),
                ("mcp", "MCP servers", "Connect Copilot to trusted external tools and data sources."),
            ],
            "usecase_rewrites": {
                1: {
                    "title": "Ground a diagram explainer with Copilot Spaces",
                    "features": ["spaces", "chat"],
                    "situation": "You have slides, a scanned diagram, and tutor notes, and you want an accessible digital explainer instead of one more image embedded in a PDF.",
                    "steps": [
                        "Create a Space and upload the diagram image, the relevant slide text, and a plain-language caption.",
                        "Ask Copilot Chat to turn that grounded material into an HTML/CSS explainer with labels, alt text, and a short glossary.",
                        "Publish the approved version on GitHub Pages so students can revisit it outside class.",
                    ],
                    "result": "A clearer, reusable explainer grounded in your own teaching material.",
                    "further": "Reuse the same Space for the next diagram-heavy topic instead of restating the context from scratch.",
                },
                7: {
                    "title": "Build a portfolio grounded in your real project files",
                    "features": ["spaces", "chat"],
                    "situation": "You want a portfolio site without rewriting every project description from scratch.",
                    "steps": [
                        "Create a Space with your README files, project screenshots, internship summary, and key links.",
                        "Ask Copilot Chat to draft a one-page portfolio with project cards and short outcome-focused bullets.",
                        "Refine the tone, then publish the result on GitHub Pages.",
                    ],
                    "result": "A portfolio that is faster to build because the raw material is already grounded.",
                    "further": "Keep the Space updated each semester so future portfolio refreshes become a short editing pass.",
                },
                16: {
                    "title": "Turn strategy notes into a shareable one-pager with Copilot Spaces",
                    "features": ["spaces", "chat"],
                    "situation": "You have meeting notes, KPI context, and a rough narrative, and you want a cleaner update than a wall of bullet points.",
                    "steps": [
                        "Create a Space with the strategy notes, the KPI sheet, and the core terms everyone uses internally.",
                        "Ask Copilot Chat for a one-page summary with priorities, risks, and next actions in plain language.",
                        "Review the wording, then publish or export the version you want to share.",
                    ],
                    "result": "A clearer leadership one-pager grounded in your actual internal material.",
                    "further": "Reuse the same Space for monthly or quarterly updates so the vocabulary stays consistent.",
                },
                22: {
                    "title": "Build a research results page grounded in your figures",
                    "features": ["spaces", "chat"],
                    "situation": "You want a public-facing explanation of your findings, but you also want the text to stay close to the abstract, figures, and talk notes you already trust.",
                    "steps": [
                        "Create a Space with the abstract, figure captions, poster text, and your plain-language summary notes.",
                        "Ask Copilot Chat for a public results page with a short methods box and a clear summary for non-specialists.",
                        "Review the text, then publish the page alongside the formal paper link.",
                    ],
                    "result": "A research-results page that is grounded, accessible, and easier to reuse in talks or grant follow-up.",
                    "further": "Add a collaboration section and keep the Space as the source for future dissemination material.",
                },
                25: {
                    "title": "Publish a campus events page from a grounded events pack",
                    "features": ["spaces", "chat"],
                    "situation": "You have calendar exports, poster copy, and accessibility notes, and you want a cleaner events page that staff can update monthly.",
                    "steps": [
                        "Create a Space with the event titles, dates, descriptions, and accessibility notes.",
                        "Ask Copilot Chat for a page that sorts events by date and highlights the next upcoming activities first.",
                        "Publish the page on GitHub Pages and update the Space each month rather than rebuilding the page from scratch.",
                    ],
                    "result": "A lightweight events page that is easier to maintain than a static poster archive.",
                    "further": "Add a “contact the organiser” block and reuse the same structure for every new month.",
                },
            },
        },
    },
    "fr": {
        "nav": {
            "plans": "Plans & réalité",
            "scenarios": "8 scénarios réels",
            "courses_menu": "Parcours",
            "mobile_group_learn": "Apprendre",
            "mobile_group_resources": "Ressources",
            "mobile_group_tools": "Outils",
        },
        "home": {
            "cta_primary": "Parcourir 8 scénarios réels",
            "cta_primary_page": "scenarios",
            "cta_secondary": "Comparer les plans et les accès gratuits",
            "cta_secondary_page": "plans",
            "cta_tertiary": "Commencer le parcours guidé",
            "cta_tertiary_page": "basics",
            "hero_note": "Commence aujourd’hui sur github.com/copilot, puis choisis la trajectoire qui correspond à ton rôle : enseignement, études, IT, RH, direction, finances, recherche ou bibliothèque.",
            "journey_title": "D’un vrai problème de campus à une application publiée",
            "journey_sub": "La même boucle concrète fonctionne pour l’enseignement, le support, l’administration et la recherche.",
            "courses_sub": "Utilise les parcours guidés pour prendre le geste, puis adapte la méthode à ta faculté, ton service, ton laboratoire, ta bibliothèque ou ton programme.",
            "scenario_section_title": "Quelques scénarios concrets pour te projeter",
            "scenario_section_sub": "La page Scénarios développe huit parcours complets. Ici, commence par quatre aperçus rapides par rôle, puis ouvre le playbook complet pour la version pas à pas.",
            "scenario_section_cta": "Voir les 8 scénarios complets",
            "start_free_title": "Comment commencer aujourd’hui",
            "start_free_sub": "Choisis la porte d’entrée qui enlève ton blocage du moment : installation, première pratique ou compréhension des accès encore gratuits.",
            "impact_stats": [
                {"value": 26, "label": "cas d’usage filtrables", "desc": "Pour huit rôles de l’enseignement supérieur"},
                {"value": 25, "label": "leçons guidées", "desc": "Du premier prompt à l’application publiée"},
                {"value": 8, "label": "scénarios phares", "desc": "De l’enseignement à la bibliothèque, tous ancrés dans de vraies fonctionnalités"},
                {"value": 5, "label": "plans individuels", "desc": "Free, Student, Pro, Pro+ et Max"},
            ],
            "hero_visual": {
                "title": "Du prompt au prototype",
                "badges": ["Chat", "Spaces", "Mode Agent", "GitHub Pages"],
                "lines": [
                    "Ouvre github.com/copilot",
                    "Décris un vrai problème de campus",
                    "Laisse Copilot construire la première version",
                    "Publie le résultat sur GitHub Pages",
                ],
            },
            "start_free_cards": [
                {
                    "icon": "🧪",
                    "title": "Commence par ton premier commit",
                    "desc": "La page guidée t’emmène du compte GitHub au premier dépôt et explique les routes navigateur, CLI et Desktop — avec le bon contexte sur les accès gratuits côté communauté étudiante et corps enseignant.",
                    "cta": "Suivre la page guidée",
                    "page": "first_commit",
                    "badge": "Commence ici",
                    "featured": True,
                },
                {
                    "icon": "⚡",
                    "title": "Teste Copilot dans le navigateur",
                    "desc": "Besoin d’un premier essai sans installation ? Ouvre Copilot Chat sur github.com/copilot et teste un vrai prompt avant toute configuration locale.",
                    "cta": "Ouvrir github.com/copilot",
                    "href": "https://github.com/copilot",
                },
                {
                    "icon": "🎓",
                    "title": "Vérifie les accès gratuits",
                    "desc": "Vois qui commence encore gratuitement en 2026 : Copilot Student pour la communauté étudiante éligible, Copilot Pro gratuit pour le corps enseignant vérifié, et le moment où le payant démarre pour les autres rôles.",
                    "cta": "Voir Plans & réalité",
                    "page": "plans",
                },
            ],
            "start_free_links_label": "Puis continue avec",
            "start_free_links": [
                {"label": "36 cas d’usage concrets", "page": "explorer"},
                {"label": "Construire ou acheter", "page": "build_vs_buy"},
            ],
            "scenario_teaser_ids": ["teacher", "student", "it", "leadership"],
            "scenario_examples_label": "Quatre autres idées selon d’autres rôles",
        },
        "home_personas": [
            ("🎓", "Enseignantes et enseignants", "Construis enfin le compagnon de cours, le quiz, la page de révision ou l’aide à la correction que tu imagines depuis longtemps.", "Exemple :", "Une personne du corps enseignant en chimie publie un microsite de révision avant le prochain laboratoire."),
            ("🧑‍🎓", "Étudiantes et étudiants", "Transforme une idée de projet de fin d’études en application qui fonctionne, branche par branche, avec revue de code avant remise.", "Exemple :", "Un groupe construit un prototype de réservation de matériel de labo au lieu de remettre une maquette statique."),
            ("🖥️", "Services IT et numériques", "Lance plusieurs sessions agentiques en parallèle, garde la main avec le mode Plan, puis valide les diffs avant publication.", "Exemple :", "L’IT absorbe trois tickets du backlog en parallèle dans l’application GitHub Copilot."),
            ("🤝", "Ressources humaines", "Ancre Copilot dans les vraies procédures, modèles et documents d’intégration pour obtenir des réponses alignées sur les politiques internes.", "Exemple :", "Les RH transforment des PDF de procédures en assistant d’onboarding sans coder un backend à la main."),
            ("🧭", "Direction et pilotage", "Automatise les synthèses hebdomadaires grâce aux agents personnalisés et aux exécutions planifiées du cloud agent.", "Exemple :", "Une direction reçoit un résumé KPI prêt à relire chaque vendredi au lieu de courir après les mises à jour."),
            ("💶", "Finances et administration", "Transforme les exports en tableaux de bord en gardant un récit de coût honnête grâce au modèle des AI credits mutualisés.", "Exemple :", "L’équipe finances convertit un export mensuel en tableau de bord de variance en quelques minutes."),
            ("🔬", "Chercheuses et chercheurs", "Connecte des données de confiance via MCP et laisse Copilot rédiger le script Python ou R que tu peux inspecter et rejouer.", "Exemple :", "Une équipe interroge des données de rétention en langage naturel puis récupère le notebook derrière le graphique."),
            ("📚", "Bibliothèque, campus et services aux étudiantes et aux étudiants", "Crée un outil léger de réservation, d’inventaire, de FAQ ou d’événements sans attendre un grand projet sur mesure.", "Exemple :", "Le personnel de bibliothèque publie une petite application de réservation de salles pour le lancement du semestre."),
        ],
        "home_examples": [
            ("Hub de questions d’onboarding", "Un assistant RH ancré dans les vraies procédures du personnel.", "RH"),
            ("Tableau de bord de variance budgétaire", "Une page unique construite à partir d’un export Excel ou CSV.", "Finances"),
            ("Assistant d’interrogation de données", "Des questions en langage naturel sur des données de confiance, avec le script derrière la réponse.", "Recherche"),
            ("Prototype de réservation pour bibliothèque", "Une petite page GitHub Pages pour salles, créneaux et accessibilité.", "Bibliothèque"),
        ],
        "best_practices": {
            "title": "Bonnes pratiques",
            "sub": "Une check-list en une page pour démarrer fort, rester factuel et garder un récit réaliste entre premier prompt et adoption institutionnelle.",
            "items": [
                ("Pars d’un vrai problème de campus", "Les meilleures idées viennent d’un irritant réel, d’un goulet d’étranglement ou d’une tâche répétitive vécue chaque semaine."),
                ("Commence petit, puis itère", "Une petite page qui fonctionne et qui est utilisée vaut mieux qu’un grand concept jamais publié."),
                ("Un changement, un test, un commit", "Les petites étapes rendent le travail relisible, testable et réversible."),
                ("Sauvegarde tout sur GitHub dès le premier jour", "Même un prototype minuscule mérite un historique, une sauvegarde et un chemin simple vers GitHub Pages."),
                ("Vérifie tôt le plan auquel tu as réellement droit", "Les étudiantes et les étudiants peuvent demander Copilot Student, les enseignantes et les enseignants vérifiés peuvent demander Copilot Pro gratuit, et le reste du personnel relève d’un plan Business ou Enterprise payant."),
                ("Ancre Copilot avant de faire confiance à la réponse", "Spaces, instructions, prompt files et serveurs MCP rapprochent Copilot de tes vrais documents et données."),
                ("Utilise .github/copilot-instructions.md", "Écris les conventions, étapes de build et règles de style que tu répètes à chaque session."),
                ("Garde les secrets et les données personnelles hors du navigateur", "Les clés d’API vont dans des secrets protégés, et les données étudiantes ou RH demandent une conception sobre et explicite."),
                ("Relis chaque suggestion avant de l’accepter", "Copilot propose ; la décision et la validation restent humaines."),
                ("Pilote avec de vraies personnes avant de passer à l’échelle", "Un test à dix personnes apprend souvent plus qu’une série de réunions abstraites sur “la stratégie IA”."),
                ("Garde des instructions personnalisées courtes et concrètes", "Quelques règles précises que Copilot suit vraiment valent mieux qu’un long document survolé. Écris des conventions, pas de la philosophie."),
                ("Garde une courte trace de ce qu’un agent a changé", "Une ligne par session d’agent — ce qui a changé, pourquoi, quoi vérifier — fait gagner un temps réel quand plusieurs personnes partagent le même dépôt."),
            ],
        },
        "about": {
            "title": "À propos de ce parcours",
            "paragraphs": [
                "Vibe Coding Copilot est une ressource indépendante et gratuite pour l’enseignement supérieur : corps enseignant, communauté étudiante, IT, RH, direction, finances, recherche, bibliothèque et services de campus qui veulent créer des outils utiles avec GitHub Copilot et GitHub.",
                "Ce site n’est ni affilié, ni approuvé, ni sponsorisé par GitHub ou Microsoft. Son rôle est d’aider les établissements à prendre des décisions d’adoption réalistes, fondées sur des faits — y compris là où les accès gratuits s’arrêtent et où le déploiement payant commence.",
            ],
            "sections": [
                ("Pourquoi ce parcours existe", [
                    "Trop de bonnes idées restent bloquées derrière une file de tickets, une ligne budgétaire ou la phrase “il faudrait un vrai projet pour ça”. Le vibe coding baisse cette barrière en transformant l’expertise métier en prototype ou en petite application."
                ]),
                ("Pourquoi GitHub en particulier", [
                    "GitHub raconte la seconde moitié de l’histoire : dépôts, branches, pull requests, GitHub Pages et maison native pour Copilot. Le GitHub Campus Program peut même fournir GitHub Enterprise Cloud ou Server à tout l’établissement, mais cet accès plateforme n’est pas synonyme de sièges Copilot gratuits pour tout le personnel."
                ]),
                ("La réalité honnête du déploiement en 2026", [
                    "Les étudiantes et les étudiants peuvent encore obtenir Copilot Student gratuitement. Les enseignantes et les enseignants vérifiés peuvent encore obtenir Copilot Pro gratuitement à titre individuel. Mais un déploiement large pour l’IT, les RH, les finances, la direction, l’administration, le support à la recherche et les autres fonctions passe désormais par Copilot Business ou Copilot Enterprise, souvent via une conversation Sales plutôt que par un self-serve sans friction."
                ]),
                ("Retours", [
                    "Traite ce site comme un support de cours vivant. Si un scénario, une leçon ou une précision factuelle mérite d’être affiné, améliore-le avec des exemples réels et des sources solides."
                ]),
            ],
        },
        "quiz_ui": {
            "eyebrow": "Quiz du parcours",
            "score_label": "Score",
            "answered_label": "Répondu",
            "correct_label": "Correct",
            "wrong_label": "Pas encore",
            "reset_label": "Recommencer le quiz",
            "success_message": "Très bien — tu peux passer à l’étape suivante.",
            "retry_message": "Bon départ — relis les explications puis réessaie.",
            "why_label": "Pourquoi c’est important",
        },
        "plans": {
            "title": "Plans & réalité",
            "sub": "La carte honnête pour 2026 : certains accès individuels restent gratuits, mais l’adoption institutionnelle pour tous les métiers passe maintenant par un plan organisationnel payant.",
            "stat_cards": [
                {"value": 5, "label": "plans individuels", "desc": "De Copilot Free à Max"},
                {"value": 2, "label": "plans organisationnels", "desc": "Business et Enterprise"},
                {"value": 50000, "label": "minutes GitHub Actions du Campus Program", "desc": "Par établissement, avec 50 Go de Packages"},
                {"value": 0, "label": "surcoût pour les complétions", "desc": "Les complétions de code et next edit suggestions restent illimitées sur les plans payants"},
            ],
            "individual_title": "Plans individuels",
            "individual_intro": "Tous les plans individuels incluent Copilot CLI et l’application GitHub Copilot. Les vraies différences concernent les limites, les modèles premium et les cas d’éligibilité gratuite.",
            "individual_columns": ["Plan", "Prix", "Pour qui", "Accès gratuit", "Réalité"],
            "individual_rows": [
                plan_row("Copilot Free", "0 $", "Toute personne ayant un compte GitHub", "Aucune demande nécessaire", ["2 000 complétions par mois", "Sélection automatique du modèle uniquement", "Pas de modèles premium", "Chat limité"]),
                plan_row("Copilot Student", "0 $", "Étudiantes et étudiants vérifiés", "Demande via GitHub Education", ["Plan étudiant complet", "Exclut les third-party coding agents", "Revalidation mensuelle", "Impossible à auto-annuler une fois accordé"], "Études"),
                plan_row("Copilot Pro", "10 $ / mois", "Usage individuel avancé", "Gratuit pour les enseignantes et les enseignants vérifiés et certains mainteneurs open source", ["C’est ce plan précis qui est offert au corps enseignant éligible", "Bon plan individuel par défaut", "Inclut CLI et application GitHub Copilot"], "Enseignement"),
                plan_row("Copilot Pro+", "39 $ / mois", "Usage individuel plus intensif", "Pas de route gratuite permanente", ["Davantage d’AI credits", "Modèles premium", "Plafond plus élevé que Pro"]),
                plan_row("Copilot Max", "100 $ / mois", "Capacité individuelle maximale", "Pas de route gratuite permanente", ["Tier individuel le plus élevé", "Davantage d’AI credits", "Modèles premium"]),
            ],
            "org_title": "Plans organisationnels et enterprise",
            "org_intro": "C’est la voie pour un déploiement large à l’échelle de l’établissement, au-delà des personnes couvertes individuellement par les dispositifs étudiants ou enseignants.",
            "org_cards": [
                {
                    "icon": "🏫",
                    "title": "Copilot Business",
                    "price": "19 $ / siège / mois",
                    "credits": "1 900 AI credits par personne et par mois incluses (3 000 en allocation promotionnelle jusqu’au 1er septembre 2026)",
                    "note": "Depuis le 22 avril 2026, les nouveaux self-serve sign-ups sont temporairement en pause pour les organisations sur GitHub Free et GitHub Team.",
                    "bullets": ["Pertinent pour un déploiement staff avec politiques et gouvernance", "Les complétions de code et next edit suggestions restent illimitées", "Le Chat, la CLI, Spaces, le cloud agent et les fonctions agentiques tirent dans le pool d’AI credits"],
                },
                {
                    "icon": "🛡️",
                    "title": "Copilot Enterprise",
                    "price": "39 $ / siège / mois",
                    "credits": "3 900 AI credits par personne et par mois incluses (7 000 en allocation promotionnelle jusqu’au 1er septembre 2026)",
                    "note": "Nécessite GitHub Enterprise Cloud et se met en place via GitHub Sales.",
                    "bullets": ["Gouvernance enterprise et contrôle admin", "Plus de crédits inclus que Business", "Pensé pour un déploiement large et des environnements gérés par politiques"],
                },
            ],
            "ocre_title": "Et le framework OCRE dans tout ça ?",
            "ocre_text": "GitHub Copilot n'apparaît pas comme un produit distinct au catalogue OCRE. En revanche, si votre institution a déjà un contrat Azure via une centrale d'achat affiliée OCRE, Copilot Business ou Enterprise peut généralement être activé en facturation à l'usage sur cette même souscription Azure — une voie indirecte mais réelle, à confirmer avec votre revendeur Azure.",
            "ocre_cta_label": "Mon institution veut profiter de l'OCRE",
            "ocre_mailto_subject": "Intérêt de notre institution pour la voie OCRE et GitHub Copilot",
            "ocre_mailto_body": "Bonjour Sébastien et Jochem,\n\nNotre institution souhaite explorer la voie OCRE pour activer GitHub Copilot Business/Enterprise via notre contrat Azure existant.\n\nNom de l'institution :\nContact IT/achat :\nContexte Azure actuel (revendeur, centrale d'achat) :\n\nMerci de nous recontacter pour en discuter.\n\nCordialement,",
            "pool_title": "Les AI credits sont mutualisées, pas enfermées par personne",
            "pool_intro": "C’est un argument fort pour les finances et la direction : les usages lourds et légers se compensent, tandis que l’autocomplétion de routine reste illimitée sans consommer de crédits.",
            "pool_total_label": "Exemple de pool Business",
            "pool_total": 5700,
            "pool_total_suffix": "credits partagées entre 3 sièges",
            "pool_users": [
                {"name": "Usage léger", "used": 250, "note": "Ouvre Chat deux fois par jour"},
                {"name": "Pilotage de projet", "used": 1200, "note": "Utilise Chat, CLI et un Space"},
                {"name": "Construction intensive", "used": 3200, "note": "Travaille toute la semaine avec des fonctions agentiques"},
            ],
            "pool_bullets": [
                "1 credit = 0,01 $.",
                "Business inclut 1 900 credits par personne et par mois ; Enterprise en inclut 3 900.",
                "Les complétions de code et next edit suggestions ne sont pas facturées en credits sur les plans payants.",
            ],
            "campus_title": "GitHub Campus Program : plateforme puissante, réalité Copilot distincte",
            "campus_intro": "Le Campus Program reste un atout stratégique majeur — mais ce n’est plus une histoire de Copilot gratuit pour tout le monde.",
            "campus_cards": [
                {"icon": "🏛️", "title": "Plateforme GitHub pour tout l’établissement", "desc": "Les écoles accréditées délivrant diplômes, certificats ou grades peuvent obtenir GitHub Enterprise Cloud ou Server pour l’ensemble de l’institution, y compris les départements académiques et techniques."},
                {"icon": "⚙️", "title": "Capacité plateforme incluse", "desc": "50 000 minutes GitHub Actions et 50 Go de Packages sont incluses, avec renouvellement annuel si les conditions restent remplies."},
                {"icon": "🧾", "title": "Ce que cela n’inclut pas", "desc": "Cela n’accorde pas automatiquement des sièges Copilot gratuits à tout le personnel. Les étudiantes et les étudiants ainsi que le corps enseignant éligible passent toujours par leurs routes individuelles ; les autres fonctions relèvent d’un plan payant."},
            ],
            "cta_title": "Commencer par la bonne porte d’entrée",
            "cta_cards": [
                {"title": "Démo immédiate dans le navigateur", "desc": "Ouvre Copilot Chat sans installation et teste ton premier prompt.", "label": "github.com/copilot", "href": "https://github.com/copilot"},
                {"title": "Route étudiante ou enseignante", "desc": "Vérifie GitHub Education pour Copilot Student ou Copilot Pro gratuit.", "label": "github.com/education", "href": "https://github.com/education"},
                {"title": "Candidature Campus Program", "desc": "La direction ou les responsables institutionnels peuvent déposer le dossier Campus Program.", "label": "education.github.com/schools", "href": "https://education.github.com/schools"},
                {"title": "Déploiement large dans l’établissement", "desc": "Au-delà des personnes éligibles individuellement, prépare une conversation Sales sur Business ou Enterprise.", "label": "Parler à GitHub Sales", "href": "https://github.com/customer-stories?type=sales"},
            ],
        },
        "scenarios": {
            "title": "Huit scénarios réels par rôle",
            "sub": "Utilise-les comme démos, trames d’atelier ou récits d’adoption interne. Chacun repose sur une vraie fonctionnalité GitHub Copilot nommée dans la documentation officielle.",
            "jump_label": "Aller vers un rôle",
            "steps_label": "Ce qui se passe",
            "deliverables_label": "Résultat concret",
            "impact_label": "Pourquoi ça donne envie",
            "items": [
                scenario_item("teacher", "🎓", "Enseignement", "Construire quelque chose de visible en direct, sans installation lourde.", "Une personne du corps enseignant dispose d’un plan de cours, veut un quiz de révision et une page d’exercice, et ne souhaite pas monter tout un environnement pour tester une idée.", ["Copilot Chat", "GitHub Pages", "Copilot Spaces"], "J’enseigne la microbiologie en première année. Construis un mini-site compatible GitHub Pages avec un index.html, un style.css et un script.js. Je veux 6 questions de révision à choix multiple, un exercice de cas, un retour instantané et un bouton de remise à zéro. Garde une formulation très claire pour la communauté étudiante.", "Voici une première version avec les trois fichiers, une mise en page propre et les six questions prêtes à être adaptées à ton cours. J’ai aussi commenté les zones à personnaliser avant publication.", ["Ouvrir github.com/copilot dans le navigateur et coller le plan du cours.", "Demander à Copilot Chat une première version statique immédiatement publiable sur GitHub Pages.", "Une fois le site utile, créer un Copilot Space “Mon syllabus” avec slides, lectures et glossaire pour ancrer les futures réponses dans ce cours."], ["Une page de révision fonctionnelle dans un dépôt", "Une URL GitHub Pages partageable le jour même", "Un Space réutilisable pour le prochain devoir ou la prochaine FAQ"], "L’effet waouh est immédiat : on ne “parle pas d’IA”, on montre un objet pédagogique réel qui existe déjà."),
                scenario_item("student", "🧑‍🎓", "Études", "Passer d’une idée de projet de fin d’études à une application qui tourne, branche par branche.", "Une équipe étudiante a un brief, peu de temps et veut avancer vers un MVP tout en comprenant ce que fait le code.", ["Copilot Student", "Mode Agent", "Copilot code review"], "Mode Agent : construis un MVP d’application de réservation de matériel de laboratoire pour un projet de fin d’études. Commence par une landing page, un formulaire de demande, une vue admin, un README, puis ajoute une fonctionnalité par branche. Explique chaque changement important avant de l’appliquer.", "Je peux commencer par le plan du dépôt, préparer la première branche, puis ouvrir des changements relisibles pour le formulaire et la vue admin séparément afin que le projet reste compréhensible.", ["Utiliser l’accès gratuit Copilot Student dans VS Code.", "Demander au mode Agent de construire le MVP une branche à la fois plutôt que de produire un gros saut opaque.", "Avant la remise, lancer Copilot code review sur les pull requests pour obtenir des pistes d’amélioration concrètes."], ["Un MVP fonctionnel plutôt qu’une simple note d’intention", "Un historique de commits et de branches plus lisible pour l’encadrement", "Des commentaires de revue qui renforcent la qualité avant remise"], "L’expérience reste formatrice : Copilot accélère, mais la structure en branches et la revue gardent l’apprentissage visible."),
                scenario_item("it", "🖥️", "IT & numérique", "Traiter plusieurs tickets internes en parallèle sans perdre le contrôle sur ce qui change où.", "Une équipe IT a une pile de petits tickets — page à rafraîchir, script à migrer, formulaire à fiabiliser — et veut aller plus vite sans semer le chaos.", ["GitHub Copilot app", "Agents parallèles", "Mode Plan"], "Crée trois sessions en mode Plan : 1) migrer ce script de nettoyage CSV vers Python, 2) rafraîchir la page d’accueil de l’annuaire du personnel, 3) ajouter des logs structurés au service de réservation de salles. Garde chaque tâche dans son propre worktree et montre le plan avant toute modification.", "J’ai préparé trois plans séparés, chacun dans sa propre session et sa propre branche. Il ne reste plus qu’à relire les diffs et n’approuver que ce que l’équipe veut publier cette semaine.", ["Lancer l’application GitHub Copilot et ouvrir plusieurs sessions agentiques en parallèle.", "Rester en mode Plan pour relire les plans et les diffs avant exécution.", "Utiliser l’intégration GitHub native pour faire passer chaque changement accepté dans le flux branche / PR / CI habituel."], ["Trois flux de travail parallèles au lieu d’une seule file bloquante", "Des diffs relisibles ticket par ticket", "Un rythme de backlog plus rapide avec validation humaine"], "C’est là que le développement piloté par agent devient utile opérationnellement : parallèle, isolé et relisible."),
                scenario_item("hr", "🤝", "RH", "Construire un assistant interne ancré dans les procédures sans coder un backend à la main.", "Les RH répondent sans cesse aux mêmes questions d’onboarding, de congés ou de modèles contractuels et veulent des réponses reliées aux vrais documents internes.", ["Copilot Spaces", "Copilot Chat"], "Crée un Space “Politiques RH” avec les guides d’intégration, les procédures de congés, les modèles de contrat et les notes de FAQ. Rédige ensuite une page de questions fréquentes qui répond aux 12 demandes les plus courantes et cite, pour chaque réponse, la source interne utilisée.", "J’ai regroupé les sources, préparé des schémas de réponse ancrés dans ces documents et produit une page de FAQ claire que les RH peuvent relire avant publication interne.", ["Créer un Space avec le matériau RH canonique.", "Utiliser Copilot Chat sur ce Space pour rédiger les réponses et une page de FAQ simple.", "Relire, ajuster le ton puis publier la version validée comme page de référence interne."], ["Une FAQ ancrée dans les documents plutôt qu’une nouvelle boîte mail saturée", "Des réponses plus rapides pour le personnel", "Un Space réutilisable qui améliore les futurs prompts RH"], "Le vrai gain est la confiance : les réponses viennent des documents de l’établissement, pas d’une prose générique."),
                scenario_item("leadership", "🧭", "Direction", "Transformer la chasse hebdomadaire aux KPI en synthèse planifiée et relisible.", "Une direction de département ou d’établissement veut une vue hebdomadaire concise sur plusieurs équipes sans compiler manuellement chaque mise à jour.", ["Custom agents", "Copilot cloud agent", "Automations"], "Dans .github/agents/reporting.md, définis un agent qui lit les fichiers KPI de /finance, /student-success, /research et /operations, puis rédige un weekly-summary.md avec les avancées, risques et questions ouvertes. Planifie son exécution chaque vendredi après-midi et ouvre une pull request plutôt que de modifier main directement.", "Je peux appliquer les instructions de cet agent personnalisé, rassembler les fichiers sources et ouvrir une PR relisible avec la synthèse proposée, afin que la direction valide le récit avant diffusion.", ["Créer un agent personnalisé correspondant au style de reporting voulu.", "Planifier une exécution hebdomadaire du Copilot cloud agent.", "Relire une PR plutôt qu’une pièce jointe opaque avant diffusion de la synthèse."], ["Un rituel de reporting hebdomadaire reproductible", "Une PR unique que la direction peut commenter", "Moins de temps de coordination passé à copier-coller des statuts"], "La direction obtient la vitesse de l’automatisation tout en gardant le point de contrôle institutionnel avant publication."),
                scenario_item("finance", "💶", "Finances", "Transformer un export mensuel en tableau de bord en quelques minutes avec une histoire de coût intelligible.", "L’équipe finances reçoit le même export Excel ou CSV à chaque cycle et veut un tableau de bord léger au lieu de reconstruire la même vue dans un tableur.", ["Prompt files", "Copilot Chat", "AI credits"], "Utilise .github/prompts/rapport-budget.prompt.md avec les entrées [fichier_export] et [mois]. Transforme l’export budgétaire joint en tableau de bord statique avec cartes de variance, tableau triable et alertes de dépassement. Garde les calculs visibles dans le code et estime l’usage d’AI credits de ce run.", "J’ai préparé le modèle de prompt file, converti l’export en tableau de bord une page et gardé les formules visibles afin que l’équipe puisse auditer les chiffres comme le processus.", ["Créer un prompt file partagé pour ce flux récurrent.", "Injecter l’export du mois au lieu de réexpliquer la demande à chaque fois.", "Suivre ce run dans le pool d’AI credits organisationnel plutôt que dans un coût opaque au forfait."], ["Un flux réutilisable de tableau de bord", "Des calculs visibles dans le code", "Une histoire concrète pour expliquer pourquoi les AI credits mutualisées sont plus pilotables qu’un coût uniforme"], "Les finances n’ont pas besoin d’aimer le hype : le résultat parle en rapidité de reporting et en lisibilité budgétaire."),
                scenario_item("research", "🔬", "Recherche", "Poser une question en langage naturel à un jeu de données tout en recevant le script qui permet de rejouer l’analyse.", "Les chercheuses et les chercheurs veulent aller plus vite sur des données de confiance sans perdre la reproductibilité.", ["MCP servers", "Copilot Chat", "Génération de scripts Python / R"], "En utilisant le serveur MCP approuvé pour les données de rétention, compare la rétention des cohortes 2022 à 2025 par faculté. Ensuite, génère le notebook Python qui reproduit le graphique et commente chaque étape de transformation.", "Je peux interroger la source connectée, résumer la comparaison en langage naturel et générer le notebook pour que l’équipe rejoue ou adapte la méthode.", ["Connecter un serveur MCP approuvé à la source de données pertinente.", "Poser la question dans Copilot Chat plutôt que de bricoler d’abord la requête manuelle.", "Prendre le script Python ou R généré comme artefact reproductible à relire, réutiliser ou joindre à une diffusion scientifique."], ["Un chemin plus rapide entre question et première analyse", "Un script que l’équipe peut inspecter et rejouer", "Un flux ancré qui respecte la traçabilité scientifique"], "On garde le confort du langage naturel sans abandonner l’exigence de reproductibilité."),
                scenario_item("campus", "📚", "Bibliothèque / campus", "Permettre à une équipe non développeuse de publier un mini-outil utile ce semestre.", "Le personnel de bibliothèque ou de services de campus a besoin d’un petit outil de réservation ou d’inventaire et veut quelque chose d’utile rapidement.", ["Mode Agent", "GitHub Pages", "GitHub Campus Program"], "Construis un prototype statique de réservation de salles pour la bibliothèque : sélecteur de date, cartes de salles, statut occupé/libre avec données fictives, notes d’accessibilité et workflow de déploiement GitHub Pages. Garde une structure facile à maintenir pour une équipe non développeuse.", "J’ai généré une petite application statique, ajouté des cartes de salles accessibles et un workflow de déploiement, puis gardé des fichiers de contenu simples pour que l’équipe de service puisse maintenir la page après le lancement.", ["Utiliser le mode Agent pour créer rapidement la première version.", "Héberger l’application sur GitHub Pages dans l’empreinte GitHub de l’établissement.", "Conserver une structure éditable afin que le personnel de bibliothèque ou de campus garde la main après lancement."], ["Un prototype de service fonctionnel plutôt qu’une longue liste d’attente", "Un hébergement statique gratuit sur GitHub Pages", "Une démonstration concrète de ce que la plateforme Campus Program peut permettre"], "L’équipe voit tout de suite la valeur parce que le résultat est un service utilisable, pas un pilote IA abstrait."),
            ],
        },
        "tracks": {
            "basics": {
                "subtitle": "Tes premiers pas en vibe coding : transforme un vrai problème de campus en application utile avec GitHub Copilot.",
                "card_desc": "Découvre le vibe coding, construis ta première application web utile avec Copilot et publie-la en ligne.",
                "lesson_updates": {
                    1: {
                        "title": "D’un vrai problème de campus à une idée d’application",
                        "paragraphs": [
                            "Le meilleur point de départ n’est jamais une technologie, mais un vrai problème de campus : des étudiantes et des étudiants n’ont pas de moyen simple de réviser, un service répond sans cesse à la même question par e-mail, une équipe suit une ligne budgétaire dans dix tableurs, un laboratoire veut une page de réservation légère. Pars du frottement réel.",
                            "Décris ce problème en une phrase, puis imagine la plus petite application possible pour réduire ce frottement. Un quiz, une page, un calculateur, un suivi, une FAQ consultable : garde la première version simple, puis élargis quand de vraies personnes l’utilisent.",
                        ],
                    },
                    2: {
                        "paragraphs": [
                            "C’est la leçon où tu construis vraiment quelque chose. Installe l’extension GitHub Copilot dans Visual Studio Code, ou ouvre Copilot Chat directement sur github.com/copilot avec ton compte GitHub, puis crée un nouveau fichier index.html.",
                            "Ci-dessous, on construit ensemble un exemple réel et fonctionnel : un « Sondage Éclair » que tu peux utiliser en cours, en formation, en réunion d’équipe ou en assemblée. Suis les étapes avec ton propre Copilot, puis teste le résultat en direct à la fin.",
                        ],
                    },
                    5: {
                        "paragraphs": [
                            "Une fois l’application utile, demande à Copilot d’améliorer la présentation : couleurs de l’établissement, espacements plus lisibles, texte plus accessible, meilleure hiérarchie visuelle. Tu peux aussi créer un petit Copilot Space avec des extraits de slides, une charte ou un exemple de ton pour garder les suggestions ancrées dans tes propres matériaux.",
                            "Pense aussi à l’accessibilité : contraste suffisant, texte lisible, labels clairs et boutons faciles à activer. Demande explicitement à Copilot de vérifier ces points avant publication.",
                        ],
                    },
                },
                "quiz": quiz("Quiz Débutant — peux-tu lancer une première application proprement ?", "Cinq vérifications rapides avant de passer au niveau suivant. Lis l’explication dès que tu réponds.", [
                    q("Où peux-tu essayer Copilot Chat sans rien installer ?", ["Uniquement dans VS Code", "Sur github.com/copilot", "Uniquement dans GitHub Desktop", "Uniquement dans l’application mobile"], 1, "github.com/copilot est le point d’entrée navigateur sans installation, parfait pour une première démonstration."),
                    q("Quelle est la meilleure forme pour démarrer un projet de vibe coding ?", ["Une version minuscule qui fonctionne déjà", "Une plateforme complète avec toutes les fonctionnalités prévues", "Un grand document d’architecture avant toute page", "Une identité visuelle parfaite avant le moindre code"], 0, "Une petite version fonctionnelle donne quelque chose à tester, publier et améliorer tout de suite."),
                    q("Pourquoi mettre très tôt même un petit projet sur GitHub ?", ["Seulement pour impressionner des collègues", "Parce que GitHub le rend automatiquement privé pour toujours", "Pour la sauvegarde, l’historique et la publication simple", "Parce que Copilot refuse sinon de fonctionner"], 2, "GitHub apporte sauvegarde, branches, commits et un chemin direct vers GitHub Pages."),
                    q("Quelle est la manière la plus sûre d’améliorer une application avec Copilot ?", ["Demander dix changements d’un coup", "Un changement, un test, un commit", "Ne jamais tester avant la fin", "Réécrire tout le projet à chaque fois"], 1, "Les petites étapes testables rendent la progression compréhensible et réversible."),
                    q("Qui garde la main quand Copilot propose du code ?", ["Copilot seul", "Le cache du navigateur", "Toi : tu lis, ajustes et valides", "La première personne qui a créé le dépôt"], 2, "Copilot propose ; la validation humaine reste le point de contrôle."),
                ]),
            },
            "advanced": {
                "subtitle": "Connecte une base de données, donne des instructions durables à ton projet et gère ton code comme un vrai projet qui doit tenir dans le temps.",
                "lesson_updates": {
                    6: {
                        "paragraphs": [
                            "Sans instructions spécifiques, Copilot ne gardera pas automatiquement en mémoire toutes les conventions du projet. Place un fichier .github/copilot-instructions.md dans le dépôt et note les règles répétées à chaque session : nommage, ton, étapes de build, contraintes d’accessibilité ou identité visuelle.",
                            "Tu pourras ensuite compléter avec des prompt files, des fichiers d’instructions plus ciblés, AGENTS.md ou des agents spécialisés. Commence par ce fichier toujours actif pour sortir du mode “générique”.",
                        ],
                        "exercise": "Crée ton premier fichier .github/copilot-instructions.md avec au moins trois règles importantes dans ton contexte : style, étapes de build et une contrainte institutionnelle.",
                    },
                    8: {
                        "paragraphs": [
                            "Un projet qui dure a besoin d’une vraie organisation : commits clairs, petites branches, pull requests et relecture. Si l’établissement veut la plateforme GitHub à grande échelle, le GitHub Campus Program peut fournir GitHub Enterprise Cloud ou Server à toute l’école — mais il s’agit de la couche plateforme, pas d’une licence Copilot gratuite généralisée pour tout le personnel.",
                            "Pour Copilot lui-même, les étudiantes et les étudiants peuvent encore utiliser Copilot Student individuellement et les enseignantes et les enseignants vérifiés peuvent encore utiliser Copilot Pro gratuit individuellement. Pour l’IT, les RH, les finances, la direction et les autres fonctions, le déploiement large passe par Copilot Business ou Copilot Enterprise avec la bonne gouvernance et le bon modèle budgétaire.",
                        ],
                    },
                },
                "quiz": quiz("Quiz Avancé — peux-tu faire grandir un projet sans perdre la maîtrise ?", "Ces questions vérifient les habitudes qui rendent un prototype durable dans un vrai établissement.", [
                    q("Quand le mode Agent est-il le plus utile ?", ["Quand tu veux des changements en plusieurs étapes planifiés puis appliqués avec validation", "Uniquement pour renommer une variable", "Uniquement sur mobile", "Seulement une fois le projet terminé"], 0, "Le mode Agent est particulièrement utile pour les tâches plus larges qui touchent plusieurs fichiers ou étapes."),
                    q("Quand as-tu besoin d’une base de données ?", ["Dès que tu veux le mode sombre", "Quand l’application doit mémoriser des informations entre plusieurs sessions", "Seulement après 10 000 utilisatrices et utilisateurs", "Jamais dans l’enseignement supérieur"], 1, "Dès qu’il faut stocker scores, inscriptions, réservations ou suivi durable, il faut une persistance."),
                    q("Quel est le bon chemin du fichier d’instructions toujours actif au niveau du dépôt ?", ["instructions.txt", ".github/copilot-instructions.md", "README.instructions", "copilot.json"], 1, "C’est le point d’entrée officiel pour les instructions personnalisées d’un dépôt."),
                    q("Quel message honnête faut-il retenir sur Campus Program et les sièges Copilot ?", ["Campus Program donne automatiquement Copilot gratuit à tout le personnel", "Campus Program fournit la plateforme GitHub, mais l’accès Copilot large reste une décision de plan séparée", "Campus Program est réservé uniquement aux étudiantes et aux étudiants", "Campus Program remplace les pull requests"], 1, "La plateforme et l’attribution des sièges Copilot sont liées, mais ce n’est pas la même chose."),
                    q("Pourquoi garder le travail dans des branches et des pull requests ?", ["Pour compliquer le projet", "Pour éviter toute collaboration", "Pour isoler les changements, les relire et fusionner proprement", "Parce que GitHub Pages l’impose"], 2, "Le flux branche / PR permet de faire évoluer un projet sans transformer chaque essai en production immédiate."),
                ]),
            },
            "expert": {
                "lesson_updates": {
                    5: {
                        "paragraphs": [
                            "Un modèle d’IA coûte quelque chose à chaque question posée. Sur les plans Copilot organisationnels payants, les fonctionnalités gourmandes en modèle comme Chat, la CLI, Spaces, le cloud agent et les fonctions similaires consomment des AI credits — mais les complétions de code et next edit suggestions restent illimitées et ne sont pas facturées en credits.",
                            "Business inclut 1 900 AI credits par personne et par mois, Enterprise en inclut 3 900, avec des allocations promotionnelles supérieures jusqu’au 1er septembre 2026. Ces credits sont mutualisées au niveau de l’entité de facturation : les gros et petits usages se compensent au lieu d’enfermer chaque personne dans un silo séparé.",
                        ],
                        "exercise": "Note quelle partie de ton flux relève de l’autocomplétion illimitée et quelle partie demande réellement des fonctions agentiques plus coûteuses. C’est la base d’un pilotage honnête des coûts.",
                    },
                },
                "quiz": quiz("Quiz Expert — comprends-tu la vraie économie d’un déploiement IA ?", "Ces questions vérifient les réalités de sécurité, de fonctionnalités et de plans derrière un déploiement Copilot sérieux.", [
                    q("Qu’est-ce qui ne doit jamais apparaître dans un code visible côté navigateur ?", ["Une variable CSS", "Une clé API du service IA", "Un titre de page", "Un lien README"], 1, "Les secrets vont dans des variables d’environnement protégées ou des secrets GitHub, pas dans le code client."),
                    q("Quelles activités Copilot sont facturées en AI credits sur les plans organisationnels payants ?", ["Seulement les complétions de code", "Le Chat, la CLI, Spaces et les fonctions agentiques basées sur les modèles", "Les commits Git", "Les déploiements GitHub Pages"], 1, "Les fonctions pilotées par modèle consomment des credits ; l’autocomplétion de routine n’en consomme pas."),
                    q("Qu’est-ce qui reste illimité sur tous les plans payants ?", ["Les pull requests", "La taille du dépôt", "Les complétions de code et next edit suggestions", "Les PR du cloud agent"], 2, "C’est le point clé du récit “maîtrise des coûts” : l’autocomplétion reste illimitée."),
                    q("Comment les AI credits incluses sont-elles gérées sur Business et Enterprise ?", ["Elles sont mutualisées au niveau de l’entité de facturation", "Elles restent enfermées définitivement par personne", "Elles se réinitialisent toutes les heures", "Elles n’existent que sur Copilot Free"], 0, "La mutualisation permet aux usages légers et lourds de s’équilibrer."),
                    q("Qu’est-ce que le Campus Program n’inclut pas automatiquement ?", ["GitHub Enterprise Cloud ou Server pour l’établissement", "Des minutes GitHub Actions et du stockage Packages", "Des sièges Copilot gratuits pour toutes les fonctions du personnel", "Une éligibilité institutionnelle GitHub"], 2, "Le Campus Program raconte une histoire de plateforme GitHub forte, pas une histoire de sièges Copilot gratuits pour tout le monde."),
                ]),
            },
        },
        "explorer": {
            "sub": "26 cas d’usage concrets et prêts à suivre pour tous les pôles de l’enseignement supérieur. Filtre par rôle ou par vraies familles de fonctionnalités GitHub Copilot, puis ouvre une carte pour voir les étapes exactes.",
            "features": [
                ("inline", "Suggestions inline", "Des suggestions de code dans l’IDE, avec next edit suggestions dans les éditeurs compatibles."),
                ("chat", "Copilot Chat", "Poser, reformuler, expliquer et construire en langage naturel sur github.com/copilot, mobile, IDE ou Windows Terminal."),
                ("agent", "Mode Agent", "Copilot agit plus largement dans l’IDE, planifie et applique des changements multi-fichiers avec points de validation."),
                ("cli", "Copilot CLI", "Décrire le travail terminal en langage naturel et garder le flux dans la ligne de commande."),
                ("review", "Copilot code review", "Des suggestions de revue IA et des zones d’attention avant ou pendant la relecture humaine."),
                ("cloudagent", "Copilot cloud agent", "Assigner une tâche ou une issue, laisser Copilot travailler sur une branche, puis relire la pull request."),
                ("spaces", "Copilot Spaces", "Ancrer Copilot avec dépôts, fichiers, texte libre, transcriptions et images dans un espace partageable."),
                ("mcp", "Serveurs MCP", "Connecter Copilot à des outils et sources de données de confiance."),
            ],
            "usecase_rewrites": {
                1: {
                    "title": "Ancrer une explication de schéma avec Copilot Spaces",
                    "features": ["spaces", "chat"],
                    "situation": "Tu as des slides, un schéma scanné et des notes de tutorat, et tu veux un support numérique accessible plutôt qu’une image de plus dans un PDF.",
                    "steps": [
                        "Crée un Space et ajoute l’image du schéma, le texte des slides concernées et une légende en langage clair.",
                        "Demande à Copilot Chat de transformer ce matériau ancré en page HTML/CSS avec labels, texte alternatif et mini-glossaire.",
                        "Publie la version validée sur GitHub Pages pour que la communauté étudiante y revienne hors cours.",
                    ],
                    "result": "Une explication plus claire, réutilisable et ancrée dans tes propres supports.",
                    "further": "Réutilise le même Space pour le prochain thème riche en schémas au lieu de réexpliquer tout le contexte.",
                },
                7: {
                    "title": "Construire un portfolio ancré dans tes vrais fichiers de projet",
                    "features": ["spaces", "chat"],
                    "situation": "Tu veux un portfolio sans réécrire à la main chaque description de projet.",
                    "steps": [
                        "Crée un Space avec les README, captures, résumé de stage et liens clés.",
                        "Demande à Copilot Chat une page portfolio avec cartes projet et points de résultats orientés impact.",
                        "Affine le ton puis publie la version retenue sur GitHub Pages.",
                    ],
                    "result": "Un portfolio plus rapide à produire parce que la matière est déjà ancrée.",
                    "further": "Garde ce Space à jour chaque semestre pour transformer les futures mises à jour en simple passe d’édition.",
                },
                16: {
                    "title": "Transformer des notes stratégiques en one-pager partageable avec Copilot Spaces",
                    "features": ["spaces", "chat"],
                    "situation": "Tu as des notes de réunion, du contexte KPI et un récit encore flou, et tu veux mieux qu’un mur de bullet points.",
                    "steps": [
                        "Crée un Space avec les notes stratégiques, le tableau KPI et le vocabulaire interne de référence.",
                        "Demande à Copilot Chat un résumé une page avec priorités, risques et prochaines actions en langage clair.",
                        "Relis le texte, puis publie ou exporte la version à partager.",
                    ],
                    "result": "Une page de pilotage plus claire, ancrée dans le vrai matériau interne.",
                    "further": "Réutilise le même Space pour les mises à jour mensuelles ou trimestrielles afin de garder un vocabulaire cohérent.",
                },
                22: {
                    "title": "Construire une page de résultats de recherche ancrée dans tes figures",
                    "features": ["spaces", "chat"],
                    "situation": "Tu veux une page publique expliquant tes résultats tout en restant fidèle au résumé, aux figures et aux notes de conférence déjà validées.",
                    "steps": [
                        "Crée un Space avec le résumé, les légendes de figures, le texte du poster et les notes de vulgarisation.",
                        "Demande à Copilot Chat une page de résultats avec encadré méthode et résumé clair pour des non-spécialistes.",
                        "Relis le texte puis publie la page à côté du lien vers l’article formel.",
                    ],
                    "result": "Une page de résultats ancrée, accessible et facile à réutiliser dans des talks ou suites de projet.",
                    "further": "Ajoute une section collaboration et garde le Space comme source de diffusion pour les prochains supports.",
                },
                25: {
                    "title": "Publier une page d’événements de campus à partir d’un pack ancré",
                    "features": ["spaces", "chat"],
                    "situation": "Tu disposes d’exports calendrier, de textes d’affiche et de notes d’accessibilité, et tu veux une page plus propre que des affiches dispersées.",
                    "steps": [
                        "Crée un Space avec titres, dates, descriptions et notes d’accessibilité des événements.",
                        "Demande à Copilot Chat une page qui trie les événements par date et met en avant les prochains rendez-vous.",
                        "Publie la page sur GitHub Pages et mets à jour le Space chaque mois au lieu de repartir de zéro.",
                    ],
                    "result": "Une page d’événements légère, plus simple à maintenir qu’une archive d’affiches statiques.",
                    "further": "Ajoute un bloc “contacter l’organisation” et réutilise la même structure mois après mois.",
                },
            },
        },
    },
    "nl": {
        "nav": {
            "plans": "Plannen & realiteit",
            "scenarios": "8 echte scenario’s",
            "courses_menu": "Leertrajecten",
            "mobile_group_learn": "Leren",
            "mobile_group_resources": "Hulpmiddelen",
            "mobile_group_tools": "Tools",
        },
        "home": {
            "cta_primary": "Bekijk 8 echte scenario’s",
            "cta_primary_page": "scenarios",
            "cta_secondary": "Vergelijk plannen en gratis instaproutes",
            "cta_secondary_page": "plans",
            "cta_tertiary": "Start met het begeleide traject",
            "cta_tertiary_page": "basics",
            "hero_note": "Start vandaag op github.com/copilot en kies daarna het pad dat past bij je rol: onderwijs, studenten, IT, HR, directie, financiën, onderzoek of bibliotheek/campusdiensten.",
            "journey_title": "Van een echt campusprobleem naar een gepubliceerde app",
            "journey_sub": "Dezelfde praktische lus werkt voor onderwijs, support, administratie en onderzoek.",
            "courses_sub": "Gebruik de begeleide trajecten om de reflex op te bouwen en pas de methode daarna toe op je faculteit, dienst, labo, bibliotheek of opleiding.",
            "scenario_section_title": "Een paar concrete scenario’s om het tastbaar te maken",
            "scenario_section_sub": "De scenariopagina werkt de acht volledige routes uit. Begin hier met vier korte rolgerichte inkijkjes en open daarna het volledige overzicht voor de stap-voor-stapversie.",
            "scenario_section_cta": "Bekijk de 8 volledige scenario’s",
            "start_free_title": "Hoe je vandaag start",
            "start_free_sub": "Kies de ingang die je huidige blokkade wegneemt: setup, eerste oefening of zicht op wie nog gratis kan starten.",
            "impact_stats": [
                {"value": 26, "label": "filterbare use cases", "desc": "Voor acht rollen in het hoger onderwijs"},
                {"value": 25, "label": "begeleide lessen", "desc": "Van eerste prompt tot gepubliceerde app"},
                {"value": 8, "label": "vlaggenschipscenario’s", "desc": "Van docent tot bibliotheek, allemaal gebaseerd op echte features"},
                {"value": 5, "label": "individuele plannen", "desc": "Free, Student, Pro, Pro+ en Max"},
            ],
            "hero_visual": {
                "title": "Van prompt naar prototype",
                "badges": ["Chat", "Spaces", "Agent-modus", "GitHub Pages"],
                "lines": [
                    "Open github.com/copilot",
                    "Beschrijf een echt campusprobleem",
                    "Laat Copilot de eerste versie opzetten",
                    "Publiceer het resultaat via GitHub Pages",
                ],
            },
            "start_free_cards": [
                {
                    "icon": "🧪",
                    "title": "Start met je eerste commit",
                    "desc": "De begeleide beginnerspagina brengt je van GitHub-account naar eerste repository en legt de browser-, CLI- en Desktoppaden uit — inclusief waar de gratis routes voor studenten en docenten passen.",
                    "cta": "Volg de begeleide pagina",
                    "page": "first_commit",
                    "badge": "Begin hier",
                    "featured": True,
                },
                {
                    "icon": "⚡",
                    "title": "Probeer Copilot in de browser",
                    "desc": "Wil je eerst kijken zonder iets te installeren? Open Copilot Chat op github.com/copilot en test een echte prompt vóór je lokale setup aanraakt.",
                    "cta": "Open github.com/copilot",
                    "href": "https://github.com/copilot",
                },
                {
                    "icon": "🎓",
                    "title": "Bekijk de gratis routes",
                    "desc": "Zie wie in 2026 nog gratis start: Copilot Student voor geverifieerde studenten, gratis Copilot Pro voor geverifieerde docenten en waar betaald organisatiegebruik voor andere rollen begint.",
                    "cta": "Bekijk plannen & realiteit",
                    "page": "plans",
                },
            ],
            "start_free_links_label": "Ga daarna verder met",
            "start_free_links": [
                {"label": "36 concrete use cases", "page": "explorer"},
                {"label": "Bouwen of kopen", "page": "build_vs_buy"},
            ],
            "scenario_teaser_ids": ["teacher", "student", "it", "leadership"],
            "scenario_examples_label": "Nog vier ideeën uit andere rollen",
        },
        "home_personas": [
            ("🎓", "Docenten", "Bouw eindelijk die cursusbegeleider, quiz, herhalingspagina of nakijkhulp die al lang in je hoofd zit.", "Voorbeeld:", "Een docent chemie publiceert nog voor de volgende practicumweek een gegronde herhalingsmicrosite."),
            ("🧑‍🎓", "Studenten", "Verander een eindprojectidee in een werkende app, branch per branch, met codereview vóór de indiening.", "Voorbeeld:", "Een studententeam bouwt een prototype voor labomateriaalreservatie in plaats van enkel een statische mock-up."),
            ("🖥️", "IT- en digitale diensten", "Draai meerdere agentsessies parallel, houd controle met Plan-modus en keur pas daarna diffs goed.", "Voorbeeld:", "IT werkt drie backlogtickets parallel af in de GitHub Copilot-app."),
            ("🤝", "HR", "Veranker Copilot in echte procedures, sjablonen en onboardingmateriaal zodat antwoorden dicht bij het beleid blijven.", "Voorbeeld:", "HR maakt van beleids-pdf’s een onboardingassistent zonder zelf een backend te bouwen."),
            ("🧭", "Directie en beleid", "Automatiseer wekelijkse syntheses met aangepaste agents en geplande cloud-agent-runs.", "Voorbeeld:", "Een directieteam krijgt elke vrijdag één KPI-samenvatting die klaarstaat als PR."),
            ("💶", "Financiën en administratie", "Zet exports snel om in dashboards en houd het kostenverhaal eerlijk dankzij gedeelde AI credits.", "Voorbeeld:", "Het financeteam zet een maandexport in enkele minuten om in een variatiedashboard."),
            ("🔬", "Onderzoekers", "Verbind vertrouwde data via MCP en laat Copilot het Python- of R-script genereren dat je kunt inspecteren en herhalen.", "Voorbeeld:", "Een onderzoeksteam stelt natuurlijke vragen over retentiedata en krijgt het notebook achter de grafiek."),
            ("📚", "Bibliotheek, campus en studentendiensten", "Bouw een lichte reservatie-, inventaris-, FAQ- of evenemententool zonder te wachten op een volledig maatwerkproject.", "Voorbeeld:", "Bibliotheekmedewerkers publiceren een kleine ruimteboekingsapp voor de semesterstart."),
        ],
        "home_examples": [
            ("Onboarding-vragenhub", "Een HR-assistent die gegrond is in echte personeelsprocedures.", "HR"),
            ("Budgetvariatiedashboard", "Een dashboard van één pagina uit een Excel- of CSV-export.", "Financiën"),
            ("Dataset-queryassistent", "Natuurlijke vragen over vertrouwde data, met het script achter het antwoord.", "Onderzoek"),
            ("Bibliotheek-reservatieprototype", "Een kleine GitHub Pages-pagina voor ruimtes, slots en toegankelijkheidsinfo.", "Bibliotheek"),
        ],
        "best_practices": {
            "title": "Best practices",
            "sub": "Een checklist van één pagina om sterk te starten, feitelijk te blijven en je uitrol realistisch te houden van eerste prompt tot institutionele adoptie.",
            "items": [
                ("Vertrek van een echt campusprobleem", "De beste ideeën komen uit terugkerend werk, frictie of gemiste kansen die personeel of studenten wekelijks voelen."),
                ("Begin klein en itereer daarna", "Een kleine pagina die werkt en gebruikt wordt is meer waard dan een groots concept dat nooit verschijnt."),
                ("Eén wijziging, één test, één commit", "Kleine stappen maken het werk leesbaar, testbaar en omkeerbaar."),
                ("Bewaar alles op GitHub vanaf dag één", "Zelfs een mini-prototype verdient versiegeschiedenis, back-up en een eenvoudige publicatieroute."),
                ("Controleer vroeg op welk plan je echt recht hebt", "Studenten kunnen Copilot Student aanvragen, geverifieerde docenten gratis Copilot Pro, en breder personeel valt onder een betaalde Business- of Enterprise-beslissing."),
                ("Veranker Copilot vóór je het antwoord vertrouwt", "Spaces, instructies, prompt files en MCP-servers brengen Copilot dichter bij je echte documenten en data."),
                ("Gebruik .github/copilot-instructions.md", "Schrijf de conventies, buildstappen en stijlregels op die je anders elke sessie opnieuw moet uitleggen."),
                ("Houd geheimen en persoonsgegevens uit de browser", "API-sleutels horen in beschermde secrets, en student- of HR-data vraagt een sobere en expliciete aanpak."),
                ("Bekijk elke suggestie voordat je ze accepteert", "Copilot stelt voor; de menselijke goedkeuring blijft het controlepunt."),
                ("Test met echte mensen vóór je opschaalt", "Een proef met tien mensen leert vaak meer dan een reeks abstracte vergaderingen over “AI-strategie”."),
                ("Houd persoonlijke instructies kort en concreet", "Enkele precieze regels die Copilot echt volgt, verslaan een lang document dat het overslaat. Schrijf conventies, geen filosofie."),
                ("Houd een korte trace bij van wat een agent wijzigde", "Eén regel per agentsessie — wat veranderde, waarom, wat te checken — bespaart echte tijd wanneer meerdere mensen dezelfde repository delen."),
            ],
        },
        "about": {
            "title": "Over dit traject",
            "paragraphs": [
                "Vibe Coding Copilot is een onafhankelijke, gratis leerbron voor het hoger onderwijs: docenten, studenten, IT, HR, directie, financiën, onderzoek, bibliotheek en campusdiensten die met GitHub Copilot en GitHub praktische tools willen bouwen.",
                "Deze site is niet verbonden aan, goedgekeurd door of gesponsord door GitHub of Microsoft. Het doel is instellingen helpen om realistische adoptiebeslissingen te nemen op basis van feiten — ook waar gratis routes stoppen en betaalde organisatie-uitrol begint.",
            ],
            "sections": [
                ("Waarom dit traject bestaat", [
                    "Te veel goede ideeën blijven steken achter een ticketrij, een budgetlijn of de zin “daar hebben we een volledig project voor nodig”. Vibe coding verlaagt die drempel door domeinkennis om te zetten in prototypes en kleine apps."
                ]),
                ("Waarom precies GitHub", [
                    "GitHub levert het tweede deel van het verhaal: repositories, branches, pull requests, GitHub Pages en een natuurlijke thuisbasis voor Copilot. Het GitHub Campus Program kan GitHub Enterprise Cloud of Server zelfs aan de hele instelling leveren, maar die platformtoegang is niet hetzelfde als gratis Copilot-stoelen voor elke personeelsrol."
                ]),
                ("De eerlijke uitrolrealiteit in 2026", [
                    "Studenten kunnen nog altijd gratis Copilot Student krijgen. Geverifieerde docenten kunnen nog altijd gratis Copilot Pro krijgen op individuele basis. Maar brede uitrol voor IT, HR, financiën, directie, administratie, onderzoekssteun en andere functies vraagt nu om Copilot Business of Copilot Enterprise, vaak via een Sales-gesprek in plaats van wrijvingsloze self-serve."
                ]),
                ("Feedback", [
                    "Behandel deze site als levend lesmateriaal. Als een scenario, les of feitelijke nuance scherper kan, verbeter het dan met echte voorbeelden en degelijke bronnen."
                ]),
            ],
        },
        "quiz_ui": {
            "eyebrow": "Quiz van het traject",
            "score_label": "Score",
            "answered_label": "Beantwoord",
            "correct_label": "Correct",
            "wrong_label": "Nog niet",
            "reset_label": "Quiz opnieuw starten",
            "success_message": "Sterk afgerond — je bent klaar voor de volgende stap.",
            "retry_message": "Goede start — lees de uitleg opnieuw en probeer nog eens.",
            "why_label": "Waarom dit belangrijk is",
        },
        "plans": {
            "title": "Plannen & realiteit",
            "sub": "De eerlijke kaart voor 2026: sommige individuele onderwijsroutes blijven gratis, maar institutionele adoptie voor alle rollen loopt nu via een betaald organisatieplan.",
            "stat_cards": [
                {"value": 5, "label": "individuele plannen", "desc": "Van Copilot Free tot Max"},
                {"value": 2, "label": "organisatieplannen", "desc": "Business en Enterprise"},
                {"value": 50000, "label": "GitHub Actions-minuten van het Campus Program", "desc": "Per instelling, met 50 GB Packages"},
                {"value": 0, "label": "meerprijs voor completions", "desc": "Codecompletions en next edit suggestions blijven onbeperkt op betaalde plannen"},
            ],
            "individual_title": "Individuele plannen",
            "individual_intro": "Alle individuele plannen bevatten Copilot CLI en de GitHub Copilot-app. De echte verschillen zitten in limieten, premiummodellen en wie via onderwijs of open source een gratis route heeft.",
            "individual_columns": ["Plan", "Prijs", "Voor wie", "Gratis route", "Realiteitscheck"],
            "individual_rows": [
                plan_row("Copilot Free", "$0", "Iedereen met een GitHub-account", "Geen aanvraag nodig", ["2.000 completions per maand", "Alleen automatische modelselectie", "Geen premiummodellen", "Beperkte Chat"]),
                plan_row("Copilot Student", "$0", "Geverifieerde studenten", "Aanvragen via GitHub Education", ["Volledig studentenplan", "Sluit third-party coding agents uit", "Maandelijkse herverificatie", "Niet zelf opzegbaar zodra toegekend"], "Studenten"),
                plan_row("Copilot Pro", "$10 / maand", "Gevorderd individueel gebruik", "Gratis voor geverifieerde docenten en bepaalde populaire open-source-maintainers", ["Dit is het specifieke gratis docentvoordeel", "Goede standaard voor individueel betaald gebruik", "Inclusief CLI en GitHub Copilot-app"], "Docenten"),
                plan_row("Copilot Pro+", "$39 / maand", "Zwaarder individueel gebruik", "Geen vaste gratis route", ["Meer AI credits", "Premiummodellen", "Hoger plafond dan Pro"]),
                plan_row("Copilot Max", "$100 / maand", "Maximale individuele capaciteit", "Geen vaste gratis route", ["Hoogste individuele tier", "Meer AI credits", "Premiummodellen"]),
            ],
            "org_title": "Organisatie- en enterpriseplannen",
            "org_intro": "Dit is de route voor brede uitrol binnen de instelling, voorbij de mensen die individueel al door student- of docentregelingen worden gedekt.",
            "org_cards": [
                {
                    "icon": "🏫",
                    "title": "Copilot Business",
                    "price": "$19 / seat / maand",
                    "credits": "1.900 AI credits per gebruiker per maand inbegrepen (promotioneel 3.000 tot 1 september 2026)",
                    "note": "Sinds 22 april 2026 zijn nieuwe self-serve sign-ups tijdelijk gepauzeerd voor organisaties op GitHub Free en GitHub Team.",
                    "bullets": ["Geschikt voor staff-brede uitrol met beleid en governance", "Codecompletions en next edit suggestions blijven onbeperkt", "Chat, CLI, Spaces, cloud agent en gelijkaardige agentische functies gebruiken gedeelde AI credits"],
                },
                {
                    "icon": "🛡️",
                    "title": "Copilot Enterprise",
                    "price": "$39 / seat / maand",
                    "credits": "3.900 AI credits per gebruiker per maand inbegrepen (promotioneel 7.000 tot 1 september 2026)",
                    "note": "Vereist GitHub Enterprise Cloud en wordt opgezet via GitHub Sales.",
                    "bullets": ["Enterprise-governance en admincontrole", "Meer inbegrepen credits dan Business", "Ontworpen voor brede uitrol en policy-managed omgevingen"],
                },
            ],
            "ocre_title": "En het OCRE-framework dan?",
            "ocre_text": "GitHub Copilot staat niet als apart product in de OCRE-catalogus. Als je instelling echter al een Azure-contract heeft via een aan OCRE gekoppelde aankoopcentrale, kan Copilot Business of Enterprise doorgaans worden geactiveerd als verbruiksgebaseerde facturering op datzelfde Azure-abonnement — een onrechtstreekse maar reële route, te bevestigen bij je Azure-reseller.",
            "ocre_cta_label": "Mijn instelling wil de OCRE-route verkennen",
            "ocre_mailto_subject": "Interesse van onze instelling in de OCRE-route voor GitHub Copilot",
            "ocre_mailto_body": "Hallo Sébastien en Jochem,\n\nOnze instelling wil de OCRE-route verkennen om GitHub Copilot Business/Enterprise te activeren via ons bestaande Azure-contract.\n\nNaam van de instelling:\nIT/aankoopcontact:\nHuidige Azure-context (reseller, aankoopcentrale):\n\nGraag contact opnemen om dit te bespreken.\n\nMet vriendelijke groeten,",
            "pool_title": "AI credits worden gedeeld, niet opgesloten per persoon",
            "pool_intro": "Dat maakt het financiële gesprek veel eerlijker: zware en lichte gebruikers compenseren elkaar, terwijl routine-autocomplete onbeperkt blijft doorstromen zonder credits te verbruiken.",
            "pool_total_label": "Voorbeeld van een Business-pool",
            "pool_total": 5700,
            "pool_total_suffix": "credits gedeeld over 3 seats",
            "pool_users": [
                {"name": "Lichte gebruiker", "used": 250, "note": "Opent Chat twee keer per dag"},
                {"name": "Projectleider", "used": 1200, "note": "Gebruikt Chat, CLI en één Space"},
                {"name": "Intensieve bouwer", "used": 3200, "note": "Werkt de hele week met agentische functies"},
            ],
            "pool_bullets": [
                "1 credit = $0,01.",
                "Business bevat 1.900 credits per gebruiker per maand; Enterprise bevat er 3.900.",
                "Codecompletions en next edit suggestions worden op betaalde plannen niet in credits aangerekend.",
            ],
            "campus_title": "GitHub Campus Program: sterke platformstory, aparte Copilot-realiteit",
            "campus_intro": "Het Campus Program blijft een grote strategische troef — alleen niet meer als verhaal van gratis Copilot voor iedereen.",
            "campus_cards": [
                {"icon": "🏛️", "title": "GitHub-platform voor de hele instelling", "desc": "Geaccrediteerde instellingen die diploma’s, certificaten of graden toekennen kunnen GitHub Enterprise Cloud of Server krijgen voor de hele instelling, over academische en technische afdelingen heen."},
                {"icon": "⚙️", "title": "Inbegrepen platformcapaciteit", "desc": "50.000 GitHub Actions-minuten en 50 GB Packages-opslag zijn inbegrepen, met jaarlijkse vernieuwing zolang aan de voorwaarden voldaan blijft."},
                {"icon": "🧾", "title": "Wat het niet automatisch geeft", "desc": "Het geeft niet automatisch gratis Copilot-seats aan elke personeelsrol. Studenten en in aanmerking komende docenten gebruiken nog altijd hun individuele routes; andere functies vallen onder een betaald organisatieplan."},
            ],
            "cta_title": "Start via de juiste ingang",
            "cta_cards": [
                {"title": "Onmiddellijke browserdemo", "desc": "Open Copilot Chat zonder installatie en test je eerste prompt.", "label": "github.com/copilot", "href": "https://github.com/copilot"},
                {"title": "Studenten- of docentroute", "desc": "Controleer GitHub Education voor Copilot Student of gratis Copilot Pro.", "label": "github.com/education", "href": "https://github.com/education"},
                {"title": "Campus Program-aanvraag", "desc": "Instellingsleiders kunnen het GitHub Campus Program aanvragen.", "label": "education.github.com/schools", "href": "https://education.github.com/schools"},
                {"title": "Brede uitrol binnen de instelling", "desc": "Wanneer je voorbij individueel gedekte gebruikers gaat, plan dan een Sales-gesprek over Business of Enterprise.", "label": "Praat met GitHub Sales", "href": "https://github.com/customer-stories?type=sales"},
            ],
        },
        "scenarios": {
            "title": "Acht echte scenario’s per rol",
            "sub": "Gebruik ze als demo, workshopscript of intern adoptieverhaal. Elk scenario hieronder is verankerd in een echte GitHub Copilot-feature uit de officiële documentatie.",
            "jump_label": "Ga naar een rol",
            "steps_label": "Wat er gebeurt",
            "deliverables_label": "Concreet resultaat",
            "impact_label": "Waarom dit aanslaat",
            "items": [
                scenario_item("teacher", "🎓", "Docent", "Live iets zichtbaars bouwen zonder zware installatie.", "Een docent heeft een cursusoverzicht, wil een herhalingsquiz en één oefenpagina, maar wil niet eerst een volledige toolchain optuigen om het idee te testen.", ["Copilot Chat", "GitHub Pages", "Copilot Spaces"], "Ik geef eerstejaars microbiologie. Bouw een GitHub Pages-vriendelijke minisite met één index.html, één style.css en één script.js. Ik wil 6 meerkeuzevragen, één casusoefening, directe feedback en een resetknop. Hou de taal studentvriendelijk.", "Hier is een eerste versie met de drie bestanden, een nette lay-out en de eerste zes vragen klaar om op jouw cursus af te stemmen. Ik heb ook commentaar toegevoegd zodat je snel kunt aanpassen vóór publicatie.", ["Open github.com/copilot in de browser en plak het cursusoverzicht.", "Vraag Copilot Chat om een eerste statische versie die je meteen via GitHub Pages kunt publiceren.", "Maak daarna een Copilot Space “Mijn syllabus” met slides, readings en begrippenlijst zodat toekomstige antwoorden in dit vak gegrond blijven."], ["Een werkende herhalingspagina in een repository", "Een GitHub Pages-URL die je dezelfde dag kunt delen", "Een herbruikbare Space voor de volgende opdracht of FAQ"], "Het wow-effect is direct: je praat niet over AI, je toont een echt onderwijsartefact dat al bestaat."),
                scenario_item("student", "🧑‍🎓", "Student", "Van eindprojectidee naar werkende app, branch per branch.", "Een studententeam heeft een projectbrief, weinig tijd en wil van idee naar MVP gaan terwijl het de code nog altijd begrijpt.", ["Copilot Student", "Agent-modus", "Copilot code review"], "Agent-modus: bouw een minimum viable app voor reservatie van labomateriaal voor een eindproject. Start met een landingspagina, aanvraagformulier, adminlijst, README en voeg daarna één feature per branch toe. Leg elke grote wijziging uit vóór je ze toepast.", "Ik kan beginnen met het repo-plan, de eerste branch opzetten en daarna reviewbare wijzigingen openen voor formulier en adminweergave afzonderlijk zodat het project begrijpelijk blijft.", ["Gebruik het gratis Copilot Student-voordeel in VS Code.", "Laat Agent-modus het MVP branch per branch opzetten in plaats van één enorme sprong te maken.", "Laat Copilot code review vóór de indiening op de pull requests draaien zodat het team gerichte verbeterpunten krijgt."], ["Een werkend MVP in plaats van enkel een conceptnota", "Een duidelijkere branch- en commitgeschiedenis voor begeleiders", "Reviewcommentaar dat de codekwaliteit vóór de indiening versterkt"], "De ervaring blijft hands-on: Copilot versnelt, maar de branchstructuur en reviewcyclus houden het leren zichtbaar."),
                scenario_item("it", "🖥️", "IT & digitale diensten", "Meerdere interne tickets parallel aanpakken zonder controle te verliezen.", "Een IT-team heeft een stapel kleine tickets — een pagina restylen, een script migreren, een formulier verbeteren — en wil snelheid zonder chaos.", ["GitHub Copilot-app", "Parallelle agents", "Plan-modus"], "Maak drie Plan-modussessies: 1) migreer dit CSV-opruimscript naar Python, 2) vernieuw de startpagina van de personeelsgids, 3) voeg gestructureerde logging toe aan de ruimteboekingsservice. Houd elke taak in zijn eigen worktree en toon het plan vóór er iets wordt aangepast.", "Ik heb drie aparte plannen klaargezet, elk in zijn eigen sessie en branch. Het team hoeft alleen de diffs te bekijken en goed te keuren wat deze week echt moet landen.", ["Start de GitHub Copilot-app en open meerdere agentsessies parallel.", "Blijf in Plan-modus zodat het team plannen en diffs bekijkt vóór uitvoering.", "Gebruik de native GitHub-integratie om elke goedgekeurde wijziging in de normale branch / PR / CI-flow te brengen."], ["Drie parallelle werkstromen in plaats van één geblokkeerde rij", "Reviewbare diffs per ticket", "Een sneller backlogsritme met menselijke goedkeuring in de lus"], "Hier voelt agent-driven development operationeel nuttig: parallel, geïsoleerd en reviewbaar."),
                scenario_item("hr", "🤝", "HR", "Een interne assistent bouwen die in beleid verankerd is, zonder zelf een backend te schrijven.", "HR beantwoordt voortdurend dezelfde vragen over onboarding, verlof of contractsjablonen en wil antwoorden die aansluiten op de echte documenten.", ["Copilot Spaces", "Copilot Chat"], "Maak een Space “HR-beleid” met onboardinggidsen, verlofprocedures, contractsjablonen en FAQ-notities. Stel daarna een personeelsgerichte vragenpagina op die de 12 meest voorkomende vragen beantwoordt en per antwoord duidelijk naar de bron verwijst.", "Ik heb het bronmateriaal gegroepeerd, antwoordpatronen opgesteld die op die documenten steunen, en een heldere FAQ-pagina gemaakt die HR kan nalezen vóór interne publicatie.", ["Maak één Space met het canonieke HR-materiaal.", "Gebruik Copilot Chat op die Space om antwoorden en een eenvoudige FAQ-pagina op te stellen.", "Lees na, pas de toon aan en publiceer de goedgekeurde versie als intern referentiepunt."], ["Een FAQ die in documenten verankerd is in plaats van nog een overlopende mailbox", "Snellere antwoorden voor personeel", "Een herbruikbare Space die toekomstige HR-prompts verbetert"], "De echte winst is vertrouwen: mensen krijgen antwoorden uit de documenten van de instelling zelf, niet uit generieke webtaal."),
                scenario_item("leadership", "🧭", "Directie", "Wekelijkse KPI-jacht omzetten in een geplande, reviewbare synthese.", "Een directie of diensthoofd wil één beknopt wekelijks beeld over meerdere teams zonder alles handmatig samen te voegen.", ["Custom agents", "Copilot cloud agent", "Automations"], "Definieer in .github/agents/reporting.md een agent die KPI-bestanden uit /finance, /student-success, /research en /operations leest en vervolgens een weekly-summary.md met successen, risico’s en open vragen schrijft. Plan de run elke vrijdagmiddag en open een pull request in plaats van main rechtstreeks te wijzigen.", "Ik kan die aangepaste agentinstructies volgen, de bronbestanden samenbrengen en een reviewbare PR openen met de voorgestelde samenvatting zodat de directie het narratief goedkeurt vóór het gedeeld wordt.", ["Maak een aangepaste agentpersona die bij de gewenste rapportagestijl past.", "Plan een wekelijkse run van de Copilot cloud agent.", "Bekijk een PR in plaats van een ondoorzichtige bijlage vóór de samenvatting wordt verspreid."], ["Een reproduceerbaar wekelijks rapportageritueel", "Eén PR waar directie commentaar op kan geven", "Minder coördinatietijd verloren aan het kopiëren van statusupdates"], "De directie krijgt de snelheid van automatisering en behoudt tegelijk het institutionele reviewmoment vóór publicatie."),
                scenario_item("finance", "💶", "Financiën", "Een maandelijks exportbestand in minuten omzetten in een dashboard mét begrijpelijk kostenverhaal.", "Het financeteam ontvangt bij elke cyclus dezelfde Excel- of CSV-export en wil een licht dashboard in plaats van telkens dezelfde spreadsheetweergave opnieuw op te bouwen.", ["Prompt files", "Copilot Chat", "AI credits"], "Gebruik .github/prompts/rapport-budget.prompt.md met de invoer [exportbestand] en [maand]. Zet het bijgevoegde budgetexport om in een statisch dashboard met variatiekaarten, een sorteerbare tabel en overschrijdingswaarschuwingen. Houd alle berekeningen zichtbaar in code en schat het AI-creditgebruik van deze run.", "Ik heb het prompt-file-sjabloon voorbereid, de export omgezet in een dashboard van één pagina en de formules zichtbaar gehouden zodat het team zowel de cijfers als het proces kan auditen.", ["Maak één gedeeld prompt file voor deze terugkerende financiële workflow.", "Voer maandelijks gewoon het actuele exportbestand in in plaats van de taak opnieuw uit te leggen.", "Volg die run binnen de gedeelde AI-creditpool van de organisatie in plaats van te gissen naar een vlak mysteriebedrag."], ["Een herbruikbare dashboardworkflow", "Zichtbare berekeningen in code", "Een concreet financieel verhaal waarom gedeelde AI credits beter bestuurbaar zijn dan giswerk"], "Financiën hoeven geen hype te kopen: het resultaat spreekt in snellere rapportering en transparanter kostbeheer."),
                scenario_item("research", "🔬", "Onderzoek", "Een dataset natuurlijke taalvragen laten beantwoorden en toch het script achter het antwoord krijgen.", "Onderzoekers willen sneller bij vertrouwde data, maar hebben ook reproduceerbaarheid en een controleerbaar analysepad nodig.", ["MCP servers", "Copilot Chat", "Python / R-scriptgeneratie"], "Gebruik de goedgekeurde retention-data-MCP-server om retentie voor cohorten 2022 tot 2025 per faculteit te vergelijken. Genereer daarna het Python-notebook dat de grafiek reproduceert en voorzie commentaar bij elke transformatiestap.", "Ik kan de gekoppelde bron bevragen, de vergelijking in gewone taal samenvatten en het notebook genereren zodat het team de methode kan herhalen of aanpassen.", ["Verbind een goedgekeurde MCP-server met de relevante dataset.", "Stel de vraag in Copilot Chat in plaats van eerst handmatig de eerste query bijeen te puzzelen.", "Neem het gegenereerde Python- of R-script als reproduceerbaar artefact voor review, hergebruik of communicatie."], ["Een sneller pad van vraag naar eerste analyse", "Een script dat het team kan inspecteren en opnieuw kan uitvoeren", "Een gegronde workflow die onderzoekstraceerbaarheid respecteert"], "Je behoudt het gemak van natuurlijke taal zonder de reproduceerbaarheid op te offeren die onderzoek nodig heeft."),
                scenario_item("campus", "📚", "Bibliotheek / campusdiensten", "Een niet-ontwikkelteam laten landen met een nuttige mini-app dit semester.", "Bibliotheek- of campusmedewerkers hebben een eenvoudige ruimteboekings- of inventaristool nodig en willen snel iets bruikbaars.", ["Agent-modus", "GitHub Pages", "GitHub Campus Program"], "Bouw een statisch prototype voor ruimteboekingen in de bibliotheek: datumkiezer, ruimtekaarten, bezet/vrij-status met fictieve data, toegankelijkheidsnotities en een GitHub Pages-deployworkflow. Houd de structuur eenvoudig genoeg zodat niet-ontwikkelaars later zelf kunnen onderhouden.", "Ik heb een kleine statische app opgezet, toegankelijke ruimtekaarten toegevoegd en een deployworkflow voorzien, terwijl de contentbestanden eenvoudig genoeg blijven voor het serviceteam na de lancering.", ["Gebruik Agent-modus om de eerste versie snel op te zetten.", "Host de app op GitHub Pages binnen de GitHub-platformvoetafdruk van de instelling.", "Houd de inhoud zo bewerkbaar dat bibliotheek- of campusmedewerkers na de lancering eigenaar kunnen blijven."], ["Een werkend serviceprototype in plaats van een lange wachtlijst", "Gratis statische hosting via GitHub Pages", "Een tastbaar voorbeeld van wat het Campus Program-platform mogelijk maakt"], "Het team ziet meteen de waarde omdat het resultaat een bruikbare servicepagina is, geen abstracte AI-pilot."),
            ],
        },
        "tracks": {
            "basics": {
                "subtitle": "Je eerste stappen in vibe coding: verander een echt campusprobleem in een nuttige app met GitHub Copilot.",
                "card_desc": "Ontdek vibe coding, bouw je eerste nuttige webapp met Copilot en publiceer ze online.",
                "lesson_updates": {
                    1: {
                        "title": "Van een echt campusprobleem naar een app-idee",
                        "paragraphs": [
                            "Het beste vertrekpunt is nooit een technologie, maar een echt campusprobleem: studenten hebben geen eenvoudige manier om te herhalen, een dienst beantwoordt steeds dezelfde vraag per e-mail, een team volgt een budgetlijn in tien spreadsheets, een labo wil een lichte reservatiepagina. Vertrek van echte frictie.",
                            "Beschrijf dat probleem in één zin en bedenk dan de kleinst mogelijke app die die frictie vermindert. Een quiz, een pagina, een calculator, een tracker, een doorzoekbare FAQ: houd de eerste versie eenvoudig en breid pas uit zodra echte mensen ze gebruiken.",
                        ],
                    },
                    2: {
                        "paragraphs": [
                            "Dit is de les waarin je echt iets bouwt. Installeer de GitHub Copilot-extensie in Visual Studio Code, of open Copilot Chat rechtstreeks op github.com/copilot met je GitHub-account, en maak daarna een nieuw index.html-bestand aan.",
                            "Hieronder bouwen we samen een echt werkend voorbeeld: een “Snelle Peiling” die je in een les, opleiding, teamvergadering of personeelsbijeenkomst kunt gebruiken. Volg de stappen met je eigen Copilot en probeer het resultaat op het einde live uit.",
                        ],
                    },
                    5: {
                        "paragraphs": [
                            "Zodra je app nuttig is, vraag je Copilot om de presentatie te verbeteren: kleuren van de instelling, leesbaardere spacing, toegankelijkere tekst en een duidelijkere visuele hiërarchie. Je kunt ook een kleine Copilot Space maken met slides, een stijlgids of voorbeeldtekst zodat suggesties gegrond blijven in je eigen materiaal.",
                            "Denk ook aan toegankelijkheid: voldoende contrast, leesbare tekst, duidelijke labels en knoppen die gemakkelijk te gebruiken zijn. Vraag Copilot expliciet om die punten te controleren vóór publicatie.",
                        ],
                    },
                },
                "quiz": quiz("Basisquiz — kun je een eerste app veilig lanceren?", "Vijf snelle controles voordat je doorgaat. Lees de uitleg meteen na elk antwoord.", [
                    q("Waar kun je Copilot Chat zonder installatie uitproberen?", ["Alleen in VS Code", "Op github.com/copilot", "Alleen in GitHub Desktop", "Alleen in de mobiele app"], 1, "github.com/copilot is het browserinstappunt zonder installatie en een sterke eerste demo."),
                    q("Wat is de beste eerste vorm voor een vibe-codingproject?", ["Een mini-versie die al werkt", "Een volledig platform met alle geplande functies", "Eerst een groot architectuurdocument", "Eerst een perfecte huisstijl, dan pas code"], 0, "Een kleine werkende versie geeft je meteen iets om te testen, publiceren en verbeteren."),
                    q("Waarom zet je zelfs een heel klein project vroeg op GitHub?", ["Alleen om indruk te maken", "Omdat GitHub het voor altijd automatisch privé maakt", "Voor back-up, versiegeschiedenis en eenvoudige publicatie", "Omdat Copilot anders weigert te werken"], 2, "GitHub geeft je back-up, branches, commits en een directe weg naar GitHub Pages."),
                    q("Wat is de veiligste manier om een app met Copilot te verbeteren?", ["Tien wijzigingen ineens vragen", "Eén wijziging, één test, één commit", "Nooit testen tot het einde", "Alles telkens volledig herschrijven"], 1, "Kleine, testbare stappen maken het proces begrijpelijk en omkeerbaar."),
                    q("Wie houdt de controle wanneer Copilot code voorstelt?", ["Copilot alleen", "De browsercache", "Jij: je leest, past aan en keurt goed", "Wie het repo als eerste publiceerde"], 2, "Copilot is een voorstelsysteem; menselijke goedkeuring blijft het controlepunt."),
                ]),
            },
            "advanced": {
                "subtitle": "Koppel een database, geef je project duurzame instructies en beheer je code als een echt project dat moet standhouden.",
                "lesson_updates": {
                    6: {
                        "paragraphs": [
                            "Zonder specifieke instructies onthoudt Copilot niet automatisch alle projectconventies. Plaats een bestand .github/copilot-instructions.md in de repository en noteer de regels die je anders elke sessie herhaalt: naamgeving, toon, buildstappen, toegankelijkheidsvereisten of visuele afspraken.",
                            "Later kun je dat aanvullen met prompt files, gerichte instructiebestanden, AGENTS.md of gespecialiseerde agents. Begin met dat ene altijd actieve bestand zodat het project niet telkens terugvalt naar “generiek”.",
                        ],
                        "exercise": "Maak je eerste .github/copilot-instructions.md met minstens drie regels die in jouw context belangrijk zijn: stijl, buildstappen en één institutionele randvoorwaarde.",
                    },
                    8: {
                        "paragraphs": [
                            "Een project dat standhoudt heeft echte organisatie nodig: duidelijke commits, kleine branches, pull requests en review. Als de instelling GitHub als platform breed wil inzetten, kan het GitHub Campus Program GitHub Enterprise Cloud of Server aan de hele school leveren — maar dat is de platformlaag, niet automatisch een gratis Copilot-licentie voor elke personeelsrol.",
                            "Voor Copilot zelf kunnen studenten nog altijd individueel Copilot Student gebruiken en kunnen geverifieerde docenten nog altijd individueel gratis Copilot Pro gebruiken. Voor IT, HR, financiën, directie en andere functies vraagt brede uitrol om Copilot Business of Copilot Enterprise met de juiste governance en budgetlogica.",
                        ],
                    },
                },
                "quiz": quiz("Gevorderdenquiz — kun je opschalen zonder de controle kwijt te raken?", "Deze vragen toetsen de gewoonten die een prototype duurzaam maken in een echte instelling.", [
                    q("Wanneer is Agent-modus het nuttigst?", ["Wanneer je meerstapswijzigingen gepland en toegepast wilt krijgen met goedkeuringsmomenten", "Alleen om één variabele te hernoemen", "Alleen op mobiel", "Pas nadat een project af is"], 0, "Agent-modus blinkt uit bij grotere taken die meerdere bestanden of stappen raken."),
                    q("Wanneer heb je een database nodig?", ["Zodra je dark mode wilt", "Wanneer de app informatie tussen sessies moet onthouden", "Pas na 10.000 gebruikers", "Nooit in hoger onderwijs"], 1, "Scores, inschrijvingen, reservaties of duurzame gegevens vragen om persistentie."),
                    q("Wat is het juiste pad van het altijd actieve repository-instructiebestand?", ["instructions.txt", ".github/copilot-instructions.md", "README.instructions", "copilot.json"], 1, "Dat exacte pad is de officiële repository-ingang voor custom instructions."),
                    q("Wat is de eerlijke boodschap over Campus Program en Copilot-seats?", ["Campus Program geeft automatisch gratis Copilot aan al het personeel", "Campus Program levert het GitHub-platform, maar brede Copilot-toegang blijft een aparte planbeslissing", "Campus Program is alleen voor studenten", "Campus Program vervangt pull requests"], 1, "Platformtoegang en Copilot-seat-entitlement horen bij elkaar, maar zijn niet hetzelfde."),
                    q("Waarom werk in branches en pull requests houden?", ["Om een project ingewikkelder te maken", "Om samenwerking te vermijden", "Om wijzigingen te isoleren, te reviewen en veilig te mergen", "Omdat GitHub Pages dat vereist"], 2, "De branch/PR-flow laat een project groeien zonder dat elk experiment meteen productie wordt."),
                ]),
            },
            "expert": {
                "lesson_updates": {
                    5: {
                        "paragraphs": [
                            "Een AI-model kost iets bij elke vraag. Op betaalde Copilot-plannen voor organisaties gebruiken modelzware functies zoals Chat, CLI, Spaces, de cloud agent en vergelijkbare agentische tools AI credits — maar codecompletions en next edit suggestions blijven onbeperkt en worden niet in credits aangerekend.",
                            "Business bevat 1.900 AI credits per gebruiker per maand en Enterprise bevat er 3.900, met hogere promotionele allocaties tot 1 september 2026. Die credits worden over de hele facturatie-entiteit gedeeld, zodat zware en lichte gebruikers elkaar in evenwicht houden in plaats van elk in een apart silo te zitten.",
                        ],
                        "exercise": "Schrijf op welk deel van je workflow onbeperkte autocomplete nodig heeft en welk deel echt modelzware agentische functies vraagt. Dat onderscheid is de basis van eerlijk kostenbeheer.",
                    },
                },
                "quiz": quiz("Expertquiz — begrijp je de echte economie van een AI-uitrol?", "Deze vragen toetsen de veiligheids-, feature- en planrealiteit achter een serieuze Copilot-uitrol.", [
                    q("Wat mag nooit zichtbaar zijn in code die in de browser terechtkomt?", ["Een CSS-variabele", "Een API-sleutel van je AI-dienst", "Een paginatitel", "Een README-link"], 1, "Secrets horen in beschermde omgevingsvariabelen of GitHub-secrets, niet in client-side code."),
                    q("Welke Copilot-activiteiten worden in AI credits aangerekend op betaalde organisatieplannen?", ["Alleen codecompletions", "Chat, CLI, Spaces en agentische modelfuncties", "Git-commits", "GitHub Pages-deploys"], 1, "Modelgedreven functies verbruiken credits; routine-autocomplete niet."),
                    q("Wat blijft onbeperkt op alle betaalde plannen?", ["Pull requests", "Repositorygrootte", "Codecompletions en next edit suggestions", "Cloud-agent-PR’s"], 2, "Dat is het belangrijke “kostencontrole”-feit: autocomplete blijft onbeperkt."),
                    q("Hoe worden inbegrepen AI credits op Business en Enterprise behandeld?", ["Ze worden op facturatieniveau gedeeld", "Ze zitten voorgoed per persoon opgesloten", "Ze resetten elk uur", "Ze bestaan alleen op Copilot Free"], 0, "Gedeelde credits laten lichte en zware gebruikers elkaar in evenwicht houden."),
                    q("Wat bevat het Campus Program niet automatisch?", ["GitHub Enterprise Cloud of Server voor de instelling", "GitHub Actions-minuten en Packages-opslag", "Gratis Copilot-seats voor alle personeelsrollen", "Institutionele GitHub-geschiktheid"], 2, "Campus Program vertelt een sterk GitHub-platformverhaal, maar geen verhaal van gratis Copilot-seats voor iedereen."),
                ]),
            },
        },
        "explorer": {
            "sub": "26 concrete, direct bruikbare use cases voor elk onderdeel van het hoger onderwijs. Filter op rol of op echte GitHub Copilot-featurefamilies en open daarna een kaart voor de exacte stappen.",
            "features": [
                ("inline", "Inline-suggesties", "Codevoorstellen in je IDE, met next edit suggestions in ondersteunde editors."),
                ("chat", "Copilot Chat", "Vragen stellen, verfijnen, uitleggen en bouwen in natuurlijke taal op github.com/copilot, mobiel, IDE of Windows Terminal."),
                ("agent", "Agent-modus", "Copilot werkt autonomer in je IDE, plant en past multi-file wijzigingen toe met goedkeuringspunten."),
                ("cli", "Copilot CLI", "Terminalwerk in natuurlijke taal beschrijven en de flow in de command line houden."),
                ("review", "Copilot code review", "AI-reviewsuggesties en aandachtspunten vóór of tijdens menselijke review."),
                ("cloudagent", "Copilot cloud agent", "Een taak of issue toewijzen, Copilot op een branch laten werken en daarna de pull request reviewen."),
                ("spaces", "Copilot Spaces", "Copilot verankeren met repos, bestanden, vrije tekst, transcripties en afbeeldingen in een deelbare Space."),
                ("mcp", "MCP-servers", "Copilot verbinden met vertrouwde tools en databronnen."),
            ],
            "usecase_rewrites": {
                1: {
                    "title": "Veranker een schemauitleg met Copilot Spaces",
                    "features": ["spaces", "chat"],
                    "situation": "Je hebt slides, een gescand schema en tutor-notities en wilt een toegankelijke digitale uitleg in plaats van nog een afbeelding in een pdf.",
                    "steps": [
                        "Maak een Space aan en voeg de schema-afbeelding, de relevante slidetekst en een heldere legenda toe.",
                        "Vraag Copilot Chat om dat gegronde materiaal om te zetten in een HTML/CSS-pagina met labels, alt-tekst en een kleine begrippenlijst.",
                        "Publiceer de goedgekeurde versie op GitHub Pages zodat studenten er buiten de les naar kunnen terugkeren.",
                    ],
                    "result": "Een duidelijkere, herbruikbare uitleg die in je eigen lesmateriaal verankerd is.",
                    "further": "Gebruik dezelfde Space voor het volgende schema-intensieve onderwerp in plaats van alles opnieuw uit te leggen.",
                },
                7: {
                    "title": "Bouw een portfolio dat in je echte projectbestanden verankerd is",
                    "features": ["spaces", "chat"],
                    "situation": "Je wilt een portfolio zonder elke projectbeschrijving opnieuw uit de losse pols te schrijven.",
                    "steps": [
                        "Maak een Space met README-bestanden, screenshots, stagesamenvatting en belangrijke links.",
                        "Vraag Copilot Chat om een portfolio van één pagina met projectkaarten en korte resultaatgerichte bullets.",
                        "Verfijn de toon en publiceer daarna de gekozen versie op GitHub Pages.",
                    ],
                    "result": "Een portfolio dat sneller gebouwd is omdat het bronmateriaal al gegrond is.",
                    "further": "Houd de Space elk semester bij zodat volgende portfolio-updates een korte bewerkingsronde worden.",
                },
                16: {
                    "title": "Zet strategienotities om in een deelbare one-pager met Copilot Spaces",
                    "features": ["spaces", "chat"],
                    "situation": "Je hebt vergadernotities, KPI-context en een nog ruwe verhaallijn en wilt iets beters dan een muur van bullets.",
                    "steps": [
                        "Maak een Space met de strategienotities, het KPI-overzicht en de kerntermen die intern gebruikt worden.",
                        "Vraag Copilot Chat om een samenvatting van één pagina met prioriteiten, risico’s en volgende acties in gewone taal.",
                        "Bekijk de tekst en publiceer of exporteer daarna de versie die je wilt delen.",
                    ],
                    "result": "Een helderdere beleidspagina die in je echte interne materiaal verankerd is.",
                    "further": "Gebruik dezelfde Space opnieuw voor maand- of kwartaalupdates zodat het vocabulaire consistent blijft.",
                },
                22: {
                    "title": "Bouw een onderzoekspagina die in je figuren verankerd is",
                    "features": ["spaces", "chat"],
                    "situation": "Je wilt een publieke pagina over je bevindingen, maar de tekst moet dicht bij abstract, figuren en congresnotities blijven.",
                    "steps": [
                        "Maak een Space met het abstract, figuurlegendes, postertekst en je samenvatting in gewone taal.",
                        "Vraag Copilot Chat om een resultatenpagina met een korte methodesectie en een heldere samenvatting voor niet-specialisten.",
                        "Bekijk de tekst en publiceer de pagina naast de link naar het formele artikel.",
                    ],
                    "result": "Een gegronde, toegankelijke resultatenpagina die je makkelijk in talks of projectopvolging hergebruikt.",
                    "further": "Voeg een samenwerkingssectie toe en gebruik de Space als bron voor toekomstig disseminatiemateriaal.",
                },
                25: {
                    "title": "Publiceer een campusevenementenpagina vanuit een gegrond eventpack",
                    "features": ["spaces", "chat"],
                    "situation": "Je hebt kalenderexports, affichetekst en toegankelijkheidsnotities en wilt een betere evenementenpagina dan losse posters.",
                    "steps": [
                        "Maak een Space met de titels, data, beschrijvingen en toegankelijkheidsnotities van de evenementen.",
                        "Vraag Copilot Chat om een pagina die evenementen op datum sorteert en de eerstvolgende activiteiten bovenaan zet.",
                        "Publiceer de pagina op GitHub Pages en werk de Space maandelijks bij in plaats van telkens opnieuw te beginnen.",
                    ],
                    "result": "Een lichte evenementenpagina die makkelijker te onderhouden is dan een statisch posterarchief.",
                    "further": "Voeg een blok “contacteer de organisator” toe en hergebruik dezelfde structuur elke nieuwe maand.",
                },
            },
        },
    },
}

EXTRA_EXPLORER_FEATURES = {
    "en": [
        ("app", "GitHub Copilot app", "Run separate Copilot agent sessions in their own worktrees, compare diffs, and keep several tasks moving in parallel."),
        ("instructions", "Custom instructions", "Repository or path-specific guidance that keeps naming, tone, accessibility, and build rules consistent."),
        ("promptfiles", "Prompt files", "Reusable task templates stored in the repository so recurring work starts from a shared prompt instead of a blank chat."),
        ("customagents", "Custom agents", "Repository-defined agents with a specific job, style, or workflow."),
        ("skills", "Agent skills", "Reusable skill bundles that teach agents how your team wants repetitive tasks done."),
        ("memory", "Copilot Memory", "Remember useful project context so recurring work does not restart from zero every session."),
    ],
    "fr": [
        ("app", "Application GitHub Copilot", "Lancer des sessions agentiques séparées dans leurs propres worktrees, comparer les diffs et garder plusieurs tâches en parallèle."),
        ("instructions", "Instructions personnalisées", "Des consignes de dépôt ou de dossier pour garder cohérence de nommage, ton, accessibilité et étapes de build."),
        ("promptfiles", "Prompt files", "Des modèles de tâches réutilisables stockés dans le dépôt afin de démarrer un travail récurrent depuis un prompt partagé plutôt qu’une page blanche."),
        ("customagents", "Custom agents", "Des agents définis dans le dépôt avec un rôle, un style ou un flux de travail précis."),
        ("skills", "Agent skills", "Des briques réutilisables qui apprennent aux agents comment ton équipe veut traiter les tâches répétitives."),
        ("memory", "Copilot Memory", "Mémoriser un contexte de projet utile afin que le travail récurrent ne reparte pas de zéro à chaque session."),
    ],
    "nl": [
        ("app", "GitHub Copilot-app", "Aparte Copilot-agentsessies in hun eigen worktrees draaien, diffs vergelijken en meerdere taken parallel laten lopen."),
        ("instructions", "Custom instructions", "Repository- of padgebonden richtlijnen die naamgeving, toon, toegankelijkheid en buildstappen consistent houden."),
        ("promptfiles", "Prompt files", "Herbruikbare taaktemplates in de repository zodat terugkerend werk start vanuit een gedeelde prompt in plaats van een lege chat."),
        ("customagents", "Custom agents", "Repository-gedefinieerde agents met een specifieke taak, stijl of workflow."),
        ("skills", "Agent skills", "Herbruikbare skillbundels die agents leren hoe je team repetitief werk wil aanpakken."),
        ("memory", "Copilot Memory", "Nuttige projectcontext onthouden zodat terugkerend werk niet elke sessie opnieuw van nul start."),
    ],
}

EXTRA_USECASES = {
    "en": [
        explorer_usecase(
            "teaching",
            "Turn one lab brief into three safe exercise variants",
            ["promptfiles", "instructions", "chat"],
            "You have one practical brief and you want several variants that keep the same learning goals, rubric language, and safety wording.",
            [
                "Create a prompt file in the repository that asks for a variant, an answer key, and a short teacher note.",
                "Add custom instructions for tone, accessibility, and any lab-safety wording that must stay untouched.",
                "Ask Copilot Chat for three versions, then keep the approved set in the same course repository.",
            ],
            "A reusable variation workflow instead of rewriting the same exercise every semester.",
            "Keep the prompt file in the repo so colleagues can generate the next set from the same structure.",
        ),
        explorer_usecase(
            "teaching",
            "Let Copilot cloud agent refresh a course FAQ from issues",
            ["cloudagent", "review", "spaces"],
            "Students keep asking the same weekly questions and you want the FAQ page updated through reviewable pull requests rather than manual copy-paste.",
            [
                "Open an issue such as “Add this week’s recurring questions to the FAQ” and attach the grounded course Space if you already use one.",
                "Assign the issue to Copilot so the cloud agent drafts the page update on its own branch.",
                "Request Copilot code review on the pull request, review the wording yourself, then merge the approved update.",
            ],
            "A course FAQ that improves week by week without turning the teaching team into web maintainers.",
            "Use the same issue pattern after every lecture block so the FAQ becomes a living teaching asset.",
        ),
        explorer_usecase(
            "students",
            "Keep an internship or thesis project moving with Copilot Memory",
            ["memory", "chat"],
            "You return to the same project every week and do not want to restate the context, stack, deadlines, and constraints from scratch every single time.",
            [
                "Store the stable project context in a Memory-enabled Copilot workflow and mirror the most important decisions in the repository README.",
                "Ask Copilot Chat for the next milestone, a progress summary, or a cleanup pass on the current code.",
                "Commit each approved change so the project history stays visible to supervisors and teammates.",
            ],
            "A steadier project rhythm with less time lost re-explaining the same background.",
            "Memory helps with continuity, but the real source of truth should still live in the repository.",
        ),
        explorer_usecase(
            "it",
            "Standardise helpdesk cleanup scripts with Agent skills",
            ["skills", "agent", "cli"],
            "Different technicians solve the same account-cleanup or log-collection ticket in slightly different ways, and the variation creates avoidable risk.",
            [
                "Define an Agent skill with the approved script pattern, logging format, and rollback expectations.",
                "Ask Agent mode or Copilot CLI to adapt that skill to the current ticket instead of starting from a blank shell.",
                "Review the resulting script or diff before running it in the target environment.",
            ],
            "Repeatable internal automations with less copy-paste drift between technicians.",
            "Version the skill in GitHub so one update improves the whole team’s starting point.",
        ),
        explorer_usecase(
            "hr",
            "Keep policy pages consistent with custom instructions",
            ["instructions", "review", "chat"],
            "HR updates policies often, but headings, tone, required caveats, and inclusive wording drift from page to page.",
            [
                "Put the required tone, section order, inclusive wording, and approval notes in .github/copilot-instructions.md.",
                "Ask Copilot Chat to draft the updated page using those repository rules.",
                "Open a pull request and use Copilot code review as a second pair of eyes before publishing internally.",
            ],
            "Faster policy-page drafting with fewer formatting corrections later in the process.",
            "Extend the instructions file each time HR or Legal adds a new must-have section.",
        ),
        explorer_usecase(
            "leadership",
            "Create a custom agent that turns pilot ideas into comparable briefs",
            ["customagents", "app", "review"],
            "Several departments pitch small internal tools at once, and leadership needs a comparable brief for each proposal before deciding what to fund.",
            [
                "Define a custom agent that must always output the same sections: problem, users, low-risk first version, data sensitivity, and next step.",
                "Run that agent in separate GitHub Copilot app sessions, one proposal per worktree.",
                "Compare the resulting briefs and PR summaries side by side instead of comparing informal hallway requests.",
            ],
            "A reviewable pipeline of lightweight prototypes instead of a backlog of vague requests.",
            "Keep the winning briefs in a shared gallery repository so the next team can fork an existing idea instead of starting from zero.",
        ),
        explorer_usecase(
            "finance",
            "Generate monthly budget notes in one shared house style",
            ["promptfiles", "instructions", "chat"],
            "Finance turns the same export into monthly comments, but wording and tables vary from person to person.",
            [
                "Store formatting rules and mandatory headings in custom instructions.",
                "Create a prompt file that asks for a variance summary, top exceptions, and next actions from the pasted export.",
                "Run the prompt each month, then review the draft note in a pull request before it circulates.",
            ],
            "More consistent monthly reporting with visible rules in the repository.",
            "This is especially useful when several people rotate across the same reporting workflow.",
        ),
        explorer_usecase(
            "research",
            "Ask a lab scheduling system for utilisation patterns through MCP",
            ["mcp", "agent", "chat"],
            "A research platform team wants to understand which equipment slots stay underused without manually exporting and reshaping the same files every month.",
            [
                "Connect Copilot to the approved scheduling system through an MCP server or another governed connector.",
                "Ask for utilisation by day, room, or lab in plain language to identify obvious underuse patterns.",
                "Let Agent mode generate the dashboard or notebook that reproduces the answer so the method stays inspectable.",
            ],
            "A faster path from operational question to reproducible utilisation view.",
            "Keep the connection scoped to approved data only and reuse the same prompts each semester.",
        ),
        explorer_usecase(
            "campus",
            "Build a citation-help assistant for the library",
            ["spaces", "chat"],
            "Library staff keep answering the same “How do I cite this?” questions across guides, workshops, and helpdesk messages.",
            [
                "Create a Copilot Space with citation guides, local library policy notes, and worked examples.",
                "Ask Copilot Chat to draft a searchable help page or chatbot copy grounded in that material.",
                "Publish the approved version on GitHub Pages and keep the Space fresh when the guide changes.",
            ],
            "A grounded citation helper that points people back to the library’s own guidance.",
            "Refresh the Space whenever the library updates its style-guide pages or exceptions.",
        ),
        explorer_usecase(
            "campus",
            "Ship a small incident-reporting form for campus facilities",
            ["agent", "review", "chat"],
            "Facilities staff need a lightweight way to collect location, photo, urgency, and follow-up status for minor incidents without waiting for a full platform replacement.",
            [
                "Ask Agent mode to scaffold the form, confirmation screen, and the simplest useful storage pattern for a pilot.",
                "Use Copilot code review to check field labels, validation, and the clarity of the follow-up flow.",
                "Pilot the first version in one building before deciding whether it deserves a bigger system.",
            ],
            "A practical reporting flow that can start small and still stay reviewable.",
            "If the pilot works, move it into a shared repo with a code owner instead of leaving it on one laptop.",
        ),
    ],
    "fr": [
        explorer_usecase(
            "teaching",
            "Transformer un seul brief de labo en trois variantes sûres",
            ["promptfiles", "instructions", "chat"],
            "Tu disposes d’un seul énoncé pratique et tu veux plusieurs variantes qui gardent les mêmes objectifs d’apprentissage, la même logique de barème et le même vocabulaire de sécurité.",
            [
                "Crée dans le dépôt un prompt file qui demande une variante, un corrigé et une courte note pour la personne enseignante.",
                "Ajoute des instructions personnalisées pour le ton, l’accessibilité et les formulations de sécurité qui ne doivent pas bouger.",
                "Demande à Copilot Chat trois versions, puis conserve l’ensemble validé dans le dépôt du cours.",
            ],
            "Un flux réutilisable de variation d’exercices au lieu de tout réécrire chaque quadrimestre.",
            "Garde le prompt file dans le dépôt afin que les collègues puissent générer la série suivante avec la même structure.",
        ),
        explorer_usecase(
            "teaching",
            "Laisser le cloud agent de Copilot rafraîchir la FAQ d’un cours",
            ["cloudagent", "review", "spaces"],
            "La communauté étudiante pose chaque semaine les mêmes questions et tu veux mettre à jour la FAQ via des pull requests relisibles plutôt qu’à coups de copier-coller.",
            [
                "Ouvre une issue du type « Ajouter les questions récurrentes de cette semaine dans la FAQ » et rattache le Space du cours si tu en utilises déjà un.",
                "Assigne l’issue à Copilot afin que le cloud agent prépare la mise à jour sur sa propre branche.",
                "Demande ensuite un Copilot code review sur la PR, relis le texte toi-même et fusionne la version approuvée.",
            ],
            "Une FAQ de cours qui s’améliore semaine après semaine sans transformer l’équipe pédagogique en équipe web.",
            "Réutilise le même modèle d’issue après chaque bloc de cours pour faire de la FAQ un vrai actif pédagogique vivant.",
        ),
        explorer_usecase(
            "students",
            "Garder un mémoire ou un stage en mouvement avec Copilot Memory",
            ["memory", "chat"],
            "Tu reviens chaque semaine sur le même projet et tu ne veux pas réexpliquer à chaque fois le contexte, la stack, les échéances et les contraintes.",
            [
                "Conserve le contexte stable dans un flux Copilot compatible Memory et recopie les décisions importantes dans le README du dépôt.",
                "Demande à Copilot Chat la prochaine étape, un résumé d’avancement ou une passe de nettoyage sur le code courant.",
                "Commite chaque changement validé afin que l’historique reste lisible pour l’encadrement et l’équipe.",
            ],
            "Un rythme de projet plus régulier, avec moins de temps perdu à répéter le même contexte.",
            "Memory aide à la continuité, mais la vraie source de vérité doit rester dans le dépôt.",
        ),
        explorer_usecase(
            "it",
            "Standardiser des scripts helpdesk répétitifs avec des Agent skills",
            ["skills", "agent", "cli"],
            "Des techniciennes et techniciens résolvent le même ticket de nettoyage de comptes ou de collecte de logs de façons légèrement différentes, ce qui crée un risque inutile.",
            [
                "Définis une Agent skill avec le patron de script approuvé, le format de log et les attentes de rollback.",
                "Demande ensuite au mode Agent ou à Copilot CLI d’adapter cette skill au ticket du jour plutôt que de repartir d’un shell vide.",
                "Relis le script ou le diff obtenu avant toute exécution dans l’environnement cible.",
            ],
            "Des automatisations internes plus répétables, avec moins de dérive par copier-coller entre collègues.",
            "Versionne la skill sur GitHub afin qu’une seule mise à jour améliore le point de départ de toute l’équipe.",
        ),
        explorer_usecase(
            "hr",
            "Garder des pages de politiques cohérentes avec des custom instructions",
            ["instructions", "review", "chat"],
            "Les RH mettent souvent à jour des politiques, mais les titres, le ton, les avertissements obligatoires et les formulations inclusives dérivent d’une page à l’autre.",
            [
                "Place dans .github/copilot-instructions.md le ton requis, l’ordre des sections, l’écriture inclusive et les notes d’approbation obligatoires.",
                "Demande à Copilot Chat une version mise à jour de la page en s’appuyant sur ces règles de dépôt.",
                "Ouvre une pull request et utilise Copilot code review comme deuxième regard avant publication interne.",
            ],
            "Une rédaction plus rapide des pages RH, avec moins de corrections de forme en fin de chaîne.",
            "Étends le fichier d’instructions chaque fois que les RH ou le juridique ajoutent une section indispensable.",
        ),
        explorer_usecase(
            "leadership",
            "Créer un custom agent qui transforme des idées pilotes en briefs comparables",
            ["customagents", "app", "review"],
            "Plusieurs services proposent de petits outils internes en même temps, et la direction a besoin d’un brief comparable pour chaque idée avant d’arbitrer.",
            [
                "Définis un custom agent qui doit toujours produire les mêmes rubriques : problème, publics, première version à faible risque, sensibilité des données et prochaine étape.",
                "Lance cet agent dans plusieurs sessions de l’application GitHub Copilot, une proposition par worktree.",
                "Compare ensuite les briefs et les résumés de PR côte à côte au lieu de comparer des demandes informelles de couloir.",
            ],
            "Un pipeline relisible de prototypes légers au lieu d’un backlog de demandes vagues.",
            "Conserve les briefs gagnants dans une galerie partagée afin que le service suivant puisse partir d’une idée existante.",
        ),
        explorer_usecase(
            "finance",
            "Produire les commentaires budgétaires mensuels dans un style partagé",
            ["promptfiles", "instructions", "chat"],
            "L’équipe finances transforme le même export en commentaire mensuel, mais la formulation et les tableaux changent selon la personne qui s’en charge.",
            [
                "Stocke les règles de mise en forme et les intertitres obligatoires dans les instructions personnalisées.",
                "Crée un prompt file qui demande un résumé des écarts, les exceptions majeures et les actions à suivre à partir de l’export collé.",
                "Lance ce prompt chaque mois, puis relis la note dans une pull request avant diffusion.",
            ],
            "Un reporting mensuel plus cohérent, avec des règles visibles dans le dépôt.",
            "C’est particulièrement utile quand plusieurs personnes se relaient sur le même rituel de reporting.",
        ),
        explorer_usecase(
            "research",
            "Interroger un planning d’équipements de recherche via MCP",
            ["mcp", "agent", "chat"],
            "Une plateforme de recherche veut comprendre quels créneaux d’équipement restent sous-utilisés sans réexporter et retraiter les mêmes fichiers chaque mois.",
            [
                "Connecte Copilot au système de planning approuvé via un serveur MCP ou un connecteur gouverné équivalent.",
                "Pose la question en langage naturel par jour, salle ou laboratoire pour repérer les sous-usages évidents.",
                "Laisse ensuite le mode Agent générer le tableau de bord ou le notebook qui reproduit la réponse afin que la méthode reste inspectable.",
            ],
            "Un chemin plus rapide entre question opérationnelle et vue de fréquentation reproductible.",
            "Garde la connexion strictement limitée aux données approuvées et réutilise les mêmes prompts à chaque quadrimestre.",
        ),
        explorer_usecase(
            "campus",
            "Construire un assistant de citation pour la bibliothèque",
            ["spaces", "chat"],
            "L’équipe bibliothèque répond sans cesse aux mêmes questions du type « Comment citer ceci ? » dans les guides, ateliers et messages de support.",
            [
                "Crée un Copilot Space avec les guides de citation, les notes locales de la bibliothèque et des exemples corrigés.",
                "Demande à Copilot Chat une page d’aide consultable ou un texte de chatbot ancré dans ce matériau.",
                "Publie la version approuvée sur GitHub Pages et mets le Space à jour dès que le guide change.",
            ],
            "Un aide-mémoire de citation ancré dans les consignes réelles de la bibliothèque.",
            "Rafraîchis le Space chaque fois que les pages du guide de style ou leurs exceptions évoluent.",
        ),
        explorer_usecase(
            "campus",
            "Lancer un petit formulaire de signalement pour les services techniques",
            ["agent", "review", "chat"],
            "Les équipes techniques ont besoin d’un moyen léger de collecter lieu, photo, urgence et suivi pour les petits incidents sans attendre le remplacement complet d’une plateforme.",
            [
                "Demande au mode Agent de générer le formulaire, l’écran de confirmation et la solution de stockage la plus simple utile pour un pilote.",
                "Utilise Copilot code review pour vérifier l’intitulé des champs, la validation et la clarté du suivi.",
                "Teste la première version dans un seul bâtiment avant de décider si l’outil mérite un système plus large.",
            ],
            "Un flux de signalement pratique qui peut commencer petit tout en restant relisible.",
            "Si le pilote fonctionne, déplace l’outil dans un dépôt partagé avec une personne responsable du code plutôt que sur un seul ordinateur.",
        ),
    ],
    "nl": [
        explorer_usecase(
            "teaching",
            "Maak van één labobrief drie veilige oefenvarianten",
            ["promptfiles", "instructions", "chat"],
            "Je hebt één practicumopdracht en wilt meerdere varianten die dezelfde leerdoelen, rubrictaal en veiligheidsformuleringen behouden.",
            [
                "Maak in de repository een prompt file die een variant, een antwoordmodel en een korte docentennota vraagt.",
                "Voeg custom instructions toe voor toon, toegankelijkheid en veiligheidszinnen die onveranderd moeten blijven.",
                "Vraag Copilot Chat om drie versies en bewaar daarna de goedgekeurde set in dezelfde cursusrepository.",
            ],
            "Een herbruikbare workflow voor oefenvarianten in plaats van elke semester alles opnieuw te schrijven.",
            "Bewaar de prompt file in de repo zodat collega’s de volgende set vanuit dezelfde structuur kunnen genereren.",
        ),
        explorer_usecase(
            "teaching",
            "Laat Copilot cloud agent een cursus-FAQ bijwerken vanuit issues",
            ["cloudagent", "review", "spaces"],
            "Studenten stellen elke week dezelfde vragen en je wilt de FAQ via reviewbare pull requests updaten in plaats van met handmatig kopiëren en plakken.",
            [
                "Open een issue zoals “Voeg de terugkerende vragen van deze week toe aan de FAQ” en koppel de cursus-Space als je die al gebruikt.",
                "Wijs het issue toe aan Copilot zodat de cloud agent de update op een eigen branch voorbereidt.",
                "Vraag daarna Copilot code review op de pull request, lees de tekst zelf na en merge de goedgekeurde versie.",
            ],
            "Een cursus-FAQ die week na week beter wordt zonder dat het docententeam webbeheerders moet worden.",
            "Herhaal hetzelfde issuepatroon na elk lesblok zodat de FAQ een levend lesinstrument wordt.",
        ),
        explorer_usecase(
            "students",
            "Houd een stage- of thesisproject op koers met Copilot Memory",
            ["memory", "chat"],
            "Je keert elke week naar hetzelfde project terug en wilt niet telkens opnieuw de context, stack, deadlines en randvoorwaarden uitleggen.",
            [
                "Bewaar de stabiele projectcontext in een Memory-geschikte Copilot-flow en zet de belangrijkste beslissingen ook in de README van de repository.",
                "Vraag Copilot Chat naar de volgende mijlpaal, een voortgangssamenvatting of een opschoonbeurt op de huidige code.",
                "Commit elke goedgekeurde wijziging zodat de historiek zichtbaar blijft voor begeleiders en teamgenoten.",
            ],
            "Een gelijkmatiger projectritme met minder tijdverlies aan dezelfde achtergrond opnieuw uitleggen.",
            "Memory helpt voor continuïteit, maar de echte bron van waarheid moet in de repository blijven staan.",
        ),
        explorer_usecase(
            "it",
            "Standaardiseer repetitieve helpdeskscripts met Agent skills",
            ["skills", "agent", "cli"],
            "Verschillende technici lossen hetzelfde account-opruim- of logverzamelingsprobleem elk net iets anders op, en die variatie creëert onnodig risico.",
            [
                "Definieer een Agent skill met het goedgekeurde scriptpatroon, logformaat en rollbackverwachtingen.",
                "Vraag daarna aan Agent-modus of Copilot CLI om die skill op het ticket van vandaag toe te passen in plaats van van een lege shell te vertrekken.",
                "Bekijk het script of de diff eerst na vóór je iets uitvoert in de doelomgeving.",
            ],
            "Herhaalbare interne automatiseringen met minder copy-paste-afwijking tussen technici.",
            "Versioneer de skill op GitHub zodat één update het vertrekpunt van het hele team verbetert.",
        ),
        explorer_usecase(
            "hr",
            "Houd beleidspagina’s consistent met custom instructions",
            ["instructions", "review", "chat"],
            "HR actualiseert vaak beleidspagina’s, maar koppen, toon, verplichte disclaimers en inclusieve formulering gaan al snel uiteenlopen.",
            [
                "Zet de vereiste toon, sectievolgorde, inclusieve formulering en goedkeuringsnotities in .github/copilot-instructions.md.",
                "Vraag Copilot Chat om de bijgewerkte pagina te schrijven op basis van die repositoryregels.",
                "Open een pull request en gebruik Copilot code review als extra check vóór interne publicatie.",
            ],
            "Snellere beleidsredactie met minder vormcorrecties op het einde van het proces.",
            "Breid het instructiebestand uit telkens wanneer HR of Legal een nieuwe verplichte sectie toevoegt.",
        ),
        explorer_usecase(
            "leadership",
            "Maak een custom agent die pilootideeën omzet in vergelijkbare briefs",
            ["customagents", "app", "review"],
            "Meerdere diensten pitchen tegelijk kleine interne tools en de directie wil voor elk voorstel eerst een vergelijkbare briefing zien.",
            [
                "Definieer een custom agent die altijd dezelfde rubrieken moet opleveren: probleem, doelgebruikers, eerste laag-risicoversie, datasensitiviteit en volgende stap.",
                "Draai die agent in aparte sessies van de GitHub Copilot-app, één voorstel per worktree.",
                "Vergelijk daarna de briefs en PR-samenvattingen naast elkaar in plaats van informele ganggesprekken te moeten vergelijken.",
            ],
            "Een reviewbare pijplijn van lichte prototypes in plaats van een backlog vol vage verzoeken.",
            "Bewaar de winnende briefs in een gedeelde galerijrepository zodat het volgende team op een bestaand idee kan voortbouwen.",
        ),
        explorer_usecase(
            "finance",
            "Genereer maandelijkse budgetnota’s in één gedeelde huisstijl",
            ["promptfiles", "instructions", "chat"],
            "Financiën maakt elke maand van dezelfde export een commentaarnota, maar formulering en tabellen verschillen per persoon.",
            [
                "Bewaar opmaakregels en verplichte tussentitels in de custom instructions.",
                "Maak een prompt file die uit de geplakte export een variantiesamenvatting, grootste uitzonderingen en volgende acties vraagt.",
                "Voer die prompt elke maand uit en bekijk de conceptnota daarna in een pull request voordat ze circuleert.",
            ],
            "Consistenter maandrapporteren met zichtbare regels in de repository.",
            "Dat is vooral handig wanneer verschillende collega’s hetzelfde rapporteringsritueel afwisselend opnemen.",
        ),
        explorer_usecase(
            "research",
            "Vraag benuttingspatronen op uit een labo-planningssysteem via MCP",
            ["mcp", "agent", "chat"],
            "Een onderzoeksplatformteam wil weten welke equipment-slots onderbenut blijven zonder elke maand opnieuw dezelfde exports te trekken en te herwerken.",
            [
                "Verbind Copilot met het goedgekeurde planningssysteem via een MCP-server of een andere governed connector.",
                "Vraag in gewone taal om benutting per dag, ruimte of labo zodat duidelijke onderbenuttingspatronen zichtbaar worden.",
                "Laat Agent-modus vervolgens het dashboard of notebook genereren dat het antwoord reproduceert zodat de methode inspecteerbaar blijft.",
            ],
            "Een snellere weg van operationele vraag naar reproduceerbaar benuttingsoverzicht.",
            "Beperk de koppeling strikt tot goedgekeurde data en hergebruik dezelfde prompts elk semester.",
        ),
        explorer_usecase(
            "campus",
            "Bouw een brongegronde citeerhulp voor de bibliotheek",
            ["spaces", "chat"],
            "Bibliotheekmedewerkers beantwoorden voortdurend dezelfde “Hoe citeer ik dit?”-vragen in handleidingen, workshops en supportmails.",
            [
                "Maak een Copilot Space met citeergidsen, lokale bibliotheeknotities en uitgewerkte voorbeelden.",
                "Vraag Copilot Chat om een doorzoekbare hulppagina of chatbottekst op basis van dat materiaal.",
                "Publiceer de goedgekeurde versie op GitHub Pages en werk de Space bij zodra de gids wijzigt.",
            ],
            "Een citeerhulp die gegrond is in de eigen richtlijnen van de bibliotheek.",
            "Ververs de Space telkens wanneer de stijlgidspagina’s of uitzonderingen veranderen.",
        ),
        explorer_usecase(
            "campus",
            "Lanceer een klein incidentmeldingsformulier voor facilitaire diensten",
            ["agent", "review", "chat"],
            "Facilitaire teams hebben een lichte manier nodig om locatie, foto, urgentie en opvolgstatus voor kleine incidenten te verzamelen zonder op een volledige platformvervanging te wachten.",
            [
                "Vraag Agent-modus om het formulier, het bevestigingsscherm en de eenvoudigste zinvolle opslag voor een pilot op te zetten.",
                "Gebruik Copilot code review om veldlabels, validatie en de duidelijkheid van de opvolgflow te controleren.",
                "Test de eerste versie in één gebouw voordat je beslist of de tool een groter systeem verdient.",
            ],
            "Een praktische meldflow die klein kan starten en toch reviewbaar blijft.",
            "Als de pilot werkt, verhuis de tool dan naar een gedeelde repo met een code owner in plaats van naar één laptop.",
        ),
    ],
}

FIRST_COMMIT_CONTENT = {
    "en": {
        "title": "Your first commit",
        "sub": "The beginner-proof path from “I do not code” to “my code is on GitHub” — with GitHub Copilot helping you, not raw git syntax.",
        "hero_note": "No credit card. No local git commands required for the flagship path. Start in the browser, then choose the route that matches your comfort level.",
        "account_title": "1. Create your GitHub account",
        "account_sub": "Start at github.com/signup. A verified email is required before you can create a repository, and enabling 2FA right after sign-up is the smart next step.",
        "account_cards": [
            {"icon": "⚡", "title": "30-second start", "desc": "Go to github.com/signup and create your account. Google and Apple sign-in are supported."},
            {"icon": "✉️", "title": "Verify your email", "desc": "GitHub asks for a verified email before you can create your first repository."},
            {"icon": "🔐", "title": "Turn on 2FA next", "desc": "Do it right after sign-up so your new account starts secure from day one."},
        ],
        "repo_title": "2. Create your first repository in the browser",
        "repo_sub": "This is the zero-install path and the friendliest way to understand what a repository feels like before you touch any tooling.",
        "repo_steps": [
            {"num": "01", "title": "Click the + icon", "desc": "In the top-right corner of GitHub, click the + menu and choose New repository."},
            {"num": "02", "title": "Give it a short name", "desc": "Pick something simple and memorable such as hello-world, quiz-demo, or campus-faq."},
            {"num": "03", "title": "Choose visibility", "desc": "Public is fine for demos; private is fine for internal experiments."},
            {"num": "04", "title": "Turn on Add README", "desc": "That creates the repository with one file already inside, so you can make a first change immediately."},
            {"num": "05", "title": "Create repository", "desc": "Click Create repository and you are done: GitHub just created your first project space."},
        ],
        "repo_mockup_title": "Screenshot-style checklist",
        "repo_mockup_lines": [
            "+  New repository",
            "Repository name: hello-world",
            "Description: optional",
            "Visibility: Public or Private",
            "Add README: On",
            "Create repository",
        ],
        "warmup_title": "Optional 60-second warm-up",
        "warmup_desc": "Open README.md, click the pencil icon, add one sentence, preview, then commit. That is already a real first change on GitHub before you ask Copilot to do more.",
        "paths_title": "3. Choose how you want Copilot to help you push code",
        "paths_sub": "There is no single “correct” beginner path. Pick the one that matches your confidence today.",
        "paths": [
            {
                "icon": "🌐",
                "label": "Best for total beginners",
                "title": "I am starting in the browser",
                "audience": "Teaching staff, HR, finance, admin, support teams",
                "summary": "Zero install. Copilot can write the code, open the pull request, update the branch, and let you merge everything without local git commands.",
                "steps": [
                    "Open or create a small issue in the repository, such as “Add a CONTRIBUTING.md file” or “Build a simple quiz page”.",
                    "In the right sidebar, open Assignees, choose Copilot, add an optional prompt if useful, then click Assign.",
                    "Optional: open the Agents tab and start a second natural-language task to show two agent sessions running in parallel.",
                    "When the pull request is ready, request Copilot as a reviewer so Copilot code review comments arrive on the PR.",
                    "If you want changes, comment @copilot on the pull request. When you are happy, merge it — and that merge is the push.",
                ],
                "note": "Copilot cloud agent must be enabled on the repository.",
                "note_page": "plans",
                "note_cta": "See the plans page",
                "success": "And there it is: your code is on GitHub, entirely through the browser.",
            },
            {
                "icon": "⌨️",
                "label": "Best for technical beginners",
                "title": "I am comfortable with a terminal",
                "audience": "IT staff, technical researchers, advanced students",
                "summary": "Copilot CLI is a strong level-two route when you like plain-language automation but still want the terminal nearby.",
                "steps": [
                    "Install Copilot CLI, move into your project folder, and run copilot.",
                    "Type /login the first time and follow the prompts to authenticate with your GitHub account.",
                    "Confirm that you trust the current directory’s files for AI use when asked.",
                    "Then use plain language, for example: “Create a simple HTML quiz page about photosynthesis with 5 questions, then commit and push it to a new branch and open a pull request.”",
                    "Review the plan or execution, keep the useful edits, and let Copilot help you finish the branch and PR flow.",
                ],
                "commands": [
                    "npm install -g @github/copilot",
                    "winget install GitHub.Copilot",
                    "brew install --cask copilot-cli",
                    "curl -fsSL https://gh.io/copilot-install | bash",
                ],
                "note": "Interactive mode is the default. Shift+Tab toggles Plan mode before code is written, and copilot -p \"prompt\" is the non-interactive route.",
                "success": "And there it is: your code is on GitHub, with Copilot guiding the terminal work instead of raw git memorisation.",
            },
            {
                "icon": "🖱️",
                "label": "Best for visual review",
                "title": "I want a graphical interface",
                "audience": "People who want buttons, diffs, and a visible review step",
                "summary": "GitHub Desktop is the bridge option: build with Copilot where you like, then review, commit, and push visually.",
                "steps": [
                    "Download GitHub Desktop from desktop.github.com and sign in with your GitHub account.",
                    "Clone your new repository or open the local project folder you are editing with Copilot elsewhere.",
                    "Make your content or code changes with Copilot in the browser or your editor of choice.",
                    "Return to GitHub Desktop, review the diff, let Copilot suggest the commit message or description, then click Commit.",
                    "Click Push origin and, if needed, open the pull request from GitHub Desktop or github.com.",
                ],
                "note": "This path is especially good when you want a clear “look at the diff before it leaves my machine” moment.",
                "success": "And there it is: your code is on GitHub, without living in a terminal.",
            },
        ],
        "after_title": "4. What next?",
        "after_sub": "Once the first repository exists, the rest gets much easier because every next step has a home.",
        "after_cards": [
            {"icon": "🎯", "title": "See 8 real scenarios", "desc": "Jump from first commit to believable higher-education examples you can demo internally.", "page": "scenarios", "cta": "Open the scenarios"},
            {"icon": "🧭", "title": "Open the learning tracks", "desc": "Use the Learning tracks menu to choose Basics, Advanced, or Expert and keep building step by step.", "page": "basics", "cta": "Start the guided track"},
            {"icon": "🚀", "title": "Publish with GitHub Pages", "desc": "When your first page exists, reuse the publishing lesson and put it online cleanly.", "page": "basics", "anchor": "lesson-4", "cta": "See the publishing lesson"},
            {"icon": "🛠️", "title": "Borrow a ready-made prompt", "desc": "Open the toolkit and copy a prompt that matches your role instead of inventing your next task from scratch.", "page": "toolkit", "cta": "Open the toolkit"},
        ],
    },
    "fr": {
        "title": "Ton premier commit",
        "sub": "Le chemin le plus clair possible entre « je ne code pas » et « mon code est sur GitHub » — avec GitHub Copilot comme guide, pas avec du git brut à mémoriser.",
        "hero_note": "Pas de carte bancaire. Pas de commandes git locales pour le parcours phare. Commence dans le navigateur, puis choisis la route qui correspond à ton niveau d’aisance.",
        "account_title": "1. Créer ton compte GitHub",
        "account_sub": "Commence sur github.com/signup. Une adresse e-mail vérifiée est nécessaire avant de pouvoir créer un dépôt, et activer la 2FA juste après l’inscription est le bon réflexe.",
        "account_cards": [
            {"icon": "⚡", "title": "Départ en 30 secondes", "desc": "Va sur github.com/signup et crée ton compte. La connexion via Google ou Apple est prise en charge."},
            {"icon": "✉️", "title": "Vérifie ton e-mail", "desc": "GitHub demande une adresse e-mail vérifiée avant la création du premier dépôt."},
            {"icon": "🔐", "title": "Active la 2FA ensuite", "desc": "Fais-le juste après l’inscription afin de démarrer avec un compte protégé dès le premier jour."},
        ],
        "repo_title": "2. Créer ton premier dépôt dans le navigateur",
        "repo_sub": "C’est la route sans installation et la manière la plus douce de comprendre ce qu’est un dépôt avant de toucher au moindre outillage.",
        "repo_steps": [
            {"num": "01", "title": "Clique sur l’icône +", "desc": "En haut à droite de GitHub, ouvre le menu + puis choisis New repository."},
            {"num": "02", "title": "Donne-lui un nom simple", "desc": "Choisis un nom court et mémorable comme hello-world, quiz-demo ou campus-faq."},
            {"num": "03", "title": "Choisis la visibilité", "desc": "Public va bien pour une démo ; privé va bien pour un essai interne."},
            {"num": "04", "title": "Active Add README", "desc": "Le dépôt est ainsi créé avec un premier fichier, ce qui permet une toute première modification immédiate."},
            {"num": "05", "title": "Crée le dépôt", "desc": "Clique sur Create repository et c’est fait : GitHub vient de créer ton premier espace de projet."},
        ],
        "repo_mockup_title": "Checklist façon capture d’écran",
        "repo_mockup_lines": [
            "+  New repository",
            "Repository name: hello-world",
            "Description: optionnelle",
            "Visibility: Public ou Private",
            "Add README: On",
            "Create repository",
        ],
        "warmup_title": "Échauffement facultatif en 60 secondes",
        "warmup_desc": "Ouvre README.md, clique sur l’icône crayon, ajoute une phrase, prévisualise, puis committe. C’est déjà une vraie première modification sur GitHub avant de demander davantage à Copilot.",
        "paths_title": "3. Choisir comment Copilot va t’aider à pousser du code",
        "paths_sub": "Il n’existe pas une seule route « correcte » pour débuter. Prends celle qui correspond à ton aisance aujourd’hui.",
        "paths": [
            {
                "icon": "🌐",
                "label": "Idéal pour les personnes totalement débutantes",
                "title": "Je débute, tout dans le navigateur",
                "audience": "Corps enseignant, RH, finances, administration, services support",
                "summary": "Zéro installation. Copilot peut écrire le code, ouvrir la pull request, mettre à jour la branche et te laisser fusionner le tout sans commandes git locales.",
                "steps": [
                    "Ouvre ou crée une petite issue dans le dépôt, par exemple « Add a CONTRIBUTING.md file » ou « Build a simple quiz page ».",
                    "Dans la barre latérale droite, ouvre Assignees, choisis Copilot, ajoute si besoin un prompt facultatif, puis clique sur Assign.",
                    "Facultatif : ouvre l’onglet Agents et lance une deuxième tâche en langage naturel pour montrer deux sessions agentiques en parallèle.",
                    "Quand la pull request est prête, demande Copilot comme reviewer afin de recevoir un Copilot code review directement sur la PR.",
                    "Si tu veux des changements, commente @copilot dans la pull request. Quand le résultat te convient, fusionne-la : cette fusion, c’est le push.",
                ],
                "note": "Le cloud agent de Copilot doit être activé sur le dépôt.",
                "note_page": "plans",
                "note_cta": "Voir la page Plans",
                "success": "Et voilà : ton code est poussé sur GitHub, entièrement depuis le navigateur.",
            },
            {
                "icon": "⌨️",
                "label": "Idéal pour les débutantes et débutants techniques",
                "title": "Je suis à l’aise avec un terminal",
                "audience": "Équipes IT, recherche technique, étudiantes et étudiants avancés",
                "summary": "Copilot CLI est une excellente route niveau 2 si tu aimes l’automatisation en langage naturel tout en gardant le terminal à portée de main.",
                "steps": [
                    "Installe Copilot CLI, place-toi dans le dossier du projet, puis lance copilot.",
                    "Tape /login la première fois et suis les prompts pour authentifier ton compte GitHub.",
                    "Confirme que tu fais confiance aux fichiers du dossier courant quand la demande apparaît.",
                    "Ensuite, écris simplement ce que tu veux, par exemple : « Create a simple HTML quiz page about photosynthesis with 5 questions, then commit and push it to a new branch and open a pull request. »",
                    "Relis le plan ou l’exécution, garde les bons changements, puis laisse Copilot t’aider à terminer la branche et la PR.",
                ],
                "commands": [
                    "npm install -g @github/copilot",
                    "winget install GitHub.Copilot",
                    "brew install --cask copilot-cli",
                    "curl -fsSL https://gh.io/copilot-install | bash",
                ],
                "note": "Le mode interactif est le comportement par défaut. Shift+Tab active le mode Plan avant écriture de code, et copilot -p \"prompt\" sert au mode non interactif.",
                "success": "Et voilà : ton code est poussé sur GitHub, avec Copilot comme guide du terminal plutôt qu’avec du git brut à réciter.",
            },
            {
                "icon": "🖱️",
                "label": "Idéal pour relire visuellement",
                "title": "Je veux une interface visuelle",
                "audience": "Personnes qui veulent des boutons, des diffs et une étape de relecture visible",
                "summary": "GitHub Desktop joue le rôle de passerelle : tu construis avec Copilot là où tu veux, puis tu relis, commits et pushes visuellement.",
                "steps": [
                    "Télécharge GitHub Desktop depuis desktop.github.com et connecte-toi avec ton compte GitHub.",
                    "Clone ton nouveau dépôt ou ouvre le dossier local du projet que tu modifies avec Copilot ailleurs.",
                    "Fais tes changements de contenu ou de code avec Copilot dans le navigateur ou dans ton éditeur préféré.",
                    "Reviens dans GitHub Desktop, relis le diff, laisse Copilot proposer le message ou la description de commit, puis clique sur Commit.",
                    "Clique sur Push origin et, si nécessaire, ouvre la pull request depuis GitHub Desktop ou github.com.",
                ],
                "note": "Cette route est particulièrement utile si tu veux un moment très clair de type « je regarde le diff avant qu’il quitte ma machine ».",
                "success": "Et voilà : ton code est poussé sur GitHub, sans vivre dans un terminal.",
            },
        ],
        "after_title": "4. Et après ?",
        "after_sub": "Une fois le premier dépôt créé, tout devient plus simple parce que chaque étape suivante a déjà une maison.",
        "after_cards": [
            {"icon": "🎯", "title": "Voir 8 scénarios réels", "desc": "Passe du premier commit à des exemples crédibles pour l’enseignement supérieur, prêts à être montrés en interne.", "page": "scenarios", "cta": "Ouvrir les scénarios"},
            {"icon": "🧭", "title": "Ouvrir les parcours", "desc": "Utilise le menu Parcours pour choisir Basics, Advanced ou Expert et continuer pas à pas.", "page": "basics", "cta": "Démarrer le parcours guidé"},
            {"icon": "🚀", "title": "Publier avec GitHub Pages", "desc": "Quand ta première page existe, réutilise la leçon de publication et mets-la proprement en ligne.", "page": "basics", "anchor": "lesson-4", "cta": "Voir la leçon de publication"},
            {"icon": "🛠️", "title": "Piquer un prompt prêt à l’emploi", "desc": "Ouvre la boîte à outils et copie un prompt adapté à ton métier au lieu d’inventer la suite depuis zéro.", "page": "toolkit", "cta": "Ouvrir la boîte à outils"},
        ],
    },
    "nl": {
        "title": "Jouw eerste commit",
        "sub": "Het meest beginner-proof pad van “ik code niet” naar “mijn code staat op GitHub” — met GitHub Copilot als gids, niet met rauwe git-syntax uit het hoofd.",
        "hero_note": "Geen kredietkaart. Geen lokale git-commando’s voor het vlaggenschippad. Start in de browser en kies daarna de route die bij je comfortniveau past.",
        "account_title": "1. Maak je GitHub-account aan",
        "account_sub": "Begin op github.com/signup. Een geverifieerd e-mailadres is nodig vóór je een repository kunt maken, en 2FA meteen daarna inschakelen is de slimme volgende stap.",
        "account_cards": [
            {"icon": "⚡", "title": "Start in 30 seconden", "desc": "Ga naar github.com/signup en maak je account aan. Aanmelden met Google of Apple wordt ondersteund."},
            {"icon": "✉️", "title": "Verifieer je e-mail", "desc": "GitHub vraagt een geverifieerd e-mailadres vóór je je eerste repository kunt aanmaken."},
            {"icon": "🔐", "title": "Schakel daarna 2FA in", "desc": "Doe dat meteen na je registratie zodat je nieuwe account vanaf dag één goed beveiligd is."},
        ],
        "repo_title": "2. Maak je eerste repository aan in de browser",
        "repo_sub": "Dit is het pad zonder installatie en de vriendelijkste manier om te voelen wat een repository is voordat je tools hoeft aan te raken.",
        "repo_steps": [
            {"num": "01", "title": "Klik op het + icoon", "desc": "Open rechtsboven op GitHub het + menu en kies New repository."},
            {"num": "02", "title": "Geef hem een korte naam", "desc": "Kies iets eenvoudigs en onthoudbaars zoals hello-world, quiz-demo of campus-faq."},
            {"num": "03", "title": "Kies de zichtbaarheid", "desc": "Public is prima voor een demo; private is prima voor een intern experiment."},
            {"num": "04", "title": "Zet Add README aan", "desc": "Zo wordt de repository meteen met één bestand aangemaakt, zodat je onmiddellijk een eerste wijziging kunt doen."},
            {"num": "05", "title": "Maak de repository aan", "desc": "Klik op Create repository en klaar: GitHub heeft net je eerste projectruimte gemaakt."},
        ],
        "repo_mockup_title": "Checklist in screenshotstijl",
        "repo_mockup_lines": [
            "+  New repository",
            "Repository name: hello-world",
            "Description: optioneel",
            "Visibility: Public of Private",
            "Add README: On",
            "Create repository",
        ],
        "warmup_title": "Optionele opwarming van 60 seconden",
        "warmup_desc": "Open README.md, klik op het potloodicoon, voeg één zin toe, bekijk de preview en commit daarna. Dat is nu al een echte eerste wijziging op GitHub voordat je Copilot meer laat doen.",
        "paths_title": "3. Kies hoe Copilot je helpt om code naar GitHub te pushen",
        "paths_sub": "Er is niet één “juist” beginpad. Neem de route die vandaag het best past bij jouw vertrouwen.",
        "paths": [
            {
                "icon": "🌐",
                "label": "Best voor totale beginners",
                "title": "Ik begin volledig in de browser",
                "audience": "Docenten, HR, financiën, administratie, supportteams",
                "summary": "Nul installatie. Copilot kan de code schrijven, de pull request openen, de branch bijwerken en jou laten mergen zonder lokale git-commando’s.",
                "steps": [
                    "Open of maak een kleine issue in de repository, bijvoorbeeld “Add a CONTRIBUTING.md file” of “Build a simple quiz page”.",
                    "Open in de rechterzijbalk Assignees, kies Copilot, voeg eventueel een extra prompt toe en klik dan op Assign.",
                    "Optioneel: open het tabblad Agents en start een tweede taak in natuurlijke taal om twee agentsessies parallel te tonen.",
                    "Wanneer de pull request klaar is, vraag Copilot als reviewer zodat Copilot code review-commentaar op de PR verschijnt.",
                    "Wil je nog wijzigingen, reageer dan met @copilot op de pull request. Ben je tevreden, merge dan de PR — die merge is de push.",
                ],
                "note": "Copilot cloud agent moet op de repository ingeschakeld zijn.",
                "note_page": "plans",
                "note_cta": "Bekijk de plannenpagina",
                "success": "En klaar: je code staat op GitHub, volledig via de browser.",
            },
            {
                "icon": "⌨️",
                "label": "Best voor technische beginners",
                "title": "Ik voel me goed in een terminal",
                "audience": "IT-teams, technische onderzoekers, gevorderde studenten",
                "summary": "Copilot CLI is een sterke route van niveau 2 wanneer je van natuurlijke taal houdt maar de terminal toch dichtbij wilt houden.",
                "steps": [
                    "Installeer Copilot CLI, ga naar je projectmap en start copilot.",
                    "Typ de eerste keer /login en volg de prompts om je GitHub-account te authenticeren.",
                    "Bevestig dat je de bestanden in de huidige map vertrouwt voor AI-gebruik wanneer daarom gevraagd wordt.",
                    "Schrijf daarna gewoon wat je wilt, bijvoorbeeld: “Create a simple HTML quiz page about photosynthesis with 5 questions, then commit and push it to a new branch and open a pull request.”",
                    "Bekijk het plan of de uitvoering, behoud de nuttige wijzigingen en laat Copilot je helpen om de branch- en PR-flow af te ronden.",
                ],
                "commands": [
                    "npm install -g @github/copilot",
                    "winget install GitHub.Copilot",
                    "brew install --cask copilot-cli",
                    "curl -fsSL https://gh.io/copilot-install | bash",
                ],
                "note": "Interactieve modus is de standaard. Shift+Tab schakelt Plan-modus in vóór er code geschreven wordt, en copilot -p \"prompt\" is de niet-interactieve route.",
                "success": "En klaar: je code staat op GitHub, met Copilot als gids voor het terminalwerk in plaats van rauwe git-kennis uit het hoofd.",
            },
            {
                "icon": "🖱️",
                "label": "Best voor visuele review",
                "title": "Ik wil een grafische interface",
                "audience": "Mensen die knoppen, diffs en een zichtbare reviewstap willen",
                "summary": "GitHub Desktop is de brugoptie: je bouwt met Copilot waar je wilt en reviewt, commit en pusht daarna visueel.",
                "steps": [
                    "Download GitHub Desktop van desktop.github.com en meld je aan met je GitHub-account.",
                    "Clone je nieuwe repository of open de lokale projectmap die je elders met Copilot bewerkt.",
                    "Maak je inhouds- of codewijzigingen met Copilot in de browser of in je favoriete editor.",
                    "Ga terug naar GitHub Desktop, bekijk de diff, laat Copilot een commitboodschap of beschrijving voorstellen en klik dan op Commit.",
                    "Klik op Push origin en open indien nodig de pull request vanuit GitHub Desktop of github.com.",
                ],
                "note": "Dit pad is vooral fijn als je een duidelijk “ik bekijk de diff voordat hij mijn machine verlaat”-moment wilt.",
                "success": "En klaar: je code staat op GitHub, zonder dat je in een terminal hoeft te wonen.",
            },
        ],
        "after_title": "4. En daarna?",
        "after_sub": "Zodra de eerste repository bestaat, wordt alles eenvoudiger omdat elke volgende stap al een thuisbasis heeft.",
        "after_cards": [
            {"icon": "🎯", "title": "Bekijk 8 echte scenario’s", "desc": "Ga van een eerste commit naar geloofwaardige voorbeelden voor het hoger onderwijs die je intern kunt tonen.", "page": "scenarios", "cta": "Open de scenario’s"},
            {"icon": "🧭", "title": "Open de leertrajecten", "desc": "Gebruik het menu Leertrajecten om Basics, Advanced of Expert te kiezen en stap voor stap verder te bouwen.", "page": "basics", "cta": "Start het begeleide traject"},
            {"icon": "🚀", "title": "Publiceer met GitHub Pages", "desc": "Zodra je eerste pagina bestaat, hergebruik je de publicatieles en zet je ze netjes online.", "page": "basics", "anchor": "lesson-4", "cta": "Bekijk de publicatieles"},
            {"icon": "🛠️", "title": "Neem een kant-en-klare prompt", "desc": "Open de toolkit en kopieer een prompt die bij je rol past in plaats van je volgende taak van nul te verzinnen.", "page": "toolkit", "cta": "Open de toolkit"},
        ],
    },
}

BUILD_VS_BUY_CONTENT = {
    "en": {
        "title": "Vibe coding vs buying an off-the-shelf tool",
        "sub": "The honest comparison is not “Can Copilot replace every vendor?” It cannot. The real question is which small internal tools should stop living as shadow IT, scattered SaaS subscriptions, or permanent backlog tickets.",
        "hero_note": "Use this page for the long tail of low-stakes internal tools: event forms, mini dashboards, room pages, internal assistants, and other things that are too specific to deserve a six-month project but too important to stay hidden in spreadsheets.",
        "changes_title": "What changes when AI-assisted building becomes normal",
        "changes_sub": "Copilot does not remove engineering judgement, procurement, or compliance. It changes the speed, ownership, and economics of the first working version.",
        "change_cards": [
            {"icon": "⏱️", "title": "Time to first working version", "desc": "A natural-language prototype can appear in minutes or hours. A new SaaS purchase can mean discovery, procurement, security review, and rollout before anyone tests the first idea."},
            {"icon": "🏠", "title": "Ownership stays local", "desc": "The institution can keep code, history, and governance in its own GitHub organisation instead of hiding logic and data inside a vendor tool."},
            {"icon": "🧩", "title": "Change requests become prompts", "desc": "When the workflow is yours, “add one field”, “rename that status”, or “change the approval flow” can become the next Copilot task instead of next year’s roadmap request."},
            {"icon": "💳", "title": "The cost shape changes", "desc": "Paid Copilot plans combine unlimited code completions with pooled AI credits, while the long tail of small SaaS tools often renews as separate annual subscriptions whether usage is high or low."},
        ],
        "comparison_title": "The same problem, two paths",
        "comparison_sub": "These are deliberately modest internal tools — not your student record system, payroll suite, or ERP.",
        "comparison_columns": ["Need", "Buy a specialised tool", "Vibe-code a small internal version", "Honest note"],
        "comparison_rows": [
            {
                "need": "Room or equipment booking mini-app",
                "buy": "Evaluate a dedicated booking product, request budget, review data processing, and accept the vendor’s workflow and licensing model.",
                "build": "Start with one building, one lab, or one service point. Ask Copilot for a form, availability view, and admin list, then iterate the fields in plain language.",
                "note": "Great candidate for vibe coding when the scope is local. If it becomes the institutional source of truth for all scheduling, buying or integrating something bigger may still be smarter.",
            },
            {
                "need": "Internal FAQ or knowledge assistant",
                "buy": "Purchase another knowledge tool or chatbot product, then spend time importing documents and aligning permissions.",
                "build": "Use Copilot Spaces plus GitHub Pages or an internal app shell to publish a grounded assistant using the institution’s own documents first.",
                "note": "Especially useful when one department needs answers from its own files. Less attractive if you need vendor-managed omnichannel support and formal SLAs from day one.",
            },
            {
                "need": "Event sign-up page",
                "buy": "Adopt a form or event platform with its own templates, exports, and recurring subscription.",
                "build": "Ask Copilot to scaffold the page, accessibility copy, confirmation flow, and export format you actually need for your event team.",
                "note": "Excellent for low-risk pilots and one-off or seasonal events. Less compelling if you need payment, contracts, or a complex CRM integration immediately.",
            },
            {
                "need": "Budget-variance dashboard",
                "buy": "License another dashboarding or reporting niche tool and adapt finance to its data model.",
                "build": "Turn the monthly export into a static dashboard or small internal app, with calculations visible in code and Git history.",
                "note": "Strong when the source export is already known and the audience is internal. Not the right move when the dashboard must become a regulated, mission-critical reporting platform.",
            },
        ],
        "calculator": {
            "title": "Illustrative calculator: what does the status quo already cost?",
            "sub": "Put in your own numbers. This is not a guaranteed savings claim — just a way to compare the long tail of small tool subscriptions against a Copilot-enabled build capacity.",
            "inputs_title": "Your inputs",
            "tools_label": "How many small internal tool subscriptions do you currently pay for?",
            "average_label": "Average annual cost per tool (USD)",
            "builders_label": "How many people need the ability to build or maintain these small tools?",
            "plan_label": "Which Copilot plan are you comparing against?",
            "business_label": "Business — $19 / seat / month · 1,900 AI credits / month",
            "enterprise_label": "Enterprise — $39 / seat / month · 3,900 AI credits / month",
            "results_title": "What the illustration shows",
            "spend_label": "Annual spend on small tools",
            "copilot_label": "Annual Copilot seat budget",
            "credits_label": "Included AI credits per month",
            "gap_label": "Illustrative annual difference",
            "gap_positive": "More annual spend currently sits in small tools than in the Copilot seat budget shown here.",
            "gap_negative": "The Copilot seat budget shown here is higher than the current small-tool subscription spend you entered.",
            "footnote": "Code completions and next edit suggestions stay unlimited on paid plans. Chat, CLI, Spaces, cloud agent, and similar model-heavy features use the pooled AI credits.",
            "plan_note": "Use the Plans page for the full pricing reality, eligibility detail, and the promotional credit allocations in 2026.",
        },
        "ladder_title": "Vibe Coding Maturity Ladder",
        "ladder_sub": "A credible path from “tiny useful thing” to “institutional capability” helps teams take the first step without pretending every prototype should become a platform.",
        "ladder_steps": [
            {"stage": "1. Personal script", "scope": "One person solves one recurring irritation.", "features": "GitHub repo, Copilot Chat, quick commits.", "outcome": "A useful page, script, or calculator exists where before there was only manual work."},
            {"stage": "2. Team tool", "scope": "A small service or lab starts using it together.", "features": "Shared repo, pull requests, Copilot code review, Spaces.", "outcome": "The tool stops being personal and becomes readable, reviewable team infrastructure."},
            {"stage": "3. Department system", "scope": "Several people maintain and extend the workflow.", "features": "Custom instructions, prompt files, custom agents, Agent skills.", "outcome": "The build process becomes repeatable instead of depending on one heroic maintainer."},
            {"stage": "4. Institution platform", "scope": "Governed rollout across units that need policy, ownership, and measurement.", "features": "Organisation policies, Enterprise governance, impact measurement, and the plan choices already mapped on the Plans page.", "outcome": "Prototype energy becomes an internal capability rather than a string of isolated experiments."},
        ],
        "amnesty_title": "Shadow IT amnesty: GitHub + Copilot as a safer home for the tools you already built",
        "amnesty_sub": "Most institutions already run on quiet ingenuity: Excel macros, Access databases, forgotten scripts, and heroic workarounds. The honest pitch is not “start building weird things.” It is “bring the useful weird things into a governed home.”",
        "amnesty_cards": [
            {"now": "Private spreadsheet macro on one laptop", "future": "A small repo with version history, README, and a visible owner", "why": "If the author leaves, the workflow does not disappear into a folder called Final-Final-v3."},
            {"now": "Hidden Access database or one-off admin form", "future": "A lightweight internal web app with pull requests and review", "why": "Everyone can see what changed, why it changed, and who approved it."},
            {"now": "Ad-hoc script copied between colleagues", "future": "A shared prompt file, Agent skill, or repository tool", "why": "The team improves one source of truth instead of duplicating ten slightly different versions."},
        ],
        "gallery_title": "Internal gallery: the reuse multiplier",
        "gallery_sub": "Once a few departments have built small tools, do not hide them. Put them in a shared GitHub repository or README index so the next team can fork something real instead of starting from zero.",
        "gallery_points": [
            "The gallery is not another platform to procure. It can be a normal repository with a clean README.",
            "Each entry should make reuse easy: what problem it solves, who owns it, what data sensitivity it has, and whether another department can adapt it.",
            "This is how one good pilot becomes three useful tools instead of three separate reinventions.",
        ],
        "gallery_template_title": "Simple README listing template",
        "gallery_template": [
            "## Tool name",
            "- Problem it solves:",
            "- Primary users:",
            "- Department owner:",
            "- Live link or demo:",
            "- Can another team fork it? yes / no",
            "- Data sensitivity:",
            "- Last updated:",
        ],
        "buy_title": "When buying is still the smarter move",
        "buy_sub": "Honesty is part of the credibility. Some categories really should stay off the vibe-coding table.",
        "buy_cards": [
            {"icon": "🏛️", "title": "Systems of record", "desc": "Student information systems, HR/payroll, finance ERP, and other legally or operationally authoritative systems belong in products with proven compliance, auditability, and institutional support."},
            {"icon": "♿", "title": "Certified accessibility and support obligations", "desc": "If you need accessibility certification, formal support contracts, or strict uptime guarantees from day one, an established vendor may still be the better answer."},
            {"icon": "🔌", "title": "Deep specialised integrations", "desc": "Some tools earn their price because they already integrate with the niche systems, contracts, and workflows that would be expensive to recreate safely."},
        ],
        "evidence_title": "How to measure rather than merely hope",
        "evidence_cards": [
            {
                "title": "Human experience matters too",
                "bullets": [
                    "GitHub research (2022) found that 60–75% of surveyed developers reported feeling more fulfilled, less frustrated, and able to focus on more satisfying work when using Copilot.",
                    "73% said Copilot helped them stay in the flow.",
                    "87% said it helped preserve mental energy on repetitive tasks.",
                ],
            },
            {
                "title": "Use the impact dashboard honestly",
                "bullets": [
                    "Business and Enterprise admins can use the Copilot impact dashboard to compare adoption cohorts with pull-request throughput.",
                    "It also includes a potential ROI view that compares average developer cost against PR output across adoption phases.",
                    "GitHub’s own guidance says to treat those figures as directional estimates rather than exact financial results.",
                ],
            },
        ],
        "next_title": "Where to go next",
        "next_cards": [
            {"icon": "🧪", "title": "Start with your first commit", "desc": "Use the guided beginner page when the main blocker is still “How do I even get this onto GitHub?”", "page": "first_commit", "cta": "Open the first-commit guide"},
            {"icon": "🎯", "title": "Show concrete examples", "desc": "Use the scenarios page when you need believable higher-education stories rather than theory.", "page": "scenarios", "cta": "Open the scenarios"},
            {"icon": "💼", "title": "Check plan reality", "desc": "Use the Plans page for the current Copilot plan map, pooled credit logic, and the honest rollout constraints.", "page": "plans", "cta": "Open Plans & reality"},
        ],
    },
    "fr": {
        "title": "Vibe coding vs acheter une solution toute faite",
        "sub": "La comparaison honnête n’est pas « Est-ce que Copilot remplace tous les éditeurs ? » Non. La vraie question est : quels petits outils internes doivent cesser de vivre comme shadow IT, abonnements SaaS dispersés ou tickets qui n’aboutissent jamais ?",
        "hero_note": "Utilise cette page pour la longue traîne des petits outils internes à faible enjeu : pages d’inscription, mini-tableaux de bord, pages de salles, assistants internes et autres besoins trop spécifiques pour mériter un projet de six mois mais trop utiles pour rester cachés dans des tableurs.",
        "changes_title": "Ce que change vraiment la construction assistée par IA",
        "changes_sub": "Copilot ne supprime ni le jugement d’ingénierie, ni les achats, ni la conformité. Ce qui change, c’est la vitesse, la propriété et l’économie de la première version qui fonctionne.",
        "change_cards": [
            {"icon": "⏱️", "title": "Temps jusqu’à la première version utile", "desc": "Un prototype en langage naturel peut apparaître en minutes ou en heures. Un nouvel achat SaaS peut demander découverte, achat, revue sécurité et déploiement avant le moindre test réel."},
            {"icon": "🏠", "title": "La propriété reste chez toi", "desc": "L’établissement peut garder code, historique et gouvernance dans sa propre organisation GitHub plutôt que de cacher logique et données dans un outil fournisseur."},
            {"icon": "🧩", "title": "La demande d’évolution devient un prompt", "desc": "Quand le workflow t’appartient, « ajoute un champ », « renomme ce statut » ou « change la validation » peut devenir la prochaine tâche Copilot au lieu d’une demande de roadmap."},
            {"icon": "💳", "title": "La forme du coût change", "desc": "Les plans Copilot payants combinent complétions illimitées et AI credits mutualisées, alors que la longue traîne d’outils SaaS renouvelle souvent des abonnements annuels séparés, utilisés ou non."},
        ],
        "comparison_title": "Un même problème, deux chemins",
        "comparison_sub": "Ces exemples portent volontairement sur de petits outils internes — pas sur le système de gestion des étudiantes et étudiants, la paie ou l’ERP.",
        "comparison_columns": ["Besoin", "Acheter un outil spécialisé", "Vibe coder une petite version interne", "Note honnête"],
        "comparison_rows": [
            {
                "need": "Mini-app de réservation de salles ou d’équipements",
                "buy": "Évaluer un produit de réservation dédié, demander un budget, revoir le traitement des données et accepter le workflow ainsi que la licence du fournisseur.",
                "build": "Commencer par un bâtiment, un labo ou un point de service. Demander à Copilot un formulaire, une vue de disponibilité et une liste admin, puis itérer les champs en langage clair.",
                "note": "Très bon candidat au vibe coding quand le périmètre reste local. Si l’outil devient la source institutionnelle de vérité pour toute la planification, acheter ou intégrer plus grand reste souvent plus intelligent.",
            },
            {
                "need": "FAQ interne ou assistant de connaissances",
                "buy": "Ajouter un autre produit de base de connaissances ou de chatbot, puis passer du temps à importer les documents et à aligner les permissions.",
                "build": "Utiliser Copilot Spaces avec GitHub Pages ou une petite coque d’application interne afin de publier d’abord un assistant ancré dans les documents de l’établissement.",
                "note": "Très utile lorsqu’un service a surtout besoin de réponses tirées de ses propres fichiers. Moins attractif si tu dois avoir dès le départ un support omnicanal et des SLA formels gérés par un fournisseur.",
            },
            {
                "need": "Page d’inscription à un événement",
                "buy": "Adopter une plateforme de formulaires ou d’événementiel avec ses modèles, exports et son abonnement récurrent.",
                "build": "Demander à Copilot de générer la page, les textes d’accessibilité, le flux de confirmation et le format d’export réellement utile à l’équipe événementielle.",
                "note": "Excellent pour des pilotes à faible risque et des événements ponctuels ou saisonniers. Moins pertinent si tu as immédiatement besoin de paiement, de contrats ou d’une intégration CRM complexe.",
            },
            {
                "need": "Tableau de bord de variance budgétaire",
                "buy": "Licencier encore un outil de reporting spécialisé et adapter les finances à son modèle de données.",
                "build": "Transformer l’export mensuel en tableau de bord statique ou petite application interne, avec calculs visibles dans le code et l’historique Git.",
                "note": "Très solide lorsque l’export source est déjà connu et que l’audience reste interne. Ce n’est pas le bon mouvement si le tableau doit devenir une plateforme réglementée et critique.",
            },
        ],
        "calculator": {
            "title": "Calculateur illustratif : combien coûte déjà le statu quo ?",
            "sub": "Entre tes propres chiffres. Ce n’est pas une promesse d’économies garanties — juste une manière de comparer la longue traîne des abonnements à de petits outils avec une capacité de construction appuyée par Copilot.",
            "inputs_title": "Tes entrées",
            "tools_label": "Combien de petits abonnements à des outils internes payes-tu aujourd’hui ?",
            "average_label": "Coût annuel moyen par outil (USD)",
            "builders_label": "Combien de personnes ont besoin de construire ou maintenir ces petits outils ?",
            "plan_label": "Quel plan Copilot veux-tu comparer ?",
            "business_label": "Business — 19 $ / siège / mois · 1 900 AI credits / mois",
            "enterprise_label": "Enterprise — 39 $ / siège / mois · 3 900 AI credits / mois",
            "results_title": "Ce que montre l’illustration",
            "spend_label": "Dépense annuelle en petits outils",
            "copilot_label": "Budget annuel de sièges Copilot",
            "credits_label": "AI credits incluses par mois",
            "gap_label": "Écart annuel illustratif",
            "gap_positive": "Tu dépenses actuellement plus par an en petits outils que dans le budget Copilot illustré ici.",
            "gap_negative": "Le budget de sièges Copilot illustré ici est supérieur à la dépense d’abonnements que tu as saisie.",
            "footnote": "Les complétions de code et next edit suggestions restent illimitées sur les plans payants. Le Chat, la CLI, Spaces, le cloud agent et les fonctions similaires consomment les AI credits mutualisées.",
            "plan_note": "Utilise la page Plans pour la réalité complète des tarifs, de l’éligibilité et des allocations promotionnelles de credits en 2026.",
        },
        "ladder_title": "Échelle de maturité du vibe coding",
        "ladder_sub": "Un chemin crédible entre « petite chose utile » et « capacité institutionnelle » aide à faire le premier pas sans prétendre que chaque prototype doit devenir une plateforme.",
        "ladder_steps": [
            {"stage": "1. Script personnel", "scope": "Une personne résout une irritation récurrente.", "features": "Dépôt GitHub, Copilot Chat, commits rapides.", "outcome": "Une page, un script ou un calculateur utile existe là où il n’y avait qu’un travail manuel."},
            {"stage": "2. Outil d’équipe", "scope": "Un petit service ou labo l’utilise ensemble.", "features": "Dépôt partagé, pull requests, Copilot code review, Spaces.", "outcome": "L’outil cesse d’être personnel et devient une petite infrastructure d’équipe, lisible et relisible."},
            {"stage": "3. Système de département", "scope": "Plusieurs personnes maintiennent et font évoluer le workflow.", "features": "Instructions personnalisées, prompt files, custom agents, Agent skills.", "outcome": "La manière de construire devient répétable au lieu de dépendre d’une seule personne héroïque."},
            {"stage": "4. Capacité d’établissement", "scope": "Déploiement gouverné entre entités avec politiques, ownership et mesure.", "features": "Politiques d’organisation, gouvernance Enterprise, mesure d’impact et choix de plans déjà cartographiés sur la page Plans.", "outcome": "L’énergie prototype devient une capacité interne plutôt qu’une série d’expériences isolées."},
        ],
        "amnesty_title": "Amnistie du shadow IT : GitHub + Copilot comme maison plus sûre pour les outils déjà bricolés",
        "amnesty_sub": "La plupart des établissements vivent déjà grâce à une ingéniosité silencieuse : macros Excel, bases Access, scripts oubliés et contournements héroïques. Le pitch honnête n’est pas « construis n’importe quoi ». C’est « mets les bricolages utiles dans une maison gouvernée ».",
        "amnesty_cards": [
            {"now": "Macro de tableur privée sur un seul ordinateur", "future": "Petit dépôt avec historique, README et personne responsable visible", "why": "Si l’autrice ou l’auteur s’en va, le workflow ne disparaît pas dans un dossier Final-Final-v3."},
            {"now": "Base Access cachée ou formulaire admin bricolé", "future": "Petite application interne avec pull requests et revue", "why": "Tout le monde peut voir ce qui a changé, pourquoi, et qui a validé."},
            {"now": "Script ad hoc recopié entre collègues", "future": "Prompt file, Agent skill ou outil partagé dans un dépôt", "why": "L’équipe améliore une seule source de vérité au lieu de dupliquer dix versions légèrement différentes."},
        ],
        "gallery_title": "Galerie interne : le multiplicateur de réutilisation",
        "gallery_sub": "Une fois que quelques services ont construit de petits outils, ne les cache pas. Place-les dans un dépôt GitHub partagé ou dans un index README afin que l’équipe suivante puisse forker quelque chose de réel.",
        "gallery_points": [
            "La galerie n’est pas une plateforme de plus à acheter. Un dépôt normal avec un README propre suffit.",
            "Chaque entrée doit faciliter la réutilisation : problème résolu, propriétaire, sensibilité des données et possibilité d’adaptation par un autre service.",
            "C’est ainsi qu’un bon pilote devient trois outils utiles au lieu de trois réinventions séparées.",
        ],
        "gallery_template_title": "Modèle simple de fiche README",
        "gallery_template": [
            "## Nom de l’outil",
            "- Problème résolu :",
            "- Publics principaux :",
            "- Service propriétaire :",
            "- Lien live ou démo :",
            "- Une autre équipe peut-elle le forker ? oui / non",
            "- Sensibilité des données :",
            "- Dernière mise à jour :",
        ],
        "buy_title": "Quand acheter reste le meilleur choix",
        "buy_sub": "L’honnêteté fait partie de la crédibilité. Certaines catégories doivent vraiment rester hors de la table du vibe coding.",
        "buy_cards": [
            {"icon": "🏛️", "title": "Systèmes de référence", "desc": "Les systèmes de gestion étudiante, RH/paie, ERP financiers et autres systèmes faisant autorité sur le plan légal ou opérationnel demandent des produits avec conformité, auditabilité et support institutionnel éprouvés."},
            {"icon": "♿", "title": "Accessibilité certifiée et obligations de support", "desc": "Si tu as besoin de certification d’accessibilité, de contrats de support formels ou de garanties strictes de disponibilité dès le départ, un fournisseur établi reste souvent la meilleure réponse."},
            {"icon": "🔌", "title": "Intégrations spécialisées profondes", "desc": "Certains outils justifient leur prix parce qu’ils apportent déjà les intégrations de niche, contrats et workflows qu’il serait coûteux et risqué de recréer."},
        ],
        "evidence_title": "Mesurer plutôt qu’espérer",
        "evidence_cards": [
            {
                "title": "L’expérience humaine compte aussi",
                "bullets": [
                    "La recherche GitHub (2022) montre que 60 à 75 % des personnes interrogées ont déclaré se sentir plus accomplies, moins frustrées et davantage capables de se concentrer sur un travail satisfaisant avec Copilot.",
                    "73 % ont déclaré que Copilot les aidait à rester dans le flow.",
                    "87 % ont déclaré qu’il aidait à préserver l’énergie mentale sur les tâches répétitives.",
                ],
            },
            {
                "title": "Utiliser le dashboard d’impact avec honnêteté",
                "bullets": [
                    "Les administratrices et administrateurs Business et Enterprise peuvent utiliser le Copilot impact dashboard pour comparer les cohortes d’adoption au débit de pull requests.",
                    "Il comprend aussi une vue de ROI potentiel qui compare coût moyen du travail et production de PR selon les phases d’adoption.",
                    "La documentation GitHub indique explicitement de traiter ces chiffres comme des estimations directionnelles, pas comme des résultats financiers exacts.",
                ],
            },
        ],
        "next_title": "Où aller ensuite",
        "next_cards": [
            {"icon": "🧪", "title": "Commencer par ton premier commit", "desc": "Utilise la page guidée si le principal blocage reste « comment est-ce que je mets ça sur GitHub ? »", "page": "first_commit", "cta": "Ouvrir le guide du premier commit"},
            {"icon": "🎯", "title": "Montrer des exemples concrets", "desc": "Utilise la page Scénarios quand tu as besoin d’histoires crédibles pour l’enseignement supérieur plutôt que de théorie.", "page": "scenarios", "cta": "Ouvrir les scénarios"},
            {"icon": "💼", "title": "Vérifier la réalité des plans", "desc": "Utilise la page Plans pour la carte actuelle des offres Copilot, la logique des credits mutualisées et les vraies contraintes de déploiement.", "page": "plans", "cta": "Ouvrir Plans & réalité"},
        ],
    },
    "nl": {
        "title": "Vibe coding vs een kant-en-klare oplossing kopen",
        "sub": "De eerlijke vergelijking is niet “Kan Copilot elke leverancier vervangen?” Dat kan het niet. De echte vraag is welke kleine interne tools moeten ophouden te leven als shadow IT, verspreide SaaS-abonnementen of backlogtickets die nooit landen.",
        "hero_note": "Gebruik deze pagina voor de lange staart van lichte interne tools: eventformulieren, mini-dashboards, ruimtepagina’s, interne assistenten en andere noden die te specifiek zijn voor een project van zes maanden maar te belangrijk om in spreadsheets verborgen te blijven.",
        "changes_title": "Wat verandert er wanneer bouwen met AI normaal wordt",
        "changes_sub": "Copilot haalt engineering judgement, procurement of compliance niet weg. Wat wel verandert, is de snelheid, het eigenaarschap en de economie van de eerste werkende versie.",
        "change_cards": [
            {"icon": "⏱️", "title": "Tijd tot een eerste werkende versie", "desc": "Een prototype in natuurlijke taal kan in minuten of uren verschijnen. Een nieuwe SaaS-aankoop vraagt vaak verkenning, procurement, security review en uitrol voordat iemand het eerste idee test."},
            {"icon": "🏠", "title": "Eigenaarschap blijft lokaal", "desc": "De instelling kan code, historiek en governance in de eigen GitHub-organisatie houden in plaats van logica en data te verstoppen in een leverancierstool."},
            {"icon": "🧩", "title": "Wijzigingsverzoeken worden prompts", "desc": "Wanneer de workflow van jou is, kan “voeg een veld toe”, “hernoem die status” of “pas de goedkeuring aan” de volgende Copilot-taak worden in plaats van een roadmapverzoek."},
            {"icon": "💳", "title": "De kostvorm verandert", "desc": "Betaalde Copilot-plannen combineren onbeperkte codecompletions met gedeelde AI credits, terwijl de lange staart van kleine SaaS-tools vaak als aparte jaarabonnementen blijft terugkeren, ongeacht werkelijk gebruik."},
        ],
        "comparison_title": "Hetzelfde probleem, twee paden",
        "comparison_sub": "Dit zijn bewust bescheiden interne tools — niet je studentinformatiesysteem, payrollsuite of ERP.",
        "comparison_columns": ["Nood", "Een gespecialiseerde tool kopen", "Een kleine interne versie vibe-coden", "Eerlijke noot"],
        "comparison_rows": [
            {
                "need": "Mini-app voor zaal- of materiaalreservatie",
                "buy": "Evalueer een gespecialiseerd reservatieproduct, vraag budget aan, bekijk de dataverwerking en accepteer de workflow en licentie van de leverancier.",
                "build": "Begin met één gebouw, één labo of één servicepunt. Vraag Copilot om een formulier, beschikbaarheidsoverzicht en adminlijst, en verfijn de velden daarna in gewone taal.",
                "note": "Sterke kandidaat voor vibe coding wanneer de scope lokaal blijft. Wordt het institutionele bron-van-waarheid voor alle planning, dan blijft kopen of groter integreren vaak slimmer.",
            },
            {
                "need": "Interne FAQ of kennisassistent",
                "buy": "Koop nog een kennis- of chatbotproduct en besteed daarna tijd aan documentimport en permissie-afstemming.",
                "build": "Gebruik Copilot Spaces met GitHub Pages of een lichte interne app-shell om eerst een gegronde assistent op basis van de eigen documenten van de instelling te publiceren.",
                "note": "Vooral nuttig wanneer één dienst vooral antwoorden uit de eigen bestanden nodig heeft. Minder aantrekkelijk als je vanaf dag één vendor-managed omnichannel support en formele SLA’s nodig hebt.",
            },
            {
                "need": "Event-inschrijfpagina",
                "buy": "Adopteer een formulier- of eventplatform met eigen templates, exports en terugkerend abonnement.",
                "build": "Vraag Copilot om de pagina, toegankelijkheidstekst, bevestigingsflow en exportvorm te maken die je eventteam echt nodig heeft.",
                "note": "Uitstekend voor laag-risico pilots en eenmalige of seizoensgebonden events. Minder sterk als je meteen betalingen, contracten of een complexe CRM-koppeling nodig hebt.",
            },
            {
                "need": "Budgetvariatiedashboard",
                "buy": "Neem nog een nichetool voor reporting en pas finance aan het datamodel van die tool aan.",
                "build": "Zet de maandelijkse export om in een statisch dashboard of kleine interne app, met zichtbare berekeningen in code en Git-historiek.",
                "note": "Sterk wanneer de broneport al gekend is en het publiek intern blijft. Niet de juiste keuze als het dashboard een gereguleerd, bedrijfskritisch rapporteringsplatform moet worden.",
            },
        ],
        "calculator": {
            "title": "Illustratieve calculator: wat kost de status quo nu al?",
            "sub": "Vul je eigen cijfers in. Dit is geen gegarandeerde besparingsclaim — alleen een manier om de lange staart van kleine toolabonnementen naast Copilot-ondersteunde bouwcapaciteit te leggen.",
            "inputs_title": "Jouw input",
            "tools_label": "Hoeveel kleine interne toolabonnementen betaal je vandaag?",
            "average_label": "Gemiddelde jaarlijkse kost per tool (USD)",
            "builders_label": "Hoeveel mensen moeten deze kleine tools kunnen bouwen of onderhouden?",
            "plan_label": "Met welk Copilot-plan vergelijk je?",
            "business_label": "Business — $19 / seat / maand · 1.900 AI credits / maand",
            "enterprise_label": "Enterprise — $39 / seat / maand · 3.900 AI credits / maand",
            "results_title": "Wat de illustratie laat zien",
            "spend_label": "Jaarlijkse spend op kleine tools",
            "copilot_label": "Jaarlijks Copilot-seatbudget",
            "credits_label": "Inbegrepen AI credits per maand",
            "gap_label": "Illustratief jaarlijks verschil",
            "gap_positive": "Er zit momenteel meer jaarlijkse spend in kleine tools dan in het Copilot-seatbudget dat hier getoond wordt.",
            "gap_negative": "Het Copilot-seatbudget dat hier getoond wordt ligt hoger dan de abonnementsspend die je hebt ingevoerd.",
            "footnote": "Codecompletions en next edit suggestions blijven onbeperkt op betaalde plannen. Chat, CLI, Spaces, cloud agent en gelijkaardige modelzware functies gebruiken de gedeelde AI credits.",
            "plan_note": "Gebruik de Plannen-pagina voor de volledige prijsrealiteit, details rond eligibility en de promotionele creditallocaties in 2026.",
        },
        "ladder_title": "Vibe Coding Maturity Ladder",
        "ladder_sub": "Een geloofwaardig pad van “klein nuttig ding” naar “institutionele capaciteit” helpt teams om de eerste stap te zetten zonder te doen alsof elk prototype een platform moet worden.",
        "ladder_steps": [
            {"stage": "1. Persoonlijk script", "scope": "Eén persoon lost één terugkerende irritatie op.", "features": "GitHub-repository, Copilot Chat, snelle commits.", "outcome": "Er bestaat nu een nuttige pagina, script of calculator waar vroeger alleen manueel werk was."},
            {"stage": "2. Teamtool", "scope": "Een kleine dienst of labo gebruikt het samen.", "features": "Gedeelde repo, pull requests, Copilot code review, Spaces.", "outcome": "De tool stopt met persoonlijk te zijn en wordt leesbare, reviewbare teaminfrastructuur."},
            {"stage": "3. Departementssysteem", "scope": "Meerdere mensen onderhouden en breiden de workflow uit.", "features": "Custom instructions, prompt files, custom agents, Agent skills.", "outcome": "Het bouwproces wordt herhaalbaar in plaats van af te hangen van één heroïsche beheerder."},
            {"stage": "4. Instellingsplatform", "scope": "Governed uitrol over eenheden die beleid, eigenaarschap en meting nodig hebben.", "features": "Organisatiebeleid, Enterprise-governance, impactmeting en de plankeuzes die al op de Plannen-pagina staan.", "outcome": "Prototype-energie wordt een interne capaciteit in plaats van een reeks losse experimenten."},
        ],
        "amnesty_title": "Shadow IT-amnestie: GitHub + Copilot als veiliger thuis voor de tools die je al bouwde",
        "amnesty_sub": "De meeste instellingen draaien nu al op stille vindingrijkheid: Excel-macro’s, Access-databases, vergeten scripts en heroïsche workarounds. De eerlijke pitch is niet “ga rare dingen bouwen”. Het is “breng de nuttige rare dingen naar een governed thuisbasis”.",
        "amnesty_cards": [
            {"now": "Privé spreadsheetmacro op één laptop", "future": "Kleine repo met versiegeschiedenis, README en zichtbare eigenaar", "why": "Als de maker vertrekt, verdwijnt de workflow niet in een map met Final-Final-v3."},
            {"now": "Verborgen Access-database of eenmalig adminformulier", "future": "Lichte interne webapp met pull requests en review", "why": "Iedereen kan zien wat veranderde, waarom het veranderde en wie het goedkeurde."},
            {"now": "Ad-hoc script dat tussen collega’s wordt doorgestuurd", "future": "Gedeelde prompt file, Agent skill of repositorytool", "why": "Het team verbetert één bron van waarheid in plaats van tien licht verschillende kopieën."},
        ],
        "gallery_title": "Interne galerij: de hergebruikvermenigvuldiger",
        "gallery_sub": "Wanneer een paar diensten al kleine tools gebouwd hebben, verstop ze dan niet. Zet ze in een gedeelde GitHub-repository of README-index zodat het volgende team iets echts kan forken in plaats van opnieuw van nul te beginnen.",
        "gallery_points": [
            "De galerij is geen extra platform dat je moet aankopen. Een normale repository met een duidelijke README volstaat.",
            "Elke entry moet hergebruik makkelijk maken: welk probleem ze oplost, wie eigenaar is, hoe gevoelig de data zijn en of een andere dienst ze kan aanpassen.",
            "Zo wordt één goede pilot drie bruikbare tools in plaats van drie aparte heruitvindingen.",
        ],
        "gallery_template_title": "Eenvoudige README-sjabloon",
        "gallery_template": [
            "## Naam van de tool",
            "- Probleem dat ze oplost:",
            "- Primaire gebruikers:",
            "- Dienst als eigenaar:",
            "- Live link of demo:",
            "- Kan een ander team dit forken? ja / nee",
            "- Datasensitiviteit:",
            "- Laatst bijgewerkt:",
        ],
        "buy_title": "Wanneer kopen nog altijd slimmer is",
        "buy_sub": "Eerlijkheid hoort bij geloofwaardigheid. Sommige categorieën horen echt buiten de vibe-codingtafel te blijven.",
        "buy_cards": [
            {"icon": "🏛️", "title": "Systemen van record", "desc": "Studentinformatiesystemen, HR/payroll, financiële ERP en andere juridisch of operationeel gezaghebbende systemen vragen producten met bewezen compliance, auditability en institutionele support."},
            {"icon": "♿", "title": "Gecertificeerde toegankelijkheid en supportverplichtingen", "desc": "Heb je vanaf dag één toegankelijkheidscertificatie, formele supportcontracten of strikte uptimegaranties nodig, dan blijft een gevestigde leverancier vaak de betere keuze."},
            {"icon": "🔌", "title": "Diepe gespecialiseerde integraties", "desc": "Sommige tools verdienen hun prijs omdat ze de nichesystemen, contracten en workflows al veilig ingebouwd hebben."},
        ],
        "evidence_title": "Meten in plaats van alleen hopen",
        "evidence_cards": [
            {
                "title": "De menselijke ervaring telt ook",
                "bullets": [
                    "GitHub-onderzoek (2022) liet zien dat 60–75% van de bevraagde developers zich meer vervuld, minder gefrustreerd en beter in staat voelde om zich op bevredigender werk te richten met Copilot.",
                    "73% zei dat Copilot hielp om in de flow te blijven.",
                    "87% zei dat het mentale energie op repetitief werk hielp sparen.",
                ],
            },
            {
                "title": "Gebruik het impact dashboard eerlijk",
                "bullets": [
                    "Business- en Enterprise-admins kunnen het Copilot impact dashboard gebruiken om adoptiecohorten te koppelen aan pull-requestthroughput.",
                    "Er is ook een mogelijke ROI-weergave die gemiddelde ontwikkelkost vergelijkt met PR-output over adoptiefases heen.",
                    "GitHub zegt zelf dat je die cijfers als directionele schattingen moet behandelen, niet als exacte financiële resultaten.",
                ],
            },
        ],
        "next_title": "Waarnaartoe nu",
        "next_cards": [
            {"icon": "🧪", "title": "Start met je eerste commit", "desc": "Gebruik de begeleide pagina wanneer de grootste blokkade nog altijd “hoe krijg ik dit op GitHub?” is.", "page": "first_commit", "cta": "Open de eerste-commitgids"},
            {"icon": "🎯", "title": "Toon concrete voorbeelden", "desc": "Gebruik de scenario’spagina wanneer je geloofwaardige hogeronderwijsverhalen nodig hebt in plaats van theorie.", "page": "scenarios", "cta": "Open de scenario’s"},
            {"icon": "💼", "title": "Controleer de planrealiteit", "desc": "Gebruik de Plannen-pagina voor de actuele Copilot-kaart, gedeelde-creditslogica en de eerlijke uitrolbeperkingen.", "page": "plans", "cta": "Open Plannen & realiteit"},
        ],
    },
}

TOOLKIT_SPOTLIGHT = {
    "en": {
        "title": "Two smart next steps",
        "sub": "If the prompt library gave you ideas, the next question is usually either “How do I make my first commit?” or “When should we build instead of buy?”",
        "cards": [
            {"icon": "🧪", "title": "Your first commit", "desc": "The zero-jargon walkthrough from account creation to browser-based pull-request merge.", "page": "first_commit", "cta": "Open the guide"},
            {"icon": "⚖️", "title": "Build vs buy", "desc": "Use the honest comparison, maturity ladder, and calculator before another small SaaS decision lands by default.", "page": "build_vs_buy", "cta": "Open the comparison"},
        ],
    },
    "fr": {
        "title": "Deux prochaines étapes intelligentes",
        "sub": "Si la boîte à outils t’a donné des idées, la question suivante est souvent soit « comment faire mon premier commit ? », soit « quand faut-il construire au lieu d’acheter ? »",
        "cards": [
            {"icon": "🧪", "title": "Ton premier commit", "desc": "Le guide sans jargon entre création de compte et fusion d’une pull request dans le navigateur.", "page": "first_commit", "cta": "Ouvrir le guide"},
            {"icon": "⚖️", "title": "Construire ou acheter", "desc": "Utilise la comparaison honnête, l’échelle de maturité et le calculateur avant de laisser un nouveau petit SaaS s’imposer par défaut.", "page": "build_vs_buy", "cta": "Ouvrir la comparaison"},
        ],
    },
    "nl": {
        "title": "Twee slimme volgende stappen",
        "sub": "Als de toolkit ideeën gaf, is de volgende vraag meestal ofwel “hoe maak ik mijn eerste commit?” ofwel “wanneer bouwen we beter zelf dan te kopen?”",
        "cards": [
            {"icon": "🧪", "title": "Jouw eerste commit", "desc": "De walkthrough zonder jargon van accountaanmaak tot merge van een pull request in de browser.", "page": "first_commit", "cta": "Open de gids"},
            {"icon": "⚖️", "title": "Bouwen of kopen", "desc": "Gebruik de eerlijke vergelijking, maturity ladder en calculator voordat nog een kleine SaaS-keuze automatisch gemaakt wordt.", "page": "build_vs_buy", "cta": "Open de vergelijking"},
        ],
    },
}

SCENARIO_STARTER_CALLOUT = {
    "en": {
        "starter_title": "Need the setup first?",
        "starter_desc": "Use the first-commit guide if your audience still needs the crystal-clear path from GitHub sign-up to a real merged pull request with Copilot.",
        "starter_cta": "Open the first-commit guide",
    },
    "fr": {
        "starter_title": "Besoin du tout début avant les scénarios ?",
        "starter_desc": "Utilise le guide du premier commit si ton public a encore besoin du chemin ultra-clair entre inscription GitHub et vraie pull request fusionnée avec Copilot.",
        "starter_cta": "Ouvrir le guide du premier commit",
    },
    "nl": {
        "starter_title": "Eerst de opstart nodig?",
        "starter_desc": "Gebruik de eerste-commitgids als je publiek nog de glasheldere route nodig heeft van GitHub-sign-up tot een echte gemergede pull request met Copilot.",
        "starter_cta": "Open de eerste-commitgids",
    },
}

MATURITY_CONTEXT_NOTES = {
    "en": {
        "plans_cta": "Take the 2-minute diagnostic",
        "first_commit": {
            "before": "If this first test already feels bigger than one repository, ",
            "link": "take the 2-minute diagnostic",
            "after": " to choose the most useful institutional next page.",
        },
        "toolkit": {
            "before": "Before one good prompt turns into a wider rollout conversation, ",
            "link": "take the 2-minute diagnostic",
            "after": " to choose the best institutional starting point.",
        },
        "scenarios": {
            "before": "If you are still unsure whether you need examples, rollout facts, or a first real GitHub loop, ",
            "link": "take the 2-minute diagnostic",
            "after": " to choose the right next page.",
        },
    },
    "fr": {
        "plans_cta": "Faire le diagnostic en 2 minutes",
        "first_commit": {
            "before": "Si ce premier essai semble déjà dépasser un seul dépôt, ",
            "link": "fais le diagnostic en 2 minutes",
            "after": " pour choisir la prochaine page institutionnelle la plus utile.",
        },
        "toolkit": {
            "before": "Avant de transformer un bon prompt en conversation de déploiement plus large, ",
            "link": "fais le diagnostic en 2 minutes",
            "after": " pour choisir le meilleur point de départ institutionnel.",
        },
        "scenarios": {
            "before": "Si tu hésites encore entre besoin d’exemples, questions de déploiement ou premier vrai flux GitHub, ",
            "link": "fais le diagnostic en 2 minutes",
            "after": " pour choisir la bonne prochaine page.",
        },
    },
    "nl": {
        "plans_cta": "Doe de diagnose in 2 minuten",
        "first_commit": {
            "before": "Als deze eerste test al groter voelt dan één repository, ",
            "link": "doe de diagnose in 2 minuten",
            "after": " om de nuttigste institutionele volgende pagina te kiezen.",
        },
        "toolkit": {
            "before": "Voor je één goed promptidee omzet in een breder uitrolgesprek, ",
            "link": "doe de diagnose in 2 minuten",
            "after": " om het beste institutionele startpunt te kiezen.",
        },
        "scenarios": {
            "before": "Als je nog twijfelt tussen nood aan voorbeelden, uitrolvragen of eerst een echte GitHub-lus, ",
            "link": "doe de diagnose in 2 minuten",
            "after": " om de juiste volgende pagina te kiezen.",
        },
    },
}

for lang in ("en", "fr", "nl"):
    patch = CONTENT_UPDATES[lang]
    patch["nav"].update({
        "first_commit": FIRST_COMMIT_CONTENT[lang]["title"],
        "build_vs_buy": BUILD_VS_BUY_CONTENT[lang]["title"],
    })
    patch["home"]["cta_tertiary"] = FIRST_COMMIT_CONTENT[lang]["title"]
    patch["home"]["cta_tertiary_page"] = "first_commit"
    patch["home"]["impact_stats"][0]["value"] = 26 + len(EXTRA_USECASES[lang])
    patch["home"]["quickref_teaser"] = {
        "en": "New here? See the 2-minute guide",
        "fr": "Nouveau sur le site ? Voir le repère en 2 minutes",
        "nl": "Nieuw op de site? Bekijk de wegwijzer in 2 minuten",
    }[lang]
    patch["home"]["start_free_diagnostic_prompt"] = {
        "en": "Still unsure?",
        "fr": "Tu hésites encore ?",
        "nl": "Nog niet zeker?",
    }[lang]
    patch["home"]["start_free_diagnostic_cta"] = {
        "en": "Take the 2-minute diagnostic",
        "fr": "Faire le diagnostic en 2 minutes",
        "nl": "Doe de diagnose in 2 minuten",
    }[lang]
    patch["toolkit_updates"] = {
        "spotlight_title": TOOLKIT_SPOTLIGHT[lang]["title"],
        "spotlight_sub": TOOLKIT_SPOTLIGHT[lang]["sub"],
        "spotlight_cards": TOOLKIT_SPOTLIGHT[lang]["cards"],
    }
    patch["scenarios"].update(SCENARIO_STARTER_CALLOUT[lang])
    patch["first_commit"] = FIRST_COMMIT_CONTENT[lang]
    patch["build_vs_buy"] = BUILD_VS_BUY_CONTENT[lang]
    patch["explorer"]["features"] = patch["explorer"]["features"] + EXTRA_EXPLORER_FEATURES[lang]
    patch["explorer"]["extra_usecases"] = EXTRA_USECASES[lang]
    patch["explorer"]["sub"] = {
        "en": "36 concrete, ready-to-follow use cases across every part of higher education. Filter by role or by real GitHub Copilot feature families, then open a card for the exact steps.",
        "fr": "36 cas d’usage concrets, directement exploitables dans tout l’enseignement supérieur. Filtre par rôle ou par vraies familles de fonctionnalités GitHub Copilot, puis ouvre une carte pour voir les étapes exactes.",
        "nl": "36 concrete, direct bruikbare use cases voor elk onderdeel van het hoger onderwijs. Filter op rol of op echte GitHub Copilot-featurefamilies en open daarna een kaart voor de exacte stappen.",
    }[lang]


def apply_content_updates(content):
    for lang, patch in CONTENT_UPDATES.items():
        if not patch:
            continue

        data = content[lang]
        data["nav"].update(patch["nav"])
        data["home"].update(patch["home"])
        data["home"]["personas"] = patch["home_personas"]
        data["home"]["examples"] = patch["home_examples"]
        data["best_practices"] = patch["best_practices"]
        data["about"] = patch["about"]
        data["quiz_ui"] = patch["quiz_ui"]
        data["plans"] = patch["plans"]
        data["scenarios"] = patch["scenarios"]
        if patch.get("toolkit_updates"):
            data["toolkit"].update(patch["toolkit_updates"])
        if patch.get("first_commit"):
            data["first_commit"] = patch["first_commit"]
        if patch.get("build_vs_buy"):
            data["build_vs_buy"] = patch["build_vs_buy"]
        for key, value in EXTRA_PAGE_CONTENT.get(lang, {}).items():
            data[key] = value

        for track_key, track_patch in patch["tracks"].items():
            track = data["tracks"][track_key]
            for key, value in track_patch.items():
                if key in {"lesson_updates", "quiz"}:
                    continue
                track[key] = value
            for lesson_index, lesson_patch in track_patch.get("lesson_updates", {}).items():
                track["lessons"][lesson_index].update(lesson_patch)
            track["quiz"] = track_patch["quiz"]

        explorer = data["explorer"]
        explorer["sub"] = patch["explorer"]["sub"]
        explorer["features"] = patch["explorer"]["features"]
        for usecase in explorer["usecases"]:
            usecase["features"] = [FEATURE_KEY_REMAP.get(feature, feature) for feature in usecase["features"]]
        for idx, usecase_patch in patch["explorer"]["usecase_rewrites"].items():
            explorer["usecases"][idx].update(usecase_patch)
        if patch["explorer"].get("extra_usecases"):
            explorer["usecases"].extend(patch["explorer"]["extra_usecases"])


def generate_site(content, root, langs, lang_label):
    apply_content_updates(content)
    track_order = ["basics", "advanced", "expert"]

    def esc(s):
        if s is None:
            return ""
        return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def slugify(value):
        normalized = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
        return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-") or "item"

    def json_html(data):
        return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    def page_filename(lang, page_key):
        if page_key in track_order:
            return content[lang]["tracks"][page_key]["slug"] + ".html"
        return ROUTE_FILENAMES.get(page_key, "index.html")

    def page_href(lang, page_key):
        return f"../{lang}/{page_filename(lang, page_key)}"

    def local_href(page_key, lang):
        return page_filename(lang, page_key)

    def glossary_href(lang, item_id):
        return f'{local_href("glossary", lang)}#{item_id}'

    def current_page_label(lang, current_page):
        nav = content[lang]["nav"]
        ui = PAGE_UI[lang]
        if current_page in track_order:
            return content[lang]["tracks"][current_page]["title"]
        return nav.get(current_page) or {
            "explorer": content[lang]["explorer"]["title"],
            "plans": content[lang]["plans"]["title"],
            "scenarios": content[lang]["scenarios"]["title"],
            "best_practices": content[lang]["best_practices"]["title"],
            "toolkit": content[lang]["toolkit"]["title"],
            "about": content[lang]["about"]["title"],
            "first_commit": content[lang]["first_commit"]["title"],
            "build_vs_buy": content[lang]["build_vs_buy"]["title"],
            "glossary": ui["glossary_title"],
            "workshop": ui["workshop_title"],
            "certificate": ui["certificate_title"],
            "quick_reference": content[lang]["quick_reference"]["title"],
            "sitemap": ui["sitemap_title"],
            "maturity": content[lang]["maturity"]["title"],
            "changelog": content[lang]["changelog"]["title"],
        }.get(current_page, "")

    def hreflang_links_html(page_key):
        links = [
            f'<link rel="alternate" hreflang="{other}" href="{page_href(other, page_key)}">'
            for other in langs
        ]
        links.append(f'<link rel="alternate" hreflang="x-default" href="{page_href("en", page_key)}">')
        return "\n  ".join(links)

    def language_banner_shell(lang, current_page):
        banner = LANGUAGE_BANNER_UI[lang]
        data_attrs = " ".join(
            [
                f'data-alt-{other}="{page_href(other, current_page)}"'
                for other in langs
            ]
            + [
                f'data-label-{other}="{LANGUAGE_NAMES[other]}"'
                for other in langs
            ]
        )
        return f"""<div class="language-banner-shell" data-language-banner hidden
  {data_attrs}
  data-prefix="{esc(banner["prefix"])}"
  data-cta="{esc(banner["cta"])}"
  data-dismiss="{esc(banner["dismiss"])}"></div>"""

    def source_link(lang, url, label=None):
        return f'<a class="source-link" href="{url}" target="_blank" rel="noopener">{esc(label or SOURCE_LABEL[lang])}</a>'

    def source_links_html(lang, items):
        if not items:
            return ""
        links = []
        for item in items:
            if isinstance(item, tuple):
                label, url = item
            else:
                label, url = None, item
            links.append(source_link(lang, url, label))
        return f'<span class="source-links">{" ".join(links)}</span>'

    def render_fact_banner(lang):
        ui = PAGE_UI[lang]
        return f"""<div class="fact-banner" data-reveal>
      <strong>{esc(ui["verified_tag"])}</strong>
      <span>{esc(FACT_BANNERS[lang])}</span>
    </div>"""

    def feature_html(feature, lang):
        url = FEATURE_DOCS.get(feature)
        if not url:
            return f'<span class="feature-chip">{esc(feature)}</span>'
        return f'<a class="feature-chip feature-chip-link" href="{url}" target="_blank" rel="noopener">{esc(feature)}</a>'

    def glossary_shortcuts_html(lang, item_ids):
        ui = PAGE_UI[lang]
        lookup = {
            item["id"]: item["term"]
            for group in GLOSSARY_GROUPS[lang]
            for item in group["items"]
        }
        links = "".join(
            f'<a href="{glossary_href(lang, item_id)}">{esc(lookup[item_id])}</a>'
            for item_id in item_ids
            if item_id in lookup
        )
        return f"""<div class="glossary-shortcuts" data-reveal>
      <strong>{esc(ui["glossary_shortcuts_title"])}</strong>
      <div class="glossary-shortcuts-links">{links}</div>
    </div>"""

    def search_modal_html(lang):
        ui = PAGE_UI[lang]
        return f"""<div class="search-modal" data-search-modal hidden>
  <div class="search-modal-backdrop" data-search-close></div>
  <div class="search-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="search-modal-title">
    <div class="search-modal-head">
      <div>
        <h2 id="search-modal-title">{esc(ui["search_title"])}</h2>
        <p>{esc(ui["search_hint"])}</p>
      </div>
      <button type="button" class="search-close" data-search-close aria-label="{esc(ui["search_close"])}">×</button>
    </div>
    <label class="search-input-wrap">
      <span class="sr-only">{esc(ui["search_title"])}</span>
      <input type="search" data-search-input placeholder="{esc(ui["search_placeholder"])}" autocomplete="off">
    </label>
    <div class="search-results" data-search-results></div>
    <p class="search-empty" data-search-empty hidden>{esc(ui["search_empty"])}</p>
  </div>
  </div>"""

    def lang_switch_html(lang, page_key, desktop=True):
        cls = "lang-switch desktop-only" if desktop else "lang-switch"
        links = []
        for other in langs:
            active = "active" if other == lang else ""
            links.append(f'<a class="{active}" href="{page_href(other, page_key)}">{lang_label[other]}</a>')
        return f'<div class="{cls}">' + "".join(links) + "</div>"

    def nav_course_group_html(lang, track_key):
        track = content[lang]["tracks"][track_key]
        nav = content[lang]["nav"]
        href = local_href(track_key, lang)
        items = "".join(
            f'<li><a href="{href}#lesson-{i+1}"><span>{i+1}</span><strong>{esc(lesson["title"])}</strong></a></li>'
            for i, lesson in enumerate(track["lessons"])
        )
        return f"""<div class="nav-course-group">
      <a class="nav-trigger" href="{href}">{esc(nav[track_key])}</a>
      <div class="nav-lesson-panel">
        <div class="nav-lesson-panel-head"><span>{esc(nav["all_lessons"])}</span><strong>{esc(track["level_label"])}</strong></div>
        <ol class="nav-lesson-list">{items}</ol>
        <a class="nav-lesson-overview" href="{href}">{esc(nav["view_route"])}<span aria-hidden="true">→</span></a>
      </div>
    </div>"""

    def nav_courses_menu_html(lang):
        nav = content[lang]["nav"]
        ui = PAGE_UI[lang]
        items = "".join(
            f'<li><a href="{local_href(t, lang)}"><span>{i + 1}</span>'
            f'<strong>{esc(nav[t])}</strong></a></li>'
            for i, t in enumerate(track_order)
        )
        first_href = local_href(track_order[0], lang)
        first_commit_link = ""
        if nav.get("first_commit"):
            first_commit_link = (
                f'<a class="nav-lesson-overview" href="{local_href("first_commit", lang)}">'
                f'{esc(nav["first_commit"])}<span aria-hidden="true">→</span></a>'
            )
        certificate_link = (
            f'<a class="nav-certificate-link" data-certificate-cta href="{local_href("certificate", lang)}" hidden>'
            f'{esc(ui["certificate_cta"])}<span aria-hidden="true">↘</span></a>'
        )
        return f"""<div class="nav-course-group">
      <a class="nav-trigger" href="{first_href}">{esc(nav.get("courses_menu", "Courses"))}</a>
      <div class="nav-lesson-panel">
        <div class="nav-lesson-panel-head"><span>{esc(nav.get("courses_menu", "Courses"))}</span></div>
        <ol class="nav-lesson-list">{items}</ol>
        {first_commit_link}
        {certificate_link}
      </div>
    </div>"""

    def mobile_course_group_html(lang, track_key):
        track = content[lang]["tracks"][track_key]
        nav = content[lang]["nav"]
        href = local_href(track_key, lang)
        items = "".join(
            f'<li><a href="{href}#lesson-{i+1}"><span>{i+1}</span><strong>{esc(lesson["title"])}</strong></a></li>'
            for i, lesson in enumerate(track["lessons"])
        )
        return f"""<details class="mobile-course-details">
      <summary class="mobile-course-summary"><span>{esc(nav[track_key])}</span></summary>
      <div class="mobile-course-body">
        <ol class="nav-lesson-list">{items}</ol>
        <a class="nav-lesson-overview" href="{href}">{esc(nav["view_route"])}<span aria-hidden="true">→</span></a>
      </div>
    </details>"""

    def header_link(label, href, active=False, accent=False):
        classes = ["nav-trigger"]
        if active:
            classes.append("active")
        if accent:
            classes.append("accent")
        return f'<a class="{" ".join(classes)}" href="{href}">{esc(label)}</a>'

    def render_wayfinding(lang, current_page):
        nav = content[lang]["nav"]
        ui = PAGE_UI[lang]
        trail = [f'<a href="{local_href("home", lang)}">{esc(nav["home"])}</a>']

        if current_page in track_order:
            track = content[lang]["tracks"][current_page]
            trail.extend([
                f'<span>{esc(nav.get("courses_menu", "Courses"))}</span>',
                f'<span aria-current="page">{esc(track["title"])}</span>',
            ])
            switcher = ""
            for key in track_order:
                current_attr = ' aria-current="page"' if key == current_page else ""
                active_class = " is-active" if key == current_page else ""
                switcher += f'<a class="track-pill{active_class}" href="{local_href(key, lang)}"{current_attr}>{esc(content[lang]["tracks"][key]["level_label"])}</a>'
            return f"""<div class="page-wayfinding">
      <nav class="page-breadcrumb" aria-label="Breadcrumb">{'<span class="page-breadcrumb-sep" aria-hidden="true">/</span>'.join(trail)}</nav>
      <div class="track-wayfinding" aria-label="{esc(nav.get("courses_menu", "Courses"))}">{switcher}</div>
    </div>"""

        current_label = current_page_label(lang, current_page)
        trail.append(f'<span aria-current="page">{esc(current_label)}</span>')
        return f"""<div class="page-wayfinding">
      <nav class="page-breadcrumb" aria-label="Breadcrumb">{'<span class="page-breadcrumb-sep" aria-hidden="true">/</span>'.join(trail)}</nav>
    </div>"""

    def header_html(lang, current_page):
        nav = content[lang]["nav"]
        meta = content[lang]["meta"]
        ui = PAGE_UI[lang]
        courses_menu = nav_courses_menu_html(lang)
        mobile_groups = "".join(mobile_course_group_html(lang, t) for t in track_order)
        home_href = local_href("home", lang)
        explorer_href = local_href("explorer", lang)
        scenarios_href = local_href("scenarios", lang)
        plans_href = local_href("plans", lang)
        bp_href = local_href("best_practices", lang)
        toolkit_href = local_href("toolkit", lang)
        about_href = local_href("about", lang)
        glossary_href_local = local_href("glossary", lang)
        workshop_href = local_href("workshop", lang)
        quickref_href = local_href("quick_reference", lang)
        sitemap_href = local_href("sitemap", lang)
        maturity_href = local_href("maturity", lang)
        changelog_href = local_href("changelog", lang)
        return f"""<header class="site-header">
  <div class="container header-inner">
    <a class="brand-mark" href="{home_href}" aria-label="{esc(meta["site_name"])}">
      <svg width="26" height="26" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0a8 8 0 0 0-2.53 15.59c.4.07.55-.17.55-.38l-.01-1.49c-2.01.44-2.43-.97-2.43-.97-.33-.83-.8-1.05-.8-1.05-.66-.45.05-.44.05-.44.72.05 1.1.74 1.1.74.64 1.1 1.68.78 2.09.6.07-.46.25-.78.46-.96-1.6-.18-3.29-.8-3.29-3.57 0-.79.28-1.43.74-1.93-.07-.18-.32-.92.07-1.92 0 0 .61-.19 1.99.74a6.9 6.9 0 0 1 3.63 0c1.38-.93 1.99-.74 1.99-.74.39 1 .14 1.74.07 1.92.46.5.74 1.14.74 1.93 0 2.78-1.69 3.39-3.3 3.57.26.22.49.66.49 1.33l-.01 1.97c0 .21.14.45.55.38A8 8 0 0 0 8 0Z"/></svg>
      <span class="brand-text"><span class="b1">{esc(meta["site_name"])}</span><span class="b2">{esc(meta.get("brand_tagline", "GitHub Copilot"))}</span></span>
    </a>
    <nav class="desktop-nav" aria-label="Main">
      <span>{header_link(nav.get("explorer", "Use cases"), explorer_href, current_page == "explorer", accent=True)}</span>
      <span>{header_link(nav.get("scenarios", "Scenarios"), scenarios_href, current_page == "scenarios")}</span>
      {courses_menu}
      <span>{header_link(nav.get("plans", "Plans"), plans_href, current_page == "plans")}</span>
      <span>{header_link(nav.get("toolkit", "Toolkit"), toolkit_href, current_page == "toolkit")}</span>
      <span>{header_link(nav["best_practices"], bp_href, current_page == "best_practices")}</span>
      <span>{header_link(nav["about"], about_href, current_page == "about")}</span>
    </nav>
    <div class="header-actions">
      {lang_switch_html(lang, current_page, desktop=True)}
      <button class="search-toggle" type="button" data-search-open aria-label="{esc(ui["search_open"])}">🔍</button>
      <button class="mobile-nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav-panel"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="mobile-nav-panel container" id="mobile-nav-panel" hidden>
    <div class="mobile-nav-group">
      <div class="mobile-nav-group-label">{esc(nav.get("mobile_group_learn", "Learn"))}</div>
      <a href="{scenarios_href}" class="mobile-nav-link">{esc(nav.get("scenarios", "Scenarios"))}</a>
      {mobile_groups}
      <a href="{local_href("first_commit", lang)}" class="mobile-nav-link">{esc(nav.get("first_commit", "First commit"))}</a>
      <a href="{local_href("build_vs_buy", lang)}" class="mobile-nav-link">{esc(nav.get("build_vs_buy", "Build vs buy"))}</a>
    </div>
    <div class="mobile-nav-group">
      <div class="mobile-nav-group-label">{esc(nav.get("mobile_group_tools", "Tools"))}</div>
      <button type="button" class="mobile-nav-link mobile-nav-button" data-search-open>{esc(ui["mobile_search"])}</button>
      <a href="{explorer_href}" class="mobile-nav-link accent">{esc(nav.get("explorer", "Use cases"))}</a>
      <a href="{plans_href}" class="mobile-nav-link">{esc(nav.get("plans", "Plans"))}</a>
      <a href="{toolkit_href}" class="mobile-nav-link">{esc(nav.get("toolkit", "Toolkit"))}</a>
      <a href="{quickref_href}" class="mobile-nav-link">{esc(content[lang]["quick_reference"]["title"])}</a>
      <a href="{maturity_href}" class="mobile-nav-link">{esc(content[lang]["maturity"]["title"])}</a>
    </div>
    <div class="mobile-nav-group">
      <div class="mobile-nav-group-label">{esc(nav.get("mobile_group_resources", "Resources"))}</div>
      <a href="{workshop_href}" class="mobile-nav-link">{esc(ui["workshop_title"])}</a>
      <a href="{glossary_href_local}" class="mobile-nav-link">{esc(ui["glossary_title"])}</a>
      <a href="{sitemap_href}" class="mobile-nav-link">{esc(ui["sitemap_title"])}</a>
      <a href="{changelog_href}" class="mobile-nav-link">{esc(content[lang]["changelog"]["title"])}</a>
      <a href="{bp_href}" class="mobile-nav-link">{esc(nav["best_practices"])}</a>
      <a href="{about_href}" class="mobile-nav-link">{esc(nav["about"])}</a>
    </div>
  </div>
  </header>"""

    def footer_html(lang):
        nav = content[lang]["nav"]
        footer = content[lang]["footer"]
        meta = content[lang]["meta"]
        ui = PAGE_UI[lang]
        links = [
            ("home", nav["home"]),
            ("explorer", nav.get("explorer", "Use cases")),
            ("scenarios", nav.get("scenarios", "Scenarios")),
            ("first_commit", nav.get("first_commit", "First commit")),
            ("build_vs_buy", nav.get("build_vs_buy", "Build vs buy")),
            ("plans", nav.get("plans", "Plans")),
            ("quick_reference", content[lang]["quick_reference"]["title"]),
            ("maturity", content[lang]["maturity"]["title"]),
            ("workshop", ui["workshop_title"]),
            ("glossary", ui["glossary_title"]),
            ("sitemap", ui["sitemap_title"]),
            ("changelog", content[lang]["changelog"]["title"]),
            ("best_practices", nav["best_practices"]),
            ("about", nav["about"]),
        ]
        link_html = "".join(f'<a href="{local_href(key, lang)}">{esc(label)}</a>' for key, label in links)
        promo = footer.get("crosspromo")
        promo_html = ""
        if promo:
            promo_html = f"""<a class="footer-crosspromo" href="{esc(promo["url"])}" target="_blank" rel="noopener">
      <span class="footer-crosspromo-icon" aria-hidden="true">📅</span>
      <span class="footer-crosspromo-body">
        <span class="footer-crosspromo-eyebrow">{esc(promo["eyebrow"])}</span>
        <strong class="footer-crosspromo-title">{esc(promo["title"])}</strong>
        <span class="footer-crosspromo-text">{esc(promo["text"])}</span>
      </span>
      <span class="footer-crosspromo-cta">{esc(promo["cta"])} &rarr;</span>
    </a>"""
        return f"""<footer class="site-footer">
  <div class="container footer-inner">
    {promo_html}
    <p>© {CURRENT_YEAR} {esc(meta["site_name"])}. {esc(footer["text"])}</p>
    <div class="footer-links">{link_html}</div>
  </div>
  </footer>"""

    def feedback_widget_html(lang, current_page):
        if current_page not in FEEDBACK_WIDGET_PAGES:
            return ""
        t = FEEDBACK_WIDGET_TEXT[lang]
        return f"""<div class="feedback-widget container" data-feedback-widget data-feedback-page="{esc(current_page)}">
    <p class="feedback-question">{esc(t["question"])}</p>
    <div class="feedback-actions">
      <button type="button" class="feedback-btn" data-feedback-vote="up">{esc(t["yes"])}</button>
      <button type="button" class="feedback-btn" data-feedback-vote="down">{esc(t["no"])}</button>
    </div>
    <p class="feedback-thanks" hidden>{esc(t["thanks"])}</p>
  </div>"""

    def page_shell(lang, current_page, title, description, body_html):
        meta = content[lang]["meta"]
        full_title = f"{title} — {meta['site_name']}"
        body_class = f"page-{current_page.replace('_', '-')}"
        body_html = re.sub(r"<main(?=[\s>])", '<main id="main-content"', body_html, count=1)
        goatcounter_script = ""
        if GOATCOUNTER_CODE and GOATCOUNTER_CODE != "PLACEHOLDER_GOATCOUNTER_CODE":
            goatcounter_script = (
                f'<script data-goatcounter="https://{GOATCOUNTER_CODE}.goatcounter.com/count" '
                f'async src="https://gc.zgo.at/count.js"></script>\n  '
            )
        return f"""<!DOCTYPE html>
  <html lang="{meta["html_lang"]}">
  <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(full_title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta property="og:title" content="{esc(full_title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{OG_LOCALE[lang]}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{esc(full_title)}">
  <meta name="twitter:description" content="{esc(description)}">
  {hreflang_links_html(current_page)}
  <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
  <link rel="stylesheet" href="../assets/style.min.css">
  </head>
  <body class="{body_class}" data-search-index="../assets/search-index.{lang}.json" data-lang="{lang}">
  <a class="skip-link" href="#main-content">{esc(SKIP_LINK_LABEL[lang])}</a>
  {header_html(lang, current_page)}
  {language_banner_shell(lang, current_page)}
  {body_html}
  {feedback_widget_html(lang, current_page)}
  {footer_html(lang)}
  {search_modal_html(lang)}
  <button type="button" class="back-to-top" data-back-to-top aria-label="{esc(BACK_TO_TOP_LABEL[lang])}" title="{esc(BACK_TO_TOP_LABEL[lang])}" hidden>&#8593;</button>
  <script src="../assets/qrcode.min.js" defer></script>
  <script src="../assets/script.js" defer></script>
  {goatcounter_script}</body>
  </html>"""
    def render_counter_card(item):
        return f"""<div class="impact-stat" data-reveal>
      <div class="impact-stat-value" data-counter="{int(item["value"])}">0</div>
      <h3>{esc(item["label"])}</h3>
      <p>{esc(item["desc"])}</p>
    </div>"""

    def render_course_progress(lang, track_key):
        ui = PAGE_UI[lang]
        track = content[lang]["tracks"][track_key]
        suffix = {
            "fr": "leçons terminées",
            "en": "lessons completed",
            "nl": "lessen voltooid",
        }[lang]
        return f"""<div class="course-progress-card" data-track-progress data-lang="{lang}" data-track="{track_key}" data-total="{len(track["lessons"])}">
      <div class="course-progress-copy">
        <span class="eyebrow">{esc(ui["progress_label"])}</span>
        <strong data-track-progress-text>0 / {len(track["lessons"])} {esc(suffix)}</strong>
        <p>{esc(ui["quiz_status"])}</p>
      </div>
      <a class="btn btn-primary course-certificate-cta" data-certificate-cta href="{local_href("certificate", lang)}" hidden>{esc(ui["certificate_cta"])}</a>
    </div>"""

    def render_quiz(lang, track_key):
        track = content[lang]["tracks"][track_key]
        quiz_data = track.get("quiz")
        if not quiz_data:
            return ""
        ui = content[lang]["quiz_ui"]
        questions_html = ""
        for idx, item in enumerate(quiz_data["questions"]):
            options = "".join(
                f'<button type="button" class="quiz-option" data-index="{i}" data-correct="{"true" if i == item["answer"] else "false"}">{esc(option)}</button>'
                for i, option in enumerate(item["options"])
            )
            questions_html += f"""<article class="quiz-question" data-reveal>
      <div class="quiz-question-head"><span>{idx + 1}</span><h3>{esc(item["question"])}</h3></div>
      <div class="quiz-options">{options}</div>
      <div class="quiz-feedback" hidden>
        <strong></strong>
        <p>{esc(item["explanation"])}</p>
      </div>
    </article>"""
        return f"""<section class="quiz-section" data-reveal>
  <div class="quiz-card" data-quiz data-lang="{lang}" data-track="{track_key}" data-storage-key="vibecoding_quiz_{lang}_{track_key}" data-pass-score="{quiz_data.get("pass_score", len(quiz_data["questions"]))}" data-correct-label="{esc(ui["correct_label"])}" data-wrong-label="{esc(ui["wrong_label"])}" data-success-message="{esc(ui["success_message"])}" data-retry-message="{esc(ui["retry_message"])}">
    <div class="quiz-head">
      <span class="eyebrow">{esc(ui["eyebrow"])}</span>
      <h2>{esc(quiz_data["title"])}</h2>
      <p>{esc(quiz_data["intro"])}</p>
    </div>
    <div class="quiz-scoreboard">
      <div><span>{esc(ui["score_label"])}</span><strong data-quiz-score>0</strong> / <span data-quiz-total>{len(quiz_data["questions"])}</span></div>
      <div><span>{esc(ui["answered_label"])}</span><strong data-quiz-answered>0</strong> / <span>{len(quiz_data["questions"])}</span></div>
      <button type="button" class="btn btn-ghost quiz-reset">{esc(ui["reset_label"])}</button>
    </div>
    <p class="quiz-storage-note">{esc(PAGE_UI[lang]["quiz_status"])}</p>
    <div class="quiz-questions">{questions_html}</div>
    <p class="quiz-summary-note" hidden data-quiz-summary></p>
  </div>
</section>"""

    def render_home(lang):
        home = content[lang]["home"]
        nav = content[lang]["nav"]
        meta = content[lang]["meta"]
        scenarios = content[lang]["scenarios"]

        hero_visual = home["hero_visual"]
        badge_html = "".join(f'<span class="hero-visual-badge">{esc(badge)}</span>' for badge in hero_visual["badges"])
        hero_lines = hero_visual["lines"]
        line_html = "".join(
            f'<span class="hero-visual-line{" is-last" if i == len(hero_lines) - 1 else ""}" '
            f'style="--line-delay:{i * 0.9:.2f}s"><span class="hero-visual-line-text" '
            f'style="--char-count:{len(line)}">{esc(line)}</span></span>'
            for i, line in enumerate(hero_lines)
        )
        stat_cards = "".join(render_counter_card(item) for item in home.get("impact_stats", []))
        start_cards = "".join(
            f"""<a class="start-card{' is-featured' if card.get('featured') else ''}" data-reveal href="{card.get("href") or local_href(card["page"], lang)}">{f'<span class="start-card-badge">{esc(card["badge"])}</span>' if card.get("badge") else ''}<span class="start-card-icon">{card["icon"]}</span><h3>{esc(card["title"])}</h3><p>{esc(card["desc"])}</p><span class="start-card-cta">{esc(card["cta"])} →</span></a>"""
            for card in home.get("start_free_cards", [])
        )
        start_links = "".join(
            f'<a href="{local_href(item["page"], lang)}">{esc(item["label"])}</a>'
            for item in home.get("start_free_links", [])
        )
        start_diagnostic = ""
        if home.get("start_free_diagnostic_cta"):
            start_diagnostic = f'<div class="start-inline-links" data-reveal><span>{esc(home["start_free_diagnostic_prompt"])}</span><a href="{local_href("maturity", lang)}">{esc(home["start_free_diagnostic_cta"])}</a></div>'
        quickref_teaser = ""
        if home.get("quickref_teaser"):
            quickref_teaser = f'<div class="hero-link-row"><a class="filter-pill" href="{local_href("quick_reference", lang)}">{esc(home["quickref_teaser"])} →</a></div>'
        persona_cards = "".join(
            f"""<div class="persona-card" data-reveal>
      <div class="persona-icon">{icon}</div>
      <h3>{esc(role)}</h3>
      <p class="persona-pitch">{esc(pitch)}</p>
      <p class="persona-example"><strong>{esc(example_label)}</strong> {esc(example_text)}</p>
    </div>"""
            for icon, role, pitch, example_label, example_text in home.get("personas", [])
        )
        journey_cards = "".join(
            f"""<div class="journey-card" data-reveal><div class="num">{num}</div><h3>{esc(title)}</h3><p>{esc(desc)}</p></div>"""
            for num, title, desc in home["journey"]
        )
        extra_examples = "".join(
            f"""<li data-reveal><span class="persona-pill">{esc(persona)}</span><div><strong>{esc(title)}</strong><span>{esc(desc)}</span></div></li>"""
            for title, desc, persona in home.get("examples", [])
        )

        course_cards = ""
        for track_key in track_order:
            track = content[lang]["tracks"][track_key]
            href = local_href(track_key, lang)
            course_cards += f"""<a class="course-card" data-reveal href="{href}" style="text-decoration:none;">
      <span class="level-tag {track["tag_class"]}">{esc(track["level_label"])}</span>
      <h3>{esc(track["title"])}</h3>
      <p>{esc(track["card_desc"])}</p>
      <div class="meta">{esc(track["meta"])}</div>
      <div class="cta">{esc(nav["view_route"])} →</div>
    </a>"""

        scenario_lookup = {item["id"]: item for item in scenarios["items"]}
        scenario_cards = ""
        for scenario_id in home.get("scenario_teaser_ids", []):
            item = scenario_lookup.get(scenario_id)
            if not item:
                continue
            scenario_cards += f"""<a class="scenario-preview-card" data-reveal data-persona="{item["id"]}" href="{local_href("scenarios", lang)}#{item["id"]}">
      <div class="scenario-preview-top"><span class="persona-chip">{item["icon"]} {esc(item["role"])}</span></div>
      <h3>{esc(item["hook"])}</h3>
      <span class="scenario-preview-cta">{esc(home["scenario_section_cta"])} →</span>
    </a>"""

        body = f"""<main>
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy" data-reveal>
      <span class="eyebrow">{esc(home["eyebrow"])}</span>
      <h1><span class="grad">{esc(home["h1_line1"])}</span><br>{esc(home["h1_line2"])}</h1>
      <p class="lede">{esc(home["lede"])}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="{local_href(home.get("cta_primary_page", "scenarios"), lang)}">{esc(home["cta_primary"])}</a>
        <a class="btn btn-ghost" href="{local_href(home.get("cta_secondary_page", "plans"), lang)}">{esc(home["cta_secondary"])}</a>
      </div>
      {quickref_teaser}
      <div class="hero-link-row"><a href="{local_href(home.get("cta_tertiary_page", "basics"), lang)}">{esc(home["cta_tertiary"])} →</a></div>
      <p class="hero-note">{esc(home["hero_note"])}</p>
    </div>
    <div class="hero-visual" data-reveal>
      <div class="hero-orb"></div>
      <div class="hero-visual-card">
        <div class="hero-visual-head"><strong>{esc(hero_visual["title"])}</strong><div class="hero-visual-badges">{badge_html}</div></div>
        <div class="hero-visual-code">{line_html}</div>
      </div>
    </div>
  </div>
</section>

<section class="impact-strip">
  <div class="container">
    <div class="impact-grid">{stat_cards}</div>
  </div>
</section>

<section class="start-free-section">
  <div class="container">
    <div class="section-head" data-reveal>
      <h2>{esc(home["start_free_title"])}</h2>
      <p>{esc(home["start_free_sub"])}</p>
    </div>
    <div class="start-grid">{start_cards}</div>
    <div class="start-inline-links" data-reveal><span>{esc(home["start_free_links_label"])}</span>{start_links}</div>
    {start_diagnostic}
  </div>
</section>

<section class="personas">
  <div class="container">
    <div class="section-head" data-reveal>
      <h2>{esc(home["personas_title"])}</h2>
      <p>{esc(home["personas_sub"])}</p>
    </div>
    <div class="persona-grid">{persona_cards}</div>
  </div>
</section>

<section class="journey">
  <div class="container">
    <div class="section-head" data-reveal>
      <h2>{esc(home["journey_title"])}</h2>
      <p>{esc(home["journey_sub"])}</p>
    </div>
    <div class="journey-grid">{journey_cards}</div>
  </div>
</section>

<section class="scenario-preview">
  <div class="container">
    <div class="section-head" data-reveal>
      <h2>{esc(home["scenario_section_title"])}</h2>
      <p>{esc(home["scenario_section_sub"])}</p>
    </div>
    <div class="scenario-preview-grid">{scenario_cards}</div>
    <div class="scenario-extra" data-reveal>
      <p class="scenario-extra-label">{esc(home["scenario_examples_label"])}</p>
      <ul class="scenario-mini-list">{extra_examples}</ul>
      <a class="btn btn-primary" href="{local_href("scenarios", lang)}">{esc(home["scenario_section_cta"])} →</a>
    </div>
  </div>
</section>

<section class="courses">
  <div class="container">
    <div class="section-head" data-reveal>
      <h2>{esc(home["courses_title"])}</h2>
      <p>{esc(home["courses_sub"])}</p>
    </div>
    <div class="course-grid">{course_cards}</div>
  </div>
</section>

<div class="teaser" data-reveal>
  <div>
    <h3>{esc(home["teaser_title"])}</h3>
    <p>{esc(home["teaser_desc"])}</p>
  </div>
  <a class="btn btn-primary" href="{local_href("best_practices", lang)}">{esc(home["teaser_cta"])}</a>
</div>
</main>"""
        return page_shell(lang, "home", meta["title_suffix"], meta["description"], body)

    def render_course(lang, track_key):
        track = content[lang]["tracks"][track_key]
        nav = content[lang]["nav"]
        ui = PAGE_UI[lang]
        print_label = {"fr": "Imprimer cette page", "en": "Print this page", "nl": "Druk deze pagina af"}[lang]
        toc_items = "".join(
            f'<li><a href="#lesson-{i+1}">{esc(lesson["title"])}</a></li>'
            for i, lesson in enumerate(track["lessons"])
        )
        lesson_blocks = ""
        total = len(track["lessons"])
        for i, lesson in enumerate(track["lessons"]):
            paras = "".join(f"<p>{esc(paragraph)}</p>" for paragraph in lesson["paragraphs"])
            extra = lesson.get("extra_html") or ""
            tip = f'<div class="tip-box"><strong>Tip</strong><span>{esc(lesson["tip"])}</span></div>' if lesson.get("tip") else ""
            exercise = (
                f'<div class="exercise-box"><strong>{esc(nav.get("exercise_label", "Exercise"))}</strong><span>{esc(lesson["exercise"])}</span></div>'
                if lesson.get("exercise")
                else ""
            )
            prev_link = f'<a href="#lesson-{i}">← {esc(track["lessons"][i-1]["title"])}</a>' if i > 0 else "<span></span>"
            next_link = f'<a href="#lesson-{i+2}">{esc(track["lessons"][i+1]["title"])} →</a>' if i < total - 1 else "<span></span>"
            progress_toggle = f"""<label class="lesson-progress-toggle">
      <input type="checkbox" data-progress-checkbox data-lang="{lang}" data-track="{track_key}" data-lesson="{i+1}" data-key="vibecoding_progress_{lang}_{track_key}_{i+1}">
      <span data-label-off="{esc(ui["progress_button"])}" data-label-on="{esc(ui["progress_done"])}">{esc(ui["progress_button"])}</span>
    </label>"""
            lesson_blocks += f"""<article class="lesson" data-reveal id="lesson-{i+1}">
      <div class="lesson-kicker">{esc(lesson["kicker"])}</div>
      <h2>{esc(lesson["title"])}</h2>
      {paras}
      {extra}
      {tip}
      {exercise}
      <div class="lesson-progress-row">{progress_toggle}</div>
      <div class="lesson-nav">{prev_link}{next_link}</div>
    </article>"""

        body = f"""<main>
<section class="course-hero">
  <div class="container" data-reveal>
    {render_wayfinding(lang, track_key)}
    {render_course_progress(lang, track_key)}
    <span class="level-tag {track["tag_class"]}">{esc(track["level_label"])}</span>
    <h1>{esc(track["title"])}</h1>
    <p>{esc(track["subtitle"])}</p>
    <button type="button" class="btn btn-ghost print-action" onclick="window.print()">{esc(print_label)}</button>
  </div>
</section>
<div class="container course-layout">
  <aside class="toc" data-reveal>
    <h4>{esc(nav["all_lessons"])}</h4>
    <ol>{toc_items}</ol>
  </aside>
  <div class="lessons">{lesson_blocks}{render_quiz(lang, track_key)}</div>
</div>
</main>"""
        return page_shell(lang, track_key, track["title"], track["subtitle"], body)

    def render_best_practices(lang):
        bp = content[lang]["best_practices"]
        items_html = "".join(
            f"""<div class="bp-item" data-reveal><span class="idx">{i+1:02d}</span><h3>{esc(title)}</h3><p>{esc(desc)}</p></div>"""
            for i, (title, desc) in enumerate(bp["items"])
        )
        body = f"""<main>
<section class="bp-page">
  <div class="container">
    <div class="section-head" data-reveal>
      <h1>{esc(bp["title"])}</h1>
      <p>{esc(bp["sub"])}</p>
    </div>
    <div class="bp-grid">{items_html}</div>
  </div>
</section>
</main>"""
        return page_shell(lang, "best_practices", bp["title"], bp["sub"], body)

    def render_about(lang):
        about = content[lang]["about"]
        paras = "".join(f"<p>{esc(paragraph)}</p>" for paragraph in about["paragraphs"])
        sections_html = ""
        for heading, paragraphs in about["sections"]:
            sections_html += f'<section class="about-section" data-reveal><h2>{esc(heading)}</h2>' + "".join(
                f"<p>{esc(paragraph)}</p>" for paragraph in paragraphs
            ) + "</section>"
        body = f"""<main>
<section class="about-page">
  <div class="container about-body">
    <div data-reveal>
      <h1>{esc(about["title"])}</h1>
      {paras}
    </div>
    {sections_html}
  </div>
</section>
</main>"""
        return page_shell(lang, "about", about["title"], about["paragraphs"][0][:150], body)

    def render_explorer(lang):
        exp = content[lang]["explorer"]
        feature_label = {key: label for key, label, _desc in exp["features"]}
        persona_lookup = {key: (icon, label) for key, icon, label in exp["personas"]}

        persona_pills = '<button type="button" class="filter-pill active" data-persona="all">' + esc(exp["all_label"]) + "</button>"
        for key, icon, label in exp["personas"]:
            persona_pills += f'<button type="button" class="filter-pill" data-persona="{key}">{icon} {esc(label)}</button>'

        feature_pills = "".join(
            f'<button type="button" class="filter-pill" data-feature="{key}">{esc(label)}</button>'
            for key, label, _desc in exp["features"]
        )
        legend_items = "".join(
            f"""<div class="feature-legend-item" data-reveal>{feature_html(label, lang)}<p>{esc(desc)}</p></div>"""
            for _key, label, desc in exp["features"]
        )

        cards_html = ""
        for index, usecase in enumerate(exp["usecases"], start=1):
            p_icon, p_label = persona_lookup[usecase["persona"]]
            feature_chips = "".join(feature_html(feature_label[feature], lang) for feature in usecase["features"])
            steps_html = "".join(f"<li>{esc(step)}</li>" for step in usecase["steps"])
            search_blob = esc(
                " ".join(
                    [
                        usecase["title"],
                        usecase["situation"],
                        usecase["result"],
                        usecase["further"],
                        " ".join(usecase["steps"]),
                        " ".join(feature_label[feature] for feature in usecase["features"]),
                    ]
                ).lower()
            )
            cards_html += f"""<div class="usecase-card" data-reveal id="usecase-{index}" data-persona="{usecase["persona"]}" data-features="{' '.join(usecase["features"])}" data-search="{search_blob}">
      <div class="usecase-top">
        <span class="persona-chip">{p_icon} {esc(p_label)}</span>
        {feature_chips}
      </div>
      <h3>{esc(usecase["title"])}</h3>
      <p class="usecase-situation">{esc(usecase["situation"])}</p>
      <button type="button" class="usecase-toggle" data-label-show="{esc(exp['show_steps'])}" data-label-hide="{esc(exp['hide_steps'])}"><span class="toggle-label">{esc(exp['show_steps'])}</span><span class="chevron" aria-hidden="true">▾</span></button>
      <div class="usecase-details" hidden>
        <ol class="usecase-steps">{steps_html}</ol>
        <p class="usecase-result"><strong>{esc(exp['result_label'])}</strong> {esc(usecase['result'])}</p>
        <p class="usecase-further"><strong>{esc(exp['further_label'])}</strong> {esc(usecase['further'])}</p>
      </div>
    </div>"""

        body = f"""<main>
<section class="explorer-page">
  <div class="container">
    <div class="section-head" data-reveal>
      {render_wayfinding(lang, "explorer")}
      <h1>{esc(exp["title"])}</h1>
      <p>{esc(exp["sub"])}</p>
    </div>
    {render_fact_banner(lang)}
    <div class="feature-legend">{legend_items}</div>
    <div class="explorer-toolbar" data-reveal>
      <div class="explorer-search"><input type="text" placeholder="{esc(exp['search_placeholder'])}"></div>
      <div class="filter-row"><span class="filter-label">{esc(exp['persona_filter_label'])}</span>{persona_pills}</div>
      <div class="filter-row"><span class="filter-label">{esc(exp['feature_filter_label'])}</span>{feature_pills}</div>
    </div>
    <p class="explorer-count">{esc(exp['count_prefix'])} <strong>{len(exp['usecases'])}</strong> {esc(exp['count_suffix'])}</p>
    <div class="usecase-grid">{cards_html}</div>
    <div class="explorer-empty">{esc(exp['empty_message'])}</div>
  </div>
</section>
</main>"""
        return page_shell(lang, "explorer", exp["title"], exp["sub"], body)

    def render_toolkit(lang):
        toolkit = content[lang]["toolkit"]
        ui = PAGE_UI[lang]
        prompt_ui = PROMPT_CONFIGURATOR_UI[lang]
        maturity_note = MATURITY_CONTEXT_NOTES[lang]["toolkit"]
        groups_html = ""
        explorer_personas = content[lang]["explorer"]["personas"]
        for index, (icon, role, prompts) in enumerate(toolkit["groups"]):
            prompt_items = "".join(f'<div class="prompt-item"><span class="quote-mark">&gt;</span><span>{esc(prompt)}</span></div>' for prompt in prompts)
            persona_key = explorer_personas[index][0] if index < len(explorer_personas) else ""
            groups_html += f"""<div class="toolkit-group" data-reveal data-persona="{persona_key}">
      <div class="toolkit-group-head">
        <div class="persona-icon">{icon}</div>
        <h2>{esc(role)}</h2>
      </div>
      <div class="prompt-list">{prompt_items}</div>
    </div>"""
        persona_data = []
        home_personas = content[lang]["home"]["personas"]
        for index, (key, icon, label) in enumerate(content[lang]["explorer"]["personas"]):
            pitch = home_personas[index][2] if index < len(home_personas) else label
            persona_patch = prompt_ui["personas"][key]
            persona_data.append({
                "key": key,
                "icon": icon,
                "label": label,
                "pitch": pitch,
                "presets": persona_patch["presets"],
                "surface": persona_patch["surface"],
                "instruction": persona_patch["instruction"],
            })
        prompt_script = json_html({
            "empty": prompt_ui["empty"],
            "copy": prompt_ui["copy"],
            "copied": prompt_ui["copied"],
            "fallback": prompt_ui["fallback"],
            "constraintsLabel": prompt_ui["constraints_label"],
            "presetDefault": prompt_ui["preset_default"],
            "personas": persona_data,
        })
        persona_options = "".join(
            f'<option value="{item["key"]}">{item["icon"]} {esc(item["label"])}</option>'
            for item in persona_data
        )
        constraint_items = "".join(
            f"""<label class="form-check"><input type="checkbox" data-prompt-constraint value="{esc(text)}"><span>{esc(text)}</span></label>"""
            for text in prompt_ui["constraints"]
        )
        configurator_html = f"""<section class="toolkit-configurator" id="prompt-configurator">
      <div class="section-head left" data-reveal>
        <h2>{esc(prompt_ui["title"])}</h2>
        <p>{esc(prompt_ui["sub"])}</p>
      </div>
      <div class="tool-form-layout">
        <div class="tool-form-card" data-reveal>
          <div class="tool-form-grid" data-prompt-configurator>
            <label class="tool-field">
              <span>{esc(prompt_ui["role_label"])}</span>
              <select data-prompt-role>
                <option value="">{esc(prompt_ui["default_option"])}</option>
                {persona_options}
              </select>
            </label>
            <label class="tool-field">
              <span>{esc(prompt_ui["preset_label"])}</span>
              <select data-prompt-preset disabled>
                <option value="">{esc(prompt_ui["preset_default"])}</option>
              </select>
            </label>
            <label class="tool-field tool-field-full">
              <span>{esc(prompt_ui["goal_label"])}</span>
              <input type="text" data-prompt-goal placeholder="{esc(prompt_ui["goal_placeholder"])}">
            </label>
            <fieldset class="tool-field tool-field-full">
              <legend>{esc(prompt_ui["constraints_label"])}</legend>
              <div class="tool-check-grid">{constraint_items}</div>
            </fieldset>
          </div>
        </div>
        <div class="generated-tool-card" data-reveal>
          <p class="tool-output-label">{esc(prompt_ui["output_label"])}</p>
          <div class="chat-mockup">
            <div class="chat-head">Copilot Chat</div>
            <div class="chat-body">
              <pre class="generated-prompt-output" data-prompt-output>{esc(prompt_ui["empty"])}</pre>
            </div>
          </div>
          <div class="generated-tool-actions">
            <button type="button" class="btn btn-primary" data-prompt-copy>{esc(prompt_ui["copy"])}</button>
          </div>
        </div>
      </div>
      <script type="application/json" data-prompt-config>{prompt_script}</script>
    </section>"""
        spotlight_cards = "".join(
            f"""<a class="cta-card" data-reveal href="{local_href(card["page"], lang)}"><span class="plan-icon">{card["icon"]}</span><h3>{esc(card["title"])}</h3><p>{esc(card["desc"])}</p><span>{esc(card["cta"])} →</span></a>"""
            for card in toolkit.get("spotlight_cards", [])
        )
        spotlight_cards += f"""<a class="cta-card" data-reveal href="{local_href("workshop", lang)}"><span class="plan-icon">🧑‍🏫</span><h3>{esc(ui["workshop_title"])}</h3><p>{esc(ui["workshop_sub"])}</p><span>{esc(ui["workshop_print"])} →</span></a>"""
        body = f"""<main>
<section class="toolkit-page">
  <div class="container">
    <div class="section-head" data-reveal>
      {render_wayfinding(lang, "toolkit")}
      <h1>{esc(toolkit["title"])}</h1>
      <p>{esc(toolkit["sub"])}</p>
      <p class="page-hero-note">{esc(maturity_note["before"])}<a href="{local_href("maturity", lang)}">{esc(maturity_note["link"])}</a>{esc(maturity_note["after"])}</p>
    </div>
    {groups_html}
    {configurator_html}
    <section class="toolkit-spotlight">
      <div class="section-head" data-reveal>
        <h2>{esc(toolkit.get("spotlight_title", "Two smart next steps"))}</h2>
        <p>{esc(toolkit.get("spotlight_sub", ""))}</p>
      </div>
      <div class="resource-grid">{spotlight_cards}</div>
    </section>
  </div>
</section>
</main>"""
        return page_shell(lang, "toolkit", toolkit["title"], toolkit["sub"], body)

    def render_first_commit(lang):
        guide = content[lang]["first_commit"]
        install_label = {"en": "Install options", "fr": "Options d’installation", "nl": "Installatieopties"}[lang]
        maturity_note = MATURITY_CONTEXT_NOTES[lang]["first_commit"]
        account_sources = [[DOC_URLS["create_account"]], [DOC_URLS["create_account"]], [DOC_URLS["create_account"]]]
        account_cards = "".join(
            f"""<article class="plan-card quick-fact-card" data-reveal><div class="plan-card-top"><span class="plan-icon">{card["icon"]}</span><div><h3>{esc(card["title"])} {source_links_html(lang, account_sources[index])}</h3><p>{esc(card["desc"])}</p></div></div></article>"""
            for index, card in enumerate(guide["account_cards"])
        )
        repo_steps = "".join(
            f"""<article class="number-step-card" data-reveal><span class="step-number">{esc(step["num"])}</span><h3>{esc(step["title"])} {source_link(lang, DOC_URLS["repo_quickstart"])}</h3><p>{esc(step["desc"])}</p></article>"""
            for step in guide["repo_steps"]
        )
        mockup_lines = "".join(f'<li>{esc(line)}</li>' for line in guide["repo_mockup_lines"])
        path_cards = ""
        path_sources = [
            [DOC_URLS["agents_overview"], DOC_URLS["pages_quickstart"]],
            [DOC_URLS["cli_getting_started"], DOC_URLS["cli_install"], DOC_URLS["cli_about"]],
            [DOC_URLS["desktop"]],
        ]
        for path_index, path in enumerate(guide["paths"]):
            steps = "".join(f"<li>{esc(step)}</li>" for step in path["steps"])
            commands = ""
            if path.get("commands"):
                command_lines = "".join(f"<li><code>{esc(line)}</code></li>" for line in path["commands"])
                commands = f"""<div class="command-stack">
      <strong>{esc(install_label)}</strong>
      <ul class="command-list">{command_lines}</ul>
    </div>"""
            note = ""
            if path.get("note"):
                note = f"<p class=\"path-note\">{esc(path['note'])}"
                if path.get("note_page"):
                    note += f" <a href=\"{local_href(path['note_page'], lang)}\">{esc(path.get('note_cta', content[lang]['nav'].get(path['note_page'], 'Learn more')))}</a>"
                note += "</p>"
            path_cards += f"""<article class="plan-card commit-path-card" data-reveal>
      <div class="plan-card-top">
        <span class="plan-icon">{path["icon"]}</span>
        <div>
          <p class="path-label">{esc(path["label"])}</p>
          <h3>{esc(path["title"])} {source_links_html(lang, path_sources[path_index])}</h3>
        </div>
      </div>
      <p class="path-audience">{esc(path["audience"])}</p>
      <p>{esc(path["summary"])}</p>
      {commands}
      <ol class="path-steps">{steps}</ol>
      {note}
      <p class="path-success">{esc(path["success"])}</p>
    </article>"""
        after_cards = ""
        for card in guide["after_cards"]:
            href = local_href(card["page"], lang)
            if card.get("anchor"):
                href += f'#{card["anchor"]}'
            after_cards += f"""<a class="cta-card" data-reveal href="{href}"><span class="plan-icon">{card["icon"]}</span><h3>{esc(card["title"])}</h3><p>{esc(card["desc"])}</p><span>{esc(card["cta"])} →</span></a>"""
        body = f"""<main>
<section class="page-hero">
  <div class="container">
    <div class="section-head left" data-reveal>
      {render_wayfinding(lang, "first_commit")}
      <h1>{esc(guide["title"])}</h1>
      <p>{esc(guide["sub"])}</p>
      <p class="page-hero-note">{esc(guide["hero_note"])}</p>
      <p class="page-hero-note">{esc(maturity_note["before"])}<a href="{local_href("maturity", lang)}">{esc(maturity_note["link"])}</a>{esc(maturity_note["after"])}</p>
    </div>
  </div>
</section>

<section class="first-commit-page">
  <div class="container">
    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(guide["account_title"])} {source_link(lang, DOC_URLS["create_account"])}</h2>
        <p>{esc(guide["account_sub"])}</p>
      </div>
      <div class="resource-grid">{account_cards}</div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(guide["repo_title"])} {source_link(lang, DOC_URLS["repo_quickstart"])}</h2>
        <p>{esc(guide["repo_sub"])}</p>
      </div>
      <div class="two-column-grid">
        <div class="number-step-grid">{repo_steps}</div>
        <div class="chat-mockup repo-mockup" data-reveal>
          <div class="chat-head">{esc(guide["repo_mockup_title"])}</div>
          <div class="chat-body">
            <ol class="mockup-list">{mockup_lines}</ol>
          </div>
        </div>
      </div>
      <div class="tip-box" data-reveal><strong>{esc(guide["warmup_title"])}</strong><span>{esc(guide["warmup_desc"])}</span></div>
      {glossary_shortcuts_html(lang, ["repository", "commit", "branch", "pull-request", "issue"])}
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(guide["paths_title"])}</h2>
        <p>{esc(guide["paths_sub"])}</p>
      </div>
      <div class="resource-grid">{path_cards}</div>
      {glossary_shortcuts_html(lang, ["copilot-cli", "agent-mode", "github-pages"])}
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(guide["after_title"])}</h2>
        <p>{esc(guide["after_sub"])}</p>
      </div>
      <div class="resource-grid">{after_cards}</div>
    </section>
  </div>
</section>
</main>"""
        return page_shell(lang, "first_commit", guide["title"], guide["sub"], body)

    def render_build_vs_buy(lang):
        page = content[lang]["build_vs_buy"]
        change_cards = "".join(
            f"""<article class="plan-card comparison-card" data-reveal><div class="plan-card-top"><span class="plan-icon">{card["icon"]}</span><div><h3>{esc(card["title"])}</h3><p>{esc(card["desc"])}</p></div></div></article>"""
            for card in page["change_cards"]
        )
        comparison_rows = "".join(
            f"""<tr>
      <td><strong>{esc(row["need"])}</strong></td>
      <td>{esc(row["buy"])}</td>
      <td>{esc(row["build"])}</td>
      <td>{esc(row["note"])}</td>
    </tr>"""
            for row in page["comparison_rows"]
        )
        calc = page["calculator"]
        ladder_steps = "".join(
            f"""<article class="plan-card ladder-step" data-reveal><span class="step-number">{esc(str(index + 1).zfill(2))}</span><h3>{esc(step["stage"])}</h3><p><strong>{esc(step["scope"])}</strong></p><p>{esc(step["features"])}</p><p class="ladder-outcome">{esc(step["outcome"])}</p></article>"""
            for index, step in enumerate(page["ladder_steps"])
        )
        amnesty_cards = "".join(
            f"""<article class="plan-card shadow-card" data-reveal><h3>{esc(card["now"])}</h3><p class="shadow-arrow">→ {esc(card["future"])}</p><p>{esc(card["why"])}</p></article>"""
            for card in page["amnesty_cards"]
        )
        gallery_points = "".join(f"<li>{esc(point)}</li>" for point in page["gallery_points"])
        gallery_template = "\n".join(page["gallery_template"])
        buy_cards = "".join(
            f"""<article class="plan-card truth-card" data-reveal><div class="plan-card-top"><span class="plan-icon">{card["icon"]}</span><div><h3>{esc(card["title"])}</h3><p>{esc(card["desc"])}</p></div></div></article>"""
            for card in page["buy_cards"]
        )
        evidence_sources = [
            [DOC_URLS["research_2022"], DOC_URLS["research_2022"], DOC_URLS["research_2022"]],
            [DOC_URLS["impact_dashboard"], DOC_URLS["impact_dashboard"], DOC_URLS["impact_dashboard"]],
        ]
        evidence_cards = ""
        for card_index, card in enumerate(page["evidence_cards"]):
            bullets = "".join(
                f"<li>{esc(item)} {source_link(lang, evidence_sources[card_index][min(item_index, len(evidence_sources[card_index]) - 1)])}</li>"
                for item_index, item in enumerate(card["bullets"])
            )
            evidence_cards += f"""<article class="plan-card evidence-card" data-reveal><h3>{esc(card["title"])}</h3><ul class="mini-list">{bullets}</ul></article>"""
        next_cards = "".join(
            f"""<a class="cta-card" data-reveal href="{local_href(card["page"], lang)}"><span class="plan-icon">{card["icon"]}</span><h3>{esc(card["title"])}</h3><p>{esc(card["desc"])}</p><span>{esc(card["cta"])} →</span></a>"""
            for card in page["next_cards"]
        )
        body = f"""<main>
<section class="page-hero">
  <div class="container">
    <div class="section-head left" data-reveal>
      {render_wayfinding(lang, "build_vs_buy")}
      <h1>{esc(page["title"])}</h1>
      <p>{esc(page["sub"])}</p>
      <p class="page-hero-note">{esc(page["hero_note"])}</p>
    </div>
  </div>
</section>

<section class="build-buy-page">
  <div class="container">
    {render_fact_banner(lang)}
    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["changes_title"])}</h2>
        <p>{esc(page["changes_sub"])}</p>
      </div>
      <div class="resource-grid">{change_cards}</div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["comparison_title"])}</h2>
        <p>{esc(page["comparison_sub"])}</p>
      </div>
      <div class="plans-table-wrap" data-reveal>
        <table class="plans-table comparison-table">
          <thead><tr>{"".join(f"<th>{esc(col)}</th>" for col in page["comparison_columns"])}</tr></thead>
          <tbody>{comparison_rows}</tbody>
        </table>
      </div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(calc["title"])}</h2>
        <p>{esc(calc["sub"])}</p>
      </div>
      <div class="calculator-card" data-reveal data-buildbuy-calculator data-business-price="19" data-business-credits="1900" data-enterprise-price="39" data-enterprise-credits="3900" data-default-plan="business" data-gap-positive="{esc(calc['gap_positive'])}" data-gap-negative="{esc(calc['gap_negative'])}">
        <div class="calculator-layout">
          <div class="calculator-controls">
            <h3>{esc(calc["inputs_title"])}</h3>
            <label class="calc-field"><span>{esc(calc["tools_label"])}</span><input data-input="tools" type="number" min="0" step="1" value="6"></label>
            <label class="calc-field"><span>{esc(calc["average_label"])}</span><input data-input="average" type="number" min="0" step="100" value="2800"></label>
            <label class="calc-field"><span>{esc(calc["builders_label"])}</span><input data-input="builders" type="number" min="1" step="1" value="15"></label>
            <div class="plan-switch">
              <span class="calc-label">{esc(calc["plan_label"])}</span>
              <div class="plan-switch-buttons">
                <button type="button" class="plan-option is-active" data-plan="business" aria-pressed="true">{esc(calc["business_label"])}</button>
                <button type="button" class="plan-option" data-plan="enterprise" aria-pressed="false">{esc(calc["enterprise_label"])}</button>
              </div>
            </div>
            <p class="calc-footnote">{esc(calc["footnote"])}</p>
            <p class="calc-footnote">{esc(calc["plan_note"])} <a href="{local_href("plans", lang)}">{esc(content[lang]["nav"]["plans"])}</a>.</p>
          </div>
          <div class="calculator-results">
            <h3>{esc(calc["results_title"])}</h3>
            <div class="resource-grid calculator-results-grid">
              <article class="plan-card calc-result-card"><h4>{esc(calc["spend_label"])}</h4><strong data-output="tool-spend">$0</strong></article>
              <article class="plan-card calc-result-card"><h4>{esc(calc["copilot_label"])}</h4><strong data-output="copilot-spend">$0</strong></article>
              <article class="plan-card calc-result-card"><h4>{esc(calc["credits_label"])}</h4><strong data-output="credits">0</strong></article>
              <article class="plan-card calc-result-card"><h4>{esc(calc["gap_label"])}</h4><strong data-output="gap">$0</strong><p data-output="gap-note"></p></article>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["ladder_title"])}</h2>
        <p>{esc(page["ladder_sub"])}</p>
      </div>
      <div class="resource-grid">{ladder_steps}</div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["amnesty_title"])}</h2>
        <p>{esc(page["amnesty_sub"])}</p>
      </div>
      <div class="resource-grid">{amnesty_cards}</div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["gallery_title"])}</h2>
        <p>{esc(page["gallery_sub"])}</p>
      </div>
      <div class="two-column-grid gallery-grid">
        <article class="plan-card" data-reveal>
          <ul class="mini-list">{gallery_points}</ul>
        </article>
        <div class="chat-mockup gallery-template" data-reveal>
          <div class="chat-head">{esc(page["gallery_template_title"])}</div>
          <div class="chat-body"><pre>{esc(gallery_template)}</pre></div>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["buy_title"])}</h2>
        <p>{esc(page["buy_sub"])}</p>
      </div>
      <div class="resource-grid">{buy_cards}</div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["evidence_title"])}</h2>
      </div>
      <div class="resource-grid">{evidence_cards}</div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(page["next_title"])}</h2>
      </div>
      <div class="resource-grid">{next_cards}</div>
    </section>
  </div>
</section>
</main>"""
        return page_shell(lang, "build_vs_buy", page["title"], page["sub"], body)

    def render_plans(lang):
        plans = content[lang]["plans"]
        stat_cards = "".join(render_counter_card(item) for item in plans["stat_cards"])

        def plan_row_sources(plan_name):
            plan_name = plan_name.lower()
            if "student" in plan_name:
                return [DOC_URLS["students"], DOC_URLS["plans"]]
            if plan_name == "copilot pro":
                return [DOC_URLS["teachers"], DOC_URLS["plans"]]
            if "pro+" in plan_name:
                return [DOC_URLS["plans"], DOC_URLS["billing"]]
            if "max" in plan_name:
                return [DOC_URLS["plans"], DOC_URLS["billing"]]
            return [DOC_URLS["plans"], DOC_URLS["features"]]

        def plan_fact_sources(plan_name, fact):
            fact_lower = fact.lower()
            if "cli" in fact_lower:
                return [DOC_URLS["cli_about"]]
            if "application github copilot" in fact_lower or "copilot app" in fact_lower:
                return [DOC_URLS["copilot_app"]]
            if "ai credits" in fact_lower:
                return [DOC_URLS["billing"]]
            if "third-party coding agents" in fact_lower:
                return [DOC_URLS["students"]]
            if "teacher" in fact_lower or "enseign" in fact_lower or "docent" in fact_lower or "open-source" in fact_lower:
                return [DOC_URLS["teachers"]]
            return [plan_row_sources(plan_name)[0]]

        row_html = ""
        for row in plans["individual_rows"]:
            badge = f'<span class="table-badge">{esc(row["badge"])}</span>' if row.get("badge") else ""
            row_sources = plan_row_sources(row["plan"])
            facts = "".join(
                f"<li>{esc(fact)} {source_links_html(lang, plan_fact_sources(row['plan'], fact))}</li>"
                for fact in row["facts"]
            )
            row_html += f"""<tr>
      <td><strong>{esc(row["plan"])}</strong>{badge}<br>{source_links_html(lang, row_sources)}</td>
      <td>{esc(row["price"])}</td>
      <td>{esc(row["audience"])}</td>
      <td>{esc(row["free_note"])} {source_links_html(lang, row_sources[:1])}</td>
      <td><ul class="mini-list">{facts}</ul></td>
    </tr>"""

        org_cards = ""
        for card in plans["org_cards"]:
            bullets = "".join(f"<li>{esc(bullet)}</li>" for bullet in card["bullets"])
            org_cards += f"""<article class="plan-card" data-reveal>
      <div class="plan-card-top"><span class="plan-icon">{card["icon"]}</span><div><h3>{esc(card["title"])}</h3><p class="plan-price">{esc(card["price"])}</p></div></div>
      <p class="plan-credits">{esc(card["credits"])}</p>
      <p class="plan-note">{esc(card["note"])}</p>
      <ul class="mini-list">{bullets}</ul>
    </article>"""

        total = plans["pool_total"]
        used_sum = 0
        users_html = ""
        for item in plans["pool_users"]:
            used_sum += item["used"]
            width = max(6, round(item["used"] / total * 100))
            users_html += f"""<div class="credit-user" data-reveal>
      <div class="credit-user-head"><strong>{esc(item["name"])}</strong><span>{item["used"]} credits</span></div>
      <div class="credit-bar-track"><div class="credit-bar" data-bar-target="{width}"></div></div>
      <p>{esc(item["note"])}</p>
    </div>"""

        pool_bullets = "".join(f"<li>{esc(bullet)}</li>" for bullet in plans["pool_bullets"])
        campus_cards = "".join(
            f"""<div class="campus-card" data-reveal><span class="plan-icon">{card["icon"]}</span><h3>{esc(card["title"])} {source_link(lang, DOC_URLS["campus_program"])}</h3><p>{esc(card["desc"])}</p></div>"""
            for card in plans["campus_cards"]
        )
        cta_cards = "".join(
            f"""<a class="cta-card" data-reveal href="{card["href"]}"><h3>{esc(card["title"])}</h3><p>{esc(card["desc"])}</p><span>{esc(card["label"])} →</span></a>"""
            for card in plans["cta_cards"]
        )
        cta_cards += f"""<a class="cta-card" data-reveal href="{local_href("maturity", lang)}"><span class="plan-icon">🧭</span><h3>{esc(content[lang]["maturity"]["title"])}</h3><p>{esc(content[lang]["maturity"]["sub"])}</p><span>{esc(MATURITY_CONTEXT_NOTES[lang]["plans_cta"])} →</span></a>"""

        body = f"""<main>
<section class="plans-page">
  <div class="container">
    <div class="section-head" data-reveal>
      {render_wayfinding(lang, "plans")}
      <h1>{esc(plans["title"])}</h1>
      <p>{esc(plans["sub"])}</p>
    </div>
    {render_fact_banner(lang)}
    <div class="impact-grid">{stat_cards}</div>

    <section class="plans-block">
      <div class="section-head left" data-reveal>
        <h2>{esc(plans["individual_title"])}</h2>
        <p>{esc(plans["individual_intro"])}</p>
      </div>
      <div class="plans-table-wrap" data-reveal>
        <table class="plans-table">
          <thead><tr>{"".join(f"<th>{esc(col)}</th>" for col in plans["individual_columns"])}</tr></thead>
          <tbody>{row_html}</tbody>
        </table>
      </div>
    </section>

    <section class="plans-block">
      <div class="section-head left" data-reveal>
        <h2>{esc(plans["org_title"])}</h2>
        <p>{esc(plans["org_intro"])}</p>
      </div>
      <div class="plan-card-grid">{org_cards}</div>
      <div class="ocre-note" data-reveal>
        <h3>{esc(plans["ocre_title"])}</h3>
        <p>{esc(plans["ocre_text"])}</p>
        <a class="btn btn-primary" href="{mailto_href(plans["ocre_mailto_subject"], plans["ocre_mailto_body"])}">{esc(plans["ocre_cta_label"])} →</a>
      </div>
    </section>

    <section class="plans-block credit-pool" data-reveal>
      <div class="section-head left">
        <h2>{esc(plans["pool_title"])}</h2>
        <p>{esc(plans["pool_intro"])}</p>
      </div>
      <div class="credit-pool-summary">
        <div>
          <span class="eyebrow">{esc(plans["pool_total_label"])}</span>
          <div class="credit-total"><strong data-counter="{total}">0</strong><span>{esc(plans["pool_total_suffix"])}</span></div>
          <p class="credit-total-note"><strong data-counter="{used_sum}">0</strong> / {total} credits used in this illustrative month.</p>
        </div>
      </div>
      <div class="credit-user-grid">{users_html}</div>
      <ul class="mini-list">{pool_bullets}</ul>
    </section>

    <section class="plans-block">
      <div class="section-head left" data-reveal>
        <h2>{esc(plans["campus_title"])}</h2>
        <p>{esc(plans["campus_intro"])}</p>
      </div>
      <div class="campus-grid">{campus_cards}</div>
    </section>

    <section class="plans-block">
      <div class="section-head left" data-reveal>
        <h2>{esc(plans["cta_title"])}</h2>
      </div>
      <div class="cta-grid">{cta_cards}</div>
    </section>
  </div>
</section>
</main>"""
        return page_shell(lang, "plans", plans["title"], plans["sub"], body)

    def render_scenarios(lang):
        scenarios = content[lang]["scenarios"]
        onepager_ui = SCENARIO_ONEPAGER_UI[lang]
        maturity_note = MATURITY_CONTEXT_NOTES[lang]["scenarios"]
        jump_html = "".join(f'<a class="filter-pill" data-persona="{item["id"]}" href="#{item["id"]}">{item["icon"]} {esc(item["role"])}</a>' for item in scenarios["items"])
        cards = ""
        for item in scenarios["items"]:
            features = "".join(feature_html(feature, lang) for feature in item["features"])
            steps = "".join(f"<li>{esc(step)}</li>" for step in item["steps"])
            deliverables = "".join(f"<li>{esc(deliverable)}</li>" for deliverable in item["deliverables"])
            cards += f"""<article class="scenario-card" data-reveal data-persona="{item["id"]}" id="{item["id"]}">
      <div class="scenario-card-head">
        <span class="persona-chip">{item["icon"]} {esc(item["role"])}</span>
        <div class="scenario-features">{features}</div>
      </div>
      <h2>{esc(item["hook"])}</h2>
      <p class="scenario-problem">{esc(item["problem"])}</p>
      <div class="scenario-grid-inner">
        <div>
          <h3>{esc(scenarios["steps_label"])}</h3>
          <ol class="scenario-steps">{steps}</ol>
        </div>
        <div class="chat-mockup scenario-chat">
          <div class="chat-head">Copilot</div>
          <div class="chat-body">
            <div class="chat-bubble-user">{esc(item["prompt"])}</div>
            <div class="chat-bubble-ai">{esc(item["output"])}</div>
          </div>
        </div>
      </div>
      <div class="scenario-outcomes">
        <div>
          <h3>{esc(scenarios["deliverables_label"])}</h3>
          <ul class="mini-list">{deliverables}</ul>
        </div>
        <div>
          <h3>{esc(scenarios["impact_label"])}</h3>
          <p>{esc(item["impact"])}</p>
        </div>
      </div>
    </article>"""
        persona_lookup = {}
        home_personas = content[lang]["home"]["personas"]
        for index, (key, icon, label) in enumerate(content[lang]["explorer"]["personas"]):
            persona_lookup[key] = {
                "key": key,
                "icon": icon,
                "label": label,
                "pitch": home_personas[index][2] if index < len(home_personas) else label,
            }
        onepager_data = {
            "personas": list(persona_lookup.values()),
            "usecases": [],
            "ui": onepager_ui,
        }
        for usecase in content[lang]["explorer"]["usecases"]:
            start_page = "plans" if usecase["persona"] in {"it", "leadership", "research"} or any(
                feature in {"mcp", "cloudagent", "review"} for feature in usecase["features"]
            ) else "first_commit"
            onepager_data["usecases"].append({
                "persona": usecase["persona"],
                "title": usecase["title"],
                "situation": usecase["situation"],
                "steps": usecase["steps"],
                "result": usecase["result"],
                "further": usecase["further"],
                "startHref": local_href(start_page, lang),
                "startLabel": current_page_label(lang, start_page),
            })
        onepager_html = f"""<section class="scenario-onepager" id="onepager-generator">
      <div class="section-head left" data-reveal>
        <h2>{esc(onepager_ui["title"])}</h2>
        <p>{esc(onepager_ui["sub"])}</p>
      </div>
      <div class="tool-form-layout">
        <div class="tool-form-card" data-reveal data-onepager-generator>
          <div class="tool-form-grid">
            <label class="tool-field">
              <span>{esc(onepager_ui["persona_label"])}</span>
              <select data-onepager-persona>
                <option value="">{esc(onepager_ui["default_option"])}</option>
                {"".join(f'<option value="{item["key"]}">{item["icon"]} {esc(item["label"])}</option>' for item in onepager_data["personas"])}
              </select>
            </label>
            <label class="tool-field">
              <span>{esc(onepager_ui["usecase_label"])}</span>
              <select data-onepager-usecase disabled>
                <option value="">{esc(onepager_ui["default_option"])}</option>
              </select>
            </label>
          </div>
          <script type="application/json" data-onepager-config>{json_html(onepager_data)}</script>
        </div>
        <article class="onepager-brief" data-reveal data-onepager-brief hidden>
          <div class="onepager-brief-head">
            <div>
              <p class="tool-output-label">{esc(onepager_ui["brief_title"])}</p>
              <h3 data-onepager-title>—</h3>
            </div>
            <button type="button" class="btn btn-ghost print-action" data-onepager-print>{esc(onepager_ui["print"])}</button>
          </div>
          <div class="onepager-brief-grid">
            <section>
              <h4>{esc(onepager_ui["pitch_label"])}</h4>
              <p data-onepager-pitch>—</p>
            </section>
            <section>
              <h4>{esc(onepager_ui["context_label"])}</h4>
              <p data-onepager-situation>—</p>
            </section>
          </div>
          <section>
            <h4>{esc(onepager_ui["steps_label"])}</h4>
            <ol class="mini-list" data-onepager-steps></ol>
          </section>
          <div class="onepager-brief-grid">
            <section>
              <h4>{esc(onepager_ui["outcome_label"])}</h4>
              <p data-onepager-result>—</p>
            </section>
            <section>
              <h4>{esc(onepager_ui["further_label"])}</h4>
              <p data-onepager-further>—</p>
            </section>
          </div>
          <section class="onepager-start">
            <h4>{esc(onepager_ui["start_label"])}</h4>
            <a href="{local_href("first_commit", lang)}" data-onepager-start-link>{esc(current_page_label(lang, "first_commit"))} →</a>
          </section>
        </article>
      </div>
    </section>"""

        body = f"""<main>
<section class="scenario-page">
  <div class="container">
    <div class="section-head" data-reveal>
      {render_wayfinding(lang, "scenarios")}
      <h1>{esc(scenarios["title"])}</h1>
      <p>{esc(scenarios["sub"])}</p>
      <p class="page-hero-note">{esc(maturity_note["before"])}<a href="{local_href("maturity", lang)}">{esc(maturity_note["link"])}</a>{esc(maturity_note["after"])}</p>
    </div>
    {render_fact_banner(lang)}
    <div class="teaser scenario-bridge" data-reveal>
      <div>
        <h3>{esc(scenarios.get("starter_title", ""))}</h3>
        <p>{esc(scenarios.get("starter_desc", ""))}</p>
      </div>
      <a class="btn btn-primary" href="{local_href("first_commit", lang)}">{esc(scenarios.get("starter_cta", content[lang]["nav"].get("first_commit", "First commit")))} →</a>
    </div>
    {glossary_shortcuts_html(lang, ["agent-mode", "copilot-spaces", "mcp-servers"])}
    <div class="scenario-jump" data-reveal>
      <span class="filter-label">{esc(scenarios["jump_label"])}</span>
      {jump_html}
    </div>
    <div class="scenario-stack">{cards}</div>
    {onepager_html}
  </div>
</section>
</main>"""
        return page_shell(lang, "scenarios", scenarios["title"], scenarios["sub"], body)

    def render_glossary(lang):
        ui = PAGE_UI[lang]
        print_label = {"fr": "Imprimer cette page", "en": "Print this page", "nl": "Druk deze pagina af"}[lang]
        groups_html = ""
        for group in GLOSSARY_GROUPS[lang]:
            items_html = ""
            for item in group["items"]:
                items_html += f"""<article class="glossary-item" id="{item["id"]}" data-reveal>
      <div class="glossary-item-head">
        <h3>{esc(item["term"])}</h3>
        {source_link(lang, item["source"])}
      </div>
      <p>{esc(item["desc"])}</p>
    </article>"""
            groups_html += f"""<section class="glossary-group">
      <div class="section-head left" data-reveal>
        <h2>{esc(group["title"])}</h2>
      </div>
      <div class="glossary-grid">{items_html}</div>
    </section>"""
        body = f"""<main>
  <section class="page-hero">
    <div class="container">
    <div class="section-head left" data-reveal>
      {render_wayfinding(lang, "glossary")}
      <h1>{esc(ui["glossary_title"])}</h1>
      <p>{esc(ui["glossary_sub"])}</p>
      <button type="button" class="btn btn-ghost print-action" onclick="window.print()">{esc(print_label)}</button>
    </div>
    </div>
  </section>
  <section class="glossary-page">
    <div class="container">
    {groups_html}
    </div>
  </section>
  </main>"""
        return page_shell(lang, "glossary", ui["glossary_title"], ui["glossary_sub"], body)

    def render_workshop(lang):
        ui = PAGE_UI[lang]
        agenda_cards = ""
        for index, (timing, title, desc) in enumerate(ui["workshop_sections"], start=1):
            agenda_cards += f"""<article class="number-step-card workshop-agenda-card" data-reveal>
      <span class="step-number">{index:02d}</span>
      <p class="agenda-time">{esc(timing)}</p>
      <h3>{esc(title)}</h3>
      <p>{esc(desc)}</p>
    </article>"""
        prep_items = "".join(f"<li>{esc(item)}</li>" for item in ui["workshop_prep"])
        resource_cards = "".join(
            [
                f"""<a class="cta-card" data-reveal href="{local_href("first_commit", lang)}"><span class="plan-icon">🧪</span><h3>{esc(content[lang]["first_commit"]["title"])}</h3><p>{esc(content[lang]["first_commit"]["sub"])}</p><span>{esc(content[lang]["nav"]["first_commit"])} →</span></a>""",
                f"""<a class="cta-card" data-reveal href="{local_href("scenarios", lang)}"><span class="plan-icon">🎭</span><h3>{esc(content[lang]["scenarios"]["title"])}</h3><p>{esc(content[lang]["scenarios"]["sub"])}</p><span>{esc(content[lang]["nav"]["scenarios"])} →</span></a>""",
                f"""<a class="cta-card" data-reveal href="{local_href("explorer", lang)}"><span class="plan-icon">🧭</span><h3>{esc(content[lang]["explorer"]["title"])}</h3><p>{esc(content[lang]["explorer"]["sub"])}</p><span>{esc(content[lang]["nav"]["explorer"])} →</span></a>""",
                f"""<a class="cta-card" data-reveal href="{local_href("toolkit", lang)}"><span class="plan-icon">🧰</span><h3>{esc(content[lang]["toolkit"]["title"])}</h3><p>{esc(content[lang]["toolkit"]["sub"])}</p><span>{esc(content[lang]["nav"]["toolkit"])} →</span></a>""",
            ]
        )
        body = f"""<main>
  <section class="page-hero">
    <div class="container">
    <div class="section-head left" data-reveal>
      {render_wayfinding(lang, "workshop")}
      <h1>{esc(ui["workshop_title"])}</h1>
      <p>{esc(ui["workshop_sub"])}</p>
      <p class="page-hero-note">{esc(ui["workshop_intro"])}</p>
      <button type="button" class="btn btn-primary print-action" onclick="window.print()">{esc(ui["workshop_print"])}</button>
    </div>
    </div>
  </section>
  <section class="workshop-page">
    <div class="container">
    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(ui["workshop_agenda_title"])}</h2>
      </div>
      <div class="resource-grid workshop-agenda-grid">{agenda_cards}</div>
    </section>

    <section class="content-section">
      <div class="two-column-grid workshop-two-column">
        <article class="plan-card" data-reveal>
          <h2>{esc(ui["workshop_prep_title"])}</h2>
          <ul class="mini-list">{prep_items}</ul>
        </article>
        <article class="plan-card workshop-qr-card" data-reveal>
          <h2>{esc(ui["workshop_qr_label"])}</h2>
          <div class="qr-target" data-qr-widget data-qr-url="{esc(ui["workshop_qr_url"])}" aria-label="{esc(ui["workshop_qr_label"])}"></div>
          <p><code>{esc(ui["workshop_qr_url"])}</code></p>
          <p>{esc(ui["workshop_qr_note"])}</p>
        </article>
      </div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(ui["workshop_demo_title"])}</h2>
      </div>
      <div class="demo-frame-wrap" data-reveal>
        <div class="demo-frame-bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="url">quick-poll-{lang}.html</span></div>
        <iframe title="Quick Poll demo" src="../assets/demo/quick-poll-{lang}.html" loading="lazy"></iframe>
      </div>
    </section>

    <section class="content-section">
      <div class="section-head left" data-reveal>
        <h2>{esc(ui["workshop_resources_title"])}</h2>
      </div>
      <div class="resource-grid">{resource_cards}</div>
    </section>
    </div>
  </section>
  </main>"""
        return page_shell(lang, "workshop", ui["workshop_title"], ui["workshop_sub"], body)

    def render_certificate(lang):
        ui = PAGE_UI[lang]
        track_counts = "|".join(f"{track_key}:{len(content[lang]['tracks'][track_key]['lessons'])}" for track_key in track_order)
        track_items = "".join(
            f"""<li><span>{esc(content[lang]["tracks"][track_key]["level_label"])}</span><strong>{esc(content[lang]["tracks"][track_key]["title"])}</strong></li>"""
            for track_key in track_order
        )
        body = f"""<main>
  <section class="page-hero">
    <div class="container">
    <div class="section-head left" data-reveal>
      {render_wayfinding(lang, "certificate")}
      <h1>{esc(ui["certificate_title"])}</h1>
      <p>{esc(ui["certificate_sub"])}</p>
    </div>
    </div>
  </section>
  <section class="certificate-page">
    <div class="container">
    <div class="certificate-shell" data-certificate-page data-lang="{lang}" data-tracks="{','.join(track_order)}" data-track-counts="{track_counts}" data-ready-text="{esc(ui['certificate_ready'])}" data-locked-text="{esc(ui['certificate_locked'])}">
      <p class="certificate-status" data-certificate-status>{esc(ui["certificate_locked"])}</p>
      <label class="certificate-name-field">
        <span>{esc(ui["certificate_name"])}</span>
        <input type="text" data-certificate-name-input data-storage-key="vibecoding_certificate_name_{lang}" placeholder="{esc(ui["certificate_name_placeholder"])}">
      </label>
      <article class="certificate-card" data-certificate-card>
        <p class="certificate-site-name">{esc(content[lang]["meta"]["site_name"])}</p>
        <h2>{esc(ui["certificate_title"])}</h2>
        <p class="certificate-name-value" data-certificate-name-display>{esc(ui["certificate_name_placeholder"])}</p>
        <div class="certificate-meta-grid">
          <div>
            <span>{esc(ui["certificate_tracks"])}</span>
            <ul>{track_items}</ul>
          </div>
          <div>
            <span>{esc(ui["certificate_date"])}</span>
            <strong data-certificate-date>—</strong>
          </div>
        </div>
      </article>
      <div class="certificate-actions">
        <a class="btn btn-ghost" href="{local_href("home", lang)}">{esc(content[lang]["nav"]["home"])}</a>
        <button type="button" class="btn btn-primary print-action" data-certificate-print disabled>{esc(ui["certificate_print"])}</button>
      </div>
      <p class="certificate-footnote">{esc(ui["certificate_footer"])}</p>
    </div>
    </div>
  </section>
  </main>"""
        return page_shell(lang, "certificate", ui["certificate_title"], ui["certificate_sub"], body)

    def render_quick_reference(lang):
        page = content[lang]["quick_reference"]
        ui = PAGE_UI[lang]
        home = content[lang]["home"]
        stats_html = "".join(render_counter_card(item) for item in home.get("impact_stats", []))
        situation_cards = ""
        for item in page["situations"]:
            href = item.get("href") or local_href(item["page"], lang)
            situation_cards += f"""<a class="cta-card" data-reveal href="{href}"><span class="plan-icon">{item["icon"]}</span><h3>{esc(item["title"])}</h3><p>{esc(item["desc"])}</p><span>{esc(item["cta"])} →</span></a>"""
        body = f"""<main>
  <section class="page-hero">
    <div class="container">
      <div class="section-head left" data-reveal>
        {render_wayfinding(lang, "quick_reference")}
        <h1>{esc(page["title"])}</h1>
        <p>{esc(page["sub"])}</p>
        <p class="page-hero-note">{esc(page["intro"])}</p>
      </div>
    </div>
  </section>
  <section class="plans-page">
    <div class="container">
      <section class="content-section">
        <div class="section-head left" data-reveal>
          <h2>{esc(page["situations_title"])}</h2>
          <p>{esc(page["situations_sub"])}</p>
        </div>
        <div class="resource-grid">{situation_cards}</div>
      </section>
      <div class="tip-box" data-reveal><strong>{esc(page["search_label"])}</strong><span>{esc(page["search_before"])} <a href="{local_href("glossary", lang)}">{esc(ui["glossary_title"])}</a> {esc(page["search_after"])}</span></div>
      <section class="content-section">
        <div class="section-head left" data-reveal>
          <h2>{esc(page["overview_title"])}</h2>
          <p>{esc(page["overview_sub"])}</p>
        </div>
        <div class="impact-grid">{stats_html}</div>
      </section>
      <div class="tip-box" data-reveal><strong>{esc(page["sitemap_label"])}</strong><span>{esc(page["sitemap_before"])} <a href="{local_href("sitemap", lang)}">{esc(ui["sitemap_title"])}</a>{esc(page["sitemap_after"])}</span></div>
    </div>
  </section>
  </main>"""
        return page_shell(lang, "quick_reference", page["title"], page["sub"], body)

    def render_maturity(lang):
        page = content[lang]["maturity"]
        question_html = ""
        for index, question in enumerate(page["questions"], start=1):
            options_html = "".join(
                f"""<label class="maturity-option"><input type="radio" name="{question["id"]}" value="{option["value"]}"><span>{esc(option["label"])}</span></label>"""
                for option in question["options"]
            )
            question_html += f"""<article class="maturity-question" data-reveal>
      <div class="quiz-question-head">
        <span>{index}</span>
        <h3>{esc(question["question"])}</h3>
      </div>
      <div class="maturity-options">{options_html}</div>
    </article>"""
        body = f"""<main>
  <section class="page-hero">
    <div class="container">
      <div class="section-head left" data-reveal>
        {render_wayfinding(lang, "maturity")}
        <h1>{esc(page["title"])}</h1>
        <p>{esc(page["sub"])}</p>
      </div>
    </div>
  </section>
  <section class="maturity-page">
    <div class="container">
      <div class="fact-banner" data-reveal>
        <strong>{esc(page["banner_label"])}</strong>
        <span>{esc(page["banner_text"])}</span>
      </div>
      <div class="tool-form-card" data-reveal data-maturity-diagnostic>
        <p class="page-hero-note">{esc(page["intro"])}</p>
        <div class="maturity-question-stack">{question_html}</div>
        <div class="generated-tool-actions">
          <button type="button" class="btn btn-primary" data-maturity-submit>{esc(page["submit"])}</button>
          <button type="button" class="btn btn-ghost" data-maturity-reset>{esc(page["reset"])}</button>
        </div>
        <article class="maturity-result" data-maturity-result hidden>
          <p class="tool-output-label">{esc(page["result_title"])}</p>
          <h2 data-maturity-result-title>—</h2>
          <p data-maturity-result-body>—</p>
          <ul class="mini-list" data-maturity-result-bullets></ul>
          <a class="btn btn-primary" href="{local_href("first_commit", lang)}" data-maturity-result-link>{esc(content[lang]["first_commit"]["title"])} →</a>
        </article>
        <script type="application/json" data-maturity-config>{json_html(page)}</script>
      </div>
    </div>
  </section>
  </main>"""
        return page_shell(lang, "maturity", page["title"], page["sub"], body)

    def render_changelog(lang):
        page = content[lang]["changelog"]
        entries_html = ""
        for entry in page["entries"]:
            links_html = "".join(
                f'<a class="source-link" href="{local_href(page_key, lang)}">{esc(label)}</a>'
                for page_key, label in entry["links"]
            )
            entries_html += f"""<article class="changelog-entry" data-reveal>
      <div class="changelog-entry-head">
        <p class="changelog-date">{esc(entry["date"])}</p>
        <h2>{esc(entry["title"])}</h2>
      </div>
      <p>{esc(entry["summary"])}</p>
      <div class="source-links">{links_html}</div>
    </article>"""
        body = f"""<main>
  <section class="page-hero">
    <div class="container">
      <div class="section-head left" data-reveal>
        {render_wayfinding(lang, "changelog")}
        <h1>{esc(page["title"])}</h1>
        <p>{esc(page["sub"])}</p>
      </div>
    </div>
  </section>
  <section class="changelog-page">
    <div class="container">
      <div class="fact-banner" data-reveal>
        <strong>{esc(page["banner_label"])}</strong>
        <span>{esc(page["banner_text"])}</span>
      </div>
      <div class="changelog-stack">{entries_html}</div>
    </div>
  </section>
  </main>"""
        return page_shell(lang, "changelog", page["title"], page["sub"], body)

    def render_sitemap(lang):
        ui = PAGE_UI[lang]
        nav = content[lang]["nav"]
        main_links = [
            ("home", nav["home"]),
            ("explorer", nav["explorer"]),
            ("scenarios", nav["scenarios"]),
            ("first_commit", nav["first_commit"]),
            ("build_vs_buy", nav["build_vs_buy"]),
            ("plans", nav["plans"]),
            ("toolkit", nav["toolkit"]),
            ("best_practices", nav["best_practices"]),
            ("about", nav["about"]),
        ]
        main_html = "".join(f'<li><a href="{local_href(key, lang)}">{esc(label)}</a></li>' for key, label in main_links)
        track_html = ""
        for track_key in track_order:
            track = content[lang]["tracks"][track_key]
            lessons = "".join(
                f'<li><a href="{local_href(track_key, lang)}#lesson-{index + 1}">{esc(lesson["title"])}</a></li>'
                for index, lesson in enumerate(track["lessons"])
            )
            track_html += f"""<li class="sitemap-track-item"><a href="{local_href(track_key, lang)}"><strong>{esc(track["title"])}</strong></a><ul>{lessons}</ul></li>"""
        resource_links = [
            ("quick_reference", content[lang]["quick_reference"]["title"]),
            ("maturity", content[lang]["maturity"]["title"]),
            ("workshop", ui["workshop_title"]),
            ("glossary", ui["glossary_title"]),
            ("certificate", ui["certificate_title"]),
            ("sitemap", ui["sitemap_title"]),
            ("changelog", content[lang]["changelog"]["title"]),
        ]
        resource_html = "".join(f'<li><a href="{local_href(key, lang)}">{esc(label)}</a></li>' for key, label in resource_links)
        body = f"""<main>
  <section class="page-hero">
    <div class="container">
    <div class="section-head left" data-reveal>
      {render_wayfinding(lang, "sitemap")}
      <h1>{esc(ui["sitemap_title"])}</h1>
      <p>{esc(ui["sitemap_sub"])}</p>
    </div>
    </div>
  </section>
  <section class="sitemap-page">
    <div class="container">
    <div class="sitemap-group" data-reveal>
      <h2>{esc(ui["sitemap_groups"][0][0])}</h2>
      <ul>{main_html}</ul>
    </div>
    <div class="sitemap-group" data-reveal>
      <h2>{esc(ui["sitemap_groups"][1][0])}</h2>
      <ul>{track_html}</ul>
    </div>
    <div class="sitemap-group" data-reveal>
      <h2>{esc(ui["sitemap_groups"][2][0])}</h2>
      <ul>{resource_html}</ul>
    </div>
    </div>
  </section>
  </main>"""
        return page_shell(lang, "sitemap", ui["sitemap_title"], ui["sitemap_sub"], body)

    def build_search_index(lang):
        entries = []
        ui = PAGE_UI[lang]

        def add_entry(title, description, href, category, keywords=""):
            entries.append({
                "title": title,
                "description": description,
                "href": href,
                "category": category,
                "keywords": keywords,
            })

        add_entry(content[lang]["meta"]["site_name"], content[lang]["meta"]["description"], local_href("home", lang), "page", content[lang]["meta"]["title_suffix"])
        add_entry(content[lang]["explorer"]["title"], content[lang]["explorer"]["sub"], local_href("explorer", lang), "page")
        add_entry(content[lang]["scenarios"]["title"], content[lang]["scenarios"]["sub"], local_href("scenarios", lang), "page")
        add_entry(content[lang]["plans"]["title"], content[lang]["plans"]["sub"], local_href("plans", lang), "page")
        add_entry(content[lang]["first_commit"]["title"], content[lang]["first_commit"]["sub"], local_href("first_commit", lang), "page")
        add_entry(content[lang]["build_vs_buy"]["title"], content[lang]["build_vs_buy"]["sub"], local_href("build_vs_buy", lang), "page")
        add_entry(content[lang]["toolkit"]["title"], content[lang]["toolkit"]["sub"], local_href("toolkit", lang), "page")
        add_entry(content[lang]["best_practices"]["title"], content[lang]["best_practices"]["sub"], local_href("best_practices", lang), "page")
        add_entry(content[lang]["about"]["title"], content[lang]["about"]["paragraphs"][0], local_href("about", lang), "page")
        add_entry(content[lang]["quick_reference"]["title"], content[lang]["quick_reference"]["sub"], local_href("quick_reference", lang), "page")
        add_entry(content[lang]["maturity"]["title"], content[lang]["maturity"]["sub"], local_href("maturity", lang), "page")
        add_entry(content[lang]["changelog"]["title"], content[lang]["changelog"]["sub"], local_href("changelog", lang), "page")
        add_entry(ui["workshop_title"], ui["workshop_sub"], local_href("workshop", lang), "page")
        add_entry(ui["glossary_title"], ui["glossary_sub"], local_href("glossary", lang), "page")
        add_entry(ui["sitemap_title"], ui["sitemap_sub"], local_href("sitemap", lang), "page")
        add_entry(ui["certificate_title"], ui["certificate_sub"], local_href("certificate", lang), "page")
        add_entry(PROMPT_CONFIGURATOR_UI[lang]["title"], PROMPT_CONFIGURATOR_UI[lang]["sub"], f'{local_href("toolkit", lang)}#prompt-configurator', "tool")
        add_entry(SCENARIO_ONEPAGER_UI[lang]["title"], SCENARIO_ONEPAGER_UI[lang]["sub"], f'{local_href("scenarios", lang)}#onepager-generator', "tool")

        for track_key in track_order:
            track = content[lang]["tracks"][track_key]
            add_entry(track["title"], track["subtitle"], local_href(track_key, lang), "track", track["level_label"])
            for index, lesson in enumerate(track["lessons"], start=1):
                add_entry(
                    lesson["title"],
                    lesson["kicker"],
                    f'{local_href(track_key, lang)}#lesson-{index}',
                    "lesson",
                    " ".join(lesson["paragraphs"][:2]) + " " + lesson.get("exercise", ""),
                )

        for index, usecase in enumerate(content[lang]["explorer"]["usecases"], start=1):
            add_entry(
                usecase["title"],
                usecase["situation"],
                f'{local_href("explorer", lang)}#usecase-{index}',
                "use case",
                " ".join(usecase["steps"]) + " " + usecase["result"] + " " + usecase["further"],
            )

        for item in content[lang]["scenarios"]["items"]:
            add_entry(
                item["hook"],
                item["problem"],
                f'{local_href("scenarios", lang)}#{item["id"]}',
                "scenario",
                item["role"] + " " + " ".join(item["features"] + item["deliverables"]),
            )

        for group in GLOSSARY_GROUPS[lang]:
            for item in group["items"]:
                add_entry(item["term"], item["desc"], f'{local_href("glossary", lang)}#{item["id"]}', "glossary", group["title"])

        return entries

    def all_generated_paths():
        paths = [""]
        page_keys = [
            "home",
            "explorer",
            "plans",
            "scenarios",
            "best_practices",
            "toolkit",
            "about",
            "first_commit",
            "build_vs_buy",
            "glossary",
            "workshop",
            "certificate",
            "quick_reference",
            "sitemap",
            "maturity",
            "changelog",
        ]
        for lang in langs:
            for page_key in page_keys:
                paths.append(f"{lang}/{page_filename(lang, page_key)}")
            for track_key in track_order:
                paths.append(f"{lang}/{page_filename(lang, track_key)}")
        return paths

    def build_xml_sitemap():
        comment = "Published at https://sebplace.github.io/vibe-coding-copilot/ via GitHub Pages."
        urls = "\n".join(
            f"  <url><loc>{PLACEHOLDER_SITE_BASE}{path}</loc></url>"
            for path in all_generated_paths()
        )
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- {comment} -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""

    def build_robots_txt():
        return "\n".join([
            "# Published at https://sebplace.github.io/vibe-coding-copilot/ via GitHub Pages.",
            "User-agent: *",
            "Allow: /",
            f"Sitemap: {PLACEHOLDER_SITE_BASE}sitemap.xml",
            "",
        ])

    def render_root_index():
        links = "".join(
            f'<a class="btn btn-primary" style="margin:6px;" href="{lang}/index.html">{lang_label[lang]}</a>'
            for lang in langs
        )
        brand = content["en"]["meta"]["site_name"]
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=en/index.html">
<title>{esc(brand)}</title>
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="stylesheet" href="assets/style.min.css">
</head>
<body>
<div class="container" style="padding:120px 0; text-align:center;">
  <h1>{esc(brand)}</h1>
  <p style="color:var(--text-muted); margin-bottom:28px;">Choose your language / Choisissez votre langue / Kies je taal</p>
  {links}
</div>
</body>
</html>"""

    for lang in langs:
        lang_dir = os.path.join(root, lang)
        os.makedirs(lang_dir, exist_ok=True)

        pages = {
            "index.html": render_home(lang),
            "cas-usage.html": render_explorer(lang),
            "plans.html": render_plans(lang),
            "scenarios.html": render_scenarios(lang),
            "best-practices.html": render_best_practices(lang),
            "toolkit.html": render_toolkit(lang),
            "about.html": render_about(lang),
            "first-commit.html": render_first_commit(lang),
            "build-vs-buy.html": render_build_vs_buy(lang),
            "glossary.html": render_glossary(lang),
            "workshop.html": render_workshop(lang),
            "certificate.html": render_certificate(lang),
            "quick-reference.html": render_quick_reference(lang),
            "sitemap.html": render_sitemap(lang),
            "maturity.html": render_maturity(lang),
            "changelog.html": render_changelog(lang),
        }
        for filename, html in pages.items():
            with open(os.path.join(lang_dir, filename), "w", encoding="utf-8") as handle:
                handle.write(html)

        for track_key in track_order:
            filename = content[lang]["tracks"][track_key]["slug"] + ".html"
            with open(os.path.join(lang_dir, filename), "w", encoding="utf-8") as handle:
                handle.write(render_course(lang, track_key))

        with open(os.path.join(root, "assets", f"search-index.{lang}.json"), "w", encoding="utf-8") as handle:
            json.dump(build_search_index(lang), handle, ensure_ascii=False, indent=2)

    with open(os.path.join(root, "assets", "favicon.svg"), "w", encoding="utf-8") as handle:
        handle.write(FAVICON_SVG)

    with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as handle:
        handle.write(render_root_index())

    with open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8") as handle:
        handle.write(build_xml_sitemap())

    with open(os.path.join(root, "robots.txt"), "w", encoding="utf-8") as handle:
        handle.write(build_robots_txt())

    style_css_path = os.path.join(root, "assets", "style.css")
    with open(style_css_path, "r", encoding="utf-8") as handle:
        style_source = handle.read()
    with open(os.path.join(root, "assets", "style.min.css"), "w", encoding="utf-8") as handle:
        handle.write(minify_css(style_source))

    print("Site generated for languages:", ", ".join(langs))
