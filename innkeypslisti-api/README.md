# Innkeypslisti API

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

| Adressa | Hvat er tað |
|---|---|
| http://localhost:8000/api/items | Innkeypslistin sum JSON |
| http://localhost:8000/docs | Royn API'ið beinleiðis |

Listin verður goymdur í `../sql/innkeypslisti.db`. Tað er ein SQLite database, sum bara er ein fíla. Hon kann latast upp í DB Browser for SQLite.

Legg nakað afturat úr JavaScript:

```js
fetch('http://localhost:8000/api/items?item=Snickers', { method: 'POST' })
```
