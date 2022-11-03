import { createClient } from 'redis';
const util = require('util');

const redis = require('redis');
const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));

client.HSET('HolbertonSchools', 'Portland', 50, redis.print);
client.HSET('HolbertonSchools', 'Seattle', 80, redis.print);
client.HSET('HolbertonSchools', 'New York', 20, redis.print);
client.HSET('HolbertonSchools', 'Bogota', 20, redis.print);
client.HSET('HolbertonSchools', 'Cali', 40, redis.print);
client.HSET('HolbertonSchools', 'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (error, data) => {
    console.log(data)
});