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

});