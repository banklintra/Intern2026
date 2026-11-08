import { useEffect, useState } from 'react';

const API = 'http://localhost:8000/api/items';

export default function App() {
  const [items, setItems] = useState([]);
  const [text, setText] = useState('');

  // Heintar listan, tá ið síðan verður lisin inn.
  useEffect(() => {
    fetch(API)
      .then(r => r.json())
      .then(setItems);
  }, []);

  // Sendir eina nýggja vøru til API'ið. API'ið sendir allan listan aftur.
  function addItem(event) {
    event.preventDefault();
    fetch(API + '?item=' + encodeURIComponent(text), { method: 'POST' })
      .then(r => r.json())
      .then(setItems);
    setText('');
  }

  return (
    <main>
      <h1>Innkeypslisti</h1>

      <form onSubmit={addItem}>
        <input value={text} onChange={e => setText(e.target.value)} placeholder="Vøra" required />
        <button>Legg afturat</button>
      </form>

      <ul>
        {items.map((item, i) => <li key={i}>{item}</li>)}
      </ul>
    </main>
  );
}
