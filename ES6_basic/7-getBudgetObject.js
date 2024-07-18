/**
 * A function that returns the object budget in using simply
 * the object property value shorthand syntax.
 * @param {string} income
 * @param {string} gdp
 * @param {string} capita
 * @returns the object budget.
 */
export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income,
    gdp,
    capita,
  };

  return budget;
}
