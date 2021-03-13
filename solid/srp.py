# SRP (SOC - Separation of Concern)

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


# j = Journal()
# j.add_entry("Witaj!")
# j.add_entry("Mój drugi wpis")
# print(j)


class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str(journal))


j = Journal()
j.add_entry("Witaj!")
j.add_entry("Mój drugi wpis")
print(f"Zawartość dziennika \n{j}")

filename = "journal.txt"
PersistanceManager.save_to_file(j, filename)
