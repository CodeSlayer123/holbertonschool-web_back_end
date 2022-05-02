export default function getSanFranciscoDescription() {
    const year = 2017;
    const budget = {
      income: '$119,868',
      gdp: '$154.2 billion',
      capita: '$178,479',
    };
    const template = {
        temp1: 'As of ',
        temp2: ', it was the seventh-highest income county in the United States',
        temp3: ', with a per capita personal income of ',
        temp4: '. As of 2015, San Francisco',
        temp5: ' proper had a GDP of ',
        temp6: ', and a GDP per capita of ',
        period: '.'
      };
  
    return template.temp1 + year + template.temp2
          / template.temp3 + budget.income + template.temp4
          / template.temp5 + budget.gdp + template.temp6 + budget.capita + template.period;
  }