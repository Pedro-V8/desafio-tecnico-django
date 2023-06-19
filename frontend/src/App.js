import logo from './logo.svg';
import './App.css';

import axios from 'axios';
import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);
  const [formulario, setFormulario] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/formulario/1/');
      setData(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const handleFieldChange = (event, campoId) => {
    const valor = event.target.value;
    setFormulario((prevFormulario) => ({
      ...prevFormulario,
      [campoId]: { id_formulario: data.id, id_campo: campoId, valor },
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    

    let arr = []

    for (let key in formulario) {
        arr.push(formulario[key])
    }

    try {
        const response = await axios.post('http://localhost:8000/registro/', arr);
        console.log(response.data);
        // Faça algo com a resposta, se necessário

        alert("Registrado com Sucesso!")
      } catch (error) {
        console.log(error);
        // Trate o erro, se necessário
      }
  };

  return (
    <form onSubmit={handleSubmit}>
      {data &&
        data.campos.map((item) => (
          <div key={item.id}>
            <label htmlFor={item.nome_campo}>{item.nome_campo}:</label>
            <input
              type="text"
              id={item.nome_campo}
              value={formulario[item.id]?.valor || ''}
              onChange={(event) => handleFieldChange(event, item.id)}
            />
          </div>
        ))}
      <button type="submit">Enviar</button>
    </form>
  );
}

export default App;
