"use client";
import React, { useState, useEffect } from 'react';

const DocentesList = () => {
  const [docentes, setDocentes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDocentes = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/docentes/');
        const data = await response.json();
        setDocentes(data.docentes);
        console.log(data.docentes);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchDocentes();
  }, []);

  return (
    <div>
      <h2>Listado de Docentes</h2>
      {loading ? (
        <p>Cargando...</p>
      ) : (
        <ul>
          {docentes.map((docente) => (
            <li key={docente.codigo}>
              <strong>{docente.nombre}</strong> - {docente.materia} - {docente.ciudad}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default DocentesList;
