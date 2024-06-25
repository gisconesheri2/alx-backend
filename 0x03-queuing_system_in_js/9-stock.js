import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1010',
    price: 550,
    initialAvailableQuantity: 5
  }
];

function getItemyId (id) {
  listProducts.forEach(product => {
    if (product.id === id) {
      return product;
    }
  });
}

const app = express();
const client = redis.createClient();
const asyncHgetAll = promisify(client.hgetall).bind(client);

client.on('connect', () => console.log('redis client connected'));

listProducts.forEach(product => {
  product.currentQuantity = product.initialAvailableQuantity;
  const redisKey = product.itemId;
  for (const [key, val] of Object.entries(product)) {
    client.hset(redisKey, key, val);
  }
});

async function getCurrentReservedStockById (itemId) {
  const product = await asyncHgetAll(itemId);
  return product;
}
function reserveStockById (itemId, stock) {
  client.hset(itemId, 'currentQuantity', stock.currentQuantity - 1);
}

app.get('/list_products', (_, res) => {
  res.send(JSON.stringify(listProducts));
});

app.get('/list_products/:itemId', (req, res) => {
  const id = req.params.itemId;
  getCurrentReservedStockById(id).then(product => {
    if (product !== null) {
      res.send(JSON.stringify(product));
    } else {
      res.send(JSON.stringify({ status: 'Product not found' }));
    }
  });
});

app.get('/reserve_product/:itemId', (req, res) => {
  const id = req.params.itemId;
  getCurrentReservedStockById(id).then(product => {
    if (product === null) {
      res.send(JSON.stringify({ status: 'Product not found' }));
    } else {
      if (product.currentQuantity <= 0) {
        res.send(JSON.stringify(
          {
            status: 'Not enough stock available',
            itemId: id
          }));
      } else {
        reserveStockById(id, product);
        res.send(JSON.stringify(
          {
            status: 'Reservation confirmed',
            itemId: id
          }));
      }
    }
  }).catch(err => {
    console.log(err);
  }
  );
});
app.listen(1245, () => {
  console.log('server statred on port 1245');
});
