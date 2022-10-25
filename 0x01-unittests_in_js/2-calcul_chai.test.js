const calculateNumber = require('./2-calcul_chai.js');
const expect = require('chai').expect;

describe('calculateNumber', () => {
    it('adds positive numbers', () => {
        expect(calculateNumber('SUM', 1, 3)).to.equal(4);
        expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
        expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);

    });
    it('adds negative numbers', () => {
        expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
        expect(calculateNumber('SUM', -1, -3.7)).to.equal(-5);
        expect(calculateNumber('SUM', -1.5, 3.7)).to.equal(3);
    });
    it('subtracts numbers', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
        expect(calculateNumber('SUBTRACT', -1.4, 4.5)).to.equal(-6);
    });
    it('divides numbers', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        expect(calculateNumber('DIVIDE', -1.4, -4.5)).to.equal(0.25);
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

  });