# wiki_bot.py
import pywikibot

class WikiBot:
    def __init__(self, site_code='en', family='wikipedia'):
        """
        Initialize the bot with a given wiki site.
        site_code: language code, e.g., 'en' for English
        family: wiki family, e.g., 'wikipedia'
        """
        self.site = pywikibot.Site(code=site_code, fam=family)
        print(f"Initialized bot for {self.site}")

    def login(self):
        """
        Log in the bot using credentials from user-config.py.
        Pywikibot automatically uses your saved username/password.
        """
        user = self.site.user()
        print(f"Bot logged in as: {user}")

    def edit_page(self, page_title, new_text, summary="Bot edit"):
        """
        Edit a page with the given text.
        page_title: str, the title of the wiki page
        new_text: str, the content to replace the page with
        summary: str, edit summary
        """
        page = pywikibot.Page(self.site, page_title)
        try:
            page.text = new_text
            page.save(summary=summary)
            print(f"Page '{page_title}' edited successfully.")
        except Exception as e:
            print(f"Error editing page '{page_title}': {e}")

















