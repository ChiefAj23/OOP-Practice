from dataclasses import dataclass

@dataclass(frozen=True)
class Note:
    id: str
    text: str
    version: int

class NoteBook:
    def __init__(self):
        self._store = {}

    def add_note(self, note_id, text):
        if note_id in self._store:
            raise ValueError("Note exists. Use update_note.")
        first = Note(note_id, text, 1)
        self._store[note_id] = [first]
        return first

    def update_note(self, note_id, new_text):
        if note_id not in self._store:
            raise ValueError("Note not found. Use add_note first.")
        history = self._store[note_id]
        new_ver = history[-1].version + 1
        new_note = Note(note_id, new_text, new_ver)
        history.append(new_note)
        return new_note

    def get_current(self, note_id):
        if note_id not in self._store:
            return None
        return self._store[note_id][-1]

    def get_history(self, note_id):
        if note_id not in self._store:
            return []
        return list(self._store[note_id])

    def rollback(self, note_id, target_version):
        if note_id not in self._store:
            raise ValueError("Note not found.")
        for old in self._store[note_id]:
            if old.version == target_version:
                return self.update_note(note_id, old.text)
        raise ValueError("Version not found.")

if __name__ == "__main__":
    nb = NoteBook()
    print("Create-", nb.add_note("todo", "Buy milk"))
    print("Update-", nb.update_note("todo", "Buy milk and eggs"))
    print("Current-", nb.get_current("todo"))
    print("History-", nb.get_history("todo"))
    print("Rollback to v1 -> new version:", nb.rollback("todo", 1))
    print("Final history-", nb.get_history("todo"))
