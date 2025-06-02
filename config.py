class Config:
    def __init__(self):
        self.variables = {
            "YouTube Download Path": "./downloads/youtube",
            "Spotify Download Path": "./downloads/spotify",
            "Last.fm API Key": "",
            "Last.fm API Secret": "",
            "Last.fm Username": "",
            "Last.fm Password Hash": "",
            "Twitch Token": "",
            "Twitch Channel": "",
        }

    def ask_for_variables(self):
        print("Please provide the following details:")
        for key in self.variables:
            value = input(f"{key} (default: {self.variables[key]}): ").strip()
            if value:
                self.variables[key] = value

    def remove_variable(self, key):
        if key in self.variables:
            confirmation = input(f"Are you sure you want to remove {key}? (yes/no): ").strip().lower()
            if confirmation == "yes":
                del self.variables[key]
                print(f"{key} has been removed.")
            else:
                print(f"{key} was not removed.")
        else:
            print(f"{key} does not exist.")

    def get_variable(self, key):
        return self.variables.get(key, None)
