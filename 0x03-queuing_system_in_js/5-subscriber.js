import redis from 'redis';

const clientSub = redis.createClient();
clientSub.on('error', err => console.log('Redis client not connected to the server:', err));
clientSub.on('connect', () => console.log('Redis client connected to the server'));

clientSub.subscribe('holberton school channel');

clientSub.on('message', (chn, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') {
    clientSub.unsubscribe();
    clientSub.quit();
    // clientPub.quit();
  }
});
