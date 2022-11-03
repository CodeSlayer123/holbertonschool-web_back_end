import { createClient } from 'redis';
const util = require('util');

const redis = require('redis');
const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));


async function setNewSchool(schoolName, value){
    let set = util.promisify(client.set).bind(client);
    redis.print(null, await set(schoolName, value))

}

async function displaySchoolValue(schoolName){
    let get = util.promisify(client.get).bind(client);
    try{
        console.log(await get(schoolName))
    }
    catch(error){
        console.log(error)

    }

}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');