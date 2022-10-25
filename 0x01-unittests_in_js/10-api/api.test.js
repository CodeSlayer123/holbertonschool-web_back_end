const { expect } = require('chai');
const request = require('request');

describe('app', () => {

    it('tests the GET return', (done) => {
        request('http://localhost:7865/', (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
        })

    });

    it('tests the cart status code with valid id', (done) => {
        request('http://localhost:7865/cart/42', (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 42');
        done();
        })

    });
    it('tests the cart status code with invalid id', (done) => {
        request('http://localhost:7865/cart/the-answer-to-life-the-universe-and-everything', (err, res, body) => {
        expect(res.statusCode).to.equal(404);
        done();
        })

    });

    it('tests the available_payments status code', (done) => {
        request('http://localhost:7865/available_payments', (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal(`{"payment_methods":{"credit_cards":true,"paypal":false}}`);
        done();
        })

    });

    it('tests the login status code', (done) => {
        request({
            method: 'POST',
            url: 'http://localhost:7865/login',
            json: {
                userName: 'PizzaMan42'
            }
        }, (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome PizzaMan42');
        done();
        })

    });

});