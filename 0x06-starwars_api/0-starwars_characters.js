#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Star Wars API URL for the specified Movie ID
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the film data
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Invalid Movie ID or API issue');
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    // Fetch and display each character in the same order as the API
    characterUrls.forEach((url) => {
      request(url, (error, response, body) => {
        if (error) {
          console.error('Error fetching character data:', error);
          return;
        }

        try {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } catch (parseError) {
          console.error('Error parsing character data:', parseError);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing film data:', parseError);
  }
});
