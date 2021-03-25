"""
extensions
"""
import json


class Extensions:
    def __init__(self):
        self.events_cog = "events"
        self.main_cog = "main"
        self.source_cog = "source"
        self.load_extensions()

    def load_extensions(self):
        self.load_events_cog()
        self.load_main_cog()
        self.load_source_cog()

    def load_events_cog(self):
        with open("data/extensions.json") as file:
            data = json.load(file)
            self.events_cog = data[self.events_cog]

    def load_main_cog(self):
        with open("data/extensions.json") as file:
            data = json.load(file)
            self.main_cog = data[self.main_cog]

    def load_source_cog(self):
        with open("data/extensions.json") as file:
            data = json.load(file)
            self.source_cog = data[self.source_cog]

    def get_events_cog(self):
        return self.events_cog

    def get_main_cog(self):
        return self.main_cog

    def get_source_cog(self):
        return self.source_cog

    def get_all_extensions(self):
        return [self.get_events_cog(), self.get_main_cog(), self.get_source_cog()]
