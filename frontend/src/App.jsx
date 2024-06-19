import React, { useState } from 'react';
import './App.css'; // Importamos estilos CSS para centrar el contenido

function App() {
  const [items, setItems] = useState([
    { id: 1, name: 'Item 1', description: 'Descripción del Item 1', image: 'https://via.placeholder.com/150' },
    { id: 2, name: 'Item 2', description: 'Descripción del Item 2', image: 'https://via.placeholder.com/150' },
    { id: 3, name: 'Item 3', description: 'Descripción del Item 3', image: 'https://via.placeholder.com/150' },
  ]);

  return (
    <div className="App">
      <h1>Items</h1>
      <div className="item-container">
        {items.map(item => (
          <div key={item.id} className="item">
            <div>
              <h3>{item.name}</h3>
              <p>{item.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
