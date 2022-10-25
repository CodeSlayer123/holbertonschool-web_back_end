const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
    it('checks positive numbers', () => {
      assert.equal(calculateNumber(1, 3), 4);
      assert.equal(calculateNumber(1, 3.7), 5);
      assert.equal(calculateNumber(1.5, 3.7), 6);

    });
    it('checks negative numbers', () => {
        assert.equal(calculateNumber(-1, -3), -4);
        assert.equal(calculateNumber(-1, -3.7), -5);
        assert.equal(calculateNumber(-1.5, 3.7), 3);
    });
  });