import React, { useState, useEffect } from 'react';
import { getHeroes, createHero, deleteHero } from '../api';

const HeroList = () => {
  const [heroes, setHeroes] = useState([]);
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [secretName, setSecretName] = useState('');

  useEffect(() => {
    fetchHeroes();
  }, []);

  const fetchHeroes = async () => {
    const data = await getHeroes();
    setHeroes(data);
  };

  const handleCreateHero = async () => {
    const newHero = { name, age: parseInt(age), secret_name: secretName };
    await createHero(newHero);
    fetchHeroes();
  };

  const handleDeleteHero = async (heroId) => {
    await deleteHero(heroId);
    fetchHeroes();
  };

  return (
    <div>
      <h1>Heroes</h1>
      <ul>
        {heroes.map((hero) => (
          <li key={hero.id}>
            {hero.name} ({hero.age}) - {hero.secret_name}
            <button onClick={() => handleDeleteHero(hero.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <h2>Create Hero</h2>
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="number"
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />
      <input
        type="text"
        placeholder="Secret Name"
        value={secretName}
        onChange={(e) => setSecretName(e.target.value)}
      />
      <button onClick={handleCreateHero}>Create</button>
    </div>
  );
};

export default HeroList;