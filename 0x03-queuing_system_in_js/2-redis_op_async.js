import redis from 'redis';
import util from 'util';

const client = redis.createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const asyncGet = util.promisify(client.get).bind(client);
async function displaySchoolValue (schoolName) {
  const val = await asyncGet(schoolName);
  console.log(val);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
