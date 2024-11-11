#!/usr/bin/node

const request = require('request');

async function getUsers() {
    try {
        const argValue = process.argv[2];
        const intValue = parseInt(argValue, 10);

        if (isNaN(intValue)) {
            console.error('Please provide a valid integer as the argument');
            return;
        }
        
        request(`https://swapi-api.alx-tools.com/api/films/${intValue}/`, function (error, response, body) {
            const data = JSON.parse(body);
            const characters = data.characters;

            for (let i = 0; i < characters.length; i++) {
                const character = request(characters[i], function (error, response, body) {
                    const data = JSON.parse(body);
                    console.log(data.name);
                })
            }  
});
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}
getUsers();