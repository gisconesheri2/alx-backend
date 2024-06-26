import redis from 'redis';
import kue from 'kue';
import express from 'express';
import { promisify } from 'util';

const client = redis.createClient();
const queue = kue.createQueue();
const app = express();
let reservationEnabled = true;
client.on('connect', () => {
  client.set('available_seats', 50);
  console.log('redis server connected');
});

const asyncGet = promisify(client.get).bind(client);

async function reserveSeat (number) {
  return promisify(client.SET).bind(client)('available_seats', number);
}

async function getCurrentAvailableSeats () {
  const seats = await asyncGet('available_seats');
  return seats;
}

app.get('/available_seats', (_, res) => {
  getCurrentAvailableSeats().then((seats) => {
    res.send(JSON.stringify({ numberOfAvailableSeats: seats }));
  });
});

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
    res.send(JSON.stringify({
      status: 'Reservation are blocked'
    }));
  } else {
    const job = queue.create('reserve_seat', { num: 1 }).save((err) => {
      if (err) {
        res.send(JSON.stringify({
          status: 'Reservation failed'
        }));
      } else {
        res.send(JSON.stringify({
          status: 'Reservation in process'
        }));
      }
    });
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
  }
});

app.get('/process', (_, res) => {
  queue.process('reserve_seat', (_, done) => {
    getCurrentAvailableSeats().then(num => {
      if (num <= 0) {
        reservationEnabled = false;
        done(new Error('Not enough seats available'));
      } else {
        reserveSeat(num - 1).then(() => done());
      }
    });
  });
  res.send(JSON.stringify({
    status: 'Queue processing'
  }));
});

app.listen(1245, () => {
  console.log('express server started');
});
