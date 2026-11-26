from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

entries: list[dict[str, str]] = []


class Entry(BaseModel):
    name: str
    message: str


@app.post("/entries")
def add_entry(entry: Entry):
    entries.append({"name": entry.name, "message": entry.message})
    return {"ok": True}


@app.get("/entries")
def get_entries():
    return entries

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int):
    if entry_id < 0 or entry_id >= len(entries):
        raise HTTPException(status_code=404, detail="Entry not found")
    deleted = entries.pop(entry_id)
    return {"ok": True, "deleted": deleted}