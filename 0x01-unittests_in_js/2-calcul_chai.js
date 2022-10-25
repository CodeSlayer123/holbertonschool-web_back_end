function calculateNumber(type, a, b) {
    const types = ['SUM', 'SUBTRACT', 'DIVIDE']

    if (!types.includes(type)){
        throw new TypeError("Type must be be SUM, SUBTRACT, or DIVIDE")
    }
    if (type === types[0]){
        return Math.round(a) + Math.round(b);
    }
    if (type === types[1]){
        return Math.round(a) - Math.round(b);
    }
    if (type === types[2]){
        if (Math.round(b) === 0) {
            return 'Error'
        }
        return Math.round(a) / Math.round(b);
    }
  };

  module.exports = calculateNumber;