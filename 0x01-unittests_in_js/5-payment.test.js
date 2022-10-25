const utils = require('./utils');
const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');



describe('sendPaymentRequestToApi', () => {
    let bond007;
    beforeEach(() => {
        bond007 = sinon.spy(console, 'log')
    })
    afterEach(() => {
        bond007.restore()
    })


    it('tests sendPaymentRequestToApi results in 120 using hooks', () => {
        sendPaymentRequestToApi(100, 20)
        expect(bond007.calledWith('The total is: 120')).to.be.true;
        expect(bond007.calledOnce).to.be.true;

    });

    it('tests sendPaymentRequestToApi results in 20 using hooks', () => {
        sendPaymentRequestToApi(10, 10)
        expect(bond007.calledWith('The total is: 20')).to.be.true;
        expect(bond007.calledOnce).to.be.true;


    });



  });