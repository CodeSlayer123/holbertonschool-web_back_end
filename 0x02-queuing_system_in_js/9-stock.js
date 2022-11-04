import { createClient } from 'redis';
const express = require('express');
const util = require('util');

const client = createClient();
const app = express();
const port = 1245;
const set = util.promisify(client.set).bind(client);
const get = util.promisify(client.get).bind(client);

const listProducts = [
    {
        itemId: 1,
        itemName: 'Suitcase 250',
        price: 50,
        initialAvailableQuantity: 4,
        currentQuantity: 4
    },
    {
        itemId: 2,
        itemName: 'Suitcase 450',
        price: 100,
        initialAvailableQuantity: 10,
        currentQuantity: 10
    },
    {
        itemId: 3,
        itemName: 'Suitcase 650',
        price: 350,
        initialAvailableQuantity: 2,
        currentQuantity: 2
    },
    {
        itemId: 4,
        itemName: 'Suitcase 1050',
        price: 550,
        initialAvailableQuantity: 5,
        currentQuantity: 5

    }
]
const allListProducts = Array.from(listProducts)


function getItemById(id){
    for (let product of listProducts){
        console.log(product)
        if (product.itemId === id) {
            return product
        }
    }
}


function reserveStockById(itemId, stock){
    set(`item.${itemId}`, stock);
}
async function getCurrentReservedStockById(itemId){
    await get(`item.${itemId}`)
}

app.get('/list_products', (req, res) => {
    let currentQuantity = []
    let i = 0;
    for (let product of allListProducts){
        console.log(product)
        currentQuantity.push(product['currentQuantity'])
        delete product['currentQuantity']

        console.log(product)
    }
    res.send(JSON.stringify(allListProducts));
    for (let product of allListProducts){
        product['currentQuantity'] = currentQuantity[i]
        i++;
    }

});
app.get('/list_products/:itemId', (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(parseInt(itemId))
    if (!item){
        res.status(404).send({"status":"Product not found"})
    } else {
        getCurrentReservedStockById(itemId).then(() => {
            res.send(item);
        })
    }

  });

app.get('/reserve_product/:itemId', (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(parseInt(itemId))
    if (!item){
        res.status(404).send({"status":"Product not found"})
    }
    else {
        if (item.currentQuantity < 1){
            res.send({"status":"Not enough stock available","itemId":itemId})
        }
        else {
            getCurrentReservedStockById(itemId).then(() => {
                item.currentQuantity--;
                reserveStockById(itemId, item.currentQuantity)
                res.send({"status":"Reservation confirmed","itemId":itemId})
            });
        }

    }

})
app.listen(port);

