const expect = require('chai').expect;
const sinon = require('sinon');
const getPaymentTokenFromAPI = require('./6-payment_token');



describe('getPaymentTokenFromAPI', () => {
    it('tests promise success', (done) => {
        getPaymentTokenFromAPI(true).then((response) => {
            expect(response.data).to.equal('Successful response from the API');
            done();

        })

    });

  });