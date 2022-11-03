import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value){

    client.set(schoolName, value, redis.print)

}

function displaySchoolValue(schoolName){
    client.get(schoolName, (error, value) => {
        if (error) {
            console.log(error)
        }
        console.log(value)
    })

}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');