const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
    it('adds positive numbers', () => {
      assert.equal(calculateNumber('SUM', 1, 3), 4);
      assert.equal(calculateNumber('SUM', 1, 3.7), 5);
      assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
      assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);

    });
    it('adds negative numbers', () => {
        assert.equal(calculateNumber('SUM', -1, -3), -4);
        assert.equal(calculateNumber('SUM', -1, -3.7), -5);
        assert.equal(calculateNumber('SUM', -1.5, 3.7), 3);
    });
    it('subtracts numbers', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.equal(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
        assert.equal(calculateNumber('SUBTRACT', -1.4, 4.5), -6);
    });
    it('divides numbers', () => {
        assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.equal(calculateNumber('DIVIDE', -1.4, -4.5), 0.25);
        assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

  });