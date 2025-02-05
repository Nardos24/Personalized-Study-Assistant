import wikipediaapi

def get_wikipedia_summary(topic):
    # ✅ Specify a user-friendly User-Agent
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="PersonalizedStudyAssistant/1.0 (contact: your-email@example.com)",
        language="en"
    )
    page = wiki_wiki.page(topic)
    return page.summary if page.exists() else "No additional information available from Wikipedia."
